"""Standalone exact exhaustive checks for one contiguous-block permutation channel."""
from collections import Counter
from itertools import product, permutations
from math import factorial

def descendants(x,k):
    ans={tuple(x)}
    for start in range(len(x)-k+1):
        for w in set(permutations(x[start:start+k])):
            ans.add(tuple(x[:start])+w+tuple(x[start+k:]))
    return ans

def local_count(v):
    m=len(v)
    c=Counter(v)
    tot=factorial(m)
    for ct in c.values():tot//=factorial(ct)
    a,b=c[v[0]],c[v[-1]]
    return (tot*(m*(m-1)-(a+b)*(m-1)+a*(b-int(v[0]==v[-1]))))//(m*(m-1))

def predicted(x,k):
    n=len(x)
    return 1+sum(local_count(x[i:i+m]) for m in range(2,k+1) for i in range(n-m+1))

def universal(n,k):
    return 1+sum((n-m+1)*(factorial(m)-2*factorial(m-1)+factorial(m-2)) for m in range(2,k+1))

def check():
    c=0
    for q in (2,3,4):
      for n in range(2,8 if q<=3 else 6):
       for k in range(2,n+1):
        maxv=0; achievers=0
        for x in product(range(q),repeat=n):
         direct=len(descendants(x,k))
         calc=predicted(x,k)
         assert calc==direct,(q,n,k,x,calc,direct)
         c+=1
         maxv=max(maxv,direct)
         if direct==universal(n,k):achievers+=1
        if q>=k:
         assert maxv==universal(n,k),(q,n,k,maxv,universal(n,k))
         expect=factorial(q)//factorial(q-k)*(q-k+1)**(n-k)
         assert achievers==expect,(q,n,k,achievers,expect)
        else: assert maxv<universal(n,k),(q,n,k)
    for n in range(3,17):
      vals=[len(descendants(x,3)) for x in product((0,1),repeat=n)] if n<=9 else [predicted(x,3) for x in product((0,1),repeat=n)]
      ub=(3*n)//2-1
      assert max(vals)==ub,(n,max(vals),ub)
      cnt=2 if n%2==0 else n+3
      assert vals.count(ub)==cnt,(n,vals.count(ub),cnt)
    # Independent weight distribution from a two-state transfer matrix.
    for n in range(3,13):
      dists=Counter(len(descendants(x,3)) if n<=8 else predicted(x,3)
                    for x in product((0,1),repeat=n))
      # f(state,sphere weight) counts difference sequences, two original initial bits.
      cur={(0,1):1,(1,2):1}
      for _ in range(n-2):
        nxt=Counter()
        for (last,weight),count in cur.items():
          for b in (0,1):nxt[b,weight+b+(last!=b)]+=count
        cur=nxt
      pred=Counter()
      for (last,weight),count in cur.items():pred[weight]+=2*count
      assert pred==dists,(n,pred,dists)
      assert sum(v*dists[v] for v in dists)==2**n*(n-0.5)
      assert sum(((v-(n-0.5))**2)*dists[v] for v in dists)==2**n*(2*n-3)/4
    print('PASS direct vs local formula, high-alphabet sharp classification, binary k3 spectrum and moments; source instances:',c)
if __name__=='__main__':check()
