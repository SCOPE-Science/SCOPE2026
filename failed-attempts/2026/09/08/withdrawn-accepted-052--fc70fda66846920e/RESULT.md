# Exact stretched Littlewood-Richardson polynomials on an sl(4) ray

## Context
Beyond Knutson-Tao saturation (positivity/nonvanishing), the
King-Tollu-Toumazet (KTT) stretched program studies the one-parameter
families c(t*lambda, t*mu; t*nu) as polynomials in t: their degrees,
leading coefficients, coefficient nonnegativity (conjectured 2004), and
Fulton rigidity thresholds. General theorems (Derksen-Weyman,
Rassart, Thawinrak via Steinberg/Kostant chamber complexes) prove a
polynomial exists but give no explicit coefficients for any concrete
ray. Explicit ray polynomials are the recognized test data for the KTT
nonnegativity conjecture and for hive-Ehrhart counting benchmarks.

## Definitions
Work in GL(4) with partitions with last part 0 (A3 Dynkin labels via
partial differences). Let

- lambda = (4,2,0,0) (Dynkin (2,2,0)), dim V = 126;
- mu = (4,2,1,0) (Dynkin (2,1,1)), dim V = 140;
- c(lambda, mu; nu) the Littlewood-Richardson coefficient.

The product has dim 126 * 140 = 17640 and decomposes into exactly 25
distinct constituents (verified by exhaustive scoring of all 39
partitions of 13 with at most 4 parts; dimension sum check passes).
In sorted order the first four are (4,4,3,2):1, (4,4,4,1):1,
(5,3,3,2):1, (5,4,2,2):2. Hence

- nu* = (5,4,2,2) is the lex-first constituent of multiplicity >= 2,
  with c(lambda, mu; nu*) = 2;
- nu_max = (6,4,2,1) is the unique maximal-multiplicity constituent,
  with c = 4.

Write P(t) = c(t*lambda, t*mu; t*nu*) and
Q(t) = c(t*lambda, t*mu; t*nu_max) for integers t >= 0.
The Fulton threshold is t0 = min{t >= 1 : P(t) > 1}.

## Result
For every integer t >= 0,

- P(t) = t + 1. Hence deg P = 1, leading coefficient 1, all
  coefficients >= 0 (KTT-nonnegative), and Fulton threshold t0 = 1.
- Companion: Q(t) = (t+1)^2 for every integer t >= 0. Hence deg 2,
  leading coefficient 1, nonnegative coefficients.

At t = 1 the two hives on the nu* ray are exactly
(x,y,z) = (8,10,11) and (9,10,11) in interior coordinates
(x = a(1,1), y = a(2,1), z = a(1,2)).

## Proof / evidence
Two independent from-scratch counts agree everywhere checked:

- (A) A3 Kostant partition function + Steinberg formula (24x24 signed
  sum over S4 x S4).
- (B) GL(4) hive integer-point enumeration (3 interior variables, 18
  rhombus inequalities; opposite-sign convention returns 0,
  confirming orientation).

Base: (A) = (B) = table on all 25 constituents. Stretched t = 0..8:
(A) = (B) = t+1 on the nu* ray, = (t+1)^2 on the nu_max ray.

All-t proof by symbolic hive fiber analysis (no interpolation guess).
On the nu* ray the 18 rhombus forms (auditor-reconstructed) include
y - 10t >= 0 with -y + 10t >= 0, forcing y = 10t, and
z - 11t >= 0 with -z + 11t >= 0, forcing z = 11t, for every t >= 0.
Substituting y = 10t, z = 11t, the 14 remaining forms are automatic
(0, t >= 0) or equivalent to x >= 8t or x <= 9t. Hence the integer
hive fiber is exactly {(x, 10t, 11t) : 8t <= x <= 9t}, which has
t + 1 lattice points. By the Knutson-Tao hive theorem (cited),
P(t) = t + 1 for all t >= 0. The fiber keeps one fixed combinatorial
type (same forcing equalities) for all t >= 0 -- the chamber
certificate; the a priori hive-dimension degree bound is 3, sharpened
to actual degree 1.

P(1) = 2 > 1 and P(0) = 1 give t0 = 1.

Companion: same setup with nu = (6,4,2,1) again forces y = 10t. With
u = x - 8t, v = z - 11t the residual system collapses to
0 <= u <= 2t, 0 <= v <= t, u + v >= t, u - v <= t
(the form v - u <= t is automatic on the box). The fiber is the
(2t+1) x (t+1) box minus A = {u+v <= t-1} (t(t+1)/2 points) minus
B = {u-v >= t+1} (t(t+1)/2 points), disjoint since A needs u <= t-1
and B needs u >= t+1. Count = (2t+1)(t+1) - t(t+1) = (t+1)^2.

## Limitations
Cites the Knutson-Tao hive theorem c = #hives as a black box; the
Steinberg/Kostant chamber is a cross-check while the hive fiber
analysis carries the all-t proof. Originality per substantive
prior comparison (general polynomiality/positivity/monotonicity
theorems imply existence, not this ray's coefficients).

## Reproducibility
`python3 output/artifacts/verify_ray.py` (stdlib only, seconds):
base 25-constituent Steinberg==hive==table check, stretched t = 0..8
two-method formula checks on both rays, forcing-equality checks, and
t = 1 witness print. Prints ALL CHECKS PASSED.

## References
- Knutson-Tao, The honeycomb model of GL(n) tensor products I
  (saturation). https://arxiv.org/abs/math/9807160
- Rassart, A polynomiality property for Littlewood-Richardson
  coefficients. https://arxiv.org/abs/math/0308101
- Thawinrak, A Short Proof for the Polynomiality of the Stretched
  Littlewood-Richardson Coefficients. https://arxiv.org/abs/2211.06810
- Gutschwager, Generalised Stretched Littlewood-Richardson
  Coefficients. https://arxiv.org/abs/0904.4778
- McAllister, Degrees of stretched Kostka coefficients.
  https://arxiv.org/abs/math/0603173
- Belkale, Geometric Proof of a Conjecture of Fulton.
  https://arxiv.org/abs/math/0511664
- King, Stretched Newell-Littlewood coefficients.
  https://arxiv.org/abs/2101.00984
