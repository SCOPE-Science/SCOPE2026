from itertools import combinations, permutations
from math import comb, factorial
from collections import Counter

def rook(n): return [comb(n,k)**2*factorial(k) for k in range(n+1)]
def conv(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,v in enumerate(a):
  for j,w in enumerate(b):out[i+j]+=v*w
 return out

def predicted(a,b):
 N=a+b
 R=conv(rook(a),rook(b)); R += [0]*(N+1-len(R))
 C=[0]*(N+1)
 for k in range(1,min(a,b)+1): C[k]=comb(a,k)*comb(b,k)*factorial(k)
 Npoly=[2*x+y for x,y in zip(C,conv(C,C)[:N+1])]
 F=[x+y for x,y in zip(R,Npoly)]
 if a==b: return F,[0]*(N+1)
 return F,Npoly

def brute(a,b):
 n=a+b; colors=[0]*a+[1]*b
 total=Counter();non=Counter()
 for k in range(n+1):
  for dom in combinations(range(n),k):
   for img in combinations(range(n),k):
    for dest in permutations(img):
     p=dict(zip(dom,dest)); valid=all((colors[u]!=colors[v])==(colors[p[u]]!=colors[p[v]]) for i,u in enumerate(dom) for v in dom[i+1:])
     if not valid:continue
     total[k]+=1
     # Does a full automorphism extend p?
     ex=all(colors[u]==colors[v] for u,v in p.items())
     if a==b:ex=ex or all(colors[u]!=colors[v] for u,v in p.items())
     if not ex:non[k]+=1
 return [total[k] for k in range(n+1)],[non[k] for k in range(n+1)]
if __name__=='__main__':
 for a,b in [(1,1),(2,1),(2,2),(3,1),(3,2),(3,3),(4,2),(5,1)]:
  p=predicted(a,b);v=brute(a,b)
  assert p==v, (a,b,p,v)
  print((a,b),'total',p[0],'nonextendible',p[1])
 print('PASS')
