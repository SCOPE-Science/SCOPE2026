#!/usr/bin/env python3
"""Exhaustive F2-line incidence and exact Picard Gram checker."""
from itertools import combinations, product

def contains(u,v):
 p=lambda i,j:(u[i]*v[j]+u[j]*v[i])%2
 a,b,c,d=p(0,1),p(1,2),p(2,3),p(3,0)
 A=(u[1]*a+u[2]*b+u[3]*c+(u[0]+u[3])*d)%2
 B=(v[1]*a+v[2]*b+v[3]*c+(v[0]+v[3])*d)%2
 return A==B==0

def rref_lines():
 for i,j in combinations(range(4),2):
  pos=[(row,col) for row,p in enumerate((i,j)) for col in range(p+1,4) if col not in (i,j)]
  for bits in product((0,1),repeat=len(pos)):
   a=[[0]*4 for _ in range(2)];a[0][i]=a[1][j]=1
   for (row,col),val in zip(pos,bits):a[row][col]=val
   yield tuple(a[0]),tuple(a[1])

def nonzero_points(line):
 u,v=line
 return frozenset((u,v,tuple(a^b for a,b in zip(u,v))))

def det(a):
 from fractions import Fraction
 m=[[Fraction(x) for x in row] for row in a]; out=Fraction(1)
 for i in range(len(m)):
  k=next((j for j in range(i,len(m)) if m[j][i]),None)
  assert k is not None
  if k!=i:m[i],m[k]=m[k],m[i];out=-out
  p=m[i][i];out*=p
  for j in range(i+1,len(m)):
   d=m[j][i]/p
   for c in range(i+1,len(m)):m[j][c]-=d*m[i][c]
   m[j][i]=0
 return int(out)

def main():
 all_lines=list(rref_lines());assert len(all_lines)==35 and len(set(all_lines))==35
 lines=[L for L in all_lines if contains(*L)]
 assert len(lines)==5,lines
 names=['1001/0101','1010/0111','1011/0110','1000/0010','0100/0001']
 expected=[(tuple(int(x) for x in s.split('/')[0]),tuple(int(x) for x in s.split('/')[1])) for s in names]
 assert set(lines)==set(expected),lines
 intersections={(i,j) for i,j in combinations(range(5),2) if nonzero_points(expected[i]) & nonzero_points(expected[j])}
 assert intersections=={(0,4),(1,2),(1,3)},intersections
 M=[[4]+[1]*5]
 for i in range(5):M.append([1]+[(-2 if i==j else int(tuple(sorted((i,j))) in intersections)) for j in range(5)])
 assert det(M)==-132,det(M)
 assert [sum(tuple(sorted((i,j))) not in intersections for j in range(5) if j!=i) for i in range(5)]==[3,2,3,3,3]
 print('PASS 35 exhaustive RREF lines; 5 contained; graph A3+A2; matrix det -132; section counts (3,2,3,3,3)')
if __name__=='__main__':main()
