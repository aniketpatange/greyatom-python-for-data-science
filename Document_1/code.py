# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=',',skip_header=1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census=np.concatenate([data,new_record])
print(census)
#Code starts here



# --------------
#Code starts here
age=census[:,0]
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=age.std()

print(age_mean)
print(age_std)


# --------------
#Code starts here
import numpy as np
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
list_1=[len_0,len_1,len_2,len_3,len_4]
print(list_1)
min_f=min(list_1)
minority_race=list_1.index(min_f)
print(minority_race)


# --------------
#Code starts here
import numpy as np
senior_citizens=census[census[:,0]>60]
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)
avg_working_hours=(working_hours_sum)/(senior_citizens_len)
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=np.mean(high,axis=0)[7]
avg_pay_low=np.mean(low,axis=0)[7]
np.array_equal


