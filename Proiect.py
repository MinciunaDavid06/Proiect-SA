import time
import random
import sys
sys.setrecursionlimit(10**6) #creste limita de la recursivitate (quick sort e obraznica)

def bubbleSort(l):
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
    n=len(l)
    for i in range(n-1):
        minim=i
        for j in range(i+1,n):
            if l[j]<l[minim]:
                minim=j
        l[i],l[minim]=l[minim],l[i]
    return l

def insertionSort(l):
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

def quickSort(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    st=[]
    dr=[]
    for i in l[1:]:
        if i <= pivot:
            st.append(i)
        else:
            dr.append(i)
    return quickSort(st)+[pivot]+quickSort(dr)

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

l1=lista_aleatoare(n)
print("\nLista aleatore:")
print(f"Bubble: {timp_sortare(bubbleSort,l1):.6f} sec")
print(f"Selection: {timp_sortare(selectionSort,l1):.6f} sec")
print(f"Insertion: {timp_sortare(insertionSort,l1):.6f} sec")
print(f"Quick: {timp_sortare(quickSort,l1):.6f} sec")

l2=lista_sortata(n)
print("\nLista sortata:")
print(f"Bubble: {timp_sortare(bubbleSort,l2):.6f} sec")
print(f"Selection: {timp_sortare(selectionSort,l2):.6f} sec")
print(f"Insertion: {timp_sortare(insertionSort,l2):.6f} sec")
print(f"Quick: {timp_sortare(quickSort,l2):.6f} sec")

l3=lista_invers_sortata(n)
print("\nLista sortata invers:")
print(f"Bubble: {timp_sortare(bubbleSort,l3):.6f} sec")
print(f"Selection: {timp_sortare(selectionSort,l3):.6f} sec")
print(f"Insertion: {timp_sortare(insertionSort,l3):.6f} sec")
print(f"Quick: {timp_sortare(quickSort,l3):.6f} sec")

l4=lista_aproape_sortata(n)
print("\nLista aproape sortata:")
print(f"Bubble: {timp_sortare(bubbleSort,l4):.6f} sec")
print(f"Selection: {timp_sortare(selectionSort,l4):.6f} sec")
print(f"Insertion: {timp_sortare(insertionSort,l4):.6f} sec")
print(f"Quick: {timp_sortare(quickSort,l4):.6f} sec")