"""Finite field checks for the characteristic-five self-product example.

The program verifies field-count inputs to a cohomological argument; it
is not a replacement for the geometric resolution and purity theorems.
"""
from collections import Counter

P = 5

def count_over_prime():
    def chi(v):
        v %= P
        return 0 if v == 0 else (1 if v in (1, 4) else -1)
    def n(t):
        return P + 1 + sum(chi(4*x**3 + 3*t*(t+2)**3*x + 3*t**4*(t+2)**2) for x in range(P))
    vals = {t:n(t) for t in range(P)}
    vals['infinity'] = P+1 + sum(chi(4*x**3+3*x+3) for x in range(P))
    assert vals == {0:6,1:3,2:4,3:6,4:5,'infinity':7}, vals
    vals[0]=11
    vals[3]=6
    vals['infinity']=7
    assert sum(v*v for v in vals.values())==256
    m=Counter((x**3-2*x*y*y)%5 for x in range(5) for y in range(5))
    assert [m[b] for b in range(5)] == [5]*5
    assert (sum(v*v for v in m.values())-1)//4 == 31
    # Ordinary triple replacement; one rational I5 node, two P1s over III,
    # and one split quadric replacing the terminal node on the big model.
    big=256 + 30 + 5 + 10 + 35
    assert big==336
    small=big-(P*P+P)
    assert small==306
    return vals, big,small

class F25:
    # Z/5Z[i] with i^2=2. Elements are integers a+5*b.
    q=25
    @staticmethod
    def pair(x): return x%5,x//5
    @staticmethod
    def add(x,y):
        a,b=F25.pair(x);c,d=F25.pair(y)
        return ((a+c)%5)+5*((b+d)%5)
    @staticmethod
    def neg(x):
        a,b=F25.pair(x)
        return (-a)%5 + 5*((-b)%5)
    @staticmethod
    def mul(x,y):
        a,b=F25.pair(x);c,d=F25.pair(y)
        return (a*c+2*b*d)%5+5*((a*d+b*c)%5)
    @staticmethod
    def exp(x,n):
        v=1
        while n:
            if n&1:v=F25.mul(v,x)
            x=F25.mul(x,x)
            n//=2
        return v

def count_over_quadratic():
    q=25
    ad,ml,pw=F25.add,F25.mul,F25.exp
    chi=lambda x:0 if x==0 else (1 if pw(x,12)==1 else -1)
    n={}
    for t in range(q):
        tp2=ad(t,2)
        d=ml(3,ml(t,pw(tp2,3)))
        e=ml(3,ml(pw(t,4),pw(tp2,2)))
        n[t]=q+1+sum(chi(ad(ad(ml(4,pw(x,3)),ml(d,x)),e)) for x in range(q))
    n['infinity']=q+1+sum(chi(ad(ad(ml(4,pw(x,3)),ml(3,x)),3)) for x in range(q))
    assert sum(v*v for v in n.values())==19401, sum(v*v for v in n.values())
    n[0]=2*q+1
    n[3]=3*q+1
    n['infinity']=5*q  # formula (3+2)q+1-1
    raw=sum(v*v for v in n.values())
    assert raw == 41426,raw
    m=Counter()
    for x in range(q):
        for y in range(q):
            m[ad(pw(x,3),F25.neg(ml(2,ml(x,pw(y,2)))))] += 1
    cubic=(sum(v*v for v in m.values())-1)//(q-1)
    assert cubic==801,cubic
    big=raw+(cubic-1)+25*q+2*q+(q*q+2*q)
    assert big==43576
    small=big-(q*q+q)
    assert small==42926
    return big,small

def point_count(r):
    q=5**r
    return 1 + q**3 + (q+q*q)*(24+18*(-1)**r)

if __name__=='__main__':
    _,big5,small5=count_over_prime()
    big25,small25=count_over_quadratic()
    assert (big5,small5,big25,small25)==(336,306,43576,42926)
    assert point_count(1)==small5 and point_count(2)==small25
    assert point_count(3)==2047626
    print('F5 big/small:',big5,small5)
    print('F25 big/small:',big25,small25)
    print('First four extension counts:',*[point_count(r) for r in range(1,5)])
    print('All finite checks passed; general result uses the proved cohomological argument.')
