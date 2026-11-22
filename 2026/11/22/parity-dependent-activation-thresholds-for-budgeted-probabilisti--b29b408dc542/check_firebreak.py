"""Finite exact checks for independent-bond firebreak allocation on a path.

Only standard-library Python 3 is required. This checks examples and formulas;
the unbounded theorem is established by the accompanying proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import exp, log

COUNT = 0

def check(test):
    global COUNT
    assert test
    COUNT += 1


def interval_product(qs, i, j):
    out = Q(1)
    for k in range(i, j):
        out *= qs[k]
    return out


def pair_sum(qs):
    n = len(qs) + 1
    return sum((interval_product(qs, i, j) for i in range(n) for j in range(i + 1, n)), Q(0))


def expected_burn(qs):
    return 1 + Q(2, len(qs) + 1) * pair_sum(qs)


def enumerate_burn(qs):
    n = len(qs) + 1
    total = Q(0)
    for bits in product((0,1), repeat=n-1):
        prob = Q(1)
        for bit, q in zip(bits, qs):
            prob *= q if bit else 1-q
        start = 0
        weighted = 0
        for k in range(n):
            if k == n-1 or not bits[k]:
                size = k-start+1
                weighted += size*size
                start = k+1
        total += prob*Q(weighted,n)
    return total


def gradient(qs,k):
    n = len(qs) + 1
    return -sum((interval_product(qs,i,j) for i in range(n) for j in range(i+1,n) if i<=k<j),Q(0))


def f_float(g):
    n=len(g)+1
    return sum(exp(-sum(g[i:j])) for i in range(n) for j in range(i+1,n))


def four_opt(B):
    if B <= log(2): return 0.
    lo,hi=0.,B/2
    for _ in range(95):
        x=(lo+hi)/2
        derivative=-2*exp(-x)+2*exp(-B+2*x)+2*exp(-B+x)
        if derivative<0: lo=x
        else:hi=x
    return (lo+hi)/2

# Direct exhaustive stochastic calculation, with exact rational edge laws.
sequences = [Q(1,4),Q(2,5),Q(1,2),Q(3,5),Q(3,4)]
for n in range(2,9):
    for shift in range(6):
        qs=[sequences[(shift+2*k)%len(sequences)] for k in range(n-1)]
        check(expected_burn(qs)==enumerate_burn(qs))
        for k in range(n-1):
            check(gradient(qs,k)==-(sum((interval_product(qs,i,j) for i in range(k+1) for j in range(k+1,n)),Q(0))))

# Even-path derivative identity, including every noncentral candidate.
for m in range(2,13):
    for q in (Q(1,5),Q(1,3),Q(1,2),Q(2,3),Q(3,4),Q(9,10)):
        qs=[Q(1)]*(2*m-1);qs[m-1]=q
        for k in range(1,m):
            left=gradient(qs,k-1)-gradient(qs,m-1)
            check(left == (m-k)*(m*q-k))
            check(gradient(qs,2*m-1-k)==gradient(qs,k-1))
        all_eligible=all(gradient(qs,k)>=gradient(qs,m-1) for k in range(2*m-1))
        check(all_eligible == (m*q>=m-1))

# Odd-path derivative identity, two equal central gaps.
for m in range(2,13):
    for q in (Q(1,5),Q(1,3),Q(1,2),Q(2,3),Q(3,4),Q(9,10)):
        qs=[Q(1)]*(2*m);qs[m-1]=q;qs[m]=q
        for k in range(1,m):
            left=gradient(qs,k-1)-gradient(qs,m-1)
            check(left == (m-k)*(q + m*q*q-k))
            check(gradient(qs,2*m-k)==gradient(qs,k-1))
        check(gradient(qs,m-1)==gradient(qs,m))
        all_eligible=all(gradient(qs,k)>=gradient(qs,m-1) for k in range(2*m))
        check(all_eligible == (m*q >= m-1))

# Four-patch full optimizer and a global symmetric search check.
for B in [0.03,0.2,log(2),0.7,1.0,2.0,5.0,10.0]:
    x=four_opt(B)
    check(0<=x<=B/2)
    check(f_float([x,B-2*x,x]) <= f_float([0,B,0])+1e-11)
    for j in range(601):
        xx=B*j/1200
        check(f_float([x,B-2*x,x]) <= f_float([xx,B-2*xx,xx])+1e-10)

# Positive curvature: interval quadratic form is strictly positive for v != 0.
for n in range(2,18):
    qs=[Q((k%5)+1,7) for k in range(n-1)]
    for mode in range(n-1):
        v=[(-1 if k%2 else 2) * (int(k==mode)+1) for k in range(n-1)]
        h=sum((interval_product(qs,i,j)*sum(v[i:j])**2 for i in range(n) for j in range(i+1,n)),Q(0))
        check(h>0)

print('PASS',COUNT,'finite/exact checks')
