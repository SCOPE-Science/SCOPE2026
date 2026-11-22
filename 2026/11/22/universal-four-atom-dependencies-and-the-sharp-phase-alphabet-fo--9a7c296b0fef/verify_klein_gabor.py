#!/usr/bin/env python3
"""Exact four-vector Gabor-circuit and phase-alphabet verification.
Only the Python standard library is required.
"""
from itertools import combinations, permutations, product
from collections import Counter
from math import comb

G = range(4)
LABELS = tuple((t,m) for t in G for m in G)
SETS4 = tuple(combinations(range(16),4))
P4 = tuple((p,(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))) for p in permutations(range(4)))
POLYS={1:(-1,1),2:(1,1),3:(1,1,1),4:(1,0,1),5:(1,1,1,1,1),6:(1,-1,1),7:(1,1,1,1,1,1,1)}

def dot(x,y):
    return ((x&y).bit_count()&1)

def omega(a,b):
    t,m=LABELS[a];u,n=LABELS[b]
    return dot(t,n)^dot(u,m)

def is_circuit(ids):
    a,b,c=(x^ids[0] for x in ids[1:])
    return a^b^c != 0 and omega(a,b)==omega(a,c)==omega(b,c)==1

def entry(r,j):
    t,m=LABELS[j]
    return r^t, (-1 if dot(m,r) else 1)

def symbolic_det(ids):
    terms={}
    for p,sgn in P4:
        exp=[0]*4;v=sgn
        for r in range(4):
            k,sign=entry(r,ids[p[r]])
            exp[k]+=1;v*=sign
        key=tuple(exp)
        terms[key]=terms.get(key,0)+v
    return {k:v for k,v in terms.items() if v}

def bareiss(matrix):
    a=[list(row) for row in matrix]
    n=len(a);sign=1;den=1
    for k in range(n-1):
        if a[k][k]==0:
            s=next((s for s in range(k+1,n) if a[s][k]!=0),None)
            if s is None:return 0
            a[k],a[s]=a[s],a[k];sign=-sign
        v=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a[i][j]=(v*a[i][j]-a[i][k]*a[k][j])//den
            a[i][k]=0
        den=v
    return sign*a[-1][-1]

def integer_det(ids,window=(1,2,3,5)):
    return bareiss([[entry(r,j)[1]*window[entry(r,j)[0]] for j in ids] for r in range(4)])

def root_det(ids,exps,q):
    # 4-by-4 determinant in Z[z]/(Phi_q), expressed with integer coefficients
    coeff=[0]*q
    for p,sgn in P4:
        e=0;v=sgn
        for r in range(4):
            k,sign=entry(r,ids[p[r]])
            v*=sign;e+=exps[k]
        coeff[e%q]+=v
    phi=POLYS[q];d=len(phi)-1
    for i in range(q-1,d-1,-1):
        t=coeff[i]
        if t:
            for j in range(d+1):coeff[i-d+j]-=t*phi[j]
    return tuple(coeff[:d])

def main():
    universal=set()
    matched=0
    for ids in SETS4:
        z=(not symbolic_det(ids));g=is_circuit(ids)
        assert z==g,(ids,z,g)
        if z:universal.add(ids)
        assert (integer_det(ids)==0)==g,('integer witness',ids)
        matched+=1
    assert matched==comb(16,4)==1820
    assert len(universal)==240
    # Direct count of ordered differences in the symplectic four-space:
    # 15 nonzero a, 8 possibilities for b with omega(a,b)=1,
    # then 4 solutions to omega(a,c)=omega(b,c)=1,
    # of which c=a+b is the only dependent choice.
    assert len(universal)==16*15*8*3//24
    assert all(not is_circuit(ids) for ids in SETS4 if ids not in universal)
    best={}
    for q in range(1,7):
        m=100000
        sample=None
        for tail in product(range(q),repeat=3):
            phase=(0,)+tail
            extra=sum(root_det(ids,phase,q)==(0,)*(len(POLYS[q])-1) for ids in SETS4 if ids not in universal)
            if extra<m:m=extra;sample=phase
        best[q]=m
        assert m>0
    assert best=={1:1324,2:1324,3:12,4:24,5:4,6:12},best
    hepta=(0,1,2,4)
    assert all((root_det(ids,hepta,7)==(0,)*6)==(ids in universal) for ids in SETS4)
    # Check all 560 triples are independent for this explicit flat window,
    # using 3x3 direct determinants in Z[zeta_7].
    p3=tuple((p,(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))) for p in permutations(range(3)))
    for ids in combinations(range(16),3):
        some=False
        for rows in combinations(range(4),3):
            a=[0]*7
            for perm,sgn in p3:
                val=sgn;e=0
                for i in range(3):
                    k,sg=entry(rows[i],ids[perm[i]]);val*=sg;e+=hepta[k]
                a[e%7]+=val
            if len(set(a))>1:
                some=True;break
        assert some,('3 dependence',ids)
    print('SYMBOLIC_CIRCUITS=240; FOUR_NONCIRCUITS=1580; GEOMETRY=EXACT')
    print('INTEGER_WITNESS=(1,2,3,5); FOUR_RANKS_MATCH=1820')
    print('MIN_EXTRA_ZEROS_BY_PHASE_ORDER=',','.join(f'{q}:{best[q]}' for q in best))
    print('HEPTAPHASE_WITNESS=(1,zeta_7,zeta_7^2,zeta_7^4); FOUR_EXTRA_ZEROS=0')
    print('HEPTAPHASE_ALL_560_THREE_SETS_INDEPENDENT=TRUE')
    print('OK')

if __name__=='__main__':main()
