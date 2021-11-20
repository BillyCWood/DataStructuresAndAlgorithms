#Author: Billy Wood

import random, time


#---------------Sorting Concepts-----------------


#------------Stability---------------
# A sorting algorithm is stable if the relative order of equal keys is maintained
# i.e A[2,1,3,5,4,3*] -> A'[1,2,3,3*,4,5]
# if the sorted output was A'[1,2,3*,3,4,5], then the sort is unstable


#------------In Place-----------------
# If an algorithm is in-place then it does not need extra space to manipulate the data
# and produces an output in the same memory that contains the data


#----------Stable----------------


def bubble(arr):
    #In-place
    #Time Complexity - O(n^2)
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
        
def selection(arr):
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
    
    return arr

def merge(arr):
    #Divide and Conquer
    #Out-of-Place
    #Time Complexity - O(nlgn)
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        left = arr[:mid]
  
        # into 2 halves
        right = arr[mid:]
  
        # Sorting the first half
        merge(left)
  
        # Sorting the second half
        merge(right)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
    return arr

def insert(arr):
    #Time Complexity - O(n^2)
    
    n = len(arr)

    for i in range(1,n):
        tmp = arr[i]
        j = i-1
        
        while(j>=0 and arr[j] > tmp):
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = tmp    
            
    
    return arr

def counting(arr):
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
    

    return final_list


#Counting sort implementation for Radix Sort
def counting(arr, exp):
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
    

    return arr

#---------Unstable---------------

def partition(arr,low,high):
    
    #pivot is the last element
    pivot = arr[high]

    i = low -1

    for j in range(low, high+1):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1
def quick(arr,low,high):
    
    if low < high:
        p = partition(arr,low,high)

        quick(arr, low, p-1)
        quick(arr, p+1, high)


    return arr


def shell(arr):
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

            i += 1
            j += 1

            k = i

            while k - interval > -1:

                if arr[k - interval] > arr[k]:
                    arr[k-interval],arr[k] = arr[k],arr[k-interval]
                k-=1
        
        interval //= 2 


    return arr

def radix(arr):
    #Faster alternative to Counting sort
    #Time Complexity - 
    largest = max(arr)

    exp = 1

    while largest/exp > 0:
        counting(arr, exp)
        exp *=10
    
    return arr
def bucket(arr):
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
        merge(current)
        if len(current) != 0:
            arr.extend(current)

    
    return arr


def main():

    reps = 100
    numbers = []
    


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


    ''' 
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
    '''

main()