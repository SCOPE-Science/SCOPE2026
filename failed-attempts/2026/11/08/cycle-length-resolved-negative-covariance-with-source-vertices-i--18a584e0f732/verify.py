"""Exact and numerical checks for cycle-length/zero-indegree covariance identities.
No external data or dependencies. Running this file recomputes all counts.
"""
from fractions import Fraction
from itertools import product
from math import factorial, exp, sqrt, pi

def cycles(f):
    n=len(f); done=[False]*n; counts=[0]*(n+1)
    for start in range(n):
        if done[start]: continue
        seen={}; path=[]; at=start
        while at not in seen and not done[at]:
            seen[at]=len(path); path.append(at); at=f[at]
        if at in seen: counts[len(path)-seen[at]]+=1
        for v in path: done[v]=True
    return counts

def b(m,j):
    if j>m or m==0: return Fraction(0)
    ans=Fraction(1)
    for r in range(j): ans*=Fraction(m-r,m)
    return ans

def falling(n,k):
    z=1
    for v in range(n-k+1,n+1): z*=v
    return z

def exact_verification(max_n=7):
    assertions=0; maps=0
    for n in range(2,max_n+1):
        sums=[0]*(n+1); mixed=[0]*(n+1)
        f2=[0]*(n+1); normZ=0; normZ2=0; cycMean=0; compMean=0
        count=n**n
        for f in product(range(n),repeat=n):
            maps+=1
            z=n-len(set(f)); c=cycles(f)
            normZ+=z
            normZ2+=z*(z-1)
            cycMean+=sum(j*c[j] for j in range(1,n+1))
            compMean+=sum(c)
            for j in range(1,n+1):
                sums[j]+=c[j]; mixed[j]+=z*c[j]; f2[j]+=z*(z-1)*c[j]
        q=Fraction(n-1,n)**n
        assert Fraction(normZ,count)==n*q; assertions+=1
        assert Fraction(normZ2,count)==falling(n,2)*Fraction(n-2,n)**n; assertions+=1
        for j in range(1,n+1):
            p=Fraction(b(n,j),j)
            expected= n*q*(b(n-1,j)-b(n,j))/j
            actual=Fraction(mixed[j],count)-Fraction(normZ,count)*Fraction(sums[j],count)
            assert Fraction(sums[j],count)==p,(n,j,'cycle expectation'); assertions+=1
            assert actual==expected,(n,j,'covariance',actual,expected); assertions+=1
            if n>=3:
                expected2=falling(n,2)*Fraction(n-2,n)**n*b(n-2,j)/j if n-2>0 else 0
                assert Fraction(f2[j],count)==expected2,(n,j,'factorial2'); assertions+=1
            assert (actual==0 if j==1 else actual<0),(n,j,'sign'); assertions+=1
        total_c= sum(j*mixed[j] for j in range(1,n+1))
        total_h= sum(mixed[1:])
        cov_c=Fraction(total_c,count)-Fraction(normZ,count)*Fraction(cycMean,count)
        cov_h=Fraction(total_h,count)-Fraction(normZ,count)*Fraction(compMean,count)
        assert cov_c==n*q*sum(b(n-1,j)-b(n,j) for j in range(1,n+1)); assertions+=1
        assert cov_h==n*q*sum((b(n-1,j)-b(n,j))/j for j in range(1,n+1)); assertions+=1
        print(f'n={n}: {count} maps, exact assertions passed; cov(Z,H)={float(cov_h):.8f}; cov(Z,C)={float(cov_c):.8f}')
    return assertions,maps

def approximate_cov(n):
    A=1.; D=1.; cq=0.; cc=0.
    q=(1-1/n)**n
    for j in range(1,n+1):
        if j>1:
            A*=1-(j-1)/n
            D*=max(0,1-(j-1)/(n-1))
        delta=A-D
        cq-=n*q*delta
        cc-=n*q*delta/j
        if j>=3 and A<1e-16: break
    return cc,cq

if __name__=='__main__':
    asserts,maps=exact_verification()
    print('Exact assertions:',asserts,'maps enumerated:',maps)
    for n in [50,200,1000,10000,100000]:
        h,c=approximate_cov(n)
        print(n,'component covariance',h,'limit',-1/(2*exp(1)),'cyclic covariance / sqrt(n)',c/sqrt(n),'limit',-sqrt(pi/8)/exp(1))


def mesoscopic_checks():
    n=10000
    for x in [0.5,1.0,2.0]:
        j=round(x*sqrt(n))
        a=1.0; c=1.0
        for r in range(1,j):
            a*=1-r/n
            c*=1-r/(n-1)
        observed=sqrt(n)*n*((n-1)/n)**n*(c-a)/j
        limit=-x*exp(-x*x/2)/(2*exp(1))
        assert abs(observed-limit)<0.003, (n,x,observed,limit)
    h,cyc=approximate_cov(n)
    assert abs(h+1/(2*exp(1)))<0.005
    assert abs(cyc/sqrt(n)+sqrt(pi/8)/exp(1))<0.005
    print('Mesoscopic diagnostics: 3 tests passed; aggregate asymptotic diagnostics: 2 passed.')

mesoscopic_checks()
