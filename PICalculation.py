
# Using Leibniz formula for PI ie. 1 - 1/3 + 1/5 - 1/7 + ......... = PI



def oddrange():
    current = 1
    while True:
        yield current
        current += 2

def pi_series():
    odds = oddrange()
    approx = 0
    while True:
        approx += (4/(next(odds)))
        yield approx
        approx -= (4/(next(odds)))
        yield approx

approx_pi = pi_series()

for i in range(100):
    print(next(approx_pi))
