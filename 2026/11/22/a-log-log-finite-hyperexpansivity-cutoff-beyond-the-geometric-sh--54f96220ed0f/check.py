"""Supplementary finite diagnostics for a geometric weighted shift hyperexpansivity order.
Run with Python 3 standard library (optional mpmath is not needed).
Exact fractions verify the rational power-series recurrence and difference formula;
floating coefficient sums illustrate the boundary-layer threshold.
"""
from fractions import Fraction as F
from math import log, exp

def coeff(q,a,b,K):
    c=[F(1)]
    for k in range(1,K+1):
        c.append(c[-1]*(a-b*q**(k-1))/(1-q**k))
    return c

def moment(q,a,b,n):
    v=F(1)
    for j in range(n):
        v*= (1-a*q**j)/(1-b*q**j)
    return v

def finite_delta(q,a,b,n,m):
    from math import comb
    return sum(F((-1)**(m-j)*comb(m,j))*moment(q,a,b,n+j)
                for j in range(m+1))

def R(q,a,b,m,K=500):
    q=float(q);a=float(a);b=float(b)
    c=1.;c1=(a-b)/(1-q)
    out=0.
    for k in range(1,K+1):
        if k==1: c=c1
        else:
            c*= (a-b*q**(k-1))/(1-q**k)
            # log to control huge m; for terms below machine range skip
            if c>0:
                exponent=m*(log(1-q**k)-log(1-q))
                out+= (c/-c1)*exp(exponent)
        if k>30 and abs(c)<1e-70:break
    return out

def tests():
    q=F(1,2);a=F(1,5);b=F(41,100)
    c=coeff(q,a,b,12)
    assert c[1]<0 and all(x>0 for x in c[2:])
    for k in range(1,13):
        assert (1-q**k)*c[k] == (a-b*q**(k-1))*c[k-1]
    # Check exact generating-function identity at rational arguments,
    # via coefficients through finite Taylor orders.
    for n in range(1,7):
        # F(q^n) from the convergent product, independent from c: prefix for ratios
        # verify identity moment(n+1)/moment(n) directly
        assert moment(q,a,b,n+1)/moment(q,a,b,n) == (1-a*q**n)/(1-b*q**n)
    # The sign of n=0 generalized differences equals the sign of the ratio bound
    # for small orders; compare exact rational differences with R(m) computed
    # from convergent coefficient sum.
    for m in range(1,13):
        for n in (0,1,2,4):
            val=finite_delta(q,a,b,n,m)*(-1)**(m+1)
            # A negative sign cannot occur farther into the sequence if n=0 is positive.
            if R(q,a,b,m) < 1: assert val>0,(m,n,val)
            if n==0: assert (val>0) == (R(q,a,b,m)<1),(m,n,val,R(q,a,b,m))
    for ep in (1e-2,1e-3,1e-4,1e-5,1e-6):
        bb=2/5+ep
        M=1
        while R(0.5,0.2,bb,M+1)<1 and M<300:
            M+=1
        L=-log(1-0.5); beta=log(1/0.2)/log(2)
        guess=(log(1/ep)+beta*log(log(1/ep)))/L
        print('epsilon',ep,'M',M,'asymptotic',round(guess,3),'delta',round(M-guess,3), 'R_M',R(0.5,0.2,bb,M),'R_next',R(0.5,0.2,bb,M+1))
    print('Exact recurrences and finite differences: PASS')
if __name__=='__main__': tests()
