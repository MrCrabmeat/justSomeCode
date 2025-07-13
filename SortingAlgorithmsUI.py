from os import system, name
from SortingAlgorithms import *

# Clearing the Screen
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
thelist =[]
temp = False
class initalEntry():
    def __init__(self):
        self.thelist = []
        self.Avaliable_sorting_options = []
        self.sortingChoice = int()
    
    def DataInput(self):
        temp = False
        while temp == False:
            x = input("what value do you want to add: ")
            if not x: temp = True
            try:
                x = int(x)
                thelist.append(int(x))
                clear()
            except ValueError: 
                print("please enter a valid number")
        self.SortAvaliablity()
        self.SortChoice() 
        self.ForwardSelections()

    
    def SortChoice(self):
        try: 
            print("How do you want to sort your data?")
            x = int(input())
            if 0 <= x < len(self.Avaliable_sorting_options)+1:
                self.sortingChoice = x    
            else:
                print("please input an interger within range")
                return None
        except ValueError:
            print("please enter a valid number")
            return None
        
        
   
    def SortAvaliablity(self): 
        i = 1; self.Avaliable_sorting_options = []
        if BubbleSorter:
            print(f"{i}. BubbleSort"); i += 1
            self.Avaliable_sorting_options.append("BS")
        if MergeSorter:
            print(f"{i}. MergeSort"); i += 1
            self.Avaliable_sorting_options.append("MS")
        if InsertionSort:
            print(f"{i}. InsertionSort" ); i += 1
            self.Avaliable_sorting_options.append("IS")
        if BogoSort:
            print(f"{i}. BogoSort" ); i += 1
            self.Avaliable_sorting_options.append("BoS")
        if quicksort:
            print(f"{i}. QuickSort"); i += 1
            self.Avaliable_sorting_options.append("QS")
        
        if len(self.Avaliable_sorting_options) >= 0:
            return 0
        else:
            return
        
    def ForwardSelections(self):
        match self.Avaliable_sorting_options[self.sortingChoice - 1]:
            case "BS":
                mysort = BubbleSorter(thelist)
            case "MS":
                mysort = MergeSorter(thelist)
            case "IS":
                mysort = InsertionSort(thelist)
            case "BoS":
                mysort = BogoSort(thelist)
            case "QS":
                mysort = quicksort(thelist)

        clear()
        mysortedlist = mysort.sort()
        print(mysortedlist)

myList = initalEntry()
myList.DataInput()
