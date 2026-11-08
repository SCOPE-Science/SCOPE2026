"""Numerical and exact-arithmetic checks for unit-indexed finite Fourier compressions.
Requires Python 3 and NumPy. Run: python CHECKER.py.
"""
from math import gcd, isclose, cos, sin, pi, sqrt
from collections import Counter
from itertools import product
import cmath
import numpy as np

def units(n):return [a for a in range(n) if gcd(a,n)==1]
def matrix(n,b=1):
 u=np.asarray(units(n),dtype=np.int64)
 return np.exp(2j*np.pi*(b*np.outer(u,u)%n)/n)/sqrt(n)
def dyadic_expected(k,b):
 if k==1:return Counter({complex(-1/sqrt(2)):1})
 if k==2:return Counter({(1j)**(b%4):1,0j:1})
 if k==3:
  return Counter({complex(1 if cos(b*pi/4)>0 else -1):1,1j*(1 if sin(b*pi/4)>0 else -1):1,0j:2})
 return Counter({1+0j:2**(k-4),-1+0j:2**(k-4),1j:2**(k-4),-1j:2**(k-4),0j:2**(k-2)})
def eval_spectrum(M,expected,n):
 vals=np.linalg.eigvals(M)
 d=dict(expected)
 for v in vals:
  key=min(d,key=lambda z:abs(z-v))
  assert abs(key-v)<1e-7,(n,v,key)
  d[key]-=1
 assert all(x==0 for x in d.values()),(n,d)
 return max(min(abs(z-v) for z in expected) for v in vals)

cases=0; err=0
for k in range(1,8):
 n=2**k
 for b in [1,3,5,7,11]:
  if k==1 and b>1:continue
  A=matrix(n,b)
  ep=dyadic_expected(k,b)
  err=max(err,eval_spectrum(A,ep,(n,b)))
  r=2**(k-2) if k>=2 else 1
  assert sum(z for v,z in ep.items() if abs(v)>1e-8)==r
  assert abs(np.trace(A)-sum(v*z for v,z in ep.items()))<1e-7
  if k>=2:
   u=units(n); h=n//2
   T=np.array([[int((y==(x+h)%n)) for y in u] for x in u],dtype=float)
   K=(np.eye(len(u))-T)/2
   R=np.array([[int(y==(-x)%n) for y in u] for x in u],dtype=float)
   assert np.max(abs(A@A.conj().T-K))<1e-12
   assert np.max(abs(A@A-K@R))<1e-12
  cases+=1
print('DYADIC_EIGENPHASE_PASS',cases,'max_error',err)

# Exact integer root-count identities on larger powers.
for k in range(2,12):
 n=2**k; u=units(n)
 for b in [1,3,5,7]:
  trace=sum(cmath.exp(2j*pi*((b*x*x)%n)/n) for x in u)/sqrt(n)
  expected=sum(v*m for v,m in dyadic_expected(k,b).items())
  assert abs(trace-expected)<2e-10,(k,b,trace,expected)
print('DYADIC_TRACE_PASS',10*4)

# CRT product claim checked with exact phase congruences for even nonprime-power moduli.
for n in [6,10,12,14,18,20,24,28,30,36,40,42,48,60,72,80,96,120]:
 primes=[]; x=n; p=2
 while p*p<=x:
  if x%p==0:
   pp=1
   while x%p==0: pp*=p; x//=p
   primes.append(pp)
  p+=1
 if x>1:primes.append(x)
 if len(primes)==1:continue
 bs=[pow(n//q,-1,q) for q in primes]
 for a in units(n):
  for b in units(n):
   difference=sum((bs[j]*(a%q)*(b%q)*(n//q)) for j,q in enumerate(primes))-a*b
   assert difference%n==0,(n,a,b)
print('CRT_PHASE_PASS')

def prime_powers(n):
 ans=[]; p=2; x=n
 while p*p<=x:
  if x%p==0:
   q=1;a=0
   while x%p==0: x//=p;q*=p;a+=1
   ans.append((p,a,q))
  p+=1
 if x>1:ans.append((x,1,x))
 return ans

def expected_odd(p,k,b):
 q=p**k
 if k>=2:
  h=(p-1)*p**(k-2); r=(p-1)**2*p**(k-2)
  return Counter({0j:h,1+0j:r//4,-1+0j:r//4,1j:r//4,-1j:r//4})
 s=1 if pow(b%p,(p-1)//2,p)==1 else -1
 if p%4==1:
  m1,m2=(p-3+2*s)//4,(p-3-2*s)//4
  m3=m4=(p-1)//4
 else:
  m1=m2=(p-3)//4
  m3,m4=(p-1+2*s)//4,(p-1-2*s)//4
 return Counter({complex(-1/sqrt(p)):1,1+0j:m1,-1+0j:m2,1j:m3,-1j:m4})

def normalize_counter(C):return Counter({z:n for z,n in C.items() if n>0})
def global_expected(n):
 local=[]
 for p,k,q in prime_powers(n):
  b=pow(n//q,-1,q)
  local.append(dyadic_expected(k,b) if p==2 else expected_odd(p,k,b))
 C=Counter({1+0j:1})
 for D in local:
  new=Counter()
  for u,m in C.items():
   for v,z in D.items():
    w=complex(round((u*v).real,12),round((u*v).imag,12))
    new[w]+=m*z
  C=new
 return normalize_counter(C)

samples=[6,10,12,14,18,20,22,24,26,30,36,40,42,44,48,54,56,60,72,80,84,90,96,100,104,108,120]
gerr=0
for n in samples:
 E=global_expected(n); M=matrix(n)
 gerr=max(gerr,eval_spectrum(M,E,n))
 assert sum(E.values())==len(units(n))
print('GLOBAL_EVEN_SPECTRUM_PASS',len(samples),'max_error',gerr)
