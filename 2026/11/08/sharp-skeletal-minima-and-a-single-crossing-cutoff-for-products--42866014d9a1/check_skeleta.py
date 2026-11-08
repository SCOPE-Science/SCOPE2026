"""Exact Q(sqrt(3)) coefficient checks for products of planar triangles.

This is a finite reproducibility test only, not a substitute for the all-m proof.
Standard library only: python check_skeleta.py
"""
from math import comb


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def mul(a, b):
    return (a[0]*b[0]+3*a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def sign(a):
    p, q = a
    if q == 0:
        return (p > 0)-(p < 0)
    if p == 0:
        return (q > 0)-(q < 0)
    if p > 0 and q > 0:
        return 1
    if p < 0 and q < 0:
        return -1
    if p > 0:
        return (p*p > 3*q*q)-(p*p < 3*q*q)
    return (3*q*q > p*p)-(3*q*q < p*p)


def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def scale(a, s):
    return (a[0]*s, a[1]*s)


def poly_mul(a, b):
    c = [(0,0)]*(len(a)+len(b)-1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] = add(c[i+j], mul(ai, bj))
    return c


def main():
    h = [(0,3), (0,6), (3,0)]  # 3sqrt(3)+6sqrt(3)t+3t^2
    c = [(1,0)]
    cutoffs = []
    num_checks=0
    for m in range(1,31):
        c=poly_mul(c,h)
        N=2*m
        ratios=[]
        for k in range(N+1):
            d=sub(c[k],(4**m*comb(N,k),0))
            ratios.append(sign(d))
            num_checks+=1
        assert ratios[0]==1 and ratios[1]==1 and ratios[-1]==-1
        assert all(ratios[k]>=ratios[k+1] for k in range(len(ratios)-1))
        K=max(k for k,r in enumerate(ratios) if r>=0)
        if m>=2: assert K>=2
        # R_k>=R_{k+1}, strict for k>=1, with exact comparisons
        assert sign(sub(scale(c[0],comb(N,1)),scale(c[1],comb(N,0))))==0
        for k in range(1,N):
            diff=sub(scale(c[k],comb(N,k+1)),scale(c[k+1],comb(N,k)))
            assert sign(diff)>0
            num_checks+=1
        cutoffs.append(K)
    assert cutoffs[:8]==[1,2,4,5,7,8,9,11]
    assert c[0][0]>0
    # In dimension four, Phi_2=108+18sqrt(3) >96; Phi_1=36sqrt(3)<64.
    c2=poly_mul(h,h)
    assert c2[2]==(108,18) and c2[3]==(0,36)
    assert sign(sub(c2[2],(96,0)))>0
    assert sign(sub(c2[3],(64,0)))<0
    print('EXACT_COEFFICIENT_CHECK_OK', 'm=1..30', 'checks=', num_checks)
    print('cutoff K_m for m=1..12:',cutoffs[:12])

if __name__=='__main__':
    main()
