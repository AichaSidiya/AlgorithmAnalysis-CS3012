#function that returns maximum number of non overlapping intervals
def nonOverlappingInterval(arr):
    end = float('-inf')
    
    nonOverlappingInterval = 0

    #sort the list of time intervals according to their end time
    arr.sort(key = lambda x: x[1])

    #loop through the sorted time intervals 
    for subList in arr:
        
        #if the begin time of the current interval is greater or equal then the highest end time recorded till now
        if subList[0] >= end: 
            
            #increment the number of non-overlapping intervals
            nonOverlappingInterval += 1
            #update the max end time to the end time of the current interval
            end = subList[1]
         
    #return the maximum number of non overlapping intervals
    return nonOverlappingInterval 

#program driver main function 
def main():
    print('***********************\tWelcome to your Interval scheduling program\t*********************')
    
    #inpyt file name from user
    filename = input('\nPlease enter the name of your input file: ') + '.txt'
    print()
    #loop through file and store all elements as a list of sublist of intervals with begin and end time
    try:
        with open(filename, 'r') as file:
            timeList = [list(map(int, line.strip().split(','))) for line in file]
            print("Current number of time intervals: ", len(timeList)) #print the original number of intervals
            print()
        print("The maximum number of non overlapping intervals is: ", nonOverlappingInterval(timeList)) #print the non overlapping time intervals
    except FileNotFoundError:
        msg = "Sorry, the file "+ filename + " does not exist."
        print(msg)     

#this function call the main and repeat it as long as answer=yes
def repeat():

    print('\nDo you want to fix a schedule? ')
    answer = input('y or Y: ')

    while answer == 'y' or answer == 'Y':

        main()

        print('\nDo you want to fix another schedule? ')
        answer = input('y or Y: ')

    if answer != 'y' or answer != 'Y':

        print('\n*********************\tThank you, bye\t**************************\n')

repeat()
