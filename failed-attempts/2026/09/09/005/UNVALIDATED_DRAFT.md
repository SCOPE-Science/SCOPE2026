# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Uniform lattice width 2 for centrally symmetric reflexive polytopes, with a certified census of the 13 three-dimensional classes

## Result

**Lemma (general, any dimension).** Let $P \subset \mathbb{R}^d$ be a centrally symmetric
reflexive lattice polytope (origin the unique interior lattice point, every facet at
lattice distance 1, $P = -P$). Then the lattice width of $P$ is exactly $2$.

*Proof.* For nonzero $u \in \mathbb{Z}^d$, write
$w_u(P) = \max_{x \in P} \langle u,x\rangle - \min_{x \in P} \langle u,x\rangle$.
Since $0$ is interior and $P = -P$, $\max \geq 1$ and $\min \leq -1$ for every primitive
$u$, so $w_u(P) \geq 2$ and hence $w(P) \geq 2$. Conversely, reflexivity gives a facet
$F$ with primitive outward normal $u_0$ at lattice distance 1, i.e.
$\max_{x \in P}\langle u_0,x\rangle = 1$; central symmetry gives
$\min_{x \in P}\langle u_0,x\rangle = -1$. Hence $w_{u_0}(P) = 2$ and $w(P) = 2$. ∎

**Corollary (sharp family bound).** Over the closed family $F$ of all
$\mathrm{GL}(3,\mathbb{Z})$-classes of centrally symmetric reflexive lattice 3-polytopes,
$$W^* = \max_{P \in F} w(P) = 2,$$
attained at every class; the runner-up gap is $0$ (uniform value).

**Census certificate.** Filtering the fixed 4319-entry Kreuzer–Skarke list (PALP format,
`RefPoly.d3`) by the exact integer test "$V = -V$ as sets" yields exactly **13** entries
(1-based KS# 418, 419, 924, 925, 974, 975, 2310, 2311, 3056, 3998, 3999, 4309, 4310).
This symmetry test is complete: reflexivity forces the unique interior lattice point to
be the origin, so any central symmetry fixes the origin and permutes vertices. Each of
the 13 is certified reflexive (all facet lattice distances equal 1), has unique interior
lattice point $(0,0,0)$, has normalized volume cross-checked by two independent
determinant triangulations, and has an explicit primitive attaining direction with
width exactly 2.

## Certified table

Columns: KS index (1-based in `RefPoly.d3`), #vertices, #facets, normalized volume
($6\cdot\mathrm{vol}$, two agreeing triangulations), $|P\cap\mathbb{Z}^3|$,
explicit attaining direction $u$ with $w_u(P)=2$, #width-2 direction pairs mod sign
(= #primitive boundary lattice points of the dual $P^*$ mod $\pm$, all dual boundary
points verified primitive and each verified to give width 2).

| KS# | nv | nfac | normvol | \|P∩Z³\| | attaining u | w | w2-pairs |
|-----|----|------|---------|----------|-------------|---|----------|
| 418 | 6 | 8 | 8 | 7 | (−1,−1,−1) | 2 | 13 |
| 419 | 8 | 6 | 48 | 27 | (−1,0,0) | 2 | 3 |
| 924 | 6 | 8 | 16 | 11 | (−1,−1,0) | 2 | 7 |
| 925 | 8 | 6 | 24 | 15 | (−1,−1,0) | 2 | 5 |
| 974 | 6 | 8 | 32 | 19 | (−1,0,0) | 2 | 4 |
| 975 | 8 | 6 | 12 | 9 | (−1,−1,−1) | 2 | 9 |
| 2310 | 8 | 12 | 12 | 9 | (−1,−1,−1) | 2 | 10 |
| 2311 | 12 | 8 | 36 | 21 | (−1,−1,−1) | 2 | 4 |
| 3056 | 8 | 8 | 20 | 13 | (−1,−1,−1) | 2 | 6 |
| 3998 | 10 | 12 | 16 | 11 | (−1,−1,−1) | 2 | 8 |
| 3999 | 12 | 10 | 28 | 17 | (−1,−1,−1) | 2 | 5 |
| 4309 | 12 | 14 | 20 | 13 | (−1,−1,−1) | 2 | 7 |
| 4310 | 14 | 12 | 24 | 15 | (−1,−1,−1) | 2 | 6 |

Notes.
- The invariant signatures (nv, nfac, normvol, $|P\cap\mathbb{Z}^3|$, facet-size multiset)
  are pairwise distinct across the 13, and an exhaustive vertex-triple $\mathrm{GL}(3,\mathbb{Z})$
  correspondence search found no equivalences among same-vertex-count pairs, consistent with
  the Kreuzer–Skarke list being one representative per class.
- Width lower bound $w \geq 2$ is general (no search needed); the attaining directions above
  (first facet normals from exact hull computation) certify $w \leq 2$ per class. An exhaustive
  primitive-direction enumeration to bound 6 independently confirms minimum 2.
- Dual check: since $w_u(P) = 2h_P(u)$, width-2 primitive directions are exactly the primitive
  boundary lattice points of the dual polytope $P^*$; all dual boundary points here are
  primitive, giving the w2-pairs column (values 3..13, minimum 3 at KS#419, maximum 13 at
  KS#418, the octahedron/cube-dual pair extremes).

## What is proved vs computed vs conjectured

- **Proved (general):** the Lemma — every centrally symmetric reflexive lattice polytope, in
  any dimension, has lattice width exactly 2. Three-line proof above; needs no computer.
- **Computed evidence (certified):** the 13-class census — completeness of the symmetry filter
  over the fixed 4319 list, per-class reflexivity/unique-interior-point/volume agreement/
  attaining-direction/dual-direction-count certificates, all replayed by `verify.py`
  (stdlib + numpy only) printing `VERIFY_OK`.
- **Conjectured:** nothing. No conjecture is made.
- **Uncertainty / originality limit (stated explicitly):** because the Lemma is elementary and
  dimension-free, the sharp bound $W^* = 2$ itself carries no computational novelty; the
  citable content is the completeness certificate over the closed 3D family, the stratified
  table (volumes, point counts, facet data), and the per-class width-2 direction census.
  The author does not claim the width-2 fact is new mathematics — only the complete certified
  census layer over this closed family with replay artifacts is claimed as new.

## Replay

1. Source list: `artifacts/RefPoly.d3` (Kreuzer–Skarke 4319 reflexive 3-polytopes, PALP format;
   upstream: http://hep.itp.tuwien.ac.at/~kreuzer/pub/K3/RefPoly.d3).
2. Run `python3 artifacts/verify.py` (requires only Python 3 + numpy). It asserts the parse
   yields 4319 entries, the symmetry filter yields exactly the 13 listed classes, all facet
   distances equal 1, the two volume triangulations agree, each attaining direction gives
   width 2, the unique interior point is the origin, and the dual width-2-pair counts match
   the table. Expected output ends with `VERIFY_OK` and the 13-row table.
3. Method notes: facets by triple-enumeration convex hull with primitive outward normals and
   affine-rank-2 check; volumes by centroid-ordered (SVD plane basis) facet-cycle fans from
   the origin and from a vertex; lattice points by bounding-box halfspace enumeration.
   A triangulation-ordering bug (angle sort around a vertex) was caught by the two-method
   volume cross-check on hexagon-facet cases and fixed by sorting around the facet centroid.

## References

- M. Kreuzer, H. Skarke, "Classification of reflexive polyhedra in three dimensions,"
  hep-th/9805190 (the 4319 census; bare volumes/point counts, no width data).
- H. Iriyeh, M. Shibata, symmetric Mahler volume-product bound 32/3 in 3D (orthogonal:
  volume products, not widths).
- M. Blanco, F. Santos, lattice 3-polytopes with six lattice points classified by width
  (different family; precedent that width classification is a recognized result kind).
