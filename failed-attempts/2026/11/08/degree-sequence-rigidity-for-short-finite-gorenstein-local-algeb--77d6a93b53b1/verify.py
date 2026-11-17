#!/usr/bin/env python3
"""Independent finite-field zero-divisor graph degree enumeration for short Gorenstein algebras.

Run with Python 3 (standard library only). This tests finite instances rather
than proving the all-field theorem. Different implementations of the ring
product and the predicted degree multiplicities are compared.
"""
from collections import Counter
from itertools import product


def field(p,poly=None):
    if poly is None:
        return p, lambda a,b:(a+b)%p, lambda a,b:(a*b)%p
    # Binary field with monic irreducible defining polynomial.
    d=poly.bit_length()-1; q=1<<d
    def multiply(a,b):
        c=0
        while b:
            if b&1:c^=a
            b>>=1; a<<=1
            if a&q:a^=poly
        return c
    return q,lambda a,b:a^b,multiply


def invertible(M, q,add,mul):
    n=len(M); A=[row[:] for row in M]; j=0
    for k in range(n):
        pivot=next((i for i in range(j,n) if A[i][k]),None)
        if pivot is None:continue
        A[j],A[pivot]=A[pivot],A[j]
        for i in range(j+1,n):
            if not A[i][k]:continue
            for b in range(1,q):
                if mul(b,A[j][k])==A[i][k]:break
            else:raise AssertionError('field division failure')
            A[i]=[add(A[i][h],mul(b,A[j][h])) for h in range(n)] if q&(q-1)==0 else [(A[i][h]-mul(b,A[j][h]))%q for h in range(n)]
        j+=1
    return j==n


def isotropic_count(M, q,add,mul):
    n=len(M); count=0
    for v in product(range(q),repeat=n):
        s=0
        for i in range(n):
            for j in range(n):
                s=add(s,mul(v[i],mul(M[i][j],v[j])))
        count+=(s==0)
    return count


def predicted(q,n,I):
    return Counter({q**(n+1)-2:q-1,q**n-2:q*(I-1),q**n-1:q*(q**n-I)})


def direct_degrees(M,q,add,mul):
    n=len(M)
    elements=list(product(range(q),repeat=n+1))
    elements.remove((0,)*(n+1))
    def product_zero(x,y):
        s=0
        for i in range(n):
            if x[i]:
                for j in range(n):
                    s=add(s,mul(x[i],mul(M[i][j],y[j])))
        return s==0
    out=Counter()
    for ix,x in enumerate(elements):
        out[sum(x!=y and product_zero(x,y) for y in elements)]+=1
    return out


def test_field(p,poly,nmax,exhaustive):
    q,add,mul=field(p,poly)
    tested=0; split={}
    for n in range(2,nmax+1):
        pairs=[(i,j) for i in range(n) for j in range(i,n)]
        cases=product(range(q),repeat=len(pairs))
        for k,values in enumerate(cases):
            if not exhaustive and k>=12:break
            M=[[0]*n for _ in range(n)]
            for (i,j),v in zip(pairs,values):M[i][j]=M[j][i]=v
            if not invertible(M,q,add,mul):continue
            I=isotropic_count(M,q,add,mul)
            if p==2:
                exact_I=q**n if all(M[i][i]==0 for i in range(n)) else q**(n-1)
            elif n%2:
                exact_I=q**(n-1)
            else:
                # Test cases here use n=2 over odd prime fields.
                det=(M[0][0]*M[1][1]-M[0][1]*M[1][0])%q
                sign=pow((-det)%q,(q-1)//2,q)
                assert sign in (1,q-1)
                exact_I=q**(n-1)+(q-1)*(1 if sign==1 else -1)
            assert I==exact_I,('isotropic count',q,n,M,I,exact_I)
            pred=predicted(q,n,I)
            pred=+pred  # discard possible zero-multiplicity degree strata
            actual=direct_degrees(M,q,add,mul)
            assert actual==pred,(q,n,M,I,actual,pred)
            typ=('alternating' if (q&(q-1)==0 and all(M[i][i]==0 for i in range(n))) else 'nonalternating') if p==2 else 'odd'
            split.setdefault((n,typ),set()).add(I)
            tested+=1
    print('field',q,'nmax',nmax,'tested',tested,'isotropic strata',split)
    return tested

if __name__=='__main__':
    count=0
    count+=test_field(2,None,3,True)
    count+=test_field(3,None,2,True)
    count+=test_field(2,0b111,2,True)
    count+=test_field(5,None,2,False)
    count+=test_field(2,0b1011,2,False)
    print('VERIFY_OK',count)
