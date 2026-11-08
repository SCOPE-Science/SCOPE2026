#!/usr/bin/env python3
"""Independent finite-field direct check of idempotent weight -1 RB maps on T2."""
from itertools import product

def mul(x,y,q):
    a,d,b=x; A,D,B=y
    return ((a*A)%q,(d*D)%q,(a*B+b*D)%q)
def add(*xs,q):
    return tuple(sum(x[i] for x in xs)%q for i in range(3))
def negate(x,q):
    return tuple(-a%q for a in x)
def lin(M,x,q):
    return tuple(sum(M[j][i]*x[i] for i in range(3))%q for j in range(3))
def valid(M,q):
    es=((1,0,0),(0,1,0),(0,0,1))
    Rs=[lin(M,e,q) for e in es]
    if any(lin(M,r,q)!=r for r in Rs):return False
    for i,x in enumerate(es):
      for j,y in enumerate(es):
        r=mul(Rs[i],Rs[j],q)
        a=mul(Rs[i],y,q);b=mul(x,Rs[j],q);c=mul(x,y,q)
        t=tuple((a[z]+b[z]-c[z])%q for z in range(3))
        if r!=lin(M,t,q): return False
    return True

def rank(M,q):
    A=[list(col) for col in M]
    r=0
    for j in range(3):
      piv=next((i for i in range(r,3) if A[i][j]%q),None)
      if piv is None:continue
      A[piv],A[r]=A[r],A[piv]
      z=pow(A[r][j],-1,q)
      A[r]=[v*z%q for v in A[r]]
      for i in range(3):
        if i!=r:
          u=A[i][j]
          A[i]=[(A[i][k]-u*A[r][k])%q for k in range(3)]
      r+=1
    return r

def brute(q):
    ct=[0]*4
    for entries in product(range(q),repeat=9):
      M=(entries[:3],entries[3:6],entries[6:])
      if valid(M,q): ct[rank(M,q)]+=1
    expected=[1,2*q*q+3*q+2,2*q*q+3*q+2,1]
    assert ct==expected,(q,ct,expected)
    print(f'q={q}: ranks={ct}, total={sum(ct)}; PASS')

if __name__=='__main__':
    for q in (2,3):brute(q)
    print('ALL_IDEMPOTENT_TRIANGULAR_RB_TESTS_PASS')

def orbit_check(q):
    from collections import Counter
    def matmult(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%q for j in range(3)) for i in range(3))
    def inverse_phi(lam,t):
        il=pow(lam,-1,q)
        return ((1,0,0),(0,1,0),((-t*il)%q,(t*il)%q,il))
    def phi(lam,t): return ((1,0,0),(0,1,0),(t%q,(-t)%q,lam%q))
    maps=set()
    for ent in product(range(q),repeat=9):
        M=(ent[:3],ent[3:6],ent[6:])
        if valid(M,q):maps.add(M)
    group=[(phi(lam,t),inverse_phi(lam,t)) for lam in range(1,q) for t in range(q)]
    assert len(group)==q*(q-1)
    unexplored=set(maps); size_by_rank=[Counter() for _ in range(4)]
    while unexplored:
        M=next(iter(unexplored))
        orb={matmult(matmult(g,M),gi) for g,gi in group}
        assert orb<=unexplored or all(x in maps for x in orb)
        unexplored-=orb
        size_by_rank[rank(M,q)][len(orb)]+=1
    expected=Counter({1:2, q:5, q*(q-1):2})
    # Sizes collide when q=2; Counter tally must add collisions.
    expected=Counter()
    expected[1]+=2;expected[q]+=5;expected[q*(q-1)]+=2
    for j in (1,2):assert size_by_rank[j]==expected,(q,j,size_by_rank[j],expected)
    assert size_by_rank[0]==Counter({1:1}) and size_by_rank[3]==Counter({1:1})
    print(f'q={q}: automorphism orbit distributions by rank={size_by_rank}; PASS')

if __name__=='__main__':
    for q in (2,3):orbit_check(q)
    print('ALL_AUTOMORPHISM_ORBIT_TESTS_PASS')
