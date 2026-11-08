#!/usr/bin/env python3
"""Exact independent integer checks for a fixed-weight cyclic-track theorem.
Standard-library only; run: python3 verify.py
This is finite verification; the all-parameter proof is in RESULT.md.
"""
from collections import defaultdict
from itertools import combinations, product
from math import comb, factorial, gcd


def masks(n, k):
    for supp in combinations(range(n), k):
        chosen = set(supp)
        yield tuple(int(i in chosen) for i in range(n))


def rotations(x):
    return {x[i:] + x[:i] for i in range(len(x))}


def support_orbits(n, k):
    remaining = set(masks(n, k))
    while remaining:
        rep = min(remaining)
        orbit = rotations(rep)
        remaining -= orbit
        yield rep, len(orbit)


def matrix_determinant(M):
    """Fraction-free Bareiss determinant with exact pivoting."""
    A = [list(row) for row in M]
    n = len(A)
    if n == 0:
        return 1
    sign = 1
    den = 1
    for k in range(n-1):
        if A[k][k] == 0:
            j = next((j for j in range(k+1,n) if A[j][k] != 0),None)
            if j is None:
                return 0
            A[k],A[j] = A[j],A[k]
            sign = -sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                top=A[i][j]*piv-A[i][k]*A[k][j]
                assert top%den==0
                A[i][j]=top//den
            A[i][k]=0
        den=piv
    return sign*A[-1][-1]


def graph(q,n,k,rep):
    pat_orbit=rotations(rep)
    E=[]
    for word in product(range(q),repeat=n):
        sup=tuple(int(t!=0) for t in word)
        if sup in pat_orbit:
            E.append((word[:-1],word[1:],word))
    V=sorted({w for e in E for w in e[:2]})
    index={w:i for i,w in enumerate(V)}
    d=[0]*len(V); incoming=[0]*len(V)
    lap=[[0]*len(V) for _ in V]
    for tail,head,_ in E:
        i=index[tail];j=index[head]
        d[i]+=1;incoming[j]+=1
        lap[i][i]+=1
        lap[i][j]-=1
    assert d==incoming
    return V,E,lap,d


def euler_cyclic_count(E):
    """Brute-force cyclic Euler tours, anchoring the unique first edge."""
    bytail=defaultdict(list)
    for i,(u,v,w) in enumerate(E):
        bytail[u].append(i)
    start=0; first=E[0]
    def dfs(v,used):
        if used.bit_count()==len(E):
            return int(v==first[0])
        ans=0
        for j in bytail[v]:
            if not used>>j&1:
                ans+=dfs(E[j][1],used|(1<<j))
        return ans
    return dfs(first[1],1<<start)


def totient(d):
    return sum(gcd(j,d)==1 for j in range(1,d+1))

def verify(q,n,k,brute=False):
    s=q-1
    orbits=list(support_orbits(n,k))
    ne=len(orbits)
    predicted_ne=sum(totient(d)*comb(n//d,k//d)
                     for d in range(1,gcd(n,k)+1) if gcd(n,k)%d==0)//n
    assert ne==predicted_ne
    got_a=0; product_cycles=1
    for rep,h in orbits:
        V,E,L,d=graph(q,n,k,rep)
        assert h*k%n==0
        a=h*k//n
        got_a+=a
        assert len(E)==h*s**k
        assert len(V)==(h-a)*s**k+a*s**(k-1)
        tau=matrix_determinant([row[:-1] for row in L[:-1]])
        expected_tau=s**(a*s**(k-1)-k)
        assert tau==expected_tau,(q,n,k,rep,tau,expected_tau)
        val=tau
        for degree in d:
            val*=factorial(degree-1)
        expected_count=s**(a*s**(k-1)-k)*factorial(s-1)**(a*s**(k-1))
        assert val==expected_count
        if brute:
            if len(E)<=16:
                brute_count=euler_cyclic_count(E)
                assert brute_count==val,(rep,brute_count,val)
        product_cycles*=val
    assert got_a==comb(n-1,k-1)
    expected_all=(s**(s**(k-1)*comb(n-1,k-1)-k*ne)
                  *factorial(s-1)**(s**(k-1)*comb(n-1,k-1)))
    assert product_cycles==expected_all
    print('PASS',dict(q=q,n=n,k=k,necklaces=ne,cycles=product_cycles,arborescences='exact',brute=brute))


if __name__=='__main__':
    tasks=[(2,5,3,True),(3,3,2,True),(3,3,3,True),
           (3,4,2,False),(3,4,3,False),(3,4,4,False),
           (3,5,3,False),(3,6,3,False),(4,3,2,False),
           (4,3,3,False),(4,4,2,False),(4,4,3,False)]
    for q,n,k,brute in tasks:
        verify(q,n,k,brute)
    print('ALL EXACT CHECKS PASSED')
