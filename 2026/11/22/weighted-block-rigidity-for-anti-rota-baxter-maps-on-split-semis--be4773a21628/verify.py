#!/usr/bin/env python3
"""Finite-field replay for the anti-Rota-Baxter coordinate-product classification.
Run: python3 verify.py. Only Python's standard library is needed.
Checks original polynomial identities, independent normal forms, ranks, and square-zero/strong subfamilies.
"""
from itertools import product
from math import comb, factorial

class Field:
    def __init__(self,q):
        self.q=q
        if q == 9:
            self.add=lambda a,b: ((a%3+b%3)%3)+3*((a//3+b//3)%3)
            self.mul=lambda a,b: (((a%3)*(b%3)+2*(a//3)*(b//3))%3)+3*(((a%3)*(b//3)+(a//3)*(b%3))%3)
        else:
            self.add=lambda a,b:(a+b)%q
            self.mul=lambda a,b:(a*b)%q
    def sum(self,*xs):
        o=0
        for x in xs:o=self.add(o,x)
        return o

def is_anti(R,n,F):
    # identity on all pairs of primitive coordinate idempotents
    for i in range(n):
      for s in range(n):
        for t in range(n):
          v=F.sum(F.mul(R[i*n+s],R[i*n+t]),
                  F.mul(R[i*n+t],R[t*n+s]),
                  F.mul(R[i*n+s],R[s*n+t]))
          if v: return False
    return True

def is_block_normal(R,n,F):
    # Purely combinatorial reconstruction, without evaluating the identity
    if F.q not in (3,9):return all(x==0 for x in R)
    active=[s for s in range(n) if R[s*n+s]]
    for s in range(n):
      if s not in active and any(R[i*n+s] for i in range(n)):return False
      if s in active and any(R[i*n+s] not in (0,R[s*n+s]) for i in range(n)):return False
    for s in active:
      S={i for i in range(n) if R[i*n+s]}
      for t in active:
        T={i for i in range(n) if R[i*n+t]}
        if S != T and S & T:return False
    return True

def rank(R,n,F):
    a=[list(R[i*n:(i+1)*n]) for i in range(n)]
    row=0
    for j in range(n):
        pivot=next((i for i in range(row,n) if a[i][j]),None)
        if pivot is None:continue
        a[row],a[pivot]=a[pivot],a[row]
        for i in range(row+1,n):
            if not a[i][j]:continue
            p=a[i][j]
            d=a[row][j]
            # Eliminate via d * row_i - p * row_pivot, without inversion.
            for k in range(j,n):
                u=F.mul(d,a[i][k]);v=F.mul(p,a[row][k]);
                # additive inverse through field enumeration
                neg=next(h for h in range(F.q) if F.sum(h,v)==0)
                a[i][k]=F.sum(u,neg)
        row+=1
        if row==n:break
    return row

def is_strong(R,n,F):
    # T(e_s)T(e_t)e_u=e_sT(e_t)T(e_u) in all basis triples
    for s in range(n):
      for t in range(n):
        for u in range(n):
          lhs=F.mul(R[u*n+s],R[u*n+t]); rhs=F.mul(R[s*n+t],R[s*n+u])
          if u==s:
              if lhs!=rhs:return False
          elif lhs or rhs:return False
    return True

def is_squarezero(R,n,F):
    for i in range(n):
      for j in range(n):
        z=F.sum(*(F.mul(R[i*n+k],R[k*n+j]) for k in range(n)))
        if z:return False
    return True

def S2(n,r):
    if r==0:return int(n==0)
    return sum((-1)**(r-j)*comb(r,j)*j**n for j in range(r+1))//factorial(r)

def expected(n,q):
    if q not in (3,9):return [1]+[0]*n
    ans=[1]
    for r in range(1,n+1):
        z=sum(comb(n,a)*S2(a,r)*(r+1)**(n-a)*(q-1)**a for a in range(r,n+1))
        alt=sum((-1)**(r-j)*comb(r,j)*(r+1+j*(q-1))**n for j in range(r+1))//factorial(r)
        assert z==alt,(n,q,r,z,alt)
        ans.append(z)
    return ans

def expected_squarezero(n,q):
    if q not in (3,9):return 1
    # N_c: nonzero weights on c active positions summing to zero.
    N=[0]+[((q-1)**c+(q-1)*((-1)**c))//q for c in range(1,n+1)]
    B=[0]+[sum(comb(m,c)*N[c] for c in range(1,m+1)) for m in range(1,n+1)]
    dp=[[0]*(n+1) for _ in range(n+1)]
    dp[0][0]=1
    for r in range(1,n+1):
        for j in range(r,n+1):
            dp[r][j]=sum(comb(j,m)*B[m]*dp[r-1][j-m] for m in range(1,j+1))//r
    return sum(comb(n,j)*dp[r][j] for r in range(n+1) for j in range(n+1))

def run_case(q,n):
    F=Field(q); actual=[0]*(n+1); block=0; sq=0; strong=0
    for R in product(range(q),repeat=n*n):
        is_a=is_anti(R,n,F); is_b=is_block_normal(R,n,F)
        assert is_a==is_b,(q,n,R,is_a,is_b)
        if is_a:
            actual[rank(R,n,F)]+=1
            iss=is_strong(R,n,F)
            assert iss==(all(R[i*n+j]==0 for i in range(n) for j in range(n) if i!=j)),(q,n,R)
            strong+=iss
            sq+=is_squarezero(R,n,F)
            block+=1
    assert actual==expected(n,q),(q,n,actual,expected(n,q))
    assert block==sum(actual)
    assert strong==(q**n if q in (3,9) else 1),(q,n,strong)
    assert sq==expected_squarezero(n,q),(q,n,sq,expected_squarezero(n,q))
    print(f'FIELD={q} N={n} RANK={actual} TOTAL={block} STRONG={strong} SQUARE_ZERO={sq}')

if __name__=='__main__':
    for q,n in [(2,2),(3,1),(3,2),(3,3),(5,2),(9,2)]:run_case(q,n)
    print('VERIFY_ANTI_RB_COORDINATE_PARTITIONS_OK')
