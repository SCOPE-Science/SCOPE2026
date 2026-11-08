from math import factorial
from collections import defaultdict
E=((1,1,1,2),(1,1,2,1),(1,2,0,1),(2,1,1,1))
def mat(p):
 A=[]
 for i in E:
  row=[]
  for j in E:
   X,Y,Z,W=(p*a-b for a,b in zip(i,j)); ans=defaultdict(int)
   if min(X,Y,Z,W)<0 or W%2:row.append({});continue
   d=W//2; n=p-1-d
   if not(0<=d<=p-1):row.append({});continue
   for b in range(p):
    if (X-n)!=3*b:continue
    for a in range(p-b):
     c=p-1-a-b;e=Y-2*a;f=n-e
     if min(c,e,f)<0 or Z!=a+3*c+f:continue
     coeff=(factorial(p-1)//(factorial(a)*factorial(b)*factorial(c)))*(factorial(p-1)//(factorial(d)*factorial(e)*factorial(f)))*(-1)**(b+c+e+f)
     ans[f]=(ans[f]+coeff)%p
   row.append({i:(v if v<=p//2 else v-p) for i,v in ans.items() if v%p})
  A.append(row)
 return A
expected={5:[[{}, {}, {}, {}],[{}, {}, {}, {}],[{}, {}, {}, {}],[{}, {}, {}, {0:-2,2:1}]],7:[[{0:3},{},{},{}],[{},{1:-2,3:3},{},{}],[{},{},{},{}],[{},{},{},{1:-2,3:1}]]}
for p in (5,7):
 A=mat(p)
 assert A==expected[p], (p,A)
 print('characteristic',p, 'Hasse-Witt',A)
print('VERIFY_MULTINOMIAL_PASS')
