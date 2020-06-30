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

 <p class="centre"><img src="%s" alt="Standard curve" width="450" height="350"/></p>

 <p style="font-size:12px"> <b>OD cutoff</b> %s</p>   
 <p style="font-size:12px"> <b>Blanks</b>  mean: %s   CV: %s</p>
 <p style="font-size:12px"> <b>Positive control </b>  mean: %s   CV: %s</p>
 <p style="font-size:12px"> <b>Negative control</b>  mean: %s   CV: %s</p>
 <p style="font-size:12px"> <b>Standards</b>  %s</p>
 <p style="font-size:12px"> <b>Exclusions</b>  %s</p>

<font size="2">
 <table>
   <tr>
     <th>S</th>
     <th>SampleID</th>
     <th>OD</th>
     <th>CV</th>
     <th>Ab-Units</th>
     <th>Result</th>
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
   </tr>
   <tr>
     <td>08</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
   </tr>
   <tr>
     <td>09</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
   </tr>
   <tr>
     <td>10</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
   </tr>      
   <tr>
     <td>11</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
   </tr>      
   <tr>
     <td>12</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>  
     <td>%s</td>      
   </tr>
   <tr>
     <td>13</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
   </tr>      
   <tr>
     <td>14</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
   </tr>      
   <tr>
     <td>15</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>      
     <td>%s</td>  
   </tr>
   <tr>
     <td>16</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td> 
     <td>%s</td>       
   </tr>      
   <tr>
     <td>17</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
   </tr>      
   <tr>
     <td>18</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>        
   </tr>
   <tr>
     <td>19</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>   
     <td>%s</td>     
   </tr>          
   <tr>
     <td>20</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td> 
     <td>%s</td>       
   </tr>
   <tr>
     <td>21</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>    
     <td>%s</td>    
   </tr>          
   <tr>
     <td>22</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>    
     <td>%s</td>    
   </tr>        
   <tr>
     <td>23</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>   
     <td>%s</td>     
   </tr>  
   <tr>
     <td>24</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>        
     <td>%s</td>
   </tr>  
   <tr>
     <td>25</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>        
     <td>%s</td>
   </tr>  
   <tr>
     <td>26</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td> 
     <td>%s</td>       
   </tr>  
   <tr>
     <td>27</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td> 
     <td>%s</td>       
   </tr>  
   <tr>
     <td>28</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>        
     <td>%s</td>
   </tr>  
   <tr>
     <td>29</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>        
     <td>%s</td>
   </tr>  
   <tr>
     <td>30</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>  
     <td>%s</td>      
   </tr>  
   <tr>
     <td>31</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>        
     <td>%s</td>
   </tr>  
   <tr>
     <td>32</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>
     <td>%s</td>        
     <td>%s</td>
   </tr>  

 </table>
 </font>

 </body>
 </html>

 """