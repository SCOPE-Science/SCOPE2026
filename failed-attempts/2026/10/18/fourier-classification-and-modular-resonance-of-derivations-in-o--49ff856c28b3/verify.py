#!/usr/bin/env python3
"""Finite-field check of a derivation calculation in cyclic quandle algebras."""
from math import gcd

def totient(n):
 return sum(gcd(j,n)==1 for j in range(1,n+1))

def divs(n):return [d for d in range(1,n+1) if n%d==0]

def order2(d):
 a,r=2%d,1
 while a!=1:
  a=a*2%d;r+=1
 return r

def dimension_formula(n,p):
 assert n%2 and (p==0 or gcd(n,p)==1)
 if p in (0,2):return 0
 count=0
 for d in divs(n):
  if d==1:continue
  r=order2(d)
  negative=(r%2==0 and pow(2,r//2,d)==d-1)
  good=pow(2,r,p)==1 and (not negative or pow(2,r//2,p)==p-1)
  if good:
   L=r if negative else 2*r
   assert totient(d)%L==0
   count+=totient(d)//L
 return count

def rank_derivation_system(n,p):
 # Sparse exact modular elimination of coefficient equations for D(e_x) = sum_z d[z,x] e_z.
 pivot={}
 for x in range(n):
  for y in range(n):
   for z in range(n):
    row={}
    def add(j,v):
     a=(row.get(j,0)+v)%p
     if a:row[j]=a
     else:row.pop(j,None)
    add(z*n+(2*y-x)%n,1)
    add(((2*y-z)%n)*n+x,-1)
    for a in range(n):
     if (2*a-x)%n==z:add(a*n+y,-1)
    while row:
     j=min(row)
     if j not in pivot:
      inv=pow(row[j],-1,p)
      row={k:inv*v%p for k,v in row.items() if v%p}
      pivot[j]=row
      break
     factor=row[j]
     for k,v in pivot[j].items():
      a=(row.get(k,0)-factor*v)%p
      if a:row[k]=a
      else:row.pop(k,None)
 return len(pivot)

def legendre(a,l):
 if a%l==0:return 0
 return 1 if pow(a%l,(l-1)//2,l)==1 else -1

def verify_legendre(l):
 assert l>3 and l%8==3
 c=[legendre(s,l)%3 for s in range(l)]
 for s in range(l):
  assert c[s]==(c[-s%l]+c[(s*pow(2,-1,l))%l])%3
 # The above coefficient equation, after shifting x,y, is precisely Leibniz on each basis pair.
 assert sum(c)%3==0
 return True

if __name__=='__main__':
 for n,p in [(3,2),(3,5),(5,2),(5,3),(7,3),(9,2),(11,3),(13,5)]:
  expected=dimension_formula(n,p)
  observed=n*n-rank_derivation_system(n,p)
  assert observed==expected,(n,p,observed,expected)
  print('rank PASS: n=%d characteristic=%d dimension=%d'%(n,p,expected))
 for l in (11,19,43,59):
  verify_legendre(l)
  print('Legendre derivation PASS: prime index',l,'dimension',dimension_formula(l,3))
 print('ALL CHECKS PASSED')
