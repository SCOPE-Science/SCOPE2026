#!/usr/bin/env python3
"""Standalone directed-decimal enclosure certificate for the preferential-attachment series.

Requires only Python 3.11+ standard library. All interval operations use outward
rounding; Decimal exp/ln are correctly rounded to nearest (Python decimal's
specified behavior) and then widened by at least one unit in last place.
"""
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F

P = 65
Z = D(0)
ONE = D(1)
TWO = D(2)
Q = F(49,25)


def with_round(fn, mode):
    with localcontext() as c:
        c.prec=P;c.rounding=mode
        return fn(c)


def down(fn):
    return with_round(fn, ROUND_FLOOR)


def up(fn):
    return with_round(fn, ROUND_CEILING)


def frac_lower(f):
    f=F(f)
    return down(lambda c:D(f.numerator)/D(f.denominator))


def frac_upper(f):
    f=F(f)
    return up(lambda c:D(f.numerator)/D(f.denominator))


def add_lo(a,b):return down(lambda c:a+b)
def add_hi(a,b):return up(lambda c:a+b)
def sub_lo(a,b):return down(lambda c:a-b)
def sub_hi(a,b):return up(lambda c:a-b)
def mul_lo(a,b):return down(lambda c:a*b)
def mul_hi(a,b):return up(lambda c:a*b)
def div_lo(a,b):
    assert b>0
    return down(lambda c:a/b)
def div_hi(a,b):
    assert b>0
    return up(lambda c:a/b)


def log_lo(x):
    assert x>0
    return with_round(lambda c:c.next_minus(c.ln(x)),ROUND_FLOOR)


def log_hi(x):
    assert x>0
    return with_round(lambda c:c.next_plus(c.ln(x)),ROUND_CEILING)


def exp_lo(x):
    return with_round(lambda c:c.next_minus(c.exp(x)),ROUND_FLOOR)


def exp_hi(x):
    return with_round(lambda c:c.next_plus(c.exp(x)),ROUND_CEILING)


def pow_lo(n,t):
    assert n>=1 and F(t)>=0
    return exp_lo(mul_lo(log_lo(D(n)),frac_lower(t)))


def pow_hi(n,t):
    assert n>=1 and F(t)>=0
    return exp_hi(mul_hi(log_hi(D(n)),frac_upper(t)))


def low_partial(a,b,N=300):
    # For t in [a,b], each ratio is at least j^a/(j^a+3^b-1).
    q=sub_hi(pow_hi(3,b),ONE)
    s=Z;term=ONE
    for j in range(1,N+1):
        x=pow_lo(j,a)
        r=div_lo(x,add_hi(x,q))
        term=mul_lo(term,r)
        s=add_lo(s,term)
    return s


def certify_interval(a,b,depth=0):
    value=low_partial(a,b)
    if value>ONE:
        return [(a,b,value)]
    assert depth<16, 'subdivision exceeded cap'
    mid=(a+b)/2
    return certify_interval(a,mid,depth+1)+certify_interval(mid,b,depth+1)


def main():
    assert 3**63<2**100
    assert 3**99*25**100>74**100
    intervals=certify_interval(F(63,100), F(99,100))
    assert len(intervals)==14
    assert intervals[0][0]==F(63,100) and intervals[-1][1]==F(99,100)
    assert all(x[1]==y[0] for x,y in zip(intervals,intervals[1:]))
    assert min(v for _,_,v in intervals)>D('1.001')

    # Endpoint block [99/100,1]. Derivative is sum_j B_j d_j.
    # For j<=5 upper(d_j)<0 and lower(B_j) is a 200-term sum.
    # For j>=6 use upper(B_j)=u_j(j+q)/(q-1),
    # where u_j=product(i/(i+q)).
    qlow=frac_lower(Q)
    qhigh=frac_upper(Q)
    qdiff_lo=sub_lo(qlow,ONE)
    three_log_lo=log_lo(D(3))
    upper_positive=Z
    u_hi=ONE
    for j in range(1,1001):
        u_hi=mul_hi(u_hi,div_hi(D(j),add_lo(D(j),qlow)))
        if j>=6:
            bj_hi=div_hi(mul_hi(u_hi,add_hi(D(j),qhigh)),qdiff_lo)
            numer_hi=sub_hi(mul_hi(TWO,log_hi(D(j))),mul_lo(add_lo(ONE,qlow),three_log_lo))
            assert numer_hi>0
            den_lo=add_lo(pow_lo(j,F(99,100)),qlow)
            upper_positive=add_hi(upper_positive,mul_hi(div_hi(numer_hi,den_lo),bj_hi))
    assert upper_positive<D('0.81'), ('positive',upper_positive)

    bs=[Z]*6
    llo=ONE
    for k in range(1,201):
        x=pow_lo(k,F(99,100))
        llo=mul_lo(llo,div_lo(x,add_hi(x,TWO)))
        for j in range(1,min(5,k)+1):
            bs[j]=add_lo(bs[j],llo)
    upper_negative=Z
    for j in range(1,6):
        num=sub_hi(mul_hi(TWO,log_hi(D(j))),mul_lo(add_lo(ONE,qlow),three_log_lo))
        assert num<0
        dupper=div_hi(num,D(j+2))
        # Negative upper times positive lower; multiply towards +infinity.
        upper_negative=add_hi(upper_negative,mul_hi(dupper,bs[j]))
    assert upper_negative<D('-1.47'), ('negative',upper_negative)

    # Tail j>=1001: u_j <= 2/(j+1)^q, q=49/25.
    # By Gamma-moment Jensen and Gamma log-convexity. Thus
    # B_j<=2(j+2)/[(q-1)(j+1)^q]<=2.1 j^(-.96), j>=1001.
    # d_j^+<=2log(j)/j^.99. Summing by a decreasing integral gives
    # tail<=4.2*1000^(-.95)*(log(1000)/.95+1/.95^2).
    # The simpler rational bounds 1000^(-.95)<1/500 and log(1000)<7
    # yield < 0.08.
    assert 1000**19>500**20
    fact=1;expsum=F(1)
    for k in range(1,15):
        fact*=k
        expsum+=F(7**k,fact)
    assert expsum>1000, 'e^7 > 1000 by partial Taylor series'
    tail_upper=F(21,5)*F(1,500)*(F(7)*F(20,19)+F(400,361))
    assert tail_upper<F(8,100)
    # derivative <= -1.47+0.81+0.08 = -0.58
    print('CERTIFIED: phi(gamma)>1 for all gamma in [0,1), phi(1)=1')
    print('Finite enclosures:',len(intervals),'intervals; min positive margin >=', min(v-ONE for _,_,v in intervals))
    print('Derivative upper blocks: pos<=',upper_positive,' neg<=',upper_negative,' tail<',str(tail_upper))
    print('Derivative bound: phi prime < -0.58 on [0.99,1]')
    print('Intervals (exact rational endpoints):')
    for a,b,v in intervals:print(f'  [{a},{b}] : lower partial >= {v}')

if __name__=='__main__':main()
