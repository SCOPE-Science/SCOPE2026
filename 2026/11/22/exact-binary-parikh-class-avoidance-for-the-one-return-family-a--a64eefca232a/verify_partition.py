#!/usr/bin/env python3
"""Second approach: enumerate bounded Ferrers rows, detect pattern via strict drop after row r."""
from collections import defaultdict
from math import comb


def rows(A,B):
 def f(pref,cap):
  if len(pref)==A:
   yield tuple(pref)
   return
  for val in range(cap,-1,-1):
   yield from f(pref+[val],val)
 yield from f([],B)

def is_avoiding(lam,r):
 positive=[x for x in lam if x>0]
 return len(positive)<=r or len(set(positive[r-1:]))==1

def polynomial(A,B,r):
 out=defaultdict(int)
 for lam in rows(A,B):
  if is_avoiding(lam,r):out[sum(lam)]+=1
 return dict(out)

def gaussian(n,k):
 # exact q-binomial coefficients with recurrence
 if k<0 or k>n:return [0]
 pol={(0,0):[1]}
 for i in range(1,n+1):
  for j in range(0,min(i,k)+1):
   if j==0:pol[i,j]=[1];continue
   a=pol.get((i-1,j),[0]);b=pol[i-1,j-1];s=i-j
   arr=[0]*max(len(a),len(b)+s)
   for x,v in enumerate(a):arr[x]+=v
   for x,v in enumerate(b):arr[x+s]+=v
   pol[i,j]=arr
 return pol[n,k]

def proposed(A,B,r):
 out=defaultdict(int);out[0]=1
 for m in range(1,min(A,r-1)+1):
  for w,v in enumerate(gaussian(B+m-1,m)):
   if v:out[m+w]+=v
 for m in range(r,A+1):
  for v in range(1,B+1):
   for w,x in enumerate(gaussian(B-v+r-1,r-1)):
    if x:out[m*v+w]+=x
 return dict(out)

cases=0
for A in range(0,9):
 for B in range(0,9):
  for r in range(2,8):
   expected=proposed(A,B,r)
   observed=polynomial(A,B,r)
   assert expected==observed,(A,B,r,expected,observed)
   if A>=r:
    total=comb(B+r-1,r-1)+(A-r+1)*comb(B+r-1,r)
   else:total=comb(A+B,A)
   assert sum(expected.values())==total,(A,B,r,total)
   if A>=r+1 and B>=2:
    assert observed.get(A*B-1,0)==0
    assert observed.get(A*B,0)==1
   cases+=1
print('INDEPENDENT_FERRERS_MATCH',cases,'A,B<=8 r=2..7')
print('A4_B4_r2',sorted(proposed(4,4,2).items()))
