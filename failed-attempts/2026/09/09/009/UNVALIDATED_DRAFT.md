# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified Nill-criterion audit on seven reflexive 3-polytopes: sufficient-but-not-necessary witness, extremals, and a non-reductive witness

## 1. Setting (cited theory, no originality claimed here)

We use B. Nill, *Complete toric varieties with reductive automorphism group*,
arXiv:math/0407491 (Math. Z. 252 (2006), 767–786). For a reflexive polytope
$P \subset M_{\mathbb{R}}$, $\dim P = d$:

- (Prop. 2.2) $\mathrm{Aut}(X_P)$ is reductive iff the Demazure-root set
  $\mathcal{R}$ is symmetric ($\mathcal{R} = -\mathcal{R}$, i.e. the
  unipotent part $\mathcal{U} = \varnothing$), and
  $\dim \mathrm{Aut}^\circ(X_P) = |\mathcal{R}| + d$.
- For reflexive $P$, $\mathcal{R}$ is exactly the set of lattice points in
  the relative interiors of facets of $P$ (Section 3).
- (Thm. 4.2(2)(i)) $b_P = 0$ (polytope barycenter) is **sufficient** for
  semisimplicity (reductivity). Nill notes (Remark 4.3) the sufficient
  conditions (i)–(v) are pairwise independent, but gives no per-polytope
  sharpness table for the dimension-3 classification.
- (Thm. 2.21) If reductive, $\dim \mathrm{Aut}^\circ \le d^2+2d$ with equality
  only for projective space; (Cor. 3.3) at most $2d$ facets carry roots.
- (Ex. 2.16) $W = \mathrm{conv}((1,0,0),(1,3,0),(1,0,3),(-5,-6,-3))$ has
  $\dim_{\mathbb{R}}\mathcal{S} = 2$, $|\mathcal{S}| = 4$, and two facets
  each with three unipotent roots (weighted $\mathbb{P}(1,1,2,2)$).

Our contribution is purely computational/certifying: exact facet, root,
barycenter, and verdict data for seven *explicitly committed* reflexive
3-polytopes, including the first explicit certified witness in this lane
that $b_P = 0$ is not necessary, plus reproduced extremals. We make **no**
claim over the full 4319 classification.

## 2. Committed panel

Vertex sets (frozen in `artifacts/verify_panel.py`):

1. `cube`: $[-1,1]^3$ (8 vertices).
2. `octahedron`: $\mathrm{conv}(\pm e_1,\pm e_2,\pm e_3)$.
3. `E3`: $\mathrm{conv}(e_1,e_2,e_3,-e_1-e_2-e_3)$.
4. `E3star`: $\mathrm{conv}((-1,-1,-1),(3,-1,-1),(-1,3,-1),(-1,-1,3))$
   (dual of E3, $\mathbb{P}^3$ type).
5. `W_nill`: Nill Example 2.16 simplex above.
6. `prismQ`: $E_1 \times Q$, $Q = \mathrm{conv}((1,0),(0,1),(-1,-1),(0,-1))$
   (quadrilateral with one interior edge point).
7. `prismH`: $E_1 \times H$,
   $H = \mathrm{conv}((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1))$.

## 3. Method (exact, stdlib only)

For each $P$, the script `artifacts/verify_panel.py` (run:
`python3 artifacts/verify_panel.py`) does the following with
`Fraction` exact arithmetic:

1. Facet enumeration: every supporting triple of vertices, kept iff all
   vertices lie on one side; normals reduced to primitive integer form.
2. Reflexivity certificate: every facet level $=1$ and the lattice-point
   census (bounding-box scan with facet-inequality membership) has unique
   interior point $0$.
3. Roots: boundary lattice points lying on exactly one facet; split into
   semisimple $\mathcal{S} = \mathcal{R}\cap(-\mathcal{R})$ and unipotent
   $\mathcal{U}$; verdict reductive iff $\mathcal{U} = \varnothing$;
   $\dim = |\mathcal{R}|+3$.
4. Barycenter: exact determinant (origin-fan) triangulation of $P$ into
   tetrahedra, centroid = volume-weighted mean; **cross-checked** by an
   independent fan triangulation from the first vertex. Dual-polytope
   barycenter computed identically after exact dual-vertex extraction.
5. Dual audit: dual vertices integral, dual reflexive, dual interior $\{0\}$.

Any failed certificate exits nonzero; the committed run prints
`ALL VERIFY_OK`.

## 4. Certified table

| $P$ | facets | $|P\cap M|$ | vol$_6$ | $b_P$ | $b_{P^*}$ | $|\mathcal{R}|$ | $|\mathcal{S}|$ | $|\mathcal{U}|$ | verdict | $\dim\mathrm{Aut}^\circ$ |
|---|---|---|---|---|---|---|---|---|---|---|
| cube | 6 | 27 | 8 | $0$ | $0$ | 6 | 6 | 0 | reductive | 9 |
| octahedron | 8 | 7 | $4/3$ | $0$ | $0$ | 0 | 0 | 0 | reductive (torus only) | 3 |
| E3 | 4 | 5 | $2/3$ | $0$ | $0$ | 0 | 0 | 0 | reductive | 3 |
| E3* | 4 | 35 | $32/3$ | $0$ | $0$ | 12 | 12 | 0 | reductive | 15 |
| W (Ex 2.16) | 4 | 30 | 9 | $(-1/2,-3/4,0)$ | $(1/4,0,-1/4)$ | 10 | 4 | 6 | **non-reductive** | 13 |
| prismQ | 6 | 15 | 4 | $(0,0,-1/6)$ | $(0,-1/16,1/8)$ | 2 | 2 | 0 | **reductive with $b_P\ne0$** | 5 |
| prismH | 8 | 21 | 6 | $0$ | $0$ | 2 | 2 | 0 | reductive | 5 |

## 5. Theorems (proved by the computation)

**Theorem A (sufficiency confirmed on panel).** Every panel member with
$b_P = 0$ (cube, octahedron, E3, E3*, prismH) has $\mathcal{U} = \varnothing$,
hence reductive $\mathrm{Aut}(X_P)$ by Nill Prop. 2.2. These are five new
machine-checked instances of Thm. 4.2(2)(i).

**Theorem B (barycenter-zero is not necessary — sharpness witness).**
$P = \mathrm{prismQ} = E_1 \times \mathrm{conv}((1,0),(0,1),(-1,-1),(0,-1))$
is reflexive with exact barycenter $b_P = (0,0,-1/6) \ne 0$, while
$\mathcal{R} = \{r, -r\}$ (two antipodal facet-interior points), so
$\mathcal{U} = \varnothing$ and $X_P$ has reductive automorphism group of
dimension $5$. Hence Nill's sufficient condition is not necessary (cf. Nill
Remark 4.3 on pairwise independence of (i)–(v); this is a new explicitly
certified instance, not the first theoretical observation).

**Theorem C (non-reductive witness, Nill Ex 2.16 reproduced).**
$W = \mathrm{conv}((1,0,0),(1,3,0),(1,0,3),(-5,-6,-3))$ is reflexive with
$b_W = (-1/2,-3/4,0) \ne 0$, $|\mathcal{S}| = 4$, $|\mathcal{U}| = 6$ in two
antipodal triples, so $\mathrm{Aut}(X_W)$ is non-reductive and
$\dim\mathrm{Aut}^\circ = 13$.

**Theorem D (extremals).** E3* attains the Nill bound
$\dim\mathrm{Aut}^\circ = d^2+2d = 15$ (Thm. 2.21, projective-space case);
the cube attains the Cor. 3.3 bound of $2d = 6$ root-carrying facets.
Dual barycenters (e.g. $b_{W^*} = (1/4,0,-1/4)$) are computed exactly.

## 6. Limitations and non-claims

- Panel-only result: no claim over the full 4319 Kreuzer–Skarke
  classification; the admitted full census was not completed.
- Barycenters are Euclidean volume centroids of the polytopes (matching
  Nill's $b_P$), not lattice-point averages; root counts use the
  facet-relative-interior definition, equivalent to Demazure roots for
  reflexive $P$ by Nill Section 3.
- Theory (Prop. 2.2, Thm. 4.2, bounds) is credited to Nill; originality is
  only the exact certified per-polytope data and the two sharpness
  witnesses (Theorems B–D).

## 7. Reproduction

```
python3 artifacts/verify_panel.py   # → ALL VERIFY_OK (stdlib only)
```

All numbers in Section 4 are printed verbatim by that script.
