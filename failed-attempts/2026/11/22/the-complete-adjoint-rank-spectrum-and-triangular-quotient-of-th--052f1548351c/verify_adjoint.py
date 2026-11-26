#!/usr/bin/env python3
"""Reproduce the four-dimensional adjoint-action matrices from the Hopf maps.
Scientific standalone verifier; no external packages or data are required.
"""
from itertools import product

def multiply(i,j):
    a, n= i%2,i//2
    b, m= j%2,j//2
    if n+m>=2: return (0,None)
    return ((-1)**(n*b), (a+b)%2+2*(n+m))

COPRODUCT={0:[(0,0,1)],1:[(1,1,1)],2:[(1,2,1),(2,0,1)],3:[(0,3,1),(3,1,1)]}
ANTIPODE={0:[(0,1)],1:[(1,1)],2:[(3,-1)],3:[(2,1)]}

def adjoint_basis(i):
    out=[[0]*4 for _ in range(4)]
    for j in range(4):
        for s,t,k in COPRODUCT[i]:
            sg,u=multiply(s,j)
            if u is None:continue
            for m,v in ANTIPODE[t]:
                sh,w=multiply(u,m)
                if w is not None:out[w][j]+=k*v*sg*sh
    return out

def rank_mod(matrix,p):
    arr=[[v%p for v in row] for row in matrix]
    rank=0
    for c in range(len(arr[0])):
        piv=next((i for i in range(rank,len(arr)) if arr[i][c]),None)
        if piv is None:continue
        arr[rank],arr[piv]=arr[piv],arr[rank]
        d=pow(arr[rank][c],-1,p)
        arr[rank]=[(v*d)%p for v in arr[rank]]
        for j in range(rank+1,len(arr)):
            k=arr[j][c]
            if k:arr[j]=[(x-k*y)%p for x,y in zip(arr[j],arr[rank])]
        rank+=1
    return rank

B=[adjoint_basis(i) for i in range(4)]
assert B[0]==[[int(i==j) for j in range(4)] for i in range(4)]
assert B[1]==[[int(i==j)*(1 if i<2 else -1) for j in range(4)] for i in range(4)]
assert B[2]==[[(-2 if (i,j)==(3,1) else 0) for j in range(4)] for i in range(4)]
assert B[3]==[[ (2 if (i,j)==(3,1) else 0) for j in range(4)] for i in range(4)]

for p in (3,5,7,11):
    counts=[0]*5
    for a,b,d,e in product(range(p), repeat=4):
        A=[[ (a*B[0][i][j]+b*B[1][i][j]+d*B[2][i][j]+e*B[3][i][j])%p for j in range(4)] for i in range(4)]
        counts[rank_mod(A,p)]+=1
    expected=[p, p*(p-1), 2*p*p*(p-1),0, p*p*(p-1)**2]
    assert counts==expected,(p,counts,expected)
    assert sum(counts)==p**4
    print(f'q={p} rank_counts={counts}')
print('SWEEDLER_HOPF_ADJOINT_RANKS_OK')
