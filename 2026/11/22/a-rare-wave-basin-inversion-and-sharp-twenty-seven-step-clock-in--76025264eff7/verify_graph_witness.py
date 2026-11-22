"""Independent small witness check and explicit Frucht-graph relabeling certificate."""
A=[(0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),(4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11)]
L=[-5,-2,-4,2,5,-2,2,5,-2,-5,4,2]
P=[5,3,2,1,0,7,6,4,10,11,8,9]
E=set(tuple(sorted(e)) for e in A)
F=set(tuple(sorted((i,(i+1)%12))) for i in range(12))
F.update(tuple(sorted((i,(i+L[i])%12))) for i in range(12))
assert len(E)==len(F)==18
assert set(tuple(sorted((P[a],P[b]))) for a,b in E)==F
N=[set() for _ in range(12)]
for a,b in E:N[a].add(b);N[b].add(a)
assert all(len(x)==3 for x in N)
def step(x):
 c=[(x>>(2*i))&3 for i in range(12)]
 out=0
 for i in range(12):
  z=(c[i]+1)%4 if c[i] else int(any(c[j]==1 for j in N[i]))
  out+=z<<(2*i)
 return out
witness=5999879
seen={};x=witness; t=0
while x not in seen:
 seen[x]=t
 x=step(x);t+=1
assert seen[x]==27 and t-seen[x]==4
print('GRAPH_ISOMORPHISM_OK mapping='+str(P))
print('WITNESS_OK start='+str(witness)+' first_entry='+str(seen[x])+' period='+str(t-seen[x])+' periodic_state='+str(x))
