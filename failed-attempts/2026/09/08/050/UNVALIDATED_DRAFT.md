# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Minimal exponential growth in a 7–9 vertex right-angled Coxeter survey window

## Claim
In the committed 12-graph survey pool of right-angled Coxeter groups on 7–9 vertex
defining graphs, the group defined by **K8 minus two adjacent edges** (missing edges
{0,1},{0,2}; complement = V-graph plus 5 isolates) has the strictly smallest
exponential growth rate. Its growth rate is the golden ratio
**τ = φ = (1+√5)/2 ≈ 1.61803**, exactly, separated from the runner-up rate τ = 2
by the committed gap **2 − φ ≈ 0.38197**. Equivalently its growth-series radius
R = 1/φ ≈ 0.61803 exceeds every other pool member's radius by ≥ 0.11803.

## Objects and formulas
For a RACG W(Γ) with clique counts c_k (c_0 = 1), the (spherical) growth series is
the rational function **W(t) = 1/Q(t)** with **Q(t) = F(t/(1+t))**, where
**F(u) = Σ_k (−1)^k c_k u^k** is the clique polynomial (Steinberg formula for
right-angled groups: 1/W(t) = Σ_{cliques T} (−1)^{|T|}(t/(1+t))^{|T|}).
The exponential growth rate is τ = 1/R with R the smallest-modulus pole of W.

## Winner (W8star)
- Clique counts: [1, 8, 26, 45, 45, 26, 8, 1].
- Exact factorization: F(u) = −(u−1)^5 (u² − 3u + 1) (verified by expansion).
- Smallest positive root u* = (3−√5)/2 ∈ (0.381965, 0.38197) [rational sandwich with
  2.23606² < 5 < 2.23607²; uniqueness: quadratic strictly decreasing on [0, 2/5]
  with q(1/3) = 1/9 > 0 > −1/25 = q(2/5), and no other positive root below u = 1].
- Radius R = u*/(1−u*) ∈ (0.6180313, 0.6180445); τ = 1/R ∈ (1.6180066, 1.6180410).
- Closed form: W(t) = (1+t)^7/(1−t−t²); coefficients from n = 7 are Fibonacci
  numbers: 1, 8, 30, 73, 138, 232, 377, 610, 987, 1597, 2584, 4181, 6765.
- Interpretation: the missing V-pair forces the u²−3u+1 factor; the five clique
  vertices contribute the (u−1)^5 factor (poles at t = −1 only, no growth effect).

## Runner-up and pool table (all exact/rational-interval certified)
| graph | F(u) | τ |
|---|---|---|
| W8star (K8∖V) | −(u−1)^5(u²−3u+1) | φ ≈ 1.61803 |
| K7∖tri, K8∖tri, K9∖tri | ±(u−1)^k(3u−1) | 2 exact |
| K8∖C4, K9∖C4 | ±(u−1)^m(2u²−4u+1) | 1+√2 ≈ 2.41421 |
| K8∖3-star | −(u−1)^4(u³−3u²+4u−1) | ∈ (2.14465, 2.15458) |
| K9∖4-star | (u−1)^4(u⁴−4u³+6u²−5u+1) | ∈ (2.62319, 2.63637) |
| K(3,5) | (3u−1)(5u−1) | 4 exact |
| P8 | (u−1)(7u−1) | 6 exact |
| C9 | 9u²−9u+1 | ∈ (6.85402, 6.85413) |
| P9 | (u−1)(8u−1) | 7 exact |

Minimality: the winner's radius lower bound 76393/123607 ≈ 0.6180313 strictly
exceeds every other pool radius upper bound (next: 1/2). Machine-checked in
`artifacts/verify_poles.py` using only integer/Fraction arithmetic.

## Verification (replayable)
1. `python3 artifacts/compute_all.py` — recomputes clique data, Steinberg series to
   length 12, and shortlex-automaton counts; asserts 12/12 agreement.
2. `python3 artifacts/verify_poles.py` — checks every Z-factorization by expansion,
   re-isolates each smallest positive root with exact rational evaluations
   (uniqueness via strict monotonicity on the bracketing interval: linear factors,
   quadratics with negative derivative, cubic with derivative 3(u−1)²+1 > 0,
   quartic with derivative 4(u−1)³−1 < 0 on [0,1]), converts to R/τ intervals via
   the increasing map u ↦ u/(1−u), and asserts the radius gap. Exits nonzero on failure.
3. Independent check: series-tail ratios a(n+1)/a(n) converge to each certified τ
   (φ, 2, 1+√2, 4, 6, 7 to the displayed precision); a brute-force Tits-reduction +
   trace-normal-form word enumerator (documented in WORKLOG) confirms initial
   coefficients on small cases (e.g. K(3,5): 1, 8, 41, 182).

## The shortlex automaton (evidence, not axiom)
States are right-descent cliques (≤ 2^9). From state S on generator s (in fixed
order): reject if s ∈ S (Tits: non-geodesic); reject if s < max(S ∩ N(s))
(lexicographic minimality: s could shuffle past a larger commuting descent letter);
else move to (S ∩ N(s)) ∪ {s}. Each group element admits exactly one accepted word;
path counts equal spherical-growth coefficients. Corrected during this work (an
earlier variant under/over-accepted); the stated rule matches the Steinberg series
on all 12 pool graphs to length 12 and on hand-enumerated small cases.

## Scope, originality, and limits
- The census is over the committed 12-graph survey pool (dense near-complete graphs
  where exponential growth is slowest, plus sparse benchmarks); it is **not** an
  enumeration of all 7–9 vertex graphs. "Minimal" and "runner-up" are within-pool
  statements, proved as stated.
- No prior work found (per topic admission scan) records this witness, its
  (1+t)^7/(1−t−t²) series, or the φ-vs-2 gap table; growth-formula literature
  (Chiswell-type, multivariate, Okun–Scott) provides tools, not this extremal.
- Standard rational-growth fact used: for these explicit W(t) with a unique
  smallest-modulus (positive real) pole, τ = 1/R; pole tables are rigorous, and the
  comparison logic needs no floating point.
