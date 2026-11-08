"""Finite exact checks for a sparse-degree sign-recoding theorem.

Run: python verify.py
Finite checks test identities, not the martingale functional limit theorem.
"""
from fractions import Fraction
from math import comb, exp, factorial
import itertools

checks = 0

def check(cond, description):
    global checks
    assert cond, description
    checks += 1

# Exact one-degree parity moment.  The M active indicators may be viewed as
# coefficients on M eligible subsets of the negative-coordinate set.
for m in range(0, 13):
    for p in [Fraction(0), Fraction(1, 7), Fraction(1, 3), Fraction(1, 2)]:
        total = sum((-1)**j * comb(m, j) * p**j * (1-p)**(m-j)
                    for j in range(m+1))
        check(total == (1 - 2*p)**m, ("parity",m,p))

# Exact independent multi-degree identity, using a direct convolution of
# independent binomial counts instead of multiplying expected signs.
for sizes in itertools.product(range(0,5), repeat=3):
    if sum(sizes)>9:
        continue
    probs = [Fraction(1,7),Fraction(1,4),Fraction(2,5)]
    distribution={0:Fraction(1)}
    for m,p in zip(sizes,probs):
        newer={}
        for old,val in distribution.items():
            for j in range(m+1):
                newer[old+j]=newer.get(old+j,Fraction(0))+val*comb(m,j)*p**j*(1-p)**(m-j)
        distribution=newer
    signed=sum(((-1)**k)*v for k,v in distribution.items())
    check(signed == (1-2*probs[0])**sizes[0]*(1-2*probs[1])**sizes[1]*(1-2*probs[2])**sizes[2],("mixed",sizes))
    check(sum(distribution.values())==1,("normalization",sizes))

# Compare direct conditional moment (finite n, S_n=floor(n/2)) with the
# stated limiting coefficient for three critical degrees.
for lam in (0.3, 1.0, 3.0):
    for degree in (1,2,3):
        rho=exp(-2*lam/(2**degree*factorial(degree)))
        for n in (5000,10000):
            p=lam/(n**degree)
            direct=(1-2*p)**comb(n//2,degree)
            check(abs(direct-rho)<0.004,('critical asymptotic',lam,degree,n,direct,rho))

# Exact value of the visible count for chosen negative coordinates.
# This verifies the combinatorial intensity used in the proof.
for n in range(1,12):
    for s in range(n+1):
        negative=set(range(s))
        for d in range(1, min(n,4)+1):
            eligible=sum(all(x in negative for x in k)
                         for k in itertools.combinations(range(n), d))
            check(eligible == comb(s,d) if s>=d else eligible==0,
                  ('eligible count',n,s,d))
# The second-order history statistic is a deterministic harmonic weighted sum.
for N in range(1,101):
    weights=[sum((Fraction(1,n) for n in range(j,N+1)),Fraction(0))
             for j in range(1,N+1)]
    harmonic=sum((Fraction(1,j) for j in range(1,N+1)),Fraction(0))
    check(sum(weights)==N,('harmonic covariance',N))
    check(sum(w*w for w in weights)==2*N-harmonic,('harmonic variance',N))

# Equivalent formula for the second-order cross coefficient at a fixed rho.
for degree in (1,2,3,5):
    for rho in (0.1,0.3,0.6,0.9):
        from math import log
        lam=-(2**(degree-1))*factorial(degree)*log(rho)
        a=rho*lam/(2**(degree-1)*factorial(degree-1))
        check(abs(a+degree*rho*log(rho))<1e-12,('coefficient identity',degree,rho))
        v=1-rho**2+2*a*a
        check(v>a*a,('positive covariance',degree,rho))
print(f'PASS: {checks} exact combinatorial/rational and numerical assertions')
