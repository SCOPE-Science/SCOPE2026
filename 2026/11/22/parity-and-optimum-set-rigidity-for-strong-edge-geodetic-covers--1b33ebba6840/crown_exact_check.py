import networkx as nx,itertools,collections,time

def calc(n):
 G=nx.Graph(); A=[('a',i) for i in range(n)];B=[('b',i) for i in range(n)];G.add_nodes_from(A+B);G.add_edges_from((a,b) for a in A for b in B if a[1]!=b[1]); E=list(G.edges()); idx={frozenset(e):i for i,e in enumerate(E)};V=A+B
 paths={}
 for a,b in itertools.combinations(V,2):
  paths[(a,b)]=list(set(sum(1<<idx[frozenset((c,d))] for c,d in zip(p,p[1:])) for p in nx.all_shortest_paths(G,a,b)))
 # feasibility target all edges, forced single path and optional 2+; exhaustive DFS
 def feasible(S):
  ss=set(S);opts=[c for p,c in paths.items() if p[0] in ss and p[1] in ss];mask=(1<<len(E))-1
  forced=0; choices=[]
  for c in opts:
   if len(c)==1:forced|=c[0]
   else:choices.append(c)
  mask &=~forced
  if not mask:return True
  avail=0
  for c in choices:
   for z in c:avail|=z
  if mask & ~avail:return False
  d={i:[] for i in range(len(E)) if mask>>i&1}
  for j,c in enumerate(choices):
   for k,z in enumerate(c):
    for i in d:
     if z>>i&1:d[i].append((j,z))
  memo=set()
  def rec(uncovered,used):
   if not uncovered:return True
   key=(uncovered,used)
   if key in memo:return False
   e=min((i for i in d if uncovered>>i&1),key=lambda i:sum(not used>>j&1 for j,_ in d[i]))
   for j,z in d[e]:
    if not used>>j&1 and rec(uncovered&~z, used|(1<<j)):return True
   memo.add(key);return False
  return rec(mask,0)
 stats=collections.Counter();mins=[]
 for mask in range(1<<(2*n)):
  S=[V[i] for i in range(2*n) if mask>>i&1]
  if len(S)>min(stats, default=2*n+1):continue
  if feasible(S):
   stats[len(S)]+=1
   if len(S)<len(mins[0]) if mins else True:mins=[S]
   elif len(S)==len(mins[0]):mins.append(S)
 print('n',n,'min',min(stats),'count',stats[min(stats)],flush=True)
 expected={3:(3,14),4:(5,32),5:(5,2),6:(7,12),7:(7,2)}[n]
 assert (min(stats),stats[min(stats)])==expected

for n in [3,4,5,6,7]:
 t=time.time();calc(n);print('seconds',time.time()-t,flush=True)
