"""Exact finite corroboration of fixed digraph complexes and homology characters.
No external dependencies. All homology computations are over the field with two elements.
"""
from itertools import combinations, permutations
from math import factorial, gcd
from collections import defaultdict


def orbits_of_arcs(perms):
    n=len(perms[0]); arcs={(u,v) for u in range(n) for v in range(n) if u!=v}; orbits=[]
    while arcs:
        e=next(iter(arcs)); o={e}; q=[e]
        for x in q:
            for p in perms:
                y=(p[x[0]],p[x[1]])
                if y not in o:o.add(y);q.append(y)
        assert o <= arcs
        orbits.append(tuple(sorted(o)));arcs.difference_update(o)
    return sorted(orbits)


def is_strong(n, arcs):
    rows=[1<<i for i in range(n)]
    for u,v in arcs:rows[u]|=1<<v
    for k in range(n):
        for i in range(n):
            if rows[i] & (1<<k):rows[i]|=rows[k]
    return all(r==(1<<n)-1 for r in rows)


def fixed_faces(n,perms):
    oo=orbits_of_arcs(perms); assert len(oo)<25
    faces=set()
    for mask in range(1<<len(oo)):
        arcs=[x for j,o in enumerate(oo) if mask>>j&1 for x in o]
        if not is_strong(n,arcs):faces.add(mask)
    assert 0 in faces
    assert all(mask & ~(1<<j) in faces for mask in faces for j in range(len(oo)) if mask>>j&1)
    return oo,faces


def mod2_betti(faces,m):
    bydim=defaultdict(list)
    for f in faces:
        if f:bydim[f.bit_count()-1].append(f)
    if not bydim:return []
    ranks={}
    for d in sorted(bydim):
        if d==0:ranks[d]=0;continue
        cod={x:i for i,x in enumerate(bydim[d-1])}
        basis={}
        for f in bydim[d]:
            v=0
            for j in range(m):
                if f>>j&1:v^=1<<cod[f^(1<<j)]
            while v:
                pivot=v.bit_length()-1
                if pivot in basis:v^=basis[pivot]
                else:basis[pivot]=v;break
        ranks[d]=len(basis)
    return [len(bydim.get(d,[]))-ranks.get(d,0)-ranks.get(d+1,0)-(d==0) for d in range(max(bydim)+1)]


def ct(n,p):
    seen=set();res=[]
    for i in range(n):
        if i in seen:continue
        x=i;l=0
        while x not in seen:seen.add(x);x=p[x];l+=1
        res.append(l)
    return tuple(sorted(res,reverse=True))


def mobius(n):
    k=0;m=n;p=2
    while p*p<=m:
        if m%p==0:
            m//=p;k+=1
            if m%p==0:return 0
        else:p+=1
    if m>1:k+=1
    return (-1)**k


def lie_char(parts):
    if len(set(parts))>1:return 0
    d=parts[0];k=len(parts)
    return mobius(d)*d**(k-1)*factorial(k-1)


def char_trace(n,p):
    oo,faces=fixed_faces(n,[p]);s=sum((-1)**(mask.bit_count()) for mask in faces)
    return -s,len(oo)

for n in (2,3,4,5):
    reps={}
    for p in permutations(range(n)):
        reps.setdefault(ct(n,p),p)
    for parts,p in sorted(reps.items()):
        value,orb=char_trace(n,p)
        assert value==lie_char(parts),(n,parts,value,lie_char(parts))
    print('S%d_character_PASS classes=%d'%(n,len(reps)),flush=True)
# Large enough to detect an erroneous global sign twist, except identity: its rank is classical.
n=6;reps={}
for p in permutations(range(n)):reps.setdefault(ct(n,p),p)
for parts,p in sorted(reps.items()):
    if parts==(1,)*n:continue
    value,orb=char_trace(n,p)
    assert value==lie_char(parts),(n,parts,value,lie_char(parts))
print('S6_nonidentity_character_PASS classes=10',flush=True)

# Cyclic regular action: arc orbit is specified by nonzero cyclic difference.
for n in range(2,13):
    p=tuple((i+1)%n for i in range(n))
    oo,faces=fixed_faces(n,[p]);assert len(oo)==n-1
    by_orbit=[next(iter(o))[1]-next(iter(o))[0] for o in oo]
    by_orbit=[d%n for d in by_orbit]
    for mask in range(1<<(n-1)):
        selected=[by_orbit[j] for j in range(n-1) if mask>>j&1]
        expect=(gcd(n,*selected)>1 if selected else True)
        assert (mask in faces)==expect,(n,mask)
    if n<=10:
        betti=mod2_betti(faces,n-1)
        # Proper divisor lattice of n, empty for prime, sphere when squarefree composite,
        # otherwise contractible.
        proper=[d for d in range(2,n) if n%d==0]
        if not proper:expected=[]
        elif mobius(n)==0:expected=[0]*len(betti)
        else:
            w=len(set(d for d in range(2,n+1) if n%d==0 and mobius(d)==-1)) # not used
            m=n;omega=0;v=2
            while v*v<=m:
                if m%v==0:
                    omega+=1
                    while m%v==0:m//=v
                v+=1
            if m>1:omega+=1
            expected=[int(i==omega-2) for i in range(len(betti))]
        assert betti==expected,(n,betti,expected)
    print('C%d_fixed_PASS orbit_vertices=%d faces=%d'%(n,len(oo),len(faces)),flush=True)

# Regular group examples, with Cayley arcs indexed by nonidentity elements.
# S3 regular action on its six elements.
G=list(permutations(range(3))); ix={g:i for i,g in enumerate(G)}
mult=lambda a,b:tuple(a[b[k]] for k in range(3))
left=[tuple(ix[mult(a,b)] for b in G) for a in G]
_,f=fixed_faces(6,left)
assert mod2_betti(f,5)==[3,0] and len(f)==7 # edge + three isolated vertices
print('S3_regular_fixed_PASS components=4',flush=True)
# Elementary abelian group F2^r.
for r in (2,3):
    n=1<<r
    left=[tuple(a^b for b in range(n)) for a in range(n)]
    oo,f=fixed_faces(n,left)
    bh=mod2_betti(f,n-1)
    expect=p=2**(r*(r-1)//2)
    assert bh[:r-1]==([0]*(r-2)+[expect]) and all(v==0 for v in bh[r-1:]),(r,bh,expect)
    print('F2^%d_regular_fixed_PASS betti=%s'%(r,bh),flush=True)
print('DIRECTED_NONSTRONG_EQUIVARIANT_CHECKS_PASS')
