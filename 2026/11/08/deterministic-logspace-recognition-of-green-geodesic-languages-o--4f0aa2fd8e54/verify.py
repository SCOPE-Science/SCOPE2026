#!/usr/bin/env python3
"""Exact finite test of Green-language shortest-representative predicates.
For symbolic proof of arbitrary length see RESULT.md; this checks finite input sets.
"""
from itertools import product
from collections import defaultdict

ALPH = 'aAbB'
INV = {'a':'A','A':'a','b':'B','B':'b'}

def reduce_word(w):
    s=[]
    for a in w:
        if s and s[-1] == INV[a]:
            s.pop()
        else:
            s.append(a)
    return ''.join(s)

def inverse(w):
    return ''.join(INV[c] for c in reversed(w))

def prefixes(w):
    s=[]; v=['']
    for a in w:
        if s and s[-1]==INV[a]: s.pop()
        else:s.append(a)
        v.append(''.join(s))
    return v

def d(x,y):
    return len(reduce_word(inverse(x)+y))

def classkey(w,kind):
    v=prefixes(w)
    V=frozenset(v)
    if kind=='H': return (V,v[-1])
    if kind=='R': return V
    if kind=='L':
        return frozenset(reduce_word(inverse(v[-1])+x) for x in V)
    if kind=='D':
        shifted=[]
        for x in V:
            shifted.append(tuple(sorted(reduce_word(inverse(x)+y) for y in V)))
        return min(shifted)
    raise ValueError(kind)

def expected_minima(w):
    v=prefixes(w); V=set(v)
    E=len(V)-1; beta=v[-1]
    delta=max(d(x,y) for x in V for y in V)
    rad0=max(d('',x) for x in V)
    radb=max(d(beta,x) for x in V)
    return {'H':2*E-d('',beta), 'R':2*E-rad0,
            'L':2*E-radb, 'D':2*E-delta}


def main():
    # Independent brute force across all 4-letter words of length at most 7;
    # D keys canonicalize the unlabeled embedded trees modulo left translation.
    max_n=7
    minima={k:{} for k in 'HRLD'}
    count=0
    for n in range(max_n+1):
        for tup in product(ALPH,repeat=n):
            w=''.join(tup); count+=1
            for kind in minima:
                key=classkey(w,kind)
                if key not in minima[kind]: minima[kind][key]=n
                elif minima[kind][key]>n:
                    raise AssertionError('bruteforce order')
    checks=0
    membership_counts={k:0 for k in 'HRLD'}
    for n in range(max_n+1):
        for tup in product(ALPH,repeat=n):
            w=''.join(tup); preds=expected_minima(w)
            for kind in minima:
                obs=minima[kind][classkey(w,kind)]
                # Every member of this class has its attainable minimum visible
                # among words up to n, because w is one representative.
                assert preds[kind]==obs,(w,kind,preds,obs)
                assert (n==preds[kind]) == (n==obs)
                membership_counts[kind]+=(n==obs)
                checks+=1
    print('VERIFY_OK alphabet=4 max_length=7 words=',count,'class_checks=',checks)
    print('MIN_CLASSES', {k:len(v) for k,v in minima.items()})
    print('GEODESIC_COUNTS', membership_counts)
    # additional fixed witnesses of nonminimal words in each class
    for w in ['aaAA','abaA','aAbB','abBA','aabbAAbb','ababABAB']:
        print('WITNESS',w,'length',len(w),'minima',expected_minima(w))

if __name__=='__main__':main()

def modular_identity(w):
    """Finite-modulus word test using Sanov's integral free matrices.
    Bound 2..32 is used only for the finite verification inputs (length<=5).
    The mathematical algorithm uses 2..c*n with c fixed from the matrix norm.
    """
    mats={
        'a':(1,2,0,1),'A':(1,-2,0,1),
        'b':(1,0,2,1),'B':(1,0,-2,1),
    }
    for mod in range(2,33):
        a,b,c,d=1,0,0,1
        for letter in w:
            e,f,g,h=mats[letter]
            a,b,c,d=((a*e+b*g)%mod,(a*f+b*h)%mod,
                     (c*e+d*g)%mod,(c*f+d*h)%mod)
        if (a,b,c,d)!=(1,0,0,1):
            return False
    return True

def mod_eq(u,v):
    return modular_identity(inverse(u)+v)

def parity_dist(v,i,j):
    edgelist=[(v[t-1],v[t]) for t in range(i+1,j+1)]
    count=0
    for ii,(x,y) in enumerate(edgelist):
        def match(edge):
            p,q=edge
            return (mod_eq(x,p) and mod_eq(y,q)) or (mod_eq(x,q) and mod_eq(y,p))
        if any(match(e) for e in edgelist[:ii]):
            continue
        occur=sum(bool(match(e)) for e in edgelist)
        count+=occur%2
    return count

def logspace_kernel_test():
    c=0; comparisons=0
    for n in range(6):
        for t in product(ALPH,repeat=n):
            w=''.join(t); v=prefixes(w); c+=1
            for i in range(n+1):
                for j in range(i,n+1):
                    assert mod_eq(v[i],v[j]) == (v[i]==v[j])
                    assert parity_dist(v,i,j) == d(v[i],v[j])
                    comparisons+=1
    print('LOGSPACE_KERNEL_OK words=',c,'vertex_and_distance_pairs=',comparisons)

if __name__=='__main__':
    logspace_kernel_test()
