#!/usr/bin/env python3
"""Independent finite checks of the signed two-part-size function and its lag profile."""
from fractions import Fraction
from math import pi

def coeffs(N):
 s=[0]*(N+1); lamb=[0]*(N+1)
 for d in range(1,N+1):
  chi=1 if d%4==1 else -1 if d%4==3 else 0
  for j in range(d,N+1,d):
   s[j]+=d
   lamb[j]+=chi
 a=[0]*(N+1)
 for n in range(1,N+1):
  a4=s[n]-lamb[n]
  if n%2==0: a4-=2*s[n//2]
  if n%4==0: a4+=4*s[n//4]
  assert a4%4==0,(n,a4)
  a[n]=a4//4
 return a

def brute(n):
 total=0
 for x in range(1,n):
  for y in range(x+1,n):
   for r in range((n-x)//(2*x)+1):
    rem=n-(2*r+1)*x
    if rem>0 and rem%y==0 and (rem//y)%2==1:
     total+=(-1)**(r+(rem//y-1)//2)
 return total

def L2(t):
 return Fraction(1) if t==0 else Fraction(8,7)-Fraction(15,7*8**t)

def R(h):
 n=h
 if n%2==0:
  while n%2==0:n//=2
 q=3; ans=Fraction(1)
 while q*q<=n:
  if n%q==0:
   v=0
   while n%q==0:n//=q;v+=1
   ans*=sum((Fraction(1,q**(3*j)) for j in range(v+1)),Fraction(0))
  q+=2
 if n>1:ans*=1+Fraction(1,n**3)
 return ans

def target(h):
 t=0
 while h%2==0:h//=2;t+=1
 return float(Fraction(3,32)*L2(t)*R(h*2**t))

if __name__=='__main__':
 N=120000
 a=coeffs(N+30)
 for n in range(1,121):assert a[n]==brute(n),(n,a[n],brute(n))
 for h in [1,2,3,4,5,6,8,9,10,12,15,24,30]:
  calc=sum((a[n]/n)*(a[n+h]/(n+h)) for n in range(1,N+1))/N
  ref=target(h)
  assert abs(calc-ref)<0.0015,(h,calc,ref)
  print('lag',h,'empirical',round(calc,8),'limit',round(ref,8))
 m=sum(a[n]/n for n in range(1,N+1))/N
 assert abs(m-pi*pi/32)<0.001
 assert target(3)-pi**4/1024>0 and target(2)-pi**4/1024<0 and target(5)-pi**4/1024<0
 print('ARITHMETIC_LAG_CHECK_OK',120,13,'mean',round(m,8))
