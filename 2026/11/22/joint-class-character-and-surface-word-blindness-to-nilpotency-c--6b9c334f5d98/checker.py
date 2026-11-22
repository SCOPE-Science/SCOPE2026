"""Finite computations supporting semidirect-product group spectra; no external dependencies."""
from collections import Counter,deque
from math import prod

def action_matrix(p,partition):
    n=sum(partition)
    N=[[0]*n for _ in range(n)]
    x=0
    for l in partition:
        for i in range(l-1): N[x+i][x+i+1]=1
        x+=l
    return N

def mul(A,B,p):
    n=len(A);return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]

def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def matpow(A,k,p):
    ans=ident(len(A))
    for _ in range(k):ans=mul(ans,A,p)
    return ans

def rank(M,p):
    A=[x[:] for x in M];m=len(A);n=len(A[0]);r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if A[i][j]%p),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        a=pow(A[r][j],-1,p)
        A[r]=[x*a%p for x in A[r]]
        for i in range(m):
            if i!=r:
                a=A[i][j];A[i]=[(A[i][k]-a*A[r][k])%p for k in range(n)]
        r+=1
    return r

def check(p,parts,enumerate_classes=True):
    n=sum(parts);b=len(parts)
    N=action_matrix(p,parts)
    I=ident(n);T=[[(I[i][j]+N[i][j])%p for j in range(n)] for i in range(n)]
    assert matpow(T,p,p)==I
    assert matpow(N,max(parts),p)==[[0]*n for _ in range(n)]
    assert (max(parts)==1 or rank(matpow(N,max(parts)-1,p),p)>0)
    assert rank(N,p)==n-b
    assert all(rank([[(matpow(T,j,p)[i][k]-I[i][k])%p for k in range(n)] for i in range(n)],p)==n-b for j in range(1,p))
    assert matpow(N,p-1,p)==[[0]*n for _ in range(n)]
    # Check commutator image and uniformity on each nontrivial coset pair via linear image rank
    for j in range(p):
      for k in range(p):
        Tj=matpow(T,j,p); Tk=matpow(T,k,p)
        C=[[(I[i][c]-Tk[i][c])%p for c in range(n)]+[(Tj[i][c]-I[i][c])%p for c in range(n)] for i in range(n)]
        assert rank(C,p)==(0 if j==k==0 else n-b)
    hist_theory=Counter({1:p**b,p:(p**n-p**b)//p,p**(n-b):(p-1)*p**b})
    if enumerate_classes:
        m=p**n; seen=set();hist=Counter()
        def unpack(x):
            v=[]
            for _ in range(n):v.append(x%p);x//=p
            return v
        def pack(v):return sum(v[i]*p**i for i in range(n))
        vectors=[unpack(a) for a in range(m)]
        Tv=[pack([sum(T[i][h]*v[h] for h in range(n))%p for i in range(n)]) for v in vectors]
        Mpows=[]
        for j in range(p):
            U=matpow(T,j,p)
            M=[[(I[i][h]-U[i][h])%p for h in range(n)] for i in range(n)]
            Mpows.append([tuple(M[i][h] for i in range(n)) for h in range(n)])
        for z in range(p*m):
            if z in seen: continue
            x=z//p;y=z%p
            orbit={z}; stack=[z]
            while stack:
                w=stack.pop();vnum=w//p;j=w%p;v=vectors[vnum]
                # conjugate by cyclic generator
                a=Tv[vnum]*p+j
                if a not in orbit:orbit.add(a);stack.append(a)
                # conjugate by each vector basis generator
                for h in range(n):
                    new=tuple((v[i]+Mpows[j][h][i])%p for i in range(n))
                    a=pack(new)*p+j
                    if a not in orbit:orbit.add(a);stack.append(a)
            seen.update(orbit);hist[len(orbit)]+=1
        assert sum(s*c for s,c in hist.items())==p**(n+1)
        assert hist==hist_theory,(hist,hist_theory)
    return {'p':p,'partition':parts,'group_order':p**(n+1),'nilpotency_class':max(parts),'exponent':p,'derived_order':p**(n-b),'class_counts':dict(sorted(hist_theory.items())),'character_degree_counts':{1:p**(b+1),p:(p**n-p**b)//p},'enumerated_conjugacy_classes':enumerate_classes}
if __name__=='__main__':
    for p,parts in [(5,(3,1)),(5,(2,2)),(5,(4,3,1,1,1)),(5,(2,2,2,2,2)),(7,(3,1)),(7,(2,2)),(7,(6,3,1,1,1,1,1)),(7,(2,)*7)]:
        print(check(p,parts,enumerate_classes=(sum(parts)<=4)))
    print('ALL CHECKS PASS')
