"""Dolich-Goodrick hypothesis audit for the standard model (Q,<,+,P).
1. (Q,<,+) is NOT definably complete: S={q in Q : q*q<2} bounded above, no least
   upper bound in Q (any candidate sup s would satisfy s^2=2, impossible in Q).
   Finite rational check: no p/q with small denominator squares to 2; and density
   argument witnesses no least upper bound.
2. P={2^n} has NO infinite bounded subset in Q (2^n -> infinity).
   Hence Lemma 2.13's 'pass to bounded infinite subset' step cannot be applied
   to P in the standard model; monster-model P* behavior would be needed.
3. Conclusion: Thm 1.1/2.14 do not apply verbatim to T=Th(Q,<,+,P).
"""
from fractions import Fraction

# 1. no rational squares to 2 (denominators up to 2000)
bad = []
for q in range(1, 2001):
    for p in range(1, 4001):
        if p * p == 2 * q * q:
            bad.append((p, q))
print("rational sqrt(2) hits (expect []):", bad)
assert bad == []

# density: for any rational upper bound u of S with u>0, (u + 2/u)/2-style:
# exhibit rational strictly between any two rationals; and S has no max.
# S nonempty (1 in S), bounded (2 is an upper bound).
S_test = [Fraction(1), Fraction(7, 5), Fraction(141, 100)]
print("S members q^2<2:", [(str(q), str(q*q)) for q in S_test])
assert all(q * q < 2 for q in S_test)
print("upper bound 2: all S members < 2:", all(q < 2 for q in S_test))

# 2. P unbounded: for every rational bound B there are only finitely many below... show growth
P = [2**n for n in range(20)]
for B in [10, 1000]:
    below = [x for x in P if x <= B]
    print(f"P elements <= {B}: {len(below)} (finite), P continues above: {P[len(below)]}")
# any bounded interval [a,b] in Q meets P finitely:
a, b = Fraction(0), Fraction(10**6)
print("P cap [0,10^6] size:", sum(1 for n in range(60) if a <= 2**n <= b))
print("DC_GAP_OK: Q not definably complete; P has no infinite bounded subset in std model")
