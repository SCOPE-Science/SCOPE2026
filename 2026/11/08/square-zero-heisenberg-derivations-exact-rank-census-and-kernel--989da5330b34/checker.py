#!/usr/bin/env python3
"""Direct finite-field checks of square-zero Heisenberg derivation counts."""
from itertools import product
from collections import Counter
from math import prod

class Field:
    def __init__(self,q):
        assert q in (2,3,4)
        self.q=q
    def add(self,a,b): return (a^b) if self.q==4 else (a+b)%self.q
    def neg(self,a): return a if self.q in (2,4) else (-a)%3
    def mul(self,a,b):
        if self.q!=4: return (a*b)%self.q
        v=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1): v^=1<<(i+j)
        if v&8: v^=0b1110 # x^3=x(x+1)=x^2+x = 1 (since x^2=x+1), so x^3=1
        if v&4: v^=0b111 # x^2=x+1
        return v
    def pow(self,a,k):
        v=1
        for _ in range(k): v=self.mul(v,a)
        return v
    def inv(self,a):
        assert a
        return self.pow(a,self.q-2)

def matmul(A,B,F):
    return [[sumfield((F.mul(a,b) for a,b in zip(row,col)),F) for col in zip(*B)] for row in A]

def sumfield(vals,F):
    s=0
    for v in vals:s=F.add(s,v)
    return s

def mv(A,v,F):return [sumfield((F.mul(a,b) for a,b in zip(row,v)),F) for row in A]

def dot(a,b,F):return sumfield((F.mul(x,y) for x,y in zip(a,b)),F)

def rr(A,F):
    M=[row[:] for row in A if any(row)]
    if not M:return [],0
    rows=len(M);cols=len(M[0]); i=0
    for j in range(cols):
        pivot=next((k for k in range(i,rows) if M[k][j]),None)
        if pivot is None:continue
        M[i],M[pivot]=M[pivot],M[i]
        fac=F.inv(M[i][j]);M[i]=[F.mul(v,fac) for v in M[i]]
        for k in range(rows):
            if k!=i and M[k][j]:
                c=M[k][j]
                M[k]=[F.add(v,F.neg(F.mul(c,w))) for v,w in zip(M[k],M[i])]
        i+=1
        if i==rows:break
    return M[:i],i

def rank(A,F):
    if not A:return 0
    return rr(A,F)[1]

def Jform(n,F):
    d=2*n
    J=[[0]*d for _ in range(d)]
    for i in range(n):J[i][n+i]=1;J[n+i][i]=F.neg(1)
    return J

def pairing(u,v,J,F):return dot(u,mv(J,v,F),F)

def is_sympl_inf(T,J,F):
    d=len(T)
    for i in range(d):
        for j in range(d):
            x=sumfield((F.mul(J[i][k],T[k][j]) for k in range(d)),F)
            y=sumfield((F.mul(T[k][i],J[k][j]) for k in range(d)),F)
            if F.add(x,y):return False
    return True

def is_squarezero(T,F):return all(not a for row in matmul(T,T,F) for a in row)

def gaussian(n,r,q):
    if not 0<=r<=n:return 0
    num=prod(q**(n-i)-1 for i in range(r))
    den=prod(q**(r-i)-1 for i in range(r))
    return num//den

def gl(r,q): return prod(q**r-q**i for i in range(r))

def isotropic_count(n,r,q):
    if not 0<=r<=n:return 0
    return prod(q**(2*n-i)-q**i for i in range(r))//gl(r,q)

def symmetric_non_degenerate_count(r,q):
    # Kernel-subspace recurrence, independent of orthogonal-group classification.
    a=[1]
    for k in range(1,r+1):
        a.append(q**(k*(k+1)//2)-sum(gaussian(k,j,q)*a[k-j] for j in range(1,k+1)))
    return a[r]

def expected(n,q):
    C=Counter()
    for r in range(n+1):
        m=isotropic_count(n,r,q)*symmetric_non_degenerate_count(r,q)
        C[(r,2*(n-r))]+=m*q**r
        if r<n:C[(r+1,2*(n-r-1))]+=m*(q**(2*n-r)-q**r)
    return C

def enumerate_direct(n,q):
    F=Field(q);d=2*n;J=Jform(n,F)
    obs=Counter();typecount=Counter(); derivcount=0; squarecount=0
    vectors=list(product(range(q),repeat=d))
    z=(0,)*d
    for entries in product(range(q),repeat=d*d):
        T=[list(entries[i*d:(i+1)*d]) for i in range(d)]
        if not is_sympl_inf(T,J,F):continue
        derivcount+=1
        if not is_squarezero(T,F):continue
        squarecount+=1
        r=rank(T,F)
        for f in vectors:
            if any(dot(f,mv(T,v,F),F) for v in vectors):continue
            # Recheck original basis Leibniz and full D^2 equations.
            for i in range(d):
                e=[int(j==i) for j in range(d)]
                assert mv(T,mv(T,e,F),F)==[0]*d
                assert dot(f,mv(T,e,F),F)==0
            for i in range(d):
                ei=[int(j==i) for j in range(d)]
                for j in range(d):
                    ej=[int(k==j) for k in range(d)]
                    # D[e_i,e_j]=0, and bracket RHS uses only T components.
                    assert F.add(pairing(mv(T,ei,F),ej,J,F),pairing(ei,mv(T,ej,F),J,F))==0
            fullD=[row[:]+[0] for row in T]+[list(f)+[0]]
            dr=rank(fullD,F)
            K=[list(v) for v in vectors if mv(T,v,F)==[0]*d and dot(f,v,F)==0]
            kerbasis, kdim=rr(K,F)
            restricted=[[pairing(v,w,J,F) for w in kerbasis] for v in kerbasis]
            br=rank(restricted,F) if restricted else 0
            assert kdim==d-dr
            obs[(dr,br)]+=1
            typecount[r]+=1
    return obs,typecount,derivcount,squarecount

def main():
    for n,q in ((1,2),(1,3),(1,4),(2,2)):
        obs,typ,nd,ns=enumerate_direct(n,q)
        exp=expected(n,q)
        assert obs==exp,(n,q,obs,exp)
        print(f'n={n} q={q} symplectic_derivations_T={nd} squarezero_T={ns} total_D={sum(obs.values())} joint={sorted(obs.items())} ranks_T={sorted(typ.items())}')
    for n,q in ((2,3),(3,2),(3,3),(4,2)):
        P=expected(n,q)
        print(f'FORMULA n={n} q={q} total={sum(P.values())} joint_terms={len(P)} values={sorted(P.items())}')
    print('DIRECT_HEISENBERG_SQUARE_ZERO_DERIVATION_AND_KERNEL_FORM_OK')

if __name__=='__main__':main()
