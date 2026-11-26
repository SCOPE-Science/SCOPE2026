"""Exact rational finite-case checks of a conditional variance inequality."""
from fractions import Fraction as F
from itertools import product
from random import Random


def distribution(triples):
    dist={0:F(1)}
    for (a,b,c) in triples:
        nd={}
        for j,v in dist.items():
            for k,w in ((0,a),(1,b),(2,c)):
                nd[j+k]=nd.get(j+k,F(0))+v*w
        dist=nd
    return dist


def moments_on_parity(d,parity):
    sub={k:v for k,v in d.items() if k%2==parity}
    z=sum(sub.values(),F(0))
    if z==0:
        return None
    m=sum((F(k,2)*v for k,v in sub.items()),F(0))/z
    sec=sum((F(k*k,4)*v for k,v in sub.items()),F(0))/z
    return (m,sec-m*m)


def check(triples):
    d=distribution(triples)
    e=moments_on_parity(d,0)
    o=moments_on_parity(d,1)
    if e is None or o is None:
        return False
    dif=e[1]-o[1]
    assert -F(1,4)<=dif<=F(1,4), (triples,dif)
    return True


def run():
    cnt=0
    t=[(F(a,4),F(b,4),F(4-a-b,4))
       for a in range(5) for b in range(5-a)]
    for n in range(1,5):
        for triples in product(t,repeat=n):
            cnt+=bool(check(triples))
    rng=Random(26030919)
    for n in (5,6,7,9):
        for _ in range(300):
            tri=[]
            for __ in range(n):
                a=rng.randrange(14)
                b=rng.randrange(14-a)
                tri.append((F(a,13),F(b,13),F(13-a-b,13)))
            cnt+=bool(check(tri))
    pos=distribution([(F(1,4),F(1,2),F(1,4))])
    neg=distribution([(F(0),F(1),F(0)),(F(1,4),F(1,2),F(1,4))])
    assert moments_on_parity(pos,0)[1]-moments_on_parity(pos,1)[1]==F(1,4)
    assert moments_on_parity(neg,0)[1]-moments_on_parity(neg,1)[1]==-F(1,4)
    print('PASS: %d exact finite-law checks, both sharp endpoint witnesses verified.' % cnt)

if __name__=='__main__':
    run()
