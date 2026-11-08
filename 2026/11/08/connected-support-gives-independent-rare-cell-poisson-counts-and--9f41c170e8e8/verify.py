#!/usr/bin/env python3
"""Reproduce finite checks for rare-cell limits of margin-conditioned Poisson tables.
Only Python standard library is needed. Finite tests do not replace the analytic limit proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial, exp, lgamma, log, sqrt


def tables(d, n):
    """All d-by-d nonnegative integer matrices with each margin n."""
    counts = [n]*d
    rows=[]
    def compositions(total, caps, j=0, cur=None):
        cur=[] if cur is None else cur
        if j == d-1:
            if 0 <= total <= caps[j]:
                yield tuple(cur+[total])
            return
        for k in range(min(total,caps[j])+1):
            yield from compositions(total-k,caps,j+1,cur+[k])
    def rec(i):
        if i == d:
            if not any(counts):
                yield tuple(rows)
            return
        for row in compositions(n,counts):
            for j,v in enumerate(row): counts[j]-=v
            rows.append(row)
            yield from rec(i+1)
            rows.pop()
            for j,v in enumerate(row): counts[j]+=v
    yield from rec(0)


def weight_direct(t, n, theta):
    val=Fraction(1)
    for i,row in enumerate(t):
        for j,x in enumerate(row):
            val*=Fraction(1,factorial(x))
            if i==j:
                val*=Fraction(theta[i],n)**x
    return val


def weight_poisson_tilt(t,n,theta):
    d=len(t); q=Fraction(n,d-1)
    val=Fraction(1)
    for i,row in enumerate(t):
        for j,x in enumerate(row):
            mean=Fraction(theta[i],d-1) if i==j else q
            val*=mean**x / factorial(x)
    return val


def check_exact_weights():
    checked=0
    for d,n,theta in ((3,1,(1,2,3)),(3,2,(1,2,3)),(3,3,(1,2,3)),(3,4,(1,2,3)),(4,1,(1,2,3,4)),(4,2,(1,2,3,4))):
        base=Fraction(n,d-1)**(d*n)
        ntable=0
        for t in tables(d,n):
            a=weight_direct(t,n,theta)
            b=weight_poisson_tilt(t,n,theta)
            assert b==a*base,(d,n,t,a,b)
            checked+=1;ntable+=1
        assert ntable>0
        print('exact conditional factorization:',d,'x',d,'margin',n,'tables',ntable)
    return checked


def bessel_tv(n,alpha):
    masses=[]; limit=[]; fall=1.; term=1.
    for k in range(120):
        if k>0:term*=alpha/(k*k)
        limit.append(term)
        if k<=n:
            if k:fall*=1-(k-1)/n
            masses.append(term*fall*fall)
    A=sum(masses); B=sum(limit)
    return (sum(abs(x/A-y/B) for x,y in zip(masses,limit))
            +sum(limit[n+1:])/B)/2


def three(n,theta):
    weights=[]; records=[]
    for k in product(range(n+1),repeat=3):
        a,b,c=k
        for t in range(n+1):
            tab=((a,t,n-a-t),
                 (n-a-b+c-t,b,a-c+t),
                 (b-c+t,n-b-t,c))
            if any(z<0 for row in tab for z in row):continue
            logw=sum(k[i]*log(theta[i]/n) for i in range(3))-sum(lgamma(z+1) for row in tab for z in row)
            records.append((k,t));weights.append(logw)
    maxw=max(weights)
    weights=[exp(v-maxw) for v in weights]
    z=sum(weights)
    means=[0.,0.,0.];cyclevar=0.
    for (k,t),v in zip(records,weights):
        for i in range(3):means[i]+=k[i]*v/z
        cyclevar+=(t-n/2)**2*v/z/n
    return means,cyclevar


def checks():
    num=check_exact_weights()
    prev=1.
    for n in (3,6,12,30,60):
        tv=bessel_tv(n,.6*.9)
        print('two-block Bessel total variation',n,round(tv,9))
        assert tv<prev
        prev=tv;num+=1
    prev=[float('inf')]*3;pv=float('inf')
    for n in (3,5,8,12):
        mu,v=three(n,(.6,.9,1.4))
        diff=[abs(mu[i]-x) for i,x in enumerate((.3,.45,.7))]
        print('three-block means',n,tuple(round(x,7) for x in mu),'cycle variance/n',round(v,7))
        assert all(diff[i]<prev[i] for i in range(3))
        assert abs(v-1/12)<pv
        prev=diff;pv=abs(v-1/12);num+=4
    # Exact incidence rank via rational Gaussian elimination.
    def rank(M):
        M=[[Fraction(x) for x in r] for r in M]
        if not M:return 0
        k=0
        for j in range(len(M[0])):
            piv=next((i for i in range(k,len(M)) if M[i][j]),None)
            if piv is None:continue
            M[k],M[piv]=M[piv],M[k]
            a=M[k][j]
            M[k]=[x/a for x in M[k]]
            for i in range(len(M)):
                if i!=k and M[i][j]:
                    b=M[i][j];M[i]=[x-b*y for x,y in zip(M[i],M[k])]
            k+=1
        return k
    for d in (2,3,4,5,6):
        E=[(i,j) for i in range(d) for j in range(d) if i!=j]
        B=[[int(i==v) for i,j in E] for v in range(d)] + [[int(j==v) for i,j in E] for v in range(d-1)]
        r=rank(B)
        assert r==2*d-1 if d>=3 else r==2
        print('off-diagonal support incidence rank',d,r,'of',2*d-1)
        num+=1
    # Exact covariance projection for the K_{d,d} minus diagonal support.
    def inverse(M):
        n=len(M);M=[[Fraction(x) for x in row]+[Fraction(i==j) for j in range(n)] for i,row in enumerate(M)]
        for j in range(n):
            k=next(i for i in range(j,n) if M[i][j])
            M[j],M[k]=M[k],M[j]
            a=M[j][j];M[j]=[x/a for x in M[j]]
            for i in range(n):
                if i!=j:
                    a=M[i][j];M[i]=[u-a*v for u,v in zip(M[i],M[j])]
        return [row[n:] for row in M]
    for d in (3,4,5):
        edges=[(i,j) for i in range(d) for j in range(d) if i!=j]
        R=2*d-1; q=Fraction(1,d-1); M=len(edges)
        B=[[Fraction(i==v) for i,j in edges] for v in range(d)] + [[Fraction(j==v) for i,j in edges] for v in range(d-1)]
        Q=[[q*sum(B[a][i]*B[b][i] for i in range(M)) for b in range(R)] for a in range(R)]
        inv=inverse(Q)
        Sigma=[[q*Fraction(i==j)-q*q*sum(B[a][i]*inv[a][b]*B[b][j] for a in range(R) for b in range(R)) for j in range(M)] for i in range(M)]
        assert all(sum(B[a][i]*Sigma[i][j] for i in range(M))==0 for a in range(R) for j in range(M))
        if d==3: assert Sigma[0][0]==Fraction(1,12)
        print('exact covariance projection',d,'edge fluctuation variance',Sigma[0][0])
        num+=R*M + 1
    print('PASS',num,'exact-table and asymptotic-consistency checks')

if __name__=='__main__':checks()
