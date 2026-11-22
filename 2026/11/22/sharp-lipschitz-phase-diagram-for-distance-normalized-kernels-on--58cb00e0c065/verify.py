"""Exact-rational supplementary finite tests for weighted-star distance localization.

Only Python standard library is required. The symbolic proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def data(a, bs, q):
    m = len(bs)
    w = [F(a)] + [F(b) for b in bs]
    d = lambda x,y: 0 if x==y else (1 if (x==0 or y==0) else 2)
    rows = []
    for x in range(m+1):
        un = [w[y]*q**d(x,y) for y in range(m+1)]
        z = sum(un)
        rows.append([u/z for u in un])
    return rows


def exact_formula(a, bs, q, i):
    a, b = F(a), F(bs[i-1]); S = sum(map(F,bs))-b; B=b+S
    return (1-q*q)*b*(a+2*q*S)/((a+q*B)*(b+a*q+S*q*q))


def obstruction(a, bs, q, i):
    a,b=F(a),F(bs[i-1]); S=sum(map(F,bs))-b;B=b+S
    return b*(S-b)-a*a-2*a*B*q-S*(3*b+S)*q*q


def check(a,bs,q):
    assert len(bs)>=1 and a>0 and min(bs)>0 and 0<q<1
    m=len(bs)
    rows=data(a,bs,q)
    cols=[range(1,m+1)]
    brute=F(0)
    for signs in product((-1,1),repeat=m):
        f=(0,)+signs
        edge=max(abs(sum((rows[0][j]-rows[i][j])*f[j] for j in range(m+1))) for i in range(1,m+1))
        brute=max(brute,edge)
    vals=[exact_formula(a,bs,q,i) for i in range(1,m+1)]
    assert brute==max(vals)
    for i,c in enumerate(vals,start=1):
        # Direct construction of the sign extremizer for edge (0,i).
        f=(0,)+tuple(-1 if j==i else 1 for j in range(1,m+1))
        direct=abs(sum((rows[0][j]-rows[i][j])*f[j] for j in range(m+1)))
        assert direct==c
        assert (c>1)==(obstruction(a,bs,q,i)>0)
        assert c<2


def main():
    cases=0
    qs=(F(1,20),F(1,7),F(1,3),F(1,2),F(4,5),F(19,20))
    for m in range(1,6):
        for a in (F(1,5),F(1),F(9)):
            for bs in (tuple(F(1) for _ in range(m)),tuple(F(i) for i in range(1,m+1)),tuple(F(7-i) for i in range(1,m+1))):
                for q in qs:
                    check(a,bs,q)
                    cases+=1
    rng=Random(21113)
    for m in range(1,7):
        for _ in range(100):
            a=F(rng.randint(1,15),rng.randint(1,9))
            bs=[F(rng.randint(1,25),rng.randint(1,9)) for j in range(m)]
            q=F(rng.randint(1,40),41)
            check(a,bs,q)
            cases+=1
    # Uniform threshold at exactly four leaves; and unbalanced three-vertex amplification.
    assert exact_formula(1,[1]*3,F(1,100),1)<1
    assert exact_formula(1,[1]*4,F(1,100),1)>1
    assert exact_formula(F(1,10),[1,9],F(1,100),1)>1
    # Sharp unattained 2 as degree grows while q tends to zero slowly relative to 1/m.
    from math import isclose
    for m in (500,5000):
        q=F(1,round(m**.75))
        c=exact_formula(1,[1]*m,q,1)
        assert F(1)<c<F(2)
    print('PASS: %d weighted-star cases (exact rational) plus threshold and envelope probes' % cases)

if __name__=='__main__':
    main()
