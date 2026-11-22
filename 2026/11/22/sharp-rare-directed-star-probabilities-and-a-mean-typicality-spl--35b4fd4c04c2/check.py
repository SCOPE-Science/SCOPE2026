"""Standalone diagnostic checks for sharp rare directed-star tails in random cube orders.

Only finite exact identities and analytic integral evaluations are tested;
asymptotic convergence is established by the supplied proof, not by this code.
Run: python check.py
"""
from fractions import Fraction
from itertools import permutations, product
from math import comb, exp, factorial, gamma, isclose, log

checks = 0

def assert_equal(a,b):
    global checks
    assert a == b, (a,b)
    checks += 1

def assert_near(a,b,rtol=2e-5):
    global checks
    assert isclose(a,b,rel_tol=rtol,abs_tol=rtol), (a,b)
    checks += 1

def exact_expected_stars(n,d,r):
    return Fraction(n*comb(n-1,r), (r+1)**d)

def enumeration_expected_stars(n,d,r):
    # Permutation ranks are iid across coordinates; no grid approximation.
    p = list(permutations(range(n)))
    total = 0
    for ranks in product(p,repeat=d):
        out = [0]*n
        for i in range(n):
            for j in range(n):
                if i != j and all(a[i] < a[j] for a in ranks):
                    out[i] += 1
        total += sum(comb(x,r) for x in out if x>=r)
    return Fraction(total,len(p)**d)

for n in range(3,6):
    for d in (1,2):
        for r in range(2,min(n,4)):
            assert_equal(enumeration_expected_stars(n,d,r),exact_expected_stars(n,d,r))

# At a given fixed hub, the conditional outgoing degree is binomial.
# Verify the exact sieve formula after mixing over the product-uniform cube.
for n in range(3,12):
    for d in range(1,6):
        for r in range(2,min(n,5)):
            sieve=sum(((-1)**(k-r))*comb(k-1,r-1)*Fraction(comb(n-1,k),(k+1)**d)
                      for k in range(r,n))
            # Exactly P(D>=r); compare with a direct binomial-polynomial moment expansion.
            poly=[Fraction(0)]*n
            for k in range(r,n):
                for j in range(n-1-k+1):
                    poly[k+j] += Fraction(comb(n-1,k)*comb(n-1-k,j)*(-1)**j,1)
            direct=sum(poly[k]*Fraction(1,(k+1)**d) for k in range(n))
            assert_equal(sieve,direct)

def poisson_tail(t,r):
    if t>20:
        return 1-exp(-t)*sum(t**j/factorial(j) for j in range(r))
    # Positive-term series avoids subtractive cancellation for tiny t.
    term=exp(-t)*t**r/factorial(r)
    ans=term
    for j in range(r+1,r+120):
        term*=t/j
        ans+=term
        if term<1e-20:
            break
    return ans

def midpoint_integral(r,c,lo=-80.0,hi=80.0,steps=80000):
    width=(hi-lo)/steps
    acc=0.0
    for k in range(steps):
        s=lo+(k+.5)*width
        acc += exp((c-1)*s)*poisson_tail(exp(-s),r)
    return acc*width

for r,c in [(2,2.8),(3,3.2),(4,4.1),(5,4.4),(6,5.1)]:
    integral=midpoint_integral(r,c)
    expected=gamma(r+1-c)/((c-1)*factorial(r-1))
    assert_near(integral,expected)

# The condensation interval is nonempty for every integer r>=2.
for r in range(2,70):
    cstar=(r+1)/log(r+1)
    assert 2.718281828459045<cstar<r+1
    checks+=1
print(f'PASS {checks} finite exact / integral checks')
