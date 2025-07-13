import random, time

class Sort:
    def __init__(self, thelist):
        self.thelist = thelist.copy()

    def sort(self):
        pass
    
class BubbleSorter(Sort):
    def sort(self):
        #do bubble sort stuff
        for i in range(len(self.thelist) - 1):
            x = False #init a swap func to track swaps

            for j in range(len(self.thelist) - i - 1):
                if self.thelist[j] > self.thelist[j+1]:
                    self.thelist[j], self.thelist[j+1] = self.thelist[j+1], self.thelist[j]
                    x = True
            if not x:
                break

        return self.thelist


class MergeSorter(Sort):
    
    def __init__(self, thelist):
        self.thelist = thelist.copy()
        
    def sort(self):
        self.thelist = self.merge_sort(self.thelist)
        return self.thelist
    
    def merge_sort(self, sort):
    # If the list has 1 or less items then skip as the list is already sorted.
        if len(sort) <= 1:
            return sort
        
        # Split the array in half
        Marr = len(sort)//2
        Larr = sort[:Marr]
        Rarr = sort[Marr:]
        
        Larr = self.merge_sort(Larr)
        Rarr = self.merge_sort(Rarr)
        # Recursively sort both halves then
        # merge the sorted halves together
        return self.merge(Larr, Rarr)

    def merge(self, Larr, Rarr):
        result = []
        ## for every two lists in tempList, merge the
        ## through comparing and appending them depening
        ## on which ones are larger
        while Larr and Rarr:
        # While the left and right array are true,
        # It continues as long as both arrays have elements remaining.
            if Larr[0] < Rarr[0] or None:
                result.append(Larr[0])
                Larr.pop(0)
            else: 
                result.append(Rarr[0])
                Rarr.pop(0)
        if Larr:
            result += Larr
        if Rarr:
            result += Rarr
            
        return result
            # if the arrays still contain values, it apends them onto
            # the end to prevent data loss and cleans up the arrays.
            # this (most likey) wont unsort the result for the fact
            # of the remaining values would be the largest data in the
            # set, so adding them on the end wouldn't ruin the order.
            
class InsertionSort(Sort):
    def __init__(self, thelist):
        self.thelist = thelist.copy()

    def sort(self):
        for i in range(1, len(self.thelist)):
            x = i - 1
            y = self.thelist[i] 
            while self.thelist[x] > y and x+1 >= 1:
                self.thelist[x], self.thelist[x+1] = self.thelist[x+1], self.thelist[x]
                x -= 1 
            self.thelist[x+1] = y
        return self.thelist       
            

class BogoSort(Sort):
    def __init__(self, thelist):
        self.thelist = thelist.copy()

    def sort(self):
        start = time.time()
        randomisations = 0
        c = range(len(self.thelist) - 1)
        x = self.thelist
        while not all(x[i]<=x[i+1] for i in c):
            random.shuffle(self.thelist)
            randomisations += 1
            print(randomisations)
        end = time.time()
        timeTaken = end - start
        print(f"Attemps: {randomisations}, time taken: {timeTaken}")
        return self.thelist


class quicksort(Sort):
   def __init__(self, thelist):
       self.thelist = thelist.copy()
       print("not ready yet sorry")
       