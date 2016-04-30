# 205Final
Gender Gap in SF government employee salaries

I started this project thinking I could help potential SF government employee decide to take a job by providing them a sort of living standard that comes with their salaries. (Proposal powerpoint -Should you work as a SF government Employee.ppt) I realized that  most of the employees did not have enough salary to be able to afford housing within SF city and getting data for the suburban neighborhood would be out of scope of this project. Also, I found interesting analysis done on kaggle which talked about looking at patterns using the gender of the employees available. It led me to create a python script (cleanSFCsalaries.php) that cleans the data, use sexmachine package to determine the gender of an employee based on their names. The issue with that is I had to drop some records for which the package could not determine the gender. I used the title to determine their career track, grade level and associated department. I used this new formatted data, and uploaded in hive.

I used tableau to connect and look for some patterns. I came up with a data visualization that I implemented in d3, and is hosted at

 http://people.ischool.berkeley.edu/~sahab/w209final/
 
My future plan is to get more datasets for other major cities, and run similar scripts in them. I would use pyspark for cleaning because sex macine took a whole day in EC2 server. I will use SPARK for data aggregation once the data set is huge, and create a serving layer for users of my website, where they can pick and chose what factors and cities they want to compare. I will also apply machine learning to predict the pay based on job title, department and city (summer project). I will also do sampling of outiers to find wrongly associated department, career track and grade levels.
