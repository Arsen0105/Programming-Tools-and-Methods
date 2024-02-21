# 1
def t(n):
	if n:
		return 2 * t(n - 1) + 1
	return 0

# 2
def k(n):
	return 2 ** n - 1


n = 9
print(t(n))
