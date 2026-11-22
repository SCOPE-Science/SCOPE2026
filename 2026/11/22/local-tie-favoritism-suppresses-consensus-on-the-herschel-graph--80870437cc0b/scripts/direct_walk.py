from collections import Counter
from itertools import combinations
A=((2,4,5),(1,3,6,7),(2,4,8),(1,3,9,10),(1,6,10),(2,5,11),(2,8,11),(3,7,9),(4,8,11),(4,5,11),(6,7,9,10))
assert sum(map(len,A))==36
hub=(2,4,11)

def step(s,B):
 t=0
 for i,ns in enumerate(A):
  sm=sum((s>>(u-1))&1 for u in ns)
  if sm*2>len(ns):v=1
  elif sm*2<len(ns):v=0
  else:v=1 if i+1 in B else ((s>>i)&1)
  t |=v<<i
 return t

def calc(B):
 N=2**11
 F=[step(s,B) for s in range(N)]
 # independent full walk with true first-periodic-entry
 period,first,representative={}, {}, {}
 for s in range(N):
  path=[];seen={};u=s
  while u not in seen:
   seen[u]=len(path);path.append(u);u=F[u]
  entry=seen[u];L=len(path)-entry
  first[s]=entry; period[s]=L
  representative[s]=min(path[entry:])
 fixed=[s for s in range(N) if F[s]==s]
 twos=sorted(set(representative[s] for s in range(N) if period[s]==2))
 basin=Counter(representative.values())
 return dict(k=len(B), B=list(sorted(B)), fixed=len(fixed), twos=len(twos),max_entry=max(first.values()),basin0=basin[0],basin1=basin[N-1], fixed_basin=sum(v for a,v in basin.items() if F[a]==a), fixed_hist=sorted(Counter(basin[a] for a in fixed).items()),two_hist=sorted(Counter(basin[a] for a in twos).items()), entries=sorted(Counter((first[s],period[s]) for s in range(N)).items()))

if __name__=='__main__':
 for k in range(4):
  for B in combinations(hub,k):
   r=calc(B)
   print('B',B, 'fixed',r['fixed'],'twos',r['twos'],'T',r['max_entry'],'basins',r['basin0'],r['basin1'],'fixedbasin',r['fixed_basin'])
   print('  fixedhist',r['fixed_hist']);print('  twohist',r['two_hist']); print('  classes',r['entries'])
