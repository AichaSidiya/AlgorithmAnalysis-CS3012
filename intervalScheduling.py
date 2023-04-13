#!/usr/bin/env python
# coding: utf-8

# In[8]:


#function that returns non overlapping intervals
def nonOverlappingInterval(arr):
    end = float('-inf')
    
    nonOverlappingInterval = []
    
    #loop through the sorted time intervals that are sorted according to their end time
    for subList in sorted(arr, key=lambda x: x[1]):
        
        #if the begin time of the current interval is greater or equal then the highest end time recorded till now
        if subList[0] >= end: 
            
            #append this interval to the list of non-overlapping intervals
            nonOverlappingInterval.append(subList)
            #update the max end time to the end time of the current interval
            end = subList[1]
         
    #return the list of non overlapping intervals
    return nonOverlappingInterval 


# In[9]:


#program driver main function 
def main():
    print('***********************\tWelcome to your Interval scheduling program\t*********************')
    
    #inpyt file name from user
    filename = input('\nPlease enter the name of your input file: ') + '.txt'
    print()
    #loop through file and store all elements as a list of sublist of intervals with begin and end time
    with open(filename, 'r') as file:
        timeList = [list(map(int, line.strip().split(','))) for line in file]
        print("Time list: ",timeList) #print the original list
        print()
    print("Non overlapping time list: ", nonOverlappingInterval(timeList)) #print the non overlapping time intervals
        
main()


# In[ ]:




