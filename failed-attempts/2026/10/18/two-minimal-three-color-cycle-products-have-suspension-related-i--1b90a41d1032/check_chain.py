#!/usr/bin/env python3
"""Independent exact integral cellular-chain cancellation check for two finite graphs."""
from collections import defaultdict

def product_graph(m,n):
 adj=[0]*(m*n)
 for i in range(m):
  for a in range(n):
   for d in (-1,1):
    for b in range(n):
     if b!=a:adj[i*n+a]|=1<<(((i+d)%m)*n+b)
 return adj

def faces(adj):
 output=defaultdict(list)
 def rec(mask,available,count):
  if mask:output[count].append(mask)
  while available:
   bit=available&-available;available^=bit
   vertex=bit.bit_length()-1
   rec(mask|bit, available & ~adj[vertex], count+1)
 rec(0,(1<<len(adj))-1,0)
 return output

from collections import Counter,deque
import time,sys,json

def reduce(m,n,verbose=True,writecert=None):
 t=time.monotonic(); ff=faces(product_graph(m,n)); cells=[mask for k in sorted(ff) for mask in ff[k]]; N=len(cells)
 ids={mask:i for i,mask in enumerate(cells)}
 dims=[x.bit_count()-1 for x in cells]; bd=[{} for _ in cells]; cb=[set() for _ in cells]
 for i,mask in enumerate(cells):
  if dims[i]==0:continue
  p=0;bitset=mask
  while bitset:
   b=bitset&-bitset;bitset-=b;j=ids[mask^b];a=1 if (p%2==0) else -1
   bd[i][j]=a;cb[j].add(i);p+=1
 alive=set(range(N)); changes=deque();logs=[];scores=Counter()
 for j in alive:
  if len(cb[j])==1: changes.append(('col',j))
  if len(bd[j])==1: changes.append(('row',j))
 for step in range(N//2):
  chosen=None
  while changes:
   typ,v=changes.popleft()
   if v not in alive:continue
   if typ=='col' and len(cb[v])==1:
    i=next(iter(cb[v]));a=bd[i][v]
    if abs(a)==1:chosen=(i,v,a);break
   if typ=='row' and len(bd[v])==1:
    j=next(iter(bd[v]));a=bd[v][j]
    if abs(a)==1:chosen=(v,j,a);break
  if chosen is None:
   best_score=10**12
   for j in alive:
    cj=cb[j]
    if not cj:continue
    for i in cj:
     a=bd[i][j]
     if abs(a)!=1:continue
     s=(len(bd[i])-1)*(len(cj)-1)
     if s<best_score:chosen=(i,j,a);best_score=s
  if chosen is None:break
  i,j,a=chosen
  assert i in alive and j in alive and i!=j
  score=(len(bd[i])-1)*(len(cb[j])-1);scores[score]+=1
  for ii in list(cb[j]):
   if ii==i:continue
   c=bd[ii][j];ratio=c//a
   for jj,x in bd[i].items():
    if jj==j:continue
    old=bd[ii].get(jj,0);new=old-ratio*x
    if new==0:
     if old:del bd[ii][jj];cb[jj].remove(ii)
    else:bd[ii][jj]=new;cb[jj].add(ii)
    if len(cb[jj])==1:changes.append(('col',jj))
   del bd[ii][j];cb[j].remove(ii)
   if len(bd[ii])==1:changes.append(('row',ii))
  for k in list(cb[i]):
   del bd[k][i]
   if len(bd[k])==1:changes.append(('row',k))
  for jj in bd[i]:
   cb[jj].discard(i)
   if len(cb[jj])==1:changes.append(('col',jj))
  for jj in bd[j]:
   cb[jj].discard(j)
   if len(cb[jj])==1:changes.append(('col',jj))
  cb[i].clear();cb[j].clear();bd[i].clear();bd[j].clear();alive.remove(i);alive.remove(j)
  logs.append((cells[i],cells[j],a,score))
  if step%500==0 and verbose:print(step,'remaining',len(alive),'time',round(time.monotonic()-t,2),flush=True)
 remain=sorted(alive)
 if verbose:print('COMPLETE',m,n,'facecounts',[(k,len(f)) for k,f in sorted(ff.items())], 'alive',len(alive),'dims',Counter(dims[i] for i in alive),'nonzero',[(dims[i],[(cells[j],a) for j,a in bd[i].items()]) for i in remain if bd[i]],'pivot_score',scores,'elapsed',round(time.monotonic()-t,2),flush=True)
 if writecert:
  with open(writecert,'w') as f:json.dump(dict(m=m,n=n,face_counts={str(k):len(v) for k,v in ff.items()},pivots=[[i,j,a] for i,j,a,s in logs],remaining=[cells[i] for i in remain],remaining_boundaries={str(cells[i]):{str(cells[j]):a for j,a in bd[i].items()} for i in remain if bd[i]}),f,separators=(',',':'))
 return cells,dims,bd,alive,logs
if __name__=='__main__':
 for m,expected in ((7,{0:1,3:1,4:3}),(8,{0:1,4:1,5:3})):
  cells,dims,bd,alive,logs=reduce(m,3,False)
  from collections import Counter
  actual=dict(Counter(dims[i] for i in alive))
  assert actual==expected,(m,actual,expected)
  assert not any(bd[i] for i in alive)
  assert len(cells)==(5281 if m==7 else 18721)
  print('CHAIN_OK',m,'faces',len(cells),'unit_pivots',len(logs),'remaining',actual)

