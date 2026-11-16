"""Exact combinatorial checks of the prime quadratic-chirp triple-phase law.

Run with Python 3: python check_mub_phase.py
No external dependencies.  Numerical spot checks use the defining vector inner products.
"""
from collections import Counter
from itertools import permutations, product
from math import pi, sqrt
from cmath import exp


def chi(x, p):
    x %= p
    return 0 if x == 0 else (1 if pow(x, (p-1)//2, p) == 1 else -1)


def symbolic_phase(bases, labels, p):
    """Return (sign, exponent) for tau / eps**3 = sign * zeta**exponent."""
    if -1 not in bases:
        b0, b1, b2 = bases
        a0, a1, a2 = labels
        B = (b1-b0)*(b2-b1)*(b0-b2) % p
        D = ((b2-b0)*(a1-a0)-(b1-b0)*(a2-a0)) % p
        s = D*D*pow(4*B % p,-1,p) % p
        return chi(B,p),s
    # Rotate cyclically so the standard-basis vector occurs first.
    idx = bases.index(-1)
    bb = bases[idx:]+bases[:idx]
    aa = labels[idx:]+labels[:idx]
    t, a1, a2 = aa
    db = (bb[2]-bb[1]) % p
    da = (a2-a1) % p
    q = (t + da*pow(2*db%p,-1,p)) % p
    s = (-db*q*q) % p
    return chi(-db,p),s  # eps*chi(db)/eps**3 = chi(-db)


def exhaustive(p):
    bases = [-1]+list(range(p))
    counts = Counter()
    nonzero_base_triples = 0
    for bb in permutations(bases,3):
        nonzero_base_triples += 1
        for aa in product(range(p),repeat=3):
            counts[symbolic_phase(bb,aa,p)] += 1
    M=p*(p*p-1)
    C=M*p*p
    assert nonzero_base_triples == M
    # The p-1 nonzero phases have fixed chi(s), and both zero phases occur.
    expected = Counter({(1,0):C//2,(-1,0):C//2})
    expected.update({(chi(s,p),s):C for s in range(1,p)})
    assert counts == expected, (p,counts-expected,expected-counts)
    assert sum(counts.values()) == M*p**3
    return len(counts),C,sum(counts.values())


def vector(b,a,p):
    if b == -1:
        return [1.0+0j if j==a else 0j for j in range(p)]
    z = exp(2j*pi/p)
    return [z**((a*t+b*t*t)%p)/sqrt(p) for t in range(p)]


def inner(u,v):
    return sum(x.conjugate()*y for x,y in zip(u,v))


def numerical_samples(p):
    z=exp(2j*pi/p)
    eps=1.0+0j if p%4==1 else 1j
    bases=[-1]+list(range(p))
    samples=0
    max_error=0.0
    for bb in permutations(bases,3):
        # Deterministic grid of 3 vectors per each basis triple.
        for a0 in (0,p-1):
            aa=(a0,(2*a0+1)%p,(3*a0+2)%p)
            vs=[vector(b,a,p) for b,a in zip(bb,aa)]
            got=(p**1.5)*inner(vs[0],vs[1])*inner(vs[1],vs[2])*inner(vs[2],vs[0])
            sg,ex=symbolic_phase(bb,aa,p)
            predicted=eps**3*sg*z**ex
            max_error=max(max_error,abs(got-predicted))
            samples+=1
    assert max_error < 1e-11,(p,max_error)
    return samples,max_error


def full_tensor_arg0_count(p):
    N=p*(p+1)
    M=p*(p*p-1)
    C=M*p*p
    baseline=N**3-M*p**3
    return baseline+(C//2 if p%4==1 else 0)


def main():
    for p in (3,5,7,11):
        phases,C,count=exhaustive(p)
        print('EXACT_PHASE_HIST',p,'phases',phases,'nonzero_triples',count,'per_nonzero_phase',C)
    for p in (3,5,7,11):
        n,err=numerical_samples(p)
        print('DIRECT_INNER_PRODUCTS',p,'cases',n,'maximum_error',f'{err:.2e}')
    # Check published dimension-3 and dimension-5 phase-zero multiplicities.
    assert full_tensor_arg0_count(3)==1080
    assert full_tensor_arg0_count(5)==13500
    for p in (3,5,7,11):
        distinct=((p+3)//2 if p%4==1 else (p+1)//2)
        print('THREE_COLUMN_GRAM_TYPES',p,distinct)
    print('PRIME_MUB_BARGMANN_HISTOGRAM_PASS')

if __name__=='__main__':
    main()
