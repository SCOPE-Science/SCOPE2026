"""Exact finite checks for a two-rank pointed order polytope.
Only built-in Python modules are needed. These tests support, but do not replace, the proof.
"""
from fractions import Fraction
from math import comb, factorial
from random import Random


def integral_polynomial(p, q, extra_power=0):
    """Integrate q*t^extra_power*(1+t)^(p-1)*(1-t)^(q-1) on [0,1]."""
    total = Fraction()
    for i in range(p):
        for j in range(q):
            total += Fraction(q*comb(p-1, i)*comb(q-1,j)*(-1)**j, i+j+extra_power+1)
    return total


def volume_binomial(p,q):
    return Fraction(factorial(p-1)*factorial(q),factorial(p+q-1))*sum(comb(p+q-1,k) for k in range(p))


def volume_sign_pattern(p,q):
    return sum((Fraction(comb(p-1,k)*factorial(k)*factorial(q),factorial(q+k)) for k in range(p)),Fraction())


def trial(p,q,rng):
    # Exact order-statistic sampler, conditional on positive lower-coordinate count.
    weights=[Fraction(comb(p-1,k)*factorial(k)*factorial(q),factorial(q+k)) for k in range(p)]
    # float weights only in stochastic diagnostics; exact rational theorem does not rely on this step.
    z=rng.random()*float(sum(weights))
    cum=0.
    for k,w in enumerate(weights):
        cum+=float(w)
        if z<=cum:break
    else: k=p-1
    ids=list(range(p-1)); rng.shuffle(ids)
    positive=ids[:k]
    v=sorted(rng.random() for _ in range(k+q))
    lower=[-rng.random() for _ in range(p-1)]
    tmp=v[:k]; rng.shuffle(tmp)
    for j,i in enumerate(positive):lower[i]=tmp[j]
    upper=v[k:]; rng.shuffle(upper)
    assert all(-1<=x<=1 for x in lower+upper)
    assert all(x<=y for x in lower for y in upper)
    assert all(0<=y<=1 for y in upper)
    return min(upper), k


def run():
    exact=0
    for p in range(1,20):
        for q in range(1,20):
            v0=integral_polynomial(p,q)
            v1=volume_binomial(p,q)
            v2=volume_sign_pattern(p,q)
            assert v0==v1==v2, (p,q,v0,v1,v2)
            assert v0>0
            for power in (1,2,3):
                numerator=integral_polynomial(p,q,power)
                assert Fraction(0)<numerator<v0
                exact+=1
            exact+=1
    rng=Random(17891)
    n=35000
    for p,q in [(2,3),(4,4),(8,3),(3,9)]:
        ts=[trial(p,q,rng)[0] for _ in range(n)]
        theor=float(integral_polynomial(p,q,1)/volume_binomial(p,q))
        avg=sum(ts)/n
        assert abs(avg-theor)<.018,(p,q,avg,theor)
        print('sample',p,q,'mean',round(avg,6),'exact',round(theor,6))
    print('PASS: 361 exact volume equalities, 1083 exact moment bounds,',n*4,'valid sampled points')

if __name__=='__main__':run()
