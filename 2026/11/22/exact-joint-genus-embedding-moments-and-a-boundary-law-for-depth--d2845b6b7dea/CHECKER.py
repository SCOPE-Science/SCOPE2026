from itertools import combinations
from fractions import Fraction
from math import comb

def poly_mul(A,B):
 C=[0]*(len(A)+len(B)-1)
 for i,x in enumerate(A):
  for j,y in enumerate(B): C[i+j]+=x*y
 return C

def T(i,r,k):
 n=r-1; h=(i-1)//2; delta=(i%2==0)
 other=n-(1 if i<r else 0)-2*h-int(delta)
 assert other>=0,(i,r,other)
 p=[1]
 for _ in range(h):p=poly_mul(p,[1,2])
 for _ in range(other):p=poly_mul(p,[1,1])
 return p[k] if k<len(p) else 0

def derived_edim(m,r,B):
 sums={a+b for a in B for b in B}
 N=sum(i not in B and i in sums for i in range(2,r+1))
 return m-N

def independent_edim(m,r,B):
 F=m+r
 S={0,m,*[m+i for i in B],*range(F+1,4*m+2)}
 assert F not in S
 assert min(x for x in S if x>0)==m
 assert all(a+b in S for a in S for b in S if a+b <4*m+2)
 # all minimal generators below conductor + m
 gens=[s for s in range(m,F+m+2) if s in S and not any(a in S and s-a in S for a in range(m,s))]
 assert m in gens
 return len(gens)

for r in range(2,11):
 m=r+2;n=r-1
 totals={k:[0,0] for k in range(n+1)}
 for mask in range(1<<n):
  B={i for i in range(1,r) if mask>>(i-1)&1}; k=len(B)
  f=derived_edim(m,r,B); g=independent_edim(m,r,B)
  assert f==g,(m,r,B,f,g)
  totals[k][0]+=f;totals[k][1]+=1
 for k,(v,count) in totals.items():
  expect=Fraction(m-r+1+k,1)-Fraction(k,n) + Fraction(sum(T(i,r,k) for i in range(2,r+1)),comb(n,k))
  assert Fraction(v,count)==expect,(r,k,Fraction(v,count),expect)
 mean=sum(v for v,count in totals.values())/(1<<n)
 a=Fraction(3,4)
 formula=Fraction(m,1)-Fraction(r,2)+Fraction(5,2) - (2*a**(r//2-1) if r%2==0 else Fraction(3,2)*a**((r-3)//2))
 assert Fraction(sum(v for v,c in totals.values()),1<<n)==formula,(r,mean,formula)
 print('PASS r',r,'m',m,'subsets',1<<n,'mean',formula)
print('SHORT_CONDUCTOR_EMBEDDING_OK')
