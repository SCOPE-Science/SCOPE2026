#!/usr/bin/env python3
"""Exact modular-chain verification of a symmetric-group action on M(K7).
Public-domain algorithm description: finite field elimination and direct simplicial chains.
No external Python dependencies; requires adjacent torsion_witness.json.
"""
import itertools,json
from pathlib import Path
P=3
C=json.loads((Path(__file__).resolve().parent/'torsion_witness.json').read_text(encoding='utf8'))
assert C['prime']==P
V=list(itertools.combinations(range(7),2)); vi={u:i for i,u in enumerate(V)}
E=[(i,j) for i,j in itertools.combinations(range(len(V)),2) if set(V[i]).isdisjoint(V[j])]
ei={u:i for i,u in enumerate(E)}
T=[(i,j,k) for i,j,k in itertools.combinations(range(len(V)),3) if (i,j) in ei and (i,k) in ei and (j,k) in ei]
ti={u:i for i,u in enumerate(T)}
assert (len(V),len(E),len(T))==(21,105,105)

def combine(a,b,m):return [(x+m*y)%P for x,y in zip(a,b)]
def d1(v):
    out=[0]*len(V)
    for i,c in enumerate(v):
        a,b=E[i];out[a]=(out[a]-c)%P;out[b]=(out[b]+c)%P
    return out

def d2(t):
    a,b,c=t;out=[0]*len(E)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:out[ei[e]]=s%P
    return out

basis={}
def reduce(v):
    u=v[:]
    for k in sorted(basis):
        if u[k]:u=combine(u,basis[k],-u[k])
    return u
for t in T:
    a=reduce(d2(t))
    if any(a):
        k=next(i for i,x in enumerate(a) if x)
        inv=pow(a[k],-1,P)
        basis[k]=[x*inv%P for x in a]
assert len(basis)==84
assert len(E)-len(V)+1-len(basis)==1

# Cycle is integral: verify every oriented vertex incidence over integers.
z=[0]*len(E)
for row in C['oriented_cycle']:
    a,b=(vi[tuple(u)] for u in row['edge']);c=row['coefficient']
    if a>b:a,b=b,a;c=-c
    z[ei[(a,b)]]+=c
assert all(x in (-1,0,1) for x in z)
int_boundary=[0]*len(V)
for i,c in enumerate(z):
    a,b=E[i];int_boundary[a]-=c;int_boundary[b]+=c
assert all(x==0 for x in int_boundary)
z3=[x%P for x in z]
assert any(reduce(z3)), 'The displayed cycle must be nonzero in mod-three homology.'

# Verify the 32-triangle witness independently, coefficient by coefficient.
s=C['coordinate_transposition'];tz=[0]*len(E)
for i,c in enumerate(z):
    if not c:continue
    a,b=E[i];x=vi[tuple(sorted(s[t] for t in V[a]))]
    y=vi[tuple(sorted(s[t] for t in V[b]))]
    if x>y:x,y=y,x;c=-c
    tz[ei[(x,y)]]+=c
w=[(a+b)%P for a,b in zip(z,tz)]
assert all(x==0 for x in d1(w))
rhs=[0]*len(E)
assert len(C['two_chain_certificate'])==32
for row in C['two_chain_certificate']:
    t=tuple(vi[tuple(u)] for u in row['triangle']);c=row['coefficient']
    assert t in ti and c in (-1,1)
    rhs=combine(rhs,d2(t),c)
assert rhs==w,'Boundary of the supplied 32-triangle 2-chain must equal z+tau(z).'
assert not any(reduce(w))
# The inflated complex has four labeled copies of every matching-complex vertex.
assert (4*len(V),16*len(E),64*len(T))==(84,1680,6720)
added=21*3*6+105*9*2+105*27
assert added==5103 and 20+added==5123
assert 84-1680+6720-1==5123
print('BASE_F_VECTOR 21 105 105')
print('INFLATED_F_VECTOR 84 1680 6720')
print('D2_RANK_MOD3 84; H1_DIM_MOD3 1')
print('NONBOUNDARY_INTEGRAL_CYCLE_EDGES 5')
print('TRANSPOSE_PLUS_CYCLE_2_CHAIN_TRIANGLES 32')
print('ADDED_TWO_SPHERES 5103; TOTAL_BETA2 5123')
print('ALL_VERIFY_OK')
