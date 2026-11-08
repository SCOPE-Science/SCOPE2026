from collections import Counter
from itertools import combinations

def neighbors(n,a):
 N=[{(i-1)%n,(i+1)%n} for i in range(n)]
 N[0].add(a);N[a].add(0)
 return N

def propagate(N,S):
 b=set(S);t=0
 while True:
  if len(b)==len(N):return t
  new={next(iter(N[v]-b)) for v in b if len(N[v]-b)==1}
  if not new:return None
  b|=new;t+=1

def theory(n,a):
 b=n-a
 return [max(i,a-1-i)+b//2 for i in range(a)]+[max(j,b-1-j)+a//2 for j in range(b)]

for n in range(4,51):
 for a in range(2,n-1):
  N=neighbors(n,a)
  got=[propagate(N,{i,(i+1)%n}) for i in range(n)]
  want=theory(n,a)
  assert got==want,(n,a,got,want)
  assert min(got)==a//2+(n-a)//2
  assert max(got)==max(a-1+(n-a)//2,n-a-1+a//2)
  if n<=12:
   for i,j in combinations(range(n),2):
    if (j-i)%n not in (1,n-1):assert propagate(N,{i,j}) is None,(n,a,i,j)
print('PASS: all lengths n=4..50, all chord positions, all n minimum forcing pairs with exact propagation times; all other two-sets n<=12 are nonforcing')
for n,a in [(8,4),(8,3),(9,3),(10,2),(10,5),(11,4)]:
 print(f'n={n} chord={a}: time histogram {sorted(Counter(theory(n,a)).items())}, minimum={min(theory(n,a))}, maximum={max(theory(n,a))}')
