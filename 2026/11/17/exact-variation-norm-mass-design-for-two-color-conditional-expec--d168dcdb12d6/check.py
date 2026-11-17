"""Exact-rational diagnostic for the weighted-path binary conditional-expectation theorem.
Uses only Python's standard library. Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random

def blocks_of(c):
    blocks=[[0]]
    for i in range(1,len(c)):
        if c[i]!=c[i-1]: blocks.append([i])
        else: blocks[-1].append(i)
    return blocks

def norm_formula(c,m,w):
    n=len(c)
    totals=[sum((m[i] for i in range(n) if c[i]==t),Q()) for t in (0,1)]
    b=sum((w[k] for k in range(n-1) if c[k]!=c[k+1]),Q())
    s=Q(); top=Q()
    for k in range(n-1):
        s+=m[k]*(1 if c[k]==0 else -1)/totals[c[k]]
        top=max(top,abs(s)/w[k])
    return b*top

def direct_norm(c,m,w):
    n=len(c)
    totals=[sum((m[i] for i in range(n) if c[i]==t),Q()) for t in (0,1)]
    best=Q()
    for k in range(n-1):
        means=[sum((m[i] for i in range(k+1,n) if c[i]==t),Q())/totals[t] for t in (0,1)]
        yy=[means[t] for t in c]
        variation=sum((w[i]*abs(yy[i+1]-yy[i]) for i in range(n-1)),Q())
        best=max(best,variation/w[k])
    return best

def optimal_masses(c,w):
    n=len(c); blocks=blocks_of(c); r=len(blocks)-1
    t=[blocks[i][-1] for i in range(r)]
    W=sum((w[k] for k in t),Q())
    e=min(w)/(10*n*W)
    masses=[Q()]*n
    for j,bb in enumerate(blocks):
        L=len(bb)
        if j==0:
            for i in bb[:-1]: masses[i]=e
            masses[bb[-1]]=w[t[0]]/W - (L-1)*e
        elif j==r:
            masses[bb[0]]=w[t[-1]]/W - (L-1)*e
            for i in bb[1:]: masses[i]=e
        elif L==1:
            masses[bb[0]]=(w[t[j-1]]+w[t[j]])/W
        else:
            masses[bb[0]]=w[t[j-1]]/W
            for i in bb[1:-1]: masses[i]=e
            masses[bb[-1]]=w[t[j]]/W-(L-2)*e
    return masses

rng=Random(20261114)
count=0; designed=0; strict=0
for n in range(2,11):
    for tail in product((0,1),repeat=n-1):
        c=(0,)+tail
        if len(set(c))<2: continue
        for k in range(2):
            w=[Q(rng.randint(1,9),rng.randint(1,8)) for _ in range(n-1)] if k else [Q(1)]*(n-1)
            m=[Q(rng.randint(1,9),rng.randint(1,6)) for _ in range(n)]
            a=norm_formula(c,m,w)
            assert a==direct_norm(c,m,w)
            W=sum((w[j] for j in range(n-1) if c[j]!=c[j+1]),Q())
            R=W/min(w)
            assert 1<=a<=R
            if R>1: assert a<R
            if R==1: assert a==1
            count+=1
            mstar=optimal_masses(c,w)
            assert all(x>0 for x in mstar)
            assert norm_formula(c,mstar,w)==1
            assert direct_norm(c,mstar,w)==1
            designed+=1
            # Concentrate opposite-colour masses across a minimum-weight edge
            imin=w.index(min(w)); left=next(i for i in range(imin+1) if c[i]!=c[-1]) if any(c[i]!=c[-1] for i in range(imin+1)) else None
            crossing=next((i,j) for i in range(imin+1) for j in range(imin+1,n) if c[i]!=c[j])
            p,q=crossing
            mm=[Q(1)]*n;mm[p]=mm[q]=Q(1000000)
            assert norm_formula(c,mm,w)>R*Q(99,100)
            strict+=1
print('EXACT_WEIGHTED_STEP_DUAL_TESTS_PASS',count)
print('EVERY_WORD_POSITIVE_MASS_ONE_NORM_DESIGN_PASS',designed)
print('SHARP_WEIGHTED_SUPREMUM_APPROACH_PASS',strict)
print('ALL_WEIGHTED_PATH_TWO_COLOR_CHECKS_PASS')
