import itertools,networkx as nx,numpy as np
from scipy.optimize import milp,LinearConstraint,Bounds
for n in [4,5,6,7]:
 G=nx.Graph();A=[('a',i) for i in range(n)];B=[('b',i) for i in range(n)];G.add_nodes_from(A+B);G.add_edges_from((a,b) for a in A for b in B if a[1]!=b[1]);
 for S in [A, A+[B[0]]]:
  ed=list(G.edges());E={frozenset(e):j for j,e in enumerate(ed)};P=list(itertools.combinations(S,2));paths=[]
  for k,(a,b) in enumerate(P):
   for p in nx.all_shortest_paths(G,a,b):paths.append((k,[E[frozenset((c,d))] for c,d in zip(p,p[1:])]))
  c=np.zeros(len(paths));M=np.zeros((len(ed)+len(P),len(paths)))
  for j,(k,edgeids) in enumerate(paths):
   M[len(ed)+k,j]=1
   for v in edgeids:M[v,j]=1
  low=np.r_[np.ones(len(ed)),np.zeros(len(P))];upp=np.r_[np.ones(len(ed))*np.inf,np.ones(len(P))];
  r=milp(c,integrality=np.ones(len(paths)),bounds=Bounds(0,1),constraints=LinearConstraint(M,low,upp),options={'time_limit':10})
  print(n,len(S),r.status,r.message[:55],flush=True)
