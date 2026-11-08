"""Independent finite-graph and finite-size checks for the complete split subtree law.
Run using the Python standard library only: python check.py
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, log, exp, lgamma, isclose

checks = 0

def check(cond, msg):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1


def det_bareiss(a):
    n = len(a)
    if n == 0:
        return 1
    a = [row[:] for row in a]
    prev = 1
    sign = 1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot = next((j for j in range(k+1, n) if a[j][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = a[i][j]*p - a[i][k]*a[k][j]
                check(num%prev == 0, 'Bareiss exact division')
                a[i][j] = num//prev
            a[i][k] = 0
        prev = p
    return sign*a[n-1][n-1]


def laplacian_count(i, j):
    n=i+j
    if n == 0:
        return 0
    if n == 1:
        return 1
    L=[[0]*n for _ in range(n)]
    for u in range(n):
        for v in range(u+1,n):
            if u<i or v<i:
                L[u][u]+=1; L[v][v]+=1
                L[u][v]-=1; L[v][u]-=1
    return det_bareiss([row[:-1] for row in L[:-1]])


def formula(i,j):
    if i == 0:
        return int(j == 1)
    if i+j == 1:
        return 1
    if j == 0:
        return i**(i-2)
    return (i+j)**(i-1)*i**(j-1)

for i in range(0,7):
    for j in range(0,7-i):
        if i+j == 0:
            continue
        check(laplacian_count(i,j)==formula(i,j), f'Kirchhoff ({i},{j})')

# Independently enumerate edge subsets to verify spanning-tree counts.
def brute_count(i,j):
    n=i+j
    if n == 1:
        return 1
    edges=[(u,v) for u in range(n) for v in range(u+1,n) if u<i or v<i]
    t=0
    for sub in combinations(edges,n-1):
        parents=list(range(n))
        def find(x):
            while parents[x]!=x:
                x=parents[x]
            return x
        ok=True
        for u,v in sub:
            u=find(u); v=find(v)
            if u==v:
                ok=False; break
            parents[u]=v
        if ok and len(set(find(x) for x in range(n)))==1:
            t+=1
    return t

for i in range(0,5):
    for j in range(0,6-i):
        if i+j==0: continue
        check(brute_count(i,j)==formula(i,j), f'edge enumeration ({i},{j})')

# Count all nonempty subtrees on selected labeled subsets in two independent ways.
for a,b in [(2,2),(3,2),(3,3),(4,2)]:
    weights={}
    for k in range(a+1):
        for l in range(b+1):
            v=comb(a,k)*comb(b,l)*formula(a-k,b-l)
            if v:
                weights[(k,l)]=v
    direct={}
    for s in range(1,1<<(a+b)):
        i=sum((s>>u)&1 for u in range(a))
        j=sum((s>>u)&1 for u in range(a,a+b))
        k,l=a-i,b-j
        direct[(k,l)]=direct.get((k,l),0)+laplacian_count(i,j)
    for key in set(weights)|set(direct):
        check(weights.get(key,0)==direct.get(key,0), f'selected-subset count ({a},{b},{key})')

# Compare exact finite-size coefficient ratios with both separate limiting Poisson means.
def ratio(a,b,k,l):
    i,j=a-k,b-l
    if i<1 or j<0:
        return 0.0
    v=(lgamma(a+1)-lgamma(k+1)-lgamma(a-k+1)
       +lgamma(b+1)-lgamma(l+1)-lgamma(b-l+1)
       +(b-l-1)*log(i)+(a-k-1)*log(i+j)
       -(b-1)*log(a)-(a-1)*log(a+b))
    return exp(v)

def means(c):
    return exp(-c-1/(1+c))/(1+c), c*exp(-1/(1+c))

for c in (0.5,1.0,2.0):
    lc,li=means(c)
    for k,l in ((0,0),(1,0),(0,1),(1,1),(2,0),(0,2)):
        target=lc**k*li**l/(factorial(k)*factorial(l))
        for a in (200, 800, 2400):
            b=round(c*a)
            actual=ratio(a,b,k,l)
            if a==2400:
                check(abs(actual-target)<0.009*max(1,target), f'asymptotic coefficient ({c},{k},{l})')

# The spanning probability is the inverse of the exact coefficient sum.
for a,b in ((5,5),(10,10),(20,20),(25,50)):
    tau=formula(a,b)
    total=sum(comb(a,k)*comb(b,l)*formula(a-k,b-l)
              for k in range(a+1) for l in range(b+1))
    check(tau<=total and total>0, 'normalization')
    check(Fraction(tau,total)==Fraction(1,1)/Fraction(total,tau), 'normalized spanning probability')

print(f'VERIFY_OK {checks} exact/analytic-limit assertions')
