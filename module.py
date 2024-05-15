def selection(arr1):
    n = len(arr1)
    for i in range(n):
        temp = i
        for j in range(i+1, n):
            if arr1[j] < arr1[temp]:
                temp = j
        arr1[i], arr1[temp] = arr1[temp], arr1[i]

def bubble(arr2):
    n=len(arr2)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr2[j]>arr2[j+1]:
                arr2[j],arr2[j+1]=arr2[j+1],arr2[j]

def insertion(arr3):
    for i in range(1, len(arr3)):
        temp = arr3[i]
        j = i - 1
        while j >= 0 and temp < arr3[j]:
            arr3[j + 1] = arr3[j]
            j = j - 1
        arr3[j + 1] = temp
    return arr3



def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2



def heapify(arr, n, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
  
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)

  

# merge sort

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]



# Quick sort 


def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)



 # Counting sort
 
def countingSort(array):
    size = len(array)
    output = [0] * size

    count = [0] * 10

    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
        
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1


  

# Radix sort in Python


def radixSort(array)    
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

