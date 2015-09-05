
# coding: utf-8

# In[1]:

import random
import csv


# In[2]:

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


# In[3]:

# Calculate how many times are available to each person
# Because this interview matchin program algorithm is designed to 
# assign the interview time for least avialable time first. And lean on some randomness

total_num = len(int_list) # The number of applicant
tmp_num = [] # Each persons number of possible time 

for it in int_list:
    tmp = []
    tmp.append(len(it[1]))
    tmp_num.append(len(it[1]))


# In[4]:

# Match each interview time since the person who has the least number of possible time.

int_result   = []
allocate_num = []

for it in range(len(int_list)):
    
    tmp = []
    index_tmp = tmp_num.index(min(tmp_num))
    order_tmp = int_list[index_tmp][1]
    
    ran_index = random.randint(1,len(order_tmp))
    
    for it2 in allocate_num:
        try:
            index_tmp2 = order_tmp.index(it2)
            del(order_tmp[index_tmp2])
        except:
            continue

    ran_index = random.randint(1,len(order_tmp))            
    tmp.append(int_list[index_tmp][0])
    tmp.append(order_tmp[ran_index-1])
                
    int_result.append(tmp)
    
    if(not order_tmp[ran_index-1] in allocate_num):
        allocate_num.append(order_tmp[ran_index-1])

    tmp_num[index_tmp] += total_num*10 # This number has to be bigger than total number of people

avail_time = [] # Available times of applicant 

for time in int_result:
    avail_time.append(time[1])


# In[6]:

# Write down the result of matched interview time.

csv_name = 'Interview_result.csv'
csv_file = open(csv_name,'w')
cw = csv.writer(csv_file , delimiter=',')
cw.writerow(['Time','Name'])

for time in fieldname[1:]:
    for it in range(len(int_result)):
        if (not time in avail_time):
            cw.writerow([time,'No one'])
            break

        if (int_result[it][1] == time):
            cw.writerow([time,int_result[it][0]])

