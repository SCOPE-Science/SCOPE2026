#!/usr/bin/env python3
"""Finite-field fiber and Fourier rank checks for reciprocal-power curves."""
import argparse
import cmath
import math
from collections import Counter


def primitive_root(p):
    factors = [q for q in range(2, p) if (p-1) % q == 0 and all(q % r for r in range(2, math.isqrt(q)+1))]
    for g in range(2, p):
        if all(pow(g, (p-1)//q, p) != 1 for q in factors):
            return g
    raise ValueError(p)


def order(a, p):
    return next(j for j in range(1, p) if pow(a, j, p) == 1)


def verify(p, numeric=False):
    assert all(p % q for q in range(2, math.isqrt(p)+1)) and p > 3
    assert p % 9 in (4, 7) and pow(2, (p-1)//3, p) == 1
    m=p-1
    k=m//3 if p%9 == 4 else 2*m//3
    assert k%2 == 0 and k%3 == 1 and math.gcd(k,m)==m//3
    d=(-k-1)%m
    assert 1<=d<=m-1
    H={x for x in range(1,p) if pow(x,k,p)==1}
    assert len(H)==m//3 and 2 in H and p-1 in H
    w=pow(primitive_root(p),m//3,p)
    assert w!=1 and pow(w,3,p)==1 and w not in H
    f=lambda x:x*(1+pow(x,k,p))%p
    fibers={h:[] for h in H}
    for x in range(1,p):
        assert f(x) in H
        fibers[f(x)].append(x)
    inv2=pow(2,-1,p)
    for h,roots in fibers.items():
        assert len(roots)==3
        assert set(roots)=={h*inv2%p,-w*h%p,-w*w*h%p}
    t=order(-2%p,p)
    assert m//3%t==0 and t%3!=0
    # Character labels are defined by chi(g)=exp(2*pi*i*j/m).
    # This exact count checks the cubic root and (-2) phase conditions.
    g=primitive_root(p)
    logs={pow(g,i,p):i for i in range(m)}
    zeros=[j for j in range(m) if (j*logs[-2%p])%m==0 and (j*logs[w])%m !=0]
    assert len(zeros)==2*m//(3*t)
    print(f'p={p} k={k} d={d} ord(-2)={t} nullity={len(zeros)} rank={m-len(zeros)}')
    if numeric:
        import numpy as np
        xx=np.arange(1,p)
        F=np.array([[f((int(x)*int(y))%p) for y in xx] for x in xx],dtype=int)
        M=np.exp(2j*np.pi*F/p)
        singular=np.linalg.svd(M,compute_uv=False)
        nz=int(np.sum(singular>1e-6))
        assert nz==m-len(zeros),(p,nz,len(zeros),singular)
        print(f'  numeric rank={nz}; min nonzero sv={singular[nz-1]:.6g}; max zero sv={singular[nz] if nz<m else 0:.3g}')


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-prime',type=int,default=700)
    args=ap.parse_args()
    passing=[]
    for p in range(7,args.max_prime+1):
        if p%9 in (4,7) and pow(2,(p-1)//3,p)==1 and all(p%q for q in range(2,math.isqrt(p)+1)):
            passing.append(p)
            verify(p,numeric=(p<=80))
    assert len(passing)>=3
    print(f'Checked {len(passing)} admissible primes up to {args.max_prime}: {passing}')

if __name__=='__main__':
    main()
