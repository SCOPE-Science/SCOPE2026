"""Exact small-field verification of the rank-one-idempotent convolution law.

Run with Python 3 only (no external dependencies). Matrix entries and all
spectral-vanishing tests are handled by finite-field integer arithmetic.
"""
from itertools import product
from fractions import Fraction
from math import prod


def rank_mod(rows, p):
    a = [list(row) for row in rows]
    n, m = len(a), len(a[0])
    i = 0
    for j in range(m):
        k = next((k for k in range(i, n) if a[k][j] % p), None)
        if k is None:
            continue
        a[i], a[k] = a[k], a[i]
        inv = pow(a[i][j] % p, -1, p)
        a[i] = [(x * inv) % p for x in a[i]]
        for k in range(i + 1, n):
            c = a[k][j]
            if c:
                a[k] = [(x - c * y) % p for x, y in zip(a[k], a[i])]
        i += 1
        if i == n:
            break
    return i


def gaussian(n, k, p):
    if not 0 <= k <= n:
        return 0
    numerator = prod(p**(n-i)-1 for i in range(k))
    denominator = prod(p**(k-i)-1 for i in range(k))
    return numerator // denominator


def qprod(n, p):
    return prod(Fraction(1, 1) - Fraction(1, p**j) for j in range(1,n+1))


def moment_formula(n, p, u):
    t = sum(u)
    if t > n:
        return Fraction(0)
    ans = qprod(n,p) / qprod(n-t,p)
    for j in u:
        ans *= Fraction(1,p**(j*j)) / qprod(j,p)
    return ans


def exact_profile_probability(n, p, ks):
    total = Fraction(0)
    for us in product(*(range(k, n+1) for k in ks)):
        if sum(us) > n:
            continue
        weight = prod((-1)**(u-k) * p**((u-k)*(u-k-1)//2) * gaussian(u,k,p) for u,k in zip(us,ks))
        total += weight * moment_formula(n,p,us)
    return total


def idempotents(n,p):
    # Each image line is represented once by its first-nonzero-coordinate-one vector.
    for u in product(range(p), repeat=n):
        if not any(u):
            continue
        if next(x for x in u if x) != 1:
            continue
        for v in product(range(p), repeat=n):
            if sum(a*b for a,b in zip(u,v)) % p == 1:
                yield tuple((u[i]*v[j]) % p for i in range(n) for j in range(n))


def test(n, p, full_fourier=True):
    ids = list(idempotents(n,p))
    assert len(ids) == p**(n-1) * (p**n - 1) // (p-1)
    hist = {}
    allrows = 0
    zeros = 0
    # Test directly the full normalized residue-character sums, not floating roots.
    for v in product(range(p), repeat=n*n):
        A = [v[i*n:(i+1)*n] for i in range(n)]
        dims = tuple(n-rank_mod(tuple(tuple((A[i][j] - (i==j)*lam) % p for j in range(n)) for i in range(n)), p) for lam in range(p))
        hist[dims] = hist.get(dims,0) + 1
        if full_fourier:
            residues = [0]*p
            for P in ids:
                trace = sum(A[i][j]*P[j*n+i] for i in range(n) for j in range(n)) % p
                residues[trace] += 1
            # The absolute constants differ, but spectral coefficients differ as predicted.
            for lam in range(p):
                assert (residues[lam]-residues[0]) * (p-1) == p**(n-1)*(p**dims[lam] - p**dims[0]), (n,p,A,dims,residues)
            assert (len(set(residues))==1) == (len(set(dims))==1), (n,p,A,dims,residues)
        zeros += len(set(dims))==1
        allrows += 1
    assert allrows==p**(n*n)
    # Exact all-multi-index Gaussian moment identity.
    for u in product(range(n+1), repeat=p):
        if sum(u)>n:
            continue
        empirical = sum(Fraction(count, allrows) * prod(gaussian(k,j,p) for k,j in zip(dims,u)) for dims,count in hist.items())
        predicted = moment_formula(n,p,u)
        assert empirical == predicted, (n,p,u,empirical,predicted)
    for ks,count in hist.items():
        assert exact_profile_probability(n,p,ks) == Fraction(count,allrows), (p,n,ks,count)
    print('PASS', 'p',p,'n',n,'idempotents',len(ids), 'frequency_zero_count',zeros,'total',allrows,'zero_ratio',Fraction(zeros,allrows))

if __name__ == '__main__':
    test(2,2)
    test(3,2)
    test(4,2,full_fourier=False)
    test(2,3)
    test(3,3)
    print('IDEMPOTENT_FOURIER_JOINT_MOMENT_CHECKS_OK')
