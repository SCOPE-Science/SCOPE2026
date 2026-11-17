#!/usr/bin/env python3
"""Independent direct enumeration of rational points on the bitangent union.

Only standard Python. No incidence or normalisation formulas are imported.
"""
from itertools import product

def count_mod_prime(p):
    D=next(i for i in range(2,p) if pow(i,(p-1)//2,p)==p-1)
    def add(x,y):return((x[0]+y[0])%p,(x[1]+y[1])%p)
    def mul(x,y):return((x[0]*y[0]+D*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def power(x,n):
        out=(1,0)
        while n:
            if n&1:out=mul(out,x)
            x=mul(x,x);n//=2
        return out
    zeta=next((i,j) for i in range(p) for j in range(p) if power((i,j),4)==(p-1,0) and power((i,j),8)==(1,0))
    zpow=[power(zeta,k) for k in range(8)]
    def minus(x,y):return ((x[0]-y[0])%p,(x[1]-y[1])%p)
    L=[]
    for i,j in ((0,1),(0,2),(1,2)):
        for k in (1,3,5,7):
            v=[(0,0)]*3
            v[i]=(1,0)
            v[j]=minus((0,0),zpow[k])
            L.append(v)
    for a,b in product((0,2,4,6),repeat=2):
        L.append([minus((0,0),zpow[a]),minus((0,0),zpow[b]),(1,0)])
    assert len(L)==28
    points=[(x,y,1) for x in range(p) for y in range(p)] + [(1,y,0) for y in range(p)] + [(0,1,0)]
    def hit(line,pt):
        t=(0,0)
        for a,x in zip(line,pt): t=add(t,mul(a,(x,0)))
        return t==(0,0)
    return sum(any(hit(Li,pt) for Li in L) for pt in points)

for p in (3,5,7,11,13,17,19,23,29,31,37,41,43):
    if p==3:want=4*p+1
    elif p==5:want=16*p-49
    elif p==17:want=28*p-257
    elif p%8==1:want=28*p-305
    elif p%8==5:want=16*p-65
    else:want=4*p+1
    got=count_mod_prime(p)
    assert got==want,(p,got,want)
print('VERIFY_DYCK_DIRECT_OK 13_PRIME_FIELDS')

# Independent direct full-plane checks over F9, F25, and F49.
def count_extension2(p):
    D=next(i for i in range(2,p) if pow(i,(p-1)//2,p)==p-1)
    def add(x,y):return((x[0]+y[0])%p,(x[1]+y[1])%p)
    def mul(x,y):return((x[0]*y[0]+D*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def power(x,n):
        r=(1,0)
        while n:
            if n&1:r=mul(r,x)
            x=mul(x,x);n//=2
        return r
    zeta=next((a,b) for a in range(p) for b in range(p) if power((a,b),4)==(p-1,0) and power((a,b),8)==(1,0))
    zs=[power(zeta,i) for i in range(8)]
    def minus(x,y):return ((x[0]-y[0])%p,(x[1]-y[1])%p)
    L=[]
    for i,j in ((0,1),(0,2),(1,2)):
        for k in (1,3,5,7):
            v=[(0,0)]*3;v[i]=(1,0);v[j]=minus((0,0),zs[k]);L.append(v)
    for a,b in product((0,2,4,6),repeat=2):L.append([minus((0,0),zs[a]),minus((0,0),zs[b]),(1,0)])
    F=list(product(range(p),repeat=2))
    points=[(x,y,(1,0)) for x in F for y in F] + [((1,0),y,(0,0)) for y in F] + [((0,0),(1,0),(0,0))]
    def hit(line,P):
        t=(0,0)
        for c,u in zip(line,P):t=add(t,mul(c,u))
        return t==(0,0)
    return sum(any(hit(ell,P) for ell in L) for P in points)

for p,want in ((3,91),(5,411),(7,1067)):
    got=count_extension2(p)
    assert got==want,(p,got,want)
print('VERIFY_DYCK_DIRECT_EXTENSION_OK F9_F25_F49')
