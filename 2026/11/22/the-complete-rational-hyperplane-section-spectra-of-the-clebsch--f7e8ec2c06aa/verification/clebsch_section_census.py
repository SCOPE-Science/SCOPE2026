#!/usr/bin/env python3
"""Exact independent enumerations of Clebsch hyperplane-section counts at 7 and 11.

Run: python3 verify_clebsch_sections.py
Uses only the standard Python library. Every asserted result is reproducible.
"""
from itertools import combinations, product, permutations
from collections import Counter, defaultdict
from math import comb

EXPECTED={
 7: {6:10,9:40,10:60,11:60,12:120,13:20,14:30,16:45,21:5,22:10},
11: {12:30,14:60,15:100,16:300,17:300,18:440,22:30,23:24,24:135,33:35,34:10},
}

def normalize(v,p):
    for x in v:
        if x%p:
            inv=pow(x%p,-1,p)
            return tuple((y*inv)%p for y in v)
    raise ValueError('zero vector')

def projective(n,p):
    # uniquely normalized, disjoint affine charts
    for i in range(n):
        for tail in product(range(p),repeat=n-i-1):
            yield (0,)*i+(1,)+tail

def f(v,p):
    return (sum(x**3 for x in v)-sum(v)**3)%p

def point_set_first(p):
    return set(t for t in projective(4,p) if f(t,p)==0)

def point_set_second(p):
    # Solve for the fourth coordinate via a quadratic in that coordinate.
    pts={(0,0,0,1)}
    for a,b,c in projective(3,p):
        s=(a+b+c)%p
        t=(a**3+b**3+c**3)%p
        for d in range(p):
            if (t-s**3-3*s*s*d-3*s*d*d)%p==0:
                pts.add((a,b,c,d))
    return pts

def section_counts(p,pts):
    by_h={}
    for h in projective(4,p):
        by_h[h]=sum(sum(a*b for a,b in zip(h,v))%p==0 for v in pts)
    return by_h

def line_points(a,b,p):
    # distinct normalized rational points on span of a,b
    return frozenset(normalize(tuple((a[i]+t*b[i])%p for i in range(4)),p) for t in range(p))|{b}

def rational_lines(pts,p):
    arr=list(pts); found=set()
    for i,a in enumerate(arr):
        for b in arr[i+1:]:
            L=line_points(a,b,p)
            if L.issubset(pts):found.add(L)
    return found

def expected_eckardt_h(p):
    # H_ij: x_i+x_j=0, with x_4= -(x0+x1+x2+x3)
    hs=set()
    for i,j in combinations(range(5),2):
        a=[0]*5
        a[i]=a[j]=1
        hs.add(normalize(tuple((a[k]-a[4])%p for k in range(4)),p))
    return hs

def main():
    for p in (7,11):
        A=point_set_first(p)
        B=point_set_second(p)
        assert A==B,(p,len(A),len(B),len(A^B))
        n=len(A)
        assert n==({7:85,11:199}[p])
        h=section_counts(p,A)
        hist=dict(sorted(Counter(h.values()).items()))
        assert hist==EXPECTED[p],(p,hist)
        assert len(h)==(p**4-1)//(p-1)
        # Independent first- and second-factorial incidence moment identities.
        assert sum(z*c for z,c in hist.items())==n*(p*p+p+1)
        assert sum(comb(z,2)*c for z,c in hist.items())==comb(n,2)*(p+1)
        mx=max(hist)
        assert mx==3*p+1
        winners={v for v,z in h.items() if z==mx}
        assert winners==expected_eckardt_h(p) and len(winners)==10
        # Exhaustively enumerate every rational contained line and each section's line count.
        lines=rational_lines(A,p)
        assert len(lines)==({7:15,11:27}[p])
        line_count=Counter()
        categories=defaultdict(Counter)
        for coeff,z in h.items():
            k=sum(all(sum(x*y for x,y in zip(coeff,v))%p==0 for v in L) for L in lines)
            categories[z][k]+=1
            line_count[k]+=1
        assert all(categories[mx][k]==(10 if k==3 else 0) for k in range(4))
        # Classify the entire hyperplane system by the coordinate-permutation S5 action.
        orbit_by_rep=defaultdict(list)
        perms=list(permutations(range(5)))
        for coeff,z in h.items():
            a=coeff+(0,)
            rep=min(normalize(tuple((a[perm[i]]-a[perm[4]])%p for i in range(4)),p)
                    for perm in perms)
            orbit_by_rep[rep].append(z)
        assert len(orbit_by_rep)==({7:13,11:30}[p])
        assert all(len(set(values))==1 for values in orbit_by_rep.values())
        assert sorted(sum((len(vals) for vals in orbit_by_rep.values()),0) for _ in [0])==[len(h)]
        weights={n-z:(p-1)*cnt for z,cnt in hist.items()}
        assert sum(weights.values())==p**4-1
        assert min(weights)==n-(3*p+1)
        print('FIELD',p,'POINTS',n,'HYPERPLANES',len(h),'RATIONAL_LINES',len(lines),
              'MAX_ECKARDT',len(winners),'CODE',f'[{n},4,{n-(3*p+1)}]')
        print('SECTION_HIST',hist)
        print('LINE_CONTAINED_BY_SECTION', {z:dict(sorted(v.items())) for z,v in sorted(categories.items())})
        print('WEIGHTS', dict(sorted(weights.items())))
        print('S5_ORBITS',len(orbit_by_rep),'S5_ORBIT_ROWS',sorted((rep,len(values),values[0]) for rep,values in orbit_by_rep.items()))
    print('CLEBSCH_SECTION_CENSUS_OK')

if __name__=='__main__':main()
