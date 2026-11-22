#!/usr/bin/env python3
"""Finite exact corroboration for parity-conditioned random circle matchings.

Run: python verify.py. Uses only the Python standard library. Exhaustive
checks corroborate a separate all-size proof; finite checks do not prove limits.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, factorial

CHECKS=0

def check(condition, context):
    global CHECKS
    CHECKS+=1
    if not condition:
        raise AssertionError(context)

def all_matchings(items):
    if not items:
        yield ()
        return
    first=items[0]
    for j in range(1,len(items)):
        other=items[j]
        for rest in all_matchings(items[1:j]+items[j+1:]):
            yield ((first,other),)+rest

def crossing(p,q):
    a,b=sorted(p); c,d=sorted(q)
    return (a<c<b<d) or (c<a<d<b)

def graph_data(pairs,n):
    neighbors=[set() for _ in pairs]
    for i,p in enumerate(pairs):
        for j in range(i):
            if crossing(p,pairs[j]):
                neighbors[i].add(j);neighbors[j].add(i)
    degrees=[len(a) for a in neighbors]
    visited=set(); sizes=[]
    for i in range(n):
        if i in visited: continue
        stack=[i];visited.add(i);size=0
        while stack:
            x=stack.pop();size+=1
            for y in neighbors[x]:
                if y not in visited:visited.add(y);stack.append(y)
        sizes.append(size)
    simple=sum(((b-a)% (2*n) in (1,2*n-1)) for a,b in (tuple(sorted(p)) for p in pairs))
    return tuple(degrees),tuple(sorted(sizes)),simple

def closed_block(pairs,n):
    for k in range(2,n//2+1):
        for i in range(2*n):
            arc={(i+j)%(2*n) for j in range(2*k)}
            if all((a in arc)==(b in arc) for a,b in pairs):
                return True
    return False

def cycle_matchings(n,r):
    if r==0:return 1
    return 2*n*comb(2*n-r,r)//(2*n-r)

def gaussian_coeff(n,r):
    return Fraction(cycle_matchings(n,r),factorial(n)//factorial(n-r))

# Independent enumeration of arbitrary matchings and the Gauss even-degree
# endpoint-parity condition, including the exactly n! favorable matchings.
for n in range(1,7):
    even_count=0; total=0
    for pairs in all_matchings(tuple(range(2*n))):
        total+=1
        deg,_,_=graph_data(pairs,n)
        even_by_crossing=all(d%2==0 for d in deg)
        even_by_endpoint=all((a-b)%2==1 for a,b in pairs)
        check(even_by_crossing==even_by_endpoint,("parity",n,pairs))
        even_count+=even_by_crossing
    check(even_count==factorial(n),("even_count",n,even_count))
    check(total==factorial(2*n)//(2**n*factorial(n)),("total",n,total))

# Independently enumerate odd-even bijections. Verify finite joint counts,
# factorial moments, and the closed-interval obstruction principle.
for n in range(2,9):
    bins=Counter()
    for pi in permutations(range(n)):
        pairs=tuple((2*i,2*pi[i]+1) for i in range(n))
        degrees,component_sizes,s=graph_data(pairs,n)
        check(all(d%2==0 for d in degrees),("even",n,pi))
        bins[(s,len(component_sizes))]+=1
        if s<n and len(component_sizes)!=1+s:
            check(closed_block(pairs,n),("missing block",n,pi))
        if s==0 and len(component_sizes)>1:
            check(closed_block(pairs,n),("zero-simple disconnect",n,pi))
    check(sum(bins.values())==factorial(n),("total permutations",n))
    check(sum(s*v for (s,c),v in bins.items())==2*factorial(n),("mean",n))
    for r in range(n+1):
        numerator=sum(comb(s,r)*v for (s,c),v in bins.items())
        denominator=factorial(n)
        check(Fraction(numerator,denominator)==gaussian_coeff(n,r),("factorial moments",n,r))
    # Binomial inclusion-exclusion exactly reconstructs every finite mass.
    for j in range(n+1):
        mass=sum(Fraction((-1)**(r-j)*comb(r,j))*gaussian_coeff(n,r)
                 for r in range(j,n+1))
        count=sum(v for (s,c),v in bins.items() if s==j)
        check(mass==Fraction(count,factorial(n)),("mass",n,j))
    # Unmatched nontrivial components are within the interval-witness bound.
    failures=sum(v for (s,c),v in bins.items() if c!=s+1)
    bound=Fraction(2,factorial(n)) + sum(Fraction(2*n,comb(n,k))
                                        for k in range(2,n//2+1))
    check(Fraction(failures,factorial(n))<=bound,("component witness bound",n))

# Exact rational verification of the uniform moment bound used in the
# analytic total-variation proof; this is not a substitute for induction.
for n in range(4,66):
    for r in range(1,n+1):
        target=Fraction(2**r,factorial(r))
        coeff=gaussian_coeff(n,r)
        check(abs(coeff-target)<=Fraction(3*r*r,n)*target,
              ("uniform bound",n,r))

print("VERIFY_OK",CHECKS,"finite exact assertions")
