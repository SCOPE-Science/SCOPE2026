"""Exact checks for three-vertex edge dependence in attribute-intersection graphs.

Run: python3 verify.py. Uses only Python's standard library.
For each attribute, all eight membership configurations are enumerated independently.
No simulation or floating-point arithmetic is used.
"""
from fractions import Fraction
from itertools import product

EDGES = ((0, 1), (0, 2), (1, 2))


def graph_from_members(m):
    return sum((1 << k) for k, (u, v) in enumerate(EDGES) if m >> u & 1 and m >> v & 1)


def exact_three_graph_law(probs):
    law = {0: Fraction(1)}
    for p in probs:
        feature = {b: Fraction(0) for b in range(8)}
        for mask in range(8):
            k = mask.bit_count()
            feature[graph_from_members(mask)] += p**k * (1-p)**(3-k)
        new = {b: Fraction(0) for b in range(8)}
        for g, pg in law.items():
            for h, ph in feature.items():
                new[g | h] += pg*ph
        law = new
    return law


def certificate(probs):
    x = y = z = Fraction(1)
    for p in probs:
        a = 1-3*p*p+2*p**3
        b = p*p*(1-p)
        u = a+b
        v = a+2*b
        assert u*u > a*v
        assert u > v*v
        x *= a
        y *= u
        z *= v
    p0,p1,p2,p3 = x,y-x,z-2*y+x,1-3*z+3*y-x
    assert p0>0 and p1>0 and p2>=0 and p3>0
    assert x*z-y*y < 0
    assert (y-x)*(1-z)-(z-y)**2 > 0
    return p0,p1,p2,p3


def check_one(probs):
    law = exact_three_graph_law(probs)
    p0,p1,p2,p3 = certificate(probs)
    for mask in range(8):
        k = mask.bit_count()
        assert law[mask] == (p0,p1,p2,p3)[k]
    assert sum(law.values())==1
    e12_none = sum(v for k,v in law.items() if k & 1 == 0)
    assert e12_none == p0+2*p1+p2
    c0 = (p0*p2-p1*p1)/e12_none**2
    c1 = (p1*p3-p2*p2)/(1-e12_none)**2
    assert c0 < 0 < c1
    # Unconditional adjacent-edge covariance: both events are increasing
    # functions of independent underlying Bernoulli membership variables.
    mass_a = sum(v for k,v in law.items() if k & 1)
    mass_b = sum(v for k,v in law.items() if k & 2)
    both = sum(v for k,v in law.items() if k & 1 and k & 2)
    assert both-mass_a*mass_b > 0
    return c0,c1


def main():
    values = [Fraction(1,5),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(4,5)]
    count = 0
    for length in range(1,5):
        for probs in product(values, repeat=length):
            check_one(probs)
            count += 1
    example = check_one([Fraction(1,2)])
    assert example==(Fraction(-1,36),Fraction(1,4)),example
    print('PASS:',count,'heterogeneous feature sequences; full eight-state laws; exact conditional signs; unconditional signs')
    print('one attribute with p=1/2: conditional missing/present covariances:',*example)

if __name__=='__main__':main()
