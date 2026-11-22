#!/usr/bin/env python3
"""Independent direct subsequence containment versus rectangular partition polynomial for a^r b a b."""
from itertools import combinations
from math import comb
from collections import defaultdict

def contains(word,pat):
 j=0
 for c in word:
  if j<len(pat) and c==pat[j]:j+=1
 return j==len(pat)

def rectangle(h,w):
 # partition polynomial of h rows and maximum part w
 p=[1]
 for _ in range(h):
  new=[]
  for _ in range(w):
   pass
 # recursion over monotone partitions independent of direct word generation
 out=defaultdict(int)
 def rec(i,cap,weight):
  if i==h:out[weight]+=1;return
  for x in range(cap+1):rec(i+1,x,weight+x)
 rec(0,w,0)
 return dict(out)

def predicted(A,B,r):
 out=defaultdict(int);out[0]=1
 for m in range(1,min(A,r-1)+1):
  for wt,v in rectangle(m,B-1).items():out[m+wt]+=v
 for m in range(r,A+1):
  for v in range(1,B+1):
   for wt,num in rectangle(r-1,B-v).items():out[m*v+wt]+=num
 return dict(out)

checks=0
for n in range(0,15):
 for A in range(n+1):
  B=n-A
  words=[''.join('a' if i in pos else 'b' for i in range(n)) for pos in combinations(range(n),A)]
  for r in range(2,7):
   pattern='a'*r+'bab'
   actual=defaultdict(int)
   for w in words:
    if not contains(w,pattern):
     C=sum(w[i]=='a' and w[j]=='b' for i in range(n) for j in range(i+1,n))
     actual[C]+=1
   exp=predicted(A,B,r)
   assert dict(actual)==exp,('polynomial',A,B,r,dict(actual),exp)
   total=sum(exp.values())
   if A>=r:
    closed=comb(B+r-1,r-1)+(A-r+1)*comb(B+r-1,r) if B else 1
   else:closed=comb(A+B,A)
   assert total==closed,(A,B,r,total,closed)
   checks+=1
print('DIRECT_MATCH',checks,'composition-pattern cases, n<=14, r=2..6')
print('EXAMPLE_A4_B4_R2',sorted(predicted(4,4,2).items()))
for r in range(2,7):
 for A in range(r+1,9):
  for B in range(2,9):
   assert predicted(A,B,r).get(A*B-1,0)==0
print('NEAR_MAX_UNIVERSAL_OK')
