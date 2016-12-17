from __future__ import print_function
#in case you wish to use python2, but I strongly prefer that you use python3
import sys
import random

# NAME:RASMI LAMICHHANE
# STUDENT ID NUMBER:101877688
# On my honor as a University of Colorado Boulder student, I have not received any unauthorized help.
# I also realize that plagiarizing code defeats the purpose of an assignment like this and that the
# instructors and TAs have very sophisticated approaches to finding such plagiarism that can defeat
# things like renaming variables or rearranging statements.
#
# Acknowledged By: __ Rasmi Lamichhane __


def free_time_intervals(interval_lst, T):
# First design the algorithm on pen/paper before you attempt this
    my_interval=[]
    interval_lst.sort()# sorts in place
    start=interval_lst[0][0]
    end=interval_lst[0][1]
    for i in range(len(interval_lst)-1):
        if interval_lst[i+1][0]<=end:
            
            if interval_lst[i+1][1]>end:
                end=interval_lst[i+1][1]
        else:
            my_interval.append((start,end))
            start=interval_lst[i+1][0]
            end=interval_lst[i+1][1]
    my_interval.append((start,end))
    print(my_interval,"my interval")
    new_start=0
    new_end=0
    new_interval=[]
    for i in range (len(my_interval)):
        if i == 0:
            new_end=my_interval[i][1]
            if my_interval[i][0]!=0:    
                new_interval.append((new_start,my_interval[i][0]))
                new_end=my_interval[i][1]
        else:
            new_start=my_interval[i-1][1]
            new_end =my_interval[i][0]
            if new_end>T:
                new_end=T
            new_interval.append((new_start,new_end))
            new_end=my_interval[i][1]
    if T>new_end:
        new_interval.append((new_end,T))
    if new_interval[-1][0]>T:
        new_interval.pop()
        print("................................")
    return new_interval

def max_logged_in(interval_lst,T):
    # First design the algorithm on pen/paper and solve a few examples.
    my_interval=[]
    time=interval_lst[0][0]
    for i in interval_lst:
        if i[0]<T:
            my_interval.append((i[0],True))
            if i[1]<T:
                my_interval.append((i[1],False))
        my_interval.sort()
    print(my_interval,"my interval")
    max_logged_in_time=0
    max_logged_in_num=0
    count=0

    for i in range(len(my_interval)):
        if my_interval[i][1]==True:
            count+=1
            if count>max_logged_in_num:
                max_logged_in_num=count
                max_logged_in_time=my_interval[i][0]
        else:
            count-=1


    return max_logged_in_num,max_logged_in_time



if __name__ == '__main__':
    #Test Cases

    lst1 = [(5,15)]
    print('Input:', lst1)
    print(free_time_intervals(lst1,30))
    print(max_logged_in(lst1,30))

    lst2 = [(1,3), (2,8),(3,6), (2,6), (10,15), (12,17), (19,23), (27,35)]
    print('Input:', lst2)
    print(free_time_intervals(lst2,30))
    print(max_logged_in(lst2,30))

    lst3 = [(5,15), (18,25), (3,12), (4, 11), (1,15), (18,19)]
    print('Input:', lst3)
    print(free_time_intervals(lst3,30))
    print(max_logged_in(lst3,30))
