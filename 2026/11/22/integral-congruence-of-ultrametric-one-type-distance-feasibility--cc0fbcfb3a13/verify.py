"""Independent finite checks for ultrametric one-type pair-distance matrices.
Run: python verify.py. Uses only Python standard library.
"""
from itertools import combinations, product
from math import comb

def is_ultra(D):
    n=len(D)
    return all(D[i][k]<=max(D[i][j],D[j][k]) for i,j,k in product(range(n), repeat=3))

def matrices(n,r):
    pairs=list(combinations(range(n),2))
    for vals in product(range(1,r+1),repeat=len(pairs)):
        D=[[0]*n for _ in range(n)]
        for (a,b),d in zip(pairs,vals): D[a][b]=D[b][a]=d
        if is_ultra(D): yield D

def clusters(D,s):
    n=len(D)
    remaining=set(range(n)); out=[]
    while remaining:
        a=min(remaining); C=frozenset(b for b in remaining if D[a][b]<=s)
        remaining-=C; out.append(C)
    return out

def types(D,r):
    n=len(D); out=[]
    for j in range(1,r+1):
        for C in clusters(D,j):
            a=min(C)
            distances=tuple(j if b in C else D[a][b] for b in range(n))
            out.append((j,C,distances))
    return out

def is_ext_vector(D,v):
    n=len(D)
    return all(v[a]<=max(v[b],D[a][b]) and D[a][b]<=max(v[a],v[b]) and v[b]<=max(v[a],D[a][b]) for a,b in combinations(range(n),2))

def brute_types(D,r):
    n=len(D)
    return {v for v in product(range(1,r+1),repeat=n) if is_ext_vector(D,v)}

def feasible(D,v,w,s):
    return all(max(v[a],w[a],s) in (v[a],w[a],s) and sorted((v[a],w[a],s))[-1]==sorted((v[a],w[a],s))[-2] for a in range(len(D)))

def predicted(p,q,s,D):
    j,C,_=p; k,F,_=q
    if p==q:return int(s<=j)
    a=min(C);b=min(F)
    return int(s==max(j,k,D[a][b]))

def rank_mod(M,p):
    B=[[x%p for x in row] for row in M]
    N=len(B); i=0
    for j in range(N):
        row=next((k for k in range(i,N) if B[k][j]),None)
        if row is None:continue
        B[i],B[row]=B[row],B[i]
        inv=pow(B[i][j],-1,p)
        for k in range(i+1,N):
            factor=(B[k][j]*inv)%p
            if factor:
                for l in range(j,N):B[k][l]=(B[k][l]-factor*B[i][l])%p
        i+=1
        if i==N:break
    return i

def certificate_columns(T,D,s):
    """Signed standard-basis columns for a diagonal integer congruence."""
    r=max(t[0] for t in T)
    N=len(T)
    unit=lambda i: tuple(int(k==i) for k in range(N))
    subtract=lambda a,b: tuple(x-y for x,y in zip(a,b))
    idx={(t[0],t[1]):i for i,t in enumerate(T)}
    cols=[]; signs=[]
    for i,t in enumerate(T):
        if t[0]>s: cols.append(unit(i));signs.append(1)
    for U in clusters(D,s):
        root=idx[(s,U)]
        cols.append(unit(root));signs.append(1)
        if s>1:
          for W in clusters(D,s-1):
            if not W.issubset(U):continue
            rep=idx[(s-1,W)]
            cols.append(subtract(unit(rep),unit(root))); signs.append(-1)
            for i,t in enumerate(T):
                if t[0]>=s or i==rep:continue
                if t[1].issubset(W):
                    cols.append(subtract(unit(i),unit(rep))); signs.append(0)
    assert len(cols)==N
    return cols,signs

def bareiss_det(M):
    A=[list(row) for row in M];n=len(A);sign=1;last=1
    for k in range(n-1):
      if A[k][k]==0:
        pivot=next((i for i in range(k+1,n) if A[i][k]),None)
        if pivot is None:return 0
        A[k],A[pivot]=A[pivot],A[k];sign=-sign
      piv=A[k][k]
      for i in range(k+1,n):
        for j in range(k+1,n):
          z=A[i][j]*piv-A[i][k]*A[k][j]
          assert z%last==0
          A[i][j]=z//last
        A[i][k]=0
      last=piv
    return sign*A[-1][-1]

def verify_congruence(M,T,D,s):
    cols,signs=certificate_columns(T,D,s)
    assert abs(bareiss_det([list(c) for c in zip(*cols)]))==1
    for a,u in enumerate(cols):
      Mu=[sum(M[i][j]*u[j] for j in range(len(T))) for i in range(len(T))]
      for b,v in enumerate(cols):
        val=sum(Mu[i]*v[i] for i in range(len(T)))
        assert val==(signs[a] if a==b else 0)
    return signs

def verify_case(D,r,check_ranks=True):
    T=types(D,r); n=len(D); N=len(T)
    assert len({p[2] for p in T})==N
    assert {p[2] for p in T}==brute_types(D,r)
    c={j:len(clusters(D,j)) for j in range(1,r+1)}
    assert sum(c.values())==N
    for s in range(1,r+1):
        M=[[int(feasible(D,p[2],q[2],s)) for q in T] for p in T]
        assert all(M[i][j]==predicted(T[i],T[j],s,D) for i in range(N) for j in range(N))
        if s==1: pos=N; neg=0; zero=0
        else:
            pos=sum(c[j] for j in range(s+1,r+1))+c[s]
            neg=c[s-1]
            zero=sum(c[j] for j in range(1,s-1))
        assert pos+neg+zero==N
        if check_ranks:
            assert all(rank_mod(M,p)==pos+neg for p in (2,3,5))
            assert sorted(verify_congruence(M,T,D,s))==sorted([1]*pos+[-1]*neg+[0]*zero)
    return N*N*r

if __name__=='__main__':
    tests=0; entries=0; cases={}
    for r in (2,3,4):
      for n in (1,2,3,4):
        if n==1:
          mats=[[[0]]]
        else:mats=matrices(n,r)
        count=0
        for D in mats:
          entries+=verify_case(D,r)
          count+=1;tests+=1
        cases[(n,r)]=count
    # independently enumerate the ultrametric classes at five vertices for small levels
    for D in matrices(5,3):
      entries+=verify_case(D,3)
      tests+=1
    print('VERIFICATION_OK', 'bases=',tests,'direct_oriented_type_tests=',entries,'base_counts=',cases)
