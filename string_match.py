# String matching using BruteForce approach
def stringMatch(text, pattern):
	n = len(text)
	m = len(pattern)
	for i in range(n-m):
		j = 0
		while j < m and pattern[j]==text[i+j]:
			j = j+1
		if j == m:
			return i
	return -1

t = "100101011010011001100101111010"
p = "001011"
res = stringMatch(t, p)
print(res)