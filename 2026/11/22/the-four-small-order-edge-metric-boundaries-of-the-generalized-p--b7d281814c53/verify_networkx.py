import networkx as nx,itertools
for n in range(7,11):
 G=nx.Graph();G.add_nodes_from(range(2*n))
 for i in range(n):
  G.add_edge(i,(i+1)%n);G.add_edge(i,i+n);G.add_edge(i+n,((i+3)%n)+n)
 if not nx.is_connected(G):print(n,'disconnected');continue
 E=sorted(tuple(sorted(e)) for e in G.edges()); D=dict(nx.all_pairs_shortest_path_length(G))
 signatures=[tuple(min(D[v][a],D[v][b]) for a,b in E) for v in G]
 ans=[]
 for k in [2,3,4]:
  cnt=0; witness=None
  for landmark in itertools.combinations(range(2*n),k):
   if len(set(zip(*(signatures[v] for v in landmark))))==len(E):
    cnt+=1
    if witness is None:witness=landmark
  if cnt:
   ans=(k,cnt,witness)
   break
 print('n',n,'order',G.number_of_nodes(),'edges',len(E),'answer',ans,flush=True)
