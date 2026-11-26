from itertools import product
from math import isqrt

def primes_upto(N):
 sieve=bytearray(b'\x01')*(N+1); sieve[:2]=b'\x00\x00'
 for k in range(2,isqrt(N)+1):
  if sieve[k]:sieve[k*k:N+1:k]=b'\x00'*((N-k*k)//k+1)
 return [i for i in range(N+1) if sieve[i]]

def chi(a,p):
 a%=p
 if not a:return 0
 s=pow(a,(p-1)//2,p)
 return 1 if s==1 else -1

def fast_count(p):
 c2,c3,cm=chi(2,p),chi(3,p),chi(-1,p)
 E=sum(chi(n*(n+1)*(n+2)*(n+3),p) for n in range(p))
 out={}
 for a,b,c in product((-1,1),repeat=3):
  numer=(p-4+(a+c)*(-c2-1-c3)+b*(-c2-2)
         +b*(a+c)*(-1-cm-c3)+a*c*E
         +a*b*c*(-c2-2*cm))
  assert numer %8 ==0,(p,a,b,c,numer)
  out[(a,b,c)]=numer//8
 return out,E

def direct_count(p):
 out={x:0 for x in product((-1,1),repeat=3)}
 for n in range(p):
  v=[chi((n+j)*(n+j+1)//2,p) for j in (0,1,2)]
  if 0 not in v:out[tuple(v)]+=1
 return out

if __name__=='__main__':
 for p in primes_upto(997):
  if p<5:continue
  a,e=fast_count(p)
  assert a==direct_count(p),(p,a,direct_count(p))
  assert abs(e+1)<=2*p**0.5
  if p>=19:assert min(a.values())>0,(p,a)
  if p in (5,7,11,13,17,19,23,29,31):
   print('p =',p,'E =',e,'minimum count =',min(a.values()))
   assert (min(a.values()) > 0) == (p >= 19)
 print('PASS: all eight sign pattern counts identical, each prime 5..997 (166 primes).')
