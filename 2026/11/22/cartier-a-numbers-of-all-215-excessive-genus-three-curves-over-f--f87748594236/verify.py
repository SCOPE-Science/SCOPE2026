#!/usr/bin/env python3
"""Exact, standalone Hasse--Witt and rational-point certificate for 215 genus-three quartics.
Run: python3 verify.py [coefficients.json]. Uses only Python's standard library.
The input is 15 coefficients per homogeneous quartic in descending lexicographic monomial order.
"""
import json,sys,collections
from pathlib import Path
ABC='0123456789abcdefghijklmnopqrstuv'
MOD={4:(1,1,1),8:(1,1,0,1),9:(2,2,1),16:(1,1,0,0,1),32:(1,0,1,0,0,1)}
class Field:
 def __init__(self,q):
  self.q=q;self.p=next(p for p in range(2,q+1) if q%p==0);self.k=0;n=q
  while n%self.p==0:self.k+=1;n//=self.p
  assert n==1
  self.mod=MOD.get(q,(0,1))
 def digits(self,x):return [(x//self.p**i)%self.p for i in range(self.k)]
 def rep(self,a):return sum((t%self.p)*self.p**i for i,t in enumerate(a))
 def add(self,a,b):
  if self.k==1:return (a+b)%self.p
  return self.rep([x+y for x,y in zip(self.digits(a),self.digits(b))])
 def neg(self,a):
  if self.k==1:return -a%self.p
  return self.rep([-x for x in self.digits(a)])
 def sub(self,a,b):return self.add(a,self.neg(b))
 def mul(self,a,b):
  if self.k==1:return a*b%self.p
  d=self.digits(a);e=self.digits(b);t=[0]*(2*self.k-1)
  for i,x in enumerate(d):
   for j,y in enumerate(e):t[i+j]=(t[i+j]+x*y)%self.p
  for i in range(2*self.k-2,self.k-1,-1):
   h=t[i]
   for j in range(self.k):t[i-self.k+j]=(t[i-self.k+j]-h*self.mod[j])%self.p
  return self.rep(t[:self.k])
 def pow(self,a,n):
  r=1
  while n:
   if n&1:r=self.mul(r,a)
   a=self.mul(a,a);n>>=1
  return r
 def inv(self,a):assert a!=0;return self.pow(a,self.q-2)
MON=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
assert len(MON)==15
BAS=((1,0,0),(0,1,0),(0,0,1))
def polymul(A,B,f):
 C={}
 for (a,b,c),x in A.items():
  for (d,e,g),y in B.items():
   m=(a+d,b+e,c+g);v=f.add(C.get(m,0),f.mul(x,y))
   if v:C[m]=v
   elif m in C:del C[m]
 return C
def poly_power(A,n,f):
 R={(0,0,0):1}
 while n:
  if n&1:R=polymul(R,A,f)
  n>>=1
  if n:A=polymul(A,A,f)
 return R
def rank(A,f):
 A=[a[:] for a in A];r=0
 for j in range(3):
  pivot=next((i for i in range(r,3) if A[i][j]),None)
  if pivot is None:continue
  A[r],A[pivot]=A[pivot],A[r]
  v=f.inv(A[r][j]);A[r]=[f.mul(x,v) for x in A[r]]
  for i in range(3):
   if i==r:continue
   m=A[i][j]
   if m:A[i]=[f.sub(x,f.mul(m,y)) for x,y in zip(A[i],A[r])]
  r+=1
 return r
def count_fq_points(F,f):
 q=f.q;total=0
 for x in range(q):
  for y in range(q):
   z=1;u=0
   for (i,j,k),c in F.items():u=f.add(u,f.mul(c,f.mul(f.pow(x,i),f.pow(y,j))))
   total+=(u==0)
 for x in range(q):
  u=0
  for (i,j,k),c in F.items():
   if k==0:u=f.add(u,f.mul(c,f.pow(x,i)))
  total+=(u==0)
 total+=(F.get((0,4,0),0)==0)
 return total

def main():
 p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('coefficients.json')
 data=json.loads(p.read_text('utf-8'));assert len(data)==15
 observed={};exceptions=[];total=0;missing=[]
 for qs in sorted(data,key=int):
  q=int(qs);f=Field(q);hist=collections.Counter()
  for ix,rec in enumerate(data[qs],1):
   assert len(rec)==15
   cs=[ABC.index(c) for c in rec];assert all(c<q for c in cs)
   A={m:v for m,v in zip(MON,cs) if v}
   P=poly_power(A,f.p-1,f)
   H=[[P.get(tuple(f.p*u[t]-v[t]+f.p-1 for t in range(3)),0) for v in BAS] for u in BAS]
   a=3-rank(H,f);hist[a]+=1;total+=1
   if a==2:exceptions.append({'q':q,'index':ix,'matrix':H,'encoded':rec})
   n=count_fq_points(A,f)
   if n!=0:missing.append((q,ix,n))
  observed[q]=[hist[0],hist[1],hist[2],hist[3]]
 expect={2:[2,2,0,0],3:[5,2,1,0],4:[15,6,0,0],5:[26,5,0,0],7:[28,4,0,0],8:[36,3,0,0],9:[18,6,3,0],11:[17,4,0,0],13:[11,0,0,0],16:[8,0,0,0],17:[7,0,0,0],19:[2,0,0,0],23:[2,0,0,0],29:[1,0,0,0],32:[1,0,0,0]}
 assert total==215 and observed==expect,(total,observed)
 assert len(exceptions)==4 and {(e['q'],e['index']) for e in exceptions}=={(3,5),(9,25),(9,26),(9,27)},exceptions
 assert missing==[],missing
 sums=[sum(row[i] for row in observed.values()) for i in range(4)]
 assert sums==[179,32,4,0]
 print('EXACT_QUARTIC_CARTIER_CENSUS_VERIFIED', 'total',total,'a_counts',sums)
 for q in sorted(observed):print('FIELD',q,'count',len(data[str(q)]),'a0_a1_a2_a3',observed[q])
 print('A2_EXCEPTIONS',json.dumps(exceptions,sort_keys=True))
 print('POINTLESS_CHECK all_215_zero_rational_points')
if __name__=='__main__':main()
