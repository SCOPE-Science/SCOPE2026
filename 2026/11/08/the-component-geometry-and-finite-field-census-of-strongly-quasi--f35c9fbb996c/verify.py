from itertools import product

def mm(a,b,n,q):
 return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%q for i in range(n) for j in range(n))
def power(a,n,q):
 b=tuple(int(i==j) for i in range(n) for j in range(n)); e=n
 while e:
  if e&1:b=mm(b,a,n,q)
  a=mm(a,a,n,q);e//=2
 return b

def gaussian(n,r,q):
 if not r or r==n:return 1
 from fractions import Fraction
 f=Fraction(1,1)
 for i in range(r):f*=Fraction(q**(n-i)-1,q**(r-i)-1)
 return int(f)
def formula(n,q):
 from fractions import Fraction
 s=q**(n*n-n)
 return s+sum((q-1)*gaussian(n,r,q)*q**(r*(n-r))*q**(r*r-r+(n-r)**2-(n-r)) for r in range(1,n+1))
for q,n in [(2,1),(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)]:
 cnt=0
 for a in product(range(q),repeat=n*n):
  an=power(a,n,q)
  if not any(an):cnt+=1;continue
  for u in range(1,q):
   au=tuple((a[i*n+j]-(u if i==j else 0))%q for i in range(n) for j in range(n))
   if not any(mm(an,power(au,n,q),n,q)):
    cnt+=1;break
 f=formula(n,q)
 print(f'q={q} n={n} direct={cnt} expected={f} total={q**(n*n)}',flush=True)
 assert cnt==f
print('VERIFY_OK')
