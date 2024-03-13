#python program to sort the given tuple according to the given index
from operator import itemgetter
tl = [(0,25,36), (5,62,14), (9,4,5)]
print("Given tuple list: " + str(tl))
N = int(input("Enter the index to sort:"))
tl.sort(key = itemgetter(N)) 
print("Tuple list after sorting according to index", N,": " + str(tl))
