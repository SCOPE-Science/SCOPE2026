#!/usr/bin/env python3
"""Exact rational checks for a star-fusion residual in complete-pair variation."""
from fractions import Fraction as F
from itertools import product
import random


def gini(a):
    return sum(abs(a[i]-a[j]) for i in range(len(a)) for j in range(i+1,len(a)))


def clip(v,c):
    return min(c,max(-c,v))


def star_prox(x,c):
    # All quantities exact. c holds positive edge penalties, including lambda.
    n=len(x)
    assert len(c)==n-1 and all(v>0 for v in c)
    def equation(u):
        return u-x[0]-sum((clip(x[i]-u,c[i-1]) for i in range(1,n)),F(0))
    endpoints=sorted(set([x[0]]+[v+d for v,d in zip(x[1:],c)]+[v-d for v,d in zip(x[1:],c)]))
    lo=min(endpoints)-sum(c)-1
    hi=max(endpoints)+sum(c)+1
    marks=[lo]+endpoints+[hi]
    for l,r in zip(marks,marks[1:]):
        fl,fr=equation(l),equation(r)
        if fl==0:u=l;break
        if fr==0:u=r;break
        if fl<0<fr:
            u=l-fl*(r-l)/(fr-fl)
            assert equation(u)==0
            break
    else:raise ValueError('No root')
    fit=[u]
    for i in range(1,n):
        v=x[i]-u
        fit.append(u if abs(v)<=c[i-1] else x[i]-clip(v,c[i-1]))
    # KKT verified independently of construction:
    q=[clip(x[i]-u,c[i-1]) for i in range(1,n)]
    assert fit[0]-x[0]-sum(q)==0
    for i in range(1,n):
        assert fit[i]-x[i]+q[i-1]==0
        if fit[i]>u:assert q[i-1]==c[i-1]
        if fit[i]<u:assert q[i-1]==-c[i-1]
    return fit


def center_block(h,m):
    mean=sum(h[:m],F(0))/m
    return [v-mean for v in h[:m]]+[F(0)]*(len(h)-m)


def formula(n,m):
    return F((m-1)*(2*n-m),m*(n-1))


def upper(n):
    return max(formula(n,m) for m in range(2,n+1))


def run():
    checks=0
    for n in range(2,19):
        exact=upper(n)
        m_star=[m for m in range(2,n+1) if formula(n,m)==exact]
        assert all(m*(m-1)<=2*n<=m*(m+1) for m in m_star)
        for m in range(2,n+1):
            actual=F(0)
            # All inequivalent binary inputs, including all outsider occupancies.
            for j in range(m+1):
                for t in range(n-m+1):
                    s=j+t
                    if s==0 or s==n:continue
                    h=[F(1)]*j+[F(0)]*(m-j)+[F(1)]*t+[F(0)]*(n-m-t)
                    actual=max(actual,gini(center_block(h,m))/gini(h))
                    checks+=1
            assert actual==formula(n,m),(n,m,actual,formula(n,m))
        for m in m_star:
            # Construct an actual strictly complementary primal-dual region.
            c=[F(1+i%3,2) for i in range(n-1)]
            base_y=[F(0)]*m+[F(10+i) for i in range(n-m)]
            base_x=base_y[:]
            # Every inactive leaf is above the hub: positive dual edge force.
            for i in range(m,n):base_x[i]+=c[i-1]
            base_x[0]-=sum(c[i-1] for i in range(m,n))
            fit0=star_prox(base_x,c)
            assert fit0==base_y
            eps=F(1,10000)
            x2=base_x[:]
            x2[1]+=eps
            fit1=star_prox(x2,c)
            residual0=[a-b for a,b in zip(base_x,fit0)]
            residual1=[a-b for a,b in zip(x2,fit1)]
            dr=[a-b for a,b in zip(residual1,residual0)]
            din=[a-b for a,b in zip(x2,base_x)]
            assert gini(dr)/gini(din)==exact,(n,m,dr,din)
    print('EXACT_ALL_BLOCK_BINARY_CUTS_AND_OPTIMAL_INTEGER_SIZES_PASSED',checks)
    print('EXACT_STRICT_COMPLEMENTARITY_SHARP_TWO_INPUT_WITNESSES_PASSED')
    rng=random.Random(90231)
    cases=0
    for n in range(2,22):
        C=upper(n)
        for _ in range(75):
            c=[F(rng.randint(1,8),rng.randint(1,5)) for i in range(n-1)]
            x=[F(rng.randint(-15,15),rng.randint(1,3)) for i in range(n)]
            z=[F(rng.randint(-15,15),rng.randint(1,3)) for i in range(n)]
            y=star_prox(x,c); w=star_prox(z,c)
            r=[a-b for a,b in zip(x,y)]
            s=[a-b for a,b in zip(z,w)]
            assert gini([a-b for a,b in zip(r,s)])<=C*gini([a-b for a,b in zip(x,z)])
            cases+=1
    print('EXACT_RANDOM_ACTUAL_NONLINEAR_TWO_INPUT_CHECKS_PASSED',cases)
    assert all(upper(n)==F(1) for n in (2,3))
    assert all(upper(n)>F(1) for n in range(4,100))
    print('SHARP_FIRST_AMPLIFICATION_DIMENSION_FOUR_PASSED')
    print('ALL_STAR_FUSION_RESIDUAL_CHECKS_PASSED')

if __name__=='__main__':run()
