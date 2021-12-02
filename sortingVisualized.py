#Author: Billy Wood

import random, time
from typing import final
from colors import *


#---------------Sorting Concepts-----------------


#------------Stability---------------
# A sorting algorithm is stable if the relative order of equal keys is maintained
# i.e A[2,1,3,5,4,3*] -> A'[1,2,3,3*,4,5]
# if the sorted output was A'[1,2,3*,3,4,5], then the sort is unstable


#------------In Place-----------------
# If an algorithm is in-place then it does not need extra space to manipulate the data
# and produces an output in the same memory that contains the data


#----------Stable----------------


#def bubble(arr):
def bubble(arr,drawData,timeTick):
    #In-place
    #Time Complexity - O(n^2)
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                drawData(arr, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(arr))] )
                time.sleep(timeTick)
    
    #return arr
    drawData(arr, [BLUE for x in range(len(arr))])
        
#def selection(arr):
def selection(arr,drawData,timeTick):
    #In-Place
    #Time Complexity - O(n^2)

    n = len(arr)
    for i in range(n):
        smallest = arr[i]
        smallest_index = i
        

        for j in range(i+1,n):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j

        arr[i],arr[smallest_index] = arr[smallest_index], arr[i]
        drawData(arr,[BLUE for x in range(len(arr))])
    
    
    time.sleep(timeTick)
    drawData(arr,[BLUE for x in range(len(arr))])
    #return arr

#def merge(arr):
def merge(arr, start, end, drawData, timeTick):
    #Divide and Conquer
    #Out-of-Place
    #Time Complexity - O(nlgn)
    #if len(arr) > 1:
    if start < end:
  
        #temporary arr
        tmp = []
         # Finding the mid of the array
        mid = (start+end)//2
  
        # Dividing the array elements
        #left = arr[:mid]
  
        # into 2 halves
        #right = arr[mid:]

  
        # Sorting the first half
        merge(arr,start,mid,drawData,timeTick)
  
        # Sorting the second half
        merge(arr,mid+1,end,drawData,timeTick)
  
        #i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        '''
        while i < len(arr[:mid]) and j < len(arr[mid:]):
            if arr[i] < arr[j]:
                arr[k] = arr[i]
                i += 1
            else:
                arr[k] = arr[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(arr[:mid]):
            arr[k] = arr[i]
            i += 1
            k += 1
  
        while j < len(arr[mid:]):
            arr[k] = arr[j]
            j += 1
            k += 1

        '''

        p = start
        q = mid+1

        for i in range(start, end+1):
            if p > mid:
                tmp.append(arr[q])
                q+=1
            elif q > end:
                tmp.append(arr[p])
                p+=1
            elif arr[p]<arr[q]:
                tmp.append(arr[p])
                p+=1
            else:
                tmp.append(arr[q])
                q+=1
        
        for p in range(len(tmp)):
            arr[start] = tmp[p]
            start+=1


    
        drawData(arr, [PURPLE if x >= start and x < mid else YELLOW if x == mid 
                            else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(arr))])
        time.sleep(timeTick)

    drawData(arr, [BLUE for x in range(len(arr))])
    # return arr

#def insert(arr):
def insert(arr,drawData,timeTick):
    #Time Complexity - O(n^2)
    
    n = len(arr)

    for i in range(1,n):
        tmp = arr[i]
        j = i-1
        
        while(j>=0 and arr[j] > tmp):
            arr[j+1] = arr[j]
            j -= 1
            drawData(arr, [YELLOW if x == j else BLUE for x in range(len(arr))] )

        arr[j+1] = tmp
        drawData(arr,[BLUE for x in range(len(arr))])    
            
    
    time.sleep(timeTick)
    drawData(arr,[BLUE for x in range(len(arr))])
    #return arr

#def counting(arr):
def counting(arr,drawData,timeTick):
    #Out-of-Place
    #Not a comparison based sort
    #Time Complexity- Best - O(n+k)
    #Time Complexity - Worst- O(n^2)

    n = len(arr)

    #Create list of the unique keys

    unique_keys = [0] * (max(arr)+1)
    for i in range(max(arr)+1):
        unique_keys[i] = i
    
    
    #Count the number of occurrences of elements in 
    #the unique keys list that are in the inputted list
    occurrences = [0] * len(unique_keys)
    for i in range(len(unique_keys)):
        count = 0
        for j in range(len(arr)):
            if unique_keys[i] == arr[j]:
                count +=1

        occurrences[i] = count

    #Add up the number of occurences
    for i in range(1,len(occurrences)):
        occurrences[i] = occurrences[i] + occurrences[i-1]

    #The number of occurrences now becomes the starting index for each element
    index = len(occurrences)-1
    while index >= 0:
        if index == 0:
            occurrences[index] = 0
        else:
            occurrences[index] = occurrences[index-1]

        index -= 1    

    #Where the actual sorting happens
    final_list = [0] * len(arr)

    for i in range(n):
        final_list[occurrences[unique_keys.index(arr[i])]] = arr[i]
        occurrences[unique_keys.index(arr[i])] += 1
        drawData(final_list, [BLUE for x in range(len(final_list))])
    

    time.sleep(timeTick)
    drawData(final_list,[BLUE for x in range(len(final_list))])
    arr.clear()
    arr.extend(final_list)
    #return final_list


#Counting sort implementation for Radix Sort
def countingSort(arr, exp,drawData,timeTick):
    #Out-of-Place
    #Not a comparison based sort
    #Time Complexity- Best - O(n+k)
    #Time Complexity - Worst- O(n^2)

    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = arr[i] // exp
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]
        drawData(arr, [BLUE for x in range(len(arr))])
    

    time.sleep(timeTick)
    drawData(arr,[BLUE for x in range(len(arr))])
    return arr

#---------Unstable---------------

def partition(arr,low,high,drawData):
    
    #pivot is the last element
    pivot = arr[high]

    i = low -1

    for j in range(low, high+1):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
            drawData(arr, [PURPLE if x >= low and x < pivot else YELLOW if x == pivot 
                            else DARK_BLUE if x > pivot and x <=high else BLUE for x in range(len(arr))])

    arr[i+1],arr[high] = arr[high],arr[i+1]

    drawData(arr, [BLUE for x in range(len(arr))])
    return i+1
#def quick(arr,low,high):
def quick(arr,low,high,drawData,timeTick):
    if low < high:
        p = partition(arr,low,high,drawData)

        quick(arr, low, p-1,drawData,timeTick)
        quick(arr, p+1, high,drawData,timeTick)
        drawData(arr, [PURPLE if x >= low and x < p else YELLOW if x == p 
                        else DARK_BLUE if x > p and x <=high else BLUE for x in range(len(arr))])

    
    time.sleep(timeTick)
    drawData(arr, [BLUE for x in range(len(arr))])
    #return arr

def heapify(arr, n, i):

	largest = i # Initialize largest as root
	left = 2 * i + 1
	right = 2 * i + 2
    

	# See if left child of root exists and is
	# greater than root
	if left < n and arr[largest] < arr[left]:
		largest = left

	# See if right child of root exists and is
	# greater than root
	if right < n and arr[largest] < arr[right]:
		largest = right

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap


		# Heapify the root.
		heapify(arr, n, largest)

#def heap(arr):
def heap(arr,drawData,timeTick):
    n = len(arr)
    

	# Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
        drawData(arr,[BLUE for x in range(len(arr))])

	# One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        drawData(arr,[BLUE for x in range(len(arr))])


    time.sleep(timeTick)
    drawData(arr,[BLUE for x in range(len(arr))])
    # return arr


    


#def shell(arr):
def shell(arr,drawData,timeTick):
    #variation of insertion sort
    #Partially sorting by sorting elements that are a certain number of spacess apart
    #In-Place
    #Time Complexity - O(n^2)
    
    interval = len(arr)//2

    while interval > 0:
        i = 0
        j = interval

        while j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                drawData(arr,[BLUE for x in range(len(arr))])

            i += 1
            j += 1

            k = i

            while k - interval > -1:

                if arr[k - interval] > arr[k]:
                    arr[k-interval],arr[k] = arr[k],arr[k-interval]
                    drawData(arr,[BLUE for x in range(len(arr))])

                drawData(arr,[YELLOW if x == k else BLUE for x in range(len(arr))])
                k-=1
        
        interval //= 2 


    time.sleep(timeTick)
    drawData(arr,[BLUE for x in range(len(arr))])
    
    #return arr

def radix(arr,drawData,timeTick):
    #Faster alternative to Counting sort
    #Time Complexity - 
    largest = max(arr)

    exp = 1

    while largest/exp > 0:
        countingSort(arr, exp,drawData,timeTick)
        exp *=10
        if isSorted(arr):
            break
    
    time.sleep(timeTick)
    drawData(arr,[BLUE for x in range(len(arr))])
    #return arr

#def bucket(arr):
def bucket(arr,drawData,timeTick):
    #In-Place
    #Use when input is uniformily distributed or floating point values
    #Time Complexity - Worst Case - O(n^2)
    #Time Complexity - Best Case - O(n)

    buckets = 5
    bucketList = []

    largest = max(arr)
    smallest = min(arr)
    #How many values go into each bucket
    bucketRange = (largest - smallest) // buckets + 1

    #create the buckets
    while buckets > 0:
        newBucket = []
        bucketList.append(newBucket)
        buckets -= 1

    #place the values into their respective buckets
    for i in range(len(arr)):
        number = arr[i]
        difference = number - smallest
        bucketIndex = (int)(difference//bucketRange)
        bucketList[bucketIndex].append(number)

    
    #Sort the buckets and merge them
    arr.clear()
    for bucket in bucketList:
        current = bucket
        merge(current,0,len(current)-1,drawData,timeTick)
        drawData(arr,[BLUE for x in range(len(arr))])
        if len(current) != 0:
            arr.extend(current)

    
    time.sleep(timeTick)
    drawData(arr,[BLUE for x in range(len(arr))])
    #return arr


#---------Joke Sorts---------------

def stooge(arr,l,h):

    if l >= h:
        return
  
    # If first element is smaller
    # than last, swap them
    if arr[l]>arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t
  
    # If there are more than 2 elements in
    # the array
    if h-l + 1 > 2:
        t = (int)((h-l + 1)/3)
  
        # Recursively sort first 2 / 3 elements
        stooge(arr, l, (h-t))
  
        # Recursively sort last 2 / 3 elements
        stooge(arr, l + t, (h))
  
        # Recursively sort first 2 / 3 elements
        # again to confirm
        stooge(arr, l, (h-t))
    
    return arr

def bogo(arr):
    #Runtime - O(n!)
    #Shuffle until array is sorted
    while not isSorted(arr):
        for i in range(len(arr)):
            index = random.randint(i, (len(arr)-1))
            arr[i],arr[index] = arr[index],arr[i]
    return arr

#-------------------------------
def isSorted(arr):

    if len(arr) == 0 or len(arr) == 1:
        return True

    for i in range(1, len(arr)):
        if not arr[i] >= arr[i-1]:
            return False

    return True  
    

'''
def main():

    reps = 100
    numbers = []

    
    #---------------------------------------------------------- 
    
    for i in range(reps):
        numbers.append(random.randint(0,100))
    
    print("***Heap Sort***")
    print(numbers)
    
    start = time.time()
    #heap(numbers)
    print(heap(numbers))
    end = time.time()

    print("Runtime with {} elements: {}".format(reps,end-start))
    print()





    

    #---------------------------------------------------------- 

    for i in range(1000):
        numbers.append(random.randint(0,100))
    
    print("***Stooge Sort***")
    #print(numbers)
    
    start = time.time()
    stooge(numbers,0, len(numbers)-1)
    #print(stooge(numbers,0,len(numbers)-1))
    end = time.time()

    print("Runtime with 1000 elements: {}".format(end-start))
    print()

    #---------------------------------------------------------- 
    
    for i in range(10):
        numbers.append(random.randint(0,100))
    
    print("***Bogo Sort***")
    print(numbers)
    
    start = time.time()
    #bucket(numbers)
    print(bogo(numbers))
    end = time.time()

    print("Runtime with 10 elements: {}".format(end-start))
    print()
    
    #---------------------------------------------------------- 
    
    for i in range(reps):
        numbers.append(random.randint(0,100))
    
    print("***Bucket Sort***")
    print(numbers)
    
    start = time.time()
    #bucket(numbers)
    print(bubble(numbers))
    end = time.time()

    print("Runtime with {} elements: {}".format(reps,end-start))
    print()

    #---------------------------------------------------------- 
     
    for i in range(reps):
        numbers.append(random.randint(0,100))
    
    print("***Radix Sort***")
    #print(numbers)
    
    start = time.time()
    radix(numbers)
    #print(bubble(numbers))
    end = time.time()

    print("Runtime with {} elements: {}".format(reps,end-start))
    print()
    
    
    #---------------------------------------------------------- 
    
    for i in range(reps):
        numbers.append(random.randint(0,100))
    
    print("***Bubble Sort***")
    #print(numbers)
    
    start = time.time()
    #bubble(numbers)
    #print(bubble(numbers))
    end = time.time()

    print("Runtime with {} elements: {}".format(reps,end-start))
    print()


   #---------------------------------------------------------- 
    for i in range(reps):
        numbers[i] = random.randint(0,100)
    
    print("***Selection Sort***")
    #print(numbers)
    
    start = time.time()
    #selection(numbers)
    end = time.time()
    #print(selection(numbers))
    print("Runtime with {} elements: {}".format(reps,end-start))
    print()

    #---------------------------------------------------------- 
    for i in range(reps):
        numbers[i] = random.randint(0,100)
    
    print("***Merge Sort***")
    #print(numbers)
    
    start = time.time()
    merge(numbers)
    end = time.time()
    #print(merge(numbers))
    print("Runtime with {} elements: {}".format(reps,end-start))
    print()

    
    #---------------------------------------------------------- 
    for i in range(reps):
        numbers[i] = random.randint(0,100)
    
    print("***Insert Sort***")
    #print(numbers)
    
    
    start = time.time()
    #insert(numbers)
    end = time.time()
    #print(insert(numbers))
    print("Runtime with {} elements: {}".format(reps,end-start))
    print()

   
   #---------------------------------------------------------- 
    for i in range(reps):
        numbers[i] = random.randint(0,100)
    
    print("***Counting Sort***")
    #print(numbers)
    

    start = time.time()
    counting(numbers)
    end = time.time()
    #print(counting(numbers))
    print("Runtime with {} elements: {}".format(reps,end-start))
    print()



    #---------------------------------------------------------- 
    for i in range(reps):
        numbers[i] = random.randint(0,100)
    
    print("***Quick Sort***")
    #print(numbers)


    start = time.time()
    quick(numbers,0,len(numbers)-1)
    end = time.time()
    #print(quick(numbers,0,len(numbers)-1))
    print("Runtime with {} elements: {}".format(reps,end-start))
    print()



    #---------------------------------------------------------- 
    for i in range(reps):
        numbers[i] = random.randint(0,100)
    
    print("***Shell Sort***")
    #print(numbers)
    
    
    start = time.time()
    #shell(numbers)
    end = time.time()
    #print(shell(numbers))
    print("Runtime with {} elements: {}".format(reps,end-start))
    print()
    

main()
'''