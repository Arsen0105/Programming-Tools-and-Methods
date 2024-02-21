def p(n):
	return q(n, n)

def q(n, m):
	if n == 1:
		return 1
	if m == 1:
		return 1
	if n > m:
		return q(n, m - 1) + q(n - m, m)
	if n == m:
		return q(n, n - 1) + 1
	if n < m:
		return q(n, n)


n = 15
print(p(n))
