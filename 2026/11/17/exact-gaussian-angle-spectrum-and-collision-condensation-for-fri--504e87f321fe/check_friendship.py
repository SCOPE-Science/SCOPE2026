#!/usr/bin/env python3
"""Independent finite enumeration for friendship-graph angular probabilities.
Scientific algorithm: assign all total orders of hub plus 2m leaves;
classify each induced acyclic triangle orientation; check beta-integral formula.
Only integer and rational operations are used.
"""
from itertools import permutations
from collections import Counter
from math import factorial
from fractions import Fraction


def all_cone_counts(m):
    n=2*m+1
    counts=Counter()
    for perm in permutations(range(n)):
        pos=[0]*n
        for i,x in enumerate(perm):
            pos[x]=i
        hub=pos[0]
        key=[]
        for j in range(m):
            a,b=pos[2*j+1],pos[2*j+2]
            # full three-vertex ordering, encoded by order of hub and two named leaves
            triple=tuple(sorted((0,2*j+1,2*j+2),key=lambda v:pos[v]))
            key.append(triple)
        counts[tuple(key)]+=1
    return counts


def prediction(key,m):
    a=b=c=0
    for triple in key:
        if triple[2]==0: a+=1
        elif triple[0]==0: b+=1
        else: c+=1
    return factorial(2*a+c)*factorial(2*b+c)//(2**(a+b)) if (factorial(2*a+c)*factorial(2*b+c))%(2**(a+b))==0 else Fraction(factorial(2*a+c)*factorial(2*b+c),2**(a+b))


def collision_formula(m):
    total=Fraction(0)
    for a in range(m+1):
        for b in range(m-a+1):
            c=m-a-b
            multiplicity=2**m*factorial(m)//(factorial(a)*factorial(b)*factorial(c))
            prob=Fraction(factorial(2*a+c)*factorial(2*b+c), 2**(a+b)*factorial(2*m+1))
            total+=multiplicity*prob**2
    return total


def main():
    for m in range(1,5):
        counts=all_cone_counts(m)
        assert len(counts)==6**m,(m,len(counts))
        total=factorial(2*m+1)
        assert sum(counts.values())==total
        for key,number in counts.items():
            predicted=prediction(key,m)
            assert number==predicted,(m,key,number,predicted)
        exact=sum((Fraction(k,total)**2 for k in counts.values()),Fraction(0))
        assert exact==collision_formula(m),(m,exact,collision_formula(m))
        print(f'm={m}: permutations={total} cones={len(counts)} collision={exact} PASS')
    for m in range(1,11):
        c=collision_formula(m)
        assert 0<c<=1
    print('FRIENDSHIP_ANGULAR_SPECTRUM_PASS')
if __name__=='__main__': main()
