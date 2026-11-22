#!/usr/bin/env python3
"""Independent integer and high-precision checks for an Abelian-complexity fluctuation law.
Runs with Python 3 standard library only. Finite checks support but do not replace proof."""
from decimal import Decimal, localcontext
from math import pi, sqrt, atan, cos


def atan_series(x, n=100):
    v = Decimal(0)
    xx = x*x
    term = x
    for k in range(n):
        v += (1 if k % 2 == 0 else -1)*term / (2*k+1)
        term *= xx
    return v


def cosine_small(x):
    # |x| <= pi/6. Error after j=19 bounded by |x|^40/40! < 1e-57.
    out = Decimal(1)
    term = Decimal(1)
    for j in range(1,20):
        term *= -x*x/Decimal((2*j-1)*(2*j))
        out += term
    return out


def count_values(m):
    counts = [1,0,0]
    A=2
    values=[]
    for i in range(m+1):
        values.append(A)
        A+=3*(max(counts)-min(counts))
        counts=[3*counts[0]+counts[2],3*counts[1]+counts[0],3*counts[2]+counts[1]]
    return values


def oracle_windows(m):
    words = ['0','1','2']
    for _ in range(m):
        words = [''.join(c*3+str((int(c)+1)%3) for c in word) for word in words]
    L=4**m
    extrema=[]
    for a in words:
        for b in words:
            s=a+b
            hits=[int(s[i:i+L].count('0')) for i in range(L+1)]
            extrema.extend(hits)
    return max(extrema)-min(extrema)+1


def decimal_skew(N=16384,K=24):
    with localcontext() as ctx:
        ctx.prec=60
        one=Decimal(1)
        p=16*atan_series(one/5)-4*atan_series(one/239)
        sqrt3=Decimal(3).sqrt()
        rho=Decimal(7).sqrt()
        theta=atan_series(sqrt3/5)
        period=p/3
        mu=6*sqrt3/(p*(rho-1))
        weights=[]
        w=one
        for k in range(K):
            w /= rho
            weights.append(2*w)
        phases=[-k*theta-period/2 for k in range(1,K+1)]
        sum_cube=Decimal(0)
        sum_sq=Decimal(0)
        for j in range(N):
            t=(Decimal(2*j+1)*period)/(2*N)
            h=Decimal(0)
            for k in range(K):
                z=t+phases[k]
                # pi/3-periodic expression: R(z)=sqrt(3)*cos(centered(z)).
                quotient=int((z/period+Decimal('0.5')).to_integral_value(rounding='ROUND_FLOOR'))
                z-=quotient*period
                h+=weights[k]*sqrt3*cosine_small(z)
            d=h-mu
            sum_cube+=d*d*d
            sum_sq+=d*d
        observed=sum_cube/N
        second=sum_sq/N
        # Conservative *proved analytic* errors: |H-H_K|<2 sqrt(3) rho^-K/(rho-1)
        tail=2*sqrt3*(rho**(-K))/(rho-1)
        # The exact mean mu lies in [3/(rho-1), 2sqrt(3)/(rho-1)] and |H-mu|<0.3.
        # Thus t->(H(t)-mu)^3 is Lipschitz with constant <3*0.3^2*4/(rho-1)<0.657.
        # Averaged midpoint rule error <= Lip*period/(4*N).
        quad=Decimal('0.657')*period/(4*N)
        perturb=3*Decimal('0.301')**2*tail
        # 60-digit Decimal arithmetic and Taylor/atan truncations contribute below 1e-18;
        # this bound is intentionally generous, and can be reduced by re-running at 80 digits.
        numeric=Decimal('1e-15')
        err=quad+perturb+numeric
        return {'pi':p,'rho':rho,'theta':theta,'mean':mu,'skew_midpoint':observed,'skew_lower':observed-err,'skew_upper':observed+err,'skew_error':err,'sample_variance':second,'tail':tail}


if __name__=='__main__':
    seq=count_values(10)
    assert seq[:10]==[2,5,14,38,95,260,707,1787,4805,13112],seq
    print('INTEGER_RECURRENCE: PASS',seq[:10])
    for m in range(6):
        q=oracle_windows(m)
        assert q ==seq[m],(m,q,seq[m])
    print('DIRECT_WINDOW_ORACLE: PASS for m=0..5 (nine ordered block pairs each)')
    rho=sqrt(7);theta=atan(sqrt(3)/5)
    exact_mean=6*sqrt(3)/(pi*(rho-1))
    variance=sum(216/(pi*pi*(36*j*j-1)**2*(8-2*rho*cos(6*j*theta))) for j in range(1,5001))
    print('FOURIER_MEAN:',format(exact_mean,'.15f'))
    print('FOURIER_VARIANCE:',format(variance,'.15f'))
    out=decimal_skew()
    for k in ['mean','skew_midpoint','skew_error','skew_lower','skew_upper','tail','sample_variance']:
        print('HIGH_PRECISION_'+k.upper()+':',str(out[k]))
    assert out['skew_upper']<0
    assert abs(float(out['sample_variance'])-variance)<0.000002
    print('NEGATIVE_THIRD_CENTERED_MOMENT: PASS by Lipschitz quadrature bound')
