#!/usr/bin/env python3
"""Exact initial period-three census for the second power of a cycle.
Requires Python 3 and SymPy. All entries and comparisons are integers.
"""
from itertools import product
from sympy import Matrix, Symbol, factor

colors = list(product(range(3), repeat=4))
index = {s: i for i, s in enumerate(colors)}
T = [[0]*81 for _ in range(81)]
for a,b,c,d in colors:
    for e in range(3):
        if any(v == (c+1)%3 for v in (a,b,d,e)):
            T[index[(a,b,c,d)]][index[(b,c,d,e)]] += 1

z=Symbol('z')
observed = factor(Matrix(T).charpoly(z).as_expr())
expected = z**69*(z+1)*(z**3-3*z**2+2*z-2)*(z**4+z**3+2*z**2+3*z+4)**2
assert (observed-expected).expand()==0
print('CHARACTERISTIC POLYNOMIAL:',observed)

# Independently evaluate traces by dynamic programming on directed paths.
succ=[[(j, v) for j,v in enumerate(row) if v] for row in T]
def trace_power(k):
    total=0
    for root in range(81):
        v=[0]*81;v[root]=1
        for _ in range(k):
            w=[0]*81
            for i, ni in enumerate(v):
                if ni:
                    for j,m in succ[i]:w[j]+=ni*m
            v=w
        total+=v[root]
    return total

def power_sums(c,k):
    d=len(c);s=[d]
    for n in range(1,k+1):
        x=-(sum(c[j-1]*s[n-j] for j in range(1,min(d,n-1)+1)) + (n*c[n-1] if n<=d else 0))
        s.append(x)
    return s
s3=power_sums([-3,2,-2],22)
s4=power_sums([1,2,3,4],22)
for n in range(5,19):
    formula=(-1)**n+s3[n]+2*s4[n]
    tr=trace_power(n)
    assert tr==formula,(n,tr,formula)
    print('n=%2d trace=%d formula=%d'%(n,tr,formula))
print('EXACT TRANSFER / TRACE CHECKS PASSED')
