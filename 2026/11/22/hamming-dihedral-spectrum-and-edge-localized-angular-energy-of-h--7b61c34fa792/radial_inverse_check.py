"""Solve two radial Poisson equations, without Walsh diagonalization."""
from fractions import Fraction as F
from math import comb

def solve(d,f):
    M = [comb(d,h) for h in range(d+1)]
    assert sum(n*v for n,v in zip(M,f))==0
    u, acc = [F(0)], F(0)
    for h in range(d):
        acc += M[h]*f[h]
        u.append(u[-1]-acc/(M[h]*(d-h)))
    mean = sum(n*v for n,v in zip(M,u))/2**d
    return [v-mean for v in u]

for d in range(2,31):
    N=2**d
    f=[F(h==0)-F(1,N) for h in range(d+1)]
    c=solve(d,solve(d,f))
    A=sum(F(comb(d,k),4*N*k*k) for k in range(1,d+1))
    B=sum(F(comb(d,k),16*N*k**4) for k in range(1,d+1))
    assert c[0]==A and sum(comb(d,h)*x*x for h,x in enumerate(c))==B
    assert all(c[h]>c[h+1] for h in range(d))
    assert (c[1]>0)==(d>=3)
    assert c[-1]==-(sum(F(1,k) for k in range(1,d+1))**2+
                    sum(F(1,k*k) for k in range(1,d+1)))/(8*N)
    for h,x in enumerate(c):
        assert x==sum(F(sum((-1)**j*comb(h,j)*comb(d-h,k-j)
                             for j in range(max(0,k-d+h),min(h,k)+1)),4*N*k*k)
                       for k in range(1,d+1))
print('Exact radial double inverse agrees with all shells and energy, d=2..30')
