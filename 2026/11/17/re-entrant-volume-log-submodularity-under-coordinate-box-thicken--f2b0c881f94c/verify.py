#!/usr/bin/env python3
"""Reproduce exact four-dimensional zonotope-volume defect coefficients.

Requires Python >=3.9 only. Computes all maximal minors by integer determinants;
no data files, symbolic packages, or numerically estimated coefficients required.
"""
from itertools import combinations, permutations, product
from fractions import Fraction

V = [
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 1, 0, -1),
    (0, 0, 1, -1),
    (1, -1, -1, 0),
]
W = (1, 0, 0, -1)
Q = (0, 1, -1, 0)
E = [tuple(int(i == j) for i in range(4)) for j in range(4)]
ZERO = (0, 0, 0, 0)


def determinant_four(columns):
    out = 0
    for perm in permutations(range(4)):
        inv = sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
        term = -1 if inv % 2 else 1
        for i in range(4):
            term *= columns[perm[i]][i]
        out += term
    return out


def add(A, B):
    R = dict(A)
    for k, v in B.items():
        R[k] = R.get(k, 0) + v
        if not R[k]:
            del R[k]
    return R


def mul(A, B):
    R = {}
    for a, x in A.items():
        for b, y in B.items():
            c = tuple(a[i] + b[i] for i in range(4))
            R[c] = R.get(c, 0) + x*y
    return {k:v for k,v in R.items() if v}


def volume_poly(base):
    """Volume as multiaffine polynomial in box side lengths t1..t4."""
    generators = base + E
    shift = len(base)
    coeff = {}
    for index in combinations(range(len(generators)), 4):
        det = abs(determinant_four([generators[i] for i in index]))
        if not det:
            continue
        powers = tuple(int(shift + j in index) for j in range(4))
        coeff[powers] = coeff.get(powers, 0) + det
    return coeff


def block_reduce(P):
    """(t1,t2,t3,t4) = (u,v,v,u): exponent pair to coefficient."""
    out = {}
    for e, coefficient in P.items():
        pair = (e[0] + e[3], e[1] + e[2])
        out[pair] = out.get(pair,0) + coefficient
    return out


def val(P, *ts):
    return sum(Fraction(c) * __import__('functools').reduce(lambda x,y:x*y,
                    (Fraction(ts[j])**e[j] for j in range(4)), Fraction(1))
               for e,c in P.items())


def main():
    checks=0
    a,b,c,d = [volume_poly(V + appended) for appended in ([],[W],[Q],[W,Q])]
    for p in (a,b,c,d):
        assert all(x>=0 for x in p.values())
        assert all(all(ei in (0,1) for ei in k) for k in p)
        checks+=2
    # Directly observed zeroth-order determinants, matching source's four volumes.
    assert [p.get(ZERO) for p in (a,b,c,d)] == [14,30,26,56]
    checks+=1
    defect=add(mul(a,d),{k:-v for k,v in mul(b,c).items()})
    target = {
      (2,2,0,0):-1,(2,1,1,0):2,(2,0,2,0):-1,(2,0,0,0):-4,
      (1,2,0,1):2,(1,1,1,0):8,(1,1,0,1):6,(1,1,0,0):8,
      (1,0,2,1):2,(1,0,1,1):6,(1,0,1,0):8,(1,0,0,1):4,
      (0,2,0,2):-1,(0,1,1,0):8,(0,1,0,2):-4,(0,1,0,0):8,
      (0,0,2,2):-1,(0,0,1,2):-4,(0,0,1,0):8,
      (0,0,0,2):-8,(0,0,0,1):-4,(0,0,0,0):4,
    }
    assert defect==target, ('four-variable formula mismatch',defect)
    checks+=1
    expected={
      'A':{(2,2):1,(2,1):6,(2,0):8,(1,2):4,(1,1):20,(1,0):22,(0,2):4,(0,1):16,(0,0):14},
      'AB':{(2,2):1,(2,1):6,(2,0):8,(1,2):6,(1,1):32,(1,0):38,(0,2):8,(0,1):32,(0,0):30},
      'AC':{(2,2):1,(2,1):8,(2,0):14,(1,2):4,(1,1):28,(1,0):40,(0,2):4,(0,1):24,(0,0):26},
      'ABC':{(2,2):1,(2,1):8,(2,0):14,(1,2):6,(1,1):44,(1,0):68,(0,2):8,(0,1):48,(0,0):56},
    }
    for name,p in zip(('A','AB','AC','ABC'),(a,b,c,d)):
        assert block_reduce(p)==expected[name], (name,block_reduce(p))
        checks+=1
    # 2[(u+2)^2*v*(v+2)-2*(u+1)*(2*u-1)]
    target_blocks={
       (2,2):2,(2,1):4,(2,0):-8,
       (1,2):8,(1,1):16,(1,0):-4,
       (0,2):8,(0,1):16,(0,0):4
    }
    assert block_reduce(defect)==target_blocks
    checks+=1
    # Exact rational specialization and sign tests with independently computed
    # four determinants at 121 pairs; no floating-point sign decisions.
    samples=[Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1),Fraction(3,2),Fraction(2),Fraction(4),Fraction(10)]
    for u,v in product(samples,repeat=2):
        raw=val(a,u,v,v,u)*val(d,u,v,v,u)-val(b,u,v,v,u)*val(c,u,v,v,u)
        formula=2*((u+2)**2*v*(v+2)-2*(u+1)*(2*u-1))
        assert raw==formula,(u,v,raw,formula)
        checks+=1
    # Full anisotropic polynomial: coefficientwise, hence all nonnegative weights.
    for weights in [(0,0,0,0),(1,1,1,1),(0,0,0,1),(1,0,0,0),
                    (Fraction(1,3),2,Fraction(5,2),4),
                    (2,0,0,2),(3,1,1,3)]:
        aa,bb,cc,dd = (val(p,*weights) for p in (a,b,c,d))
        assert aa*dd-bb*cc==val(target,*weights)
        checks+=1
    print('PASS',checks,'assertion groups',len(target),'nonzero four-variable defect monomials')
    print('Block defect:',sorted(target_blocks.items()))

if __name__=='__main__':main()
