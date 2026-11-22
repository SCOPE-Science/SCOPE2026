"""Standalone finite-field checks for ternary quadratic regular-multiplication Jordan strata.
Run: python3 research12_checker.py. Only prime fields are used for sample checks;
the proof covers all finite extensions of every odd prime field.
"""
from itertools import product
from math import factorial
from random import Random
from collections import Counter

TERMS = ((2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1))

def poly_multiply(P,Q,p):
    out={}
    for a,ca in P.items():
        for b,cb in Q.items():
            t=tuple(a[i]+b[i] for i in range(3))
            if max(t)>=p:continue
            out[t]=(out.get(t,0)+ca*cb)%p
    return {t:c for t,c in out.items() if c}

def matrix_rank(columns,p):
    pivots={}
    for column in columns:
        v={j:c%p for j,c in column.items() if c%p}
        while v:
            pivot=max(v)
            if pivot not in pivots:
                scale=pow(v[pivot],-1,p)
                pivots[pivot]={j:c*scale%p for j,c in v.items()}
                break
            f=v[pivot]
            for j,c in pivots[pivot].items():
                val=(v.get(j,0)-f*c)%p
                if val:v[j]=val
                elif j in v:del v[j]
    return len(pivots)

def form_rank(coeffs,p):
    inv2=pow(2,-1,p)
    a,b,c,d,e,f=coeffs
    A=[[a,d*inv2%p,e*inv2%p],[d*inv2%p,b,f*inv2%p],[e*inv2%p,f*inv2%p,c]]
    return matrix_rank([{i:A[i][j] for i in range(3) if A[i][j]} for j in range(3)],p)

def jordan_from_polynomial(coeffs,p,higher=None):
    monomials=list(product(range(p),repeat=3))
    indexes={e:i for i,e in enumerate(monomials)}
    Q={t:c%p for t,c in zip(TERMS,coeffs) if c%p}
    if higher:
        Q.update({t:c%p for t,c in higher.items() if c%p})
    powers={(0,0,0):1}
    ranks=[p**3]
    for k in range(1,p+1):
        powers=poly_multiply(powers,Q,p)
        cols=[]
        for e in monomials:
            col={}
            for a,c in powers.items():
                dest=tuple(a[j]+e[j] for j in range(3))
                if max(dest)<p:col[indexes[dest]]=c
            cols.append(col)
        ranks.append(matrix_rank(cols,p))
    ranks.append(0)
    assert ranks[p]==0
    blocks={j:ranks[j-1]-2*ranks[j]+ranks[j+1] for j in range(1,p+1)}
    return {j:b for j,b in blocks.items() if b}

def predicted(rank,p):
    m=(p-1)//2
    if rank==0:return {1:p**3}
    if rank==1:
        c=Counter([m,m+1]);return {j:p*p*v for j,v in c.items()}
    if rank==2:return {**{j:2*p for j in range(1,p)},p:p}
    if rank==3:return {**{j:4*min(j,p-j) for j in range(1,p)},p:(p*p+1)//2}
    raise AssertionError

def run():
    for p in [3,5,7]:
        vectors=list(product(range(p),repeat=6)) if p==3 else [tuple([0]*6), (1,0,0,0,0,0), (0,0,0,1,0,0), (0,0,1,1,0,0)]
        if p!=3:
            rng=Random(110619)
            vectors += [tuple(rng.randrange(p) for i in range(6)) for j in range(24 if p==5 else 10)]
        counts=Counter()
        for c in vectors:
            r=form_rank(c,p)
            blocks=jordan_from_polynomial(c,p)
            expectation=predicted(r,p)
            assert blocks==expectation,(p,c,r,blocks,expectation)
            counts[r]+=1
        if p==3:
            theoretical={0:1,1:p**3-1,2:p*p*(p**3-1),3:p*p*(p-1)*(p**3-1)}
            assert dict(counts)==theoretical,(counts,theoretical)
        print(f'prime={p}, quadratic_forms_tested={len(vectors)}, rank_counts={dict(sorted(counts.items()))}, all_Jordan_partitions_match=True')
    for p in [3,5]:
        rng=Random(250719)
        high=[e for e in product(range(p),repeat=3) if sum(e)>=3]
        tests=16 if p==3 else 8
        for t in range(tests):
            while True:
                coeff=tuple(rng.randrange(p) for _ in range(6))
                if form_rank(coeff,p)==3:break
            higher={e:rng.randrange(p) for e in high}
            assert jordan_from_polynomial(coeff,p,higher)==predicted(3,p)
        print(f'prime={p}, random_higher_order_full_rank_lifts_tested={tests}, rigid_Jordan_type_matches=True')
    for p in [3,5,7,11,13,17,19]:
        m=(p-1)//2
        tally=Counter({p:p})
        for a in range(1,p):
            for b in [m,m+1]:
                lo,hi=sorted((a,b))
                if lo+hi<=p+1:
                    blocks=[lo+hi-2*i+1 for i in range(1,lo+1)]
                else:
                    blocks=[p]*(lo+hi-p)+[hi-lo+2*i-1 for i in range(1,p-hi+1)]
                for j in blocks:tally[j]+=2
        assert dict(tally)==predicted(3,p)
        print(f'prime={p}, modular_fusion_decomposition_matches=True')
    print('PASS: independent polynomial-power linear algebra and modular fusion agree with all predicted Jordan partitions.')

if __name__=='__main__':run()
