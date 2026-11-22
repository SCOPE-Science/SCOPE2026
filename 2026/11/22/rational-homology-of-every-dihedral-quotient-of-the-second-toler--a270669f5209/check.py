from itertools import combinations
from math import comb

def signed_orbits(n,k):
 per=[[ (s*i+t)%n for i in range(n)] for s in (1,-1) for t in range(n)]
 out={}; eligible={}
 for sub in combinations(range(n),k):
  if k==4 and not any((a-b)%n in (1,n-1) for a,b in combinations(sub,2)):continue
  perms=[]
  for P in per:
   sub2=tuple(sorted(P[i] for i in sub));perms.append(sub2)
  key=min(perms)
  if key not in out:
   out[key]=1
   odd=False
   for P in per:
    if tuple(sorted(P[i] for i in sub))!=sub:continue
    pp=[sub.index(P[i]) for i in sub];par=sum(pp[i]>pp[j] for i in range(k) for j in range(i+1,k))%2
    if par:odd=True;break
   eligible[key]=not odd
 return sum(eligible.values()),len(out)

def c(n,k):return comb(n,k) if n>=k>=0 else 0
for n in range(4,31):
 a3,_=signed_orbits(n,3);a4,_=signed_orbits(n,4)
 form3=((n-3)**2+6)//12
 if n>=5:form4=(c(n-1,3)-c(n-5,3)+4*n-16-2*(n%2==0))//8
 else:form4=0
 assert (a3,a4)==(form3,form4),(n,a3,a4,form3,form4)
 print(n,a3,a4,a4-a3)
print('PASS')

from itertools import combinations
from collections import defaultdict
from math import comb
import sys

def rank_modp(cols,p):
 piv={}
 for col in cols:
  col=dict(col)
  while col:
   q=max(col)
   if q not in piv:
    k=pow(col[q],-1,p)
    piv[q]={i:v*k%p for i,v in col.items() if v%p};break
   f=col[q];
   for i,v in piv[q].items():
    w=(col.get(i,0)-f*v)%p
    if w:col[i]=w
    else:col.pop(i,None)
 return len(piv)

def build(n):
 perm=[[((s*i+t)%n) for i in range(n)] for s in [1,-1] for t in range(n)]
 maps=[]
 for P in perm:
  maps.append({m:sum(1<<P[i] for i in range(n) if (m>>i)&1) for m in range(1,1<<n) if m.bit_count()<=4})
 faces={k:[] for k in range(1,5)}
 for k in range(1,5):
  for v in combinations(range(n),k):
   m=sum(1<<i for i in v)
   if k<=3 or any((a-b)%n in (1,n-1) for a,b in combinations(v,2)):
    faces[k].append(m)
 orbit={};canon={}
 for k in faces:
  for f in faces[k]:
   canon[f]=min(M[f] for M in maps)
 def chains(d):
  seen={}
  def insert(flags):
   c=min(tuple(M[x] for x in flags) for M in maps)
   seen[c]=True
  def rec(flags, avail):
   if len(flags)==d+1:
    insert(flags);return
   x=flags[-1]
   for k in range(x.bit_count()+1,5):
    for y in faces[k]:
     if x & y==x:
      rec(flags+[y],None)
  for k in range(1,5):
   for f in faces[k]: rec([f],None)
  return sorted(seen)
 cs=[]
 for d in range(4):
  cs.append(chains(d))
 idx=[{v:i for i,v in enumerate(c)} for c in cs]
 Bs=[]
 for d in range(1,4):
  cols=[]
  for flag in cs[d]:
   col=defaultdict(int)
   for i in range(d+1):
    sub=flag[:i]+flag[i+1:]
    key=min(tuple(M[x] for x in sub) for M in maps)
    col[idx[d-1][key]]+=(-1)**i
   cols.append({k:v for k,v in col.items() if v})
  Bs.append(cols)
 return cs,Bs
def cchoose(n,k):return comb(n,k) if n>=k>=0 else 0
if __name__=='__main__':
 for n in range(4,14):
  cs,Bs=build(n)
  c=[len(x) for x in cs]
  r=[0]+[rank_modp(B,p) for B,p in zip(Bs,[1009]*3)]+[0]
  b=[c[i]-r[i]-r[i+1] for i in range(4)]
  r2=[0]+[rank_modp(B,2) for B in Bs]+[0]
  b2=[c[i]-r2[i]-r2[i+1] for i in range(4)]
  expected = 0 if n==4 else (cchoose(n-1,3)-cchoose(n-5,3)+4*n-16-2*(n%2==0))//8-((n-3)**2+6)//12
  assert b==[1,0,0,expected], (n,b,expected)
  print(n, 'c',c,'r',r[1:4],'hom',b,'mod2',b2, flush=True)
