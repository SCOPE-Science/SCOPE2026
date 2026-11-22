#!/usr/bin/env python3
"""Independent explicit mismatch witnesses, in an order-twelve connected cubic bipartite graph."""
ROW=(7,11,21,44,50,56)
N=12
NB=[[] for _ in range(N)]
for i,r in enumerate(ROW):
 for j in range(6):
  if r & (1<<j): NB[i].append(j+6);NB[j+6].append(i)
def step(x,mode):
 y=[0]*N
 for v,c in enumerate(x):
  if mode=='CCA':y[v]=(c+1)%3 if any(x[w]==(c+1)%3 for w in NB[v]) else c
  else:y[v]= (c+1)%3 if c>0 or any(x[w]==1 for w in NB[v]) else 0
 return tuple(y)
def describe(x,mode):
 pos={}; seq=[]
 while x not in pos:
  pos[x]=len(seq);seq.append(x);x=step(x,mode)
 return pos[x],len(seq)-pos[x]
def decode(n):return tuple(n//(3**i)%3 for i in range(N))
if __name__=='__main__':
 seen={}
 for code in range(3**N):
  x=decode(code);p=describe(x,'CCA')[1];q=describe(x,'GHM')[1]
  if (p,q) in ((8,4),(10,5)) and (p,q) not in seen:
   seen[(p,q)]=(code,describe(x,'CCA'),describe(x,'GHM'))
  if len(seen)==2:break
 for pair,w in sorted(seen.items()):print('periods',pair,'base3',w)
 assert len(seen)==2
