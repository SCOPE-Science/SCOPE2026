#!/usr/bin/env python3
"""High-precision finite combinatorics corroboration for the three-gap bounded-remainder census.
No finite check is used as proof of the general theorem.
"""
from decimal import Decimal, getcontext, ROUND_FLOOR
from math import floor

getcontext().prec = 100

def flo(x):
    return int(x.to_integral_value(rounding=ROUND_FLOOR))

def frac(x):
    return x - Decimal(flo(x))

def formula(n, m, alpha):
    if n == 1:
        return 0
    a = min(range(1, n), key=lambda i: frac(Decimal(i)*alpha))
    b = max(range(1, n), key=lambda i: frac(Decimal(i)*alpha))
    assert a+b >= n
    flag = lambda d: int(flo(Decimal(d)*alpha) % m == 0)
    return m*((n-a)*flag(a) + (n-b)*flag(-b) + (a+b-n)*flag(a-b))

def direct_circular_edges(n, m, alpha):
    # Each phase cut has the form j-i*alpha, with i=0,...,n-1 and j mod m.
    # List one fractional unit: the orbit label is j-floor(-i*alpha).
    points = []
    for i in range(n):
        z = -Decimal(i)*alpha
        points.append((frac(z), -flo(z) % m, i))
    points.sort()
    count = 0
    for k in range(n):
        _, a, _ = points[k]
        _, b, _ = points[(k+1) % n]
        # Crossing from one unit interval to the next increments j by one.
        if (b-a+int(k==n-1)) % m == 0:
            count += m
    return count

def successor_check(n, alpha):
    if n == 1:
        return
    vals = [frac(Decimal(i)*alpha) for i in range(n)]
    a = min(range(1, n), key=lambda i: vals[i])
    b = max(range(1, n), key=lambda i: vals[i])
    order = sorted(range(n), key=lambda i: vals[i])
    successor = dict(zip(order, order[1:]+order[:1]))
    for i in range(n):
        j = i+a if i+a < n else i-b if i >= b else i+a-b
        assert successor[i] == j, (n, i, a, b)

slopes = [(Decimal(k).sqrt()-1) / (k-1) for k in (2,3,5,7)]
# Every chosen slope is irrational, and lies strictly between 0 and 1.
tests = 0
for alpha in slopes:
    for n in range(1, 161):
        successor_check(n,alpha)
        for m in range(2, 8):
            assert formula(n,m,alpha) == direct_circular_edges(n,m,alpha), (alpha,n,m)
            tests += 1

fib = [0,1]
for _ in range(18):
    fib.append(fib[-1]+fib[-2])
golden = (Decimal(5).sqrt()-1)/2
for r in range(4,17):
    n = fib[r]
    expected = 0 if r%3 == 1 else 2*(fib[r-2] if r%3 == 2 else fib[r-1])
    assert formula(n,2,golden) == expected, (r,n)

print('PASS:', tests, 'direct circular-edge/count comparisons; 640 successor-map tests; 13 Fibonacci phase checks')
