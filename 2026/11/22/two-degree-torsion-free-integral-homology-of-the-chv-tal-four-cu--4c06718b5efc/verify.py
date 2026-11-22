#!/usr/bin/env python3
"""Exact integral homology certificate for the Chvatal ordinary four-cut complex.
Requires Python 3.10+ and SymPy 1.12+. Outputs only reproducible scientific checks.
"""
import itertools
from collections import Counter
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

EDGES=((0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11))
N=12
ADJ=[set() for _ in range(N)]
for u,v in EDGES:
    ADJ[u].add(v); ADJ[v].add(u)
assert len(EDGES)==24 and all(len(s)==4 for s in ADJ)
assert all(not ({u,v}<=ADJ[w]) for w in range(N) for u,v in EDGES)

def connected(t):
    t=set(t); reached={next(iter(t))}
    while True:
        next_reached=reached|{w for v in reached for w in ADJ[v] if w in t}
        if next_reached==reached: return len(reached)==len(t)
        reached=next_reached

def mask(t):return sum(1<<i for i in t)
forbidden=[mask(q) for q in itertools.combinations(range(N),4) if not connected(q)]
assert len(forbidden)==282
faces={z for z in range(1,1<<N) if not any(z&f==f for f in forbidden)}
original_counts=Counter(z.bit_count()-1 for z in faces)
assert [original_counts[i] for i in range(5)]==[12,66,220,213,48]
assert max(original_counts)==4

# Repeated free-face collapses. The 2-face selected must have precisely
# one surviving immediate coface and that coface must be maximal.
face_set=faces.copy(); moves=[]
for d in [4,3,2,1]:
    while True:
        selected=None
        for x in sorted(face_set, key=lambda z:(z.bit_count(),z)):
            if x.bit_count()!=d: continue
            co=[z for z in face_set if z.bit_count()==d+1 and z&x==x]
            if len(co)!=1: continue
            z=co[0]
            if not any(t!=z and t&z==z for t in face_set):selected=(x,z);break
        if selected is None:break
        x,z=selected;face_set.remove(x);face_set.remove(z);moves.append(selected)
move_counts=Counter(z.bit_count()-1 for x,z in moves)
assert move_counts=={4:48,3:77}
remaining_counts=Counter(z.bit_count()-1 for z in face_set)
assert [remaining_counts[i] for i in range(4)]==[12,66,143,88]
assert not any(z.bit_count()==5 for z in face_set)
# The remaining faces are closed under nonempty subset.
for z in face_set:
    for v in range(N):
        if z&(1<<v) and z.bit_count()>1:assert z^(1<<v) in face_set

def boundary(d):
    low=sorted(x for x in face_set if x.bit_count()==d)
    high=sorted(x for x in face_set if x.bit_count()==d+1)
    row={x:i for i,x in enumerate(low)}
    data={}
    for j,z in enumerate(high):
        vertices=[v for v in range(N) if z&(1<<v)]
        for k,v in enumerate(vertices):
            data[row[z^(1<<v)],j]=1 if k%2==0 else -1
    return SparseMatrix(len(low),len(high),data)

ranks={}; diagonal_profiles={}
for d in [1,2,3]:
    M=boundary(d)
    S=smith_normal_form(M,domain=ZZ)
    nonzero=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0]
    assert all(v==1 for v in nonzero)
    ranks[d]=len(nonzero)
    diagonal_profiles[d]=(len(nonzero),min(S.shape)-len(nonzero))
assert [ranks[i] for i in (1,2,3)]==[11,55,80]
assert boundary(2)*boundary(3)==SparseMatrix(66,88,{})
assert boundary(1)*boundary(2)==SparseMatrix(12,143,{})
assert (remaining_counts[2]-ranks[2]-ranks[3],remaining_counts[3]-ranks[3])==(8,8)

# Independently compute the original full dual's ranks over two fields;
# collapses are not used in this separate finite-field computation.
def rank_mod_p(d,p):
    low=sorted(x for x in faces if x.bit_count()==d)
    high=sorted(x for x in faces if x.bit_count()==d+1)
    row={x:i for i,x in enumerate(low)}; piv={}
    for z in high:
        verts=[v for v in range(N) if z&(1<<v)]
        column={row[z^(1<<v)]:(1 if k%2==0 else p-1) for k,v in enumerate(verts)}
        while column:
            i=max(column)
            if i not in piv:
                inv=pow(column[i],-1,p)
                piv[i]={j:(x*inv)%p for j,x in column.items() if x%p}
                break
            factor=column[i]
            for j,x in piv[i].items():
                v=(column.get(j,0)-factor*x)%p
                if v:column[j]=v
                else:column.pop(j,None)
    return len(piv)
for p in (2,3):
    r=[rank_mod_p(d,p) for d in (1,2,3,4)]
    assert r==[11,55,157,48],(p,r)
print('CHVATAL_FOUR_CUT_VERIFIED')
print('n=12 edges=24 disconnected_quadruples=282')
print('dual_fvector=',[original_counts[i] for i in range(5)])
print('elementary_collapses=125 by_dimensions=',dict(sorted(move_counts.items())))
print('remaining_fvector=',[remaining_counts[i] for i in range(4)])
print('reduced_integer_boundary_ranks=',ranks)
print('reduced_integer_boundary_smith_nonzero_factors_are_all_one=True')
print('reduced_dual_integral_homology: H2=Z^8, H3=Z^8, all_other_reduced=0')
print('four_cut_integral_homology: H6=Z^8, H7=Z^8, all_other_reduced=0')
print('full_dual_F2_F3_boundary_ranks=(11,55,157,48)')
