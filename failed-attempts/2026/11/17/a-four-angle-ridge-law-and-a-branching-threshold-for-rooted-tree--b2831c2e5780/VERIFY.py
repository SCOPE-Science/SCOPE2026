import networkx as nx, numpy as np, itertools, math
total=0
for n in range(2,10):
 checked=0
 for T in nx.generators.nonisomorphic_trees(n):
  for root in range(n):
   parent={root:None};queue=[root]
   for v in queue:
    for u in T.neighbors(v):
     if u not in parent: parent[u]=v;queue.append(u)
   children={i:[] for i in range(n)}
   for v,p in parent.items():
    if p is not None: children[p].append(v)
   leaves=[i for i in range(n) if not children[i]]
   V=np.array([v for v in itertools.product([0,1],repeat=n) if all(v[p]<=v[u] for u,p in parent.items() if p is not None)],dtype=float)
   F=[(-np.eye(n)[root],0,'B',root)]
   F += [(np.eye(n)[v],1,'U',v) for v in leaves]
   F += [(np.eye(n)[p]-np.eye(n)[u],0,'E',(p,u)) for u,p in parent.items() if p is not None]
   counts={}
   for f,g in itertools.combinations(F,2):
    v=V[np.isclose(V@f[0],f[1])&np.isclose(V@g[0],g[1])]
    rk=np.linalg.matrix_rank(v-v[0]) if len(v) else -1
    if rk==n-2:
     c=round(float(f[0]@g[0] / (np.linalg.norm(f[0])*np.linalg.norm(g[0]))),6)
     counts[c]=counts.get(c,0)+1
   deg={i:len(children[i]) for i in children}
   Tleaf=sum(deg[parent[v]]==1 for v in leaves)
   fct=n+len(leaves)
   R=fct*(fct-1)//2-len(leaves)+Tleaf
   acute=sum(deg[i] for i in range(n) if i!=root)
   obtuse=sum(d*(d-1)//2 for d in deg.values())
   forty=deg[root]+Tleaf
   ex={-.707107:forty,-.5:acute,.5:obtuse,0.0:R-forty-acute-obtuse}
   counts={k:v for k,v in counts.items() if v}
   ex={k:v for k,v in ex.items() if v}
   if counts!=ex:
    print('FAIL',n,root,T.edges(),counts,ex);raise SystemExit(1)
   checked+=1
 print('PASS',n,checked)
 total+=checked

assert total==748, total
print(f"ROOTED_TREE_RIDGE_SPECTRUM_PASS cases={total}")
