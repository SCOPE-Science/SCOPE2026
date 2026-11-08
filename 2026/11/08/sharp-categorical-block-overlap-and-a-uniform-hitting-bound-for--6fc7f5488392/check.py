"""Exact finite checks for categorical-window overlap and the lazy-walk formula."""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import sqrt, log, exp, pi

checks=0

def ok(condition, label):
    global checks
    assert condition, label
    checks += 1


def extremes(q,b):
    a=1-(q-1)*b
    assert 0<b<Fraction(1,q)
    v=[]
    for i in range(q):
        z=[b]*q; z[i]=a; v.append(tuple(z))
    return v


def product_overlap(q,b,d):
    E=extremes(q,b); A,B=E[:2]
    total=Fraction(0)
    for w in product(range(q),repeat=d):
        x=y=Fraction(1)
        for t in w: x*=A[t];y*=B[t]
        total+=min(x,y)
    return total


def weighted_product(q,b,d,x,y):
    E=extremes(q,b); A,B=E[:2]
    total=Fraction(0)
    for w in product(range(q),repeat=d):
        u,v=x,y
        for t in w: u*=A[t];v*=B[t]
        total+=min(u,v)
    return total


def dynamic_min(q,b,depth,x,y):
    E=extremes(q,b)
    @lru_cache(None)
    def f(d,x,y):
        if d==0: return min(x,y)
        return min(sum(f(d-1,x*P[j],y*Q[j]) for j in range(q)) for P in E for Q in E)
    return f(depth,x,y)


def multinomial_overlap(q,b,d):
    from math import factorial
    a=1-(q-1)*b; out=Fraction(0)
    for k in range(d+1):
        for ell in range(d-k+1):
            r=d-k-ell
            mult=factorial(d)//(factorial(k)*factorial(ell)*factorial(r))
            out += mult*(q-2)**r * a**min(k,ell)*b**(d-min(k,ell))
    return out


def lazy_overlap(q,b,d):
    a=float(1-(q-1)*b);b=float(b)
    theta=(q-2)*b+2*sqrt(a*b)
    u=sqrt(a*b)/theta;t=log(a/b)/2
    dist={0:1.0}
    for _ in range(d):
        nxt={}
        for s,p in dist.items():
            for off,prob in ((-1,u),(0,1-2*u),(1,u)):
                nxt[s+off]=nxt.get(s+off,0)+p*prob
        dist=nxt
    return theta**d*sum(v*exp(-t*abs(k)) for k,v in dist.items())

for q,b in ((3,Fraction(1,10)),(3,Fraction(1,7)),(4,Fraction(1,12)),(5,Fraction(1,10))):
    for d in range(1,6):
        c=product_overlap(q,b,d)
        ok(c==multinomial_overlap(q,b,d),(q,b,d,'multinomial'))
        ok(abs(float(c)-lazy_overlap(q,b,d))<1e-12,(q,b,d,'lazy'))
        if d>=2:
            ok(c<product_overlap(q,b,d-1),(q,b,d,'strict'))
    for d in range(1,4):
        for x,y in ((Fraction(1),Fraction(1)),(Fraction(1),Fraction(2)),(Fraction(3),Fraction(2)),(Fraction(1,3),Fraction(7,5))):
            if q>=5 and d==3:continue
            res=dynamic_min(q,b,d,x,y)
            ok(res==weighted_product(q,b,d,x,y),(q,b,d,x,y,'adaptive minima'))

# Verify an arbitrary (non-extreme) q-ary sliding-window chain against the sharp bound.
from random import Random
rng=Random(137)
for q,d,b in ((3,2,Fraction(1,10)),(3,3,Fraction(1,7)),(4,2,Fraction(1,12))):
    words=list(product(range(q),repeat=d))
    for trial in range(24):
        rows={}
        for w in words:
            zz=[rng.randrange(1,15) for _ in range(q)]
            spare=1-q*b
            rows[w]=tuple(b+spare*Fraction(z,sum(zz)) for z in zz)
        laws={}
        for state in words:
            dist={state:Fraction(1)}
            for _ in range(d):
                new={}
                for old,wt in dist.items():
                    for sym,pr in enumerate(rows[old]):
                        nxt=old[1:]+(sym,)
                        new[nxt]=new.get(nxt,Fraction(0))+wt*pr
                dist=new
            laws[state]=dist
        c=product_overlap(q,b,d)
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                ov=sum(min(laws[words[i]].get(w,0),laws[words[j]].get(w,0)) for w in words)
                ok(ov>=c,(q,d,trial,'transition bound'))
    # Realize equality with oldest-symbol kernel.
    E=extremes(q,b); uniform=tuple([Fraction(1,q)]*q)
    def row(w):return E[0] if w[0]==0 else E[1] if w[0]==1 else uniform
    laws=[]
    for init in ((0,)*d,(1,)*d):
        dist={init:Fraction(1)}
        for _ in range(d):
            new={}
            for old,wt in dist.items():
                for sym,pr in enumerate(row(old)):
                    nxt=old[1:]+(sym,)
                    new[nxt]=new.get(nxt,Fraction(0))+wt*pr
            dist=new
        laws.append(dist)
    ok(sum(min(laws[0][w],laws[1][w]) for w in words)==product_overlap(q,b,d),'attainment')

# Check convergence towards the sharp local-limit constant numerically.
for q,b in ((3,0.10),(3,0.14),(4,0.08)):
    a=1-(q-1)*b;theta=(q-2)*b+2*sqrt(a*b);u=sqrt(a*b)/theta
    t=0.5*log(a/b)
    K=(1+exp(-t))/(1-exp(-t))/sqrt(4*pi*u)
    for d in (250,1000,2500):
        if theta**d>1e-250:
            ratio=lazy_overlap(q,Fraction(str(b)),d)/(theta**d/sqrt(d)*K)
            ok(abs(ratio-1)<0.1,(q,b,d,ratio))

print('PASS',checks,'exact/finite checks')
