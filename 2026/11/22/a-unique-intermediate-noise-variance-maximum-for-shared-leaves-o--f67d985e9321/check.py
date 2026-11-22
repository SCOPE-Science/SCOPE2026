"""Exact finite verification for paired Prüfer-code leaf-overlap laws.
Independent computation via exhaustive pairs of words and integer weights.
"""
from fractions import Fraction
from itertools import product
from math import exp


def predicted(n, r):
    m=n-2
    q=Fraction(n-1,n)**m
    a=lambda k: r*(1-Fraction(k,n))+(1-r)*(1-Fraction(k,n))**2
    Q=a(1)**m
    Q2=a(2)**m
    b=(1-Fraction(2,n))*(1-(1-r)*Fraction(1,n))
    c=1-Fraction(2,n)+(1-r)*Fraction(1,n*n)
    meanH=n*Q
    varH=n*Q*(1-Q)+n*(n-1)*(Q2-Q*Q)
    meanL=n*q
    varL=n*q*(1-q)+n*(n-1)*((1-Fraction(2,n))**m-q*q)
    covHL=n*Q+n*(n-1)*b**m-n*n*Q*q
    covLL=n*Q+n*(n-1)*c**m-n*n*q*q
    return meanH,varH,meanL,varL,covHL,covLL


def brute(n,r):
    m=n-2
    den=2*n*n if r==Fraction(1,2) else None
    assert den is not None
    results=[0]*6
    total=0
    for pairs in product(range(n*n),repeat=m):
        xs=[];ys=[];w=1
        for pair in pairs:
            x,y=divmod(pair,n);xs.append(x);ys.append(y)
            w*=1+n*(x==y)
        total+=w
        a=sum(x not in xs for x in range(n))
        b=sum(x not in ys for x in range(n))
        h=sum(x not in xs and x not in ys for x in range(n))
        for i,value in enumerate((h,h*h,a,a*a,h*a,a*b)):
            results[i]+=w*value
    assert total==den**m
    rh,rh2,ra,ra2,rha,rab=(Fraction(x,total) for x in results)
    return rh,rh2-rh*rh,ra,ra2-ra*ra,rha-rh*ra,rab-ra*ra


def main():
    count=0
    for n in range(2,6):
        r=Fraction(1,2)
        result=brute(n,r)
        target=predicted(n,r)
        for k,(x,y) in enumerate(zip(result,target)):
            assert x==y,(n,k,x,y)
            count+=1
    for n in range(2,31):
        for r in (Fraction(0), Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
            x=predicted(n,r)
            assert x[1]>=0 and x[3]>=0
            assert x[4]*x[4]<=x[1]*x[3]
            assert x[5]*x[5]<=x[3]*x[3]
            count+=4
            if r==0:
                assert x[5]==0
                count+=1
            if r==1:
                assert x[0]==x[2] and x[1]==x[3] and x[4]==x[1] and x[5]==x[3]
                count+=4
    print('PASS',count,'exact rational checks, independent weighted enumeration n=2..5')
if __name__=='__main__': main()
