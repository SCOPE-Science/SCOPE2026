"""Independent exact-rational pair-enumeration and transition checks for nested circular isolation counts."""
from fractions import Fraction as F
from math import exp, log

def p(n,z):
    return (1-z)**(n-1) if z<1 else F(0)

def direct(n,t,s):
    # For two marked vertices, union all adjacent gaps with their stronger thresholds.
    probs=[]
    for i in range(n):
        for j in range(n):
            requirements={}
            for g in [(i-1)%n,i]:requirements[g]=max(requirements.get(g,F(0)),t)
            for g in [(j-1)%n,j]:requirements[g]=max(requirements.get(g,F(0)),s)
            probs.append(p(n,sum(requirements.values())))
    return sum(probs)-n*n*p(n,2*t)*p(n,2*s)

def closed(n,t,s):
    return n*(p(n,2*s)+2*p(n,t+2*s)+(n-3)*p(n,2*t+2*s)-n*p(n,2*t)*p(n,2*s))

def critical(n):
    return (1-n**(-1/(n-1)))/2

def sparse_K(x,y):
    from math import exp
    return exp(-2*(x+y))*(exp(2*x)+2*exp(x)-3-4*x*y)

def finite_ratio(n,t,s):
    return closed(n,t,s)/n

checks=0
for n in range(3,15):
    for a in range(1,11):
        for b in range(a,18):
            t=F(a,50);s=F(b,50)
            assert direct(n,t,s)==closed(n,t,s), (n,a,b)
            checks+=1
for n in range(3,35):
    tstar=critical(n)
    for t in [tstar*0.4,tstar*0.8,tstar*1.2,min(.49,tstar*2)]:
        if t<=0 or t>=.5:continue
        samples=[t+(.5-t)*j/99 for j in range(99)]
        cv=[1+2*max(1-t/(1-2*s),0)**(n-1)+(n-3)*max(1-2*t/(1-2*s),0)**(n-1)-n*(1-2*t)**(n-1) for s in samples]
        # Nonpositive region must be terminal; zero plateau permitted at critical t.
        sg=[(1 if v>1e-10 else -1 if v< -1e-10 else 0) for v in cv]
        assert sg[0]==1,(n,t,cv[0])
        assert all(sg[i]>=sg[i+1] for i in range(98)),(n,t,sg)
        checks+=1
for x in [0.2,0.6,1,2,3]:
    yc=(exp(2*x)+2*exp(x)-3)/(4*x)
    assert yc>x
    for y in [x, (x+yc)/2, yc*1.25]:
        k=sparse_K(x,y)
        for n in [250,1000,5000]:
            if y/n>=.5:continue
            d=float(finite_ratio(n,F(x/n),F(y/n)))
            assert abs(d-k)<max(.02,2.5*(1+x+y)**3/n),(x,y,n,k,d)
            checks+=1
print('PASS',checks,'rational enumerations, sign order checks, asymptotic approximations')
for n,t,s in [(8,.03,.3),(12,.03,.3),(50,.01,.12),(300,.005,.03)]:
 print(n,t,s,'covariance',float(closed(n,F(t),F(s))),'tcrit',critical(n))
