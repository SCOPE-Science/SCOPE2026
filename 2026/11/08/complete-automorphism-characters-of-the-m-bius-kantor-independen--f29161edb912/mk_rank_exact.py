import itertools,networkx as nx,sympy as sp
from sympy.polys.matrices import DomainMatrix
n=16;G=nx.Graph();G.add_nodes_from(range(n))
for i in range(8):G.add_edges_from([(i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)])
adj=[set(G.neighbors(i)) for i in range(16)];f=[[] for _ in range(8)]
for m in range(1,1<<16):
 s=tuple(i for i in range(16) if m>>i&1)
 if all(j not in adj[i] for k,i in enumerate(s) for j in s[k+1:]):f[len(s)-1].append(s)
I=[{v:i for i,v in enumerate(g)} for g in f]
for k in range(1,8):
 M=sp.MutableSparseMatrix(len(f[k-1]),len(f[k]),{(I[k-1][s[:j]+s[j+1:]],t):(-1)**j for t,s in enumerate(f[k]) for j in range(k+1)})
 print('build',k,M.shape,flush=True)
 D=DomainMatrix.from_Matrix(M)
 print('rank',k,D.rank(),flush=True)

print("EXACT_RATIONAL_BOUNDARY_RANKS_VERIFIED",flush=True)
