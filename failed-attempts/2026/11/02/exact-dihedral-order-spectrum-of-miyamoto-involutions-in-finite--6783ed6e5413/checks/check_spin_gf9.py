from itertools import product
from collections import Counter
from math import gcd,prod
# x=a+b*t in F_3[t]/(t^2+1), encoded a+3b.
def add(x,y):return (x%3+y%3)%3+3*((x//3+y//3)%3)
def neg(x):
 a,b=x%3,x//3
 return (-a)%3+3*((-b)%3)
def mul(x,y):
 a,b=x%3,x//3;c,d=y%3,y//3
 return ((a*c+2*b*d)%3)+3*((a*d+b*c)%3)
def sub(x,y):return add(x,neg(y))
def powf(x,n):
 r=1
 while n:
  if n%2:r=mul(r,x)
  x=mul(x,x);n//=2
 return r
def chi(x):return 0 if x==0 else (1 if powf(x,4)==1 else -1)
def phi(n):return sum(gcd(i,n)==1 for i in range(1,n+1))
def mm(A,B):
 m=len(A)
 return [[sumf(mul(A[i][k],B[k][j]) for k in range(m)) for j in range(m)] for i in range(m)]
def sumf(vals):
 r=0
 for v in vals:r=add(r,v)
 return r
def R(u,d):
 m=len(u)
 return [[sub(mul(mul(2,u[i]),mul(d[j],u[j])),int(i==j)) for j in range(m)] for i in range(m)]
def order(M):
 m=len(M);I=[[int(i==j) for j in range(m)] for i in range(m)]; P=I
 for a in range(1,50):
  P=mm(P,M)
  if P==I:return a
 raise Exception('bad order')
for d in [[1,1,1],[1,1,4],[1,1,1,1]]:
 u=[1]+[0]*(len(d)-1); M=R(u,d); c=Counter()
 for v in product(range(9),repeat=len(d)):
  if sumf(mul(z,mul(x,x)) for z,x in zip(d,v))!=1:continue
  c[order(mm(M,R(v,d)))]+=1
 n=len(d)-1
 D=1
 for z in d[1:]:D=mul(D,z)
 eps=chi(mul(powf(2,n//2),D))
 def N(s):
  if n%2==0:return 9**(n-1)+((8 if not s else -1)*eps*9**(n//2-1))
  return 9**(n-1)+(0 if not s else eps*chi(s)*9**((n-1)//2))
 expected={1:2,3:2*(N(0)-1)}
 for a in [2,4]:
  # split torus size 4, nonsplit 5
  if a==2: expected[a]=phi(a)* (9**(n-1)-eps*9**(n//2-1) if n%2==0 else 9**(n-1)+eps*chi(2)*9**((n-1)//2))
  if a==4: expected[a]=phi(a)* (9**(n-1)-eps*9**(n//2-1) if n%2==0 else 9**(n-1)+eps*chi(2)*9**((n-1)//2))
 expected[5]=phi(5)*(9**(n-1)-eps*9**(n//2-1) if n%2==0 else 9**(n-1)-eps*chi(2)*9**((n-1)//2))
 # split d2,d4, nonsplit d5. For q9 Q on first e1, this formula holds.
 expected={x:y for x,y in expected.items() if y}
 print(d,'actual',dict(sorted(c.items())),'pred',expected)
 assert dict(c)==expected
print('GF9_EXTENSION_OK')
