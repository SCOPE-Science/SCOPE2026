#!/usr/bin/env python3
"""Exact, dependency-free checks for odd binary-form quadratic hulls.

Reconstructs the three (r-1)-st transvectant coefficients using the
binomial-coordinate normalization f=sum binom(r,i)*a_i*x^(r-i)*y^i.
In the a0=1,a1=0 slice, eliminates the two linear pivots and checks
weighted homogeneity, transverse quadratic rank, and small explicit
critical-value identities. These finite checks are not a proof for all r.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb


def add(out, mon, coef):
    out[tuple(sorted(mon))] += Fraction(coef)


def raw_q(r, h):
    # h=0,1,2 is the coefficient of x^(2-h)*y^h in (f,f)_(r-1).
    k = r - 1
    out = defaultdict(Fraction)
    for i in range(k+1):
        c = (-1)**i * comb(k, i)
        pairs = ([(i,k-i)] if h==0 else
                 [(i,k-i+1),(i+1,k-i)] if h==1 else
                 [(i+1,k-i+1)])
        for ii,jj in pairs:
            if ii==1 or jj==1:
                continue
            mon = [j for j in (ii,jj) if j!=0]
            add(out,mon,c)
    return {a:b for a,b in out.items() if b}


def plus(P,Q,scalar=1):
    out=defaultdict(Fraction,P)
    for m,c in Q.items():add(out,m,scalar*c)
    return {m:c for m,c in out.items() if c}


def mul_monomial(P,i,coef=1):
    out=defaultdict(Fraction)
    for m,c in P.items():add(out,m+(i,),coef*c)
    return {m:c for m,c in out.items() if c}


def eliminate(r):
    q0,q1,q2=[raw_q(r,h) for h in range(3)]
    assert q0.get((r-1,))==2 and q1.get((r,))==2
    b=plus(q0,{(r-1,):Fraction(-2)})
    sol={mon:-c/2 for mon,c in b.items()}
    # q2 has a_(r-1) only linearly, and no a_r after a1=0.
    F=defaultdict(Fraction)
    for mon,c in q2.items():
        assert r not in mon
        if r-1 in mon:
            others=list(mon);others.remove(r-1)
            assert len(others)==1
            for m,v in sol.items():add(F,m+tuple(others),c*v)
        else:add(F,mon,c)
    F={m:c for m,c in F.items() if c}
    assert all(2<=i<=r-2 for m in F for i in m)
    assert all(sum(m)==r+1 for m in F)
    return F


def hessian(F, vars):
    result=[]
    for x in vars:
        row=[]
        for y in vars:
            m=tuple(sorted((x,y)))
            row.append(F.get(m,0)*(2 if x==y else 1))
        result.append(row)
    return result


def det(M):
    M=[[Fraction(z) for z in row] for row in M]
    n=len(M);d=Fraction(1)
    for i in range(n):
        j=next((j for j in range(i,n) if M[j][i]!=0),None)
        if j is None:return 0
        if j!=i: M[i],M[j]=M[j],M[i]; d=-d
        v=M[i][i];d*=v
        for j in range(i+1,n):
            w=M[j][i]/v
            for k in range(i,n):M[j][k]-=w*M[i][k]
    return d


def evaluate(P, sub):
    out=defaultdict(Fraction)
    for m,c in P.items():
        val=c;exp=0
        for i in m:
            z=sub.get(i,(0,0))
            val*=z[0];exp+=z[1]
        if val:add(out,(exp,),val)
    return {e[0]:v for e,v in out.items() if v}


def differentiate(P,i):
    out=defaultdict(Fraction)
    for m,c in P.items():
        k=m.count(i)
        if k:
            mm=list(m);mm.remove(i)
            add(out,tuple(mm),k*c)
    return {m:c for m,c in out.items() if c}


def run():
    samples={
        5: ({3:(0,0)},Fraction(24),3),
        7: ({3:(0,0),4:(Fraction(9,2),2),5:(0,0)},Fraction(405),4),
        9: ({3:(0,0),4:(4,2),5:(0,0),6:(40,3),7:(0,0)},Fraction(8960),5),
    }
    for r in (5,7,9,11,13,15):
        F=eliminate(r)
        z=list(range(3,r-1))
        d=det(hessian(F,z))
        assert d!=0,('degenerate quadratic part',r)
        print('QUADRATIC_RANK_OK',r,len(z),'DETERMINANT',d)
        if r in samples:
            sample,critical_val,exp=samples[r]
            sample={2:(Fraction(1),1),**sample}
            for i in z:
                assert not evaluate(differentiate(F,i),sample),(r,i,'not critical')
            assert evaluate(F,sample)=={exp:critical_val},(r,'incorrect critical value')
            print('CRITICAL_VALUE_OK',r,critical_val,exp)
    print('CERTIFICATE_OK')

if __name__=='__main__':run()
