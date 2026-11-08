#!/usr/bin/env python3
"""Independent exact rational and high-precision checks of clipped-cube asymptotic claim."""
from fractions import Fraction as F
from math import comb, factorial
from decimal import Decimal, localcontext

def irwin_cdf_moment(n, t, power):
    """Integrate u**power * Pr(sum of n-1 uniforms <= t-u) du, exactly."""
    if n == 1:
        return min(F(1),max(F(0),t))**(power+1)/F(power+1)
    ans=F(0)
    for k in range(n):
        a=t-k
        if a <= 0: continue
        b=min(F(1),a)
        integ=sum(F(comb(n-1,j)*(-1)**j, power+j+1)*a**(n-1-j)*b**(power+j+1) for j in range(n))
        ans += (-1)**k*comb(n-1,k)*integ/F(factorial(n-1))
    return ans

def formula(n,t):
    A=sum((-1)**k*comb(n,k)*max(F(0),t-k)**n for k in range(n+1))
    # n! times first coordinate second moment integral in [0,1]^n
    D=sum((-1)**k*comb(n,k)*(F(2)*max(F(0),t-k)**(n+2)/F((n+1)*(n+2))
              +F(2*k,n*(n+1))*max(F(0),t-k)**(n+1)
              +F(k,n)*max(F(0),t-k)**n) for k in range(n+1))
    # Sum over k counts all shifted coordinates, need 1/n for coordinate second moment
    # correct first-coordinate T: ∫ u_1^2 (sum u <=t) du = D/n!
    return A/F(factorial(n)), D/F(factorial(n))

def B(l):
    q=(-l).exp()
    return (-l*l+4*l+2) + (-2*l**3-3*l*l-6*l-4)*q+(2*l+2)*q*q

def D_result(l):
    q=(-l).exp()
    z=(1-q)/l
    u1=(1-(1+l)*q)/(l*(1-q))
    u2=(2-(l*l+2*l+2)*q)/(l*l*(1-q))
    u3=(6-(l**3+3*l*l+6*l+6)*q)/(l**3*(1-q))
    var=u2-u1*u1
    cov=u3-u1*u2
    direct=2*l*var*u2-cov
    factored=-q*B(l)/(l*l*(1-q)**3)
    return direct,factored

def root():
    with localcontext() as c:
        c.prec=65
        lo=Decimal('2.5');hi=Decimal('3.5')
        assert B(lo)>0 and B(hi)<0
        for _ in range(230):
            mi=(lo+hi)/2
            if B(mi)>0:lo=mi
            else:hi=mi
        l=(lo+hi)/2
        q=(-l).exp();Z=(1-q)/l
        a=1/l-q/(1-q)
        m2=(2-(l*l+2*l+2)*q)/(l*l*(1-q))
        I=-Z.ln()-l*a
        limit=m2*(2*I).exp()/4
        return l,a,limit

def derivative_coeff(n):
    # n-th derivative at zero of e^(2*l)*(-l^2+4*l+2)
    # +e^l*(-2*l^3-3*l^2-6*l-4)+2*l+2.
    res=(2**n)*2+ (4*n*2**(n-1) if n>=1 else 0)
    if n>=2:res-=n*(n-1)*2**(n-2)
    res-=4
    if n>=1:res-=6*n
    if n>=2:res-=3*n*(n-1)
    if n>=3:res-=2*n*(n-1)*(n-2)
    if n==0:res+=2
    if n==1:res+=2
    return res

if __name__ == '__main__':
    count=0
    for n in range(2,11):
        for j in range(1,3*n):
            t=F(j,3)
            if t > n:continue
            gotv,gotm=irwin_cdf_moment(n,t,0),irwin_cdf_moment(n,t,2)
            v,m=formula(n,t)
            assert (gotv,gotm)==(v,m), (n,t,gotv,gotm,v,m)
            count+=1
    coeff=[derivative_coeff(i) for i in range(14)]
    assert coeff[:5]==[0]*5
    assert coeff[5:10]==[10,46,112,132,-258], coeff
    assert all(derivative_coeff(i)<0 for i in range(9,101))
    with localcontext() as c:
        c.prec=65
        for s in ['0.05','0.1','0.3','1','2','2.7','2.84','2.9','3','4','8','20']:
            l=Decimal(s);a,b=D_result(l)
            assert abs(a-b)<Decimal('1e-45'), (s,a,b)
        l,alpha,f=root()
        assert Decimal('2.84171173')<l<Decimal('2.84171175')
        assert Decimal('0.28996222')<alpha<Decimal('0.28996225')
        assert Decimal('0.06227291')<f<Decimal('0.06227293')
        cross=1/(2*Decimal(1).exp()**2)
        assert f<cross and f<Decimal(1)/12
        print('CLIPPED_CUBE_UNIQUE_MIN_CHECKS_PASSED',count,'exact rational volume/moment tests; 101 derivative signs; 12 derivative factorizations')
        print('lambda',l,'alpha',alpha,'L_squared',f,'endpoint_cross',cross)
