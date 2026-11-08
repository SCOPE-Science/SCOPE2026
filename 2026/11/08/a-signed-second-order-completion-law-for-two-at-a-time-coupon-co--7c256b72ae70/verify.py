"""Reproducibility for two-coupon group collection; Python standard library only."""
from fractions import Fraction
from decimal import Decimal, localcontext
from math import comb, log, exp, floor

def coverage_ie(n,m):
    assert n >= 2 and m >= 0
    den = n*(n-1)
    return sum(((-1)**k)*comb(n,k)*Fraction((n-k)*(n-k-1),den)**m for k in range(n+1))

def coverage_dp(n,m):
    den=comb(n,2)
    state=[Fraction(0)]*(n+1);state[n]=Fraction(1)
    for _ in range(m):
        nex=[Fraction(0)]*(n+1)
        for j,p in enumerate(state):
            if not p: continue
            if n-j>=2: nex[j]+=p*Fraction(comb(n-j,2),den)
            if j and n-j: nex[j-1]+=p*Fraction(j*(n-j),den)
            if j>=2: nex[j-2]+=p*Fraction(comb(j,2),den)
        state=nex
    return state[0]

def coverage_decimal(n,m):
    with localcontext() as ctx:
        ctx.prec=110
        out=Decimal(0)
        for k in range(n+1):
            if k>n-2 and m: continue
            q=Decimal((n-k)*(n-k-1))/Decimal(n*(n-1))
            out+=(-1 if k%2 else 1)*Decimal(comb(n,k))*q**m
        return +out

def predicted_correction(n,m):
    c=2*m/n-log(n)
    lam=exp(-c)
    return -exp(-lam)*(lam**2+(lam**2-2*lam)*(log(n)+c))/(2*n)

def check():
    tests=0
    for n in range(2,10):
        for m in range(0,19):
            assert coverage_ie(n,m)==coverage_dp(n,m),(n,m)
            tests+=1
    for c in (-log(2),0,0.8):
        last=None
        for n in (80,160,320):
            m=floor(n/2*(log(n)+c))
            lam=exp(-(2*m/n-log(n)))
            with localcontext() as ctx:
                ctx.prec=100
                actual=float(coverage_decimal(n,m))
            correction=predicted_correction(n,m)
            discrepancy=abs(actual-exp(-lam)-correction)
            scaled=discrepancy*n*n/(log(n)**2)
            assert scaled < 5, (n,c,scaled)
            tests+=1
            if last is not None: assert abs(actual-exp(-lam))<last;tests+=1
            last=abs(actual-exp(-lam))
    for n in (80,160,320,640):
        m=floor(n/2*(log(n)-log(2)))
        lam=exp(-(2*m/n-log(n)))
        with localcontext() as ctx: ctx.prec=110; actual=float(coverage_decimal(n,m))
        assert abs(n*(actual-exp(-lam))+2*exp(-2)) < 1.0*log(n)**2/n,(n,actual,lam)
        tests+=1
    print('VERIFY_OK',tests,'checks')
if __name__=='__main__':check()
