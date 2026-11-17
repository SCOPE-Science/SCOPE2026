"""Supplementary exact-arithmetic checks for rational-primitive commutator ranks.
Run: python3 verify_rank.py. Finite tests support, but do not replace, the infinite proof.
"""
from fractions import Fraction as F
from math import comb


def matrix_rank(a):
    a = [[F(x) for x in row] for row in a]
    m, n = len(a), len(a[0])
    pivot = 0
    for col in range(n):
        hit = next((r for r in range(pivot,m) if a[r][col]),None)
        if hit is None: continue
        a[hit],a[pivot]=a[pivot],a[hit]
        t=a[pivot][col]
        a[pivot]=[x/t for x in a[pivot]]
        for row in range(pivot+1,m):
            if a[row][col]:
                t=a[row][col]
                a[row]=[x-t*y for x,y in zip(a[row],a[pivot])]
        pivot+=1
        if pivot==m: break
    return pivot


def rank_kernel(poly, poles, N):
    # poly is degree/coefficient map; poles contain (lambda, order/coefficient map)
    def r(k):
        v=poly.get(k,F(0))
        for lam,terms in poles:
            v+=sum(F(a)*comb(k+ell-1,ell-1)*lam**k for ell,a in terms.items())
        return v
    return matrix_rank([[(u-v)*r(u+v) for v in range(1,N+1)] for u in range(1,N+1)])


def predicted(poly,poles):
    d=max((k for k,v in poly.items() if v),default=-1)
    base=2*max(0,(d-1)//2)
    return base+sum(2*((max(k for k,v in terms.items() if v)+1)//2) for _,terms in poles)


def check():
    # Distinct exact rational poles, both polynomial and several local pole orders.
    cases=[({},[(F(1,2),{1:1})]),({3:F(1)},[]),({4:F(1)},[]),
      ({6:F(1)},[]),({},[(F(1,2),{3:1})]),({},[(F(1,2),{4:1})]),
      ({6:F(1)},[(F(1,2),{1:1}),(F(1,3),{3:2})]),
      ({4:F(2)},[(F(1,2),{2:4,1:3})]),
      ({8:F(-2),3:F(5)},[(F(1,3),{1:2}),(F(-1,2),{2:1})])]
    for poly,poles in cases:
        target=predicted(poly,poles)
        assert rank_kernel(poly,poles,target+4)==target, (poly,poles,target)
    # Verify monomial Toeplitz projection directly for every small u,v.
    # Q(z^a conjugate(z)^b) is z^(a-b)*(a-b+1)/(a+1) when a>=b,
    # and conjugate(z)^(b-a)*(b-a+1)/(b+1) otherwise.
    def q(a,b):
        return ('a',a-b,F(a-b+1,a+1)) if a>=b else ('c',b-a,F(b-a+1,b+1))
    def T(k, input_pair):
        # T_{z^k} applied to a harmonic monomial basis item.
        side,degree=input_pair
        return q(k,0) if side=='a' and degree==0 else (('a',k+degree,F(1)) if side=='a' else q(k,degree))
    for D in range(2,11):
      for v in range(1,10):
        # Compare analytic positive-mode commutator coefficient by direct projection.
        for u in range(1,10):
          k=D-1
          def apply_twice(first,second):
            p=T(first,('c',v))
            q2=T(second,p[:2])
            return p[2]*q2[2] if q2[:2]==('a',u) else F(0)
          # Products T_z T_{z^(D-1)} and reverse; monomial projection can have
          # additional terms via coanalytic paths, all captured in T.
          left=apply_twice(k,1)
          right=apply_twice(1,k)
          direct=F(D)*(left-right)
          expect=F(u-v,v+1) if u+v==D else F(0)
          assert direct==expect,(D,u,v,direct,expect)
    return len(cases),9*9*9

if __name__=='__main__':
    print('Exact rational rank cases and monomial action coefficient assertions:',check())
