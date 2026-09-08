# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Distinct-pair-sum split for the spiked 7-point subfamily, with a maximal-volume dps witness

## 1. Setting and definitions
A lattice 3-polytope is **distinct-pair-sum (dps)** if its C(7,2) = 21 unordered
pair sums `p+q` (`p<q` lattice points of `P`) are pairwise distinct.
We use the Blanco–Santos test (Choi–Lam–Reznick Lemma 1): for a finite lattice set,
21-sum distinctness holds iff the set contains no three collinear lattice points
forcing a repeated sum and no parallelogram vertices; the verifier checks the
21 sums directly and logs the structural cross-checks.
**Spiked** is in the Blanco–Santos sense (boxed/spiked/merged census,
arXiv:1601.02577, Thms 3.2/3.3): a quasi-minimal polytope projecting along a lattice
direction with unique vertex fibers. Width is the minimum spread over primitive
integer functionals; normalized volume is `6 ×` Euclidean volume.

## 2. Theorem (spiked 7-point dps split + extremal witness)
**Theorem.** At exactly 7 lattice points, the Blanco–Santos spiked families
contribute exactly **29** unimodular classes, pairwise inequivalent, of which
exactly **15 are dps and 14 are non-dps**. The maximal normalized volume among
the dps ones is **19**, attained uniquely (within this subfamily) by

    P* = conv{(1,0,0), (0,1,0), (-1,-1,-2), (1,1,7)},

a tetrahedron (Blanco–Santos type T3.3(9), `a=-2, b=1, k=2`).

**Certificate for P*.** Lattice points of P* (7):
`(-1,-1,-2), (0,0,0), (0,0,1), (0,0,2), (0,1,0), (1,0,0), (1,1,7)`.
Facets: `(2,2,-3).x<=2`, `(7,7,-1).x<=7`, `(5,-14,2).x<=5`, `(-14,5,2).x<=5`.
Vertices: the four generators; `(0,0,0),(0,0,1),(0,0,2)` are non-vertices
(3 interior points). Normalized volume 19 (fan triangulation from `(0,0,0)`).
Width 2, e.g. along `(-1,0,0)`; exhaustive primitive-function search in the
adjugate-certified box proves no width-1 functional. All 21 pair sums distinct:
sorted, `(-1,-1,-2),(-1,-1,-1),(-1,-1,0),(-1,0,-2),(0,-1,-2),(0,0,1),(0,0,2),
(0,0,3),(0,0,5),(0,1,0),(0,1,1),(0,1,2),(1,0,0),(1,0,1),(1,0,2),(1,1,0),
(1,1,7),(1,1,8),(1,1,9),(1,2,7),(2,1,7)`.

## 3. Census table (representative vertex matrices; `1`=dps, `0`=non-dps)
| # | family | vertices | dps |
|---|--------|----------|-----|
| 1 | T3.2 a=b=0 | (1,0,0),(0,1,0),(-1,0,0),(0,-1,4) | 1 |
| 2 | T3.2 a=0,b=1 | (1,0,0),(0,1,0),(-1,0,0),(0,-1,5) | 1 |
| 3 | T3.2 a=b=1 | (1,0,0),(0,1,0),(-1,0,-1),(0,-1,5) | 1 |
| 4 | T3.3(1) | (1,-1,-1),(-1,1,1),(-1,-1,0),(0,0,3) | 0 |
| 5 | T3.3(2) | (1,-1,0),(-1,1,-1),(-1,-1,0),(0,0,2) | 1 |
| 6 | T3.3(4) | (2,-1,-1),(-1,2,1),(-1,-1,0),(0,0,3) | 0 |
| 7 | T3.3(5) a=-1 | (1,-1,-1),(0,1,-1),(-1,-1,0),(0,0,3) | 0 |
| 8 | T3.3(5) a=0 | (1,-1,-1),(0,1,0),(-1,-1,0),(0,0,3) | 0 |
| 9 | T3.3(7) a=-5 | (2,1,0),(-1,1,-5),(-1,-1,0),(0,0,3) | 0 |
| 10 | T3.3(7) a=-1 | (2,1,0),(-1,1,-1),(-1,-1,0),(0,0,3) | 0 |
| 11–15 | T3.3(8) a=-1,b=-1..3 | (1,0,0),(0,1,0),(-1,0,-1),(0,-1,b),(0,0,2) | 0,1,0,0,0 (dps only b=0) |
| 16–19 | T3.3(8) a=0,b=0..3 | (1,0,0),(0,1,0),(-1,0,0),(0,-1,b),(0,0,2) | 0,0,0,0 |
| 20–25 | T3.3(9) | (1,0,0),(0,1,0),(-1,-1,a),(1,1,4-a+b), a in {-2,-1,0}, b in {0,1} | 1,1,1,1,1,1 |
| 26–27 | T3.3(10a) | (1,0,a),(0,2,-1),(-1,0,0),(0,0,2), a in {-1,0} | 1,1 |
| 28–29 | T3.3(10b) | (1,0,0),(0,2,a),(-1,0,0),(0,1,2), a in {-1,0} | 1,1 |
Totals: 29 classes; 15 dps / 14 non-dps. All 29 verified width 2 except
T3.3(4) (width 3). Pairwise unimodular inequivalence checked over all 406 pairs
by exact affine-matching (adjugate-divisibility + determinant ±1 + set image).

## 4. Method (reproducible)
Facets by oriented-plane vote + maximal-coplanar filter; lattice points by
bounding-box scan against facets; dps by direct 21-sum comparison with
collinear-triple/parallelogram logging; volume by exact facet-fan triangulation;
width by adjugate-row-sum certified finite search; equivalence by solving the
affine map on nonsingular vertex quadruples. Replay:
`python3 output/artifacts/verify_dps_spiked7.py` -> `VERIFY_OK`.

## 5. Scope, originality, limits
This is the **fallback fragment** of the admitted plan: the constructive spiked
7-point subfamily only — not the full 496-class width>1 7-point census (boxed and
merged strata not covered), and width-1 infinite families untouched. The dps split
at 7 points is new (triage: dps counts published only at 6 points, 44+1; no 7-point
dps table; enumeration tables stratify by width/points, never pair sums).
Caveat: at `k=2` Blanco–Santos Remark 5 notes some listed polytopes become minimal
rather than quasi-minimal-not-minimal; we do **not** re-prove their spiked-ness —
we certify the 29 size-7 outputs as computed classes with dps labels regardless of
that terminology subtlety, and separately audited all 29 as quasi-minimal
(T3.2 trio minimal; the rest exactly one non-essential deletion) with no merged
pair. "Maximal volume" is maximal within this spiked subfamily, not global over
all 7-point polytopes.
