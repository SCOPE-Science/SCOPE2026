"""Integer-arithmetic verification of orthogonal incidence and symmetric rank sums."""
from fractions import Fraction
from math import prod, ceil, comb
from itertools import product

def gauss(n,k,q):
    if k<0 or k>n: return 0
    out=Fraction(1)
    for j in range(k): out*=Fraction(q**(n-j)-1,q**(k-j)-1)
    assert out.denominator==1
    return int(out)

def symrank(e,t,q):
    if t<0 or t>e:return 0
    result=Fraction(gauss(e,t,q)*q**(t*(t+1)//2))
    for h in range(1,(t+1)//2+1):
        result*=1-Fraction(1,q**(2*h-1))
    assert result.denominator==1
    return int(result)

def isotropic_count(n,q,typ,d):
    w=(n//2 if typ=='split' and n%2==0 else (n-2)//2 if n%2==0 else n//2)
    if d<0 or d>w:return 0
    top=1
    for i in range(d):
        m=n-2*i
        if n%2: s=q**(m-1)-1
        else: s=q**(m-1)+(1 if typ=='split' else -1)*(q-1)*q**(m//2-1)-1
        top*=q**i*s
    bot=prod(q**d-q**i for i in range(d))
    assert top%bot==0
    return top//bot

def joint(d, ranks, q):
    return sum((-1)**j*gauss(d,j,q)*q**(j*(j-1)//2)*prod(symrank(d-j,t,q) for t in ranks) for j in range(d+1))

def test():
    expected_split={(0,0,0):1,(1,0,1):32,(1,1,0):32,(1,1,1):64,(2,0,2):144,(2,1,1):384,(2,1,2):1152,(2,2,0):144,(2,2,1):1152,(2,2,2):2592}
    expected_nonsplit={(0,0,0):1,(1,0,1):20,(1,1,0):20,(1,1,1):40}
    for typ, expected in [('split',expected_split),('nonsplit',expected_nonsplit)]:
        out={}
        for d in range(3):
            iso=isotropic_count(4,3,typ,d)
            for ranks in product(range(d+1),repeat=2):
                count=iso*joint(d,ranks,3)
                assert count>=0
                if count:out[(d,)+ranks]=count
        assert out==expected,(typ,out)
        print('q=3 n=4',typ,'verified rank-vector histogram',sum(out.values()),'tuples')
    for q,total in [(3,33),(5,145)]:
        out=sum(isotropic_count(3,q,'odd',d)*joint(d,(a,b),q) for d in range(2) for a,b in product(range(d+1),repeat=2))
        assert out==total
        print('q=',q,'n=3 odd verified pair total',out)
    for n,typ in [(4,'split'),(4,'nonsplit'),(5,'odd'),(6,'split'),(6,'nonsplit')]:
      for r in (2,3,4):
       for q in (3,5,7):
        w=(n//2 if typ=='split' else (n-2)//2 if typ=='nonsplit' else n//2)
        rank_sum=sum(isotropic_count(n,q,typ,d)*joint(d,ranks,q) for d in range(w+1) for ranks in product(range(d+1),repeat=r))
        unrefined=sum(isotropic_count(n,q,typ,d)*sum((-1)**j*gauss(d,j,q)*q**(j*(j-1)//2)*q**(r*(d-j)*(d-j+1)//2) for j in range(d+1)) for d in range(w+1))
        assert rank_sum==unrefined
    print('ALL_ORTHOGONAL_FORMULA_CHECKS_PASS')
if __name__=='__main__':test()
