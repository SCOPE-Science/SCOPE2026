#!/usr/bin/env python3
"""Finite reproducibility checks for central trinomial congruences."""
from math import comb

def coefficients(N):
    t = [1, 1]
    for n in range(1, N):
        numerator = (2*n+1)*t[-1] + 3*n*t[-2]
        assert numerator % (n+1) == 0
        t.append(numerator//(n+1))
    return t

def main():
    nmax = 2048
    t=coefficients(nmax)
    for n in range(101):
        exact=sum(comb(n,2*j)*comb(2*j,j) for j in range(n//2+1))
        assert t[n]==exact
    assert all(v&1 for v in t)
    levels=10
    for k in range(1, levels+1):
        mod=1<<k
        observed={v%mod for v in t}
        # The full-coverage check is empirical, not the proof.
        if k<=8: assert observed == set(range(1,mod,2)), (k,len(observed))
        for r in range(max(1,k),11):
            if 1<<r > nmax-1: break
            assert (t[1<<r]-t[1<<(r-1)]) % (1<<r)==0
            max_m=min((1<<(r-k+1))-1,nmax-1-(1<<r))
            for m in range(max(0,max_m)+1):
                assert (t[(1<<r)+m]-t[1<<r]*t[m])%mod==0,(k,r,m)
    # The abstract limit has the predicted cyclic subgroup at finite precision.
    for k in range(3,11):
        mod=1<<k
        L=t[1<<min(10,k)]%mod
        assert L%8==3
        order=1<<(k-2)
        assert pow(L,order,mod)==1
        assert (k==3 or pow(L,order//2,mod)!=1)
        attained={pow(L,j,mod) for j in range(order)}
        attained |= {(7*z)%mod for z in list(attained)}
        assert attained==set(range(1,mod,2))
    print('VERIFY_OK formula_n=0..100 parity_n=0..2048 block_k=1..10 residue_levels=1..8 cyclic_k=3..10')

if __name__=='__main__':
    main()
