#!/usr/bin/env python3
"""Independent direct multiplication check for truncated multi-axis ideal products."""
from itertools import combinations,product
from collections import Counter

def all_rref(N,d,q):
    for piv in combinations(range(N),d):
        free=[(i,j) for i in range(d) for j in range(piv[i]+1,N) if j not in piv]
        for values in product(range(q),repeat=len(free)):
            rows=[[0]*N for _ in range(d)]
            for i,p in enumerate(piv):rows[i][p]=1
            for (i,j),v in zip(free,values):rows[i][j]=v
            yield rows

def rank(vs,q):
    if not vs:return 0
    N=len(vs[0]); M=[v[:] for v in vs if any(v)]; p=0
    for j in range(N):
        i=next((i for i in range(p,len(M)) if M[i][j]%q),None)
        if i is None:continue
        M[p],M[i]=M[i],M[p]
        mul=pow(M[p][j],-1,q);M[p]=[(mul*v)%q for v in M[p]]
        for i in range(len(M)):
            if i!=p and M[i][j]:
                c=M[i][j];M[i]=[(x-c*y)%q for x,y in zip(M[i],M[p])]
        p+=1
        if p==len(M):break
    return p

def equal_span(A,B,q):
    d=rank(A,q);return d==rank(B,q)==rank(A+B,q)

def coords_for(ns):return [(i,a) for i,n in enumerate(ns) for a in range(1,n)]
def vecmul(v,w,ns,coords,index,q):
    out=[0]*len(coords)
    for j,(i,a) in enumerate(coords):
        if not v[j]:continue
        for k,(i2,b) in enumerate(coords):
            if i==i2 and w[k] and a+b<ns[i]:
                out[index[(i,a+b)]]=(out[index[(i,a+b)]]+v[j]*w[k])%q
    return out

def ideals(ns,q):
    coords=coords_for(ns);N=len(coords);index={e:j for j,e in enumerate(coords)}
    out=[]
    for d in range(N+1):
        for rows in all_rref(N,d,q):
            if all(rank(rows+[vecmul(v,[int(c==(i,1)) for c in coords],ns,coords,index,q)],q)==d
                for v in rows for i in range(len(ns))):
                out.append(rows)
    return out

def model_product(I,J,ns,q,coords,index):
    a=[];b=[]
    for arm,n in enumerate(ns):
        a.append(next((deg for i,deg in coords if i==arm and any(row[index[(arm,deg)]] for row in I)),n))
        b.append(next((deg for i,deg in coords if i==arm and any(row[index[(arm,deg)]] for row in J)),n))
    c=[min(n,a0+b0) for n,a0,b0 in zip(ns,a,b)]
    out=[]
    for arm,n in enumerate(ns):
        for deg in range(c[arm]+1,n):
            v=[0]*len(coords);v[index[(arm,deg)]]=1;out.append(v)
    for u in I:
        for v in J:
            lead=[0]*len(coords)
            for arm,n in enumerate(ns):
                if c[arm]<n:
                    lead[index[(arm,c[arm])]]=u[index[(arm,a[arm])]]*v[index[(arm,b[arm])]]%q
            if any(lead):out.append(lead)
    return out,c

for ns,q in [((2,2,2),2),((3,3,3),2),((2,2,2,2),2),((3,2,2),3),((4,3),3)]:
    cs=coords_for(ns);ix={v:i for i,v in enumerate(cs)}
    ins=ideals(ns,q); count=0;zero=0
    for I in ins:
        for J in ins:
            raw=[vecmul(u,v,ns,cs,ix,q) for u in I for v in J]
            pred,c=model_product(I,J,ns,q,cs,ix)
            assert equal_span(raw,pred,q),(ns,q,I,J,raw,pred)
            actualzero=rank(raw,q)==0
            assert actualzero==all(c0==n for c0,n in zip(c,ns))
            count+=1;zero+=actualzero
    print('field=%s arms=%s proper_ideals=%d checked_ordered_products=%d zero_products=%d PASS'%(q,ns,len(ins),count,zero))
print('IDEAL_PRODUCTS_SCHUR_DIRECT_PASS')
