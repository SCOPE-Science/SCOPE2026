"""Independent pure-death Laplace-transform test for barbell dimer adsorption."""
from fractions import Fraction
from functools import lru_cache
from math import log

def rate(k): return Fraction(k*(k-1),2)

def surv_coeffs(n):
    # Pure death chain K_n(t): k -> k-2 at rate k(k-1)/2.
    ks=list(range(n,n%2-1,-2))
    c={n:{n:Fraction(1)}}
    for k in ks[1:]:
        d={}
        for j, v in c[k+2].items():
            d[j]=rate(k+2)*v/(rate(k)-rate(j))
        d[k]=-sum(d.values(),Fraction(0))
        c[k]=d
    s={j:sum((Fraction(k,n)*c[k].get(j,0) for k in ks),Fraction(0)) for j in ks}
    assert sum(s.values(),Fraction(0))==1
    return s

def bridge_p(n,m,lam=Fraction(1)):
    a=surv_coeffs(n);b=surv_coeffs(m)
    return sum((Fraction(lam)*u*v/(Fraction(lam)+rate(i)+rate(j)) for i,u in a.items() for j,v in b.items()),Fraction(0))

@lru_cache(None)
def p_recur(a,b,lam):
    val=Fraction(lam)
    if a>=2:val+=Fraction(a*(a-1),2)*p_recur(a-2,b,lam)
    if b>=2:val+=Fraction(b*(b-1),2)*p_recur(a,b-2,lam)
    return val/(Fraction(lam)+Fraction(a*(a+1),2)+Fraction(b*(b+1),2))

def run():
    tests=0
    for n in range(2,16):
      for m in range(2,16):
        for lam in [Fraction(1),Fraction(2),Fraction(1,3)]:
          p=bridge_p(n,m,lam)
          assert p==p_recur(n-1,m-1,lam),(n,m,lam,p)
          tests+=1
    print('Laplace decomposition versus exact recurrence:',tests,'rational comparisons PASS')
    for ratio in [1,2,3]:
      h=1 if ratio==1 else log(ratio)/(ratio-1)
      print('ratio',ratio,'asymptotic h',h)
      for n in [12,24,48]:
       p=float(bridge_p(n,ratio*n))
       print('  n',n,'n*p',n*p)
    for n in range(2,13):
      p0=surv_coeffs(n).get(n%2,Fraction(0))
      assert p0 == Fraction(n%2,n)
    print('odd-clique residual hub survival checks PASS')

if __name__=='__main__': run()
