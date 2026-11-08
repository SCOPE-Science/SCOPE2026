"""Exact and numerical checks for beta-binomial Dorfman pooling."""
from fractions import Fraction as F
from math import comb, log

checks=0

def eq(a,b):
 global checks
 assert a==b, (a,b)
 checks+=1

def qfrac(alpha,kappa,k):
 out=F(1)
 for j in range(k):out*= (kappa-alpha+j)/(kappa+j)
 return out

def rising(x,n):
 out=F(1)
 for i in range(n):out*=x+i
 return out

for kappa in (F(1,2),F(1),F(3,2),F(2),F(4),F(7)):
 for alpha in (kappa/F(20), kappa/F(5),kappa*F(4,5)):
  if alpha>=1:continue
  prevH=None
  for k in range(1,30):
   q=qfrac(alpha,kappa,k)
   from_moments=sum(((-1)**j)*comb(k,j)*rising(alpha,j)/rising(kappa,j) for j in range(k+1))
   eq(q,from_moments)
   c=F(1,k)+1-q
   cn=F(1,k+1)+1-qfrac(alpha,kappa,k+1)
   H=alpha*k*(k+1)*q/(kappa+k)
   eq(cn-c,(H-1)/(k*(k+1)))
   if prevH is not None:
    eq(H>prevH,True)
   prevH=H


def find_opt(kappa,p):
 alpha=kappa*p
 q=1.0
 k=1
 while k<2000000:
  q*= (kappa-alpha+k-1)/(kappa+k-1)
  H=alpha*k*(k+1)*q/(kappa+k)
  if H>=1: return k, 1.0/k+1-q
  k+=1
 raise RuntimeError('unreached')

GAMMA=0.5772156649015329
for kappa in (1.,2.,3.):
 digamma={1.: -GAMMA,2.:1-GAMMA,3.:1.5-GAMMA}[kappa]
 prev_err=1e10
 for p in (0.004,0.001,0.00025):
  a=kappa*p
  k,c=find_opt(kappa,p)
  loc=a*k
  asym=c/a-(log(1/a)+1-digamma)
  print('asymptotic',kappa,p,k,round(loc,8),round(c,10),round(asym,8))
  assert 0.85<loc<1.25
  assert abs(asym)<prev_err
  prev_err=abs(asym)
  checks+=2
print('CHECKS_PASS',checks)
