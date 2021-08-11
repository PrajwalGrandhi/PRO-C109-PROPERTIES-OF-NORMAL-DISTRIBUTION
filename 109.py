import pandas as pd
import statistics

df=pd.read_csv("stpe.csv")

list=df["math score"].to_list()


mean=sum(list)/len(list)
median=statistics.median(list)
mode=statistics.mode(list)

print("mean median mode: ",mean,median,mode)

std=statistics.stdev(list)

std1_start,std1_end=mean-std,mean+std
std2_start,std2_end=mean-(2*std),mean+(2*std)
std3_start,std3_end=mean-(3*std),mean+(3*std)

std1_data=[result for result in list if result>std1_start and result<std1_end]
std2_data=[result for result in list if result>std2_start and result<std2_end]
std3_data=[result for result in list if result>std3_start and result<std3_end]

print("{}% of data lies in 1st Standard Deviation".format(len(std1_data)/len(list)*100.0))
print("{}% of data lies in 2st Standard Deviation".format(len(std2_data)/len(list)*100.0))
print("{}% of data lies in 3st Standard Deviation".format(len(std3_data)/len(list)*100.0))
