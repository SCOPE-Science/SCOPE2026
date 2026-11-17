#!/usr/bin/env python3
"""Exact integer Fourier--Motzkin proof for >=2 restored crown matching edges.
Variables are (t00,t01,t10,t11,q,r); n=2q+1, r unmatched pairs.
"""
from itertools import product
from math import gcd
LEVELS='LMPH'

def maps(a,b):
 def mp(old,mate,cat):
  return {'L':lambda:0,'H':lambda:1,'M':lambda:old if mate==0 else 0,'P':lambda:1 if mate==0 else old}[cat]()
 T=tuple(2*mp(j//2,j%2,b)+mp(j%2,j//2,a) for j in range(4))
 return T,int(b in 'PH'),int(a in 'PH')

def red(row):
 a,b=row;c=a[3]
 return (a[0]-c,a[1]-c,a[2]-c,a[4]+2*c,a[5]-c),b-c # t3=2q+1-r-t0-t1-t2

def simple(rows):
 unique={}
 for a,b in rows:
  g=0
  for v in (*a,b):g=gcd(g,abs(v))
  if g>1:a=tuple(v//g for v in a);b//=g
  if not any(a):
   if b<0:return None
  elif a not in unique or unique[a]>b:unique[a]=b
 return list(unique.items())

def feas(rows):
 rows=simple(rows)
 if rows is None:return False
 N=5
 while N:
  x=min(range(N),key=lambda j:sum(a[j]>0 for a,b in rows)*sum(a[j]<0 for a,b in rows))
  p=[(a,b) for a,b in rows if a[x]>0];m=[(a,b) for a,b in rows if a[x]<0]
  new=[(a[:x]+a[x+1:],b) for a,b in rows if a[x]==0]
  for a,b in p:
   for c,d in m:
    mul1=-c[x];mul2=a[x]
    new.append((tuple(mul1*a[j]+mul2*c[j] for j in range(N) if j!=x),mul1*b+mul2*d))
  rows=simple(new)
  if rows is None:return False
  N-=1
 return True

def level(cat,coef):
 c=list(coef);c[4]-=1
 if cat=='L':return [(tuple(c),-1)]
 if cat=='M':return [(tuple(c),0),(tuple(-v for v in c),0)]
 if cat=='P':return [(tuple(c),1),(tuple(-v for v in c),-1)]
 if cat=='H':return [(tuple(-v for v in c),-2)]

def make(a,b,a1,b1,x,y,T,X1,Y1,mask):
 rows=[((0,0,0,0,-1,0),-1),((0,0,0,0,0,-1),-2)]
 for j in range(4):
  v=tuple(int(j==z) for z in range(4))+(0,0)
  if mask>>j&1:rows.append((tuple(-t for t in v),-1))
  else:rows.extend(((v,0),(tuple(-t for t in v),0)))
 A0=(0,0,1,1,0,x); B0=(0,1,0,1,0,y)
 A1=tuple(int(T[j]>=2) for j in range(4))+(0,X1)
 B1=tuple(int(T[j]%2==1) for j in range(4))+(0,Y1)
 for cat,coef in ((a,A0),(b,B0),(a1,A1),(b1,B1)):
  rows.extend(level(cat,coef))
 return [red(z) for z in rows]

def run():
 tested=0;kept=[]
 for a,b,a1,b1 in product(LEVELS,repeat=4):
  T,X1,Y1=maps(a,b);U,X2,Y2=maps(a1,b1)
  for x,y in product((0,1),repeat=2):
   if (X2,Y2)!=(x,y):continue
   for mask in range(16):
    members=tuple(j for j in range(4) if mask>>j&1)
    if any(U[T[j]]!=j for j in members):continue
    if all(T[j]==j for j in members) and (X1,Y1)==(x,y):continue
    tested+=1
    rows=make(a,b,a1,b1,x,y,T,X1,Y1,mask)
    if feas(rows):kept.append((a,b,a1,b1,x,y,members,rows))
 print('tested',tested,'survive',len(kept))
 for a,b,a1,b1,x,y,m,rows in kept:print(a,b,a1,b1,x,y,m)
if __name__=='__main__':run()
