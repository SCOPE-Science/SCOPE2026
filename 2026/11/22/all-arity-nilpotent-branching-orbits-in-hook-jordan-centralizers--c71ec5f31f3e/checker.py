from itertools import product
from collections import Counter,defaultdict

def bracket_zero(x,y,q):return (x[1]*y[2]-y[1]*x[2])%q==0

def act(g,x,q,m):
 u,e,f,d=g; a,b,c=x
 ui=pow(u,-1,q);di=pow(d,-1,q)
 bp=u*b*di%q;cp=d*c*ui%q
 ap=list(a);ap[-1]=(a[-1]+e*c*ui-bp*f*ui)%q
 return (tuple(ap),bp,cp)

def key(tup,q,m):
 r=len(tup); low=tuple(x[0][:-1] for x in tup);z=tuple(x[0][-1] for x in tup)
 b=tuple(x[1] for x in tup);c=tuple(x[2] for x in tup)
 if not any(b) and not any(c):return (low,'center',z)
 v=b if any(b) else c
 j=next(i for i,a in enumerate(v) if a)
 inv=pow(v[j],-1,q)
 v=tuple(vi*inv%q for vi in v)
 s=b[j];t=c[j]
 assert all(b[i]==s*v[i]%q and c[i]==t*v[i]%q for i in range(r))
 rest=tuple((z[i]-z[j]*v[i])%q for i in range(r))
 typ='mix' if s and t else ('b' if s else 'c')
 return (low,typ,(s*t)%q if typ=='mix' else None,v,rest)

def run(q,m,r,exhaustive=True):
 items=[(a,b,c) for a in product(range(q),repeat=m-1) for b,c in product(range(q),repeat=2)]
 groups=defaultdict(list)
 # enumerate commuting tuples through common b/c-line; independently verify bracket property
 for tup in product(items,repeat=r):
  if not all(bracket_zero(tup[i],tup[j],q) for i in range(r) for j in range(i)) :continue
  groups[key(tup,q,m)].append(tup)
 total=sum(map(len,groups.values()));N=q**(r*(m-1))*(1+(q+1)*(q**r-1))
 orbits=q**(r*(m-2))*(q**r+(q+1)*((q**r-1)//(q-1))*q**(r-1))
 assert total==N,(q,m,r,total,N)
 assert len(groups)==orbits,(q,m,r,len(groups),orbits)
 sizes=Counter(map(len,groups.values()))
 assert sizes[1]==q**(r*(m-1))
 assert sizes[q*(q-1)]==orbits-sizes[1] if q>2 else True
 # independently check all tuple group conjugates from first representative and recover entire orbit for small cases
 if exhaustive:
  for k,tups in groups.items():
   x=tups[0]
   target=set(tups)
   observed={tuple(act(g,xx,q,m) for xx in x) for g in product(range(1,q),range(q),range(q),range(1,q))}
   assert observed==target,(q,m,r,k,len(observed),len(target))
 print('PASS',f'q={q}',f'm={m}',f'r={r}',f'commuting_tuples={total}',f'orbits={len(groups)}',f'class_sizes={dict(sizes)}')

for q,m,r in ((2,2,2),(2,3,2),(2,3,3),(2,4,2),(3,2,2),(3,3,2),(5,2,2)):
 run(q,m,r)
