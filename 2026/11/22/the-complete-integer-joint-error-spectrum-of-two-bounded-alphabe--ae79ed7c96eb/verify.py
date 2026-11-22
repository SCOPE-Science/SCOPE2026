#!/usr/bin/env python3
"""Finite checks of a joint functional-dependency error spectrum.

Only uses the Python standard library. Executable enumeration is not a proof
for unbounded parameters; the accompanying result gives an integer-flow proof.
"""
import itertools
import math
import random
from collections import defaultdict, deque


def bound(n, b, c, p, q):
    A, B = n-p, n-q
    m0 = max(A+B-n, (A+c-1)//c, (B+b-1)//b,
             (n+b*c-1)//(b*c))
    return max(p,q), n-m0


def table_errors(a, b, c):
    n = sum(a)
    rows = [sum(a[i*c:(i+1)*c]) for i in range(b)]
    cols = [sum(a[i*c+j] for i in range(b)) for j in range(c)]
    return n-max(rows), n-max(cols), n-max(a)


def weak_compositions(n, k):
    # Stars-and-bars, intentionally independent of the formula to be checked.
    for separators in itertools.combinations(range(n+k-1), k-1):
        marks = (-1,) + separators + (n+k-1,)
        yield tuple(marks[j+1]-marks[j]-1 for j in range(k))


def exhaustive(b, c, nmax):
    count = 0
    for n in range(1, nmax+1):
        possible = defaultdict(set)
        for table in weak_compositions(n, b*c):
            p, q, r = table_errors(table, b, c)
            possible[p,q].add(r)
            lo, hi = bound(n,b,c,p,q)
            assert lo <= r <= hi, (n,b,c,p,q,r,lo,hi)
            count += 1
        for p in range(n-(n+b-1)//b+1):
            for q in range(n-(n+c-1)//c+1):
                lo, hi = bound(n,b,c,p,q)
                actual = possible.get((p,q),set())
                expect = set(range(lo,hi+1))
                assert actual == expect, (n,b,c,p,q,sorted(actual),lo,hi)
    return count


class Flow:
    def __init__(self, count):
        self.g=[[] for _ in range(count)]
    def add(self,u,v,cap):
        f=[v,cap,None]
        r=[u,0,f]
        f[2]=r
        self.g[u].append(f); self.g[v].append(r)
        return f
    def max_flow(self,s,t):
        total=0
        while True:
            prev=[None]*len(self.g)
            prev[s]=(s,None)
            Q=deque([s])
            while Q and prev[t] is None:
                u=Q.popleft()
                for e in self.g[u]:
                    if e[1] and prev[e[0]] is None:
                        prev[e[0]]=(u,e)
                        Q.append(e[0])
                        if e[0]==t:break
            if prev[t] is None:return total
            d=10**30;v=t
            while v!=s:
                u,e=prev[v];d=min(d,e[1]);v=u
            v=t
            while v!=s:
                u,e=prev[v];e[1]-=d;e[2][1]+=d;v=u
            total+=d


def witness(n,b,c,p,q,m):
    # Integer feasible circulation with lower/upper capacities; no MILP solver.
    A,B=n-p,n-q
    s=0; t=1; rows=list(range(2,2+b)); cols=list(range(2+b,2+b+c))
    SS=2+b+c; TT=SS+1
    fl=Flow(TT+1)
    demand=[0]*(TT+1)
    cells={}
    def edge(u,v,l,h):
        assert 0<=l<=h
        e=fl.add(u,v,h-l)
        demand[u]-=l;demand[v]+=l
        return (e,h-l,l)
    for i,x in enumerate(rows): edge(s,x,A if i==0 else 0,A)
    for i,x in enumerate(rows):
        for j,y in enumerate(cols):
            l=m if (i,j)==(0,0) else 0
            cells[i,j]=edge(x,y,l,m)
    for j,y in enumerate(cols):edge(y,t,B if j==0 else 0,B)
    edge(t,s,n,n)
    need=0
    for i,d in enumerate(demand):
        if d>0: fl.add(SS,i,d);need+=d
        elif d<0: fl.add(i,TT,-d)
    if fl.max_flow(SS,TT)!=need:return None
    a=[]
    for i in range(b):
        for j in range(c):
            e,initial,lower=cells[i,j]
            a.append(lower+initial-e[1])
    assert sum(a)==n and max(a)==m and table_errors(a,b,c)==(p,q,n-m)
    return a


def constructed_tests():
    rng=random.Random(112583)
    checked=0
    for b in range(2,8):
        for c in range(2,8):
            for n in (1,2,3,7,12,25,40):
                for z in range(8):
                    p=rng.randrange(n-(n+b-1)//b+1)
                    q=rng.randrange(n-(n+c-1)//c+1)
                    A,B=n-p,n-q
                    m0=n-bound(n,b,c,p,q)[1]
                    candidates={m0,min(A,B),rng.randint(m0,min(A,B))}
                    for m in candidates:
                        assert witness(n,b,c,p,q,m) is not None,(n,b,c,p,q,m)
                        checked+=1
    return checked


def multi_fiber_tests():
    rng=random.Random(42565)
    checked=0
    for _ in range(10000):
        b=rng.randrange(1,6)
        c=rng.randrange(1,6)
        fibers=rng.randrange(1,8)
        n=p=q=r=0
        for unused in range(fibers):
            a=[rng.randrange(0,6) for _ in range(b*c)]
            if not any(a):continue
            ni=sum(a)
            pi,qi,ri=table_errors(a,b,c)
            n+=ni;p+=pi;q+=qi;r+=ri
        if not n:continue
        lo,hi=bound(n,b,c,p,q)
        assert lo<=r<=hi,(n,b,c,p,q,r,lo,hi)
        checked+=1
    return checked


def main():
    checked=0
    for b,c,nmax in ((1,1,12),(1,3,10),(3,1,10),(2,2,18),(2,3,14),(3,3,10),(3,4,8),(4,4,6)):
        checked+=exhaustive(b,c,nmax)
    flow=constructed_tests()
    multi=multi_fiber_tests()
    print(f'VERIFY_OK exhaustive_tables={checked} constructed_instances={flow} multi_fiber_tests={multi}')

if __name__=='__main__':main()
