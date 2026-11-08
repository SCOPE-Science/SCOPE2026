"""Exact edge-selection/Euler-circuit certificate for ternary order 3.

Nine reversal pairs of nonpalindromic triples yield exactly 512 choices.
For each choice compute the balanced and strongly connected conditions,
exact arborescences (Bareiss), and independently enumerate Euler tours.
"""
from itertools import combinations, product
from collections import Counter, defaultdict
from math import factorial, prod

SIGMA = '012'
PAIRS = [(a+b+c, c+b+a)
         for a,c in combinations(SIGMA,2) for b in SIGMA]
assert len(PAIRS) == 9

def reachable(start, adjacency):
    seen={start}
    stack=[start]
    while stack:
        for v in adjacency.get(stack.pop(), []):
            if v not in seen:
                seen.add(v); stack.append(v)
    return seen

def graph(edges):
    out=Counter(e[:2] for e in edges)
    inc=Counter(e[1:] for e in edges)
    vertices=set(out)|set(inc)
    if any(out[v]!=inc[v] for v in vertices):
        return None
    adj=defaultdict(list)
    rev=defaultdict(list)
    for e in edges:
        adj[e[:2]].append(e[1:]);rev[e[1:]].append(e[:2])
    start=min(vertices)
    strong=(reachable(start,adj)==vertices and reachable(start,rev)==vertices)
    return vertices,adj,strong

def determinant_bareiss(M):
    A=[row[:] for row in M]
    n=len(A)
    if n==0:return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            swap=next((r for r in range(k+1,n) if A[r][k]),None)
            if swap is None:return 0
            A[k],A[swap]=A[swap],A[k];sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*p-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
        for i in range(k+1,n):A[i][k]=0
        prev=p
    return sign*A[-1][-1]

def arborescences(edges,vertices,root):
    vs=sorted(vertices); ix={v:i for i,v in enumerate(vs)}
    L=[[0]*len(vs) for _ in vs]
    for e in edges:
        i=ix[e[:2]];j=ix[e[1:]]
        L[i][i]+=1;L[i][j]-=1
    ri=ix[root]
    return determinant_bareiss([[L[i][j] for j in range(len(vs)) if j!=ri]
                                for i in range(len(vs)) if i!=ri])

def tour_count(edges,start_edge):
    # Anchor the cyclic circuit at its unique specified length-three edge.
    rem=set(edges)
    assert start_edge in rem
    rem.remove(start_edge)
    origin=start_edge[:2]
    def rec(v):
        if not rem:
            return int(v==origin)
        ans=0
        for e in tuple(rem):
            if e[:2]!=v:continue
            rem.remove(e)
            ans+=rec(e[1:])
            rem.add(e)
        return ans
    return rec(start_edge[1:])

balanced=[]; strong=[]
for bits in product('01',repeat=9):
    mask=''.join(bits)
    E=[p[int(b)] for p,b in zip(PAIRS,bits)]
    G=graph(E)
    if G is None:continue
    vertices,adj,connected=G
    balanced.append(mask)
    if connected:
        root=min(vertices)
        tau=arborescences(E,vertices,root)
        factor=prod(factorial(len(adj[v])-1) for v in vertices)
        direct=tour_count(E,min(E))
        assert tau==4 and factor==1 and direct==4, (mask,tau,factor,direct)
        strong.append(mask)

assert sorted(balanced)==[
'000111000','001101100','001110001','010101010','011100011',
'100011100','101010101','110001110','110010011','111000111'
],balanced
assert strong==['001101100','110010011'],strong
assert len(strong)*4==8
print('EULER_VERIFY_OK', len(balanced), strong, 'cycles=8')
