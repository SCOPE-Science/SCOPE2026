"""Exact independent checks for random dimer adsorption on complete-graph coronas.
Dependencies: Python >= 3.9 standard library only.
"""
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
from math import log, sqrt


def reduced(n, w):
    w=Fraction(w)
    rows=[{0:Fraction(1)}, {1:Fraction(1)}]
    for k in range(2,n+1):
        p=2*w/(k-1+2*w)
        v=defaultdict(Fraction)
        for j,mass in rows[k-1].items():
            v[j+1]+=p*mass
        for j,mass in rows[k-2].items():
            v[j]+=(1-p)*mass
        rows.append(dict(v))
    return rows[n]


def labeled(n,w):
    w=Fraction(w)
    edges=[(i,j,Fraction(1),False) for i in range(n) for j in range(i+1,n)]
    edges +=[(i,n+i,w,True) for i in range(n)]
    @lru_cache(None)
    def solve(mask):
        viable=[(i,j,rate,isleaf) for i,j,rate,isleaf in edges if (mask & (1<<i)) and (mask & (1<<j))]
        if not viable: return {0:Fraction(1)}
        s=sum((e[2] for e in viable),Fraction(0))
        out=defaultdict(Fraction)
        for i,j,rate,isleaf in viable:
            sub=solve(mask^(1<<i)^(1<<j))
            for c,p in sub.items():out[c+int(isleaf)]+=(rate/s)*p
        return dict(out)
    return solve((1<<(2*n))-1),solve.cache_info()


def mu_exact(n):
    return sum((Fraction(1,k if k%2 else k+1) for k in range(1,n+1)),Fraction(0))


def check():
    tests=0
    for w in [Fraction(1,3),Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2),Fraction(5)]:
      for n in range(1,8):
        a=reduced(n,w)
        b,info=labeled(n,w)
        assert a==b,(n,w,a,b)
        assert sum(a.values())==1
        assert all(k%2==n%2 for k in a)
        assert all(0<=k<=n for k in a)
        tests+=4
        if w==1:
            mean=sum((k*p for k,p in a.items()),Fraction(0))
            assert mean==mu_exact(n),(n,mean,mu_exact(n))
            tests+=1
    for n in range(1,61):
        a=reduced(n,Fraction(1))
        assert sum((k*p for k,p in a.items()),Fraction(0))==mu_exact(n)
        tests+=1
    for w in [Fraction(1,2),Fraction(1),Fraction(2)]:
        for n in [100,400,1000,2000]:
            # moment recursion avoids large rational distribution
            mu0=0.;mu1=1.
            v0=0.;v1=0.
            for k in range(2,n+1):
                p=2*float(w)/(k-1+2*float(w))
                mk=p*(1+mu1)+(1-p)*mu0
                sk=p*(1+2*mu1+v1+mu1**2)+(1-p)*(v0+mu0**2)
                vk=sk-mk*mk
                mu0,mu1=mu1,mk
                v0,v1=v1,vk
            assert abs(float(mu1)-float(w)*log(n))<4+float(w)*3
            assert abs(float(v1)-float(w)*log(n))<4+float(w)*3
            tests+=2
    print('PASS', tests, 'exact and numerical assertions')
    for n in [10,20,100,1000]:
        a=reduced(n,Fraction(1)) if n<101 else None
        print('n',n, 'mean',float(mu_exact(n)), 'log_n',log(n))

if __name__=='__main__': check()
