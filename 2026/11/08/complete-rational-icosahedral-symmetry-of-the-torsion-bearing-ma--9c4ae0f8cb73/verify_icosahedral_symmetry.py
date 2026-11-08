#!/usr/bin/env python3
"""Exact rational icosahedral matching-homology character certificate.
Uses Python 3 standard library; all graph, group, faces, ranks, and signed traces
are reconstructed. No external datasets or other files required.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
from math import lcm

# Explicit icosahedral graph: two staggered pentagons and two apices.
ED=[]
for i in range(5):
    u,v=1+i,6+i
    ED.extend(((0,u),(11,v),(u,1+(i+1)%5),(v,6+(i+1)%5),
               (u,v),(u,6+(i-1)%5)))
ED=sorted(tuple(sorted(e)) for e in ED)
assert len(ED)==len(set(ED))==30
N=[set() for _ in range(12)]
for a,b in ED:N[a].add(b);N[b].add(a)
assert all(len(v)==5 for v in N)
TRI=[t for t in combinations(range(12),3) if all(b in N[a] for a,b in combinations(t,2))]
assert len(TRI)==20
assert all(sum(set(e).issubset(t) for t in TRI)==2 for e in ED)
assert all(len({x for x in N[v] if x in N[u]})==2 for u,v in ED)

# Every automorphism is uniquely determined by its image of the oriented
# triangle (0,1,2): propagate across every adjacent pair of triangular faces.
def propagate(target):
    m={0:target[0],1:target[1],2:target[2]}
    q=deque([(0,1,2)]);seen=set()
    while q:
        tri=q.popleft();key=frozenset(tri)
        if key in seen:continue
        seen.add(key)
        for a,b,c in ((tri[0],tri[1],tri[2]),
                      (tri[1],tri[2],tri[0]),(tri[2],tri[0],tri[1])):
            d=next(x for x in N[a]&N[b] if x!=c)
            opts=N[m[a]]&N[m[b]]
            target_d=next(x for x in opts if x!=m[c])
            if d in m:assert m[d]==target_d
            else:m[d]=target_d
            q.append((b,a,d))
    assert len(m)==12 and len(set(m.values()))==12
    p=tuple(m[i] for i in range(12))
    assert all(p[b] in N[p[a]] for a,b in ED)
    return p
AUT=set(propagate(t) for tri in TRI for t in permutations(tri))
assert len(AUT)==120
identity=tuple(range(12))

def compose(p,q):return tuple(p[q[i]] for i in range(12))

def order(p):
    z=1;seen=set()
    for i in range(12):
        if i in seen:continue
        v=i;k=0
        while v not in seen:seen.add(v);v=p[v];k+=1
        z=lcm(z,k)
    return z

# Canonical global sphere orientation; adjacent oriented faces induce
# opposite orientations along their shared edge.
orient={(0,1,2),(1,2,0),(2,0,1)}
q=deque([(0,1,2)]);seen=set()
while q:
    tri=q.popleft();key=frozenset(tri)
    if key in seen:continue
    seen.add(key)
    for a,b,c in ((tri[0],tri[1],tri[2]),
                  (tri[1],tri[2],tri[0]),(tri[2],tri[0],tri[1])):
        d=next(x for x in N[a]&N[b] if x!=c)
        new=(b,a,d)
        if frozenset(new) not in seen:q.append(new)
        for x in (new,(new[1],new[2],new[0]),(new[2],new[0],new[1])):
            orient.add(x)
assert len(seen)==20 and len(orient)==60
# Verify adjacent triangles are consistently oppositely oriented.
for a,b in ED:
    x,y=tuple(N[a]&N[b]);assert ((a,b,x) in orient)!=((a,b,y) in orient)

def orientation(p):return 1 if (p[0],p[1],p[2]) in orient else -1
assert Counter(orientation(p) for p in AUT)=={1:60,-1:60}
ROT={p for p in AUT if orientation(p)==1}
assert identity in ROT
assert all(compose(a,b) in ROT for a in ROT for b in ROT)

CENT=[p for p in AUT if all(compose(p,g)==compose(g,p) for g in AUT)]
assert len(CENT)==2
z=next(p for p in CENT if p!=identity)
assert orientation(z)==-1 and order(z)==2
assert all(i!=z[i] and z[i] not in N[i] and not (N[i]&N[z[i]]) for i in range(12))

# Full matching complex on graph edges. Over Q, mod-two rank lower bounds
# together with chain-complex inequalities force equality of all rational ranks.
edge_ix={e:i for i,e in enumerate(ED)}
mask=[(1<<u)|(1<<v) for u,v in ED]
LEVEL=[[(i,) for i in range(30)]]
for k in range(2,7):
    LEVEL.append([f+(j,) for f in LEVEL[-1] for j in range(f[-1]+1,30)
                  if all(mask[j]&mask[t]==0 for t in f)])
fvector=list(map(len,LEVEL))
assert fvector==[30,315,1400,2535,1482,125]

def rank_f2(cols,lower):
    ix={f:i for i,f in enumerate(lower)};basis={}
    for f in cols:
        bits=0
        for i in range(len(f)):bits ^= 1<<ix[f[:i]+f[i+1:]]
        while bits:
            pivot=bits.bit_length()-1
            if pivot not in basis:basis[pivot]=bits;break
            bits ^= basis[pivot]
    return len(basis)
mod2=[rank_f2(LEVEL[i],LEVEL[i-1]) for i in range(1,6)]
assert mod2==[29,286,1114,1357,125]
# Chain inequalities: r1<=29; rk+r(k+1)<=f_{k-1}; r5<=f5.
# For 1..5 the mod-two lower ranks sum to 2911, and the bounds
# r1+r2<=315, r2+r3<=1400, r4+r5<=1482, plus r1<=29 force
# rational ranks exactly their mod-two values (r3+r4<2535 gives H3).
assert 30-1-mod2[0]==0
assert 315-mod2[0]-mod2[1]==0
assert 1400-mod2[1]-mod2[2]==0
assert 2535-mod2[2]-mod2[3]==64
assert 1482-mod2[3]-mod2[4]==0
assert 125-mod2[4]==0

# Exact Lefschetz character via signed fixed simplices, including -1 in
# reduced degree -1. Concentration in degree 3 means chi_H3=1-chi_chain.
def sign_sort(images):
    return -1 if sum(images[i]>images[j] for i in range(len(images))
                     for j in range(i+1,len(images)))%2 else 1

def character(p):
    ep=tuple(edge_ix[tuple(sorted((p[u],p[v])))] for u,v in ED)
    assert len(set(ep))==30
    total=1
    for d,level in enumerate(LEVEL):
        tr=0
        for f in level:
            im=tuple(ep[i] for i in f)
            if sorted(im)==list(f):tr+=sign_sort(im)
        total-=(-1)**d*tr
    return total

char={p:character(p) for p in AUT}
assert char[identity]==64 and char[z]==16
# Finer order-five A5 classes have the same rational character.
counts=Counter((orientation(p),order(p),char[p]) for p in AUT)
assert counts=={(1,1,64):1,(1,2,0):15,(1,3,-2):20,(1,5,-1):24,
                (-1,2,16):1,(-1,2,0):15,(-1,6,-2):20,(-1,10,1):24}
# Central eigenspace character across rotations. Character of A5 rational
# irreducibles for classes (1,2,3,5a,5b):
# 1: (1,1,1,1,1); 4: (4,0,1,-1,-1)
# 5: (5,1,-1,0,0); 6: (6,-2,0,1,1)
# The 6-character is 3+3' over C; its ordinary self-inner-product is 2.
size={1:1,2:15,3:20,5:24}
plus={};minus={}
for g in ROT:
    h=compose(z,g)
    assert h in AUT
    plus[g]=(char[g]+char[h])//2
    minus[g]=(char[g]-char[h])//2
    assert (char[g]+char[h])%2==0
assert sum(plus.values())==sum(minus.values())==0 # no rotation invariants
assert Counter((order(g),plus[g],minus[g]) for g in ROT)=={
 (1,40,24):1,(2,0,0):15,(3,-2,0):20,(5,0,-1):24}
# multiplicities computed using ordinary complex-character inner product;
# two conjugate degree-three constituents must have equal multiplicities.
char4={1:4,2:0,3:1,5:-1};char5={1:5,2:1,3:-1,5:0}
char6={1:6,2:-2,3:0,5:1}
mult=[]
for vals in [plus,minus]:
    m4=sum(vals[g]*char4[order(g)] for g in ROT)//60
    m5=sum(vals[g]*char5[order(g)] for g in ROT)//60
    m6=sum(vals[g]*char6[order(g)] for g in ROT)//120
    mult.append((m4,m5,m6))
assert mult==[(2,4,2),(2,2,1)]
# Signed action is a chain map for every graph automorphism: every
# codimension-one deletion is transported with the expected sign.
for p in AUT:
    ep=tuple(edge_ix[tuple(sorted((p[u],p[v])))] for u,v in ED)
    for level in LEVEL[1:]:
        for f in level:
            im=[ep[x] for x in f]
            sorted_im=sorted(im)
            s=sign_sort(im)
            for i,x in enumerate(f):
                rem=im[:i]+im[i+1:]
                # coefficient of g(d_i f) equals coefficient in d(g f).
                j=sorted_im.index(ep[x])
                assert ((-1)**i)*sign_sort(rem)==s*((-1)**j)
print('ICOSAHEDRAL_MATCHING_SYMMETRY_PASS')
print('f_vector='+str(fvector)+'; ranks_mod_2='+str(mod2))
print('group_automorphisms=120; rotations=60; antipodal_involution=1')
print('character_class_counts='+str(sorted(counts.items())))
print('central_even_multiplicities_V4_V5_V6='+str(mult[0]))
print('central_odd_multiplicities_V4_V5_V6='+str(mult[1]))
print('fixed_dimensions_under_A5=0; under_center=40; under_full_group=0')
print('all_signed_boundary_equivariance_checks_pass')
