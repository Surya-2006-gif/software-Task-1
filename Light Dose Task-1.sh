#!/bin/bash 

#making a new subdirectory from home directory
mkdir ~/rover_mission

#navigating into that directory
cd rover_mission 

#creating three text files inside it
touch log1.txt log2.txt log3.txt


#renaming one of the text file
mv log1.txt 'mission_log.txt'


#Finding all files with extension .log
find . -type f -name  "*.log"

#showing the contents of the textfile in a expanded manner
cat mission_log.txt


#printing the line containing the word error
grep -n "ERROR" mission_log.txt >  nums.txt
awk -F : '{print $1}' nums.txt > nums2.txt
for i in $(cat nums2.txt)
do
  sed -n '${i}p' mission_log.txt

done



#getting the no of lines in the text file

wc -l mission_log.txt

#displaying the date and time
echo $(date)


#displaying the cpu
#press ctrl + c to close
mpstat  -P ALL 1

#scheduling shutdown in 10 minutes

shutdown -h +10