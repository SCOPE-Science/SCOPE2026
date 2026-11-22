"""Exact finite verification of the symmetric-edge-polytope metric decoder.
Standard library only.  Finite tests do not establish the general theorem.
"""
from itertools import combinations


def oriented_roots(edges):
    return [r for u,v in edges for r in ((u,v),(v,u))]


def squared_distance(r,s):
    # Direct coordinate expansion, avoiding a matrix or geometry package.
    a={}
    for v,sgn in ((r[0],1),(r[1],-1),(s[0],-1),(s[1],1)):
        a[v]=a.get(v,0)+sgn
    return sum(x*x for x in a.values())


def reconstruct_line_adjacency(edges):
    roots=oriented_roots(edges)
    m=len(edges)
    for i,r in enumerate(roots):
        opposite=[j for j,s in enumerate(roots) if squared_distance(r,s)==8]
        assert opposite==[i^1], (edges,i,opposite)
    recovered=set()
    for i,j in combinations(range(m),2):
        shell={squared_distance(roots[x],roots[y])
               for x in (2*i,2*i+1) for y in (2*j,2*j+1)}
        assert shell in ({2,6},{4}), (edges,i,j,shell)
        if shell=={2,6}: recovered.add((i,j))
    expected={(i,j) for i,j in combinations(range(m),2)
              if set(edges[i]) & set(edges[j])}
    assert recovered==expected, (edges,recovered,expected)
    return recovered


def rank_of_roots(n,edges):
    mat=[]
    for u,v in edges:
        r=[0]*n; r[u]=1; r[v]=-1
        mat.append(r)
    # Exact rational-free elimination: ranks are unchanged by integer
    # row operations; select nonzero pivots and eliminate with integers.
    rank=0
    for col in range(n):
        k=next((j for j in range(rank,len(mat)) if mat[j][col]!=0),None)
        if k is None: continue
        mat[rank],mat[k]=mat[k],mat[rank]
        pivot=mat[rank][col]
        for j in range(rank+1,len(mat)):
            q=mat[j][col]
            if q:
                mat[j]=[pivot*x-q*y for x,y in zip(mat[j],mat[rank])]
        rank+=1
        if rank==len(mat): break
    return rank


def edges_from_mask(n,mask):
    pairs=list(combinations(range(n),2))
    return [pairs[i] for i in range(len(pairs)) if mask>>i&1]


def exercise(n,masks):
    cases=0
    for mask in masks:
        es=edges_from_mask(n,mask)
        if not es: continue
        reconstruct_line_adjacency(es)
        cases+=1
    return cases


count=sum(exercise(n,range(1<<(n*(n-1)//2))) for n in range(2,6))
# Include deterministic 6-vertex dense and sparse configurations.
count+=exercise(6,[i*61 % (1<<15) for i in range(600)]+[(1<<15)-1])
tri=[(0,1),(1,2),(0,2)]
claw=[(0,1),(0,2),(0,3)]
assert reconstruct_line_adjacency(tri)==reconstruct_line_adjacency(claw)
assert rank_of_roots(3,tri)==2
assert rank_of_roots(4,claw)==3
path=[(0,1),(1,2),(2,3)]
assert reconstruct_line_adjacency(path)!=reconstruct_line_adjacency(claw)
# Squared-distance perturbation below 1 never changes its nearest-even shell.
for es in (tri,claw,path,[(0,1),(1,2),(2,3),(3,0)]):
    roots=oriented_roots(es)
    for i,j in combinations(range(len(roots)),2):
        d=squared_distance(roots[i],roots[j])
        assert d in (2,4,6,8)
        for noise in (-0.99,-0.37,0.0,0.37,0.99):
            assert 2*round((d+noise)/2)==d
print('SEP_METRIC_RECONSTRUCTION_EXACT_PASS')
print('graphs_tested',count)
print('Whitney_exception_dimensions',rank_of_roots(3,tri),rank_of_roots(4,claw))
print('squared_distance_shells',(2,4,6,8))
