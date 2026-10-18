#!/usr/bin/env python3
from itertools import combinations, product

def inv(a,p): return pow(a,p-2,p)

def rref(rows,p,n=4):
    a=[list(map(lambda x:x%p,r)) for r in rows if any(x%p for x in r)]
    r=0
    for c in range(n):
        piv=next((i for i in range(r,len(a)) if a[i][c]%p),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        z=inv(a[r][c]%p,p); a[r]=[(z*x)%p for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]%p:
                z=a[i][c]%p; a[i]=[(x-z*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a): break
    a=[tuple(row) for row in a if any(row)]
    a.sort(key=lambda row: next(i for i,x in enumerate(row) if x))
    return tuple(a)

def rank(rows,p): return len(rref(rows,p))
def contains(B,v,p): return rank(list(B)+[v],p)==len(B)

def subspaces(p,n=4):
    yield tuple()
    for k in range(1,n+1):
        for piv in combinations(range(n),k):
            slots=[(i,j) for i,pc in enumerate(piv) for j in range(pc+1,n) if j not in piv]
            for vals in product(range(p), repeat=len(slots)):
                M=[[0]*n for _ in range(k)]
                for i,pc in enumerate(piv): M[i][pc]=1
                for (i,j),v in zip(slots,vals): M[i][j]=v
                yield tuple(tuple(row) for row in M)

def act(A,v,p):
    a,b,c,d=A
    x1,x2,y1,y2=v
    return ((a*x1+b*x2)%p,(c*x1+d*x2)%p,(a*y1+b*y2)%p,(c*y1+d*y2)%p)

def check(p):
    gens=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    invs=[]
    total=0
    for B in subspaces(p):
        total+=1
        ok=True
        for v in B:
            for A in gens:
                if not contains(B,act(A,v,p),p): ok=False; break
            if not ok: break
        if ok: invs.append(B)
    proper=[B for B in invs if 0<len(B)<4]
    assert len(invs)==p+3, (p,len(invs))
    assert len(proper)==p+1 and all(len(B)==2 for B in proper)
    for i,B in enumerate(proper):
        for C in proper[i+1:]:
            assert rank(list(B)+list(C),p)==4
            # dim intersection = 2+2-rank(sum)=0
    print(f'p={p}: vector subspaces={total}, invariant={len(invs)}, proper_nonzero={len(proper)}=|P^1(F_{p})|; all proper have dim 2 and distinct pairs are complementary')
for p in (2,3,5): check(p)
print('VERIFY_OK')
