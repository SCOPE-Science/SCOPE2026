#!/usr/bin/env python3
"""Exact tests for a central Boolean-ball Walsh frequency substitution.

Standard library only. Finite tests support the stated analytic theorem.
"""
from math import comb
from fractions import Fraction


def krawtchouk(j,w,n):
    return sum((-1)**a*comb(w,a)*comb(n-w,j-a)
               for a in range(max(0,j-(n-w)),min(j,w)+1))


def direct_walsh(n,r,w):
    eta=(1<<w)-1
    return sum(1 if (x&eta).bit_count()%2==0 else -1
               for x in range(1<<n) if x.bit_count()<=r)


def check():
    exact=0
    for r in range(1,21):
        n=2*r+1
        for s in range(r+1):
            w=2*s+1
            lhs=krawtchouk(r,w-1,2*r)*comb(2*r,2*s)
            rhs=(-1)**s*comb(2*r,r)*comb(r,s)
            assert lhs==rhs,(r,s,lhs,rhs)
            exact+=1
        ratios=[Fraction(comb(2*r,r)*comb(r,s),2**(2*r)*comb(2*r,2*s))
                for s in range(r+1)]
        best={s for s,z in enumerate(ratios) if z==max(ratios)}
        worst={s for s,z in enumerate(ratios) if z==min(ratios)}
        assert best=={0,r} and worst=={r//2,(r+1)//2},(r,best,worst)
    assert exact==230
    for r in range(1,6):
        n=2*r+1
        M=1<<(2*r)
        B=[x for x in range(1<<n) if x.bit_count()<=r]
        E=[x for x in range(1<<n) if x.bit_count()%2==0]
        assert len(B)==len(E)==M
        # Every even nonzero frequency has zero Walsh coefficient.
        for e in E[1:]:
            assert sum((-1)**((x&e).bit_count()%2) for x in B)==0
        for w in range(1,n+1,2):
            s=(w-1)//2
            W=direct_walsh(n,r,w)
            assert W*comb(2*r,2*s)==(-1)**s*comb(2*r,r)*comb(r,s)
            # Complete Parseval on the retained-even orthogonal character basis.
            mu=(1<<w)-1
            coeff=[sum((-1)**((x&(mu^e)).bit_count()%2) for x in B)
                   for e in E]
            assert sum(c*c for c in coeff)==M*M
            assert coeff[0]!=0
    print('VERIFY_OK exact_krawtchouk=230 direct_boolean_balls=5 parity_and_parseval=5 optimal_index=20')

if __name__=='__main__':
    check()
