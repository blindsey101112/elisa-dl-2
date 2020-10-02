import os
import sys
import shutil
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import pdfkit
import datetime

def mean_cv(group):
    """returns mean and cv of a group of wells"""
    group_ods = np.asarray(list(ods[group].values()))
    group_mean = sum(group_ods) / len(group_ods)
    group_sd = np.std(group_ods)
    group_cv = group_sd / group_mean
    return [group_mean, group_cv]

antigens = {"s" : "Spike", "n" : "Nucleocapsid", "n2": "Nucleocapsid2"}

cut_offs = {"s" : 0.175, "n" : 0.722, "n2": 0.1905}

if __name__ == "__main__":
    sys.path.insert(1, './scripts')
    from template import html
    from plate_plans import get_ods, get_samples
    plate_id = sys.argv[1]
    antigen = sys.argv[2]

    #read in input files
    plateplan_file = plate_id + "-pplan.xlsx"
    platereader_file = plate_id + "-preader.xlsx"
    ignore_file = plate_id + "-ignore.csv"
    ods = get_ods(platereader_file) #retutns python dictionary with ods from plate
    sample_dilution = get_samples(plateplan_file) #returns python dictionary with samples names and dilutions

    print("Found plateplan file: %s" % plateplan_file)
    print("Found plate reader file: %s" % platereader_file)
    if ignore_file in os.listdir():
        print("Found ignore file: %s" % ignore_file)
    print("Antigen: %s" % antigens[antigen])

    np.set_printoptions(suppress=True) #suppresses scientific display of numbers

### read bad wells from ignore file ###
    badwells = []
    badwells_group = []
    if ignore_file in os.listdir():
        with open(ignore_file) as infile:
            for line in infile:
                badwell = line.split(",")[0]
                group = line.split(",")[1].replace("\n", "")
                badwells.append(badwell)
                badwells_group.append(group)

### get list of sample ids
    sample_ids = {}
    for num in range(1,8):
        sample_num = "sample0%s" % str(num)
        inputed_ids = []
        for dilution in sample_dilution[sample_num].values():
            if dilution.split("-")[0] not in inputed_ids:
                inputed_ids.append(dilution.split("-")[0])
        if len(inputed_ids) != 1:
            print("Inputting error with sampleID: %s %s" % (sample_num, inputed_ids))
        sample_ids[sample_num] = inputed_ids[0]

### calculate CVs, subtract blanks from ODs and calculate mean for samples
    cvs = {}
    dilution_ods = {}
    blk_mean = mean_cv("blk")[0]
    blk_cv = mean_cv("blk")[1]
    for group in list(ods.keys()):
        if "sample" in group:
            if "_1" in group:
                for well in ods[group].keys():
                    column = int(well[1:4])
                    row = well[0:1]
                    duplicates = [well, row + str(column+1)]
                    duplicate_ods = []
                    sample_no = group[0:8]
                    id = sample_dilution[sample_no][well].split("-")[0]
                    dilution = sample_dilution[group[0:8]][well].split("-")[1]
                    for duplicate in duplicates:
                        if duplicates.index(duplicate) == 0:
                            duplicate_ods.append(ods[sample_no + "_1"][duplicate])
                        if duplicates.index(duplicate) == 1:
                            duplicate_ods.append(ods[sample_no + "_2"][duplicate])
                        if duplicate in badwells:
                            bad_duplicate = duplicates.index(duplicate)
                            del duplicate_ods[bad_duplicate]
                            duplicates.remove(duplicate)
                        np_ods = np.asarray(duplicate_ods)
                        duplicate_mean = sum(np_ods) / len(np_ods)
                        duplicate_sd = np.std(np_ods)
                        duplicate_cv = duplicate_sd / duplicate_mean
                    if id not in cvs.keys():
                        cvs[id] = {}
                    cvs[id][dilution] = round(duplicate_cv, 3)
                    for duplicate in duplicate_ods:
                        index = duplicate_ods.index(duplicate)
                        duplicate_ods[index] = duplicate - blk_mean
                    if id not in dilution_ods.keys():
                        dilution_ods[id] = {}
                    np_ods_blk = np.asarray(duplicate_ods)
                    duplicate_blk_mean = sum(np_ods_blk) / len(np_ods_blk)
                    dilution_ods[id][dilution] = duplicate_blk_mean
            if "_2" in group:
                continue
        else:
            for well in list(ods[group].keys()):
                if well in badwells:
                    del ods[group][well]
            group_cv = mean_cv(group)[1]
            cvs[group] = round(group_cv, 3)

### qc check and determine endpoint dilution
    endpoint_dilution = {}
    endpoint_error = {}
    high_low = {}
    for sample in sample_ids:
        sample_cvs = cvs[sample_ids[sample]]
        sample_ods = dilution_ods[sample_ids[sample]]
        cut_off = cut_offs[antigen]
        endpoint = 0
        for dilution in sample_ods:
            if sample_ods[dilution] > cut_off:
                if int(dilution) > endpoint:
                    endpoint = int(dilution)
        endpoint_dilution[sample] = endpoint
        dilutions = list(sample_cvs.keys())
        dilutions = sorted([int(i) for i in dilutions])
        if endpoint != 0:
            dilution_num = dilutions.index(endpoint)
        else:
            dilution_num = "NA"
            endpoint_dilution[sample] = "NA"

        ## errors
        cv_high = 0
        high_low[sample] = ""
        for cv in sample_cvs.values():
            if cv >= 0.1:
                cv_high += 1
        if cv_high >= 2:
            endpoint_error[sample] = "Too many high CVs"
            continue
        if dilution_num == "NA":
            endpoint_error[sample] = "Endpoint below titration"
            cvs[sample_ids[sample]]["NA"] = "NA"
            continue
        if cvs[sample_ids[sample]][str(endpoint)] > 0.1:
            endpoint_error[sample] = "Endpoint high CV"
            continue
        if cvs[sample_ids[sample]][str(dilutions[dilution_num-1])] > 0.1:
                if cvs[sample_ids[sample]][str(dilutions[dilution_num + 1])] > 0.1:
                    endpoint_error[sample] = "Dilution below and/or above high CV"
                else:
                    endpoint_error[sample] = "PASS"
                continue
        if dilution_num == 0:
            if cvs[sample_ids[sample]][str(dilutions[1])] > 0.1:
                endpoint_error[sample] = "Dilution above high CV"
                high_low[sample] = "Lowest dilution"
                continue
        if dilution_num == len(dilutions) - 1:
            high_low[sample] = "Highest dilution"
            if cvs[sample_ids[sample]][str(dilutions[dilution_num -1])] > 0.1:
                endpoint_error[sample] = "Dilution below high CV"
                continue
        endpoint_error[sample] = "PASS"

### determine conditional output text ###
    ignore_wells = dict(zip(badwells, badwells_group))
    if len(badwells) == 0:
        ignore_text = "No wells exlcuded"
    else:
        ignore_text = "excluded these wells: %s" % ignore_wells

### Output to pdf file ###
    print("Generating html file")
    now = datetime.datetime.now()
    date = "%s-%s-%s" % (now.day, now.strftime("%b"), now.year)

    html_page = html % (plate_id,
                            date,
                            antigens[antigen],
                            str(cut_offs[antigen]),
                            round(blk_mean, 3),
                            round(blk_cv, 3),

                            round(mean_cv("pos")[0], 3),
                            round(mean_cv("pos")[1], 3),

                            round(mean_cv("neg")[0], 3),
                            round(mean_cv("neg")[1], 3),

                            ignore_text,

                            sample_ids["sample01"],
                                endpoint_dilution["sample01"],
                                cvs[sample_ids["sample01"]][str(endpoint_dilution["sample01"])],
                                endpoint_error["sample01"],
                                high_low["sample01"],

                            sample_ids["sample02"],
                                endpoint_dilution["sample02"],
                                cvs[sample_ids["sample02"]][str(endpoint_dilution["sample02"])],
                                endpoint_error["sample02"],
                                high_low["sample02"],

                            sample_ids["sample03"],
                                endpoint_dilution["sample03"],
                                cvs[sample_ids["sample03"]][str(endpoint_dilution["sample03"])],
                                endpoint_error["sample03"],
                                high_low["sample03"],

                            sample_ids["sample04"],
                                endpoint_dilution["sample04"],
                                cvs[sample_ids["sample04"]][str(endpoint_dilution["sample04"])],
                                endpoint_error["sample04"],
                                high_low["sample04"],

                            sample_ids["sample05"],
                                endpoint_dilution["sample05"],
                                cvs[sample_ids["sample05"]][str(endpoint_dilution["sample05"])],
                                endpoint_error["sample05"],
                                high_low["sample05"],

                            sample_ids["sample06"],
                                endpoint_dilution["sample06"],
                                cvs[sample_ids["sample06"]][str(endpoint_dilution["sample06"])],
                                endpoint_error["sample06"],
                                high_low["sample06"],

                            sample_ids["sample07"],
                                endpoint_dilution["sample07"],
                                cvs[sample_ids["sample07"]][str(endpoint_dilution["sample07"])],
                                endpoint_error["sample07"],
                                high_low["sample07"]

                            )

    html_file = plate_id + ".html"
    pdf_file = plate_id + ".pdf"

    with open(plate_id + ".html", 'w') as htmlfile:
        htmlfile.write(html_page)

    print("Converting html to pdf...")
    pdfkit.from_file(html_file, pdf_file)

    shutil.move(html_file, os.path.join("html_reports", html_file))

### Output to csv ###
    print("Creating csv file")
    csv_file = plate_id + ".csv"

    with open(csv_file, "w") as csvfile:
        csvfile.write("sampleid, dilution, od, cv, qc, comments\n")
        for sample in sample_ids.keys():
           if endpoint_dilution[sample] == "NA":
                csvfile.write(sample_ids[sample]
                          + ", NA"
                          + ", NA"
                          + ", NA"
                          + ", " + endpoint_error[sample]
                          + ", " +  high_low[sample] + "\n")
           else:
                csvfile.write(sample_ids[sample]
                          + ", " + str(endpoint_dilution[sample])
                          + ", " + str(dilution_ods[sample_ids[sample]][str(endpoint_dilution[sample])])
                          + ", " + str(cvs[sample_ids[sample]][str(endpoint_dilution[sample])])
                          + ", " + endpoint_error[sample]
                          + ", " +  high_low[sample] + "\n")
