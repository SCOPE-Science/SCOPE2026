#!/usr/bin/env python3
"""Reproducible exact finite arithmetic for the three-point K_{3,4} cubical model.

Requires Python 3 standard library only.  No data files are read.
The rational rank argument additionally uses the elementary cycle-lifting proof
spelled out in RESULT.md; modular ranks alone do not prove rational equality.
"""
import itertools
from collections import Counter

A, B = 3, 4
ORIGINAL_VERTICES = A + B
VERTICES = ORIGINAL_VERTICES + A*B
EDGES=[]
for a in range(A):
    for b in range(B):
        midpoint=ORIGINAL_VERTICES+a*B+b
        EDGES.extend([tuple(sorted((a,midpoint))),tuple(sorted((A+b,midpoint)))])
EDGE_INDEX={e:i for i,e in enumerate(EDGES)}
ALL_CELLS = [(0, v, 1<<v) for v in range(VERTICES)] + [
    (1,e,(1<<u)|(1<<v)) for e,(u,v) in enumerate(EDGES)]
CUBES=[[] for _ in range(4)]
for c in itertools.combinations(range(len(ALL_CELLS)),3):
    footprints=[ALL_CELLS[x][2] for x in c]
    if footprints[0]&footprints[1] or footprints[0]&footprints[2] or footprints[1]&footprints[2]:
        continue
    dimension=sum(ALL_CELLS[x][0] for x in c)
    CUBES[dimension].append(c)
INDEX=[{c:i for i,c in enumerate(L)} for L in CUBES]
DIMENSIONS=tuple(map(len,CUBES))
assert DIMENSIONS==(969,3264,3510,1192)

def boundary(cube):
    out={}
    es=[x for x in cube if x>=VERTICES]
    for i,e in enumerate(es):
        u,v=EDGES[e-VERTICES]
        for end,coefficient in ((u,-1),(v,1)):
            face=tuple(sorted((set(cube)-{e})|{end}))
            out[face]=out.get(face,0)+(-1)**i*coefficient
    return {r:z for r,z in out.items() if z}

def rank_mod(d,p):
    pivots={}
    for cell in CUBES[d]:
        col={INDEX[d-1][r]:z%p for r,z in boundary(cell).items()}
        while col:
            top=min(col)
            if top not in pivots:
                inv=pow(col[top],-1,p)
                pivots[top]={r:(z*inv)%p for r,z in col.items()}
                break
            factor=col[top]
            for r,z in pivots[top].items():
                zz=(col.get(r,0)-factor*z)%p
                if zz:col[r]=zz
                else:col.pop(r,None)
    return len(pivots)

def cycle_type(perm):
    seen=set();cycles=[]
    for x in range(len(perm)):
        if x not in seen:
            k=x;size=0
            while k not in seen:
                seen.add(k);size+=1;k=perm[k]
            cycles.append(size)
    return tuple(sorted(cycles,reverse=True))

def inversion_sign(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def induced_action(pa,pb):
    vperm=tuple(pa)+tuple(A+b for b in pb)+tuple(ORIGINAL_VERTICES+pa[a]*B+pb[b] for a in range(A) for b in range(B))
    eperm=[EDGE_INDEX[tuple(sorted((vperm[u],vperm[v])))] for u,v in EDGES]
    return vperm,eperm

def move_cube(cube,vperm,eperm):
    moved=tuple(sorted(vperm[x] if x<VERTICES else VERTICES+eperm[x-VERTICES] for x in cube))
    moved_edges=[eperm[x-VERTICES] for x in cube if x>=VERTICES]
    sign=inversion_sign(moved_edges)
    for x in cube:
        if x>=VERTICES:
            u,v=EDGES[x-VERTICES]
            a,b=EDGES[eperm[x-VERTICES]]
            assert (vperm[u],vperm[v]) in {(a,b),(b,a)}
            if (vperm[u],vperm[v])==(b,a):sign=-sign
    return moved,sign

# Check both compositions vanish INTEGRALLY (without modular reduction).
for d in (2,3):
    for c in CUBES[d]:
        result={}
        for face,coef in boundary(c).items():
            for subface,c2 in boundary(face).items():
                result[subface]=result.get(subface,0)+coef*c2
        assert all(z==0 for z in result.values())
print('EXACT_CHAIN_SQUARES_ZERO',DIMENSIONS[2]+DIMENSIONS[3])
for prime in (2,3,5,1000000007):
    ranks=tuple(rank_mod(d,prime) for d in (1,2,3))
    assert ranks==((968,2289,1192) if prime==2 else (968,2290,1192))
    print('MODULAR_RANKS',prime,*ranks)
print('RATIONAL_RANKS_FROM_LOWER_AND_UPPER_BOUNDS',968,2290,1192)
print('RATIONAL_BETTIS',1,6,28,0)

# Independently verify cubical functoriality on a representative of every
# cycle-type pair.  Class functions are computed on ALL 144 group elements.
classes_checked=set()
CHARACTERS={}
CHARTABLE={}
ALL_TRACES=[]
for pa in itertools.permutations(range(A)):
    for pb in itertools.permutations(range(B)):
        typ=(cycle_type(pa),cycle_type(pb))
        vperm,eperm=induced_action(pa,pb)
        if typ not in classes_checked:
            for d in (1,2,3):
                for c in CUBES[d]:
                    im,sg=move_cube(c,vperm,eperm)
                    lhs={face:sg*coef for face,coef in boundary(im).items()}
                    rhs={}
                    for face,coef in boundary(c).items():
                        imface,face_sg=move_cube(face,vperm,eperm)
                        rhs[imface]=rhs.get(imface,0)+coef*face_sg
                    assert lhs==rhs
            classes_checked.add(typ)
        chain_trace=[]
        for d,L in enumerate(CUBES):
            total=0
            for c in L:
                moved,sg=move_cube(c,vperm,eperm)
                if moved==c:total+=sg
            chain_trace.append(total)
        lefschetz=sum((-1)**d*t for d,t in enumerate(chain_trace))
        fix_a=sum(pa[a]==a for a in range(A))
        fix_b=sum(pb[b]==b for b in range(B))
        trace_h1=(fix_a-1)*(fix_b-1)
        trace_h2=lefschetz-1+trace_h1
        val=(trace_h1,trace_h2)
        if typ in CHARTABLE:assert CHARTABLE[typ]==val
        CHARTABLE[typ]=val
        CHARACTERS[typ]=CHARACTERS.get(typ,0)+1
        ALL_TRACES.append((typ,val))
assert len(ALL_TRACES)==144 and len(CHARTABLE)==15 and len(classes_checked)==15
print('EXACT_EQUIVARIANCE_CLASSES',len(classes_checked))
print('CHARACTER_CLASSES',len(CHARTABLE),'GROUP_ORDER',len(ALL_TRACES))
for t in sorted(CHARTABLE):
    print('CHARACTER',str(t[0]),str(t[1]),'size',CHARACTERS[t],'H1_H2',*CHARTABLE[t])
assert CHARTABLE[((1,1,1),(1,1,1,1))]==(6,28)
assert sum(v[0] for _,v in ALL_TRACES)==0 and sum(v[1] for _,v in ALL_TRACES)==0
print('GLOBAL_FIXED_DIMENSIONS',0,0)

# Irreducible tables in the specified ordered cycle-type classes.
T3=((1,1,1),(2,1),(3,))
T4=((1,1,1,1),(2,1,1),(2,2),(3,1),(4,))
S3={'trivial':(1,1,1),'sign':(1,-1,1),'standard':(2,0,-1)}
S4={'trivial':(1,1,1,1,1),'sign':(1,-1,1,1,-1),
    'standard':(3,1,-1,0,-1),'standard_sign':(3,-1,-1,0,1),
    'partition_22':(2,0,2,-1,0)}
found=[]
for name3,char3 in S3.items():
    for name4,char4 in S4.items():
        numerator=sum(CHARACTERS[t]*CHARTABLE[t][1]*char3[T3.index(t[0])]*char4[T4.index(t[1])] for t in CHARTABLE)
        assert numerator%144==0
        mult=numerator//144
        assert mult>=0
        if mult:found.append((name3,name4,mult))
print('IRREDUCIBLE_MULTIPLICITIES_H2',found)
assert found==[
 ('sign','standard',1),('sign','standard_sign',1),('sign','partition_22',2),
 ('standard','sign',1),('standard','standard',1),('standard','standard_sign',1),
 ('standard','partition_22',1)]
print('K34_THREE_UNORDERED_CHARACTER_PASS')
