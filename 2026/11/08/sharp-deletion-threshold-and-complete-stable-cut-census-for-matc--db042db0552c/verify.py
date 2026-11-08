"""Brute-force independent verification for the matching-deleted bipartite games.
Usage: python3 verify.py. Python standard library only.
"""
from itertools import product
from math import comb


def eq(a, b, t):
    n = len(a)
    for i in range(n):
        aopp = sum(a[i] != b[j] for j in range(n) if i != j or i >= t)
        bopp = sum(b[i] != a[j] for j in range(n) if i != j or i >= t)
        if 2*aopp < n - (i < t) or 2*bopp < n - (i < t):
            return False
    return True


def pred(a, b, t):
    n = len(a)
    if (a == (0,)*n and b == (1,)*n) or (a == (1,)*n and b == (0,)*n):
        return True
    ma = sum(a); mb = sum(b)
    if n%2 == 0:
        return ma == mb == n//2 and all(a[i] == b[i] for i in range(t))
    m = (n-1)//2
    if ma == mb == m+1:
        return all(a[i] == b[i] for i in range(t)) and all(a[i] == b[i] == 0 for i in range(t,n))
    if ma == mb == m:
        return all(a[i] == b[i] for i in range(t)) and all(a[i] == b[i] == 1 for i in range(t,n))
    if ma == m+1 and mb == m:
        if t == n-1:
            return all(a[i] == b[i] for i in range(t)) and a[-1] == 1 and b[-1] == 0
        if t == n:
            return sum(a[i] == 1 and b[i] == 0 for i in range(n)) == 1 and all(a[i] >= b[i] for i in range(n))
    if ma == m and mb == m+1:
        if t == n-1:
            return all(a[i] == b[i] for i in range(t)) and a[-1] == 0 and b[-1] == 1
        if t == n:
            return sum(a[i] == 0 and b[i] == 1 for i in range(n)) == 1 and all(a[i] <= b[i] for i in range(n))
    return False


def count(n,t):
    if n%2 == 0:
        return 2 + sum(comb(t,k)*comb(n-t,n//2-k)**2 for k in range(t+1) if 0 <= n//2-k <= n-t)
    m=(n-1)//2
    return 2 + (2*comb(t,m+1) if t>=m+1 else 0) + (2*comb(n-1,m) if t==n-1 else 0) + (2*n*comb(n-1,m) if t==n else 0)


def cut(a,b,t):
    n=len(a)
    return sum(a[i] != b[j] for i in range(n) for j in range(n) if i != j or i >= t)


def expected_hist(n,t):
    result={n*n-t:2}
    if n%2==0:
        k=n*n//2
        result[k]=result.get(k,0)+count(n,t)-2
    else:
        m=(n-1)//2
        k=(n*n-1)//2
        result[k]=result.get(k,0)+(2*comb(t,m+1) if t>=m+1 else 0)+(2*n*comb(n-1,m) if t==n else 0)
        if t==n-1:
            z=(n*n+1)//2
            result[z]=result.get(z,0)+2*comb(n-1,m)
    return {k:v for k,v in result.items() if v}


def check(n,t):
    E=0; hist={}; nstates=0
    for prof in product((0,1), repeat=2*n):
        a,b=prof[:n],prof[n:]
        actual=eq(a,b,t)
        hypothesis=pred(a,b,t)
        if actual != hypothesis:
            raise AssertionError(('bad profile',n,t,a,b,actual,hypothesis))
        nstates += 1
        if actual:
            E+=1
            c=cut(a,b,t)
            hist[c]=hist.get(c,0)+1
    assert E == count(n,t), ('count',n,t,E,count(n,t))
    assert hist == expected_hist(n,t), ('cut histogram',n,t,hist,expected_hist(n,t))
    return E,hist,nstates

if __name__=='__main__':
    total=0; graphs=0; results=[]
    for n in range(2,9):
        for t in range(n+1):
            E,h,s=check(n,t)
            graphs+=1; total+=s
            if t in (0,n-1,n): results.append((n,t,E,h))
    for result in results: print(*result)
    print(f'VERIFY_OK graphs={graphs} profiles={total}')
