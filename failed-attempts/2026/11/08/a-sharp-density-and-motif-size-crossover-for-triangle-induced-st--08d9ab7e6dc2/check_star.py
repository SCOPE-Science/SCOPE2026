"""Finite reproducibility checks for the triangle/induced-star covariance identity.

Python 3 standard library only; run: python check_star.py
"""
from fractions import Fraction
from math import comb
from itertools import combinations

def choose(n,k):
    return comb(n,k) if 0<=k<=n else 0

def formula(n,r,p):
    q=1-p
    return choose(n,3)*p**(r+2)*q**choose(r,2)*(
        3*choose(n-3,r-1)*(2-(r+1)*p)
        -(r+1)*choose(n-3,r-2)*p)

def event_templates(n,r):
    edges=list(combinations(range(n),2))
    pos={e:i for i,e in enumerate(edges)}
    triangles=[]
    for t in combinations(range(n),3):
        mask=sum(1<<pos[e] for e in combinations(t,2))
        triangles.append(mask)
    stars=[]
    for v in combinations(range(n),r+1):
        for c in v:
            present=sum(1<<pos[tuple(sorted((c,x)))] for x in v if x!=c)
            absent=sum(1<<pos[e] for e in combinations(v,2) if c not in e)
            stars.append((present,absent))
    return triangles, stars, len(edges)

def pair_cov(n,r,p):
    triangles, stars, _=event_templates(n,r)
    q=1-p
    m=choose(r,2)
    marginal=p**3*p**r*q**m
    out=Fraction(0)
    for t in triangles:
        for s,a in stars:
            if t & a:
                joint=Fraction(0)
            else:
                joint=p**((t|s).bit_count())*q**(a.bit_count())
            out+=joint-marginal
    return out

def exhaustive_cov(n,r,p):
    triangles,stars,edge_count=event_templates(n,r)
    num_tri=Fraction(0);num_star=Fraction(0);num_both=Fraction(0)
    for g in range(1<<edge_count):
        w=p**g.bit_count()*(1-p)**(edge_count-g.bit_count())
        t=sum((g&x)==x for x in triangles)
        s=sum((g&x)==x and (g&a)==0 for x,a in stars)
        num_tri+=w*t; num_star+=w*s; num_both+=w*t*s
    return num_both-num_tri*num_star

def main():
    checked=0
    for n in range(3,11):
        for r in range(2,n):
            for p in (Fraction(1,7), Fraction(1,3), Fraction(1,2), Fraction(2,3), Fraction(6,7)):
                f=formula(n,r,p)
                a=pair_cov(n,r,p)
                assert a==f,(n,r,p,a,f)
                checked+=1
    for n in range(3,7):
        for r in range(2,n):
            for p in (Fraction(1,3), Fraction(1,2), Fraction(3,4)):
                assert exhaustive_cov(n,r,p)==formula(n,r,p),(n,r,p)
                checked+=1
    for n in range(3,80):
        for r in range(2,n):
            if n==r+1:
                assert formula(n,r,Fraction(1,2))<0
            else:
                pc=Fraction(6*(n-r-1),(r+1)*(3*n-2*r-4))
                assert 0<pc<Fraction(2,r+1)<1
                assert formula(n,r,pc)==0
                assert formula(n,r,pc/2)>0
                assert formula(n,r,(1+pc)/2)<0
            checked+=1
    print('PASS',checked,'exact assertions')
if __name__=='__main__': main()
