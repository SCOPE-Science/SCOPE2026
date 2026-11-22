#!/usr/bin/env python3
"""Exact rational regression checks for facet-active simplices.

Python standard library only. No sampled assertion is used to prove the theorem.
"""
from fractions import Fraction as Q
from random import Random
from itertools import product


def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def lincomb(v, a): return tuple(sum(w*point[k] for w,point in zip(a,v)) for k in range(len(v[0])))
def determinant(a):
    a=[list(row) for row in a]; n=len(a); z=Q(1)
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None: return Q(0)
        if j!=k: a[j],a[k]=a[k],a[j];z=-z
        p=a[j][j];z*=p
        for i in range(j+1,n):
            r=a[i][j]/p
            for h in range(j,n): a[i][h]-=r*a[j][h]
    return z

def solve(mat, rhs):
    a=[list(x)+[y] for x,y in zip(mat,rhs)]; n=len(a)
    for j in range(n):
        k=next(i for i in range(j,n) if a[i][j])
        a[j],a[k]=a[k],a[j]; p=a[j][j]
        a[j]=[v/p for v in a[j]]
        for i in range(n):
            if i!=j:
                r=a[i][j]
                a[i]=[x-r*y for x,y in zip(a[i],a[j])]
    return [row[-1] for row in a]

def foot_coords(verts,i):
    ids=[j for j in range(len(verts)) if j!=i]
    base=[verts[j] for j in ids]
    U=[sub(b,base[0]) for b in base[1:]]
    A=[[dot(u,v) for v in U] for u in U]
    rhs=[dot(u,sub(verts[i],base[0])) for u in U]
    coeff=solve(A,rhs)
    return ids, [Q(1)-sum(coeff)]+coeff

def vol_det(verts):
    return abs(determinant([sub(v,verts[0]) for v in verts[1:]]))

def result(verts,i):
    ids,q=foot_coords(verts,i)
    cs=[max(Q(0),-x) for x in q]
    t=Q(1)+sum(cs)
    w=lincomb([verts[i]]+[verts[j] for j in ids],[Q(1)/t]+[c/t for c in cs])
    P=[verts[j] for j in ids]+[w]
    p=vol_det(P)/vol_det(verts)
    assert p==1/t, ('bad volume',p,t)
    return ids,q,cs,t,p,w

def main():
    rng=Random(4240023); tests=0
    # All enumerated integral shears/height combinations, and independent
    # determinant calculations in dimensions 2--6.
    for d in range(2,7):
        for s in range(-4,5):
            for h in (1,2,3):
                verts=[tuple(Q(0) for _ in range(d))]
                verts += [tuple(Q(int(j==k)) for k in range(d)) for j in range(d-1)]
                verts += [tuple(Q(s) if k==0 else (Q(h) if k==d-1 else Q(0)) for k in range(d))]
                assert vol_det(verts)>0
                for i in range(d+1):
                    ids,q,cs,t,p,w=result(verts,i);tests+=3
                    assert sum(q)==1
                    for mask in range(13):
                        b=[Q(rng.randrange(1,100)) for _ in range(d+1)]
                        b=[x/sum(b) for x in b]
                        proj=[b[j]+b[i]*qq for j,qq in zip(ids,q)]
                        condition=all(z>=0 for z in proj)
                        inequalities=all(b[j]>=c*b[i] for j,c in zip(ids,cs))
                        assert condition==inequalities
                        tests+=1
    # Published monostability-example tetrahedron: probabilities exactly known.
    raw=[(-20,0,0),(-1,-1,10),(1,1,10),(20,0,0)]
    verts=[tuple(map(Q,r)) for r in raw]
    target=[Q(1,4),Q(101,105),Q(101,105),Q(1,4)]
    for i,p0 in enumerate(target):
        ids,q,cs,t,p,w=result(verts,i)
        assert p==p0,(i,p,p0)
        tests+=1
    assert sum(target)==Q(509,210)
    tests+=1
    # Sharp-angle example, d=2,3,..6 with symmetrical two outer apices;
    # verify only one positive outward-normal pair by means of gradients.
    for d in range(2,7):
        for a,b in ((Q(2),Q(1)),(Q(3),Q(1)),(Q(5),Q(2))):
            # choose (d-1) equatorial vertices as a small simplex in d-2 coords,
            # e.g. e1,...,e_{d-2},0, centered not required.
            w=[]
            if d==2: w=[()]
            else:
                w=[tuple(Q(int(j==k),10) for k in range(d-2)) for j in range(d-2)]
                w += [tuple(Q(0) for _ in range(d-2))]
            verts=[(a,b,*tuple(Q(0) for _ in range(d-2))),(-a,b,*tuple(Q(0) for _ in range(d-2)))]
            verts += [(Q(0),Q(0),*u) for u in w]
            assert vol_det(verts)>0
            probs=[result(verts,i)[4] for i in range(d+1)]
            g=(a*a-b*b)/(a*a+b*b)
            assert probs[0]==probs[1]==1/(1+g),probs
            assert probs[2:]==[Q(1)]*(d-1),probs
            assert (d+1)-sum(probs)==2*g/(1+g)
            tests+=5
    print('PASS exact rational regression tests, dimensions 2..6')

if __name__=='__main__': main()
