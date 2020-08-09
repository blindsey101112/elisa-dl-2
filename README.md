# elisa-do-little-2

### Requirements

This should run off linux, mac and windows but I have only tested it in windows subsytem for linux.

1. Some version of conda, I recommend Miniconda3. Can be downloaded from [here](https://docs.conda.io/en/latest/miniconda.html)
2. A plate plan excel file named "*plateID*-pplan.xlsx". See 'template-pplan.xlsx' as an example.
3. A plate reader file saved in ".xlsx" format named "*plateID*-preader.xlsx" . Our plate reader will generate an ".xls" file which will not work so you need to make this change manually with 'save as'
3. A plate ignore file if you want to exlude certain wells from the plate

### Install elisa-dl 

1. Clone this repository and ``cd elisa-dl-2``
2. ``conda env create -f environment.yml``

If you get an error message related to wkhtmltopdf then:
1. Download it manually from [here](https://wkhtmltopdf.org/downloads.html)
2. Open the environment.yml file with any text editor. I recommend [notepad++](https://notepad-plus-plus.org/downloads/v7.8.6/).
3. Delete the line '- wkhtmltopdf=0.12.3' and save the file.
4. Retry ``conda env create -f environment.yml``


### Running elisa-dl

1. For now you have to be with in the elisa-dl directory
2. ``conda activate elisa-dl``
3. ``python elisa_dl.py plateID antigen`` In place of 'antigen' type "s" or "n" for Spike or Nucleoprotein
5. You can do a test run with ``python elisa_dl-2.py test`` 
6. Onced finished ``conda deactivate`` to exit the environment

### Output
This should automatically generate a report named *plateID*.pdf to inspect the standard curve and see the sample concentrations.

### Important considerations
Re-running the script with the same plateID will overwrite any previously generated files in the elisa-dl directory with the same filename. So if you have modified the input files in someway and want to generate a second report move the report to another directory before running the script.
