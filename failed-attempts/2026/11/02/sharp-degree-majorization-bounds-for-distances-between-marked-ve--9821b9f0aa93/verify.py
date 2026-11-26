#!/usr/bin/env python3
"""Exact checks for fixed-degree labeled-tree marked-distance tails.
Runs without third-party packages; the proof for arbitrary size is mathematical.
"""
from collections import defaultdict
from itertools import product
from math import factorial
from fractions import Fraction


def fall(n, k):
    ans = 1
    for j in range(k):
        ans *= n - j
    return ans


def esym(vector):
    e = [1] + [0] * len(vector)
    for x in vector:
        for k in range(len(vector), 0, -1):
            e[k] += x * e[k-1]
    return e


def formula(n, deg, u=0, v=1):
    N = n-2
    b = [deg[i]-1 for i in range(n) if i not in (u, v)]
    e = esym(b)
    return tuple(Fraction(factorial(k)*e[k], fall(N, k)) for k in range(N+1))


def decode_prufer(code, n):
    deg = [1] * n
    for a in code:
        deg[a] += 1
    edges=[]
    for a in code:
        leaf=next(i for i in range(n) if deg[i]==1)
        edges.append((leaf, a))
        deg[leaf]-=1
        deg[a]-=1
    rem = [i for i in range(n) if deg[i]==1]
    edges.append((rem[0], rem[1]))
    return edges


def distance(edges, n, u=0, v=1):
    adj=[[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b); adj[b].append(a)
    seen={u}; q=[(u,0)]
    for x,d in q:
        if x==v: return d
        for y in adj[x]:
            if y not in seen:
                seen.add(y); q.append((y,d+1))
    raise AssertionError('Not connected')


def weak_comps(total, length):
    if length==0:
        if total==0: yield ()
        return
    if length==1:
        yield (total,)
        return
    for k in range(total+1):
        for remainder in weak_comps(total-k, length-1):
            yield (k,)+remainder


def main():
    checks=0
    for n in range(2,9):
        groups=defaultdict(lambda: defaultdict(int))
        for seq in product(range(n), repeat=max(0,n-2)):
            edges=decode_prufer(seq,n)
            deg=[1]*n
            for label in seq:deg[label]+=1
            d=distance(edges,n)
            groups[tuple(deg)][d]+=1
        for deg, counts in groups.items():
            size=sum(counts.values())
            tails=formula(n,deg)
            for k,prob in enumerate(tails):
                actual=Fraction(sum(v for d,v in counts.items() if d>k),size)
                assert actual==prob, (n,deg,k,actual,prob)
                checks+=1
    print('Prüfer exact group tail assertions:',checks)
    transfers=0
    for N in range(2,9):
        for s in range(N+1):
            for b in weak_comps(s,N):
                eb=esym(b)
                for i in range(N):
                    for j in range(N):
                        if i==j or b[i]<b[j]+2:continue
                        other=list(b);other[i]-=1;other[j]+=1
                        eo=esym(other)
                        rest=[b[z] for z in range(N) if z not in (i,j)]
                        er=esym(rest)
                        for k in range(N+1):
                            expected=(b[i]-b[j]-1)*(er[k-2] if 2<=k<=N else 0)
                            assert eo[k]-eb[k]==expected,(N,s,b,i,j,k)
                            if k==2: assert eo[k]>eb[k]
                            transfers+=1
    print('All Robin-Hood e_k identity assertions:', transfers)
    extremes=0
    for N in range(1,10):
        for s in range(N+1):
            lower=(s,)+(0,)*(N-1)
            upper=(1,)*s+(0,)*(N-s)
            lo=esym(lower);hi=esym(upper)
            for b in weak_comps(s,N):
                ev=esym(b)
                for k in range(N+1):
                    assert lo[k]<=ev[k]<=hi[k],(N,s,b,k)
                    extremes+=1
                ave=Fraction(1,1)+sum((Fraction(factorial(k)*ev[k],fall(N,k)) for k in range(1,N+1)),Fraction(0,1))
                assert Fraction(1,1)+Fraction(s,N)<=ave<=Fraction(N+1,N-s+1)
                extremes+=1
    print('All sharp-extrema and mean assertions:',extremes)
    print('TOTAL EXACT ASSERTIONS:',checks+transfers+extremes)


if __name__=='__main__': main()
