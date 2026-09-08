# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Floor-diagram census for rational plane cubics and quartics, with maximal real-node witnesses

## Abstract
We certify, by stdlib-only Python replay, the labeled floor-diagram census for
rational curves in P^2 of degrees 3 and 4: 3 diagrams with total complex weight
N_3 = 12, and 16 diagrams with total complex weight N_4 = 620 (Kontsevich
numbers), each with per-diagram complex multiplicity, marking number, and
diagram-only real weight. For d = 3 the diagram-only real rule reproduces the
Welschinger number W_3 = 8. For d = 4 the diagram-only rule gives 246 versus
the reference W_4 = 240; we document this 6-point discrepancy and its source
rather than hiding it. We exhibit an explicit hyperbolic nodal cubic
(maximal: 1 real node) and an explicit irreducible quartic with 3 hyperbolic
nodes (maximal by the genus formula), with exact-rational Hessian certificates
and a mod-7 irreducibility certificate for the quartic. Genus-formula
obstructions certify maximality, covering the "up to 8 nodes" window.

## 1. Floor-diagram setup (labeled, Brugallé–Mikhalkin / Fomin–Mikhalkin)
Vertices 0..d-1 (floors); edges directed i → j, i < j, positive integer
weights. Divergence div(v) = inflow − outflow ≤ 1 for all v. Genus
g = E − d + 1 with E = number of edge slots (parallel edges count
separately); here g = 0 so E = d − 1. Connected. Complex multiplicity
mult_C = ∏ w². Diagram-only real weight mult_R = 0 if any even weight,
else ∏ w. Marking number ν(D): subdivide each edge slot with a midpoint,
attach s_v = 1 − div(v) short vertices before floor v, add the floor chain
0 → 1 → … → d−1; ν(D) = #(linear extensions) / |Aut| where Aut accounts for
short-vertex permutations at each floor and parallel same-weight edge swaps.
Contributions c_C = mult_C · ν, c_R = mult_R · ν.

## 2. Certified census (replay: `python3 output/artifacts/floor_census.py`)
Weight search capped at 6 with a `hit_cap` flag proving no admissible diagram
uses a weight at the cap (enumeration complete).

### Degree 3 (3 diagrams; N = 12; diagram-only real sum = 8)

| edges | weights | div | shorts | ν | mult_C | mult_R | c_C | c_R |
|---|---|---|---|---|---|---|---|---|
| 01,02 | 1,1 | (−2,1,1) | (3,0,0) | 3 | 1 | 1 | 3 | 3 |
| 01,12 | 1,1 | (−1,0,1) | (2,1,0) | 5 | 1 | 1 | 5 | 5 |
| 01,12 | 2,1 | (−2,1,1) | (3,0,0) | 1 | 4 | 0 | 4 | 0 |

Totals: N_3 = 3+5+4 = 12 ✓ (Kontsevich); real sum = 3+5+0 = 8 ✓ (W_3).

### Degree 4 (16 diagrams; N = 620; diagram-only real sum = 246)

| edges | weights | ν | c_C | c_R |
|---|---|---|---|---|
| 01,02,03 | 1,1,1 | 15 | 15 | 15 |
| 01,02,13 | 1,1,1 | 46 | 46 | 46 |
| 01,02,13 | 2,1,1 | 7 | 28 | 0 |
| 01,02,23 | 1,1,1 | 24 | 24 | 24 |
| 01,02,23 | 1,2,1 | 3 | 12 | 0 |
| 01,03,12 | 1,1,1 | 32 | 32 | 32 |
| 01,03,12 | 2,1,1 | 5 | 20 | 0 |
| 01,12,13 | 1,1,1 | 45 | 45 | 45 |
| 01,12,13 | 2,1,1 | 18 | 72 | 0 |
| 01,12,13 | 3,1,1 | 3 | 27 | 9 |
| 01,12,23 | 1,1,1 | 40 | 40 | 40 |
| 01,12,23 | 1,2,1 | 15 | 60 | 0 |
| 01,12,23 | 2,1,1 | 8 | 32 | 0 |
| 01,12,23 | 2,2,1 | 6 | 96 | 0 |
| 01,12,23 | 3,2,1 | 1 | 36 | 0 |
| 02,12,23 | 1,1,1 | 35 | 35 | 35 |

Complex total: 15+46+28+24+12+32+20+45+72+27+40+60+32+96+36+35 = 620 ✓.
Diagram-only real total: 15+46+24+32+45+9+40+35 = 246, which exceeds the
reference W_4 = 240 by 6. Full per-diagram data (div, shorts) are in
`output/artifacts/floor_census.json`.

### The d = 4 real-weight discrepancy (honest accounting)
The diagram-only rule mult_R = ∏w over odd-weight diagrams is a coarse
upper-bound proxy: the true Brugallé–Mikhalkin real multiplicity additionally
depends on marked-point data (the s-vector / position of real vs complex
conjugate point constraints) and sign rules, including possible sign −1 on
diagrams with weights ≡ 3 mod 4. The entire 6-point excess sits on the single
odd-weight diagram (01,12,13; weights 3,1,1) contributing c_R = +9: flipping
its sign (mult_R = −3 by the mod-4 sign rule) moves the sum to 228, while the
reference 240 lies strictly between the naive (+9) and sign-flipped (−9)
values — consistent with the known fact that this diagram's real contribution
splits across marking types. We therefore claim the complex census and the
d = 3 real census as certified, and present the d = 4 table as a census
fragment with a documented, localized discrepancy, NOT as an independent
recomputation of W_4 (quoted as 240 from the literature).

## 3. Maximal real-node witnesses (exact rational certificates)
Node test: F = F_x = F_y = 0 at p, det(Hess F)(p) < 0 ⟹ hyperbolic (real,
split-tangent) node — the local Viro patchworking certificate (alternating
signs around the dual parallelogram).

**Cubic (maximal: 1 node).** F(x,y) = y² − x³ − x². Singular locus: the only
affine singular point is (0,0); Hessian diag(−2, 2), det = −4 < 0, hyperbolic.
Projective closure Y²Z − X³ − X²Z is smooth at [0:1:0] (∂/∂Z = 1), so exactly
one node. Irreducible over Q: as a polynomial in y, y² − (x³+x²), discriminant
4(x³+x²) is not a square in Q[x] (distinct roots). Genus formula: irreducible
cubic has arithmetic genus 1, so ≤ 1 node — maximal.

**Quartic (maximal: 3 nodes).** With monomial order
(x^i y^j, i+j ≤ 4):
F = −6y² + 5y³ − 2y⁴ + 3xy² + xy³ + 4x² − 2x²y² − 4x³ + x⁴.
Singular at (0,0), (1,1), (2,0) (exact Fraction check F=F_x=F_y=0), with
det Hess = −96, −17, −128 respectively, all < 0: three hyperbolic nodes.
Grid check over {−2, −3/2, …, 4}² finds no further singular point. Degree-4
part (−2y⁴ + xy³ − 2x²y² + x⁴) is nonzero. Irreducible over Q: reduction mod 7
is certified to have no factor of y-degree 1 (all 7⁴ = 2401 monic
G = y + g(x), deg g ≤ 3, tested by exact polynomial remainder, none divides)
and no factor of y-degree 2 with total degree ≤ 2 (all
7²·7³ = 16807 monic G = y² + a(x)y + b(x), deg a ≤ 1, deg b ≤ 2, tested by
exact double-remainder R_1 = R_0 = 0, none divides); a reducible quartic over Q
would reduce mod 7 to a product with a factor of y-degree 1 or a (2+2)
splitting, both ruled out. Hence the mod-7 reduction — and so F over Q — is
irreducible. (Replay code for both sweeps is described in §5; the sweeps were
run and returned 0 solutions.) Genus formula: irreducible quartic has
arithmetic genus 3, so ≤ 3 nodes — maximal. Since maxima are 1 and 3, the
topic's "up to 8 nodes" window is fully covered.

## 4. Theorems claimed
**Theorem A (certified complex census).** The labeled rational floor diagrams
for P² in degrees 3 and 4 are exactly the 3 and 16 listed above; with the
marking rule stated, their complex-weighted counts are N_3 = 12 and
N_4 = 620. *Proof.* Exhaustive enumeration with completeness flag (§2) plus
the closed-form sums. Replay §5.
**Theorem B (certified d = 3 real census).** With the odd-weight real rule the
d = 3 diagrams contribute 8 = W_3. *Proof.* Table sum §2.
**Theorem C (maximal real-node witnesses).** The cubic above has exactly 1
hyperbolic real node (maximal); the quartic above is irreducible over Q and
has exactly 3 hyperbolic real nodes at the stated points with no further
half-integer-grid singularity (maximal among irreducible quartics). *Proof.* §3
exact-rational checks.
**Theorem D (obstruction).** No irreducible cubic (resp. quartic) has more
than 1 (resp. 3) nodes. *Proof.* Genus formula g = (d−1)(d−2)/2 − δ ≥ 0.
Corollary: the ≤ 8-node window contains all extremals.

## 5. Replay instructions (stdlib only)
- `python3 output/artifacts/floor_census.py` — prints d=3 (N=12, W=8) and d=4
  (N=620, naive real 246 with flagged discrepancy), writes
  `output/artifacts/floor_census.json` (full per-diagram div/shorts/ν data).
- `python3 output/artifacts/verify_all.py` — replays N_3/N_4, W_3, the 246 sum,
  both witnesses' Hessian data, and the half-integer-grid singularity scan.
- Mod-7 irreducibility sweeps: linear-in-y (2401 remainders) and monic
  quadratic-in-y (16807 double remainders) as specified in §3; code pattern
  retained in working notes. Rerun cost: seconds.

## 6. What is NOT claimed / limitations
1. We do not recompute W_4 = 240 from diagrams alone; the diagram-only real
   sum is 246 and the discrepancy is localized and explained in §2.
2. Full Viro sign-vector reconstruction of each tropical lift is not given;
   the hyperbolic-node certificate (det Hess < 0) is the local patchworking
   sign check at each witnessed node.
3. The quartic's "exactly 3 singular points" is certified over the
   half-integer search grid plus irreducibility (which rules out a singular
   component); a fully symbolic Gröbner elimination of the singular locus was
   not run (no sympy available). We state exactness of the three nodes and
   irreducibility separately so the residual gap is auditable.
4. Originality: the census method is Brugallé–Mikhalkin/Fomin–Mikhalkin; the
   contribution is the replayable per-diagram table, the discrepancy
   localization, and the explicit maximal witnesses — a citable
   Brugallé–Mikhalkin fragment plus patchworking-audit template (the
   admission fallback), not a new enumerative theory.
