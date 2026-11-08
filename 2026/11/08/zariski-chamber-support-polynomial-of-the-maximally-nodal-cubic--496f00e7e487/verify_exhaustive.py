from itertools import combinations
from fractions import Fraction
from collections import Counter

V=list(combinations(range(4),2))
D=[]
for e in V:
 m=[0]*len(V);m[V.index(e)]=-1
 D.append((f'E{e}',(0,*m)))
for partition in [(0,1),(0,2),(0,3)]:
 complement=tuple(i for i in range(4) if i not in partition)
 m=[0]*len(V)
 for e in [tuple(sorted(partition)),complement]:m[V.index(e)]=1
 D.append((f'R{partition}',(1,*m)))
for i in range(4):
 m=[int(i in e) for e in V]
 D.append((f'L{i}',(1,*m)))

def pairing(x,y):return x[0]*y[0]-sum(a*b for a,b in zip(x[1:],y[1:]))
M=[[pairing(v,w) for _,w in D] for _,v in D]
print('curves=',len(D),[(nm,M[i][i]) for i,(nm,_) in enumerate(D)])

def negative_definite(ids):
 L=[];diag=[]
 for i,v in enumerate(ids):
  row=[]
  for j in range(i):
   x=Fraction(-M[v][ids[j]])
   for k in range(j):x-=row[k]*L[j][k]*diag[k]
   row.append(x/diag[j])
  x=Fraction(-M[v][v])-sum(row[k]*row[k]*diag[k] for k in range(i))
  if x<=0:return False
  diag.append(x);row.append(Fraction(1));L.append(row)
 return True

counts=Counter();rflags=Counter();nflags=Counter();good=[]
for mask in range(1<<len(D)):
 ids=[i for i in range(len(D)) if mask>>i&1]
 if negative_definite(ids):
  counts[len(ids)]+=1
  rflags[(bool(mask & ((1<<9)-(1<<6))),len(ids))]+=1
  nflags[(sum(bool(mask&(1<<i)) for i in range(9,13)),len(ids))]+=1
  good.append(mask)
print('count=',len(good),'distribution=',[counts[k] for k in range(max(counts)+1)])
print('R=',rflags)
print('L_count_total=',[(k,sum(v for (kk,t),v in nflags.items() if kk==k)) for k in range(5)])
print('maximum=',max(counts),'max supports=',counts[max(counts)])
print('ALL_CHECKS_PASSED')
