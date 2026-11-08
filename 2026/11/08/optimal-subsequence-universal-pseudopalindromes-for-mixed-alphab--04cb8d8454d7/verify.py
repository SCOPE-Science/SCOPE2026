#!/usr/bin/env python3
"""Independent finite checks for involutive-palindrome universality formulae.

The theorem is infinite; enumerations below are bounded consistency tests only.
"""
from itertools import product, permutations
from math import factorial
from collections import Counter

def involution(q,p):
    assert 0<=2*p<=q
    t=list(range(q))
    for j in range(p):
        t[2*j]=2*j+1; t[2*j+1]=2*j
    return tuple(t)

def min_length(q,k,p):
    f=q-2*p
    return q*k+(f-1 if k%2 and f>0 else 0)

def predicted_number(q,k,p):
    f=q-2*p; r=k//2
    if k%2==0: return factorial(q)**r
    if f==0: return factorial(q)**r*2**p*factorial(p)
    return factorial(q)**r*f*2**p*factorial(p+f-1)

def canonical(q,k,p,u,center):
    t=involution(q,p); f=q-2*p; r=k//2
    if any(len(set(u[j*q:(j+1)*q]))!=q for j in range(r)):
        return False
    rem=u[r*q:]
    if k%2==0: return len(rem)==0 and center is None
    fixed={j for j in range(q) if t[j]==j}
    reps=(set(rem))
    if len(reps)!=len(rem): return False
    if any((a in reps)==(t[a] in reps) for a in range(q) if a<t[a]):return False
    if f==0: return center is None and len(rem)==p
    return center in fixed and reps.intersection(fixed)==fixed-{center} and len(rem)==p+f-1

def arches(w,q):
    seen=set();v=0
    for c in w:
        seen.add(c)
        if len(seen)==q:
            v+=1;seen.clear()
    return v

def pattern_universal(w,q,k):
    for pat in product(range(q),repeat=k):
        j=0
        for x in w:
            if x==pat[j]:
                j+=1
                if j==k:break
        if j<k:return False
    return True

def exhaustive(q,p,k,do_direct=False):
    t=involution(q,p); n=min_length(q,k,p); f=q-2*p
    if n%2: centers=[i for i in range(q) if t[i]==i]
    else: centers=[None]
    h=n//2
    success=0; classified=0;checked=0;dircnt=0
    for u in product(range(q),repeat=h):
        for c in centers:
            w=u+((c,) if c is not None else tuple())+tuple(t[x] for x in u[::-1])
            yes=arches(w,q)>=k
            exp=canonical(q,k,p,u,c)
            if yes!=exp:
                raise AssertionError(('classification',q,p,k,u,c,yes,exp))
            if do_direct:
                direct=pattern_universal(w,q,k)
                if yes!=direct:raise AssertionError(('oracle',q,p,k,u,c,yes,direct))
                dircnt+=1
            success+=int(yes);classified+=int(exp);checked+=1
    if success!=predicted_number(q,k,p):
        raise AssertionError(('count',q,p,k,success,predicted_number(q,k,p)))
    return checked,success,dircnt

def run():
    cases=[(2,1,1),(2,1,2),(2,1,3),(2,1,4),(2,1,5),
           (2,0,1),(2,0,2),(2,0,3),(2,0,4),(2,0,5),
           (3,0,1),(3,0,2),(3,0,3),(3,1,1),(3,1,2),(3,1,3),
           (4,0,1),(4,0,2),(4,0,3),(4,1,1),(4,1,2),(4,1,3),
           (4,2,1),(4,2,2),(4,2,3),
           (5,0,1),(5,1,1),(5,1,3),(5,2,1),(5,2,3),
           (6,0,1),(6,1,1),(6,2,1),(6,3,1)]
    total=valid=direct=0
    for q,p,k in cases:
        n=min_length(q,k,p); m=n//2
        if q**m*(q-2*p if n%2 else 1)>1_500_000:
            continue
        checked,passed,d=exhaustive(q,p,k,do_direct=(q<=4 and k<=3))
        print(f'q={q}, p={p}, f={q-2*p}, k={k}: examined={checked}, valid={passed}, direct={d}')
        total+=checked;valid+=passed;direct+=d
    print(f'OK cases={len(cases)}, enumerated_palindromes={total}, extremizers={valid}, direct_full_pattern_checks={direct}')

if __name__=='__main__':run()
