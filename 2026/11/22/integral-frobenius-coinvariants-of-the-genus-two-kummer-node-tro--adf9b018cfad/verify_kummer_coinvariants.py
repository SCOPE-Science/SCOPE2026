"""Exact integral node--trope Frobenius coinvariant calculation for genus-two Kummer quartics.

Python 3, SymPy >=1.10; execute `python kummer_descent_checker.py`.
All calculations are integral and the 720 permutations are exhausted.
"""
from itertools import combinations, permutations
from collections import defaultdict, Counter
from math import factorial
from sympy import Matrix, eye, zeros
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.domains import ZZ

R=range(6)
NODES=[()] + list(combinations(R,2))
TROPES=[(i,) for i in R] + sorted({tuple(x) for x in combinations(R,3) if 0 in x})
assert len(NODES)==len(TROPES)==16

def incidence(n,t):
    if len(t)==1:
        return (len(n)==0 or (len(n)==2 and t[0] in n))
    if not n:
        return False
    return (set(n)<=set(t) or set(n).isdisjoint(t))

A=Matrix([[int(incidence(n,t)) for t in TROPES] for n in NODES])
assert all(sum(A.row(i))==6 for i in range(16))
assert all(sum(A.col(i))==6 for i in range(16))
assert A*A.T==4*eye(16)+2*Matrix.ones(16,16)

def orbit_lengths(action):
    visited=set();lens=[]
    for x in range(len(action)):
        if x not in visited:
            k=x;c=0
            while k not in visited:
                visited.add(k);c+=1;k=action[k]
            lens.append(c)
    return tuple(sorted(lens))

def cycle_partition(p):
    return tuple(sorted(orbit_lengths(p),reverse=True))

def permute_labels(p):
    node_ids={x:i for i,x in enumerate(NODES)}
    trope_ids={x:i for i,x in enumerate(TROPES)}
    nx=[]; tx=[]
    for node in NODES:
        nx.append(node_ids[tuple(sorted(p[i] for i in node))])
    for trope in TROPES:
        if len(trope)==1:
            tt=(p[trope[0]],)
        else:
            tt=tuple(sorted(p[i] for i in trope))
            if 0 not in tt:tt=tuple(i for i in R if i not in tt)
        tx.append(trope_ids[tt])
    return nx,tx

def permutation_matrix(action):
    P=zeros(len(action))
    for col,row in enumerate(action):P[row,col]=1
    return P

base=list(smith_normal_form(A,domain=ZZ).diagonal())
assert tuple(sorted(abs(x) for x in base))==(1,)*6+(2,)*4+(4,)*5+(12,)
results={}; counts=Counter()
for p in permutations(R):
    part=cycle_partition(p)
    counts[part]+=1
    nx,tx=permute_labels(p)
    P=permutation_matrix(nx)
    Q=permutation_matrix(tx)
    assert P*A == A*Q
    if part not in results:
        M=A.row_join(P-eye(16))
        D=smith_normal_form(M,domain=ZZ)
        factors=tuple(abs(int(D[i,i])) for i in range(16))
        assert all(x!=0 for x in factors)
        # Independent HNF verification, with A^{-1}=(3*A.T-J)/12.
        assert A*(3*A.T-Matrix.ones(16,16))==12*eye(16)
        counts_mod={}
        for n in (2,3,4):
            H=hermite_normal_form(M.row_join(n*eye(16)))
            counts_mod[n]=abs(int(H.det()))
        a_plus_b=counts_mod[2].bit_length()-1
        a_plus_2b=counts_mod[4].bit_length()-1
        c=0
        val=counts_mod[3]
        while val>1:
            assert val%3==0
            val//=3;c+=1
        a=2*a_plus_b-a_plus_2b
        b=a_plus_2b-a_plus_b
        tor3=sum(x%3==0 for x in factors)
        assert tor3==c
        assert sum(1 for x in factors if x%4==0)==b
        assert sum(1 for x in factors if x%2==0 and x%4!=0)==a
        assert a>=0 and b>=0 and c>=0
        results[part]=(factors,orbit_lengths(nx),orbit_lengths(tx),(a,b,c),counts_mod)
    # All permutations conjugate under S6 for the same cycle partition,
    # hence have conjugate node and trope integral permutation actions.
assert len(results)==11 and sum(counts.values())==720
assert results[(2,2,1,1)][1]==results[(2,2,2)][1]
assert results[(2,2,1,1)][2]==results[(2,2,2)][2]
assert results[(2,2,1,1)][3]!=results[(2,2,2)][3]
print('BASE SNF:',tuple(abs(int(x)) for x in base))
for part in sorted(results):
    factors, nc, tc, abc, mods=results[part]
    tor=tuple(x for x in factors if x>1)
    print(f'{str(part):<20} size={counts[part]:3} a,b,c={abc} residues={mods} node_orbits={str(nc):<30} torsion={tor}')
print('PASSED: 11 classes, 720 permutations, 16x16 incidence, exact integral Smith forms')
