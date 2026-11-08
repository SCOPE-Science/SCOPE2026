"""Exact finite checks for EF1 allocation of independent binary lottery goods.

Run: python verify.py
Uses only the Python standard library. These checks supplement the proof.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def cdf(b, p, t):
    return sum(F(comb(b, k)) * p**k * (1-p)**(b-k)
               for k in range(min(b, t) + 1))


def formula(a, b, p, q):
    def row(x, y, z):
        return sum(F(comb(x, k)) * z**k * (1-z)**(x-k)
                   * cdf(y, z, k+1) for k in range(x+1))
    return row(a,b,p) * row(b,a,q)


def exhaustive(a, b, p, q):
    m=a+b
    masks=list(product((0,1), repeat=m))
    def mass(bits, prob):
        k=sum(bits)
        return prob**k * (1-prob)**(m-k)
    mp=[mass(x,p) for x in masks]
    mq=[mass(x,q) for x in masks]
    out=F(0)
    for x, px in zip(masks,mp):
        if sum(x[:a])+1 < sum(x[a:]):
            continue
        for y,py in zip(masks,mq):
            if sum(y[a:])+1 >= sum(y[:a]):
                out += px*py
    return out


def balanced_value(p,q):
    f=lambda z: 1-z*z*(1-z)**2
    return f(p)*f(q)


def singleton_value(p):
    return 1-3*p*p+5*p**3-3*p**4


def weight(a,b,x,y):
    return x*x*comb(b,2)+y*y*comb(a,2)


def main():
    tests=0
    pairs=[(F(1,7),F(2,7)),(F(1,4),F(3,4)),
           (F(1,2),F(1,2)),(F(1,100),F(1,10)),
           (F(3,5),F(4,5)),(F(9,10),F(1,5))]
    for m in range(1,6):
        for p,q in pairs:
            values=[]
            for a in range(m+1):
                exact=exhaustive(a,m-a,p,q)
                assert exact==formula(a,m-a,p,q),(m,a,p,q,exact)
                values.append(exact)
                tests+=1
            best=max(values)
            if m<=3:
                assert all(max(a,m-a)-min(a,m-a)<=1
                           for a,v in enumerate(values) if v==best)
            if m==4:
                assert best==max(balanced_value(p,q),
                                 singleton_value(min(p,q)))
                assert values[2]==balanced_value(p,q)
                assert values[1]==singleton_value(p)
                assert values[3]==singleton_value(q)
    assert singleton_value(F(1,100))==F(99970497,100000000)
    assert balanced_value(F(1,100),F(1,10))==F(991802783881,10**12)
    for m in range(2,9):
        for x,y in [(1,1),(1,2),(2,3),(1,4),(3,1)]:
            eps=F(1,10**7)
            for a in range(m+1):
                loss=(1-formula(a,m-a,eps*x,eps*y))/(eps*eps)
                assert abs(loss-weight(a,m-a,x,y))<F(1,1000)
                tests+=1
            theta=F((m-1)*x*x,x*x+y*y)
            if theta.denominator!=1:
                a_star=theta.numerator//theta.denominator+1
                vals=[formula(a,m-a,eps*x,eps*y) for a in range(m+1)]
                assert vals.index(max(vals))==a_star,(m,x,y,a_star,vals)
    print('PASS: %d exact and rare-event consistency checks' % tests)
    print('Exact four-good example gap:',
          singleton_value(F(1,100))-balanced_value(F(1,100),F(1,10)))

if __name__=='__main__':
    main()
