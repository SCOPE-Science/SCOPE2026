import sympy as s,numpy as np,networkx as nx
T=3;N=1<<T;rule=73;G=nx.DiGraph()
for a in range(N):
 for b in range(N):
  for c in range(N):
   if all(((rule>>(4*((a>>t)&1)+2*((b>>t)&1)+((c>>t)&1)))&1)==((b>>((t+1)%3))&1) for t in range(T)):
    G.add_edge(a*N+b,b*N+c)
S=[x for x in nx.strongly_connected_components(G) if len(x)>1 or any(G.has_edge(a,a) for a in x)];V=sorted(set().union(*S));M=np.zeros((len(V),len(V)),dtype=int);P={v:i for i,v in enumerate(V)}
for a,b in G.subgraph(V).edges:M[P[a],P[b]]=1
w,v=np.linalg.eig(M.astype(float)); j=np.argmax(w.real);x=np.real(v[:,j]);x*=np.sign(x.sum());print('minvec',min(x));y=np.rint(x*10**13 / min(x)).astype('int64');My=M.astype('int64')@y
low=min(s.Rational(int(My[i]),int(y[i])) for i in range(len(y)));high=max(s.Rational(int(My[i]),int(y[i])) for i in range(len(y)))
print('lambda lower/upper',float(low),float(high));print('PF integer vector',','.join(map(str,y)))
z=s.symbols('z');q=1-z**3-3*z**4-2*z**5-z**7+z**8+2*z**9
l=s.Rational(6469466411,10**10);h=s.Rational(6469466412,10**10)
print('root brackets',float(l),float(h),'signs',s.sign(q.subs(z,l)),s.sign(q.subs(z,h)),'positive roots 0..1',s.Poly(q,z).count_roots(0,1))
print('gcd cycles',sorted({len(c) for c in nx.simple_cycles(G.subgraph(V))})[:20]);print('SCC',[len(t) for t in S]);print('primitivity',nx.is_strongly_connected(G.subgraph(V)),any(len(c)==3 for c in nx.simple_cycles(G.subgraph(V))),any(len(c)==4 for c in nx.simple_cycles(G.subgraph(V))))
