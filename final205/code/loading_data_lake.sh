cd data
lynx https://www.kaggle.com/kaggle/sf-salaries/downloads/sf-salaries-release-2015-12-21-03-21-32.zip 

unzip sf-salaries-release-2015-12-21-03-21-32.zip

python CleanSFSalaries.py
tail -n +2 "/output/Salaries.csv" > salaries.csv 
tail -n +2 "SFC.csv" > SFC.csv 
/root/start-hadoop.sh
/data/start_postgres.sh
su	- w205

hdfs dfs -mkdir /user/w205/final
hdfs dfs -mkdir /user/w205/final/salary
hdfs dfs -mkdir /user/w205/final/sfcModified
hdfs dfs -put salaries.csv /user/w205/final/salary
hdfs dfs -put SFC.csv /user/w205/final/sfcModified