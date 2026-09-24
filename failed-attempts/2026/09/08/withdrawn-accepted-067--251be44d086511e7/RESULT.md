# Exact polar-dual volumes and Mahler products for five reflexive 3-polytopes spanning normalized volumes {4, 6, 8, 10, 12}

## Context

Polar duality of reflexive lattice polytopes is the Batyrev mirror-symmetry
operation: if `P` is reflexive, its polar `P*` is again a reflexive lattice
polytope. The product `Vol(P) * Vol(P*)` is the Mahler functional. The general
3D Mahler conjecture (lower bound `64/9` in Euclidean volumes, equality for a
simplex with centroid at the Santalo point) was proved by Chen-Li-Xi-Xu
(arXiv:2605.09334, v3 June 2026, combining the general and symmetric papers);
the centrally symmetric 3D bound `32/3` was proved by Iriyeh-Shibata with a new
proof in Chen et al. The Balletti-Kasprzyk-Nill program studies upper bounds on
dual volumes via the Sylvester sequence (arXiv:1611.02455). The admitted target
asked for the complete Vol<=12 reflexive 3D slice census; what is delivered and
audited here is the admitted fallback: a verified exact-values table for five
natural witnesses spanning the slice's attained primal volumes, with two
absolute Mahler minimizers and one-sided bounds on the remainder.

## Definitions

- Normalized volume in dimension 3: `Vol = 6 * Euclidean volume`.
- `P` is reflexive if `0` is its unique interior lattice point and every facet
  has lattice distance 1 from the origin. Then
  `P = {x : <n_F, x> <= 1}` over primitive facet normals `n_F`, and
  `P* = conv{n_F}`.
- Normalized Mahler product: `M(P) = Vol(P) * Vol(P*)`. Euclidean product is
  `M/36` (since each Euclidean volume is `Vol/6`).

## Result (headline claim)

The following five lattice polytopes are reflexive, with exact normalized
volumes, dual volumes, and Mahler products (normalized; Euclidean `= /36`):

| id | P (vertices) | Vol(P) | P* (facet normals) | Vol(P*) | M = Vol*Vol* | M Euclidean |
|----|---|---|---|---|---|---|
| P4 | (1,0,0),(0,1,0),(0,0,1),(-1,-1,-1) | 4 | (1,1,1),(1,1,-3),(1,-3,1),(-3,1,1) | 64 | 256 | 64/9 |
| P6 | (1,0,0),(0,1,0),(-1,-1,0),(0,0,+/-1) | 6 | (1,1,+/-1),(1,-2,+/-1),(-2,1,+/-1) | 54 | 324 | 9 |
| P8 | (+/-1,0,0),(0,+/-1,0),(0,0,+/-1) | 8 | (+/-1,+/-1,+/-1) | 48 | 384 | 32/3 |
| P10 | (1,0,0),(0,1,0),(-1,0,0),(-1,-1,0),(0,-1,0),(0,0,+/-1) | 10 | (1,1,+/-1),(1,-1,+/-1),(-1,1,+/-1),(-1,0,+/-1),(0,-1,+/-1) | 42 | 420 | 35/3 |
| P12 | (1,0,0),(1,1,0),(0,1,0),(-1,0,0),(-1,-1,0),(0,-1,0),(0,0,+/-1) | 12 | hexagon {(1,0),(1,-1),(0,-1),(-1,0),(-1,1),(0,1)} x {+/-1} | 36 | 432 | 12 |

P6-P12 are bipyramids over the reflexive triangle/diamond/pentagon/hexagon in
`z=0` with apices `(0,0,+/-1)`; their duals are triangular prism / cube /
pentagonal prism / hexagonal prism.

Corollary A (general absolute minimizer): P4 attains normalized product 256 =
Euclidean 64/9 = `4^4/(3!)^2`, the universal 3D Mahler lower bound; its vertex
sum is (0,0,0) so the origin is its centroid = Santalo point, an equality case
of Chen-Li-Xi-Xu. Hence no convex body in R^3 has smaller Mahler product; P4 is
the absolute (hence slice-global) minimum-product witness.

Corollary B (symmetric absolute minimizer): P8 (the octahedron, centrally
symmetric, `P = -P`) attains normalized product 384 = Euclidean 32/3, the
symmetric 3D Mahler bound (Iriyeh-Shibata; new proof in Chen et al.), hence is
the absolute minimizer among centrally symmetric bodies.

Corollary C (one-sided bounds on the slice remainder): for any other reflexive
`P` of normalized volume `V`, `Vol(P*) >= 256/V`, and `>= 384/V` if `P` is
centrally symmetric. Within the five-family, P4 uniquely minimizes the product
(256) and maximizes the dual volume (64).

## Proof / evidence

Hand-checkable backbone (all cases also machine-logged in
`artifacts/table.json` with facet normal/distance/vertex sets):

- Reflexivity: every facet plane has lattice distance 1 (all facet distances
  logged as 1) and a bounding-box lattice scan shows the only interior lattice
  point is the origin (point counts 5,6,7,8,9 = origin plus vertices). Duals
  pass the same test.
- Primal volumes: P4 with apex (1,0,0):
  `det = -1(0+1) - 1(1+2) = -4`, so Vol = 4. P6-P12: bipyramid over reflexive
  k-gon base of normalized area A in {3,4,5,6} with heights +/-1:
  `Vol = A + A = 2A` in {6,8,10,12} (auditor recomputed all four base areas
  3,4,5,6 by ordered shoelace).
- Facet normals: e.g. P4 facet through (0,1,0),(0,0,1),(-1,-1,-1) has normal
  (-3,1,1) with pairing 1 on all three; P8 facet through
  (1,0,0),(0,1,0),(0,0,1) has normal (1,1,1); all sign choices give the cube.
- Dual volumes: P4* translated by -(1,1,1) is `conv{0,-4e1,-4e2,-4e3}`,
  Vol = 4^3 = 64. P8* is the cube [-1,1]^3, Euclidean 8, Vol = 48. Prism duals
  with base normalized area A* and height 2: `Vol = 3*A**2/... ` concretely
  `Vol = 6*A*`: triangular base {(1,1),(1,-2),(-2,1)} has A* = 9 -> 54;
  pentagon base has A* = 7 -> 42; hexagon base has A* = 6 -> 36 (auditor
  recomputed all three by ordered shoelace; the prism formula follows from
  normalized-volume scaling: Vol = 6 * (Euclidean base area * height) with
  Euclidean base area = A*/2 and height 2).
- Machine cross-check: `artifacts/verify.py` (stdlib only) enumerates facets
  from triples, orients them outward, runs the reflexivity + interior-point
  scan, and computes every volume by two independent exact triangulations
  (origin-fan over cyclically ordered facets; vertex-fan over opposite
  facets). Auditor re-ran the script: all ten volumes agree across both
  methods (see `artifacts/verify.log` per-case lines
  `vol(origin-fan) = vol(vertex-fan)` and likewise for duals), reproducing
  (4,64),(6,54),(8,48),(10,42),(12,36).
- Absolute minimality invokes the cited Mahler theorems (not reproved); the
  contribution here is the exact reflexive witness table plus the
  Santalo-point (vertex-sum-zero) check for P4 and the central symmetry check
  for P8 (both auditor-recomputed).

## Limitations

- Completeness over the Vol<=12 reflexive slice is NOT established (that would
  require the KS-4319 census); only the five spanning witnesses are certified.
- Slice-global maximum-dual-volume is NOT claimed; only the family-internal
  maximum (64 at P4) plus the Balletti-Kasprzyk-Nill Sylvester upper bound as
  ambient context.
- Equality-case attribution for the Mahler bounds is cited to Chen et al.
  (2605.09334) / Iriyeh-Shibata, not reproved here.

## Reproducibility

```
python3 artifacts/verify.py   # regenerates artifacts/verify.log
```

Seconds-scale, stdlib only, fully deterministic (integer arithmetic throughout;
floats used only for cyclic facet ordering, never for volumes).

## References

- M. Kreuzer, H. Skarke, Classification of Reflexive Polyhedra in Three
  Dimensions, hep-th/9805190 (4319 polytopes; primal classification only).
- G. Balletti, A. Kasprzyk, B. Nill, On the maximum dual volume of a canonical
  Fano polytope, arXiv:1611.02455 (Sylvester-sequence upper bound on dual
  volume, sharp at a simplex dual; no Vol<=12 slice census).
- S. Chen, Y. Li, D. Xi, Z.-F. Xu, The Mahler Conjecture in Three Dimensions,
  arXiv:2605.09334 (general 3D bound 64/9 with equality characterization;
  includes new proof of symmetric 32/3 case).
- S. Chen et al., The Symmetric Mahler Inequality in Dimension Three via
  Admissible Shadow Systems, arXiv:2605.13795 (symmetric bound 32/3).
- J. Bao et al., Polytopes and Machine Learning, arXiv:2109.09602 (ML
  prediction of volume/dual volume/reflexivity; no exact certified table).
- V. Batyrev, Dual Polyhedra and Mirror Symmetry for Calabi-Yau Hypersurfaces
  in Toric Varieties, alg-geom/9310003 (polar duality as mirror operation).
