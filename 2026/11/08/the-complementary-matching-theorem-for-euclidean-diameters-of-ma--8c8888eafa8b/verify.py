"""Exact finite checks for the Euclidean diameter theorem of Marion central polytopes.

Requires Python 3.9+ standard library only; not a substitute for the proof.
"""
from fractions import Fraction as F
from math import comb

checks = 0

def eq(a, b):
    global checks
    checks += 1
    assert a == b, (a, b)

def predicted(n):
    if n % 2 == 0:
        return F(4, 9*n), comb(n, n//2)//2
    return F(36*n*(n*n-1), (9*n*n-1)**2), comb(n, n//2)

def orbit_distance(n, k, l, j):
    # Derived by multiplying the two normalized two-level vectors.
    return (F(n+3*k, (n+k)**2) + F(n+3*l, (n+l)**2)
            - F(2*(n+k+l+j), (n+k)*(n+l)))

def direct_distance(n, s, t):
    k=s.bit_count(); l=t.bit_count()
    a=F(1,n+k); b=F(1,n+l)
    return sum(((2 if s>>i&1 else 1)*a -
                (2 if t>>i&1 else 1)*b)**2 for i in range(n))

# Entire orbit space: all possible sizes and intersection counts, including
# non-minimal intersections, so we independently check exact extremizer types.
for n in range(2, 51):
    mx = F(-1)
    count = 0
    for k in range(1,n):
        for l in range(k,n):
            for j in range(max(0,k+l-n), min(k,l)+1):
                val=orbit_distance(n,k,l,j)
                if val>mx:
                    mx=val
    target, _=predicted(n)
    eq(mx,target)
    for k in range(1,n):
        for l in range(k,n):
            for j in range(max(0,k+l-n), min(k,l)+1):
                val=orbit_distance(n,k,l,j)
                expected=(k+l==n and j==0 and k==n//2 and l==(n+1)//2)
                eq(val==mx, expected)

# Full vertex-pair geometry (without orbit shortcut) for all small dimensions.
for n in range(2, 10):
    all_masks=range(1,(1<<n)-1)
    target, expected_count=predicted(n)
    count=0
    for s in all_masks:
        for t in range(s+1,(1<<n)-1):
            val=direct_distance(n,s,t)
            j=(s&t).bit_count()
            eq(val, orbit_distance(n,s.bit_count(),t.bit_count(),j))
            if val==target:
                count+=1
                eq(s^t, (1<<n)-1)
                eq(abs(s.bit_count()-t.bit_count())<=1, True)
            else:
                eq(val<target, True)
    eq(count,expected_count)

print(f'PASS {checks} exact assertions; entire size/intersection orbit space n=2..50; direct vertex pairs n=2..9')
