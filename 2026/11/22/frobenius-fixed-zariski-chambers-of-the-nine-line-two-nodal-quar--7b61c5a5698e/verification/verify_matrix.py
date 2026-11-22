#!/usr/bin/env python3
"""Exact eleven-curve intersection-lattice verifier for the two-nodal quartic."""
from itertools import permutations
from collections import Counter
from sympy import Matrix, diag, zeros

H=Matrix([1,0,0,0,0,0]); E=[Matrix([int(i==j) for i in range(6)]) for j in range(1,6)]
curves=[('E'+str(i),E[i]) for i in range(5)]
curves += [('A',H-E[0]-E[1]-E[2]),('B',H-E[0]-E[3]-E[4])]
curves += [(f'L{i}{j}',H-E[i]-E[j]) for i in (1,2) for j in (3,4)]
Q=diag(1,-1,-1,-1,-1,-1)
B=Matrix([[int((v.T*Q*w)[0]) for _,w in curves] for _,v in curves])
assert len(curves)==11 and Counter(int(B[i,i]) for i in range(11))==Counter({-1:9,-2:2})

def negative(mask):
    sel=[i for i in range(11) if mask>>i&1]
    return all(((-1)**k)*int(B.extract(sel[:k],sel[:k]).det())>0 for k in range(1,len(sel)+1))
valid={m for m in range(1<<11) if negative(m)}
assert len(valid)==221
assert dict(Counter(m.bit_count() for m in valid))=={0:1,1:11,2:45,3:84,4:67,5:13}

vectors={tuple(v):i for i,(_,v) in enumerate(curves)}
def lift(p):
    perm=[]
    for _,v in curves:
        w=Matrix([v[0]]+[v[1+p.index(i)] for i in range(5)])
        perm.append(vectors[tuple(w)])
    assert sorted(perm)==list(range(11))
    assert all(B[perm[i],perm[j]]==B[i,j] for i in range(11) for j in range(11))
    return tuple(perm)

def act(mask,p):
    return sum(1<<p[i] for i in range(11) if mask>>i&1)

G=[]
for b in permutations(range(1,5)):
    if {frozenset(b[:2]),frozenset(b[2:])}=={frozenset((1,2)),frozenset((3,4))}:
        G.append((0,)+b)
assert len(G)==8
acts=[lift(p) for p in G]
# Group-conjugacy enumeration, independent of the choice of displayed representatives.
def compose(a,b):return tuple(a[b[i]] for i in range(5))
def inverse(a):return tuple(a.index(i) for i in range(5))
remaining_conjugacy=set(G);conjugacy=[]
while remaining_conjugacy:
    g=min(remaining_conjugacy)
    cl={compose(compose(h,g),inverse(h)) for h in G}
    assert cl <= remaining_conjugacy
    remaining_conjugacy-=cl
    conjugacy.append(cl)
assert sorted(map(len,conjugacy))==[1,1,2,2,2]
assert sum(len(cl) for cl in conjugacy)==8

reps={
    'identity': (0,1,2,3,4),
    'single_inner_swap':(0,2,1,3,4),
    'double_inner_swap':(0,2,1,4,3),
    'exchange_pairs':(0,3,4,1,2),
    'order_four':(0,3,4,2,1),
}
expect={
    'identity':(221,[1,11,45,84,67,13]),
    'single_inner_swap':(61,[1,5,13,18,19,5]),
    'double_inner_swap':(17,[1,3,5,4,3,1]),
    'exchange_pairs':(23,[1,3,5,6,5,3]),
    'order_four':(5,[1,1,1,0,1,1]),
}
assert {tuple(reps[name]) for name in reps} <= set(G)
assert len({next(i for i,cl in enumerate(conjugacy) if tuple(p) in cl) for p in reps.values()})==5
for name,p in reps.items():
    action=lift(p)
    fixed=[s for s in valid if act(s,action)==s]
    observed=[sum(s.bit_count()==k for s in fixed) for k in range(6)]
    assert (len(fixed),observed)==expect[name],(name,len(fixed),observed)
    print(name,len(fixed),observed)

# Same negative-curve permutation-cycle data yet different invariant supports
for name in ('double_inner_swap','exchange_pairs'):
    p=lift(reps[name]); seen=set(); lengths=[]
    for i in range(11):
        if i in seen:continue
        j=i;count=0
        while j not in seen:seen.add(j);count+=1;j=p[j]
        lengths.append(count)
    print(name,'negative_curve_cycle_lengths',sorted(lengths))
    assert sorted(lengths)==[1,1,1,2,2,2,2]

# Direct D8 orbits, and independent group average (Burnside)
remaining=valid.copy(); orbits=[]
while remaining:
    m=min(remaining); orb={act(m,p) for p in acts};assert orb<=remaining
    remaining-=orb;orbits.append(orb)
assert len(orbits)==52
assert Counter(len(o) for o in orbits)==Counter({1:5,2:6,4:31,8:10})
assert sum(sum(act(m,p)==m for m in valid) for p in acts)==8*len(orbits)
print('orbits',len(orbits),'sizes',dict(Counter(len(o) for o in orbits)))
print('TWO_NODAL_QUARTIC_MATRIX_OK')
