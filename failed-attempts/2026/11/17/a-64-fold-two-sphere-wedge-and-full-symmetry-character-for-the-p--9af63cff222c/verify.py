#!/usr/bin/env python3
"""Exact, self-contained finite certificate for the Paley-25 flag complex.

Run: python3 verify.py
Requires Python >=3.9, standard library only.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

Q=25
ID=tuple(range(Q))

def mul(x,y):
    a,b=divmod(x,5); c,d=divmod(y,5)
    return 5*((a*c+2*b*d)%5)+(a*d+b*c)%5

def add(x,y):
    a,b=divmod(x,5); c,d=divmod(y,5)
    return 5*((a+c)%5)+(b+d)%5

def sub(x,y):
    a,b=divmod(x,5); c,d=divmod(y,5)
    return 5*((a-c)%5)+(b-d)%5

def frob(x):
    a,b=divmod(x,5)
    return 5*a+(-b%5)

SQUARES={mul(x,x) for x in range(1,Q)}
assert len(SQUARES)==12 and 0 not in SQUARES
N=[{j for j in range(Q) if j!=i and sub(j,i) in SQUARES}
   for i in range(Q)]
assert all(len(z)==12 for z in N)
assert all((i in N[j]) == (j in N[i]) for i in range(Q) for j in range(Q))

# Independent construction via recursive intersections, rather than a library.
LEVELS=[[(i,) for i in range(Q)]]
while True:
    upper=[]
    for face in LEVELS[-1]:
        available=set(range(face[-1]+1,Q))
        for i in face:
            available.intersection_update(N[i])
        upper.extend(face+(k,) for k in sorted(available))
    if not upper: break
    LEVELS.append(upper)
assert [len(level) for level in LEVELS]==[25,150,250,75,15]
ALL=set().union(*(set(level) for level in LEVELS))
assert len(ALL)==515

# Deterministic sequential matching, with complete directed-Hasse DAG test.
remaining=set(ALL)
matched=set()
for pivot in range(Q):
    for lower in sorted(remaining):
        if lower not in remaining or pivot in lower:continue
        upper=tuple(sorted(lower+(pivot,)))
        if upper in remaining:
            remaining.remove(lower);remaining.remove(upper)
            matched.add((lower,upper))
critical=Counter(len(f)-1 for f in remaining)
assert critical==Counter({0:1,2:64}),critical
assert len(matched)==225

# All Hasse arrows: reversed on paired edges and downward otherwise.
indeg={s:0 for s in ALL}
out={s:[] for s in ALL}
for upper in ALL:
    if len(upper)==1:continue
    for j in range(len(upper)):
        lower=upper[:j]+upper[j+1:]
        src,dst=(lower,upper) if (lower,upper) in matched else (upper,lower)
        out[src].append(dst);indeg[dst]+=1
queue=deque([s for s in ALL if indeg[s]==0]);visited=0
while queue:
    s=queue.popleft();visited+=1
    for dst in out[s]:
        indeg[dst]-=1
        if indeg[dst]==0:queue.append(dst)
assert visited==515, ('directed Hasse graph not acyclic',visited)

# Independent mod-p boundary elimination; augmented d0 has rank 1.
def rank_mod_p(degree,p):
    if degree==0:return 1
    smaller={cell:j for j,cell in enumerate(LEVELS[degree-1])}
    piv={}
    for cell in LEVELS[degree]:
        vec={smaller[cell[:j]+cell[j+1:]]:(-1 if j%2 else 1)%p
             for j in range(len(cell))}
        while vec:
            lead=max(vec)
            if lead not in piv:
                v=vec[lead]
                piv[lead]={k:(val*pow(v,-1,p))%p for k,val in vec.items()}
                break
            factor=vec[lead]
            for k,val in piv[lead].items():
                u=(vec.get(k,0)-factor*val)%p
                if u:vec[k]=u
                else:vec.pop(k,None)
    return len(piv)
for p in (2,3,101):
    ranks=[rank_mod_p(d,p) for d in range(len(LEVELS))]+[0]
    betti=[len(LEVELS[d])-ranks[d]-ranks[d+1] for d in range(len(LEVELS))]
    assert ranks==[1,24,126,60,15,0],(p,ranks)
    assert betti==[0,0,64,0,0],(p,betti)

# Affine semilinear action; its elements are pairwise distinct.
SQ=sorted(SQUARES)
def perm(c,t,e):
    return tuple(add(t,mul(c, x if not e else frob(x))) for x in range(Q))
GROUP=[(c,t,e,perm(c,t,e)) for c in SQ for t in range(Q) for e in range(2)]
assert len(GROUP)==600 and len({g[3] for g in GROUP})==600
for c,t,e,g in GROUP:
    assert all(((j in N[i])==(g[j] in N[g[i]]))
               for i in range(Q) for j in range(i+1,Q))

# Signed, degree-alternating fixed-simplex trace; subtraction of empty face.
def trace_by_faces(g):
    z=-1
    for level in LEVELS:
        for face in level:
            permuted=[g[i] for i in face]
            if set(permuted)!=set(face):continue
            inversions=sum(permuted[i]>permuted[j]
                for i in range(len(permuted)) for j in range(i+1,len(permuted)))
            z+=(-1)**(len(face)-1+inversions)
    return z

# Independent calculation: invariant cliques are unions of eligible cycles;
# their signs collapse to (-1)^(number_of_cycles-1).
def trace_by_orbits(g):
    seen=set(); cycles=[]
    for i in range(Q):
        if i in seen:continue
        orbit=[];j=i
        while j not in seen:
            orbit.append(j);seen.add(j);j=g[j]
        if all(b in N[a] for a,b in combinations(orbit,2)):
            cycles.append(orbit)
    total=-1
    for size in range(1,len(cycles)+1):
        for chosen in combinations(cycles,size):
            union=[v for orb in chosen for v in orb]
            if all(b in N[a] for a,b in combinations(union,2)):
                total+=(-1)**(size-1)
    return total

CHAR={}
for c,t,e,g in GROUP:
    a=trace_by_faces(g)
    b=trace_by_orbits(g)
    assert a==b,(c,t,e,a,b)
    CHAR[(c,t,e)]=a
assert Counter(CHAR.values())==Counter({0:450,-1:72,4:62,-16:15,64:1})
assert sum(CHAR.values())==0
assert sum(CHAR[(5,t,0)] for t in range(Q))==100
assert sum(CHAR[(c,0,e)] for c in SQ for e in (0,1))==24

# The geometric F_5-line directions: exactly three directions, 5 lines each.
line_sets={}
for i in range(Q):
    for s in SQ:
        line=frozenset(add(i,mul(s,5*j)) for j in range(5))
        assert len(line)==5
        line_sets[line]=1
assert len(line_sets)==15
assert {frozenset(face) for face in LEVELS[4]}==set(line_sets)

# Translation character Fourier transform: support partitions into 12+12.
# The formula is exact because additive characters are fifth roots of unity.
# For nonzero frequency u, its multiplicity is 2 when u is a square and 3 otherwise;
# here the additive pairing is the absolute field trace.
# Derive using the q=25 quadratic Gauss sums, or verify coefficients in Z[zeta5].
def trace_abs(x):
    return add(x,frob(x))//5 # F_5 coefficient (Frob-conjugate sum lies in F_5)
# Exponents 0..4 represent group-ring coefficients of powers of zeta_5.
def exp_coeff(u):
    row=[0]*5
    for t in range(Q):
        exponent=trace_abs(mul(u,t))%5
        row[exponent]+=CHAR[(5,t,0)]
    # zeta^4= -1-zeta-zeta^2-zeta^3, so coefficient is (row[k]-row[4])/25
    nums=[row[k]-row[4] for k in range(4)]
    assert all(v%25==0 for v in nums),(u,row,nums)
    assert nums[1:]==[0,0,0],(u,row,nums)
    return nums[0]//25
mult={u:exp_coeff(u) for u in range(Q)}
assert mult[0]==4
assert all(mult[u]==(2 if u in SQUARES else 3) for u in range(1,Q))
assert Counter(mult.values())==Counter({3:12,2:12,4:1})
assert sum(mult.values())==64

# Class table supports a full character (not merely the trace distribution).
PERMS=[g[3] for g in GROUP]
PERM_INDEX={g:i for i,g in enumerate(PERMS)}
def compose(p,q):return tuple(p[q[i]] for i in range(Q))
INV=[]
for p in PERMS:
    q=[0]*Q
    for i,j in enumerate(p):q[j]=i
    INV.append(tuple(q))
classes=[];done=set()
for i,g in enumerate(PERMS):
    if i in done:continue
    cl=sorted({PERM_INDEX[compose(compose(h,g),INV[k])]
               for k,h in enumerate(PERMS)})
    assert all(CHAR[GROUP[j][:3]]==CHAR[GROUP[i][:3]] for j in cl)
    done.update(cl)
    rep=GROUP[cl[0]][:3]
    classes.append((rep,len(cl),CHAR[rep]))
assert len(done)==600 and len(classes)==16
assert sum(sz for _,sz,_ in classes)==600

print('faces: (25,150,250,75,15); 515 nonempty simplices')
print('Morse: 225 pairs, 1 critical vertex, 64 critical 2-simplices; DAG vertices 515')
print('ranks mod 2,3,101: (1,24,126,60,15)')
print('group: 600 semilinear affine permutations; conjugacy classes: 16')
print('character histogram:', sorted(Counter(CHAR.values()).items()))
print('translation Fourier multiplicities: 1x4, 12x3, 12x2')
print('invariant dimensions: translation 4, semilinear complement 1, full group 0')
print('class table (c,t,e), size, trace:')
for rep,size,tr in classes:
    print('%s | %d | %d'%(str(rep),size,tr))
print('PALEY25_FLAG_WEDGE_AND_FULL_SYMMETRY_PASS')
