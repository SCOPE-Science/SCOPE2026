#!/usr/bin/env python3
"""Exact Walsh verification for sink-free orientations of complete bipartite K(2,n)."""
from math import isqrt


def predicted(n, u, v):
    a = sum(((u >> i) & 1) == 0 and ((v >> i) & 1) == 0 for i in range(n))
    result = ((-1) ** (n - a)) * (3 ** a) + (-1 if ((u.bit_count() + v.bit_count()) & 1) else 1)
    if u == 0:
        result -= (1 << n) * (-1 if (v.bit_count() & 1) else 1)
    if v == 0:
        result -= (1 << n) * (-1 if (u.bit_count() & 1) else 1)
    return result


def enumerate_and_transform(n):
    N = 1 << n
    f = [0] * (N*N)
    support=[]
    for v in range(N):
        for u in range(N):
            if (u | v) != N-1: # every right vertex needs an outgoing arc
                continue
            if u == N-1 or v == N-1: # hubs need outgoing arcs
                continue
            idx = u | (v << n)
            f[idx] = 1
            support.append(idx)
    for j in range(2*n):
        h=1<<j
        for base in range(0,N*N,2*h):
            for k in range(base,base+h):
                x,y=f[k],f[k+h]
                f[k],f[k+h]=x+y,x-y
    return f, support


def main():
    tested=0
    direct=0
    for n in range(1,9):
        N=1<<n
        spectra,support=enumerate_and_transform(n)
        expected_count=0 if n==1 else 3**n-2**(n+1)+1
        assert len(support)==expected_count, (n,len(support),expected_count)
        assert spectra[0] == len(support)
        assert sum(x*x for x in spectra)==(1<<(2*n))*len(support)
        for v in range(N):
            for u in range(N):
                val=spectra[u | (v<<n)]
                assert val==predicted(n,u,v), (n,u,v,val,predicted(n,u,v))
                tested+=1
                if n <= 4:
                    independent = sum(-1 if ((z & (u | (v << n))).bit_count() & 1) else 1 for z in support)
                    assert val == independent, (n,u,v)
                    direct+=1
        zero=spectra.count(0)
        expected_zero = (N*N if n==1 else 8 if n==2 else (3**n-1)//2)
        assert zero==expected_zero, (n,zero,expected_zero)
        if n>=2:
            gap=min(abs(x) for x in spectra if x)
            assert gap==2, (n,gap)
        print(n,len(support),zero,'gap',min((abs(x) for x in spectra if x),default=0))
    print('SINK_FREE_BICLIQUE_FOURIER_EXACT_PASS frequencies=',tested,'independent_sums=',direct)

if __name__ == '__main__': main()
