"""Exact rational convolution certificates for selected prefix-average scans.
Uses sympy; all displayed probabilities are rational, with no random draws.
"""
from fractions import Fraction
import sympy as sp
x=sp.Symbol('x', real=True)

def exact_cdf(m, selected, c):
    c=sp.Rational(c.numerator,c.denominator) if isinstance(c,Fraction) else sp.Rational(c)
    selected=set(selected)
    assert 1<=min(selected)<=max(selected)<=m and 0<c<1
    # Each segment: left endpoint, right endpoint, polynomial density.
    seg=[(sp.Integer(0),sp.Integer(1),sp.Integer(1))]
    if 1 in selected:
        seg=[(sp.Integer(0),c,sp.Integer(1))]
    for k in range(2,m+1):
        breaks={sp.Integer(0),sp.Integer(k)}
        for a,b,p in seg:
            for t in (a,b,a+1,b+1):
                if 0<=t<=k:breaks.add(t)
        if k in selected:breaks.add(k*c)
        br=sorted(breaks)
        nxt=[]
        for lo,hi in zip(br[:-1],br[1:]):
            if lo==hi or (k in selected and lo>=k*c): continue
            mid=(lo+hi)/2
            val=sp.Integer(0)
            for a,b,p in seg:
                # convolution integration in t from max(a,x-1) to min(b,x)
                low=a if a>=mid-1 else x-1
                high=b if b<=mid else x
                if max(a,mid-1)>=min(b,mid):continue
                ant=sp.integrate(p,x)
                val+=ant.subs(x,high)-ant.subs(x,low)
            val=sp.expand(val)
            if val!=0:nxt.append((lo,hi,val))
        seg=nxt
    return sp.simplify(sum(sp.integrate(p,(x,a,b)) for a,b,p in seg))

if __name__=='__main__':
    assert exact_cdf(1,{1},Fraction(3,4))==sp.Rational(3,4)
    assert exact_cdf(2,{1,2},Fraction(1,2))==sp.Rational(3,8)
    assert exact_cdf(2,{1,2},Fraction(3,4))==sp.Rational(23,32)
    assert exact_cdf(3,{1,2,3},Fraction(3,4))==sp.Rational(17,24)
    assert exact_cdf(2,{2},Fraction(1,2))==sp.Rational(1,2)
    assert exact_cdf(4,{4},Fraction(1,2))==sp.Rational(1,2)
    x4=exact_cdf(4,{2,3,4},Fraction(3,4))
    print('all exact-rational checks passed; m=4 selected {2,3,4} c=3/4 CDF=',x4)
