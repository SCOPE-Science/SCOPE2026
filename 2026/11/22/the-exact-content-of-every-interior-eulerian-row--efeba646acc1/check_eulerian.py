from fractions import Fraction
from math import gcd, factorial, comb

def rows(N):
 a=[1]
 for n in range(1,N+1):
  if n==1:
   a=[1]
  else:
   a=[(k+1)*(a[k] if k<n-1 else 0)+(n-k)*(a[k-1] if k else 0) for k in range(n)]
  yield n,a

def predictor(n):
 if n==3:return 4
 if n==4:return 11
 return 2 if n>4 and n-1>0 and ((n-1)&(n-2))==0 else 1

num=0
for n,a in rows(240):
 if n<3: continue
 g=0
 for v in a[1:-1]:g=gcd(g,v)
 assert g==predictor(n),(n,g,predictor(n))
 num+=1
 if n<=20:
  total=factorial(n)
  m=[sum(k**j*v for k,v in enumerate(a)) for j in range(5)]
  mu=Fraction(m[1],total); second=Fraction(m[2],total); third=Fraction(m[3],total); fourth=Fraction(m[4],total)
  var=second-mu*mu
  mu4=fourth-4*mu*third+6*mu*mu*second-3*mu**4
  cum4=mu4-3*var**2
  if n>=4:
   assert mu == Fraction(n-1,2)
   assert var == Fraction(n+1,12)
   assert cum4 == -Fraction(n+1,120)
   num+=3
 if n<=48:
  for k,v in enumerate(a):
   rhs=sum((-1)**j*comb(n+1,j)*(k+1-j)**n for j in range(k+1))
   assert rhs==v,(n,k,v,rhs)
   num+=1
print('passed',num,'assertions, n 3..240')
for n,a in rows(17):
 if n>=3:print(n,predictor(n))
