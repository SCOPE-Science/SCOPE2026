"""Exact-rational supplementary tests for two-stage stationary-risk boundary.
Only the proof, not these finite tests, establishes the universal statements.
Requires Python 3 standard library only.
"""
from fractions import Fraction as Q
import random

def risk(m,h,noise_ratio):
    y=m-h
    return (1-m)*(1-y)*(1+noise_ratio/y**2)/((1+y)*(1+m-2*y))

def fixed_point_covariance(m,h,F,vj,va):
    y=m-h
    s=y/F
    v= s*s*vj+va
    return v*(1-y)/((1+y)*((1-y)**2-h*h))

def first_order_threshold(m,y):
    P=2*y-y*y-m
    D=(1+m-2*y)*(1-y*y)-y*P
    return y**3*P/D

def assert_rat_positive(z):
    assert z>0, z

rng=random.Random(154927)
count=0
# Independent Lyapunov system check, residuals and CV identity.
for _ in range(12000):
    m=Q(rng.randint(1,98),100)
    h=m*Q(rng.randint(0,98),100)
    F=Q(rng.randint(101,400),100)
    b=Q(rng.randint(1,40),10)
    vj=Q(rng.randint(1,80),1000)
    va=Q(rng.randint(0,80),1000)
    s=(m-h)/F
    c22=fixed_point_covariance(m,h,F,vj,va)
    c12=F*h*c22/(1-F*s)
    c11=F*F*c22+vj
    assert c12==F*s*c12+F*h*c22
    assert c22==s*s*c11+2*s*h*c12+h*h*c22+va
    mean=s*b/(1-m)
    assert c22/(mean*mean) == vj/(b*b)*risk(m,h,F*F*va/vj)
    count+=3

# Test exact derivative factorization by rational finite symbol difference:
# For R(y) with rational q, its sign matches sign(qstar(y)-q)
# while y>y0 and D>0; check via numerator expression.
for _ in range(12000):
    m=Q(rng.randint(1,98),100)
    y=Q(rng.randint(1,999),1000)*m
    q=Q(rng.randint(1,300),1000)
    T_num=2*y-y*y-m
    D=(1+m-2*y)*(1-y*y)-y*T_num
    # d/dy log R /2
    der=T_num/((1+m-2*y)*(1-y*y))-q/(y*(y*y+q))
    if T_num<=0:
        assert der<0
    elif D<=0:
        assert der>0
    else:
        test=first_order_threshold(m,y)-q
        assert (der>0)==(test>0)
        assert (der<0)==(test<0)
    count+=1

m=Q(1,2)
y=Q(1,3)
assert first_order_threshold(m,y)==Q(1,351)
assert risk(m,m-y,Q(1,351))<risk(m,Q(0),Q(1,351))
assert first_order_threshold(m,m)==Q(1,8)
count+=3

# Unimodal finite grids of risk: exact rational. Skip equality parameters.
for mm in [Q(1,5),Q(1,2),Q(7,10),Q(4,5),Q(9,10)]:
    for qq in [Q(1,10000),Q(1,351),Q(1,10),Q(1),Q(100)]:
        grid=[mm*Q(i,400) for i in range(1,401)]
        values=[risk(mm,mm-y,qq) for y in grid]
        minidx=min(range(len(values)),key=lambda i:values[i])
        assert all(values[i]>values[i+1] for i in range(minidx))
        assert all(values[i]<values[i+1] for i in range(minidx,len(values)-1))
        count+=len(values)-1
print('PASS',count,'exact rational assertions')
