"""Exact polynomial certificate for target and factor-pair mass identities.
The two differences are rational polynomials of degree at most six.
Seven distinct zero evaluations therefore prove each is identically zero.
Only Python standard library is required.
"""
from fractions import Fraction

def sums(q):
    N=[1,q*q-1,q*(q*q-1),q-1,(q-1)*(q*q-1),
       Fraction(q*(q+1)*(q-1)*(q-2),2),
       Fraction(q*q*(q-1)*(q-1),2)]
    F=[3*q**3-q*q-q,2*q*(q-1),(q-1)*(2*q-1),
       q*q*(q-1),q*(q-1),(q-1)*(q-1),q*q-1]
    return sum(N),sum(a*b for a,b in zip(N,F))
for q in range(2,9):
    t,p=sums(q)
    assert (t,p)==(q**4,q**6),(q,t,p)
    print(f'PASS q={q} targets={t} factor_pairs={p}')
print('POLYNOMIAL_MASS_IDENTITIES_PASS degree_at_most_6 seven_evaluations')
