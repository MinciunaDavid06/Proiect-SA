import time
import random
import sys
sys.setrecursionlimit(10**6) #creste limita de la recursivitate (quick sort e obraznica)
def bubbleSort(l):
    l= l.copy()
    n=len(l)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swapped=True
        if not swapped:
            break
    return l

def selectionSort(l):
    l= l.copy()
    n=len(l)
    for i in range(n-1):
        minim=i
        for j in range(i+1,n):
            if l[j]<l[minim]:
                minim=j
        l[i],l[minim]=l[minim],l[i]
    return l

def insertionSort(l):
    l= l.copy()
    n=len(l)
    if n <= 1:
        return l
    for i in range(1,n):
        key=l[i]         
        j=i-1
        while j >= 0 and key<l[j]: 
            l[j+1]=l[j]
            j-=1
        l[j+1]=key   
    return l

def quickSort(l):
    l= l.copy()
    if len(l)<=1:
        return l
    pivot = l[0]
    st=[]
    dr=[]
    for i in l[1:]:
        if i <= pivot:
            st.append(i)
        else:
            dr.append(i)
    return quickSort(st)+[pivot]+quickSort(dr)

def mergeSort(l):
    l = l.copy()
    if len(l) <= 1:
        return l
    mijloc = len(l) // 2
    stanga = mergeSort(l[:mijloc])
    dreapta = mergeSort(l[mijloc:])
    return interclasare(stanga, dreapta)
def interclasare(stanga, dreapta):
    rezultat = []
    i = 0
    j = 0
    while i < len(stanga) and j < len(dreapta):
        if stanga[i] <= dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1
    while i < len(stanga):
        rezultat.append(stanga[i])
        i += 1
    while j < len(dreapta):
        rezultat.append(dreapta[j])
        j += 1
    return rezultat

def heapSort(l):
    l = l.copy()
    n = len(l)
    for i in range(n // 2 - 1, -1, -1):
        heapify(l, n, i)
    for i in range(n - 1, 0, -1):
        l[0], l[i] = l[i], l[0]
        heapify(l, i, 0)

    return l

def heapify(l, n, i):
    maxim = i
    stanga = 2 * i + 1
    dreapta = 2 * i + 2
    if stanga < n and l[stanga] > l[maxim]:
        maxim = stanga
    if dreapta < n and l[dreapta] > l[maxim]:
        maxim = dreapta
    if maxim != i:
        l[i], l[maxim] = l[maxim], l[i]
        heapify(l, n, maxim)

def lista_aleatoare(n, min_val=0, max_val=100000):
    l=[]
    for _ in range(n):
        nr=random.randint(min_val,max_val)
        l.append(nr)
    return l

def lista_sortata(n):
    return list(range(n+1))

def lista_invers_sortata(n):
    return list(range(n,-1,-1))

def lista_aproape_sortata(n):
    l=list(range(n))
    for i in range(n//10):
        x=random.randint(0,n-1)
        y=random.randint(0,n-1)
        l[x],l[y]=l[y],l[x]
    return l


def timp_sortare(functie, l):
    start=time.time()
    functie(l)
    end=time.time()
    return end-start

n=int(input("Introdu Dimensiunea Listei: "))
#pentru lista random#
l1=lista_aleatoare(n)
print("\nLista aleatore:")
print(f"Bubble: {timp_sortare(bubbleSort,l1):.6f} sec")
print(f"Selection: {timp_sortare(selectionSort,l1):.6f} sec")
print(f"Insertion: {timp_sortare(insertionSort,l1):.6f} sec")
print(f"Quick: {timp_sortare(quickSort,l1):.6f} sec")
print(f"Merge: {timp_sortare(mergeSort, l1):.6f} sec")
print(f"Heap: {timp_sortare(heapSort, l1):.6f} sec")

#lista sortata#
l2=lista_sortata(n)
print("\nLista sortata:")
print(f"Bubble: {timp_sortare(bubbleSort,l2):.6f} sec")
print(f"Selection: {timp_sortare(selectionSort,l2):.6f} sec")
print(f"Insertion: {timp_sortare(insertionSort,l2):.6f} sec")
print(f"Quick: {timp_sortare(quickSort,l2):.6f} sec")
print(f"Merge: {timp_sortare(mergeSort, l2):.6f} sec")
print(f"Heap: {timp_sortare(heapSort, l2):.6f} sec")

#lista sortata invers#
l3=lista_invers_sortata(n)
print("\nLista sortata invers:")
print(f"Bubble: {timp_sortare(bubbleSort,l3):.6f} sec")
print(f"Selection: {timp_sortare(selectionSort,l3):.6f} sec")
print(f"Insertion: {timp_sortare(insertionSort,l3):.6f} sec")
print(f"Quick: {timp_sortare(quickSort,l3):.6f} sec")
print(f"Merge: {timp_sortare(mergeSort, l3):.6f} sec")
print(f"Heap: {timp_sortare(heapSort, l3):.6f} sec")

#lista aproapte sortata#
l4=lista_aproape_sortata(n)
print("\nLista aproape sortata:")
print(f"Bubble: {timp_sortare(bubbleSort,l4):.6f} sec")
print(f"Selection: {timp_sortare(selectionSort,l4):.6f} sec")
print(f"Insertion: {timp_sortare(insertionSort,l4):.6f} sec")
print(f"Quick: {timp_sortare(quickSort,l4):.6f} sec")
print(f"Merge: {timp_sortare(mergeSort, l4):.6f} sec")
print(f"Heap: {timp_sortare(heapSort, l4):.6f} sec")
