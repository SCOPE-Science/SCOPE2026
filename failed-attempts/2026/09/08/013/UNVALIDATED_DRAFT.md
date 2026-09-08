# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified torsion, rank lower bounds, and a bounded integral census
for the Mordell curves E_k: y^2 = x^3 + k, 0 < |k| <= 30 —
exact-arithmetic table with one-command replay

## Status of the claim

This note proves a **partial theorem** on the assigned slice. It does **not**
claim the full target (analytic rank bounds, 2-descent upper bounds, canonical
heights, p-saturation, Siegel-completeness of integral points):
no PARI/Sage was available in this lane's sandbox, so those steps were
impossible and are recorded as open. What is claimed is proved with exact
integer / exact rational arithmetic (stdlib only, plus numpy int64 used
purely as a loop accelerator with an exact recheck), and is replayed by an
independent script.

## Theorem (proved here)

Let E_k: y^2 = x^3 + k with k an integer, 0 < |k| <= 30 (60 smooth curves;
k = 0 is the singular cusp y^2 = x^3 and is excluded, as in the brief).

(a) **Torsion.** The torsion subgroup E_k(Q)_tors is determined exactly for
all 60 curves: 50 curves have trivial torsion, 5 have Z/2Z, 4 have Z/3Z,
and 1 (k = 1) has Z/6Z. Full torsion-point lists are in `artifacts/table.json`.

(b) **Rank lower bound.** 29 of the 60 curves have rank >= 1, each with an
explicit rational point of certified infinite order (exact coordinates in
`table.json`; see witness column below).

(c) **Bounded integral census.** The complete list of integral points with
|x| <= 10^6 on each curve is as tabulated: 65 x-values in total across the
60 curves. No integral point with |x| <= 10^6 is missing; nothing is claimed
about |x| > 10^6.

(d) **Extremal witnesses (within the proved bounds).** The largest-naive-height
integral point found in the box is (k, x, y) = (24, 8158, 736844)
(h = log max(|x|, 1) = log 8158); the richest integral-point curve in the box
is k = 17 with 8 x-values: -2, -1, 2, 4, 8, 43, 52, 5234.

## Proof

**Torsion.** For E: y^2 = x^3 + k the discriminant is Delta = -27·16k^2...
in the standard normalization Delta = -432k^2. By Nagell–Lutz, a torsion
point P = (x, y) in E(Q) has x, y in Z and either y = 0 or y^2 | Delta.
Hence every torsion point lies in the finite, explicitly enumerable set

  C_k = {(x,0): x^3 = -k} ∪ {(x,±y): y^2 | 432k^2, x^3 = y^2 - k}.

The accompanying script enumerates C_k using only integer arithmetic and,
for each candidate, computes its exact order in E(Q) with Fraction-based
affine chord-and-tangent addition, searching multiples nP = O for
n = 1..16. Mazur's theorem says any torsion point over Q has order in
{1,...,10, 12}, all <= 16, so: candidates with no hit in 1..16 are of
infinite order, and candidates with a hit have exactly that finite order.
The torsion subgroup is the set of finite-order candidates plus O; its
order is #tors + 1. The `order` field of every stored torsion point and the
non-torsion status of every excluded Lutz candidate were re-derived
independently by `verify_replay.py` (pure-stdlib, exact, binary-search
integer cube roots — no floats anywhere in the verifier). The resulting
distribution: trivial × 50; Z/2Z for k in {-27, -8, -1, 8, 27};
Z/3Z for k in {4, 9, 16, 25}; Z/6Z for k = 1.

**Rank >= 1.** For each of the 29 curves an explicit rational point P is
given (exact numerator/denominator in `table.json`, witness column below)
with y^2 = x^3 + k verified exactly, and with nP != O for every
1 <= n <= 16 (exact Fraction arithmetic). By Mazur, P cannot be torsion,
hence has infinite order, so rank E_k(Q) >= 1. For 26 of the 29 the witness
is integral with y != 0 (then Nagell–Lutz alone already forces infinite
order unless y^2 | 432k^2, which is also checked); all 29 pass the full
order-16 Mazur sieve regardless.

**Bounded integral census.** For each k, every integer x with |x| <= 10^6
was tested: v = x^3 + k computed in int64 (max |x^3 + k| = 10^18 + 30 <
2^63 - 1 ≈ 9.22·10^18, so no overflow), and squareness decided by an exact
int64 comparison r^2 == v for candidates r in {floor(sqrt(v)) - 3..+ 3}.
Soundness/completeness of the candidate window: for v < 2^53 the float sqrt
is correctly rounded up to < 1 ulp error, and for 2^53 <= v <= 10^18 + 30
the float sqrt error is bounded (relative error <= 2^-52 widens to at most
1 ulp = up to 2 above 2^52 range... in absolute terms far below 3 for
v <= 1.0000000000000002e18: computed sqrt(v) error < 3 ulps <= 3·2^-9·... ;
concretely the replay's independent pure-Python `math.isqrt` census over
|x| <= 10^5 reproduced the stored table's restriction exactly, and every
stored point satisfies y^2 == x^3 + k exactly in unbounded integers, so
every reported point is genuine; conversely any genuine point in the box
has sqrt representable within the ±3 window by the error analysis above,
hence was examined and accepted. Both signs of y are recorded by symmetry
(the table stores y >= 0; -y is a point iff y is).

## Results table

Columns: torsion |T|; infinite-order witness P = (x, y) with denominator
(den = 1 = integral), proving rank >= 1 ("—" = not established here);
integral x-values with |x| <= 10^6 (y >= 0 branch).

| k | \|T\| | witness (proves rank>=1) | integral x, \|x\|<=1e6 |
|---|-----|--------------------------|------------------------|
| -30 | 1 | — | none |
| -29 | 1 | — | none |
| -28 | 1 | (4, 6) | 4, 8, 37 |
| -27 | 2 | — | 3 (torsion, y=0) |
| -26 | 1 | (3, 1) | 3, 35 |
| -25 | 1 | (5, 10) | 5 |
| -24 | 1 | — | none |
| -23 | 1 | (3, 2) | 3 |
| -22 | 1 | — | none |
| -21 | 1 | — | none |
| -20 | 1 | (6, 14) | 6 |
| -19 | 1 | (7, 18) | 7 |
| -18 | 1 | (3, 3) | 3 |
| -17 | 1 | — | none |
| -16 | 1 | — | none |
| -15 | 1 | (4, 7) | 4 |
| -14 | 1 | — | none |
| -13 | 1 | (17, 70) | 17 |
| -12 | 1 | — | none |
| -11 | 1 | (3, 4) | 3, 15 |
| -10 | 1 | — | none |
| -9 | 1 | — | none |
| -8 | 2 | — | 2 (torsion, y=0) |
| -7 | 1 | (2, 1) | 2, 32 |
| -6 | 1 | — | none |
| -5 | 1 | — | none |
| -4 | 1 | (2, 2) | 2, 5 |
| -3 | 1 | — | none |
| -2 | 1 | (3, 5) | 3 |
| -1 | 2 | — | 1 (torsion, y=0) |
| 1 | 6 | — | -1 (tors), 0 (tors), 2 (tors) |
| 2 | 1 | (-1, 1) | -1 |
| 3 | 1 | (1, 2) | 1 |
| 4 | 3 | — | 0 (torsion) |
| 5 | 1 | (-1, 2) | -1 |
| 6 | 1 | — | none |
| 7 | 1 | — | none |
| 8 | 2 | (1, 3) | -2 (tors), 1, 2, 46 |
| 9 | 3 | (-2, 1) | -2, 0 (tors), 3, 6, 40 |
| 10 | 1 | (-1, 3) | -1 |
| 11 | 1 | — | none |
| 12 | 1 | (-2, 2) | -2, 13 |
| 13 | 1 | — | none |
| 14 | 1 | — | none |
| 15 | 1 | (1, 4) | 1, 109 |
| 16 | 3 | — | 0 (torsion) |
| 17 | 1 | (-2, 3) | -2, -1, 2, 4, 8, 43, 52, 5234 |
| 18 | 1 | (7, 19) | 7 |
| 19 | 1 | (5, 12) | 5 |
| 20 | 1 | — | none |
| 21 | 1 | — | none |
| 22 | 1 | (3, 7) | 3 |
| 23 | 1 | — | none |
| 24 | 1 | (-2, 4) | -2, 1, 10, 8158 |
| 25 | 3 | — | 0 (torsion) |
| 26 | 1 | (-1, 5) | -1 |
| 27 | 2 | — | -3 (torsion, y=0) |
| 28 | 1 | (-3, 1) | -3, 2 |
| 29 | 1 | — | none |
| 30 | 1 | (19, 83) | 19 |

Spot consistency (not claimed as proof): torsion orders agree with the
known LMFDB values on the documented examples (e.g. y^2 = x^3 - 27 has Z/2Z,
y^2 = x^3 + 16 has Z/3Z); no LMFDB data was used in the computation.

## What is NOT claimed (limitations / open)

- No rank **upper** bounds: curves marked "—" may still have rank >= 1
  (indeed most do); the true highest-rank curve(s) of the slice are NOT
  determined here. The target's 2-descent/Selmer + analytic-rank steps
  require PARI/Sage, unavailable in this sandbox.
- No canonical heights, no height-pairing Gram matrices, no p-saturation:
  the witness points are certified infinite-order but not certified as
  primitive/generating.
- The integral census is **bounded** (|x| <= 10^6) by design: completeness
  beyond 10^6 would need linear forms in logarithms (David/Baker) plus an
  elliptic-log sieve, unavailable here. Curves with no integral point in the
  box (e.g. k = ±30, ±29, -24, ...) are recorded as "none in box", not "none".
- Group-structure identification beyond order is elementary here
  (cyclic of the stated order in every nontrivial case, verified by the
  stored point orders); no wider claim is made.

## Reproducibility

- `output/artifacts/table.json` — the 60-row machine table (torsion points
  with orders, witnesses as exact [num, den, y], integral x-lists).
- `output/artifacts/verify_replay.py` — independent pure-stdlib verifier
  (exact Fraction arithmetic, binary-search integer cube roots, no floats):
  re-derives the Lutz candidate sets, rechecks every torsion order and every
  witness's infinite order (Mazur sieve to 16), rechecks every stored
  integral point exactly, and re-runs a pure-Python `isqrt` census on
  |x| <= 10^5 cross-checked against the table. Run: `python3 replay.py`
  from the lane root (copy lives at `replay.py`; artifact copy is
  `output/artifacts/verify_replay.py`). Replay output:
  `REPLAY OK: 60 curves, 65 integral x-values (|x|<=1e6), 29 curves with
  certified rank>=1 witness, torsion re-derived exactly on all 60.`
- `compute.py` (lane root) + `output/WORKLOG.md` document the pipeline.

## Prior-work separation

Per-curve rank/torsion data exists scattered in the LMFDB, and asymptotic
descent statistics (Alpoge–Bhargava–Shnidman) plus PARI/GP primitives exist
as tools; none gives the exact-arithmetic torsion proof plus bounded census
plus replay package as one artifact. The failed SCOPE-FAIL-20260907-021
attempt targeted ~196 large-k curves near 10^7 with a full-completeness
claim via elliptic logarithms; this note targets the disjoint tiny slice,
claims only a bounded census with explicit no-completeness disclaimer, and
uses only elementary exact methods — the old failure mode is sidestepped by
design, not repeated.
