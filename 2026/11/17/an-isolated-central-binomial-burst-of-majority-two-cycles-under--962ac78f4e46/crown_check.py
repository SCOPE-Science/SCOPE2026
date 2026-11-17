#!/usr/bin/env python3
"""Independent exact case enumeration for odd-degree-parameter crown networks."""
from exact_certificate import LEVELS,map_level,level_rows,feasible_exact
from itertools import product

def red(a,b):
 c=a[3]
 return ((a[0]-c,a[1]-c,a[2]-c,a[4]+2*c),b-c)

def check():
 tried=0;good=[]
 for a,b,c,d in product(LEVELS,repeat=4):
  T,_,_=map_level(a,b); U,_,_=map_level(c,d)
  for mask in range(1,16):
   m=tuple(j for j in range(4) if mask>>j&1)
   if any(U[T[j]]!=j for j in m):continue
   if all(T[j]==j for j in m):continue
   tried+=1
   ac=(0,0,1,1,0);bc=(0,1,0,1,0)
   a1=tuple(int(T[j]>=2) for j in range(4))+(0,)
   b1=tuple(int(T[j]%2==1) for j in range(4))+(0,)
   rows=[((0,0,0,0,-1),-1)]
   for j in range(4):
    z=tuple(int(j==i) for i in range(4))+(0,)
    if mask>>j&1:rows.append((tuple(-v for v in z),-1))
    else:rows.extend(((z,0),(tuple(-v for v in z),0)))
   for lev,co in ((a,ac),(b,bc),(c,a1),(d,b1)):
    rows.extend(level_rows(lev,co))
   rows=[red(*r) for r in rows]
   if feasible_exact(rows):good.append((a,b,c,d,m))
 print('crown candidate-support systems',tried,'real-feasible',len(good))
 for row in good:print(*row)
if __name__=='__main__':check()
