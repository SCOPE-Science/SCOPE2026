#!/usr/bin/env python3
"""Independent exact exhaustive tests for rook-network Ising ground-state laws."""
from itertools import combinations
from fractions import Fraction
from math import gcd

def cut_opt(a,b,m):
 x,r=divmod(m,a);y,s=divmod(m,b)
 return (a-r)*x*(b-x)+r*(x+1)*(b-x-1)+(b-s)*y*(a-y)+s*(y+1)*(a-y-1)

def brute(a,b):
 n=a*b
 assert n<=16
 edges=[(i,j) for i in range(n) for j in range(i+1,n) if i//b==j//b or i%b==j%b]
 maxcut=[-1]*(n+1)
 refstates={}
 for mask in range(1<<n):
  mm=mask.bit_count()
  c=sum(((mask>>i)^(mask>>j))&1 for i,j in edges)
  if c>maxcut[mm]:maxcut[mm]=c
  rows=[sum(mask>>(i*b+j)&1 for j in range(b)) for i in range(a)]
  cols=[sum(mask>>(i*b+j)&1 for i in range(a)) for j in range(b)]
  balance=(max(rows)-min(rows)<=1 and max(cols)-min(cols)<=1)
  if c==cut_opt(a,b,mm):assert balance,(a,b,mask,rows,cols,c)
  if balance:assert c==cut_opt(a,b,mm)
 for mm in range(n+1):assert maxcut[mm]==cut_opt(a,b,mm),(a,b,mm,maxcut[mm],cut_opt(a,b,mm))
 e=len(edges); best=max(maxcut)
 expect=a*(b*b//4)+b*(a*a//4)
 assert best==expect,(a,b,best,expect)
 optimal_m={i for i,x in enumerate(maxcut) if x==best}
 if a%2 and b%2:
  low=(a*b-min(a,b))//2; high=(a*b+min(a,b))//2
  assert optimal_m==set(range(low,high+1)),(a,b,optimal_m)
 else:assert optimal_m=={n//2},(a,b,optimal_m)
 # Check field energy and optimizing sector for numerous rational fields.
 for t in (Fraction(-5),Fraction(-2),Fraction(-1,2),Fraction(0),Fraction(1,2),Fraction(2),Fraction(5)):
  energies=[e-2*c-t*(2*i-n) for i,c in enumerate(maxcut)]
  minE=min(energies)
  argmin={i for i,v in enumerate(energies) if v==minE}
  assert argmin=={i for i in range(n+1) if e-2*cut_opt(a,b,i)-t*(2*i-n)==minE}
 return best,sorted(optimal_m)

if __name__=='__main__':
 pairs=[(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4),(5,3)]
 for a,b in pairs:
  best,ms=brute(a,b)
  print(a,b,'MAXCUT',best,'MAGNETIZATIONS',[2*m-a*b for m in ms])
 print('EXHAUSTIVE_OK',len(pairs),'boards, field-sector and all row/column equality checks')
 # Cross-check the convex field envelope through moderately large rectangles
 for a in range(2,21):
  for b in range(2,19):
   cm=[cut_opt(a,b,m) for m in range(a*b+1)]
   assert all(x>=y for x,y in zip([cm[i+1]-cm[i] for i in range(len(cm)-1)],[cm[i+2]-cm[i+1] for i in range(len(cm)-2)]))
   assert max(cm)==a*(b*b//4)+b*(a*a//4)
 print('ENVELOPE_OK',19*17,'boards')
 for a in range(2,21):
  for b in range(2,21):
   jumps=[2*(m//a+m//b)-(a+b-2) for m in range(a*b)]
   assert len(set(jumps))==a+b-gcd(a,b),(a,b,len(set(jumps)))
   assert all(jumps[i+1]>=jumps[i] for i in range(len(jumps)-1))
 print('GCD_THRESHOLD_COUNT_OK',19*19,'boards')
