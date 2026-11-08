"""Exact finite verification of multipartite Lipschitz-spread claims.

The universal proof in RESULT.md does not depend on finite enumeration.
Run: python3 checks/verify_multipartite_spread.py
"""
from fractions import Fraction
from itertools import product


def partitions(total, low=1):
    if total == 0:
        yield ()
        return
    for first in range(low, total+1):
        for rest in partitions(total-first, first):
            yield (first,) + rest


def metrics(parts):
    labels = [j for j, t in enumerate(parts) for _ in range(t)]
    n = len(labels)
    return [(i,j) for i in range(n) for j in range(i+1,n) if labels[i]!=labels[j]]


def val(seq):
    n = len(seq)
    return Fraction(n*sum(t*t for t in seq)-sum(seq)**2,n*n)


def predicted(parts):
    n = sum(parts)
    m = max(parts)
    binary = Fraction((n*n)//4,n*n)
    trilevel = Fraction(m*n-(m&1),n*n) if m>=2 else Fraction(-1)
    return max(binary,trilevel),binary,trilevel


def is_equality_shape(x,parts,base,tri):
    n = sum(parts); m=max(parts)
    values = sorted(set(x))
    if len(values)==2 and values[1]-values[0]==1:
        ones=sum(t==values[1] for t in x)
        return base==max(base,tri) and ones in (n//2,(n+1)//2)
    if len(values)==3 and values[2]-values[0]==2 and values[1]-values[0]==1 and m>=2:
        s=0
        for p in parts:
            block=x[s:s+p];s+=p
            if p==m and set(block)=={values[0],values[2]} and all(y==values[1] for y in x[:s-p]+x[s:]):
                return tri==max(base,tri) and abs(block.count(values[0])-block.count(values[2])) <=1
    return False


def verify():
    tested=0; profiles=0; maximizers=0
    for n in range(2,9):
        for parts in partitions(n):
            if len(parts)<2: continue
            edges=metrics(parts)
            best,binary,trilevel=predicted(parts)
            direct=Fraction(-1)
            equal=[]
            # Integer feasible potentials with first value anchored at zero.
            # Any extreme point is present, by the tight-spanning-tree argument.
            for rest in product(range(-2,3),repeat=n-1):
                x=(0,)+rest
                if any(abs(x[i]-x[j])>1 for i,j in edges): continue
                profiles+=1
                v=val(x)
                if v>direct: direct=v;equal=[x]
                elif v==direct: equal.append(x)
            assert direct==best,(parts,direct,best)
            for x in equal:
                assert is_equality_shape(x,parts,binary,trilevel),(parts,x,best)
            # Conversely every equality-shape configuration is globally optimal.
            for rest in product(range(-2,3),repeat=n-1):
                x=(0,)+rest
                if is_equality_shape(x,parts,binary,trilevel):
                    assert all(abs(x[i]-x[j])<=1 for i,j in edges),(parts,x)
                    assert val(x)==best,(parts,x)
            tested+=1; maximizers+=len(equal)
    print('EXHAUSTIVE_INTEGER_LIPSCHITZ_PROFILES_AND_EQUALITY_SHAPES_OK',tested,profiles,maximizers)
    cases=0
    for n in range(4,1001):
        q=(n*n)//4
        for m in range(1,n):
            r=m*n-(m&1)
            if m<=n//4: assert r<=q
            else: assert r>q
            if r==q: assert n%8==0 and m==n//4
            cases+=1
    print('SHARP_QUARTER_PHASE_AND_TIE_CERTIFICATES_OK',cases)
    print('ALL_MULTIPARTITE_SPREAD_CHECKS_OK')

if __name__=='__main__':verify()
