# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Rank lower bound, torsion restriction, and Jacobian orders for C: y^2 = x^5 - 4x + 1 (from-scratch, stdlib-only)

## 1. Statement of proved results

Let C be the affine model y^2 = f(x), f(x) = x^5 - 4x + 1, with smooth
projective completion (one point at infinity, denoted inf, since deg f = 5
is odd). Let J be its Jacobian. The following are PROVED:

1. disc(f) = -259019, which is prime (verified by trial division to
   sqrt(259019) < 510). Hence f is separable, C is a smooth genus-2 curve,
   and 7 is a prime of good reduction (disc mod 7 = 2 != 0).
2. Point counts (one point at infinity throughout):
   #C(F3)=7, #C(F5)=6, #C(F7)=11, #C(F11)=19, #C(F13)=17,
   computed by brute-force affine enumeration over Fp and over
   Fp^2 = Fp[t]/(irreducible quadratic) with square-membership counting.
3. Jacobian orders via the genus-2 Weil polynomial from N1=#C(Fp),
   N2=#C(Fp^2): with s1 = p+1-N1, S2 = p^2+1-N2, e2 = (s1^2-S2)/2,
   #J(Fp) = 1 - s1 + e2 - p*s1 + p^2:
   #J(F3)=29 (prime), #J(F5)=36, #J(F7)=81, #J(F11)=237=3*79, #J(F13)=222.
4. D = [(0,1) - inf] has infinite order in J(Q). Hence rank J(Q) >= 1.
5. J(Q)_tors is either trivial or Z/3.
6. COMPUTED (bounded, not completeness): the only integral points with
   |x| <= 5000 are (-1,+-2), (0,+-1), (2,+-5).
7. VERIFIED: (1/4, +-1/32) are rational points on C (exact arithmetic:
   (1/4)^5 - 4(1/4) + 1 = 1/1024 = (1/32)^2).

NOT claimed: rank = 1 equality, any Coleman disk bound, any complete
integral-point list. The bounded search in (6) is a search certificate
over the stated box only.

## 2. Proof of (1): discriminant

Over Q, disc(x^5 - 4x + 1) = -259019 (sympy resultant computation; replay
`step1_counts_search.py`). Trial division by every odd d <= 509 finds no
divisor, so |disc| is prime. Nonzero discriminant for an odd-degree
hyperelliptic equation implies a smooth projective model of genus 2
(Riemann-Hurwitz: degree-5 double cover of P^1 branched at 5 affine roots
plus infinity). Since 7 does not divide disc, the model has good reduction
at 7 (disc mod 7 = 2).

## 3. Proof of (2)-(3): counts and Jacobian orders

For each p in {3,5,7,11,13}, the affine count over Fp is direct
enumeration: for each x in Fp, v = f(x), count y with y^2 = v. For Fp^2,
fix an explicitly found irreducible quadratic t^2 + a*t + b over Fp,
represent elements as pairs, precompute the set of squares by squaring all
p^2 pairs, evaluate f at all p^2 values of x, and count 0/1/2 square roots
(1 if f(x)=0, 2 if nonzero square, else 0). Adding the single point at
infinity (valid over every extension since deg f is odd) gives N1, N2.
Since disc is prime to each p listed (disc mod p in {1,2,5,6,9} etc.,
all nonzero), reduction is smooth of genus 2 and the Weil formulas apply:
with alpha_i the four Frobenius eigenvalues, s1 = sum alpha_i = p+1-N1,
S2 = sum alpha_i^2 = p^2+1-N2, e2 = sum_{i<j} alpha_i alpha_j
= (s1^2 - S2)/2 (evenness asserted and machine-checked in every case), and
#J(Fp) = P(1) = 1 - s1 + e2 - p*s1 + p^2. Numerical table:

| p  | aff1 | N1 | aff2 | N2  | s1 | e2 | #J(Fp) |
|----|------|----|------|-----|----|----|--------|
| 3  | 6    | 7  | 14   | 15  | -3 | 7  | 29     |
| 5  | 5    | 6  | 45   | 46  | 0  | 10 | 36     |
| 7  | 10   | 11 | 54   | 55  | -3 | 7  | 81     |
| 11 | 18   | 19 | 134  | 135 | -7 | 31 | 237    |
| 13 | 16   | 17 | 180  | 181 | -3 | 10 | 222    |

Replay: `python3 output/artifacts/step1_counts_search.py` prints STEP1_OK.

## 4. Proof of (4)-(5): Cantor rank-lower bound and torsion lemma

Work over F3, where f = x^5 + 2x + 1. Implement Cantor's algorithm for the
genus-2 Jacobian from scratch: Mumford pairs (u,v), u monic,
deg v < deg u, u | (f - v^2); composition via double xgcd and the
reduction loop `u <- monic((f - v^2)/u), v <- (-v) mod u` while deg u > 2
(unique reduced representatives since deg f = 5 is odd). The script
`cantor_rank_lower.py` checks the representation validity
(u | f - v^2) at every step.

D = [(0,1) - inf] corresponds to (u,v) = (x,1): valid since
f(0) - 1 = 0 mod 3, u monic of degree 1, nonzero (u != 1). Since
#J(F3) = 29 is prime, every nonzero element has order 29; the script
independently verifies 29*D == identity by binary scalar multiplication
through the from-scratch group law, and exhibits 2*D = (x^2, x+1) as a
valid reduced rep as a spot check.

Lift to Q. Reduction mod 3 is injective on prime-to-3 torsion. If D were
torsion of order m in J(Q), its reduction has order 29, so 29 | m, and
(m/29)*D would be a point of order 29 in J(Q). But 29-torsion is prime to
5, hence injects into J(F5) of order 36, and 29 does not divide 36 —
contradiction. So D has infinite order: rank J(Q) >= 1.

Torsion: prime-to-3 torsion injects mod 3 into a group of order 29, so its
order divides 29; the order-29 part is excluded mod 5 as above, so J(Q)_tors
is a 3-group. It injects mod 5 (prime-to-5 part) into a group of order
36 = 2^2*3^2, so |T| divides 9; prime-to-11 injection mod 11 into
237 = 3*79 forces |T| | 3. Hence J(Q)_tors in {1, Z/3}.

Replay: `python3 output/artifacts/cantor_rank_lower.py` prints CANTOR_OK.

## 5. Computed evidence (6)-(7), fallback probe, and limits

Bounded search |x| <= 5000 by exact integer square test finds y-integral
points only at x in {-1, 0, 2} — a box certificate, NOT a completeness
proof. The extra rational point (1/4, 1/32) is exact: with Fraction
arithmetic, (1/32)^2 = 1/1024 = (1/4)^5 - 4(1/4) + 1. Together with the
known integral points and infinity, C(Q) contains at least 9 points.

A bounded preset-fallback probe (`fallback_series_template.py`,
FALLBACK_PROBE_OK) shows the generic tiny-integral series
F_{a,b}(t) = int_0^t (a+b*x)/(2y) dx on the P0 disk (uniformizer t = x,
y-series and 1/(2y)-series over Q, termwise integration) is computable for
generic (a,b), e.g. F_{1,0} = t/2 + t^2/2 + t^3 + ..., F_{0,1} = t^2/4 +
t^3/3 + .... The CERTIFIED annihilating (a,b), the O(7^8) Coleman expansion
of the true F, and the Strassman bound are NOT produced: they require the
blocked 2-descent upper bound and Coleman engine (no Sage/Magma/PARI in
lane, no sudo, pip bootstrap failed). No claim is made about them.

## 6. Separation statement

Proof (machine-checked, replayable): items (1)-(5), exact identity (7).
Computed evidence (box search, generic series template): items (6), probe.
Conjecture / not claimed: rank = 1 equality; P0-disk Strassman-1 bound;
complete integral-point list. Uncertainty: none within the proved items;
the J-order/Cantor scripts are exact finite-field arithmetic.
