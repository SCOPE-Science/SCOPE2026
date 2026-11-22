"""Finite exact Gram and asymptotic checks for staggered periodic linear splines.

Run: python3 check.py
Only Python's standard library is needed. These tests supplement the proof.
"""
from fractions import Fraction as F
import math


def hat(x, n, center):
    d = (x - center) % 1
    d = min(d, 1 - d)
    return max(F(0), 1 - n*d)


def gram(n, j, offset):
    center0 = F(0)
    center1 = (F(j) + offset) / n
    h = F(1,n)
    knots = {F(0), F(1)}
    for c in (center0, center1):
        for z in (c-h, c, c+h):
            knots.add(z % 1)
    knots = sorted(knots)
    total = F(0)
    for lo,hi in zip(knots,knots[1:]):
        width = hi-lo
        a0,a1 = hat(lo,n,center0),hat(hi,n,center0)
        b0,b1 = hat(lo,n,center1),hat(hi,n,center1)
        da,db=a1-a0,b1-b0
        total += width*(a0*b0+(a0*db+b0*da)/2+da*db/3)
    return total


def gamma(k,n):
    t=2*math.pi*k/n
    return abs(math.cos(t/2))*(11+math.cos(t))/(4*(2+math.cos(t)))


def eigen_from_gram(row,k,n):
    return sum(float(a)*complex(math.cos(-2*math.pi*k*j/n),math.sin(-2*math.pi*k*j/n)) for j,a in enumerate(row))


def verify():
    tests=0
    for n in (3,4,5,6,7,9,11):
        a=[gram(n,j,F(0)) for j in range(n)]
        b=[gram(n,j,F(1,2)) for j in range(n)]
        assert sum(a)==F(1,n)
        assert sum(b)==F(1,n)
        for k in range(n):
            va=eigen_from_gram(a,k,n)
            vb=eigen_from_gram(b,k,n)
            assert va.real > 0 and abs(va.imag)<1e-12
            assert abs(abs(vb)/abs(va)-gamma(k,n))<4e-12,(n,k,vb,va)
            tests+=3
        # Common refinement and circulant overlap checked by exact fractions.
        for j in range(n):
            assert a[j]==a[(-j)%n]
            assert b[j]>=0
            tests+=2
    exact={3:F(49,64),4:None}
    for n,value in exact.items():
        if value is not None:
            assert abs(gamma(1,n)**2-float(value))<1e-13
            tests+=1
    target=math.pi**4/12
    errors=[]
    for n in (24,32,48,64,96):
        mu=gamma(1,n)**2
        estimates=n**4*(1-mu)
        errors.append(abs(estimates-target))
        assert estimates>0
        tests+=1
    assert errors[-1]<errors[0]/8
    tau=0.05
    target_trace=1+2*sum(math.exp(-tau*target*k**4) for k in range(1,16))
    errs=[]
    for n in (12,16,24,32,48):
        m=int(tau*n**4)
        trace=sum(gamma(k,n)**(2*m) for k in range(n))
        errs.append(abs(trace-target_trace))
        tests+=1
    assert all(errs[i+1]<errs[i] for i in range(len(errs)-1))
    assert errs[-1]<0.003
    print('PASS:',tests,'exact-Gram / Fourier / asymptotic assertions')
    print('critical coefficient =',target)
    print('gap errors =',errors)
    print('trace errors =',errs)

if __name__=='__main__':
    verify()
