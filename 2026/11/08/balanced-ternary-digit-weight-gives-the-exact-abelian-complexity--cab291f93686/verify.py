#!/usr/bin/env python3
"""Independent finite checks of the balanced-ternary abelian-complexity formula.

The mathematical proof is supplied separately; this program only tests finite
instances and finite digit/phase identities.
"""
from itertools import product
import random
import numpy as np

PATTERNS={'a':'01?', 'b':'10?', 'c':'0?1', 'd':'1?0', 'e':'?01', 'f':'?10'}

def balanced_weight(n):
    assert n>=0
    w=0
    while n:
        q,r=divmod(n,3)
        if r==2: n=q+1;w+=1
        else: n=q;w+=(r!=0)
    return w

def generate(directive, level=9, fill=0):
    n=3**level
    out=np.empty(n,dtype=np.int8)
    for j in range(n):
        x=j
        for d in range(level):
            v=PATTERNS[directive[d%len(directive)]][x%3]
            if v!='?':
                out[j]=int(v)
                break
            x//=3
        else:out[j]=fill
    return out

def phase_pairs(p,n):
    pat=PATTERNS[p]
    out=[]
    for a in range(3):
        v=[pat[(a+j)%3] for j in range(n)]
        out.append((v.count('?'),v.count('1')-v.count('0')))
    return sorted(out)

# Critical exact finite phase algebra: covers every residue and all six patterns.
phase_cases=0
for n in range(1,300):
    m,r=divmod(n,3)
    expected={0:[(m,0)]*3,1:[(m,-1),(m,1),(m+1,0)],
              2:[(m,0),(m+1,-1),(m+1,1)]}[r]
    for p in PATTERNS:
        assert phase_pairs(p,n)==sorted(expected),(p,n)
        phase_cases+=1

# Balanced ternary recurrences and the Lipschitz step used in the proof.
digit_cases=0
for n in range(1,100001):
    m,r=divmod(n,3)
    desired={0:balanced_weight(m),1:balanced_weight(m)+1,
             2:balanced_weight(m+1)+1}[r]
    assert balanced_weight(n)==desired
    assert abs(balanced_weight(n+1)-balanced_weight(n))<=1
    assert (n-balanced_weight(n))%2==0
    digit_cases+=1

# Finite prefix windows: diverse arbitrary directive samples, not just periodic fixed points.
random.seed(40431)
directives=['a'*9,'b'*9,'c'*9,'d'*9,'e'*9,'f'*9,
            'abcdefabc','ab'*5,'ce'*5,'fedcbaabc']
directives += [''.join(random.choices(tuple(PATTERNS),k=9)) for _ in range(24)]
window_cases=0
for word in directives:
    z=generate(word,level=9,fill=0)
    pref=np.empty(len(z)+1,dtype=np.int64)
    pref[0]=0
    np.cumsum(z,out=pref[1:])
    for n in range(1,257):
        values=pref[n:]-pref[:-n]
        h=balanced_weight(n)
        assert int(values.min())==(n-h)//2,(word,n,'min',int(values.min()),h)
        assert int(values.max())==(n+h)//2,(word,n,'max',int(values.max()),h)
        window_cases+=1
    # Entire infinite-word exception at all-hole residue: changing fill has no effect.
    if word in ('e'*9,'f'*9):
        z2=generate(word,level=9,fill=1)
        pref2=np.concatenate(([0],np.cumsum(z2,dtype=np.int64)))
        for n in range(1,129):
            v=pref2[n:]-pref2[:-n]
            h=balanced_weight(n)
            assert int(v.min())==(n-h)//2
            assert int(v.max())==(n+h)//2
            window_cases+=1
for k in range(1,12):
    n=(3**k+1)//2
    assert balanced_weight(n)==k+1
    assert balanced_weight(3**k)==1
print(f'VERIFY_OK directives={len(directives)} phase_cases={phase_cases} digit_cases={digit_cases} window_cases={window_cases} peaks=11')
