"""Standard-library checks for a one-sided tie-retaining plurality cellular automaton.
Usage: python3 verify.py
"""
from itertools import product
from collections import Counter
from math import isclose

def step(x):
    n=len(x)
    return tuple(x[(i+1)%n] if x[(i+1)%n]==x[(i+2)%n] else x[i] for i in range(n))

def proper(x):
    return all(x[i]!=x[(i+1)%len(x)] for i in range(len(x)))

def thick(x):
    n=len(x)
    return all(x[i-1]==x[i] or x[i]==x[(i+1)%n] for i in range(n))

def longest_transient(x):
    seen={}; y=x
    while y not in seen:
        seen[y]=len(seen)
        y=step(y)
    return seen[y], len(seen)-seen[y],y

def trace_stable(q,n):
    states=list(product(range(q),repeat=2))
    N=len(states); M=[[0]*N for _ in states]
    index={x:i for i,x in enumerate(states)}
    for i,(a,b) in enumerate(states):
        for c in range(q):
            if a==b or b==c: M[i][index[b,c]]=1
    R=[[int(i==j) for j in range(N)] for i in range(N)]
    for _ in range(n):
        R=[[sum(R[i][k]*M[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
    return sum(R[i][i] for i in range(N))

def closed(q,n):
    # Exact spectral power sums with integer recurrence; complex roots not needed.
    def power_seq(c,n):
        a,b=2,1
        if n==0:return a
        if n==1:return b
        for j in range(2,n+1): a,b=b,b+c*a
        return b
    u=[2,1,-1,-2,-1,1][n%6]  # 2 cos(n*pi/3)
    return power_seq(q-1,n)+(q-1)*u

checks=0
for q,nmax in [(2,11),(3,10),(4,8),(5,7)]:
    for n in range(3,nmax+1):
        r=0; p=0; m=0; worst=0; bad=[]; periods=Counter();
        for x in product(range(q),repeat=n):
            t,d,y=longest_transient(x)
            worst=max(worst,t)
            assert t<=n-2 or q==2,(q,n,x,t)
            assert proper(y) or thick(y),(q,n,x,y)
            assert step(y)==y if proper(y) else step(y)==y[1:]+y[:1],(q,n,x,y)
            if proper(x):assert t==0
            if (not proper(x)) and q>=3:assert thick(y),(q,n,x,y)
            if t==0:r+=1; periods[d]+=1
            if thick(x):m+=1
            if proper(x):p+=1
            checks+=1
        assert p==(q-1)**n + (q-1)*(-1)**n,(q,n,p)
        assert m==closed(q,n)==trace_stable(q,n),(q,n,m,closed(q,n),trace_stable(q,n))
        assert r==p+m,(q,n,r,p,m)
        if q>=3:assert worst==n-2,(q,n,worst)
        print(f'q={q}, n={n}: frozen={p}, traveling={m}, recurrent={r}, max_entry={worst}, periods={dict(periods)}')
print('PASS',checks,'complete initial configurations')
