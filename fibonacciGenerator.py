def fibonacci():
	current, previous = 0, 1
	while True:
		yield current
		current, previous = current + previous, current


fib = fibonacci()
n = int(input("Enter the order of fibonacci series:"))

for i in range(n):
	print(next(fib))


