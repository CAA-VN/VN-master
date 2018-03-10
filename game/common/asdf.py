def func(n, k):
	if k == 0 or n == 0:
		return 0
	a = n // 10
	b = k - 1
	return func(a, k) if func(a, k) > n % 10 + func(a, b) else n % 10 + func(a, b)
print(func(12347, 4))





def func2(n, k):
	if k == 0 or n == 0:
		return 0
	a = n % 10 + func2(n // 10, k-1)
	b = func2(n // 10, k)
	return max(a, b)
print(func(4743738487434424335799, 5))