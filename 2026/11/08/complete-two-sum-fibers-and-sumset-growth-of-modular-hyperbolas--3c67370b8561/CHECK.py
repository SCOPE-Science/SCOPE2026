"""Exact integer checks for twofold sums of modular hyperbolas."""
from collections import Counter
from math import gcd


def phi_pk(p, k):
    return (p - 1) * p ** (k - 1)


def val(a, p, k):
    if a == 0:
        return k
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v


def sqrt_count(delta, p, m):
    if delta == 0:
        return p ** (m // 2)
    w = val(delta, p, m)
    if w % 2:
        return 0
    j = w // 2
    unit = (delta // (p ** w)) % p
    return 2 * p ** j if pow(unit, (p-1)//2, p) == 1 else 0


def multiplicity(s, t, p, k):
    q = p ** k
    vs, vt = val(s, p, k), val(t, p, k)
    if vs == k:
        return phi_pk(p, k) if vt == k else 0
    if vs != vt:
        return 0
    v = vs
    m = k - v
    h = p ** m
    a = s // p ** v
    b = t // p ** v
    delta = (s*s - 4 * a * pow(b, -1, h)) % h
    return p ** v * sqrt_count(delta, p, m)


def target_counts(p, k):
    phi = phi_pk(p, k)
    q = p ** k
    special_squares = 1 + sum(phi_pk(p, k-2*j) // 2 for j in range(1, (k-1)//2 + 1))
    positive_unit_s = (p-3) * p**(k-1) // 2 + special_squares
    size = 1 + phi * positive_unit_s + sum(phi_pk(p, m)**2 // 2 for m in range(1, k))
    energy = 3*(p-1)*p**(2*k-2)*(k*(p-1)-1)
    return size, energy


def factor_prime_powers(n):
    factors = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            k=0
            while n%d==0:
                k+=1;n//=d
            factors.append((d,k))
        d+=1
    if n>1:
        factors.append((n,1))
    return factors


def check(q, pk=None):
    units = [x for x in range(q) if gcd(x,q)==1]
    inverse = {x:pow(x,-1,q) for x in units}
    data = Counter()
    for x in units:
        for y in units:
            data[((x+y)%q, (inverse[x]+inverse[y])%q)] += 1
    if pk is not None:
        p,k=pk
        for s in range(q):
            for t in range(q):
                expected = multiplicity(s,t,p,k)
                actual = data[(s,t)]
                if actual != expected:
                    raise AssertionError((q,s,t,actual,expected))
        size,energy=target_counts(p,k)
    else:
        factors=factor_prime_powers(q)
        assert all(p%2==1 for p,k in factors)
        for (s,t),number in data.items():
            predicted=1
            for p,k in factors:
                mod=p**k
                predicted *= multiplicity(s%mod,t%mod,p,k)
            assert number==predicted
        size,energy=1,1
        for p,k in factors:
            s,e=target_counts(p,k)
            size*=s;energy*=e
    got_size = len(data)
    got_energy = sum(v*v for v in data.values())
    assert got_size==size, (q,got_size,size)
    assert got_energy==energy, (q,got_energy,energy)
    assert sum(data.values())==len(units)**2
    return got_size,got_energy,len(data)

if __name__=='__main__':
    checks=0; targets=0
    for p,k in [(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,3),(7,1),(7,2),(7,3),(11,1),(11,2),(13,1)]:
        s,e,count=check(p**k,(p,k));checks+=1;targets+=p**(2*k)
        print('prime_power',p,k,s,e)
    for n in [15,21,33,45,63,75,105,135,175]:
        s,e,count=check(n);checks+=1;targets+=n*n
        print('composite',n,s,e)
    print(f'CHECK_OK moduli={checks} target_slots={targets} all_multiplicities_exact=True')
