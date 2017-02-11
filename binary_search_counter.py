#!/usr/bin/env python3
''' A counter to show how many steps it takes
to find a number using binary search
TODO: No reason to make numbers random.
'''
import random
import math

def bin_search_counter():
    my_list = []
    print('*' * 20)
    print("This is a quick and dirty program to show the efficiency of binary search.")
    print("I'll ask you for a number (an integer) for the size of the list to search.")
    print("Then the target number for searching will be randomly selected.")
    list_size = int(input("How big of a list do you want to search through?\n> "))
    if list_size > 1e6:
        print("OK, but this might take a while.")
    search_list = [n for n in range(1, list_size)]
    target = search_list[random.randrange(len(search_list) - 1)]
    low = 0
    high = len(search_list) - 1
    counter = 0
    while low <= high:
        mid = (low + high) // 2
        guess = search_list[mid]
        if guess == target:
            break
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
        counter += 1
    print('*' * 20)
    print("The list had %s numbers in it" % str(len(search_list)))
    print("The number to look up was: %s" % str(target))
    print("Binary search found the item in %s tries." % counter)
    print("Big O notation for binary search is log(n), so this search is O(log %s)" % str(len(search_list)))
    big_O = math.log(len(search_list), 2)
    print("Calculating that logarithm would show an expected %s number of tries to get to the target number." % big_O)

if __name__ == '__main__':
    bin_search_counter()