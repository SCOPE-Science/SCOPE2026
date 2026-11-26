#!/usr/bin/env python3
"""Exact exhaustive proof checker for odd periods <= 11 of F(x,y)=(1-y+|x|,x).

Only Python standard library integer/Fraction operations; no floating point.
For every possible n-symbol sign itinerary, the program builds the affine iterate,
adds the sign halfspaces and the two fixed-point equalities, and eliminates x,y
by exact Fourier--Motzkin elimination. A feasible word has a unique fixed point.
"""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import gcd

N_VALUES=(1,3,5,7,9,11)

def mm(A,B):
    return (A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3],
            A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3])

def normalize(v):
    gg=0
    for q in v:gg=gcd(gg,abs(q))
    if gg>1:return tuple(x//gg for x in v)
    return tuple(v)

def eliminate(inequalities,index):
    pos=[];neg=[];zero=[]
    for v in inequalities:
        (pos if v[index]>0 else neg if v[index]<0 else zero).append(v)
    out=set(zero)
    for p in pos:
        for m in neg:
            v=tuple((-m[index])*p[j]+p[index]*m[j] for j in range(3))
            assert v[index]==0
            out.add(normalize(v))
    return out

def feasible(ineq):
    # Each tuple (a,b,c) means a*x+b*y+c>=0. Eliminating a variable
    # by pos/neg pair combinations exactly preserves nonempty projection.
    e=eliminate(set(map(normalize,ineq)),0)
    e=eliminate(e,1)
    return all(v[2]>=0 for v in e)

def branch(s):
    return (s,-1,1,0)

def one_word(word):
    A=(1,0,0,1);d=(0,0);half=[]
    for s in word:
        half.append((s*A[0],s*A[1],s*d[0]))
        B=branch(s)
        d=(B[0]*d[0]+B[1]*d[1]+1,B[2]*d[0]+B[3]*d[1])
        A=mm(B,A)
    # (I-A)(x,y)=d, added as two opposite weak inequalities each.
    e1=(1-A[0],-A[1],-d[0]);e2=(-A[2],1-A[3],-d[1])
    inequalities=half+[e1,tuple(-v for v in e1),e2,tuple(-v for v in e2)]
    if not feasible(inequalities):return None
    aa,bb,cc,dd=A;det=(1-aa)*(1-dd)-bb*cc
    assert det!=0, 'feasible singular branch: investigate rather than assume isolated'
    x=Q(d[0]*(1-dd)+bb*d[1],det)
    y=Q((1-aa)*d[1]+cc*d[0],det)
    assert all(s*z>=0 for s,z in zip(word,trajectory((x,y),len(word))))
    assert iterate((x,y),len(word))==(x,y)
    return (x,y),aa+dd

def map_once(z):return (1-z[1]+abs(z[0]),z[0])
def iterate(z,n):
    for _ in range(n):z=map_once(z)
    return z

def trajectory(z,n):
    out=[]
    for _ in range(n):out.append(z[0]);z=map_once(z)
    return out

def orbit(z):
    v=[z];p=map_once(z)
    while p!=z:
        assert len(v)<=11
        v.append(p);p=map_once(p)
    return tuple(v)

def canonical(v):return min(v)

def census(n):
    points={};possible=0
    for word in product((1,-1),repeat=n):
        zt=one_word(word)
        if zt is not None:
            possible+=1
            z,tr=zt
            if z in points:assert points[z]==tr
            points[z]=tr
    classes={}
    for z,tr in points.items():
        cyc=orbit(z)
        assert len(cyc) in (1,n)
        key=canonical(cyc)
        if key not in classes:classes[key]=(cyc,tr)
    print('n=%d words=%d feasible=%d distinct_points=%d primitive_cycles=%d' %
        (n,2**n,possible,len(points),sum(len(v[0])==n and n!=1 for v in classes.values())))
    return classes,points

def main():
    allclasses={}
    for n in N_VALUES:
        classes,points=census(n)
        allclasses[n]=classes
        if n in (3,7,9):assert set(points)=={(Q(1),Q(1))}
        if n==5:assert len(points)==11 and len(classes)==3
        if n==11:assert len(points)==23 and len(classes)==3
    cycles11={k:(len(v[0]),v[1]) for k,v in allclasses[11].items() if len(v[0])==11}
    assert cycles11=={(Q(-1,3),Q(1,3)):(11,5), (Q(-3,7),Q(5,7)):(11,-5)}
    cycles5={k:(len(v[0]),v[1]) for k,v in allclasses[5].items() if len(v[0])==5}
    assert cycles5=={(Q(-1),Q(1)):(5,3), (Q(-1),Q(-1)):(5,1)}
    print('period-5:',cycles5)
    print('period-11:',cycles11)
    print('EXACT_ODD_PERIOD_CENSUS_OK')
if __name__=='__main__':main()
