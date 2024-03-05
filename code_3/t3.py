def t():
	for i in range(2, n + 1):
		check(i)

	for i in range(a, b + 1):
		if n - i > 0:
			if not d[n - i]:
				print(i + flag)

def check(n):
	global d
	if n < a:
		d[n] = False
	for i in range(n - b, n - a + 1):
		if i > 0:
			if not d[i]:
				d[n] = True


n, a, b = 23, 1, 3
# False - loss, True - win
d = {i: False for i in range(1, n)}

# True - The one who takes the last match wins
# False - The one who takes the last match loses
flag = True

t()
print(d)
