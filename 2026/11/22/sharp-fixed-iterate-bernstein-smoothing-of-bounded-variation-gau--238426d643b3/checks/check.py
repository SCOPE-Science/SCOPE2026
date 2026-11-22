"""Finite arithmetic and Gaussian-profile checks for two Bernstein averaging kernels.

Requires Python 3.10+ standard library. Optional extended numerical checks use numpy/scipy.
This is a finite reproducibility check, not an infinite-asymptotic proof.
"""
from fractions import Fraction as Q
from math import comb, factorial, sqrt, pi


def integral_power(coeff, a, b):
    return sum(c * (b**(j+1)-a**(j+1))/Q(j+1) for j, c in enumerate(coeff))


def multiply(a, b):
    ans = [Q(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ans[i+j] += x*y
    return ans


def bernstein_basis(n, j):
    p = [Q(0)]*(n+1)
    for z in range(n-j+1):
        p[j+z] += comb(n,j)*comb(n-j,z)*(-1)**z
    return p


def coefficients(n, values):
    result = [Q(0)]*(n+1)
    for k, v in enumerate(values):
        for d, a in enumerate(bernstein_basis(n,k)):
            result[d] += v*a
    return result


def cdf_tail(n, k, t):
    return (n+1)*integral_power(bernstein_basis(n,k), t, Q(1))


def transition(n, typ):
    ans = []
    for k in range(n+1):
        row=[]
        for j in range(n+1):
            if typ == 'K':
                m=Q(n+1)
                v=m*integral_power(bernstein_basis(n,j),Q(k,n+1),Q(k+1,n+1))
            else:
                v=Q((n+1)*comb(n,k)*comb(n,j)*factorial(k+j)*factorial(2*n-k-j),factorial(2*n+1))
            row.append(v)
        ans.append(row)
    return ans


def mv(P, v):
    return [sum((a*b for a,b in zip(row,v)),Q(0)) for row in P]


def jump_coeffs(n, typ, t):
    if typ=='K':
        return [min(Q(1),max(Q(0),Q(k+1)-(n+1)*t)) for k in range(n+1)]
    return [cdf_tail(n,k,t) for k in range(n+1)]


def jump_error(n, typ, r, p, t):
    v=jump_coeffs(n,typ,t)
    M=transition(n,typ)
    for _ in range(r-1):v=mv(M,v)
    f=coefficients(n,v)
    gf=[Q(1)-f[0]]+[-x for x in f[1:]]
    A=[Q(1)]; B=[Q(1)]
    for _ in range(p):A=multiply(A,f);B=multiply(B,gf)
    return integral_power(A,Q(0),t)+integral_power(B,t,Q(1))


def exact():
    nchecks=0
    for n in range(1,8):
        for typ in ('K','D'):
            M=transition(n,typ)
            for row in M:
                assert sum(row,Q(0)) == 1
                assert all(Q(0)<=q<=Q(1) for q in row)
                nchecks+=2
            if typ=='D':
                assert all(M[i][j]==M[j][i] for i in range(n+1) for j in range(n+1))
                nchecks+=1
            c=jump_coeffs(n,typ,Q(1,2))
            assert all(c[i] <= c[i+1] for i in range(n))
            assert all(c[k]+c[n-k]==1 for k in range(n+1))
            nchecks+=2
            for r in (1,2,3):
                for p in (1,2):
                    e=jump_error(n,typ,r,p,Q(1,2))
                    assert 0 < e < 1
                    nchecks+=1
                if typ=='D' and r==1:
                    e=jump_error(n,typ,r,1,Q(1,2))
                    assert e == Q(comb(2*n+2,n+1),4**(n+1))
                    nchecks+=1
    print('exact rational assertions:',nchecks)
    for n in (2,4,6):
        for typ in ('K','D'):
            e=jump_error(n,typ,2,2,Q(1,2))
            print('midpoint squared L2',n,typ,'r=2:',e)
    return nchecks


def extended():
    import numpy as np
    from numpy.polynomial.legendre import leggauss
    from scipy.special import gammaln, betaln, betainc
    from scipy.stats import binom
    I=(sqrt(2)-1)/sqrt(pi)
    checked=0
    for n in (24,48):
        k=np.arange(n+1)
        low=k/(n+1);high=(k+1)/(n+1)
        Kmat=np.array([betainc(j+1,n-j+1,high)-betainc(j+1,n-j+1,low) for j in k]).T
        logC=gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)
        a=k[:,None]+k[None,:]+1;b=2*n-k[:,None]-k[None,:]+1
        Dmat=np.exp(np.log(n+1)+logC[:,None]+logC[None,:]+betaln(a,b))
        for typ,M,v in (('K',Kmat,1),('D',Dmat,2)):
            assert np.max(abs(M.sum(1)-1))<1e-10;checked+=1
            for r in (1,2,3):
                t=.5
                c=np.clip(k+1-(n+1)*t,0,1) if typ=='K' else 1-betainc(k+1,n-k+1,t)
                for _ in range(r-1):c=M@c
                g,w=leggauss(n+2)
                x=np.r_[(g+1)*t/2,t+(g+1)*(1-t)/2];weights=np.r_[w*t/2,w*(1-t)/2]
                f=binom.pmf(k[None,:],n,x[:,None])@c
                e=float(np.dot(weights,(f-(x>t))**2))
                predicted=I*sqrt(r*v)/2
                ratio=sqrt(n)*e/predicted
                assert abs(ratio-1)<.07, (typ,n,r,ratio)
                checked+=1
                print('asymptotic midpoint:',typ,n,'iterate',r,'ratio',round(ratio,7))
    print('numerical assertions:',checked)
    return checked

if __name__=='__main__':
    exact()
    try:
        extended()
    except ImportError:
        print('Optional scipy/numpy numerical extension unavailable; exact checks passed.')
