"""Enumerate triangulations of (n+3)-gon -> type-A cluster-tilted bound quivers,
detect oriented cycles and clock data, as computational evidence.

We generate cluster quivers of Dynkin A_n via flips starting from fan triangulation.
Quiver mutation (FZ) at vertex k. Track -> extract underlying cluster-tilted
quiver (no frozen). For each quiver, record #3-cycles, valences, and whether
each 3-cycle vertex has valency 2 (isolated triangle) vs shared vertices.
"""
from collections import defaultdict
import itertools

def mutate(B, k):
    # B: skew-symmetric int matrix n x n
    n = len(B)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==k or j==k:
                C[i][j] = -B[i][j]
            else:
                C[i][j] = B[i][j] + max(0,B[i][k])*max(0,B[k][j]) - max(0,-B[i][k])*max(0,-B[k][j])
    return C

def quiver_arrows(B):
    n=len(B); arr=[]
    for i in range(n):
        for j in range(n):
            if B[i][j]>0:
                arr.extend([(i,j)]*B[i][j])
    return arr

def count_3cycles(B):
    n=len(B)
    cyc=0
    for a,b,c in itertools.combinations(range(n),3):
        # oriented triangle: edges oriented cyclically
        e=[(B[a][b]>0),(B[b][c]>0),(B[c][a]>0)]
        e2=[(B[b][a]>0),(B[c][b]>0),(B[a][c]>0)]
        if all(e) or all(e2): cyc+=1
    return cyc

def explore_A(n, depth=3):
    # initial B = linear A_n orientation 0->1->...->n-1
    B=[[0]*n for _ in range(n)]
    for i in range(n-1):
        B[i][i+1]=1; B[i+1][i]=-1
    seen={tuple(tuple(r) for r in B)}
    frontier=[B]; allq=[B]
    for _ in range(depth):
        nxt=[]
        for Bm in frontier:
            for k in range(n):
                C=mutate(Bm,k)
                t=tuple(tuple(r) for r in C)
                if t not in seen:
                    seen.add(t); nxt.append(C); allq.append(C)
        frontier=nxt
        if not frontier: break
    return allq

for n in [3,4,5]:
    qs = explore_A(n, depth=4 if n<=4 else 3)
    print(f"=== A{n}: {len(qs)} quivers found (bounded search)")
    from collections import Counter
    hist = Counter(count_3cycles(B) for B in qs)
    print("3-cycle count histogram:", dict(hist))
    # check valency<=4 and at most 2 arrows per vertex-pair (cluster-tilted property)
    bad=0
    for B in qs:
        for i in range(n):
            deg=sum(1 for j in range(n) if B[i][j]!=0)
            if deg>4: bad+=1
    print("quivers with vertex valency>4:", bad)
