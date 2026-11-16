"""Exact arithmetic checks for Fourier multipliers of 101-avoiding binary words.

Run with Python 3: python CHECK.py
No external dependencies.
"""
from itertools import product
from math import gcd
from functools import reduce

A = ((1, 1, 0), (0, 1, 1), (1, 0, 0))
B = ((1, -1, 0), (0, -1, 1), (1, 0, 0))
E = (1, 0, 0)
ONE = (1, 1, 1)

def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))

def mv(a, b):
    return tuple(sum(a[i][j]*b[j] for j in range(3)) for i in range(3))

def vm(a, b):
    return tuple(sum(a[i]*b[i][j] for i in range(3)) for j in range(3))

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def power(a, k):
    z = ((1,0,0),(0,1,0),(0,0,1))
    while k:
        if k & 1: z = mm(z, a)
        a = mm(a, a)
        k //= 2
    return z

def signing(n):
    """Return one Fourier frequency with zero multiplier, or multiplier one."""
    k, r = divmod(n, 7)
    if r == 0:
        return {1+7*j for j in range(k)}
    if r == 1:
        if k == 0: return {0}
        return {0} | {6+7*j for j in range(k)}
    if r == 2:
        return {7*j for j in range(k+1)}
    if r == 3:
        return {0} | {8+7*j for j in range(k)}
    if r == 4:
        return {1+7*j for j in range(k+1)}
    if r in (5, 6):
        return {1+7*j for j in range(k+1)}
    raise AssertionError

def transfer(n, negatives):
    v = E
    for i in range(n):
        v = vm(v, B if i in negatives else A)
    return dot(v, ONE)

def direct(n, negatives):
    ans = 0
    negmask = sum(1 << i for i in negatives)
    for m in range(1 << n):
        if '101' in ''.join(str((m >> i) & 1) for i in range(n)):
            continue
        ans += (-1)**((m & negmask).bit_count() % 2)
    return ans

def all_walsh(n):
    buf = [int('101' not in ''.join(str((m >> i) & 1) for i in range(n))) for m in range(1<<n)]
    a = buf[:]
    for i in range(n):
        step = 1<<i
        for j in range(0, 1<<n, 2*step):
            for t in range(j, j+step):
                x, y = a[t], a[t+step]
                a[t], a[t+step] = x+y, x-y
    return a, sum(buf)

C = mm(B, power(A,6))
D = mm(power(A,6), B)
L = vm(E, A)
R = mv(mm(B,A), ONE)
RP = mv(A,ONE)
assert C == ((3,4,2),(-2,-3,-2),(12,16,9))
assert D == ((21,-28,16),(16,-21,12),(12,-16,9))
assert vm(L,C) == L
assert mv(C,R) == R
assert mv(D,RP) == RP
assert dot(vm(E,B),RP) == 0
assert dot(vm(vm(E,B),power(A,5)), R) == 0
assert dot(vm(L,mm(B,power(A,2))), ONE) == 0
assert dot(vm(vm(E,B),power(A,7)),R) == 1
assert dot(vm(vm(E,B),power(A,2)),ONE) == 1
for j in (3,4,5):
    assert dot(vm(L,mm(B,power(A,j))),ONE) == 1

# The seven-step cardinality recurrence has exact integer coefficients.
num = [1,2,4]
for n in range(3,121):
    num.append(2*num[-1] - num[-2] + num[-3])
for n in range(1,121):
    assert (num[n]&1) == (n%7 in (0,3,5,6))
    frequency = signing(n)
    assert all(0 <= j < n for j in frequency)
    assert transfer(n, frequency) == (1 if n%7 in (0,3,5,6) else 0)

# An independent complete enumeration of the finite Fourier spectra.
frequencies_checked = 0
for n in range(1,18):
    walsh, count = all_walsh(n)
    assert count == num[n]
    assert all(v%2 == count%2 for v in walsh)
    if n%7 in (0,3,5,6):
        assert all(v!=0 for v in walsh) and 1 in walsh
    else:
        assert 0 in walsh
    negmask = sum(1<<i for i in signing(n))
    assert walsh[negmask] == transfer(n, signing(n))
    # Check direct summation on selected Fourier characters,
    # independently of the transform and of the automaton.
    for mask in (0, 1<< (n-1), negmask, (1<<n)-1):
        neg={i for i in range(n) if (mask>>i)&1}
        assert direct(n,neg) == walsh[mask] == transfer(n,neg)
    frequencies_checked += 1<<n
print('AVOID_101_FOURIER_PERIOD7_PASS',
      f'full_frequencies={frequencies_checked}',
      'lengths=1..17', 'witness_lengths=1..120')
