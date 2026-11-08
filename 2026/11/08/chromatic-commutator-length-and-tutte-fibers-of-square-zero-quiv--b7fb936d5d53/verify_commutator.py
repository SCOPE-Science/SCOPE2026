"""Independent finite-field checks of commutator fibers in loopless square-zero quiver algebras.
Run: python verify_commutator.py. Standard library only.
"""
from itertools import product
from collections import Counter

def components(n, edges):
    parent = list(range(n))
    def root(i):
        while parent[i] != i:
            i=parent[i]
        return i
    for u,v in edges:
        ru, rv = root(u), root(v)
        if ru != rv: parent[ru] = rv
    return len({root(i) for i in range(n)})

def potts_fiber(n, edges, q, support):
    # Given a specified target commutator supported at the positions 'support'.
    # Spin labels are ordered pairs in F_q^2.
    total=0
    for labels in product(range(q*q), repeat=n):
        if any(labels[u] == labels[v] for i,(u,v) in enumerate(edges) if i in support):
            continue
        eq=sum(labels[u]==labels[v] for u,v in edges)
        total += q**(len(edges)+eq)
    return total

def fk_zero(n, edges, q):
    m=len(edges)
    return q**m*sum((q-1)**len(F)*q**(2*components(n,F))
      for mask in range(1<<m)
      for F in [[e for j,e in enumerate(edges) if mask>>j&1]])

def direct_fibers(n, edges, q):
    m=len(edges)
    # Coordinates: vertex diagonals a,b; arrows x,y.
    result=Counter()
    for a in product(range(q), repeat=n):
      for b in product(range(q), repeat=n):
        for x in product(range(q), repeat=m):
          for y in product(range(q), repeat=m):
            z=tuple(((a[u]-a[v])*y[i]-(b[u]-b[v])*x[i])%q
                    for i,(u,v) in enumerate(edges))
            result[z]+=1
    return result

def test():
    instances=[(2,[(0,1)],2), (3,[(0,1),(1,2)],2),
      (3,[(0,1),(1,2)],3), (3,[(0,1),(1,2),(0,2)],2),
      (4,[(0,1),(0,2),(0,3)],2), (4,[(0,1),(1,2),(2,3)],2),
      (2,[(0,1)]*3,2)]
    for n,edges,q in instances:
      actual=direct_fibers(n,edges,q)
      m=len(edges)
      assert sum(actual.values())==q**(2*(n+m))
      for target in product(range(q),repeat=m):
        support={i for i,t in enumerate(target) if t}
        prediction=potts_fiber(n,edges,q,support)
        assert actual[target]==prediction, (n,edges,q,target,actual[target],prediction)
      fk=fk_zero(n,edges,q)
      assert actual[(0,)*m]==fk
      print('PASS', 'q=',q,'n=',n,'m=',m,'zero_fiber=',fk,'total=',sum(actual.values()),'distinct_fibers=',len(set(actual.values())))
    # Verify precise asymptotic exponent and coefficient via the FK polynomial.
    for n,edges in [(3,[(0,1),(1,2),(0,2)]),
                    (5,[(i,j) for i in range(5) for j in range(i+1,5)]),
                    (2,[(0,1)]*4)]:
      exponents=[(len(F)+2*components(n,F),len(F))
       for mask in range(1<<len(edges))
       for F in [[e for i,e in enumerate(edges) if mask>>i&1]]]
      exponent=max(x for x,_ in exponents)
      d=exponent-2*n
      assert d==max(k-2*(n-components(n,[e for i,e in enumerate(edges) if mask>>i&1]))
                        for mask in range(1<<len(edges))
                        for k in [mask.bit_count()])
      c=sum(x==exponent for x,_ in exponents)
      print('ASYMPTOTIC', 'n=',n,'m=',len(edges),'excess=',d,'coefficient=',c)
    print('COMMUTATOR_SUPPORT_AND_FK_DIRECT_PASS')

if __name__=='__main__': test()
