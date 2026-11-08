#!/usr/bin/env python3
"""Independent finite-state checks for Bernoulli recursive-tree metric limits.

Run with: python3 check.py
Requires Python 3.9+ standard library only.
"""
from fractions import Fraction
from itertools import product
from math import comb, log
import random

checks=0

def ok(condition, label):
    global checks
    checks+=1
    if not condition:
        raise AssertionError(label)


def build(bits):
    # vertices 0..n, with parent of 1 equal to 0
    parent=[-1,0]
    height=[0,1]
    x=[1]
    for k,b in enumerate(bits,start=2):
        ancestor=k-1 if b else k-2
        parent.append(ancestor)
        height.append(height[ancestor]+1)
        x.append(height[k]-height[k-1])
    return parent,height,x


def dist(parent, a, b):
    heights=[0]*len(parent)
    for i in range(1,len(parent)):heights[i]=heights[parent[i]]+1
    seen=set()
    t=a
    while t!=-1:
        seen.add(t)
        t=parent[t]
    t=b
    while t not in seen:t=parent[t]
    return heights[a]+heights[b]-2*heights[t]


def total_distance_by_edges(parent):
    n=len(parent)-1
    childsize=[1]*(n+1)
    for i in range(n,0,-1):childsize[parent[i]]+=childsize[i]
    return sum(childsize[i]*(n+1-childsize[i]) for i in range(1,n+1))

for n in range(2,14):
    for bits in product((0,1),repeat=n-1):
        parent,height,x=build(bits)
        ok(all(v in (0,1) for v in x),'increments binary')
        ok(all(x[k-1]==(1 if bits[k-2] else 1-x[k-2]) for k in range(2,n+1)),'recurrence')
        ok(height[-1]==sum(x),'height sum')
        last_success=1
        runmax=0
        for k in range(2,n+1):
            if bits[k-2]:last_success=k
            runmax=max(runmax,k-last_success)
        ok(runmax <= n-1,'run max bound')
        total=0
        for i in range(n+1):
            for j in range(i+1,n+1):
                d=dist(parent,i,j)
                ok(0<=d-(height[j]-height[i])<=2*(1+runmax),'uniform metric error')
                total+=d
        ok(total==total_distance_by_edges(parent),'tree edge-cut sum')
        ok(abs(max(dist(parent,i,j) for i in range(n+1) for j in range(i+1,n+1))-height[-1])<=2*(1+runmax),'diameter bound')

for p in [Fraction(1,4),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(3,4)]:
    q=1-p
    mu=1/(1+q)
    sig2=p*q/(1+q)**3
    ok(sig2>0,'positive asymptotic variance')
    for n in range(2,12):
        expectation=Fraction(0)
        second=Fraction(0)
        totalprob=Fraction(0)
        for bits in product((0,1),repeat=n-1):
            k=sum(bits)
            prob=p**k*q**(n-1-k)
            _,height,_=build(bits)
            totalprob+=prob
            expectation+=prob*height[-1]
            second+=prob*height[-1]**2
        ok(totalprob==1,'prob sums to 1')
        predicted_mean=n*mu+(1-mu)*(1-(-q)**n)/(1+q)
        ok(expectation==predicted_mean,'exact height mean')
        means=[mu+(1-mu)*(-q)**(i-1) for i in range(1,n+1)]
        var_pred=Fraction(0)
        for i in range(n):
            vi=means[i]*(1-means[i])
            var_pred+=vi*(1+2*sum((-q)**k for k in range(1,n-i)))
        ok(second-expectation**2==var_pred,'exact height variance')

# A non-asymptotic martingale identity for every choice sequence and rational p.
for p in [Fraction(1,4),Fraction(1,2),Fraction(3,4)]:
    q=1-p
    mu=1/(1+q)
    for n in range(2,13):
        for bits in product((0,1),repeat=n-1):
            _,height,x=build(bits)
            yy=[v-mu for v in x]
            mart=sum(yy[i]+q*yy[i-1] for i in range(1,n))
            ok((1+q)*(height[-1]-n*mu)==mart+yy[0]+q*yy[-1], 'bounded remainder decomposition')

# Coarse numerical confirmation of the rate and variance, no limit-proof claim.
prng=random.Random(751629)
p=0.4
q=1-p
mu=1/(1+q)
sig2=p*q/(1+q)**3
n=12000
reps=1200
scaled_heights=[]
for rep in range(reps):
    x=1
    h=1
    for _ in range(2,n+1):
        b=prng.random()<p
        x=1 if b else 1-x
        h+=x
    scaled_heights.append((h-n*mu)/(n**0.5))
empmean=sum(scaled_heights)/reps
empvar=sum((v-empmean)**2 for v in scaled_heights)/reps
ok(abs(empmean)<0.045,'height CLT sample mean')
ok(abs(empvar-sig2)<0.035,'height CLT sample variance')
print('PASS',checks,'assertions; asymptotic height sample mean',round(empmean,6),'sample variance',round(empvar,6),'theory',round(sig2,6))
# Verify the distinct all-pairs distance statistic using the exact edge-cut formula.
n2=4000
reps2=1500
pair_scaled=[]
for rep in range(reps2):
    bits=[prng.random()<p for _ in range(2,n2+1)]
    parents,depths,_=build(bits)
    k=2*total_distance_by_edges(parents)/(n2*(n2+1))
    pair_scaled.append((k/n2-mu/3)*(n2**0.5))
mp=sum(pair_scaled)/reps2
vp=sum((v-mp)**2 for v in pair_scaled)/reps2
ok(abs(mp)<0.055,'pairwise-distance sample mean')
ok(abs(vp-2*sig2/15)<0.025,'pairwise-distance sample variance')
print('PASS',checks,'total assertions; mean-distance sample mean',round(mp,6),'sample variance',round(vp,6),'theory',round(2*sig2/15,6))
