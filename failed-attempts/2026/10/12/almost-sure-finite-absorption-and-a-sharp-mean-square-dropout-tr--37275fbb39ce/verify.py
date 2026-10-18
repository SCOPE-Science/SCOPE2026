"""Exact-rational checks for a Bernoulli error-feedback recurrence.

Run: python3 verify.py
Uses only the Python standard library; these finite tests corroborate the proof.
"""
from fractions import Fraction as F
from itertools import product


def update(x, e, successful):
    u = x + e
    return (x - u, F(0)) if successful else (x, u)


def exhaustive(k, p):
    value = F(0)
    for bits in product((0, 1), repeat=k):
        x, e = F(1), F(0)
        for bit in bits:
            x, e = update(x, e, bit)
        prob = p ** sum(bits) * (1 - p) ** (k-sum(bits))
        value += prob * x*x
    return value


def renewal(n, p):
    q = 1-p
    a = [F(1)]
    for k in range(1, n+1):
        ak = q**k
        for t in range(2, k+1):
            ak += p * q**(t-1) * (t-1)**2 * a[k-t]
        a.append(ak)
    return a


def cubic_recurrence(n, p):
    q = 1-p
    a = [F(1), q, q]
    for k in range(3, n+1):
        a.append(3*q*a[-1] - q*(3*q-p)*a[-2] + q*q*a[-3])
    return a[:n+1]

checks = 0
for p in [F(1,4), F(1,2), F(2,3), F(3,4), F(9,10)]:
    a = renewal(15,p)
    b = cubic_recurrence(15,p)
    for k in range(16):
        assert a[k] == b[k], (p,k,a[k],b[k])
        checks += 1
    for k in range(13):
        assert a[k] == exhaustive(k,p), (p,k)
        checks += 1
    # Renewal-epoch moment multiplier: E[(T-1)^2] = (1-p)(2-p)/p^2.
    q = 1-p
    B = q*(2-p)/(p*p)
    assert (B>1) == (p < F(2,3)), p
    assert (B==1) == (p == F(2,3)), p
    checks += 2
# At the critical p the rational GF denominator factors as
# (1-z)(1+z^2/9), and the coefficient limit is 2/5.
p=F(2,3);q=1-p
assert q*(3*q-p) == F(1,9)
assert q*q == F(1,9)
assert p*p/(1+F(1,9)) == F(2,5)
checks += 3
# Directly check that any two consecutive transmissions leave (x,e)=(0,0).
for k in range(2,10):
    for bits in product((0,1), repeat=k):
        if any(bits[i]==bits[i+1]==1 for i in range(k-1)):
            x,e=F(1),F(0)
            for bit in bits:
                x,e=update(x,e,bit)
            assert (x,e)==(F(0),F(0))
            checks += 1
# An isolating interval for the growing mean-square rate at p=1/2.
def poly(lam):
    return lam**3-F(3,2)*lam**2+F(1,2)*lam-F(1,4)
assert poly(F(126,100)) < 0 < poly(F(127,100))
checks += 1
print(f'PASS: {checks} exact-rational checks; p=1/2 rate in (1.26,1.27), critical limit 2/5')
