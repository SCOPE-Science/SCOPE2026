"""Direct commutator fiber verification in F_4=F_2[t]/(t^2+t+1)."""
from itertools import product
from collections import Counter

def mul(a,b):
    p=0
    for j in range(2):
        if (b>>j)&1:p^=a<<j
    if p&4:p^=0b111   # t^2=t+1
    return p

def test():
    q,n=4,3
    edges=[(0,1),(1,2)]
    m=len(edges)
    actual=Counter()
    for a in product(range(q),repeat=n):
      for b in product(range(q),repeat=n):
       for x in product(range(q),repeat=m):
        for y in product(range(q),repeat=m):
         z=tuple(mul(a[u]^a[v],y[i])^mul(b[u]^b[v],x[i])
                 for i,(u,v) in enumerate(edges))
         actual[z]+=1
    assert sum(actual.values())==q**(2*(n+m))
    for z in product(range(q),repeat=m):
       support=[i for i,v in enumerate(z) if v]
       ans=0
       for s in product(range(q*q),repeat=n):
           if any(s[u]==s[v] for i,(u,v) in enumerate(edges) if i in support):continue
           eq=sum(s[u]==s[v] for u,v in edges)
           ans += q**(m+eq)
       assert actual[z]==ans,(z,actual[z],ans)
    print('GF4_DIRECT_FIBERS_PASS','n=',n,'m=',m,'zero_fiber=',actual[(0,)*m],
          'all_pairs=',sum(actual.values()))
if __name__=='__main__':test()
