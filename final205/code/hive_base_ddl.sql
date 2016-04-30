

DROP TABLE salaries;

CREATE EXTERNAL TABLE salaries (Id STRING, name STRING, title STRING, basePay STRING, overTime STRING, otherPay STRING, benefits STRING, totalPay STRING, year STRING, notes STRING, agency STRING, status STRING) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES (  "separatorChar" = ",", "quoteChar" = '"',  "escapeChar" = '\\' ) STORED AS TEXTFILE LOCATION '/user/w205/final/salaries';

create table salary as select Id, lower(name), lower(title) as title, int(basePay), int(overTime), int(otherPay), int(benefits), int(totalPay), year, status
from salaries

DROP TABLE sfcModified;

CREATE EXTERNAL TABLE sfcModified (EmployeeName STRING, JobTitle STRING, BasePay STRING, OverTime STRING, OtherPay STRING, Benefits STRING, TotalPay STRING, Year STRING,  Status STRING, Gender STRING, title string, grade string, dept string) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES (  "separatorChar" = ",", "quoteChar" = '"',  "escapeChar" = '\\' ) STORED AS TEXTFILE LOCATION '/user/w205/final/sfcModified';