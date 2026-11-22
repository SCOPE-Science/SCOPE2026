#!/usr/bin/env python3
"""Independent integral orbit-chain check for length-two Hamming nerve quotients.

Each translation-orbit of cells has a unique normalized representative with
first coordinate zero. Uses signed cellular boundaries in the simplicial-set
realization; no geometric identification of ordered reversed edges occurs.
Requires SymPy for exact integer Smith normal form.
"""
from itertools import product
from math import comb
from collections import Counter
from sympy import ZZ,Matrix
from sympy.matrices.normalforms import smith_normal_form


def main():
    for d,q in [(1,2),(1,3),(1,4),(2,2),(2,3),(3,2),(3,3)]:
        origin=(0,)*d
        V=list(product(range(q),repeat=d))
        weight=lambda u: sum(x!=0 for x in u)
        sub=lambda u,v:tuple((a-b)%q for a,b in zip(u,v))
        edges=[v for v in V if weight(v) in (1,2)]
        nbr=[v for v in V if weight(v)==1]
        rows={v:i for i,v in enumerate(edges)}
        columns=[(a,tuple((x+y)%q for x,y in zip(a,b))) for a in nbr for b in nbr]
        M=Matrix.zeros(len(edges),len(columns))
        for j,(a,z) in enumerate(columns):
            # d(0,a,z)=(a,z)-(0,z)+(0,a), normalized by translation
            M[rows[sub(z,a)],j]+=1
            if z!=origin:M[rows[z],j]-=1
            M[rows[a],j]+=1
        S=smith_normal_form(M,domain=ZZ)
        diag=[abs(int(S[i,i])) for i in range(min(S.rows,S.cols)) if S[i,i]]
        units=diag.count(1);tors=sorted(x for x in diag if x>1)
        assert len(diag)==len(edges), (d,q,len(edges),len(diag))
        assert tors==[q]*d, (d,q,tors)
        b2=len(columns)-len(diag)
        k=comb(d+1,2)*(q-1)**2-d*(q-1)+1
        assert b2==k-1
        print(f'H({d},{q})/T: C=(1,{len(edges)},{len(columns)}), SNF(d2)=1^{units}, {q}^{d}; H1=(Z/{q})^{d}, H2=Z^{b2}',flush=True)

if __name__=='__main__':main()
