#!/usr/bin/env python3
"""Exact all-characteristic incidence certificate for a Fermat quartic's 28 bitangents.

Uses only the Python standard library. The ring of integers Z[t]/(t^4+1) and
field extensions F_{p^2} are implemented directly, with exact arithmetic.
"""
from collections import Counter
from itertools import combinations, permutations, product

ZERO=(0,0,0,0)
ONE=(1,0,0,0)

def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def minus(a,b): return plus(a,neg(b))
def times(a,b):
    out=[0]*4
    for i in range(4):
        for j in range(4):
            if i+j <4: out[i+j]+=a[i]*b[j]
            else: out[i+j-4]-=a[i]*b[j]
    return tuple(out)
def zpower(k):
    k=k%8
    out=[0]*4
    out[k%4]=(-1 if k>=4 else 1)
    return tuple(out)
def cross(a,b):
    return (minus(times(a[1],b[2]),times(a[2],b[1])),
            minus(times(a[2],b[0]),times(a[0],b[2])),
            minus(times(a[0],b[1]),times(a[1],b[0])))
def dot(a,b): return plus(plus(times(a[0],b[0]),times(a[1],b[1])),times(a[2],b[2]))

labels=[]
lines=[]
for i,j in ((0,1),(0,2),(1,2)):
    for k in (1,3,5,7):
        v=[ZERO]*3
        v[i]=ONE
        v[j]=neg(zpower(k))
        labels.append(('H',i,j,k))
        lines.append(tuple(v))
for a,b in product((0,2,4,6),repeat=2):
    labels.append(('B',a,b))
    lines.append((neg(zpower(a)),neg(zpower(b)),ONE))
assert len(set(labels))==len(lines)==28

intersections={}
for i,j in combinations(range(28),2):
    point=cross(lines[i],lines[j]);assert any(point)
    support=frozenset(k for k,ln in enumerate(lines) if dot(ln,point)==ZERO)
    assert len(support)>=2
    intersections[support]=point
assert Counter(map(len,intersections))==Counter({2:288,4:15})
assert sum(len(s)*(len(s)-1)//2 for s in intersections)==378

# Norm from multiplication by an element of Z[t]/(t^4+1).
PERMS=tuple(permutations(range(4)))
def norm(x):
    cols=[times(x,zpower(j)) for j in range(4)]
    val=0
    for p in PERMS:
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        prod=1
        for i in range(4):prod*=cols[p[i]][i]
        val+=(-1 if inv%2 else 1)*prod
    return val

norms=set()
exception_counts=Counter()
for i,j,k in combinations(range(28),3):
    v=dot(lines[k],cross(lines[i],lines[j]))
    if v==ZERO:continue
    nn=abs(norm(v));assert nn>0
    norms.add(nn)
    for p in (2,3,5,17):
        if nn%p==0: exception_counts[p]+=1
    trial=nn
    for p in (2,3,5,17):
        while trial%p==0: trial//=p
    assert trial==1,(i,j,k,nn)
assert norms=={1,2,4,8,9,16,17,32,36,64,256,400}
assert exception_counts==Counter({2:2448,3:384,5:32,17:192})

# Generic reduction: no new collinearity away from 2,3,5,17.
def image_label(idx,q):
    name=labels[idx]
    if name[0]=='H':
        _,i,j,k=name
        return labels.index(('H',i,j,k*q%8))
    _,a,b=name
    return labels.index(('B',a*q%8,b*q%8))

generic_fixed={}
for q in (1,3,5,7):
    perm=[image_label(i,q) for i in range(28)]
    fixed_lines=sum(i==perm[i] for i in range(28))
    point_types=Counter()
    for I in intersections:
        if frozenset(perm[i] for i in I)==I:
            rational_branches=sum(i==perm[i] for i in I)
            point_types[(len(I),rational_branches)]+=1
    generic_fixed[q]=(fixed_lines,point_types)
assert generic_fixed[1]==(28,Counter({(2,2):288,(4,4):15}))
assert generic_fixed[3]==(4,Counter({(4,2):6,(4,0):3}))
assert generic_fixed[5]==(16,Counter({(2,2):48,(4,4):12,(4,0):3}))
assert generic_fixed[7]==(4,Counter({(4,2):6,(4,0):3}))

# Exceptional arithmetic over F_{p^2} (which contains all eighth roots).
def special(p):
    D=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    zero=(0,0);one=(1,0)
    def a(n):return(n%p,0)
    def add(x,y):return((x[0]+y[0])%p,(x[1]+y[1])%p)
    def sub(x,y):return((x[0]-y[0])%p,(x[1]-y[1])%p)
    def mul(x,y):return((x[0]*y[0]+D*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def power(x,n):
        ans=one
        while n:
            if n&1:ans=mul(ans,x)
            x=mul(x,x);n//=2
        return ans
    zeta=next((i,j) for i in range(p) for j in range(p)
              if power((i,j),4)==a(-1) and power((i,j),8)==one)
    def eval4(v):
        ans=zero
        for n in reversed(v):ans=add(mul(ans,zeta),a(n))
        return ans
    ll=[tuple(eval4(v) for v in L) for L in lines]
    def normalize(x):
        v=next(t for t in x if t!=zero)
        iv=power(v,p*p-2)
        return tuple(mul(t,iv) for t in x)
    def cross2(x,y):
        return (sub(mul(x[1],y[2]),mul(x[2],y[1])),
                sub(mul(x[2],y[0]),mul(x[0],y[2])),
                sub(mul(x[0],y[1]),mul(x[1],y[0])))
    pts={}
    for i,j in combinations(range(28),2):
        P=normalize(cross2(ll[i],ll[j]))
        pts.setdefault(P,set()).update((i,j))
    for pt,I in pts.items():
        J={k for k,L in enumerate(ll) if add(add(mul(pt[0],L[0]),mul(pt[1],L[1])),mul(pt[2],L[2]))==zero}
        assert I==J
    def frac(x,n):return normalize(tuple(power(t,p**n) for t in x))
    res={}
    for n in (1,2):
        fixedlines={i for i,L in enumerate(ll) if frac(L,n)==normalize(L)}
        point_types=Counter()
        for pt,I in pts.items():
            if frac(pt,n)==pt:
                point_types[(len(I),len(I & fixedlines))]+=1
        res[n]=(len(fixedlines),point_types)
    return Counter(map(len,pts.values())),res

s3,r3=special(3)
s5,r5=special(5)
s17,r17=special(17)
assert s3==Counter({4:63})
assert s5==Counter({2:240,3:16,4:15})
assert s17==Counter({2:144,3:48,4:15})
assert r3[1]==(4,Counter({(4,0):3,(4,2):6}))
assert r3[2]==(28,Counter({(4,4):63}))
assert r5[1]==(16,Counter({(3,3):16,(4,0):3,(4,4):12}))
assert r5[2]==(28,Counter({(2,2):240,(3,3):16,(4,4):15}))
for n in (1,2):assert r17[n]==(28,Counter({(2,2):144,(3,3):48,(4,4):15}))

def count(q,points):
    L,types=points
    return L*(q+1)-sum((r-1)*v for (m,r),v in types.items())
for residue in (1,3,5,7):
    L=generic_fixed[residue]
    Q={1:41,3:11,5:13,7:7}[residue]
    expected={1:28*Q-305,3:4*Q+1,5:16*Q-65,7:4*Q+1}[residue]
    assert count(Q,L)==expected
for p,r in ((3,r3),(5,r5),(17,r17)):
    for n in (1,2):
        Q=p**n
        expected={3: (4*Q+1 if n%2 else 28*Q-161),
                  5: (16*Q-49 if n%2 else 28*Q-289),
                  17:28*Q-257}[p]
        assert count(Q,r[n])==expected
print('VERIFY_DYCK_INCIDENCE_OK 28_LINES 3276_TRIPLES 3_5_17_EXCEPTIONAL')
print('GENERIC',dict(sorted(generic_fixed.items())))
