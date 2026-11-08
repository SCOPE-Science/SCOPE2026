from itertools import product
from collections import Counter

def mul(a,b):
 r=0
 for _ in range(2):
  if b&1:r^=a
  b>>=1; a<<=1
  if a&4:a^=7
 return r

def power(a,n):
 r=1
 while n:
  if n&1:r=mul(r,a)
  a=mul(a,a);n>>=1
 return r

def inv(a):return power(a,2) if a else None

def divmodp(a,b):
 a=a[:]
 while a and a[-1]==0:a.pop()
 while b and b[-1]==0:b.pop()
 if not b:raise ZeroDivisionError
 q=[0]*(max(0,len(a)-len(b)+1))
 while len(a)>=len(b):
  j=len(a)-len(b); h=mul(a[-1],inv(b[-1]));q[j]=h
  for i,bi in enumerate(b):a[i+j]^=mul(h,bi)
  while a and not a[-1]:a.pop()
 return q,a

def sqfree(a):
 f=list(a)+[1]; d=[f[i] if i%2 else 0 for i in range(1,8)]
 while d and not d[-1]:d.pop()
 while d:
  _,rem=divmodp(f,d);f,d=d,rem
 return len(f)==1

def rank(M):
 m=[r[:] for r in M]; rows=len(m);n=len(m[0]);pivot=0
 for j in range(n):
  i=next((i for i in range(pivot,rows) if m[i][j]),None)
  if i is None:continue
  m[i],m[pivot]=m[pivot],m[i]
  t=inv(m[pivot][j]);m[pivot]=[mul(x,t) for x in m[pivot]]
  for i in range(rows):
   if i!=pivot and m[i][j]:
    t=m[i][j];m[i]=[x^mul(t,y) for x,y in zip(m[i],m[pivot])]
  pivot+=1
  if pivot==rows:break
 return pivot

def matrix(a):
 # order (v0,v1,w0,w1,w2,w3)
 A=[power(a[1],2),power(a[3],2),power(a[5],2),1]
 B=[power(a[0],2),power(a[2],2),power(a[4],2),power(a[6],2)]
 M=[[0]*6 for _ in range(6)]
 for i in range(4):M[i+2][0]=A[i];M[i+2][1]=B[i]
 M[0][3]=1;M[1][5]=1
 return M

def twisted(A,B):
 # columns = A B^{(sqrt)} since C(Mv) gives M sigma(coeff)
 return [[sumxor([mul(A[i][k],power(B[k][j],2)) for k in range(len(B))]) for j in range(len(B[0]))] for i in range(len(A))]

def sumxor(items):
 r=0
 for x in items:r^=x
 return r

def seq(a):
 M=matrix(a);T=M;r=[]
 for n in range(1,7):
  r.append(rank(T));T=twisted(M,T)
 return tuple(r)

counts=Counter();fails=[];total=0;examples={}
for a in product(range(4),repeat=7):
 if not sqfree(a):continue
 total+=1
 delta=a[2]^mul(a[3],a[6]); eps=a[3]^power(a[6],4)
 target=(4,)*6 if delta else ((4,3,2,2,2,2) if eps else (4,3,2,1,0,0))
 actual=seq(a);kind=4 if delta else (2 if eps else 0)
 counts[kind]+=1
 examples.setdefault(kind,a)
 if target!=actual:fails.append((a,target,actual))
print('squarefree:',total,'counts:',dict(sorted(counts.items())),'examples:',examples,'failures:',fails[:3]);assert not fails
