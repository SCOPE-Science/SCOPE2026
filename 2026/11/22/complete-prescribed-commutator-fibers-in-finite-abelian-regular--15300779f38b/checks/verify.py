"""Direct finite-group tests for prescribed commutator fiber formulas.
Uses only Python's standard library. All group operations are exact.
"""
from collections import Counter
from itertools import product
from math import gcd


def elems(moduli):
    return list(product(*(range(a) for a in moduli)))


def add(x, y, moduli):
    return tuple((a + b) % m for a, b, m in zip(x, y, moduli))


def neg(x, moduli):
    return tuple((-a) % m for a, m in zip(x, moduli))


def sub(x, y, moduli):
    return add(x, neg(y, moduli), moduli)


def subgroup(B, bmods, s, t):
    zero=tuple(0 for _ in bmods)
    gens=(s,t)
    seen={zero}
    pending=[zero]
    while pending:
        v=pending.pop()
        for a in gens:
            w=add(v,a,bmods)
            if w not in seen:
                seen.add(w)
                pending.append(w)
    return frozenset(seen)


def tested_case(amods, bmods):
    A, B=elems(amods), elems(bmods)
    m, n=len(A), len(B)
    index={b:i for i,b in enumerate(B)}
    vectors=list(product(A,repeat=n))
    zero=tuple(0 for _ in amods)
    zero_vector=(zero,)*n
    shifts={s:tuple(index[sub(b,s,bmods)] for b in B) for s in B}
    image=Counter()
    for s in B:
      for t in B:
        ps,pt=shifts[s],shifts[t]
        for x in vectors:
          first=tuple(sub(x[i],x[pt[i]],amods) for i in range(n))
          for y in vectors:
            z=tuple(add(first[i],sub(y[ps[i]],y[i],amods),amods)
                    for i in range(n))
            image[z]+=1
    pair_subgroups=Counter(subgroup(B,bmods,s,t) for s in B for t in B)
    cosets={}
    for H in pair_subgroups:
      unseen=set(B)
      cosets[H]=[]
      while unseen:
        r=next(iter(unseen))
        C={add(r,h,bmods) for h in H}
        unseen-=C
        cosets[H].append([index[b] for b in C])
    predicted=Counter()
    for z in vectors:
      count=0
      for H,generators in pair_subgroups.items():
        if all(sum(z[i][j] for i in C)%amods[j]==0
               for C in cosets[H] for j in range(len(amods))):
            count += generators * m**(n+len(cosets[H]))
      predicted[z]=count
    assert image==predicted,(amods,bmods,'fiber mismatch')
    assert sum(image.values())==(n*m**n)**2
    return len(image),len(set(image.values())),image[zero_vector]


def cyclic_formula(z, moduli, n):
    # z is a vector of lamp-group tuples, so works for arbitrary finite Abelian A.
    m=1
    for k in moduli:m*=k
    def jordan2(k):
      return sum(gcd(k,a,b)==1 for a in range(k) for b in range(k))
    out=0
    for d in range(1,n+1):
      if n%d:continue
      if all(sum(z[j][h] for j in range(i,n,d))%moduli[h]==0
             for i in range(d) for h in range(len(moduli))):
        out+=jordan2(n//d)*m**(n+d)
    return out


def cyclic_compare():
    # Directly compare the divisor formula against the general subgroup formula.
    for amods,n in [((2,),5),((3,),4),((4,),3),((2,2),3)]:
      B=elems((n,)); A=elems(amods); vecs=list(product(A,repeat=n))
      subgroups=Counter(subgroup(B,(n,),s,t) for s in B for t in B)
      idx={b:i for i,b in enumerate(B)}
      for z in vecs:
        val=0
        for H,k in subgroups.items():
          d=n//len(H)
          if all(all(sum(z[j][h] for j in range(i,n,d))%amods[h]==0
                         for h in range(len(amods))) for i in range(d)):
            val+=k*len(A)**(n+d)
        assert val==cyclic_formula(z,amods,n)


def direct_group_law_check():
    # Independent composition-and-inverse verification of the commutator coordinates.
    for n,mod in ((2,2),(3,2),(2,3)):
        amods=(mod,)
        vectors=list(product(range(mod),repeat=n))
        G=list(product(vectors,range(n)))
        def shift(v,k):return tuple(v[(i-k)%n] for i in range(n))
        def mult(g,h):
            x,a=g;y,b=h
            sy=shift(y,a)
            return (tuple((x[i]+sy[i])%mod for i in range(n)),(a+b)%n)
        def inverse(g):
            x,a=g
            sx=shift(x,-a)
            return (tuple((-v)%mod for v in sx),(-a)%n)
        for g in G:
          for h in G:
            x,a=g;y,b=h
            gh=mult(mult(mult(g,h),inverse(g)),inverse(h))
            sx=shift(x,b);sy=shift(y,a)
            target=tuple((x[i]-sx[i]+sy[i]-y[i])%mod for i in range(n))
            assert gh==(target,0),(n,mod,g,h,gh,target)
    print('Direct semidirect multiplication/inverse comparisons: PASS')


def main():
  for amods,bmods in [((2,),(2,)),((2,),(3,)),((2,),(4,)),
                      ((2,),(5,)),((3,),(2,)),((3,),(3,)),
                      ((3,),(4,)),((4,),(2,)),((2,2),(2,)),
                      ((2,),(2,2)),((3,),(2,2))]:
    print('lamp=',amods,'top=',bmods,'vectors/fiber-levels/zero-fiber=',tested_case(amods,bmods))
  cyclic_compare()
  direct_group_law_check()
  print('Cyclic divisor formula vs subgroup formula: PASS')
  print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':main()
