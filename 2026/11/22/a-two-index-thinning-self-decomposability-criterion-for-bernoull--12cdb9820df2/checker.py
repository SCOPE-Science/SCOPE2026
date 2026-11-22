"""Exact finite sanity checks for the BPL thinning phase diagram.

The all-index proof is in RESULT.md; these finite computations do not substitute for it.
Requires only Python 3 standard library.
"""
from fractions import Fraction as F


def ingredients(theta, b):
    q = 1 / (1 + theta)
    r = 1 / (2 + theta)
    return q, r


def canonical(k, q, r, b):
    return 2 * q**k - r**k + (-1)**(k + 1) * b**k


def tests(theta, b):
    q, r = ingredients(theta, b)
    d1 = 2 * q * (1-q) - r * (1-r) + b * (1+b)
    d2 = 2 * q*q * (1-q) - r*r * (1-r) - b*b * (1+b)
    return b <= q and d1 >= 0 and d2 >= 0


def original_pmf(k, theta, b):
    alpha = b/(1+b)
    def pl(j):
        if j < 0: return F(0)
        return theta**2 * (j + theta + 2) / (theta + 1)**(j+3)
    return (1-alpha)*pl(k) + alpha*pl(k-1)


def factored_pmf(k, q, r, b):
    norm = (1-q)**2 / ((1+b)*(1-r))
    return norm * ((k+1)*q**k + (b-r)*k*q**(k-1)
                   - b*r*(k-1)*q**(k-2)) if k>=2 else (
                   norm * (1 if k==0 else 2*q+b-r))


cases=0
for tn in range(1,19):
    theta = F(tn,10)
    q, r = ingredients(theta,F(0))
    for j in range(0,36):
        b = q*F(j,30)
        expected = tests(theta,b)
        differences = [canonical(k,q,r,b)-canonical(k+1,q,r,b) for k in range(1,61)]
        assert expected == all(x>=0 for x in differences), (theta,b,expected)
        for k in range(12):
            assert original_pmf(k,theta,b)==factored_pmf(k,q,r,b), (theta,b,k)
        if expected:
            assert all(canonical(k,q,r,b)>0 for k in range(1,61))
            assert sum([differences[k] for k in range(15)], F(0))==canonical(1,q,r,b)-canonical(16,q,r,b)
        cases+=1

# Exact creation-and-destruction witness, with all three choices infinitely divisible.
theta=F(1,10)
q,r=ingredients(theta,F(0))
witness=[]
for b in [F(0),F(1,10),F(1,3)]:
    d1=canonical(1,q,r,b)-canonical(2,q,r,b)
    d2=canonical(2,q,r,b)-canonical(3,q,r,b)
    witness.append((str(b),str(d1),str(d2),tests(theta,b)))
assert [a[-1] for a in witness]==[False,True,False]
assert witness[1][:3]==('1/10','137971/5336100','252509699/12326391000')
print('PASS: %d exact rational grid cases, PMF identities, canonical coefficients' % cases)
print('Creation/destruction at theta=1/10 (b,d1,d2,SD):')
for row in witness:print(row)
