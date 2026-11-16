#!/usr/bin/env python3
"""Exact arithmetic checks for binary Fourier spectra of clique windmills."""
from math import comb
from fractions import Fraction


def fwht(a):
    a = list(a)
    size = len(a)
    h = 1
    while h < size:
        for i in range(0, size, 2*h):
            for j in range(i, i+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return a


def independent_mask(mask, r, n):
    if mask & 1:
        return mask == 1
    for i in range(n):
        q = (mask >> (1+i*r)) & ((1 << r)-1)
        if q.bit_count() > 1:
            return False
    return True


def local_sum(r):
    assert r % 2 == 0
    m = r//2
    vals = []
    for j in range(r+1):
        z = sum((-1)**i*comb(j,i)*comb(r-j,k-i)
                for k in (m,m+1) for i in range(max(0,k-r+j),min(j,k)+1))
        vals.append(z)
    t = comb(r,m) + comb(r,m+1)
    return vals, t, sum(comb(r,j)*abs(vals[j]) for j in range(r+1))


def run():
    local_checks = 0
    for r in range(2,32,2):
        a, t, s = local_sum(r)
        assert s == (1 << (r//2))*t, (r,s,t)
        for j in range(r+1):
            h=(j+1)//2
            assert (a[j]>0)==(h%2==0)
            if r<=8:
                x=(1<<j)-1
                brute=sum((-1)**((q&x).bit_count()) for q in range(1<<r)
                          if q.bit_count() in (r//2,r//2+1))
                assert a[j]==brute
        local_checks += 1
    coef_checks = 0
    tested=[]
    for r in range(1,7):
        for n in range(1,5):
            dim=1+r*n
            if dim>13:
                continue
            N=1<<dim
            indep=[int(independent_mask(x,r,n)) for x in range(N)]
            W=fwht(indep)
            for freq,val in enumerate(W):
                h=(-1 if freq&1 else 1)
                prod=1
                for i in range(n):
                    q=(freq>>(1+i*r))&((1<<r)-1)
                    prod *= r+1-2*q.bit_count()
                assert val == prod+h, (r,n,freq,val,prod+h)
            zeros=sum(x==0 for x in W)
            t=comb(r,r//2)+comb(r,r//2+1) if r%2==0 else 0
            assert zeros==(t**n if r%2==0 else 0), (r,n,zeros,t)
            target_min = 2 if r%2==0 else 1
            assert min(abs(x) for x in W if x) == target_min
            assert max(abs(x) for x in W) == (r+1)**n+1
            support=[int(x != 0) for x in W]
            proj_num=fwht(support)
            actual_norm=Fraction(sum(map(abs,proj_num)),N)
            target_norm=(Fraction(1)+Fraction(t**n*(2**((r//2)*n)-1),2**(r*n))
                          if r%2==0 else Fraction(1))
            assert actual_norm==target_norm,(r,n,actual_norm,target_norm)
            if N<=2048:
                for freq in range(N):
                    if freq%11 != 0:
                        continue
                    direct=sum((-1)**((freq&mask).bit_count()) for mask in range(N) if indep[mask])
                    assert direct==W[freq]
            coef_checks+=N
            tested.append((r,n,N,zeros,str(actual_norm)))
    print('WINDMILL_FOURIER_PROJECTION_EXACT_PASS', 'coefficients=',coef_checks, 'local_lengths=',local_checks)
    print('TESTED', tested)


if __name__=='__main__':
    run()
