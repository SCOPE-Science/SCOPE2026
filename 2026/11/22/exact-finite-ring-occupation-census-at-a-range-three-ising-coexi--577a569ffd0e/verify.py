"""Exact supplementary checks for a range-three binary ring at its field crossing."""
from collections import defaultdict
from math import comb, isclose

def energy(bits):
    n = len(bits)
    equal = sum(bits[i] == bits[(i+d) % n] for i in range(n) for d in (1, 2, 3))
    return 3 * equal - 10 * sum(bits)

def polynomial(n):
    out = defaultdict(int)
    for a in range(n//4+1):
        if (n-4*a)%5:
            continue
        b=(n-4*a)//5
        t=a+b
        out[3*t]+=n*comb(t,a)//t
    return dict(out)

pot = [0,-3,-4,-9,-7,-10,-11,-12]
tight = set()
for a in range(8):
    oldest, middle, newest = a&1, (a>>1)&1, (a>>2)&1
    for b in range(2):
        j = a//2 + 4*b
        w = 3*(int(oldest==b)+int(middle==b)+int(newest==b))-10*b+3
        assert w >= pot[j]-pot[a]
        if w == pot[j]-pot[a]: tight.add((a,j))
assert tight == {(0,4),(1,4),(3,1),(3,5),(4,6),(5,2),(5,6),(6,7),(7,3)}
# Characterization of equality walks: the transient states 0 and 2 cannot be in a closed tight walk;
# the remaining graph consists of two loops based at vertex 3, of lengths 4 and 5.
for n in range(7,20):
    out=defaultdict(int)
    mn=10**9
    for code in range(1<<n):
        bits=[(code>>i)&1 for i in range(n)]
        e=energy(bits)
        if e < mn:
            mn=e; out.clear()
        if e == mn: out[sum(bits)] += 1
    expected=polynomial(n)
    assert mn>=-3*n
    if expected:
        assert mn == -3*n and dict(out)==expected, (n,mn,dict(out),expected)
    else:
        assert mn > -3*n, (n,mn)
# Independent counting of tight walks by a six-state matrix: trace of its n-th power.
vertices=(1,3,4,5,6,7)
idx={v:i for i,v in enumerate(vertices)}
A=[[int((u,v) in tight) for v in vertices] for u in vertices]
def mul(X,Y):
    m=len(X)
    return [[sum(X[i][k]*Y[k][j] for k in range(m)) for j in range(m)] for i in range(m)]
P=[[int(i==j) for j in range(6)] for i in range(6)]
for n in range(1,151):
    P=mul(P,A)
    assert sum(P[i][i] for i in range(6))==sum(polynomial(n).values()),n
print('ALL_RANGE3_EXACT_CHECKS_PASSED', 13+150)
