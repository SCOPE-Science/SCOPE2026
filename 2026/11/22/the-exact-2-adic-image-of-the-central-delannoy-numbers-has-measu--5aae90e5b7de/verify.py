"""Independent finite arithmetic checks of the stated analytic certificates.
The infinite image theorem also uses the explicit tail bounds and analytic identities
proved in RESULT.md; these finite tests are not an infinite proof.
"""
from fractions import Fraction
from math import factorial

def multiply(p, q):
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out

def truncated_branch(b, last):
    total = [Fraction(0)] * (2*last+1)
    for j in range(last+1):
        poly = [Fraction(1)]
        for h in range(j):
            poly = multiply(poly, [Fraction(b-h), Fraction(4)])
        term = multiply(poly, poly)
        term = [c*Fraction(2**j, factorial(j)**2) for c in term]
        for i, value in enumerate(term):
            total[i] += value
    return total

def v2(q):
    if q == 0: return 1000000
    a, b = abs(q.numerator), q.denominator
    return (a & -a).bit_length() - (b & -b).bit_length()

# Check the exact finite polynomial congruences in Q_2[u].
for b, top, precision, target in ((0,8,7,{0:1, 3:64}),
                                   (1,6,5,{0:3, 1:16}),
                                   (2,6,5,{0:13, 1:16})):
    coeff = truncated_branch(b, top)
    for power, actual in enumerate(coeff):
        assert v2(actual-target.get(power, 0)) >= precision, (b, power)

# The following exact lower bounds hold for every j beyond the finite truncations.
# For b=0, L=4-j+2 floor((j-1)/2)+2 floor((j-1)/4)+2 s_2(j).
# At j=9 L>=7, while j>=10 implies L>=j/2+2>=7.
# For b=1,2, L>=-j+2 floor(j/2)+2 floor(j/4)+2 s_2(j).
# At j=7..10 this is >=5; for j>=11 it is >=j/2-1/2>=5.
def popcount(j): return j.bit_count()
for j in range(9, 128):
    L = 4-j+2*((j-1)//2)+2*((j-1)//4)+2*popcount(j)
    assert L>=7
for j in range(7,128):
    L = -j+2*(j//2)+2*(j//4)+2*popcount(j)
    assert L>=5

# Exact modular Delannoy recurrence, plus an independently described predicted set.
values = [1, 3]
for n in range(2, 2049):
    numerator = 3*(2*n-1)*values[-1]-(n-1)*values[-2]
    assert numerator % n == 0
    values.append(numerator//n)
for k in range(1, 12):
    modulus = 1<<k
    observed = {n % modulus for n in values[:(1<<(k+1))]}
    if k < 4:
        assert len(observed) == (1<<max(0,k-1))
    else:
        predicted = {n for n in range(modulus) if n%16 in (3,13)}
        predicted.update((1%modulus, (-1)%modulus))
        for a in range(2, (k-1)//3+1):
            depth = 1 << (3*a)
            predicted.update(n for n in range(modulus)
                             if (n-1)%depth==0 and ((n-1)//depth)%2==1)
            predicted.update(n for n in range(modulus)
                             if (n+1)%depth==0 and ((n+1)//depth)%2==1)
        expected_count = (1<<(k-3))+2+sum(1<<(k-3*a)
                                           for a in range(2,(k-1)//3+1))
        assert len(predicted)==expected_count
        assert observed==predicted, (k,len(observed),len(predicted))
print('CHECK_OK: exact branch certificates, tail bounds, and finite image sets through 2^11')
