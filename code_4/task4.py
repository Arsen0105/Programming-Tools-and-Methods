def print_board():
	for i in a:
		for j in i:
			print(j, end='')
		print()
	print('\n\n')

def check(j=0):
	global h, v, dm, ds, cq
	res = 0

	if j == n:
		if cq:
			# print_board()
			return 1
		else:
			return 0

	for i in range(n):
		if h[i] and v[j] and dm[i + j] and ds[n - j - 1 + i]:
			h[i] = 0
			v[j] = 0
			dm[i + j] = 0
			ds[n - j - 1 + i] = 0
			cq += 1
			a[i][j] = '#'

			res += check(j + 1)

			h[i] = 1
			v[j] = 1
			dm[i + j] = 1
			ds[n - j - 1 + i] = 1
			cq -= 1
			a[i][j] = '*'

	# res += check(j + 1)


	return res


n = 7

# 1 - free, 0 - occupied
# horizontal
h = [1 for _ in range(n)]
# vertical
v = [1 for _ in range(n)]
# main diagonal
dm = [1 for _ in range(2 * n - 1)]
# side diagonal
ds = [1 for _ in range(2 * n - 1)]
# count queen
cq = 0

a = [['*' for _ in range(n)] for _ in range(n)]

print(check())
