"""Finite consistency checks for the two-coset exponential-basis theorem.

Uses only Python standard library. Infinite completeness/optimality follows
from the analytic proof, not these finite experiments.
"""
import cmath
import math
from fractions import Fraction

N_CHECKS = 0

def close(x, y, tol=2e-11):
    global N_CHECKS
    assert abs(x-y) < tol, (x, y)
    N_CHECKS += 1

def m_at(j):
    if j == 0:
        return 0
    return (j+1)//2 if j % 2 else -(j//2)

def interval(j):
    return (1-2.0**(-j-1), 1-2.0**(-j-2))

def predicted(alpha, m):
    theta = math.pi * alpha * (m + 0.5)
    c = abs(math.cos(theta))
    return (1-c, 1+c)

def eigenvalues_of_gram(alpha, m, t):
    z0 = cmath.exp(2j*math.pi*alpha*t)
    z1 = cmath.exp(2j*math.pi*alpha*(t+m+0.5))
    off = z0+z1
    # Norm-one synthesis coefficient convention: 1/2 times the Gram matrix.
    return (1-abs(off)/2, 1+abs(off)/2)

# Exact geometry of the partition (mass of the unobserved tail = 2^(-n-1)).
for j in range(100):
    lo, hi = interval(j)
    close(hi-lo, 2.0**(-j-2), tol=1e-14)
    assert isinstance(m_at(j), int)
    N_CHECKS += 1
assert len(set(m_at(j) for j in range(101))) == 101
N_CHECKS += 1

# Independent 2x2 complex matrix computation against the displayed formula.
for alpha in (1/3, 2/3, 5/4, -3/7, math.sqrt(2), 1+math.sqrt(2)/100):
    for m in range(-18, 19):
        for t in (0.0, 0.123456789, 0.499):
            actual = eigenvalues_of_gram(alpha, m, t)
            theory = predicted(alpha, m)
            close(actual[0], theory[0])
            close(actual[1], theory[1])

# Exact rational numerator parity test, and the optimal denominatorial bounds.
for b in range(1, 19):
    for a in range(-37, 38):
        if math.gcd(a, b) != 1:
            continue
        frac = Fraction(a,b)
        vals = [abs(math.cos(math.pi * (frac.numerator * (2*m+1)/(2*frac.denominator))))
                for m in range(2*frac.denominator)]
        if a % 2:
            close(max(vals), math.cos(math.pi/(2*b)), tol=3e-13)
        else:
            close(max(vals), 1.0, tol=3e-13)

# An explicit nonframe witness when the numerator is even.
for b in range(1, 17, 2):
    for a in (-8,-4,-2,0,2,4,8):
        if math.gcd(a,b) != 1: continue
        q=Fraction(a,b)
        m=(q.denominator-1)//2
        val=q * Fraction(2*m+1, 2)
        assert val.denominator == 1
        N_CHECKS += 1

# Diophantine small-eigenvalue evidence only (not used as the proof).
for alpha in (math.sqrt(2), math.sqrt(3), 1+math.sqrt(2)/100):
    c=max(abs(math.cos(math.pi*alpha*(m+0.5))) for m in range(-6000,6001))
    assert 1-c < 2e-6
    N_CHECKS += 1

# Direct finite-interval integration of exponential inner products.
def int_exp(freq, l, r):
    if abs(freq)<1e-13:
        return complex(r-l)
    return cmath.exp(2j*math.pi*freq*(l+r)/2) * (r-l) * (
        math.sin(math.pi*freq*(r-l))/(math.pi*freq*(r-l)))

def finite_gram(freq1,freq2,n=33):
    delta=freq1-freq2
    ans=int_exp(delta, 0, .5)
    for j in range(n):
        lo,hi=interval(j)
        shift=m_at(j)
        ans+=int_exp(delta, lo+shift, hi+shift)
    return ans

for a,b in ((1,1), (1,3), (5,4), (-3,7), (2,3)):
    alpha=a/b
    freqs=[-4,-2,0,2,4]+[-4+alpha,-2+alpha,alpha,2+alpha,4+alpha]
    A=1-math.cos(math.pi/(2*b)) if a%2 else 0.0
    B=1+math.cos(math.pi/(2*b)) if a%2 else 2.0
    # Gram diagonal normalization and Hermitian symmetry independently checked.
    gram=[[finite_gram(f,g) for g in freqs] for f in freqs]
    for i in range(len(freqs)):
        close(gram[i][i].real, 1, tol=1e-8)
        for j in range(len(freqs)):
            close(gram[i][j], gram[j][i].conjugate(), tol=1e-10)
    # Testing some coefficient vectors against sharp theoretical envelopes.
    for k in range(15):
        vec=[complex(math.cos(0.6*k+i),math.sin(0.9*k+2*i)) for i in range(10)]
        energy=sum((vec[i].conjugate()*gram[i][j]*vec[j] for i in range(10) for j in range(10))).real
        norm2=sum(abs(x)**2 for x in vec)
        assert (A-1e-6)*norm2<=energy<=(B+1e-6)*norm2, (alpha,energy/norm2,A,B)
        N_CHECKS += 1

print('TWO_COSET_UNBOUNDED_TILE_CHECKS_PASSED',N_CHECKS)
