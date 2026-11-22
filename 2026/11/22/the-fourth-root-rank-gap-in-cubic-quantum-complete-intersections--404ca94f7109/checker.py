#!/usr/bin/env python3
"""Independent finite-field enumeration of associative commutator ranks.

The multiplication table is constructed directly from the quotient relation
and does not use the normal-form matrix appearing in the proof.
"""
import itertools, random
from collections import Counter

BASIS=[(i,j) for i in range(3) for j in range(3)]
ACTIVE=[BASIS.index(p) for p in [(1,0),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]]

class Field:
    def __init__(self,q):
        self.q=q
        if q==4:
            self.add=lambda a,b:a^b
            def mul(a,b):
                z=0
                for i in range(2):
                    for j in range(2):
                        if (a>>i)&(b>>j)&1: z^=1<<(i+j)
                if z&8: z^=0b1100  # degree 3 reduction, not needed for GF(4)
                if z&4: z^=0b111
                return z
            self.mul=mul
        else:
            self.add=lambda a,b:(a+b)%q
            self.mul=lambda a,b:(a*b)%q
    def neg(self,a):return a if self.q==4 else (-a)%self.q
    def sub(self,a,b):return self.add(a,self.neg(b))
    def pow(self,a,n):
        z=1
        for _ in range(n):z=self.mul(z,a)
        return z
    def inv(self,a):
        assert a
        for b in range(1,self.q):
            if self.mul(a,b)==1:return b
        raise AssertionError('field inverse missing')

def multiplication_table(F,lam):
    table={}
    for i,(a,b) in enumerate(BASIS):
        for j,(c,d) in enumerate(BASIS):
            if a+c<3 and b+d<3:
                table[i,j]=(BASIS.index((a+c,b+d)), F.pow(lam,b*c))
    return table

def rank(F,M):
    A=[x[:] for x in M]
    r=0
    for c in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][c]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=F.inv(A[r][c])
        A[r]=[F.mul(inv,x) for x in A[r]]
        for i in range(r+1,len(A)):
            if A[i][c]:
                z=A[i][c]
                A[i]=[F.sub(v,F.mul(z,w)) for v,w in zip(A[i],A[r])]
        r+=1
        if r==len(A):break
    return r

def comm_rank(F,T,coordinates):
    # Nine basis outputs and seven active input directions.
    a=[0]*9
    for j,v in zip(ACTIVE,coordinates):a[j]=v
    M=[[0]*7 for _ in range(9)]
    for col,j in enumerate(ACTIVE):
        for i,coef in enumerate(a):
            if not coef:continue
            t=T.get((i,j)); u=T.get((j,i))
            if t:
                row,w=t; M[row][col]=F.add(M[row][col],F.mul(coef,w))
            if u:
                row,w=u; M[row][col]=F.sub(M[row][col],F.mul(coef,w))
    return rank(F,M)

def predicted(q,lam,F):
    if lam==1:return (q**7,0,0,0,0)
    if lam==F.neg(1):return (q**4,0,q**7-q**4,0,0)
    if F.add(F.pow(lam,2),1)==0:
        return (1,(q+1)*(q*q-1),q**5-q**3-q**2+q,0,(q*q-1)*q**5)
    return (1,q*q-1,q*q*(q*q+q-2),q*q*(q-1)*(q*q-1),(q*q-1)*q**5)

def run(q,lam,exhaustive=True,samples=1000):
    F=Field(q);T=multiplication_table(F,lam)
    rng=random.Random(97341+q*11+lam)
    rows=itertools.product(range(q),repeat=7) if exhaustive else (tuple(rng.randrange(q) for i in range(7)) for _ in range(samples))
    seen=Counter(comm_rank(F,T,x) for x in rows)
    expected=predicted(q,lam,F)
    if exhaustive:
        actual=tuple(seen.get(i,0) for i in range(5))
        assert actual==expected,(q,lam,actual,expected)
    else:
        assert all(expected[j] for j in seen),(q,lam,seen,expected)
    print('field',q,'twist',lam,'exhaustive' if exhaustive else 'sample',sum(seen.values()),'rank_counts',[seen[j] for j in range(5)],'PASS')

if __name__=='__main__':
    for q,lam in [(2,1),(3,1),(3,2),(4,1),(4,2),(4,3),(5,1),(5,2),(5,4)]:
        run(q,lam,exhaustive=True)
    for q,lam in [(7,2),(7,3),(7,6),(11,2),(11,10)]:
        run(q,lam,exhaustive=False,samples=1300)
