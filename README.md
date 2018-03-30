# RutgersGroupProject1

## Authors
Jan Olechowski  
Paul Arias  
Giselle Sena  
Meriedith  Umali  


Issues - Sorted
Limited to 2500 calls on the google API yet had 250,000+ Unique coordinates. 
	- Rounded the coordinates to three decimal places in order to group coordinates together to get zip codes from google API. Grouping these coordinates together allows us to only make 350 calls rather than 250,000. The zipcodes can then be added sorted in the original large dataframe. A change in the thousandths place in the rounded coordinates shifts the location by one block. Still giving us accurate locations. 