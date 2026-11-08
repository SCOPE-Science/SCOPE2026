"""Exact and numeric checks for birth-label degree / total path-length dependence."""
from fractions import Fraction
from itertools import product
from math import factorial, log


def H(m, p=1):
    return sum((Fraction(1, k**p) for k in range(1,m+1)),Fraction(0))


def exact(n,i):
    return n*sum(((H(i-1)+1-H(j-1))/Fraction(j*(j-1)) for j in range(i+1,n+1)),Fraction(0))


def closed(n,i):
    return n*(Fraction(i-1,i*i)+Fraction(H(n)-H(i-1)-1,n)-(H(n,2)-H(i,2)))


def enumeration(n):
    c=factorial(n-1)
    t=tsq=0
    ds=[0]*(n+1); dt=[0]*(n+1)
    for parents in product(*(range(1,j) for j in range(2,n+1))):
        depths=[0]*(n+1); degrees=[0]*(n+1);tt=0
        for j,p in enumerate(parents,2):
            depths[j]=1+depths[p];tt+=depths[j];degrees[p]+=1
        t+=tt;tsq+=tt*tt
        for i in range(1,n+1):
            ds[i]+=degrees[i];dt[i]+=degrees[i]*tt
    return [(Fraction(dt[i],c)-Fraction(ds[i]*t,c*c)) for i in range(n+1)]


def run():
    count=0
    for n in range(2,10):
        actual=enumeration(n)
        for i in range(1,n+1):
            assert actual[i]==exact(n,i)==closed(n,i),(n,i,actual[i],exact(n,i),closed(n,i));count+=1
        assert sum(actual)==0;count+=1 # total outdegree n-1 deterministic
    for i in range(2,70):
        hs=0.0; hi=sum(1/k for k in range(1,i))
        # for all i, positive at n=i+1; exactly one transition after positive growth
        s=0.0; first_nonpos=None
        for n in range(i+1,min(100000,max(3000,int(5*i*i*log(max(i,2)))))):
            hm=sum(1/k for k in range(1,n)) if n==i+1 else hm+1/(n-1)
            increment=(hi+1-hm)/(n*(n-1))
            s+=increment
            if first_nonpos is None and s<=0:first_nonpos=n
            if first_nonpos is not None:assert s<=1e-12
        assert first_nonpos is not None,i
        count+=1
    print('PASS:',count,'exact enumeration/analytic and numeric threshold assertions')

if __name__=='__main__':run()
