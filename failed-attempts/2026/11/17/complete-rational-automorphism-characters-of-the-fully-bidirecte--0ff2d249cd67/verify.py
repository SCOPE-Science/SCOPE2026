#!/usr/bin/env python3
"""Exact, reproducible cellular and equivariant homology calculation.

Needs Python >=3.10 and SymPy >=1.12.  All face, matching, matrix and
character data are derived afresh from the stated six-vertex digraph.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations
from math import factorial
import json
import sympy as S

# Vertex bipartition (0,1,2) and (3,4,5); arcs 0..8 point A to B,
# arcs 9..17 point B to A. Every simplex inherits increasing-arc order.
ARCS=tuple((a,b) for a in range(3) for b in range(3,6))+tuple((b,a) for a in range(3) for b in range(3,6))
assert len(ARCS)==18 and len(set(ARCS))==18
ALL=1<<18

def admissible(bits):
    incoming=[None]*6; outgoing=[None]*6
    for i,(u,v) in enumerate(ARCS):
        if bits & (1<<i):
            if outgoing[u] is not None or incoming[v] is not None:
                return False
            outgoing[u]=v; incoming[v]=u
    for u in range(6):
        seen={u}; v=u
        while outgoing[v] is not None:
            v=outgoing[v]
            if v in seen:return False
            seen.add(v)
    return True

FACES={m for m in range(ALL) if admissible(m)}
VEC=Counter(x.bit_count()-1 for x in FACES)
assert [VEC[i] for i in range(-1,5)]==[1,18,108,264,252,72]
for x in FACES:
    for i in range(18):
        if x & (1<<i):assert x^(1<<i) in FACES

# Independent rank verification over F_2 on complete simplicial chains.
def rank_mod2(cols):
    basis={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in basis:x^=basis[p]
            else:basis[p]=x;break
    return len(basis)
F2_RANKS={}
for d in range(1,5):
    lower=sorted(x for x in FACES if x.bit_count()==d)
    row={x:i for i,x in enumerate(lower)}
    cols=[]
    for x in (x for x in FACES if x.bit_count()==d+1):
        col=0
        for i in range(18):
            if x & (1<<i):col^=1<<row[x^(1<<i)]
        cols.append(col)
    F2_RANKS[d]=rank_mod2(cols)
assert [F2_RANKS[d] for d in range(1,5)]==[17,91,173,60]

# Toggle-first greedy Forman matching, never matching away the empty simplex.
# The complete directed incidence graph is tested below, not just sampled.
remaining=FACES.copy(); pairs=[]
for i in range(18):
    new=[]
    for x in sorted(remaining,key=lambda z:(z.bit_count(),z)):
        if x and not(x & (1<<i)) and (x | (1<<i)) in remaining:
            new.append((x, x | (1<<i)))
    for x,y in new:
        remaining.remove(x);remaining.remove(y)
        pairs.append((x,y))
assert len(pairs)==336
CRIT=Counter(x.bit_count()-1 for x in remaining)
assert {i:CRIT[i] for i in (-1,0,2,3,4)}=={-1:1,0:1,2:5,3:24,4:12}
match={y:x for x,y in pairs}
indeg={x:0 for x in FACES if x}; adj={x:[] for x in FACES if x}
incidences=0
for x in FACES:
    if x.bit_count()<2:continue
    for i in range(18):
        if x&(1<<i):
            y=x^(1<<i)
            if match.get(x)==y:src,dst=y,x
            else:src,dst=x,y
            adj[src].append(dst);indeg[dst]+=1;incidences+=1
q=deque(x for x in indeg if indeg[x]==0); visited=0
while q:
    x=q.popleft();visited+=1
    for y in adj[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert visited==len(FACES)-1

# Augmented oriented cellular boundaries and exact algebraic Morse cancellation.
def boundary(x):
    if not x:return {}
    out={};p=0
    for i in range(18):
        if x&(1<<i):out[x^(1<<i)]=(-1)**p;p+=1
    return out
D={x:boundary(x) for x in FACES}
bydim=defaultdict(set)
for x in FACES:bydim[x.bit_count()-1].add(x)
todo={(x,y) for x,y in pairs}
while todo:
    candidates=[(x,y) for x,y in todo if abs(D[y].get(x,0))==1]
    assert candidates,'No unit pivot for a prescribed acyclic pair'
    low,up=min(candidates,key=lambda z:(z[1].bit_count(),z[1]))
    d=up.bit_count()-1;pivot=D[up][low];col=D[up]
    for other in tuple(bydim[d]):
        if other==up:continue
        alpha=D[other].get(low,0)
        if alpha:
            for row,coef in col.items():
                if row!=low:
                    D[other][row]=D[other].get(row,0)-alpha*coef//pivot
                    if not D[other][row]:del D[other][row]
            del D[other][low]
    for higher in bydim[d+1]:D[higher].pop(up,None)
    bydim[d].remove(up);bydim[d-1].remove(low)
    todo.remove((low,up))

assert len(bydim[2])==5 and len(bydim[3])==24 and len(bydim[4])==12
assert all(not D[x] for x in bydim[2])
assert all(not D[x] for x in bydim[4])
rows=sorted(bydim[2]); cols=sorted(bydim[3]);
B=S.Matrix([[D[x].get(y,0) for x in cols] for y in rows])
assert B.shape==(5,24) and B.rank()==5
UNIT_MINOR=int(B[:,:5].det())
assert abs(UNIT_MINOR)==1
# Check d^2=0 for every remaining chain generator, including augmentation.
for x in FACES:
    if x not in bydim[x.bit_count()-1]:continue
    dd={}
    for y,a in D[x].items():
        assert y in bydim[y.bit_count()-1]
        for z,b in D[y].items():dd[z]=dd.get(z,0)+a*b
    assert all(v==0 for v in dd.values())

# Direct top-dimensional rational cycles in the ORIGINAL chain complex.
# There are no 5-cells; thus H4=ker(boundary_4). An RREF supplies a
# canonical free-column basis, permitting exact group traces.
old4=sorted(x for x in FACES if x.bit_count()==5)
old3=sorted(x for x in FACES if x.bit_count()==4)
old3_idx={x:i for i,x in enumerate(old3)}
A=S.zeros(len(old3),len(old4))
for j,x in enumerate(old4):
    for y,coef in boundary(x).items():A[old3_idx[y],j]=coef
RREF,piv=A.rref()
free=[j for j in range(len(old4)) if j not in piv]
assert len(piv)==60 and len(free)==12
cycles=[]
for j in free:
    col={old4[j]:S.Integer(1)}
    for i,p in enumerate(piv):
        if RREF[i,j]:col[old4[p]]=-RREF[i,j]
    cycles.append(col)
assert all(sum((A[:,old4.index(x)]*a for x,a in cycle.items()),S.zeros(len(old3),1))==S.zeros(len(old3),1) for cycle in cycles)

P=((0,1,2),(1,0,2),(1,2,0))
SIZES=(1,3,2)
CLASSES=[]
for i in range(3):
    for j in range(i,3):
        perm=tuple(P[i])+tuple(3+P[j][k] for k in range(3))
        CLASSES.append((f'({i},{j})',perm,SIZES[i]*SIZES[j]*(2 if i!=j else 1),i,j,False))
for i in range(3):
    perm=tuple(3+k for k in range(3))+tuple(P[i])
    CLASSES.append((f'swap({i})',perm,6*SIZES[i],i,-1,True))
assert sum(c[2] for c in CLASSES)==72
arc_index={a:i for i,a in enumerate(ARCS)}
def act(x,perm):
    t=[arc_index[(perm[a],perm[b])] for i,(a,b) in enumerate(ARCS) if x & (1<<i)]
    inversions=sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
    return sum(1<<i for i in t), (-1)**inversions

# Check actual graph automorphism preservation for all 72 group elements.
grp=set()
for a in permutations(range(3)):
    for b in permutations(range(3)):
        grp.add(tuple(a)+tuple(3+b[i] for i in range(3)))
        grp.add(tuple(3+a[i] for i in range(3))+tuple(b))
assert len(grp)==72
assert all(all((p[a],p[b]) in arc_index for a,b in ARCS) for p in grp)
assert all(act(x,p)[0] in FACES for p in grp for x in FACES)

# Conjugacy classes are determined by the unordered pair of S3 cycle types
# (no part swap), or the S3 cycle type of the product (part swap).
def cycle_class(p):
    seen=set();lens=[]
    for i in range(3):
        if i in seen:continue
        n=0;v=i
        while v not in seen:
            seen.add(v);v=p[v];n+=1
        lens.append(n)
    return {(1,1,1):0,(1,2):1,(3,):2}[tuple(sorted(lens))]
S3class={tuple(p):cycle_class(p) for p in permutations(range(3))}

def signature(p):
    if p[0]<3:
        a=tuple(p[i] for i in range(3));b=tuple(p[i+3]-3 for i in range(3))
        return tuple(sorted((S3class[a],S3class[b])))
    a=tuple(p[i]-3 for i in range(3));b=tuple(p[i+3] for i in range(3))
    return ('s',S3class[tuple(b[a[i]] for i in range(3))])
classes_expected={signature(p) for p in grp}
assert len(classes_expected)==9
sizes_grp=Counter(signature(p) for p in grp)
for _,p,size,i,j,sw in CLASSES:
    sig=('s',i) if sw else tuple(sorted((i,j)))
    assert signature(p)==sig and sizes_grp[sig]==size

CHAR=[]
for name,perm,size,i,j,sw in CLASSES:
    # Extract top-homology character using free coordinates of cycle basis.
    t4=S.Integer(0)
    for f,cyc in zip(free,cycles):
        dst=old4[f]
        t4+=sum(coeff*sign for x,coeff in cyc.items()
                for new,sign in [act(x,perm)] if new==dst)
    # Reduced simplicial Lefschetz number includes the empty-face term -1.
    lef=-1
    for x in FACES:
        if not x:continue
        y,sign=act(x,perm)
        if x==y:lef+=(-1)**(x.bit_count()-1)*sign
    # All reduced homology except H3 and H4 vanishes integrally by Morse.
    t3=t4-lef
    CHAR.append((name,size,int(t3),int(t4),int(lef)))

# Check signed Lefschetz traces for all group elements, not only the nine
# representatives; the class signatures must predict them exactly.
LEF_BY_CLASS={signature(p):lef for (_,p,_,_,_,_),(_,_,_,_,lef) in zip(CLASSES,CHAR)}
for perm in grp:
    total=-1
    for x in FACES:
        if not x:continue
        y,sign=act(x,perm)
        if y==x:total+=(-1)**(x.bit_count()-1)*sign
    assert total==LEF_BY_CLASS[signature(perm)]

# Complete irreducible list for S3 wr S2 = (S3 x S3) rtimes S2.
# T, S, V are trivial, sign and two-dimensional standard S3 characters.
CHAR3={'T':(1,1,1),'S':(1,-1,1),'V':(2,0,-1)}
IRREPS=[]
for a,b in combinations(CHAR3,2):IRREPS.append((a+b,a,b,0))
for a in CHAR3:
    for s in (1,-1):IRREPS.append((a+('+' if s==1 else '-'),a,a,s))
assert len(IRREPS)==9

def irrep_char(row):
    _,a,b,swap_sign=row
    aa,bb=CHAR3[a],CHAR3[b]
    out=[]
    for _,_,_,i,j,sw in CLASSES:
        out.append((swap_sign*aa[i] if swap_sign else 0) if sw else
                   aa[i]*bb[j] + (0 if swap_sign else bb[i]*aa[j]))
    return out
IRCH=[irrep_char(row) for row in IRREPS]
for i,c in enumerate(IRCH):
    for j,d in enumerate(IRCH):
        inner=sum(entry[2]*u*v for entry,u,v in zip(CLASSES,c,d))
        assert inner==(72 if i==j else 0)
MULT={}
for degree in (3,4):
    t=[rec[2 if degree==3 else 3] for rec in CHAR]
    mult={}
    for (name,*_),chi in zip(IRREPS,IRCH):
        prod=sum(entry[2]*x*y for entry,x,y in zip(CLASSES,t,chi))
        assert prod%72==0 and prod>=0
        mult[name]=prod//72
    MULT[degree]={k:v for k,v in mult.items() if v}
assert MULT[3]=={'TV':1,'SV':1,'T+':1,'T-':1,'S-':1,'V+':1,'V-':1}
assert MULT[4]=={'TS':1,'T-':1,'S-':1,'V+':1,'V-':1}
assert sum(v*IRCH[i][0] for i,((name,*_),_) in enumerate(zip(IRREPS,IRCH)) for v in [MULT[3].get(name,0)])==19
assert sum(v*IRCH[i][0] for i,((name,*_),_) in enumerate(zip(IRREPS,IRCH)) for v in [MULT[4].get(name,0)])==12
# The T+ constituent gives exactly one invariant H3 line, none in H4.
assert MULT[3].get('T+',0)==1 and MULT[4].get('T+',0)==0

report={'n_arcs':len(ARCS),'face_vector':[VEC[d] for d in range(5)],
        'nonempty_faces':len(FACES)-1,'incidences':incidences,
        'matching_pairs':len(pairs),'critical_cells':{str(d):CRIT[d] for d in (0,2,3,4)},
        'finite_field_boundary_ranks':F2_RANKS,
        'critical_three_to_two_matrix':B.tolist(),
        'critical_cell_masks':{str(d):sorted(bydim[d]) for d in (0,2,3,4)},
        'unimodular_minor_first_five_columns':UNIT_MINOR,
        'four_to_three_morse_boundary_zero':all(not D[x] for x in bydim[4]),
        'original_top_boundary_rank':len(piv),
        'classes':CHAR,'irreducible_multiplicities_H3':MULT[3],
        'irreducible_multiplicities_H4':MULT[4],
        'full_group_invariants':{'H3':1,'H4':0}}
print('K33_MULTIPATH_EQUIVARIANT_EXACT_PASS')
print(json.dumps(report,sort_keys=True,separators=(',',':'),default=int))
