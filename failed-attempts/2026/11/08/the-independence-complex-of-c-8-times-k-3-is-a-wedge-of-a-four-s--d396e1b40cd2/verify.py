"""Reproduce an exact integral discrete-Morse certificate for Ind(C8 x K3).

The 24 vertices use bit 3*i+c, where i is the cyclic position modulo
8 and c is the color in {0,1,2}. Requires only the Python standard library.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
from math import comb
import sys
sys.setrecursionlimit(50000)
n,m=8,3
allow=lambda a,b: a==0 or b==0 or (a==b and a.bit_count()==1)
faces=[]
def rec(states,mask):
 if len(states)==n:
  if allow(states[-1],states[0]):faces.append(mask)
  return
 for st in range(1<<m):
  if states and not allow(states[-1],st):continue
  rec(states+[st],mask|(st<<(m*len(states))))
rec([],0)
assert len(faces)==18722
F=set(faces)
# Independent reconstruction directly from all 24 graph adjacency masks.
neighbors=[]
for i in range(n):
 for c in range(m):
  nb=0
  for j in ((i-1)%n,(i+1)%n):
   for d in range(m):
    if d!=c: nb|=1<<(m*j+d)
  neighbors.append(nb)
direct={0}
for v in range(n*m):
 additions={s|(1<<v) for s in direct if not(s&neighbors[v])}
 direct.update(additions)
assert direct==F,(len(direct),len(F),len(direct^F))
print('DIRECT_ADJACENCY_FACE_CROSSCHECK_OK',len(direct))
order=[m*i+j for j in range(m) for i in range(n)]
remaining=F.copy()
paired_low={};paired_high={}
for v in order:
 bit=1<<v
 lows=[a for a in sorted(remaining) if not (a&bit) and a|bit in remaining]
 for a in lows:
  b=a|bit
  remaining.remove(a);remaining.remove(b)
  paired_low[a]=b;paired_high[b]=a
assert 0 in paired_low
base=paired_low[0]
nonempty_low={a:b for a,b in paired_low.items() if a!=0}
nonempty_high={b:a for b,a in paired_high.items() if a!=0}
crit=set(remaining)|{base}
print('FACES',len(faces),'MATCH_PAIRS_EXCLUDING_EMPTY',len(nonempty_low),'CRITICAL',len(crit),dict(sorted(Counter(a.bit_count()-1 for a in crit).items())))
assert Counter(a.bit_count()-1 for a in crit)==Counter({0:1,4:1,5:3})
# Verify no directed cycles in the entire, non-augmented Hasse diagram.
adj={a:[] for a in F if a!=0}
indeg={a:0 for a in adj}
num_edges=0
for hi in adj:
 rem=hi
 while rem:
  bt=rem&-rem;rem-=bt
  low=hi^bt
  if not low:continue
  if nonempty_low.get(low)==hi:
   adj[low].append(hi);indeg[hi]+=1
  else:
   adj[hi].append(low);indeg[low]+=1
  num_edges+=1
queue=deque(x for x in indeg if indeg[x]==0)
seen=0
while queue:
 a=queue.popleft();seen+=1
 for b in adj[a]:
  indeg[b]-=1
  if indeg[b]==0:queue.append(b)
assert seen==len(adj),(seen,len(adj))
print('GRADIENT_DAG_OK',seen,num_edges)

def boundary(face):
 out=[];t=0;bits=face
 while bits:
  bt=bits&-bits;bits-=bt
  out.append((face^bt,(-1)**t));t+=1
 return out
crit4=[x for x in crit if x.bit_count()==5]
crit5=[x for x in crit if x.bit_count()==6]
assert len(crit4)==1 and len(crit5)==3
c4=crit4[0]
@lru_cache(None)
def gradient_value(tau):
 if tau==c4:return 1
 if tau not in nonempty_low:return 0
 hi=nonempty_low[tau]
 if hi.bit_count()!=6:return 0
 b=boundary(hi)
 piv=next(sign for low,sign in b if low==tau)
 return -sum(sign*gradient_value(low) for low,sign in b if low!=tau)//piv
coeffs=[sum(sign*gradient_value(low) for low,sign in boundary(x)) for x in sorted(crit5)]
print('SIGNED_INTEGER_MORSE_BOUNDARY',coeffs,'critical4',c4,'critical5',sorted(crit5),'gradient_cache',gradient_value.cache_info())
assert coeffs==[0,0,0]
# independent mod-2 boundary-rank calculation for all dimensions
by_card={k:sorted(x for x in F if x.bit_count()==k) for k in range(13)}
rank={}
for k in range(1,13):
 ix={v:i for i,v in enumerate(by_card[k-1])}
 basis={}
 for s in by_card[k]:
  col=0
  for face,_ in boundary(s):col^=1<<ix[face]
  while col:
   pivot=col.bit_length()-1
   if pivot in basis:col^=basis[pivot]
   else:basis[pivot]=col;break
 rank[k]=len(basis)
# augmented reduced boundary for k=1 already in ranks: dim of C_{k-1} counts k-vertex faces.
# For reduced homology: beta_{k-1}=dim(C_{k-1})-rank(d_{k-1})-rank(d_k), with rank d_-? here rank[k] maps k-element to k-1-element.
betas={k-1:len(by_card[k])-rank.get(k,0)-rank.get(k+1,0) for k in range(1,13)}
print('MOD2_REDUCED_BETTI', {j:v for j,v in betas.items() if v})
assert {j:v for j,v in betas.items() if v}=={4:1,5:3}
print('VERIFY_OK faces',len(F),'matching_pairs',len(nonempty_low),'DAG',num_edges,'integer_morse_zero','mod2',betas[4],betas[5])
