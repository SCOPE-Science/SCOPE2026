# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified honeycomb-neighbourhood skeleton atlas for plane tropical quartics (flip-distance 1)

## Abstract
We certify a concrete base point and its flip neighbourhood for the tropical bitangent
program. Let $4\Delta_2 = \mathrm{conv}\{(0,0),(4,0),(0,4)\}$ with its 15 lattice points.
We exhibit an explicit regular unimodular triangulation $T_0$ of $4\Delta_2$ whose dual
tropical curve has skeleton core the complete graph $K_4$ (hence 3-edge-connected), with
exact rational lifting heights. We enumerate all $12$ geometric flips of $T_0$ (pairwise
$S_3$-inequivalent in this instance) and compute each neighbour's skeleton core and edge
connectivity: $10$ stay $3$-edge-connected; $2$ drop to a $2$-edge-cut (tandem-motion wall).
One $2$-edge-cut neighbour is certified regular by an explicit exact height vector crossing
a single secondary-fan wall. Every computational claim replays exactly in seconds with
Python standard library only (`Fractions`). We claim NO bitangent count, NO 41-type shape
label, and NO real-lift number: those need the polymake/TropicalQuarticCurves pipeline
unavailable here.

## 1. Setup and conventions
- $4\Delta_2$ lattice points in fixed order $P_0,\dots,P_{14}$:
  $(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),
  (3,0),(3,1),(4,0)$.
- A triangulation is recorded as $16$ triples of indices. Unimodular = every triangle has
  normalized area $1$; valid = interior edges shared by exactly $2$ triangles, the $12$
  boundary unit segments by exactly $1$, no proper crossings.
- Regularity = appears as the lower convex hull of some height vector $h \in \mathbb{Q}^{15}$;
  certified by storing $h$ exactly and re-running the lower-hull computation.
- Skeleton core: dual graph of the triangulation restricted to interior edges, then
  iteratively delete leaves and smooth out degree-$2$ vertices. Genus check:
  $|E_{int}| - 16 + 1 = 3$.
- Edge connectivity of the core is computed by brute force over edge-deletion subsets
  (cores have $\le 6$ edges, so this is exact and trivial).

## 2. Certified base triangulation $T_0$
Triangles (index triples):
\[
\begin{aligned}
&[0,1,5],\,[1,2,6],\,[1,5,6],\,[2,3,8],\,[2,6,7],\,[2,7,8],\,[3,4,8],\,[5,6,10],\\
&[5,9,10],\,[6,7,10],\,[7,8,11],\,[7,10,11],\,[9,10,12],\,[10,11,13],\,[10,12,13],\,[12,13,14].
\end{aligned}
\]
Lifting heights (exact, in point order):
\[
\frac{1707}{20},\ \frac{19759}{100},\ \frac{46901}{100},\ \frac{93619}{100},\
\frac{40589}{25},\ \frac{2427}{20},\ \frac{4909}{20},\ \frac{57929}{100},\
\frac{5104}{5},\ \frac{49557}{100},\ \frac{25763}{50},\ \frac{87133}{100},\
\frac{98357}{100},\ \frac{25197}{25},\ \frac{32793}{20}.
\]
Verified by replay: lower hull of these heights is exactly the above $16$ triangles;
all have normalized area $1$; boundary/interior edge incidences are $1$/$2$; genus $3$;
skeleton core is $K_4$ on dual nodes $\{4,7,9,11\}$ with edges
$(4,9),(7,4),(7,9),(7,11),(9,11),(11,4)$ — $3$-edge-connected with zero $2$-edge-cuts.

**Theorem 1 (certified base).** The above $(T_0,h_0)$ is a regular unimodular triangulation
of $4\Delta_2$ of genus $3$ whose skeleton core is $K_4$ (hence 3-edge-connected).

## 3. Flip-distance-1 atlas
$T_0$ has $12$ flippable interior edges, yielding $12$ neighbours, pairwise
$S_3$-inequivalent (distinct canonical forms). The table below is read from
`artifacts/census_d1.json` (REG = regularity certified by stored exact heights):

| row | flipped edge | core $V,E$ | edge-conn | 2-cuts | REG |
|-----|--------------|-----------|-----------|--------|-----|
| 0 | $(0,1)\times(1,0)$ | 4,6 | 3 | 0 | yes |
| 1 | $(0,1)\times(1,1)$ | 4,6 | 3 | 0 | yes |
| 2 | $(0,2)\times(1,1)$ | 4,6 | 3 | 0 | yes |
| 3 | $(0,2)\times(1,3)$ | 4,6 | 3 | 0 | yes |
| 4 | $(1,0)\times(2,1)$ | 4,6 | 3 | 0 | NO |
| 5 | $(1,1)\times(1,2)$ | 4,6 | 2 | 1 | NO |
| 6 | $(1,2)\times(2,1)$ | 4,6 | 2 | 1 | yes |
| 7 | $(1,2)\times(2,2)$ | 4,6 | 3 | 0 | yes |
| 8 | $(2,1)\times(2,2)$ | 4,6 | 3 | 0 | NO |
| 9 | $(2,1)\times(3,0)$ | 4,6 | 3 | 0 | yes |
| 10 | $(2,1)\times(3,1)$ | 4,6 | 3 | 0 | NO |
| 11 | $(3,0)\times(3,1)$ | 4,6 | 3 | 0 | yes |

**Theorem 2 (flip-distance-1 skeleton census around $T_0$).** Of the $12$ flip neighbours
of $T_0$, all have genus-$3$ skeleton cores with $4$ vertices and $6$ edges; $10$ are
$3$-edge-connected and $2$ (rows 5, 6) have edge-connectivity exactly $2$ with one
$2$-edge-cut each. No neighbour has a bridge. Row 6 is certified regular: its stored exact
height vector re-induces its triangulation through the lower-hull computation.

Row-6 detail (regular-certified $2$-edge-cut witness): flip edge $[(1,2),(2,1)]$, quad
vertices $(10,7,6,11)$ i.e. points $(2,1),(1,2),(1,1),(2,2)$; core nodes $[4,7,9,10]$,
core edges $(4,9),(7,4),(7,10)\times 2$ (parallel pair), $(9,4),(9,10)$; single
$2$-edge-cut at core-edge positions $[1,5]$. Stored wall-cross certificate records the
moved vertex, wall value $t^\star$ and offset $\delta$ alongside the full height vector.

## 4. What this means for bitangents (interpretation, not a claimed count)
Baker–Len–Morrison–Pflueger–Ren prove every smooth plane tropical quartic has either $7$
or infinitely many bitangent classes; their Lemma 3.7 identifies $2$-edge-cuts as the
tandem-motion wall where a theta characteristic can move in a positive-dimensional family.
Rows 5–6 sit exactly on that wall: they are the directions from this honeycomb-type base
in which rigidity first breaks. We do NOT convert this into a "7 vs infinite" verdict —
that conversion is a black-box citation we deliberately decline to invoke as a proved claim
here, since no bitangent was enumerated.

## 5. Reproducibility
Files under `output/artifacts/`: `honeycomb_flip.py` (exact geometry core),
`finalize_d1.py` (deterministic atlas builder), `census_d1.json` (the atlas),
`verify_census.py` (independent replay checker). Run:
`python3 output/artifacts/verify_census.py` — expect `0 failures; 8/12 rows
regular-certified`, in seconds, with Python standard library only (exact `Fraction`
arithmetic; no polymake/TOPCOM/network needed).

## 6. Limitations (explicit)
1. Distance-1 only (no distance-2 $W$ census); the original flip-to-infinite lemma,
   Cueto–Markwig 41-type labels, and real-lift counts are NOT delivered.
2. Regularity certified for 8/12 neighbours; rows 4, 5, 8, 10 are recorded with
   heights `null` (their triangulations are verified unimodular/genus-3 with correct cores,
   but no lifting vector is claimed for them).
3. The 12 classes are $T_0$'s geometric flips with distinct $S_3$-canonical forms — not a
   certified quotient of the full secondary fan; $T_0$ is a honeycomb-type (K4-core)
   representative, not a proven unique honeycomb triangulation.
4. No bridge (edge-conn 1) occurs at distance 1 here, so no infinite-bitangent witness exists
   in this atlas; the $2$-edge-cut rows are flexibility witnesses only.

## References
- Baker–Len–Morrison–Pflueger–Ren, Bitangents of tropical plane quartic curves (arXiv:1404.7568).
- Cueto–Markwig, Combinatorics and real lifts of bitangents (arXiv:2004.10891).
- Geiger–Panizzut, A tropical count of real bitangents (arXiv:2112.04433); Computing tropical
  bitangents in polymake (arXiv:2112.04447); Geiger, Real Tropical Quartics (arXiv:2503.22390).
