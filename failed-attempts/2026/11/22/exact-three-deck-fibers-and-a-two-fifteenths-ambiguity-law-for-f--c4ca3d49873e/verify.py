#!/usr/bin/env python3
"""Finite verification of palindromic binary three-deck fibers."""
from collections import defaultdict, Counter
from itertools import combinations
from math import comb

def word(a,b,c):
    return '0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*b+'1'+'0'*a

def dynamic_deck(w):
    # Ascending-length subsequence counts. Does not use the theorem's formulas.
    c1={x:0 for x in ['0','1']}
    c2={x+y:0 for x in ['0','1'] for y in ['0','1']}
    c3={x+y+z:0 for x in ['0','1'] for y in ['0','1'] for z in ['0','1']}
    for c in w:
        for v,n in c2.items(): c3[v+c]+=n
        for v,n in c1.items(): c2[v+c]+=n
        c1[c]+=1
    return tuple(c3[k] for k in sorted(c3))

def direct_deck(w):
    d=Counter(w[i]+w[j]+w[k] for i,j,k in combinations(range(len(w)),3))
    return tuple(d[k] for k in ('000','001','010','011','100','101','110','111'))

def predicted(N,a,b,c):
    t=4*a+b
    H=N*N+2*N*a-N*t-N+10*a*a-6*a*t+t*t
    return (comb(N,3) if N>=3 else 0, H, 2*N*(N-1)-2*H, N+t,
            H, 4*N-2*t, N+t, 4)

def parameters(N):
    for a in range(N//2+1):
        for b in range((N-2*a)//2+1):
            c=N-2*a-2*b
            yield a,b,c

def partner(a,b,c):
    if (b-c)%5: return None
    return a+(b-c)//5, (b+4*c)//5, (6*b-c)//5

checked=brute=0
for N in range(0,101):
    buckets=defaultdict(list)
    for a,b,c in parameters(N):
        w=word(a,b,c)
        actual=dynamic_deck(w)
        assert actual==predicted(N,a,b,c), (N,a,b,c,actual,predicted(N,a,b,c))
        checked+=1
        if N<=18:
            assert actual==direct_deck(w)
            brute+=1
        buckets[actual].append((a,b,c))
    assert all(len(v)<=2 for v in buckets.values())
    got_pairs={frozenset(v) for v in buckets.values() if len(v)==2}
    predicted_pairs=set()
    for a,b,c in parameters(N):
        if b>c and (b-c)%5==0:
            p=partner(a,b,c)
            assert p and min(p)>=0 and p!= (a,b,c)
            assert partner(*p)==(a,b,c)
            predicted_pairs.add(frozenset({(a,b,c),p}))
    assert got_pairs==predicted_pairs, (N,len(got_pairs),len(predicted_pairs))
    coeff=sum(1 for d in range(1,N//10+1)
              for c in range((N-10*d)//3+1)
              if (N-10*d-3*c)%2==0)
    assert len(got_pairs)==coeff
    assert len(buckets)==comb(N//2+2,2)-coeff

# Pure arithmetic independent from word enumeration verifies all coefficients to 500.
for N in range(0,501):
    direct=sum(1 for d in range(1,N//10+1)
               for c in range((N-10*d)//3+1)
               if (N-10*d-3*c)%2==0)
    convolution=0
    for d in range(1,N//10+1):
        m=N-10*d
        # 2a+3c=m has solutions c congruent to m modulo 2, 0<=c<=floor(m/3)
        top=m//3; parity=m%2
        if top>=parity:
            convolution+=1+(top-parity)//2
    assert direct==convolution

print('PASS: exact 3-deck identities:',checked,'parameter triples (N=0..100)')
print('PASS: independent literal triple enumeration:',brute,'parameter triples (N=0..18)')
print('PASS: every complete 3-deck fiber and involution N=0..100')
print('PASS: generating-series coefficients N=0..500')
print('known collision N=10:',partner(0,5,0),word(0,5,0),word(1,1,6))
