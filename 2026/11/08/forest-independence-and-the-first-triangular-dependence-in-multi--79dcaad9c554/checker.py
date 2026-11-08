"""Independent finite checks for three independently sampled successor paths."""
from itertools import permutations
from fractions import Fraction
from collections import Counter

def edges(p):return set(zip(p,p[1:]))
def m(a,b):return len(a & b)

def exact(n):
    ps=list(permutations(range(n)))
    es=[edges(p) for p in ps]
    c=Counter()
    for a in es:
      for b in es:
        ab=m(a,b)
        for d in es:
          c[(ab,m(a,d),m(b,d))]+=1
    den=len(ps)**3
    mu=Fraction(n-1,n)
    est= sum(Fraction(a*b*d*k,den) for (a,b,d),k in c.items())
    expr=Fraction(n**4-4*n**3+8*n**2-8*n+1,n**2*(n-1)**2)
    kappa=est-mu**3
    kexp=Fraction(n**4-2*n**3+2*n**2-4*n+1,n**3*(n-1)**2)
    assert est==expr,(n,est,expr)
    assert kappa==kexp,(n,kappa,kexp)
    # pairwise independence, all pairs, all counts
    for ij,ik in ((0,1),(0,2),(1,2)):
      marg1=Counter();marg2=Counter();pair=Counter()
      for tup,num in c.items():
        marg1[tup[ij]]+=num;marg2[tup[ik]]+=num;pair[(tup[ij],tup[ik])]+=num
      assert all(num*den==marg1[x]*marg2[y] for (x,y),num in pair.items())
    print('exact',n,'E[product]',est,'kappa',kappa)

def combinatorial(n):
    es=[(a,b) for a in range(n) for b in range(n) if a!=b]
    def compatible(x,y):
      return x==y or (x[0]!=y[0] and x[1]!=y[1] and x!=(y[1],y[0]))
    N=n*(n-1); D=(n-1)*(n-2)
    triples_distinct=sum(1 for e in es for f in es for g in es
        if len({e,f,g})==3 and compatible(e,f) and compatible(e,g) and compatible(f,g))
    T=N*(n-2)*(n**3-6*n*n+11*n-4)
    assert triples_distinct==T,(n,triples_distinct,T)
    p=Fraction(1,n);w=Fraction(1,n*(n-1))
    est=N*p**3+3*N*D*p*w*w+T*w**3
    expr=Fraction(n**4-4*n**3+8*n*n-8*n+1,n*n*(n-1)**2)
    assert est==expr,(n,est,expr)
    print('edge',n,'distinct',T,'triple',est)

for n in (2,3,4):exact(n)
for n in range(2,9):combinatorial(n)
print('ALL_CHECKS_OK')

# Independently check the graph-indexed relative-permutation law.
def inv(p):
    z=[0]*len(p)
    for i,v in enumerate(p):z[v]=i
    return z

def ratio(p,q):
    pi=inv(p)
    return tuple(pi[v] for v in q)

def ratio_distribution(n,k,arcs):
    ps=list(permutations(range(n)))
    z=Counter(tuple(ratio(sample[a],sample[b]) for a,b in arcs)
              for sample in __import__('itertools').product(ps,repeat=k))
    return z

for n,k,arcs in [(2,3,[(0,1),(1,2)]),
                 (3,3,[(0,1),(0,2)]),
                 (3,4,[(0,1),(1,2),(2,3)])]:
    z=ratio_distribution(n,k,arcs)
    import math
    assert len(z)==math.factorial(n)**len(arcs)
    assert set(z.values())=={math.factorial(n)**(k-len(arcs))}
    print('forest ratios',n,k,len(arcs),'OK')
for n in (2,3):
    z=ratio_distribution(n,3,[(0,1),(1,2),(0,2)])
    import math
    assert len(z)==math.factorial(n)**2
    assert set(z.values())=={math.factorial(n)}
    ident=tuple(range(n))
    assert z[(ident,ident,ident)]==math.factorial(n)
    print('triangle ratios',n,'support',len(z),'OK')
print('ALL_CHECKS_OK')
