#!/usr/bin/env python3
"""Exact independent exhaustive verification of first Walsh coefficients on Dyck paths."""
from math import comb

def catalan(n):
    return comb(2*n,n)//(n+1)

def tally(n):
    # Generate Dyck words recursively, not by the first-band Catalan identity.
    counts=[0]*(2*n); total=0
    def dfs(pos,height,ups,mask):
        nonlocal total
        if pos==2*n:
            assert height==0 and ups==n
            total+=1
            for j in range(2*n):counts[j]+=(mask>>j)&1
            return
        if ups<n:dfs(pos+1,height+1,ups+1,mask|(1<<pos))
        if height>0:dfs(pos+1,height-1,ups,mask)
    dfs(0,0,0,0)
    return total, counts

def test():
    total_modes=0
    for n in range(1,11):
        total,U=tally(n)
        assert total==catalan(n)
        g=[catalan(j-1)*catalan(n-j) for j in range(1,n+1)]
        assert sum(g)==total
        A=[0]
        for x in g:A.append(A[-1]+x)
        for j in range(1,n+1):
            assert U[2*j-2]==total-A[j-1],(n,j,'odd')
            assert U[2*j-1]==total-A[j],(n,j,'even')
        W=[total-2*x for x in U]
        zeros=[i+1 for i,v in enumerate(W) if v==0]
        assert zeros==([n,n+1] if n%2==0 else []),(n,zeros)
        if n%2:
            expected=catalan((n-1)//2)**2
        else:
            m=n//2
            expected=2*catalan(m-1)*catalan(m)
        assert min(abs(v) for v in W if v)!=0
        assert min(abs(v) for v in W if v)==expected,(n,'gap')
        total_modes+=2*n
    print('PASS: all positional Walsh coefficients, zero positions, sharp nonzero gap')
    print('Semilengths 1..10, first-order multipliers checked:',total_modes)
if __name__=='__main__':test()
