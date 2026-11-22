from itertools import product
from collections import Counter

def predicted(n):
 if n%2:
  return {0:5**n-(4**n-4),1:4**n-4,2:0,3:0,4:0,5:0}
 m=n//2
 luc=[2,1]
 for i in range(2,2*m+1):luc.append(luc[-1]+luc[-2])
 L=luc[2*m]
 E2=(4**m+2*L)//5
 E3=(9**m+2*L)//5
 E4=(16**m+4)//5
 a4=5
 a3=10*(E2-2)
 a2=10*(E3-3*E2+3)
 a1=5*(E4-4*E3+6*E2-4)
 return {0:5**n-a1-a2-a3-a4,1:a1,2:a2,3:a3,4:a4,5:0}

def observed(n):
 c=Counter()
 for x in product(range(5),repeat=n):
  if any(x[i]==x[(i+1)%n] for i in range(n)):continue
  y=tuple((x[i]+x[(i+1)%n])%5 for i in range(n))
  c[y]+=1
 counts=Counter(c.values())
 counts[0]=5**n-len(c)
 return {j: counts[j] for j in range(6)}

for n in range(2,9):
 p=predicted(n); c=observed(n);assert p==c,(n,p,c)
 print('n',n,'nonzero', {j:p[j] for j in range(1,6)},'unreachable',p[0])
for n in range(2,202):
 p=predicted(n)
 assert all(v>=0 for v in p.values())
 assert sum(j*v for j,v in p.items())==4**n+4*((-1)**n)
 assert sum(p.values())==5**n
print('PASS: formula matches exhaustive ring sizes 2-8; all-length identities verified at 2-201')
