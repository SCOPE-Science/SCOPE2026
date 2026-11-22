from fractions import Fraction as Q
from itertools import product
from math import factorial

def add(a,b):return [x+y for x,y in zip(a,b)]
def mul(a,b):
 n=len(a)-1;o=[Q(0)]*(n+1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b[:n-i+1]):
    if y:o[i+j]+=x*y
 return o

def power(a,k):
 n=len(a)-1;o=[Q(0)]*(n+1);o[0]=1
 for _ in range(k):o=mul(o,a)
 return o

def expseries(a):
 n=len(a)-1; assert a[0]==0
 b=[Q(0)]*(n+1);b[0]=1
 for m in range(1,n+1):b[m]=sum(Q(j)*a[j]*b[m-j] for j in range(1,m+1))/m
 return b

def generate(n):
 R=[Q(0)]+[Q(m**(m-1),factorial(m)) for m in range(1,n+1)]
 U=[Q(0)]*(n+1)
 P=[Q(0)]*(n+1);P[0]=1
 for k in range(1,n+1):
  P=mul(P,R)
  U=add(U,[x*Q((-k)**(k-1),factorial(k)) for x in P])
 assert all(x==y for x,y in zip(mul(U,expseries(U)),R))
 odd=[Q(0)]*(n+1)
 eve=[Q(0)]*(n+1)
 P=[Q(0)]*(n+1);P[0]=1
 for k in range(1,n+1):
  P=mul(P,U)
  if k%2:odd=add(odd,[x/Q(k) for x in P])
  else:eve=add(eve,[x/Q(k) for x in P])
 base=expseries([-x for x in odd]);one=expseries([-x for x in add(odd,eve)])
 inv=[Q(0)]*(n+1);inv[0]=1
 for k in range(1,n+1):inv[k]=sum(R[i]*inv[k-i] for i in range(1,k+1))
 good=mul(inv,base);single=mul(inv,one)
 # marker polynomial distribution of K unblocked even components
 out=[]
 for k in range(n//2+1):
  # good EGF * exp( (y-1)*eve ), coefficient y^k = good * exp(-eve) * eve^k/k!
  o=mul(mul(good,expseries([-x for x in eve])),[x/Q(factorial(k)) for x in power(eve,k)])
  out.append([int(x*factorial(i)) for i,x in enumerate(o)])
 return R,U,[int(x*factorial(i)) for i,x in enumerate(good)],[int(x*factorial(i)) for i,x in enumerate(single)],out


def classify_mapping(f):
    # Remove noncyclic vertices in leaf-to-root order, recording forced labels.
    n=len(f); indeg=[0]*n; incoming=[[] for _ in range(n)]
    for v,w in enumerate(f): indeg[w]+=1;incoming[w].append(v)
    from collections import deque
    Q=deque(v for v in range(n) if indeg[v]==0)
    color=[None]*n
    while Q:
        v=Q.popleft()
        color[v] = 0 if any(color[u]==1 for u in incoming[v]) else 1
        indeg[f[v]]-=1
        if indeg[f[v]]==0:Q.append(f[v])
    seen=set(); count=1; preferred=1
    for v in range(n):
        if indeg[v]==0 or v in seen:continue
        cycle=[]; u=v
        while u not in seen:
            seen.add(u);cycle.append(u);u=f[u]
        assert u==v
        blocked=any(any(color[t]==1 for t in incoming[u] if indeg[t]==0) for u in cycle)
        if not blocked:
            if len(cycle)%2:count=0
            else:count*=2;preferred*=2
    return count,preferred

def brute(n):
 hist={}; same=0
 for f in product(range(n),repeat=n):
  inmask=[0]*n
  for u,v in enumerate(f):inmask[v]|=1<<u
  admiss=[]; stable=[]
  for S in range(1<<n):
   attacks=0
   for v in range(n):
    if (S>>v)&1:attacks|=1<<f[v]
   if S&attacks:continue
   if attacks|S==(1<<n)-1:stable.append(S)
   ok=True
   for v in range(n):
    if (S>>v)&1 and (inmask[v]&~attacks):ok=False;break
   if ok:admiss.append(S)
  pref=[S for S in admiss if not any((S!=T and (S&T)==S) for T in admiss)]
  assert set(stable).issubset(pref)
  estimated,estimated_pref=classify_mapping(f)
  assert estimated==len(stable),(f,estimated,len(stable))
  assert estimated_pref==len(pref),(f,estimated_pref,len(pref))
  if len(stable)==len(pref):same+=1
  k=len(stable)
  hist[k]=hist.get(k,0)+1
  # classify number of stable extensions by individual cycle and rooted trees, independent of pref
  # n small brute enough
 return same,hist

if __name__=='__main__':
 n=8;R,U,G,S,dist=generate(n)
 print('good',G)
 print('single',S)
 print('number maps with 2^k stable')
 for k,row in enumerate(dist):print(k,[row[i] for i in range(1,n+1)])
 for m in range(1,7):
  total,hist=brute(m)
  expected={2**k:dist[k][m] for k in range(m//2+1)}
  expected[0]=m**m-G[m]
  assert hist=={a:b for a,b in expected.items() if b>0},(m,hist,expected)
  assert total==G[m]
  print('checked',m,m**m,total,hist)
 print('ALL_PASS')
