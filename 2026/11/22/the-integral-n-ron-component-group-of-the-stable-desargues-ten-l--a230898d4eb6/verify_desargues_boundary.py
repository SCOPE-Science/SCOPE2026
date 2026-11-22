"""Exact critical group of the normal-crossings Desargues ten-line boundary.
Pure Python 3, no external dependencies. All checks are exact integers or prime-power rings.
"""
from itertools import combinations
from collections import Counter
from math import prod
P = list(combinations(range(5),2))
T = list(combinations(range(5),3))
assert len(P) == len(T) == 10
L = [[0 for _ in range(20)] for _ in range(20)]

def add_edge(a,b):
    assert a != b
    L[a][a] += 1
    L[b][b] += 1
    L[a][b] -= 1
    L[b][a] -= 1

for i,p in enumerate(P):
    for j,t in enumerate(T):
        if set(p) <= set(t):
            add_edge(i,10+j)
for j,t in enumerate(T):
    for k in range(j):
        if len(set(t).intersection(T[k])) == 1:
            add_edge(10+j,10+k)
assert [L[i][i] for i in range(20)] == [3]*10+[6]*10
assert sum(L[i][i] for i in range(20))//2 == 45
assert all(sum(row)==0 for row in L)
assert sum(L[i][j]==-1 for i in range(10) for j in range(10,20)) == 30
assert sum(L[i][j]==-1 for i in range(10,20) for j in range(i+1,20)) == 15

def valuations_by_unimodular_local_steps(M,p,prec):
    """p-local Smith valuations via invertible modular row operations.
    Unipotent eliminations and unit row/column swaps over Z/(p**prec).
    Factoring out p from the zero-mod-p block advances a valuation.
    """
    A=[row[:] for row in M]
    mod=p**prec
    A=[[x%mod for x in row] for row in A]
    n=len(A);level=0;vals=[]
    while n:
        pivot = next(((i,j) for i in range(n) for j in range(n)
                      if A[i][j]%p != 0), None)
        if pivot is None:
            assert all(x%p==0 for row in A for x in row)
            mod//=p
            assert mod>1, 'insufficient p-adic precision'
            A=[[x//p for x in row] for row in A]
            level+=1
            continue
        i,j=pivot
        A[0],A[i]=A[i],A[0]
        for row in A: row[0],row[j]=row[j],row[0]
        inv=pow(A[0][0],-1,mod)
        for r in range(1,n):
            c=A[r][0]*inv%mod
            for s in range(1,n):
                A[r][s]=(A[r][s]-c*A[0][s])%mod
        A=[row[1:] for row in A[1:]]
        vals.append(level);n-=1
    assert len(vals)==len(M)
    return sorted(vals)

# Derive the spanning-tree count independently from the exact Petersen spectrum:
# the 10 x 10 point/triple incidence B has B^t B=2I+J-A_P,
# where A_P is the Petersen adjacency (3,1^5,(-2)^4).
# The nonzero Laplacian eigenvalue products are 6, 14^5, 20^4.
spanning_trees=6*14**5*20**4//20
assert spanning_trees == 2**12*3*5**3*7**5 == 25815552000

expected=[1]*11+[2]*3+[14,28,140,140,420]
assert len(expected)==19
assert all(expected[i+1]%expected[i]==0 for i in range(18))
assert prod(expected)==spanning_trees

def v_p(n,p):
    v=0
    while n%p==0 and n:
        n//=p;v+=1
    return v

# Two deleted vertices, in the distinct line and exceptional-component orbits.
for deleted in (0,10):
    R=[[L[i][j] for j in range(20) if j!=deleted]
       for i in range(20) if i!=deleted]
    actual={}
    for p,e in ((2,12),(3,1),(5,3),(7,5)):
        actual[p]=valuations_by_unimodular_local_steps(R,p,e+2)
        assert actual[p]==sorted(v_p(d,p) for d in expected), (deleted,p,actual[p])
        assert sum(actual[p])==e
    print('deleted',deleted,'local_Smith_valuations',
          {p:dict(Counter(v)) for p,v in actual.items()})

print('DESARGUES_STABLE_BOUNDARY_CRITICAL_GROUP_OK',
      'vertices=20 edges=45 genus=26 order='+str(spanning_trees),
      'factors='+str(Counter(expected)))
