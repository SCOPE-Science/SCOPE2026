#!/usr/bin/env python3
"""Independent finite checks for regular-hexagon vertex-average quantization."""
import math
import itertools
import random

SQ3=math.sqrt(3.)
STEPS=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))

def formula_first(r):
    if r<=0: return 0.
    if r>=1: return 1.
    if r<=.5: return 4*math.pi*r*r/(3*SQ3)
    return 4/SQ3*(r*r*(math.asin(1/(2*r))-math.pi/6)+math.sqrt(4*r*r-1)/4)

def formula_refined(r):
    if r<=0: return 0.
    if r>=1/SQ3: return 1.
    if r<=.5: return 2*math.pi*r*r/SQ3
    return 2/SQ3*(math.pi*r*r-6*r*r*math.acos(1/(2*r))+3*math.sqrt(r*r-.25))

def lattice_points(k):
    return {(a,b) for a in range(-k,k+1) for b in range(-k,k+1)
            if max(abs(a),abs(b),abs(a+b))<=k}

def euclidean(t):
    a,b=t
    return (a+b/2., SQ3*b/2.)

def candidates(k):
    return {(sum(z[0] for z in bag),sum(z[1] for z in bag))
            for bag in itertools.combinations_with_replacement(STEPS,k)}

for k in range(1,10):
    actual=candidates(k)
    target=lattice_points(k)
    assert actual== (target-{(0,0)} if k==1 else target), (k,len(actual),len(target))
    assert len(actual)==(6 if k==1 else 3*k*(k+1)+1)

for F,limit,want in ((formula_first,1,.25),(formula_refined,1/SQ3,5/36)):
    n=20000
    dx=limit/n
    moment=sum(2*(i+.5)*dx*dx*(1-F((i+.5)*dx)) for i in range(n))
    assert abs(moment-want)<0.000001,(moment,want)
    assert abs(F(limit)-1)<1e-12

# Independently sample uniform points in one central sector of the hexagon;
# compare empirical nearest distances against the closed CDF and second moment.
rng=random.Random(140513)
for k in range(1,7):
    nodes=[(a/k,b/k) for a,b in map(euclidean,candidates(k))]
    arr=[]
    for _ in range(12000):
        a,b=rng.random(),rng.random()
        if a+b>1: a,b=1-a,1-b
        x=a+b/2; y=SQ3*b/2
        arr.append(k*math.sqrt(min((x-u)**2+(y-v)**2 for u,v in nodes)))
    ref=formula_first if k==1 else formula_refined
    for r in ((.25,.4,.65,.85) if k==1 else (.15,.3,.45,.55)):
        err=abs(sum(x<=r for x in arr)/len(arr)-ref(r))
        assert err<.017,(k,r,err)
    moment=sum(x*x for x in arr)/len(arr)
    assert abs(moment-(.25 if k==1 else 5/36))<.014,(k,moment)

print('PASS: exhaustive lattice-site identities for k=1..9, CDF-derived exact moments, randomized direct geometric tests for k=1..6.')
