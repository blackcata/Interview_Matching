#!/usr/local/bin/python3
# coding: utf-8

# In[8]:

#----------------------------------------------------------!
#
# This program has been created to matching interviewee to
# each available time. 
# It can allocate multi people to each time and it is
# controlled by the 'key_num'
#
# You need random,csvlibrary
#
# Kyung Min Noh, 2015
#
#----------------------------------------------------------!

import random
import csv
import sys

# In[9]:

# Reading the each person's available time which is in 'Interview_apply.csv' file.

with open('Interview_apply.csv') as csvfile:
    reader    = csv.DictReader(csvfile) # All data of csv file
    fieldname = reader.fieldnames # Category names
    
    int_list = [] # This list will consist of dual list structure
    
    for row in reader:
        tmp = []
        tmp.append(row[fieldname[0]]) # Append the name of applicant
        tmp2 = []
        
        for it in fieldname[1:]:
            if(int(row[it]) == 1):
                tmp2.append(it)
                
        tmp.append(tmp2) # Append the available time of applicant 
        int_list.append(tmp) # Append applicants information
    
csvfile.close()


# In[10]:

# Making the Time_available list 
key_num   = int(sys.argv[1])  # The number of people which can be allocated to each time 
time_list = fieldname[1:]

time_avail_list = []
for it in range(len(time_list)):
    tmp = []
    tmp.append(time_list[it])
    tmp.append(key_num)
    
    time_avail_list.append(tmp)


# In[11]:

# Calculate how many times are available to each person
# Because this interview matchin program algorithm is designed to 
# assign the interview time for least avialable time first. And lean on some randomness

total_num = len(int_list) # The number of applicant
tmp_num = [] # Each persons number of possible time 

for it in int_list:
    tmp = []
    tmp.append(len(it[1]))
    tmp_num.append(len(it[1]))


# In[12]:

# Match each interview time since the person who has the least number of possible time.

int_result   = []

for it in range(len(int_list)):
    
    tmp = []
    index_tmp = tmp_num.index(min(tmp_num))
    order_tmp = int_list[index_tmp][1]

    for it3 in order_tmp:
        avail_tmp = []
        avail_tmp.append(it3)
        avail_tmp.append(0)
        
        if (avail_tmp in time_avail_list):
            index_tmp3 = order_tmp.index(it3)
            del(order_tmp[index_tmp3])

    ran_index = random.randint(1,len(order_tmp))            
    tmp.append(int_list[index_tmp][0])
    tmp.append(order_tmp[ran_index-1])
    
    index_tmp4 = time_list.index(order_tmp[ran_index-1])
    time_avail_list[index_tmp4][1] -= 1
    
    int_result.append(tmp)

    tmp_num[index_tmp] += total_num*10 # This number has to be bigger than total number of people
    
avail_time = [] # Available times of applicant 

for time in int_result:
    avail_time.append(time[1])


# In[16]:

# Write down the result of matched interview time.

csv_name = 'Interview_result.csv'
csv_file = open(csv_name,'w')

cw = csv.writer(csv_file)

category = []
category.append('Time')

for it in range(1,key_num+1):
    category.append('Name'+str(it))
    
cw.writerow(category)

time_allocate = []

for time in fieldname[1:]:
    tmp = []
    tmp.append(time)
    for it in range(len(int_result)):
        if (not time in avail_time):
            tmp.append('No one')
            break

        if (int_result[it][1] == time):
            tmp.append(int_result[it][0])
    time_allocate.append(tmp)
    
for it in time_allocate:
    cw.writerow(it)

