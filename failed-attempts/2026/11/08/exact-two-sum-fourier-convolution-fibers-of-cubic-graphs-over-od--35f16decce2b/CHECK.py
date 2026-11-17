"""Independent integer enumeration of ordered twofold sums of cubic graphs.

Run: python3 CHECK.py. No dependencies beyond Python 3.
"""
from collections import Counter
from fractions import Fraction


def vp(n, p, k):
    n %= p**k
    if n == 0:
        return k
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def root_count(w, p, ell):
    modulus = p**ell
    w %= modulus
    if w == 0:
        return p**(ell//2)
    order = vp(w, p, ell)
    if order % 2:
        return 0
    a = order//2
    u = (w // p**order) % p
    return 2*p**a if pow(u, (p-1)//2, p) == 1 else 0


def predicted_fiber(s, t, p, k):
    q = p**k
    h = vp(3*s, p, k)
    z = (4*t - s**3) % q
    if h == k:
        return q if z == 0 else 0
    m = p**h
    if z % m:
        return 0
    ell = k-h
    unit = (3*s)//m
    w = (z//m)*pow(unit, -1, p**ell) % p**ell
    return m*root_count(w,p,ell)


def formula_energy(p,k):
    q = p**k
    if p == 3:
        return q*q*(2*k*k+4*k+3)//3
    z=Fraction(1,1)+Fraction(k*(p-1),p)+Fraction(k*(k+1)*(p-1)**2,2*p**2)
    ans=z*q*q
    assert ans.denominator == 1
    return ans.numerator


def T(p,ell):
    if ell%2:
        return 1+(p**(ell+1)-1)//(2*(p+1))
    return 1+p*(p**ell-1)//(2*(p+1))


def formula_sumset(p,k):
    if p == 3:
        return p + (p-1)*sum(p**ell*T(p,ell) for ell in range(1,k))
    return 1+(p-1)*sum(p**(ell-1)*T(p,ell) for ell in range(1,k+1))


def test(p,k):
    q=p**k
    counts=Counter()
    for x in range(q):
        xx=pow(x,3,q)
        for y in range(q):
            counts[((x+y)%q,(xx+pow(y,3,q))%q)] += 1
    assert sum(counts.values())==q*q
    # Check every target, including those absent from the image.
    for s in range(q):
        for t in range(q):
            actual=counts.get((s,t),0)
            expected=predicted_fiber(s,t,p,k)
            assert actual==expected,(p,k,s,t,actual,expected)
    actual_energy=sum(a*a for a in counts.values())
    expected_energy=formula_energy(p,k)
    assert actual_energy==expected_energy,(p,k,actual_energy,expected_energy)
    assert len(counts)==formula_sumset(p,k),(p,k,len(counts),formula_sumset(p,k))
    return (p,k,q,len(counts),actual_energy)


def test_composites():
    # Directly enumerate composite-modulus graph sums and compare independent
    # Cartesian-product predictions from two coprime prime-power factors.
    cases = [(15,3,5),(21,3,7),(45,9,5),(75,3,25),(63,9,7),(175,25,7)]
    expected = {3:(3,27),5:(13,61),7:(25,127),9:(15,513),25:(233,2825)}
    for n,a,b in cases:
        counts=Counter()
        for x in range(n):
            for y in range(n):
                counts[((x+y)%n,(pow(x,3,n)+pow(y,3,n))%n)] += 1
        assert len(counts)==expected[a][0]*expected[b][0],(n,'sumset')
        assert sum(c*c for c in counts.values())==expected[a][1]*expected[b][1],(n,'energy')
    return len(cases)


def main():
    cases=[(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(5,1),(5,2),(5,3),(5,4),(7,1),(7,2),(7,3),
           (11,1),(11,2),(13,1),(13,2),(17,1),(17,2),(19,1),(19,2)]
    results=[test(p,k) for p,k in cases]
    composites=test_composites()
    print('CHECK_OK','composite_cases='+str(composites), 'cases='+str(len(results)),
          'targets='+str(sum(q*q for p,k,q,n,e in results)),
          'largest_modulus='+str(max(q for p,k,q,n,e in results)))
    for p,k,q,n,e in results:
        print('p=%s k=%s size=%s sumset=%s energy=%s'%(p,k,q,n,e))

if __name__ == '__main__':
    main()
