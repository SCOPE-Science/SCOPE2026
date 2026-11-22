#!/usr/bin/env python3
"""Independent on-demand BFS test for all subsets and relocation graphs."""
import hashlib
import itertools
import json
from collections import Counter,deque

EXPECTED={
5:{'valid':[1,10,45,110,115,30], 'max':[0,0,0,0,10,30], 'min':4,
   'slide':(0,10,0,0),'jump':(10,1,5,5)},
6:{'valid':[1,12,66,208,351,252,2], 'max':[0,0,0,0,0,240,2], 'min':5,
   'slide':(816,1,6,7),'jump':(1842,1,5,5)} }

def solve(n):
 N=2*n
 A=[[False]*N for _ in range(N)]
 for r in range(2):
  for c in range(n):
   u=n*r+c
   for v in [n*r+(c-1)%n,n*r+(c+1)%n,n*(1-r)+c]:
    A[u][v]=True
 def reach(a,b,S):
  # Two entirely separate BFS runs. Exactly the original graph distance must be reached
  # using a geodesic with all interior selected vertices forbidden.
  def bfs(allowed):
   D=[-1]*N;D[a]=0;q=deque([a])
   while q:
    v=q.popleft()
    if v==b:return D[v]
    for w in range(N):
     if A[v][w] and allowed(w) and D[w]<0:
      D[w]=D[v]+1;q.append(w)
   return -1
  d=bfs(lambda w: True)
  e=bfs(lambda w: w==b or w==a or not (S>>w&1))
  return d==e
 valid=[]
 for S in range(1<<N):
  selected=[i for i in range(N) if S>>i&1]
  valid.append(all(reach(a,b,S) for a,b in itertools.combinations(selected,2)))
 maxs=[]
 for S in range(1<<N):
  if not valid[S]:continue
  if not any(valid[S |(1<<v)] for v in range(N) if not(S>>v&1)):
   maxs.append(S)
 cc=Counter(S.bit_count() for S in range(1<<N) if valid[S]);mc=Counter(x.bit_count() for x in maxs)
 assert [cc[i] for i in range(N+1) if cc[i]]==EXPECTED[n]['valid']
 assert [mc[i] for i in range(max(EXPECTED[n]['min'],N)+1) if mc[i]]==[x for x in EXPECTED[n]['max'] if x]
 minsize=min(mc);OPT=sorted(x for x in maxs if x.bit_count()==minsize)
 status={}
 for typ in ('slide','jump'):
  AD={s:set() for s in OPT}
  for s in OPT:
   for t in OPT:
    if s>=t:continue
    d=s^t
    if d.bit_count()!=2:continue
    a=next(v for v in range(N) if d>>v&1 and s>>v&1)
    b=next(v for v in range(N) if d>>v&1 and t>>v&1)
    if typ=='slide' and not A[a][b]:continue
    AD[s].add(t);AD[t].add(s)
  seen=set();nc=0;ecc=[]
  for s in OPT:
   if s in seen:continue
   nc+=1;q=[s];seen.add(s)
   for t in q:
    for v in AD[t]:
     if v not in seen:seen.add(v);q.append(v)
  for s in OPT:
   D={s:0};q=deque([s])
   while q:
    u=q.popleft()
    for v in AD[u]:
     if v not in D:D[v]=D[u]+1;q.append(v)
   ecc.append(max(D.values()))
  ans=(sum(map(len,AD.values()))//2,nc,min(ecc),max(ecc))
  assert ans==EXPECTED[n][typ],(n,typ,ans)
  status[typ]=ans
 bit_sha=hashlib.sha256(bytes(int(v) for v in valid)).hexdigest()
 opt_sha=hashlib.sha256(','.join(map(str,OPT)).encode()).hexdigest()
 print(n,cc,mc,status,'feasible_bitset_sha256',bit_sha,'optimal_mask_sha256',opt_sha)
 return bit_sha,opt_sha
if __name__=='__main__':
 from pathlib import Path
 p=json.loads(Path(__file__).with_name('paths_results.txt').read_text().split('\nPATH_ENUMERATION_OK')[0])
 for n in (5,6):
  b,o=solve(n);q=next(x for x in p if x['n']==n)
  assert (b,o)==(q['feasible_bitset_sha256'],q['optimal_mask_sha256'])
 print('BFS_RECOMPUTATION_OK')
