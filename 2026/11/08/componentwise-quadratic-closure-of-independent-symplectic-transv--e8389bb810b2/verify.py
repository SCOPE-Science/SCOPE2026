"""Independent finite-field checks of symplectic transvection Lie-algebra dimensions.
Run: python3 verify.py. No third-party dependencies.
"""
from itertools import product, combinations
from random import Random

def row_rank(vectors, p):
    piv = {}
    for v in vectors:
        w = [int(x) % p for x in v]
        while True:
            k = next((j for j, a in enumerate(w) if a), None)
            if k is None: break
            if k in piv:
                v0 = piv[k]; a=w[k]
                w = [(x-a*y)%p for x,y in zip(w,v0)]
            else:
                inv=pow(w[k],-1,p)
                piv[k]=[(a*inv)%p for a in w]
                break
    return len(piv)

def components(J, indices):
    left=set(indices); groups=[]
    while left:
        root=min(left); left.remove(root); todo=[root]; comp={root}
        while todo:
            u=todo.pop()
            for v in sorted(left):
                if J[u][v]:
                    left.remove(v); comp.add(v);todo.append(v)
        groups.append(comp)
    return groups

def generated_dimension(J, inds, p):
    n=len(J); d=n*n
    piv={}; basis=[]
    def add(A):
        w=A[:]
        while True:
            k=next((i for i,x in enumerate(w) if x),None)
            if k is None:return
            if k in piv:
                x=w[k]; B=piv[k]
                w=[(a-x*b)%p for a,b in zip(w,B)]
            else:
                inv=pow(w[k],-1,p)
                w=[(a*inv)%p for a in w];piv[k]=w;basis.append(w)
                return
    for i in inds:
        X=[0]*d
        for j in range(n): X[i*n+j]=J[i][j]
        add(X)
    k=0
    while k<len(basis):
        X=basis[k]
        for Y in basis[:]:
            Z=[]
            for i in range(n):
                for j in range(n):
                    a=sum(X[i*n+t]*Y[t*n+j]-Y[i*n+t]*X[t*n+j] for t in range(n))
                    Z.append(a%p)
            add(Z)
        k+=1
    return len(basis)

def alternating_matrix(n, cells, p):
    A=[[0]*n for _ in range(n)]
    for (i,j),x in zip(combinations(range(n),2),cells):
        A[i][j]=x%p; A[j][i]=-x%p
    return A

counts={'exhaustive_F3_4d':0,'sample_F5_4d':0,'larger_cases':0,'subset_checks':0,'dimension_checks':0}
for p,n,limit in [(3,4,None),(5,4,450)]:
    for index,cells in enumerate(product(range(p),repeat=n*(n-1)//2)):
        if limit is not None and index>=limit:break
        J=alternating_matrix(n,cells,p)
        if row_rank(J,p)!=n:continue
        counts['exhaustive_F3_4d' if p==3 else 'sample_F5_4d']+=1
        for k in range(1,n+1):
            I=list(range(k)); comp=components(J,I)
            expected=sum(len(c)*(len(c)+1)//2 for c in comp)
            got=generated_dimension(J,I,p)
            assert got==expected,(p,n,I,cells,expected,got)
            counts['dimension_checks']+=1;counts['subset_checks']+=1

for p,n in [(3,6),(5,6),(7,6),(3,8)]:
    got=0
    for seed in range(60):
        rng=Random(4000+100*p+10*n+seed)
        J=alternating_matrix(n,[rng.randrange(p) for _ in range(n*(n-1)//2)],p)
        if row_rank(J,p)!=n:continue
        got+=1
        for k in sorted(set([1,2,3,n-1,n])):
            I=list(range(k)); comp=components(J,I)
            expected=sum(len(c)*(len(c)+1)//2 for c in comp)
            assert generated_dimension(J,I,p)==expected,(p,n,k,seed)
            counts['dimension_checks']+=1;counts['subset_checks']+=1
    counts['larger_cases']+=got

for p in (3,5,7):
    for n in (2,4,6,8):
        J=[[0]*n for _ in range(n)]
        for i in range(n-1):J[i][i+1]=1;J[i+1][i]=-1%p
        assert row_rank(J,p)==n
        assert generated_dimension(J,list(range(n)),p)==n*(n+1)//2
        counts['dimension_checks']+=1

print('VERIFY_OK '+ ' '.join(f'{k}={v}' for k,v in counts.items()))
