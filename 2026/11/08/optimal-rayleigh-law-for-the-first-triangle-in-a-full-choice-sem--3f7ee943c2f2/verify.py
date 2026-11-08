"""Standalone finite checks for the semi-random first-triangle theorem.
These are tests, not a proof of the asymptotic statement.
"""
from itertools import combinations
from collections import defaultdict
from math import exp, sqrt
import random


def active_count(n, E):
    adj = [set() for _ in range(n)]
    for a,b in E: adj[a].add(b);adj[b].add(a)
    elig=set()
    for a,b in E:
        for c in adj[b]:
            if c != a and c not in adj[a]:
                elig.add(a); elig.add(c)
        for c in adj[a]:
            if c != b and c not in adj[b]:
                elig.add(b); elig.add(c)
    return len(elig),elig


def has_triangle(n,E):
    adj=[set() for _ in range(n)]
    for a,b in E:adj[a].add(b);adj[b].add(a)
    return any(adj[a]&adj[b] for a,b in E)


def exhaustive_bound():
    tests=0
    for n in range(1,7):
        ee=list(combinations(range(n),2))
        for mask in range(1<<len(ee)):
            es=[edge for i,edge in enumerate(ee) if mask&(1<<i)]
            if has_triangle(n,es):continue
            a,_=active_count(n,es)
            assert 3*a<=4*len(es),(n,es,a)
            tests+=1
    assert active_count(4,[(0,1),(1,2),(2,3)])[0]==4
    assert active_count(3,[(0,1),(1,2)])[0]==2
    return tests


def one_sample(n,maxrounds,rng):
    # All complete P4's are kept intact until the first triangle.
    adj=[set() for _ in range(n)]
    used=set()
    # unfinished path vertices, 0-2 edges; only productive steps count
    cur=[]
    completed=[]
    r=0
    for t in range(maxrounds):
        u=rng.randrange(n)
        # Test whether offered vertex can close any triangle
        closers=[]
        for c in adj[u]:
            for v in adj[c]:
                if v!=u and v not in adj[u]:closers.append(v)
        if closers:
            return t+1, r, len(completed)
        if u in used:
            r+=1
            # Force a simple safe edge to a completely unused vertex
            v=next((v for v in range(n) if v not in used and v!=u), None)
            if v is None:return maxrounds+1,r,len(completed)
            adj[u].add(v);adj[v].add(u); used.add(v)
        else:
            if not cur:
                v=next((v for v in range(n) if v not in used and v!=u),None)
                if v is None: return maxrounds+1,r,len(completed)
                cur=[u,v]
            elif len(cur)==2:
                # extend at the last endpoint
                v=cur[-1];cur.append(u)
            else:
                v=cur[-1];cur.append(u)
                completed.append(tuple(cur))
                cur=[]
            adj[u].add(v);adj[v].add(u);used.add(u);used.add(v)
        if t+1<=maxrounds:
            active, A=active_count(n,[(a,b) for a in range(n) for b in adj[a] if a<b])
            assert active>=4*len(completed)
            assert len(completed)==(t+1-r)//3
            for path in completed:
                assert set(path)<=A
    return maxrounds+1,r,len(completed)


def simulate():
    rng=random.Random(317041)
    n=2000
    trials=420
    xs=(.5,1.,1.5)
    cap=int(max(xs)*sqrt(n))
    data=[one_sample(n,cap,rng)[0] for _ in range(trials)]
    out=[]
    for x in xs:
        m=int(x*sqrt(n))
        surv=sum(d>m for d in data)/trials
        expected=exp(-2*(m/sqrt(n))**2/3)
        # broad, 3--4 standard errors, intended only as a check
        assert abs(surv-expected)<.14,(x,surv,expected)
        out.append((x,m,surv,expected))
    return out

if __name__=='__main__':
    total=exhaustive_bound()
    print('Exhaustive labeled triangle-free graphs checked:',total)
    print('Seeded P4-strategy simulations (x, rounds, survival, limit):')
    for item in simulate():print(item)
    print('ALL CHECKS PASSED')
