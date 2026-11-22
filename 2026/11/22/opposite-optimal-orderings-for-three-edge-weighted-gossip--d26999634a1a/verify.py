#!/usr/bin/env python3
"""Exact symbolic and rational reproducibility checks for three-edge gossip."""
import itertools
from fractions import Fraction
import sympy as sp


def edge_matrices(params):
    mats=[]
    for j,p in enumerate(params,1):
        v=sp.zeros(4,1)
        v[0]=1
        v[j]=-1
        mats.append(sp.eye(4)-p*v*v.T)
    return mats


def product(mats, order):
    t=sp.eye(4)
    for k in order:
        t=mats[k]*t
    return t


def exact_error(t):
    return sp.expand(sp.trace(t.T*t)-1)


def nontrivial_sq_charpoly(t,z):
    # The vector of ones carries a single unit eigenvalue in t.T*t.
    return sp.div((t.T*t).charpoly(z).as_expr(),z-1,z)[0]


def verify():
    a,b,c=sp.symbols('a b c',positive=True)
    symbolic=edge_matrices((a,b,c))
    e1=exact_error(product(symbolic,(0,1,2)))
    e2=exact_error(product(symbolic,(0,2,1)))
    assert sp.factor(e1-e2-4*a*b*c*(1-a)*(c-b))==0
    assert sp.factor(e1-exact_error(product(symbolic,(2,1,0))))==0

    q=[sp.Rational(1,8),sp.Rational(1,4),sp.Rational(3,8)]
    mats=edge_matrices(q)
    J=sp.ones(4,4)/4
    z=sp.symbols('z')
    by_mid={}
    charpoly=None
    for perm in itertools.permutations(range(3)):
        t=product(mats,perm)
        assert t*sp.ones(4,1)==sp.ones(4,1)
        assert sp.ones(1,4)*t==sp.ones(1,4)
        E=exact_error(t)
        S=t.T*t
        U=sp.det(t)**2
        V=sp.det(sp.eye(4)-S+J)
        assert U==sp.prod((1-2*p)**2 for p in q)
        assert V==32*sp.prod(p*(1-p) for p in q)
        assert sp.simplify(sp.trace((t-J).T*(t-J))-E)==0
        poly=sp.expand(t.charpoly(z).as_expr())
        if charpoly is None:charpoly=poly
        else:assert sp.factor(poly-charpoly)==0
        squared=sp.factor(nontrivial_sq_charpoly(t,z))
        roots=sp.polys.polytools.intervals(squared,eps=sp.Rational(1,10**15))
        # root isolation is exact and includes all three roots in (0,1).
        assert len(roots)==3 and all(0<interval[0]<interval[1]<1 and multiplicity==1 for interval,multiplicity in roots)
        lo=max(interval[0] for interval,multiplicity in roots)
        hi=max(interval[1] for interval,multiplicity in roots)
        mid=perm[1]
        if mid in by_mid:
            old=by_mid[mid]
            assert E==old['E'] and (lo,hi)==old['interval']
        else:by_mid[mid]={'E':E,'interval':(lo,hi),'poly':squared}
    assert by_mid[0]['E']==sp.Rational(19565,16384)
    assert by_mid[1]['E']==sp.Rational(19505,16384)
    assert by_mid[2]['E']==sp.Rational(19421,16384)
    assert by_mid[0]['interval'][1]<by_mid[1]['interval'][0]<by_mid[1]['interval'][1]<by_mid[2]['interval'][0]

    # Independent exact rational parameter checks for all six schedules.
    samples=0
    for i,j,k in itertools.combinations(range(1,12),3):
        if (i+j+k)%7:continue
        ps=tuple(sp.Rational(h,13) for h in (i,j,k))
        m=edge_matrices(ps)
        errors={}
        eig_intervals={}
        for perm in itertools.permutations(range(3)):
            t=product(m,perm)
            E=exact_error(t)
            poly=nontrivial_sq_charpoly(t,z)
            intervals=sp.polys.polytools.intervals(poly,eps=sp.Rational(1,10**10))
            Rlo,Rhi=max((iv[0][0],iv[0][1]) for iv in intervals)
            if perm[1] in errors:
                assert E==errors[perm[1]]
            else:
                errors[perm[1]]=E
                eig_intervals[perm[1]]=(Rlo,Rhi)
        ordered=sorted(range(3),key=lambda h:ps[h])
        assert errors[ordered[0]]>errors[ordered[1]]>errors[ordered[2]]
        assert eig_intervals[ordered[0]][1]<eig_intervals[ordered[1]][0]
        assert eig_intervals[ordered[1]][1]<eig_intervals[ordered[2]][0]
        samples+=1
    assert samples>=15
    print('PASS: symbolic ordering identity, reversal, exact invariants,')
    print('six exact rational spectra and optimizer comparisons;')
    print(samples,'additional distinct rational triples checked.')
    for mid in range(3):
        print('middle',q[mid],': E=',by_mid[mid]['E'],', worst-case root interval=',by_mid[mid]['interval'])


if __name__=='__main__':
    verify()
