#!/usr/bin/env python3
"""Exact, standard-library checks for a two-clade extinction-risk variance theorem."""
from fractions import Fraction as F
from math import comb


def add(a, b):
    z = [F(0)] * max(len(a), len(b))
    for i, c in enumerate(a): z[i] += c
    for i, c in enumerate(b): z[i] += c
    return trim(z)


def scale(a, c):
    return trim([c * t for t in a])


def multiply(a, b):
    z = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): z[i + j] += x * y
    return trim(z)


def trim(a):
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a


def evaluate(a, x):
    y = F(0)
    for c in a[::-1]: y = y * x + c
    return y


def derivative(a):
    return [F(k) * a[k] for k in range(1, len(a))]


def bernstein_coefficients(a, left, right):
    # Polynomial on [left,right] under q=left+(right-left)t,
    # then transformed from monomial to degree-n Bernstein form.
    n = len(a) - 1
    c = [sum(a[k] * comb(k, j) * left ** (k-j) * (right-left)**j
             for k in range(j, n+1)) for j in range(n+1)]
    return [sum(c[j] * F(comb(i, j), comb(n, j))
                for j in range(i+1)) for i in range(n+1)]


def H(m):
    a = [F(0)] * (m+2)
    a[0] = m - 1
    a[1] = -2*(m-2)
    a[m] -= 4*m-2
    a[m+1] += 8*m-8
    return a


expected_min = {
    (2, F(1,2), F(1)): F(1,2),
    (3, F(1,2), F(1)): F(9,16),
    (4, F(1,2), F(1)): F(2,5),
    (5, F(1,2), F(1)): F(1,8),
    (6, F(1,2), F(2,3)): F(167,2187),
    (6, F(2,3), F(3,4)): F(341,5103),
    (6, F(3,4), F(1)): F(217,512),
}
for (m,left,right), target in expected_min.items():
    values=bernstein_coefficients(H(m),left,right)
    assert min(values)==target, (m,left,right,min(values),target)
    assert all(c>0 for c in values)
print('Seven exact Bernstein certificates PASS')

# For all integer m >= 7, H_m(7/10) < 0 follows from the
# decreasing rational-geometric ratio described in the proof.
q = F(7,10)
assert evaluate(H(7),q)<0
assert F(8*7-18,2*7-9)*q**7 < 1
for m in range(7,101):
    assert evaluate(H(m),q)<0
    assert evaluate(H(m),F(1,2))>0
print('All-m sign argument and first 94 instances PASS')

# Exact 8-leaf rooted tree. A leaf with edge length 1; a 7-leaf
# star whose root edge is 4/5 and whose leaf edges all have length d.
d = F(1,10000)
b = F(4,5)
qpoly = [F(0), F(1)]
p_poly = [F(1), F(-1)]
mean = [F(0)]
second = [F(0)]
for mask in range(1<<8):
    alive = mask.bit_count()
    tail = (mask >> 1).bit_count()
    pd = F(bool(mask & 1)) + b * F(tail>0) + d*tail
    prob = multiply([F(1)],[F(1)])
    for _ in range(alive): prob = multiply(prob,p_poly)
    for _ in range(8-alive): prob = multiply(prob,qpoly)
    mean = add(mean,scale(prob,pd))
    second = add(second,scale(prob,pd*pd))
variance = add(second,scale(multiply(mean,mean),F(-1)))
# q(1-q), q^7(1-q^7), q^7(1-q).
a=[F(0)]*15
a[1]+=1+7*d*d
a[2]-=1+7*d*d
a[7]+=b*b+14*b*d
a[8]-=14*b*d
a[14]-=b*b
assert trim(a)==trim(variance), (a, variance)
print('256-subset exact polynomial identity PASS')

vp=derivative(variance)
points = [(F(1,2),1),(F(3,5),-1),(F(7,10),1),(F(9,10),-1)]
for x, sign in points:
    val=evaluate(vp,x)
    assert val * sign > 0
    print('variance derivative at q=',x,'sign', '+' if sign>0 else '-', 'value',val)
# Descartes rule: derivative nonzero coefficients, low to high, have 3 sign changes.
signs=[1 if c>0 else -1 for c in vp if c]
assert sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))==3
print('Exactly three positive derivative roots by Descartes and sign intervals PASS')
print('All checks PASS')
