"""Reproduce exact defect-edge RSA probability independently by full remaining-graph-state recursion."""
from fractions import Fraction
from functools import lru_cache

def formula(a,b,lam):
    assert a>=2 and b>=1 and lam>0
    survival = Fraction(1)
    prob = Fraction(0)
    for k in range(min(a-2,b)+1):
        i,j=a-k,b-k
        den=i*j+lam
        prob += survival*lam/den
        survival *= Fraction((i-2)*j,1)/den
    return prob

def alternate_laplace(a,b,lam):
    # Occupancy of two tagged sites at the first independent defect-edge alarm.
    n=min(a,b)
    reach=Fraction(1)
    total=Fraction(0)
    for k in range(n):
        h=(a-k)*(b-k)
        f=Fraction((a-k)*(a-k-1),a*(a-1))
        total += f*reach*lam/(h+lam)
        reach *= Fraction(h,1)/(h+lam)
    ffinal=Fraction((a-n)*(a-n-1),a*(a-1))
    return total+ffinal*reach

def exact_full(a,b,lam):
    n=a+b
    # Every free-vertex subset is an independent state. Transition by edge weight.
    edges=[(i,j,Fraction(1)) for i in range(a) for j in range(a,n)]
    edges.append((0,1,lam))
    @lru_cache(None)
    def hit(mask):
        choices=[(u,v,w) for u,v,w in edges if mask>>u&1 and mask>>v&1]
        if not choices:return Fraction(0)
        den=sum((w for _,_,w in choices),Fraction(0))
        return sum((w/den if (u,v)==(0,1) else w*hit(mask^(1<<u)^(1<<v))/den for u,v,w in choices),Fraction(0))
    return hit((1<<n)-1),hit.cache_info().currsize

def jam(a,b,p):
    return (1-p)*min(a,b)+p*(1+min(a-2,b))

if __name__=='__main__':
    checks=0; states=0
    for a in range(2,7):
      for b in range(1,7):
       for lam in [Fraction(1,3),Fraction(1),Fraction(5,2),Fraction(4)]:
        f=formula(a,b,lam);e,s=exact_full(a,b,lam)
        assert e==f==alternate_laplace(a,b,lam),(a,b,lam,e,f)
        assert 0<f<1,(a,b,lam,f)
        checks+=1;states+=s
    print('exact_full_vs_formula',checks,'cases,',states,'memoized states')
    for a,b in [(2,2),(3,1),(6,2),(4,6),(10,10),(20,20)]:
      f=formula(a,b,Fraction(1));print('example',a,b,'P=',f,'mean=',jam(a,b,f))
