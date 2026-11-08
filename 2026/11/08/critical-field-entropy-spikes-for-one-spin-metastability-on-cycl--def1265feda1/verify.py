#!/usr/bin/env python3
"""Reproducible exact checks of spin-flip stability on circular ladders."""
from itertools import product
from math import isclose, sqrt
from collections import deque

ALPHABET = list(product((-1,1),repeat=2))
PAIRS = list(product(ALPHABET, repeat=2))
N=16

def transfer(t):
    a = [[0]*N for _ in range(N)]
    for i,(prev,cur) in enumerate(PAIRS):
        for nxt in ALPHABET:
            j=PAIRS.index((cur,nxt))
            if all(cur[k]*(t-prev[k]-cur[1-k]-nxt[k])>=0 for k in (0,1)):
                a[i][j] = 1
    return a

def multiply(a,b):
    size=len(a); out=[[0]*size for _ in range(size)]
    for i in range(size):
        for k,x in enumerate(a[i]):
            if x:
                for j,y in enumerate(b[k]):
                    if y: out[i][j]+=x*y
    return out

def trace(a):
    return sum(a[i][i] for i in range(len(a)))

def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def powtrace(a,n):
    cur=eye(len(a))
    for _ in range(n): cur=multiply(cur,a)
    return trace(cur)

def charpoly(a):
    # Exact Faddeev-LeVerrier from power traces.
    n=len(a)
    B=eye(n); coeff=[1]
    for k in range(1,n+1):
        B=multiply(a,B)
        ck=-trace(B)
        assert ck%k==0, (k,ck)
        ck//=k
        coeff.append(ck)
        for i in range(n): B[i][i]+=ck
    return coeff

def polymul(*polys):
    out=[1]
    for p in polys:
        z=[0]*(len(out)+len(p)-1)
        for i,a in enumerate(out):
            for j,b in enumerate(p):z[i+j]+=a*b
        out=z
    return out

def expected_coeff(t):
    # descending-degree coefficients
    if t==0: return polymul([1]+[0]*10,[1,-1],[1,1],[1,-1,-1],[1,1,1])
    if t==1: return polymul([1]+[0]*7,[1,1,2,1],[1,-1,-3,-1,1,1,1])
    if t==2: return polymul([1]+[0]*12,[1,-1,-1],[1,1,1])
    if t==3: return polymul([1]+[0]*13,[1,1],[1,-2,-1])
    if t==4: return polymul([1]+[0]*15,[1,-1])
    raise ValueError(t)

def lucas(n):
    a,b=2,1
    for _ in range(n):a,b=b,a+b
    return a

def pell(n):
    a,b=2,2
    for _ in range(n):a,b=b,2*b+a
    return a

def energy(rungs,t):
    n=len(rungs)
    return sum(rungs[i][k]*rungs[(i+1)%n][k]
               for i in range(n) for k in (0,1)) + sum(
               rungs[i][0]*rungs[i][1] for i in range(n)) - t*sum(
               sum(r) for r in rungs)

def direct_from_hamiltonian(n,t):
    count=0
    for rungs in product(ALPHABET,repeat=n):
        e=energy(rungs,t)
        stable=True
        for i in range(n):
            for k in (0,1):
                changed=[list(r) for r in rungs]
                changed[i][k]*=-1
                if energy(changed,t)<e:
                    stable=False;break
            if not stable: break
        count+=stable
    return count

def direct(n,t):
    count=0
    for rungs in product(ALPHABET,repeat=n):
        valid=True
        for i in range(n):
            prv, cur, nxt = rungs[i-1],rungs[i],rungs[(i+1)%n]
            if not all(cur[k]*(t-prv[k]-cur[1-k]-nxt[k])>=0 for k in (0,1)):
                valid=False;break
        count+=valid
    return count

def is_strong_on(a,nodes):
    z=set(nodes)
    for invert in (False,True):
        adj={i:[j for j in z if (a[j][i] if invert else a[i][j])] for i in z}
        seen=set([min(z)]); queue=deque(seen)
        while queue:
            i=queue.popleft()
            for j in adj[i]:
                if j not in seen:seen.add(j);queue.append(j)
        if seen!=z:return False
    return True

def main():
    matrices={}
    for t in (0,1,2,3,4):
        a=transfer(t); matrices[t]=a
        cp=charpoly(a)
        assert cp==expected_coeff(t),(t,cp,expected_coeff(t))
        for n in range(3,14):
            observed=powtrace(a,n)
            if t==0:target=lucas(n)+1+(-1)**n+(2 if n%3==0 else -1)
            elif t==2:target=lucas(n)+(2 if n%3==0 else -1)
            elif t==3:target=pell(n)+(-1)**n
            elif t==4:target=1
            else:target=observed
            assert observed==target,(t,n,observed,target)
        for n in range(3,9):
            count=direct(n,t)
            assert count==powtrace(a,n),(t,n,count,powtrace(a,n))
        for n in range(3,7):
            assert direct_from_hamiltonian(n,t)==powtrace(a,n), (t,n)
        print('h/J',t,'degree',len(cp)-1,'char',cp,'first', [powtrace(a,n) for n in range(3,8)])
    # distinct comparison to negative fields: brute sign reversal symmetry
    for n in range(3,7):
        for t in (1,2,3):assert direct(n,-t)==direct(n,t)
    # critical field h/J=1 has one cyclic core with 11 states, strongly connected, aperiodic
    a=matrices[1]
    core=[3,5,6,7,9,10,11,12,13,14,15]
    assert is_strong_on(a,core)
    # directed cycles of lengths 2 and 7 in that core, ensuring period one
    for cyc in ([3,12],[3,13,5,6,9,7,12]):
        assert all(a[i][j] for i,j in zip(cyc,cyc[1:]+cyc[:1]))
    # Every cycle uses only core. The complement is acyclic (also excludes self-loops).
    complement=set(range(N))-set(core)
    # power 16 is zero on complement, including paths that leave and reenter? just induced.
    B=[[a[i][j] for j in sorted(complement)] for i in sorted(complement)]
    Z=eye(len(B))
    for _ in range(len(B)): Z=multiply(Z,B)
    assert all(x==0 for row in Z for x in row)
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':main()
