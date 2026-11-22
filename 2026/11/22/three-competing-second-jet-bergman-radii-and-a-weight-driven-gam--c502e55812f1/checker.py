"""Exact rational diagnostics for weighted Bergman two-jet monomial capture.

Uses only Python's standard library. Checks are finite diagnostics; the
all-degree statement and limiting arguments have analytic proofs.
"""
from fractions import Fraction as F
from math import factorial


def mul(a, b):
    ans = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ans[i+j] += x*y
    return ans


def add(a, b):
    ans = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a): ans[i] += v
    for i, v in enumerate(b): ans[i] += v
    return ans


def scale(a, k): return [k*x for x in a]


def derivative(a): return [i*a[i] for i in range(1, len(a))] or [F(0)]


def rising(a, k):
    v = F(1)
    for i in range(k): v *= a+i
    return v


def falling(a, k):
    v = F(1)
    for i in range(k): v *= a-i
    return v


def Q(n, beta, j):
    from math import comb
    return [F((-1)**(j-a)*comb(j,a))*falling(n,j-a)*rising(n+beta,a)
            for a in range(j+1)]


def poly_value(p, x):
    v = F(0)
    for a in reversed(p): v = v*x+a
    return v


def invert(a):
    N = len(a)
    a = [[F(v) for v in row] + [F(int(i==j)) for j in range(N)]
         for i, row in enumerate(a)]
    for k in range(N):
        i = next(i for i in range(k,N) if a[i][k])
        a[k], a[i] = a[i], a[k]
        d = a[k][k]
        a[k] = [x/d for x in a[k]]
        for i in range(N):
            if i != k:
                d=a[i][k]
                a[i] = [u-d*v for u,v in zip(a[i],a[k])]
    return [row[N:] for row in a]


def gram(beta, r):
    from math import comb
    x=r*r
    result=[]
    for j in range(3):
        row=[]
        for k in range(3):
            z=F(0)
            for a in range(min(k,j)+1):
                z += (F(comb(k,a))*falling(j,a)*rising(beta,j)*
                      rising(beta+j,k-a)*r**(j+k-2*a)*
                      (1-x)**(-beta-j-k+a))
            row.append(z)
        result.append(row)
    return result


def capture(n,beta,x):
    cn=rising(beta,n)/factorial(n)
    s=F(0)
    for j in range(3):
        q=poly_value(Q(n,beta,j),x)
        s+=x**(n-j)*q*q/(factorial(j)*rising(beta,j))
    return cn*(1-x)**beta*s


class Interval:
    def __init__(self,a,b=None):
        self.a=F(a); self.b=F(a if b is None else b)
        assert self.a<=self.b
    def __add__(self,o):
        o=o if isinstance(o,Interval) else Interval(o)
        return Interval(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Interval(-self.b,-self.a)
    def __sub__(self,o): return self+(-o if isinstance(o,Interval) else -Interval(o))
    def __rsub__(self,o): return Interval(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Interval) else Interval(o)
        p=[a*b for a in (self.a,self.b) for b in (o.a,o.b)]
        return Interval(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,Interval) else Interval(o)
        assert o.a>0
        return self*Interval(1/o.b,1/o.a)
    def square(self):
        return Interval(F(0) if self.a<=0<=self.b else min(self.a*self.a,self.b*self.b),
                        max(self.a*self.a,self.b*self.b))


def exp_minus_bounds(x,terms=80):
    # Taylor's Lagrange remainder: e^{-x} is within x^{N+1}/(N+1)!
    # of its Nth Maclaurin polynomial for x >= 0.
    s=sum((-x)**k/F(factorial(k)) for k in range(terms+1))
    err=x**(terms+1)/F(factorial(terms+1))
    return s-err,s+err


def H2_interval(lo,hi):
    t=Interval(F(lo),F(hi))
    polynomial = t.square() * (1+(2-t).square()/2+
                             (t*t-6*t+6).square()/12)
    exp=Interval(exp_minus_bounds(t.b)[0],exp_minus_bounds(t.a)[1])
    return polynomial*exp


def run():
    checks=0
    for beta in [F(2),F(3),F(5),F(7,2)]:
        for n in range(3,14):
            q1,q2,q3=(Q(n,beta,j) for j in (1,2,3))
            S=add(add([F(0),F(0),F(1)],scale(mul([F(0),F(1)],mul(q1,q1)),1/beta)),
                  scale(mul(q2,q2),1/(2*beta*(beta+1))))
            deriv=add(add(scale(mul([F(1),F(-1)],S),n-2),
                          scale(mul([F(0),F(1)],S),-beta)),
                      mul([F(0),F(1),F(-1)],derivative(S)))
            assert all(a==0 for a in add(deriv,scale(mul(q2,q3),1/(2*beta*(beta+1)))))
            checks+=1
    for beta in [2,3,5]:
        for n in [3,4,6,9,13]:
            cn=rising(beta,n)/factorial(n)
            for r in [F(1,4),F(1,3),F(2,3)]:
                ginv=invert(gram(beta,r))
                jets=[falling(n,j)*r**(n-j) for j in range(3)]
                direct=cn*sum(jets[i]*ginv[i][j]*jets[j]
                              for i in range(3) for j in range(3))
                assert direct == capture(n,beta,r*r)
                checks+=1
    # Three isolated Laguerre L_3^1 roots: t^3-12t^2+36t-24=0.
    brackets=[('0.935','0.937',F(58,100),F(59,100)),
              ('3.305','3.306',F(102,100),F(103,100)),
              ('7.758','7.760',F(127,100),F(129,100))]
    p=lambda t: 24-36*t+12*t*t-t*t*t
    for a,b,lower,upper in brackets:
        a,b=F(a),F(b)
        assert p(a)*p(b)<0
        h=H2_interval(a,b)
        assert lower<h.a and h.b<upper
        checks+=3
    assert checks == 98
    print('PASS:',checks,'finite exact-rational identities, independent Gram checks, and interval certificates')


if __name__=='__main__':run()
