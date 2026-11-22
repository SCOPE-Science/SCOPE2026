"""Exact verification of a two-hard-core-particle graph Hamiltonian and transport.
Scientific definitions: two occupied distinct vertices of K_{p,q}, unit hopping,
no diagonal terms. All checker input data are built in this file.
"""
import itertools
import math
import sympy as sp
from collections import Counter

def model(p,q):
    verts=list(itertools.combinations(range(p+q),2)); loc={v:i for i,v in enumerate(verts)}
    N=len(verts); H=sp.zeros(N)
    for j,occupied in enumerate(verts):
        for u in occupied:
            for v in range(p+q):
                if (u<p)!=(v<p) and v not in occupied:
                    new=tuple(sorted((set(occupied)-{u})|{v}))
                    H[loc[new],j]=1
    return H,verts

def checks():
    count=0
    for p in range(3,8):
      for q in range(3,8):
        H,verts=model(p,q); N=H.rows
        AA=[j for j,(u,v) in enumerate(verts) if v<p]
        BB=[j for j,(u,v) in enumerate(verts) if u>=p]
        AB=[j for j,(u,v) in enumerate(verts) if u<p<=v]
        B=H.extract(AB,AA+BB)
        gram=B*B.T
        predicted=Counter()
        predicted[sp.Integer(4*p*q-2*p-2*q)]+=1
        predicted[sp.Integer(q*(p-2))]+=p-1
        predicted[sp.Integer(p*(q-2))]+=q-1
        actual=Counter({e:m for e,m in gram.eigenvals().items() if e!=0})
        assert actual==predicted,(p,q,actual,predicted)
        count+=1
        # AB diagonal spectral moments derived from claimed exact cosine formula
        x=AB[0]
        weights=[(sp.Rational((p-1)*(q-1),p*q),0),
                 (sp.Rational(1,p*q),4*p*q-2*p-2*q),
                 (sp.Rational(p-1,p*q),q*(p-2)),
                 (sp.Rational(q-1,p*q),p*(q-2))]
        assert sum(w for w,v in weights)==1
        J=sp.eye(N)
        for k in range(1,5):
            J=J*H*H
            assert J[x,x]==sum(w*sp.Integer(lam)**k for w,lam in weights),(p,q,k)
            count+=1
        # Localized AA to localized BB entry: first nonzero even moments 2,4,6,8
        i=AA[0];j=BB[0]; J=sp.eye(N)
        g2a=2*q*(p-1);g2b=2*p*(q-1);W=g2a+g2b
        for k in range(1,5):
            J=J*H*H
            expected=(2*p*q)*sp.Integer(W)**(k-1)
            # for any AA/BB distinct local pair, two-hop ways: 4 via common AB configurations,
            # same as 2pq / sqrt(C(p,2)C(q,2)) times normalization factor.
            expected=sp.Rational(2*p*q,sp.binomial(p,2)*sp.binomial(q,2))
            # full normalization cancellation: <i|A> = 1/sqrt(C(p,2)) etc.
            # <i|H^(2k)|j>=gA*gB*W^(k-1)/sqrt(C(p,2)C(q,2))
            expected=4*sp.Integer(W)**(k-1)
            assert J[i,j]==expected,(p,q,k,J[i,j],expected)
            count+=1
        assert sp.factor(g2a-g2b)==2*(p-q)
        count+=1
    # boundary p=q=2 is 4-cycle and yields perfect individual AA-to-BB transfer
    H,v=model(2,2); assert H.rows==6
    assert (H**2)[0,5]==4
    count+=1
    return count

if __name__=='__main__':
    print('ALL_EXACT_CHECKS_PASSED',checks())
