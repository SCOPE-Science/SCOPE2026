#!/usr/bin/env python3
"""Finite Coxeter Bruhat intervals and KL recursion: reproducible exact D5 bound census."""
from collections import deque, Counter, defaultdict
from itertools import permutations,product
from functools import lru_cache
import json,math

def plus(a,b):
 out=list(a)+[0]*max(0,len(b)-len(a))
 for i,v in enumerate(b):out[i]+=v
 while len(out)>1 and out[-1]==0:out.pop()
 return tuple(out)
def neg(a):return tuple(-x for x in a)
def mulq(a,pow=1):return (0,)*pow + a
def coeff(a,i):return a[i] if i>=0 and i<len(a) else 0
def scale(a,k):return tuple(k*c for c in a)
def multiply(a,b):
 o=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):o[i+j]+=x*y
 while len(o)>1 and o[-1]==0:o.pop()
 return tuple(o)
ZERO=(0,);ONE=(1,)

class Coxeter:
 def __init__(self,n=4,kind='D'):
  self.n=n;self.kind=kind;self.id=tuple(range(1,n+1))
  def right(w,i):
   w=list(w)
   if i==0:
    if kind=='D':w[0],w[1]=-w[1],-w[0]
    elif kind=='B':w[0]=-w[0]
    else:raise ValueError()
   else:w[i-1],w[i]=w[i],w[i-1]
   return tuple(w)
  if kind=='A':
   self.simple=tuple(range(1,n))
  else:self.simple=tuple(range(n))
  self.right=right
  self.words={self.id:()};self.length={self.id:0}
  q=deque([self.id])
  while q:
   w=q.popleft()
   for i in self.simple:
    v=right(w,i)
    if v not in self.words:
     self.words[v]=self.words[w]+(i,)
     self.length[v]=len(self.words[v]);q.append(v)
  self.order=sorted(self.words,key=lambda w:(self.length[w],w))
  self.pos={w:i for i,w in enumerate(self.order)}
  self.down={w:[i for i in self.simple if self.length[right(w,i)]<self.length[w]] for w in self.order}
  self.intervals={}
  for w in self.order:
   sub={self.id}
   for i in self.words[w]:sub |= {right(x,i) for x in tuple(sub)}
   assert w in sub
   self.intervals[w]=sub
  self.less=lambda x,w:x in self.intervals[w]
  assert len(self.order)=={'D':(2**(n-1))*math.factorial(n),'B':(2**n)*math.factorial(n),'A':math.factorial(n)}[kind]
  for w in self.order:
   for i in self.simple:
    assert abs(self.length[self.right(w,i)]-self.length[w])==1

 @lru_cache(None)
 def R(self,x,w):
  if x not in self.intervals[w]:return ZERO
  if x==w:return ONE
  s=self.down[w][0]
  v=self.right(w,s);xs=self.right(x,s)
  if self.length[xs]<self.length[x]:return self.R(xs,v)
  return plus(mulq(self.R(xs,v)),multiply((-1,1),self.R(x,v)))
 @lru_cache(None)
 def kl(self,x,w):
  if x not in self.intervals[w]:return ZERO
  if x==w:return ONE
  d=self.length[w]-self.length[x]
  t=ZERO
  for y in self.intervals[w]:
   if y==x or x not in self.intervals[y]:continue
   diff=self.length[y]-self.length[x]
   r=self.R(x,y)
   assert len(r)<=diff+1,(x,y,r)
   rev=tuple(reversed((r+(0,)*(diff+1-len(r)))))
   sign=(-1)**diff
   t=plus(t,scale(multiply(rev,self.kl(y,w)),sign))
  ans=tuple(-coeff(t,i) for i in range((d-1)//2+1))
  while len(ans)>1 and ans[-1]==0:ans=ans[:-1]
  lhs=plus(tuple(reversed(ans))+(0,)*(d+1-len(ans)),neg(ans)) if False else plus(mulq(tuple(reversed(ans)),d-(len(ans)-1)),neg(ans))
  assert lhs==t,(x,w,d,ans,t,lhs)
  assert ans[0]==1,(x,w,ans)
  assert all(c>=0 for c in ans),(x,w,ans)
  return ans
 def bar(self,w):
  L=self.length[w];p=[0]*(L+1)
  for x in self.intervals[w]:p[self.length[x]]+=1
  return p
 def info(self,w):
  p=self.bar(w);l=self.length[w]
  d=[p[l-i]-p[i] for i in range(l+1)]
  return p,d,self.kl(self.id,w)



def verify():
    """Complete type-D5 enumeration and independently check the essential identities."""
    # A type-A and an independent published type-D4 normalization check.
    S=Coxeter(4,'A')
    assert S.kl(S.id,(4,2,3,1))==(1,1)
    assert S.bar((4,2,3,1))==[1,3,5,6,4,1]
    H=Coxeter(4,'D')
    base=[w for w in H.order if H.length[w]==4 and H.kl(H.id,w)==(1,1)]
    assert len(base)==3 and all(H.bar(w)==[1,3,5,4,1] for w in base)
    G=Coxeter(5,'D')
    assert len(G.order)==1920
    assert max(G.length.values())==20
    longest=max(G.order,key=G.length.get)
    PW=G.bar(longest)
    assert PW[:5]==[1,5,14,30,54]
    # By intersection-cohomology duality and KL monotonicity,
    # any relevant minimal-singularity extremizer satisfies the necessary lower-degree bounds.
    eligible=[]
    for w in G.order:
        l=G.length[w]
        if l<=8:
            continue
        P=G.bar(w)
        d=[P[l-j]-P[j] for j in range(5)]
        if d[1]<=1 and d[2]<=5 and d[3]<=14:
            eligible.append((w,l,d))
    assert len(eligible)==572,len(eligible)
    max4=max(t[2][4] for t in eligible)
    assert max4==27,max4
    eq4=[(w,l,d) for w,l,d in eligible if d[4]==27]
    assert len(eq4)==7,len(eq4)
    eq3=[(w,G.length[w],G.bar(w)) for w in G.order
           if G.length[w]>6 and
              all(G.bar(w)[G.length[w]-j]-G.bar(w)[j]<=PW[j-1] for j in (1,2)) and
              G.bar(w)[G.length[w]-3]-G.bar(w)[3]>=PW[2]]
    assert len(eq3)==9,len(eq3)
    # Exact KL calculation from R-polynomial and bar-invariance recursions.
    kl3={w:G.kl(G.id,w) for w,l,P in eq3}
    winner={w for w,pol in kl3.items() if sum(pol)==2}
    a=(-1,-3,-4,2,-5)
    b=(-1,4,-2,-3,-5)
    assert winner=={a,b},winner
    assert {w for w,l,d in eq4 if sum(G.kl(G.id,w))==2}==winner
    def inverse(w):
        inv=[0]*len(w)
        for k,v in enumerate(w):
            inv[abs(v)-1]=(k+1)*(1 if v>0 else -1)
        return tuple(inv)
    assert inverse(a)==b and inverse(b)==a
    expected=[1,5,14,30,54,85,120,153,175,178,159,123,81,44,19,6,1]
    for w in (a,b):
        P=G.bar(w)
        assert G.length[w]==16
        assert P==expected
        D=[P[16-j]-P[j] for j in range(17)]
        assert D[:8]==[0,1,5,14,27,38,39,25]
        assert G.kl(G.id,w)==(1,1)
    # Cross-check R recursion with every available descent for the
    # seven degree-four possible extremizers, rather than only the fixed descent.
    for w,l,d in eq4:
        for x in G.intervals[w]:
            for s in G.down[w]:
                v=G.right(w,s)
                xs=G.right(x,s)
                if G.length[xs]<G.length[x]:
                    rhs=G.R(xs,v)
                else:
                    rhs=plus(mulq(G.R(xs,v)),multiply((-1,1),G.R(x,v)))
                assert rhs==G.R(x,w),(x,w,s,rhs,G.R(x,w))
    print('D5 group:',len(G.order),'longest:',20,'full-flag initial ranks:',PW[:5])
    print('degree-3 necessary candidates:',len(eq3),'degree-4 necessary candidates:',len(eq4))
    print('degree-4 bound-filter elements:',len(eligible),'maximum:',max4)
    for w,l,d in sorted(eq4):
        print('candidate:',w,'length:',l,'D[1..4]:',d[1:],'KL_id:',G.kl(G.id,w))
    print('sharp extremizers:',sorted(winner),'are inverse pair; PASS')

if __name__=='__main__':
    verify()
