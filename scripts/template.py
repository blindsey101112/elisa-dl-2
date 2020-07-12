html = """
 <html>
 <body>

 <style>
 .centre {
     text-align: center;
 }

 table {
   font-family: arial, sans-serif;
   border-collapse: collapse;
   margin-left:auto;margin-right:auto;
 }

 td, th {
   border: 1px solid #dddddd;
   text-align: left;
   padding: 8px;
 }

 tr:nth-child(1) {
   background-color: #dddddd;
 }
 </style>

 <h1 style="font-size:24px"> Plate Report - %s</h1>

 <p style="font-size:16px"> Report generated on %s<p>
 <p style="font-size:16px"> <b>Antigen:</b> %s</p>

 <p style="font-size:12px"> <b>OD cutoff</b> %s</p>   
 <p style="font-size:12px"> <b>Blanks</b>  mean: %s   CV: %s</p>
 <p style="font-size:12px"> <b>Positive control </b>  mean: %s   CV: %s</p>
 <p style="font-size:12px"> <b>Negative control</b>  mean: %s   CV: %s</p>

 <p style="font-size:12px"> <b>Exclusions</b>  %s</p>

<font size="2">
 <table>
   <tr>
     <th>S</th>
     <th>SampleID</th>
     <th>Dilution</th>
     <th>CV</th>
     <th>QC</th>
     <th>Comments</th>
   </tr>
   <tr>
     <td>01</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
	 <td>%s</td>
	 <td>%s</td>
   </tr>
   <tr>
     <td>02</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
	 <td>%s</td>
	 <td>%s</td>
   </tr>
   <tr>
     <td>03</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
	 <td>%s</td>
	 <td>%s</td>
   </tr>
   <tr>
     <td>04</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
	 <td>%s</td>
	 <td>%s</td>
   </tr>      
   <tr>
     <td>05</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
	 <td>%s</td>
	 <td>%s</td>
   </tr>      
   <tr>
     <td>06</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
	 <td>%s</td>
	 <td>%s</td>
   </tr>
     <td>07</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
	 <td>%s</td>
	 <td>%s</td>

 </table>
 </font>

 </body>
 </html>

 """