"""Exact rational and numerical checks for two Jacobi-weighted disk kernels.
Run with Python 3 standard library: python jacobi_kernel_check.py.
Finite checks corroborate, but do not replace, the analytic root-count proof.
"""
from fractions import Fraction as F
from math import comb, factorial, sqrt


def poly(t, m):
    t = F(t)
    if m == 1:
        return [t*(t+1), 2*(1-t*t), t*(t-1)]
    if m == 2:
        return [t*(t+1)*(t+2), 3*(1-t)*(t+1)*(t+2),
                3*t*(t-1)*(t+2), -t*(t-1)*(t+1)]
    raise ValueError(m)


def evalpoly(c, x):
    out = 0
    for v in reversed(c):
        out = out*x + v
    return out


def inverse_beta(t, m, n):
    v = F(1)
    for j in range(m+1):
        v *= n+t+j
    return v / factorial(m)


def root_bisect(c, left, right):
    fl = float(evalpoly(c, left))
    fr = float(evalpoly(c, right))
    assert fl*fr < 0
    for _ in range(100):
        mid = (left+right)/2
        fm = float(evalpoly(c, mid))
        if fl*fm > 0:
            left, fl = mid, fm
        else:
            right, fr = mid, fm
    return (left+right)/2


def main():
    trials = [F(1,9),F(1,4),F(1,2),F(3,4),F(4,5),
              F(5,6),F(9,10),F(1),F(11,10),F(3,2),F(2),F(5)]
    exact = 0
    roots = 0
    for m in (1,2):
        for t in trials:
            c = poly(t,m)
            assert evalpoly(c,1)==factorial(m+1)
            if m == 1:
                assert evalpoly(c,-1)==2*(2*t*t-1)
            else:
                assert evalpoly(c,-1)==2*(2*t+1)*(2*t*t+2*t-3)
            exact += 2
            for n in range(16):
                # coefficient of s^n in P(s)/(m! (1-s)^(m+2))
                series = sum(c[k]*comb(n-k+m+1,m+1)
                             for k in range(min(n,m+1)+1))/factorial(m)
                assert series == inverse_beta(t,m,n)
                exact += 1
            if t < 1:
                if m == 2:
                    R=float((t+2)/(1-t))
                    zr=root_bisect(c,-R,0)
                    # Vieta: the conjugate pair has modulus squared R/|zr|.
                    assert R/abs(zr)>1
                    assert abs(float(evalpoly(c,zr)))<1e-8
                    roots += 2
                else:
                    zr=root_bisect(c,-10000,0)
                    zp=root_bisect(c,1,10000)
                    assert zp>1 and abs(float(evalpoly(c,zr)))<1e-7
                    roots += 2
                has_zero=(abs(zr)<1)
                criterion=(2*t*t<1 if m==1 else 2*t*t+2*t<3)
                assert has_zero==criterion
                roots+=1
            elif t>1:
                if m==2:
                    R=float((t+2)/(t-1))
                    zp=root_bisect(c,1,R)
                    assert R/zp>1 and abs(float(evalpoly(c,zp)))<1e-7
                    roots+=2
                else:
                    assert float((t+1)/(t-1))>1
                    roots+=1
            else:
                assert all(x == 0 for x in c[1:])
                roots+=1
    # Boundary equality at the two exact threshold parameters.
    t1=1/sqrt(2)
    t2=(sqrt(7)-1)/2
    assert abs(float(evalpoly(poly(t1,1),-1)))<2e-15
    assert abs(float(evalpoly(poly(t2,2),-1)))<2e-14
    assert t1<t2<1
    print(f'JACOBI_BERGMAN_KERNEL_PASS exact={exact} root_and_threshold={roots+3}')

if __name__=='__main__':
    main()
