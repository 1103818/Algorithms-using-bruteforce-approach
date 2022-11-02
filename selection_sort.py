# Implementation of Selection Sort algorithm
def selectionSort(A):
	for i in range(len(A)-1):
		mi = i
		for j in range(i+1, len(A)):
			if A[j] < A[mi]:
				mi = j
		A[i], A[mi] = A[mi], A[i]

arr = [5, 1, 3, 2, 4]

selectionSort(arr)
print(arr)