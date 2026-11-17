#!/usr/bin/env python3
"""Reproducibility checks for the exact short-chord law of convex polygons.

Standard Python library only. The analytic proof, not the computations, establishes
all polygon and all side-count statements.
"""
import bisect
import math
import random


def geometry(vertices):
    v = [tuple(map(float, x)) for x in vertices]
    n = len(v)
    vectors = [(v[(i+1)%n][0]-v[i][0], v[(i+1)%n][1]-v[i][1]) for i in range(n)]
    lengths = [math.hypot(*e) for e in vectors]
    unit = [(a/b, c/b) for (a,c), b in zip(vectors, lengths)]
    turns = []
    for i in range(n):
        u, w = unit[i], unit[(i+1)%n]
        turn = math.atan2(u[0]*w[1]-u[1]*w[0],u[0]*w[0]+u[1]*w[1])
        assert 0 < turn < math.pi
        turns.append(turn)
    assert abs(sum(turns)-2*math.pi) < 1e-10
    return (v,vectors,lengths,turns)


def coefficient(turns):
    return sum(x/math.sin(x)-1 for x in turns)


def sharp_bound(turns):
    m=len(turns)
    mean=2*math.pi/m
    baseline=m*(mean/math.sin(mean)-1)
    variance=sum((x-mean)**2 for x in turns)
    return baseline+variance/6


def sample(vertices, count, r, seed):
    v, vectors, lengths, turns=geometry(vertices)
    p=sum(lengths)
    cumulative=[]
    t=0.0
    for length in lengths:
        t+=length
        cumulative.append(t)
    rng=random.Random(seed)
    def draw():
        pos=rng.random()*p
        i=bisect.bisect_left(cumulative,pos)
        if i==len(v): i-=1
        offset=pos-(cumulative[i-1] if i else 0)
        factor=offset/lengths[i]
        return (v[i][0]+factor*vectors[i][0],v[i][1]+factor*vectors[i][1])
    successes=0
    for _ in range(count):
        x=draw()
        y=draw()
        successes+=math.dist(x,y)<r
    empirical=successes/count
    predicted=2*r/p+coefficient(turns)*(r/p)**2
    se=math.sqrt(predicted*(1-predicted)/count)
    assert abs(empirical-predicted)<5*se, (empirical,predicted,se)
    return empirical,predicted,se


def test():
    shapes=[
        [(0,0),(1,0),(.5,math.sqrt(3)/2)],
        [(0,0),(2,0),(2,1),(0,1)],
        [(0,0),(3,0),(2.5,1.1),(.7,2)],
        [(0,0),(4,0),(4,1),(2.6,2.1),(.2,1.4)],
    ]
    n_trials=270000
    for j,poly in enumerate(shapes):
        v,vec,lengths,turns=geometry(poly)
        c=coefficient(turns)
        assert c+1e-12>=sharp_bound(turns)
        r=.05*min(lengths)*min(math.sin(x) for x in turns)
        empirical,predicted,se=sample(poly,n_trials,r,90351+j)
        print('shape',j,'short_probability',round(predicted,8),'observed',round(empirical,8),'z',round((empirical-predicted)/se,3))
    assert abs(coefficient(geometry(shapes[0])[3])-(4*math.pi/math.sqrt(3)-3))<1e-12
    assert abs(coefficient(geometry(shapes[1])[3])-(2*math.pi-4))<1e-12
    for n in (16,64,256,1024):
        b=2*math.pi/n
        eps=b/7
        turns=[b+eps if i%2==0 else b-eps for i in range(n)]
        value=coefficient(turns)
        baseline=n*(b/math.sin(b)-1)
        variance=n*eps*eps
        assert value+1e-9>=baseline+variance/6
        ratio=(value-baseline)/variance
        assert ratio>1/6-1e-5
        print('sharpness',n,round(ratio,10))
    print('VERIFY_OK convex_polygons=4 random_pairs=1080000 analytic_special_cases=2 sharpness_sizes=4')

if __name__=='__main__':
    test()
