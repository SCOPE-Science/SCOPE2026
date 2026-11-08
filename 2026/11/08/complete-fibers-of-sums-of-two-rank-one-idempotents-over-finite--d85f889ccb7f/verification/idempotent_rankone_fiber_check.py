"""Independent direct finite-field checks of rank-one idempotent sum fibers.
Usage: python idempotent_rankone_fiber_check.py
"""
import itertools
from collections import Counter

def rank_and_columns(A,n,p):
    cols=[tuple(A[i*n+j] for i in range(n)) for j in range(n)]
    selected=[]
    for c in cols:
        if linear_rank(selected+[c],p)>len(selected): selected.append(c)
    return len(selected),selected

def linear_rank(vectors,p):
    if not vectors:return 0
    mat=[list(r) for r in vectors]; rows=len(mat); cols=len(mat[0]); piv=0
    for j in range(cols):
        nz=next((i for i in range(piv,rows) if mat[i][j]%p),None)
        if nz is None: continue
        mat[nz],mat[piv]=mat[piv],mat[nz]
        inv=pow(mat[piv][j],-1,p)
        mat[piv]=[(a*inv)%p for a in mat[piv]]
        for i in range(rows):
            if i!=piv and mat[i][j]%p:
                fac=mat[i][j]
                mat[i]=[(a-fac*b)%p for a,b in zip(mat[i],mat[piv])]
        piv+=1
        if piv==rows:break
    return piv

def induced(A,n,p,basis):
    # unique coordinates of C on its image, determined by checking all p^r vectors
    r=len(basis)
    table={tuple(sum(x*b[i] for x,b in zip(c,basis))%p for i in range(n)): c
           for c in itertools.product(range(p),repeat=r)}
    arr=[]
    for j in range(r):
        v=basis[j];w=tuple(sum(A[i*n+k]*v[k] for k in range(n))%p for i in range(n))
        arr.append(table[w])
    return [[arr[j][i] for j in range(r)] for i in range(r)]

def predicted(A,n,p):
    tr=sum(A[i*n+i] for i in range(n))%p
    rk,bas=rank_and_columns(A,n,p)
    if rk>2 or tr!=2%p:return 0
    if rk==0:
        return (p**(n-1)*(p**n-1)//(p-1)) if p==2 else 0
    if rk==1:
        return 2*p**(n-1)-(0 if p==2 else 1)
    M=induced(A,n,p,bas)
    e=one=0
    for v in itertools.product(range(p),repeat=2):
        if not any(v) or next(x for x in v if x)!=1:continue
        w=[sum(M[i][k]*v[k] for k in range(2))%p for i in range(2)]
        if (v[0]*w[1]-v[1]*w[0])%p==0:
            e+=1
            if w==list(v):one+=1
    if M[0][1]==M[1][0]==0 and M[0][0]==M[1][1]:
        return p*(p+1) if M[0][0]==1%p else 0
    return p+1-e+p*one

def projectors(n,p):
    for u in itertools.product(range(p),repeat=n):
        if not any(u) or next(x for x in u if x)!=1:continue
        for v in itertools.product(range(p),repeat=n):
            if sum(a*b for a,b in zip(u,v))%p==1:
                yield tuple(u[i]*v[j]%p for i in range(n) for j in range(n))

def check(n,p):
    P=list(projectors(n,p))
    obs=Counter(tuple((a+b)%p for a,b in zip(x,y)) for x in P for y in P)
    counts=Counter()
    for A in itertools.product(range(p),repeat=n*n):
        pred=predicted(A,n,p)
        actual=obs.get(A,0)
        if pred!=actual:
            raise AssertionError(f'failure n={n},p={p},A={A}, predicted {pred}, observed {actual}')
        if actual:counts[actual]+=1
    assert sum(v*k for k,v in counts.items())==len(P)**2
    print(f'PASS n={n} q={p}: {len(P)} rank-one idempotents, {len(P)**2} ordered pairs, {p**(n*n)} targets checked, nonzero fiber distribution {dict(sorted(counts.items()))}')

if __name__=='__main__':
    for n,p in [(2,2),(2,3),(2,5),(2,7),(3,2),(3,3),(4,2)]: check(n,p)
    print('RANK_ONE_IDEMPOTENT_SUM_ALL_CHECKS_PASS')
