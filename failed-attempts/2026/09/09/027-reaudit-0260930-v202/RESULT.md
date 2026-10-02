# Angle-defect census of triangulated 2-spheres with at most nine vertices (73 types, Gauss–Bonnet certified)

## Context

Closed triangulated 2-spheres (maximal planar graphs / simplicial polyhedra) are a
natural object in the Bobenko–Pinkall discrete differential geometry program, where
angle-defect curvature and discrete Willmore energy are pre-motivated invariants,
and in the Lutz small-vertex triangulation-enumeration program. No prior source
combined a complete per-type equilateral defect table with a replay certificate:
Willmore-theory papers give the functional, enumeration programs and OEIS A000109
give types/counts only.

## Definitions

- A triangulated 2-sphere with $n$ vertices satisfies $3F=2E$, $V-E+F=2$, hence
  $E=3n-6$, $F=2n-4$, min-degree $\\ge 3$, every edge in exactly two faces.
- Equilateral realization: every edge has length 1, every face angle is $\\pi/3$.
  Vertex defect $K_v = 2\\pi - \\deg(v)\\pi/3$; in units of $\\pi/3$,
  $d_v = 6 - \\deg(v)$ (exact integer).
- Gauss–Bonnet: $\\sum_v K_v = 4\\pi$, i.e. $\\sum_v d_v = 12$.
- Bobenko discrete Willmore energy $W = \\sum_e \\beta(e) - \\pi n$ with hinge
  angles $\\beta(e)$ from circumcircle data (quaternion cross-ratio formula,
  Bobenko Prop. 2.9), which depends on a geometric realization, not on edge
  lengths alone.

## Result (headline, proved + machine-certified)

Up to isomorphism there are exactly **73** triangulated 2-spheres with
$4 \\le n \\le 9$ vertices, with per-$n$ counts **1, 1, 2, 5, 14, 50**
for $n=4,5,6,7,8,9$.

For each type the exact equilateral defect multiset $\\{6-\\deg(v)\\}$ (units
$\\pi/3$) is stored in `census.json`; every one of the 73 rows sums to 12
($=4\\pi$). Distinct defect multisets number **1, 1, 2, 5, 13, 33** for
$n=4\\ldots9$: defects determine the type for $n\\le 7$ but not for $n\\ge 8$
(e.g. at $n=8$ the row $(0,0,1,1,2,2,3,3)$ occurs twice, types T8_6/T8_7,
certified non-isomorphic; at $n=9$ there are 33 distinct rows among 50 types).

Representative rows: n=4: (3,3,3,3); n=5: (2,2,2,3,3); n=6: (2,2,2,2,2,2),
(1,1,2,2,3,3); n=7: five rows including pentagonal bipyramid (1,1,2,2,2,2,2);
n=8: 13 rows listed in DRAFT (single doubled row above); n=9: full 50-row
table in `census.json`.

Secondary benchmark (protocol-relative, replay-certified, not a
realization-independent extremum): under one fully documented deterministic
spring-embedding protocol P0 (fixed seed, Coulomb + edge-spring + central
gravity, 2500 steps, recentering, mean-radius normalization), Bobenko $W$
ranges n=4:{0}; n=5:{0.717}; n=6: 0–2.103; n=7: 3.696–5.315; n=8: 1.030–8.009;
n=9: 1.771–9.853, with global argmax **T9_0, $W=9.853014361$**, margin 0.659
over runner-up T9_2 (9.193695508). T9_0: degrees [7,7,6,6,4,3,3,3,3], defects
$[-1,-1,0,0,2,3,3,3,3]$, edges/faces/positions in `census.json`.

Delimiting lemmas: (A) equilateral edge data are Willmore-blind — the hinge
satisfies $\\cos\\beta=(3\\cos\\theta-1)/4$ for dihedral angle $\\theta$
(flat $\\beta=\\pi/3$, regular-tet hinge $\\beta=2\\pi/3$, numerically
calibrated to 1e-9), so any Willmore number needs a realization protocol;
(B) every geometric tetrahedron has Bobenko $W=0$ (3-point stars cospherical,
Bobenko Prop. 2.2), so no realization-independent maximum exists at $n=4$.

## Proof / evidence

- Generation: seed K4; for $n\\ge 5$ face-stellation of each $(n-1)$-type, then
  closure under edge flips (Wagner: flip-graph of $n$-vertex triangulated
  spheres is connected). Dedup by exact backtracking isomorphism decision
  procedure (degree/neighbor-signature/triangle-count ordered search).
- In-shipment verifier `output/artifacts/verify.py` certifies: (a) pairwise
  non-isomorphism within each $n$ (1327 pairs, all non-isomorphic);
  (b) flip-closure: all 893 flippable hinges land in the stored set of the
  same $n$ (523 non-flippable correctly skipped); flip-closure + Wagner +
  K4 base is the completeness argument; A000109 agreement is corroboration
  only. Closedness audit ($E$, $F$, min-degree, 2 faces/edge) and defect
  re-derivation included.
- Auditor re-ran verifier: VERIFY_OK, worst $|W_{replay}-W_{stored}|=1.421e-14$,
  pairs=1327, flips=893; independently recomputed sums, counts, argmax/margin;
  iso-tester probes (permuted T9_0 → isomorphic; T8_6/T8_7 → non-isomorphic)
  and $\\beta$ calibrations (flat $\\pi/3$, tet $2\\pi/3$) reproduced.
- Willmore: cyclic-order independence, $W(v)\\ge 0$ throughout, independent
  circumcircle-tangent replay (max edge discrepancy 9.4e-16 reported).

## Limitations

- Willmore extremal is scoped to protocol P0 as a reproducible benchmark; no
  realization-independent Willmore maximum is claimed (would require solving 50
  nonconvex realization optimizations); verifier replays stored positions, not
  embedding dynamics from seed.
- Completeness depends on Wagner flip-connectivity (cited theorem) and the
  shipped backtracking iso implementation (probed, not cross-checked against
  plantri).
- No smooth-limit or inscribability classification is claimed.

## Reproducibility

`python3 output/artifacts/verify.py` (stdlib + numpy) reproduces closedness,
defects, Willmore replay, non-isomorphism, flip-closure, and argmax lines.
`output/artifacts/census.json` holds all 73 types (edges, faces, degrees,
defect rows, protocol positions, $W$ values).

## References

- A. I. Bobenko, Surfaces from Circles, arXiv:0707.1318 (discrete Willmore definition, Props. 2.2/2.9).
- F. Knöppel, U. Pinkall, P. Schröder, Y. Soliman, Rolling spheres and the Willmore energy, arXiv:2311.02241.
- E. Köhler, F. H. Lutz, Triangulated Manifolds with Few Vertices I, arXiv:math/0506520.
- OEIS A000109 (simplicial polyhedra counts 1,1,2,5,14,50 for n=4..9).
- G. Brinkmann, B. McKay, plantri (planar triangulation generation; types only).
