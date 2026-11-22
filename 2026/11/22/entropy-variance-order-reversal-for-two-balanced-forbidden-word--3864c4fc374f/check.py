#!/usr/bin/env python3
"""Independent rational certificates for fluctuation comparison in binary exclusion shifts.
Only Python standard library is used. No external data are needed.
"""
from fractions import Fraction as Q
from itertools import product


def eval_f(k, q, kind):
    a = Q(1,4**k)
    if kind == 'unbordered':
        return q - 1 - a*q**(2*k)
    if kind == 'alternating':
        return q - 1 - a*q**(2*k+1)*(1-q/4)
    raise ValueError(kind)


def bracket(k, kind, steps=44):
    a=Q(1,4**k)
    lo,hi=Q(1),Q(1)+2*a
    assert eval_f(k,lo,kind)<0 and eval_f(k,hi,kind)>0
    # F is increasing in the displayed root interval:
    # unbordered F'(q) >=1-2ka(1+2a)^(2k-1)>0,
    # alternating F'(q)>=1-(2k+1)a(1+2a)^(2k)>0.
    if kind=='unbordered':
        assert 1-2*k*a*hi**(2*k-1)>0
    else:
        assert 1-(2*k+1)*a*hi**(2*k)>0
    for _ in range(steps):
        mid=(lo+hi)/2
        if eval_f(k,mid,kind)<0:lo=mid
        else:hi=mid
    assert eval_f(k,lo,kind)<0 and eval_f(k,hi,kind)>0
    return lo,hi


def variance_bounds(k, kind):
    lo,hi=bracket(k,kind)
    if kind=='unbordered':
        def fun(q):
            u=q-1
            return Q(1,4) + k*u/(2*(1-(2*k-1)*u))
        return fun(lo),fun(hi)
    ul,uh=lo-1,hi-1
    bl,bh=lo/(4-lo),hi/(4-hi)
    assert ul>=0 and 0<bl<=bh<k
    dl=1-uh*(2*k-bl)
    dh=1-ul*(2*k-bh)
    assert 0<dl<=dh
    lb=Q(1,4)+ul*(k-bh)/(2*dh)
    ub=Q(1,4)+uh*(k-bl)/(2*dl)
    return lb,ub


def count_avoiders(n, pattern):
    # Direct substring enumeration (small instance).
    a=[0]*(n+1)
    for bits in product('01',repeat=n):
        word=''.join(bits)
        if pattern not in word:
            a[word.count('1')]+=1
    return a


def predict_avoid(n,k,kind):
    # P_w(z,y)=C(z,y)/[(1-(1+y)z)C(z,y)+y^k z^(2k)].
    # Check weighted coefficients coefficientwise, using integer polynomials.
    m=2*k
    C={(0,0):1}
    if kind=='alternating':
        for j in range(1,k): C[(2*j,j)]=1
    def coefficient(poly,deg,w):
        return poly.get((deg,w),0)
    # D= C-zC-yzC+z^(2k)y^k
    D={}
    def add(i,j,val):D[(i,j)]=D.get((i,j),0)+val
    for (i,j),v in C.items():
        add(i,j,v);add(i+1,j,-v);add(i+1,j+1,-v)
    add(m,k,1)
    B=[[] for _ in range(n+1)]
    B[0]=[1]
    for i in range(1,n+1):
        B[i]=[0]*(i+1)
        for j in range(i+1):
            val=coefficient(C,i,j)
            for (di,dj),coeff in D.items():
                if di==0 or di>i or dj>j:continue
                nj=j-dj
                if nj<len(B[i-di]):val-=coeff*B[i-di][nj]
            B[i][j]=val
    return B[n]


def main():
    print('RATIONAL ROOT AND VARIANCE CERTIFICATES')
    for k in range(2,8):
        lu,uu=variance_bounds(k,'unbordered')
        la,ua=variance_bounds(k,'alternating')
        assert lu>ua, f'variance order not proved at k={k}'
        print(f'k={k}: variance-unbordered in ({float(lu):.12f},{float(uu):.12f}); '
              f'variance-alternating in ({float(la):.12f},{float(ua):.12f}); '
              f'certified gap > {float(lu-ua):.12f}')
    print('FOR k>=8: proved symbolic inequalities, check rational gate for 8..100')
    for k in range(8,101):
        a=Q(1,4**k)
        assert 160*k*k*a < k+1
        assert 4*k*a<Q(1,100)
    print('all rational gates passed')
    print('INDEPENDENT DIRECT WEIGHTED LANGUAGE ENUMERATION')
    for k,nmax in [(2,13),(3,13),(4,13)]:
        for kind in ('unbordered','alternating'):
            pattern='0'*k+'1'*k if kind=='unbordered' else '01'*k
            for n in range(0,nmax+1):
                assert count_avoiders(n,pattern)==predict_avoid(n,k,kind),(k,kind,n)
            print(f'{kind} k={k}: all coefficients through n={nmax} verified')
    print('ALL CHECKS PASSED')
if __name__=='__main__':main()
