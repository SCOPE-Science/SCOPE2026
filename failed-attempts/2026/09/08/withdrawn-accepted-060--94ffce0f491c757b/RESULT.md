# Replayable Vieta-orbit census for Markoff–Hurwitz surfaces x^2+y^2+z^2 = 3xyz + k (k = 0, 1, 2) to height 10^4

## Context

The surfaces S_k: x^2 + y^2 + z^2 = 3xyz + k over Z are the Hurwitz normalization
of the Markoff-type equation (k = 0 is the classical Markoff surface up to scaling).
Recognized frontiers motivating exact low-height data are the Markoff unicity
conjecture, Cohn-tree growth, and Hurwitz component/orbit counts. Asymptotic,
Hasse-principle, and Brauer–Manin literature plus sporadic Markoff-number tables
do not publish a uniform bounded-height census with per-point Vieta parent logs,
component decomposition, and trace-identity replay for these S_k.

## Definitions

- S_k: x^2 + y^2 + z^2 = 3xyz + k, k in {0, 1, 2}, over integers.
- Height bound H = 10^4; count ordered triples (x, y, z) with max(|x|, |y|, |z|) <= H.
- Vieta involutions: F_x(x,y,z) = (3yz - x, y, z), F_y(x,y,z) = (x, 3xz - y, z),
  F_z(x,y,z) = (x, y, 3xy - z). Each preserves S_k (quadratic in each variable
  with root-sum 3yz, 3xz, 3xy respectively).
- Components are Vieta-connected components of the box graph: vertices are ordered
  integer points on S_k in the box; edges join pairs differing by one Vieta flip.
  A component root is one ordered triple per component (seed of its flood).

## Result

Exact ordered-triple census at H = 10^4 (machine-verified):

| k | total ordered points | # Vieta (box) components | component sizes | nonneg sorted triples | max coord attained |
|---|---|---|---|---|---|
| 0 | 473 | 5 | [1, 118, 118, 118, 118] | 22 | 9077 at (34, 89, 9077) |
| 1 | 6 | 3 | [2, 2, 2] | 1 | 1 |
| 2 | 360 | 3 | [120, 120, 120] | 16 | 6765 at (1, 2584, 6765) |

Component roots (one ordered triple per box-component; pairwise disjointness verified):
- k = 0: (0,0,0); (1,1,1); (-1,-1,1), (-1,1,-1), (1,-1,-1).
- k = 1: (0,0,1), (0,1,0), (1,0,0); S_1(Z) = {6 axis points}, finite.
- k = 2: (0,1,1); (-1,-1,0), (-1,0,-1). (0,-1,-1) is not a fourth root:
  (0,1,1) -> (0,-1,1) -> (0,-1,-1), so it lies in the main tree.

Nonneg sorted triples (all verified on-surface, max <= H):
- k = 0 (22): (0,0,0), (1,1,1), (1,1,2), (1,2,5), (1,5,13), (1,13,34), (1,34,89),
  (1,89,233), (1,233,610), (1,610,1597), (1,1597,4181), (2,5,29), (2,29,169),
  (2,169,985), (2,985,5741), (5,13,194), (5,29,433), (5,194,2897), (5,433,6466),
  (13,34,1325), (13,194,7561), (34,89,9077).
- k = 1 (1): (0,0,1).
- k = 2 (16): (0,1,1), (1,1,3), (1,3,8), (1,8,21), (1,21,55), (1,55,144),
  (1,144,377), (1,377,987), (1,987,2584), (1,2584,6765), (3,8,71), (3,71,631),
  (3,631,5608), (8,21,503), (8,71,1701), (21,55,3464).

Extremal-growth witnesses (each step one ordered Vieta flip, re-verified):
- k = 0 Fibonacci branch (9 ordered flips):
  (1,1,1) -> (2,1,1) -> (2,5,1) -> (13,5,1) -> (13,34,1) -> (89,34,1) ->
  (89,233,1) -> (610,233,1) -> (610,1597,1) -> (4181,1597,1),
  realizing sorted values (1,1,1), (1,1,2), (1,2,5), ..., (1,1597,4181).
  The box maximum (34,89,9077) is one further flip from (89,34,1)
  (flip z: 3*89*34 - 1 = 9077).
  The artifact's certified longest ordered k = 0 chain in the box is the mirror
  two-negative chain (-4181,-1597,1) -> ... -> (-1,-1,1) (9 flips, depth 9).
- k = 2 longest chain (11 ordered flips, deepest in box):
  (1,2584,6765) -> (1,2584,987) -> (1,377,987) -> (1,377,144) -> (1,55,144) ->
  (1,55,21) -> (1,8,21) -> (1,8,3) -> (1,1,3) -> (1,1,0) -> (1,-1,0) -> (-1,-1,0).
- k = 1 longest chains have depth 1 (axis pairs, e.g. (0,0,-1) -> (0,0,1)).
- Cohn/Fricke trace replay for the k = 0 Fibonacci branch (exact integers):
  P = [[2,1],[1,1]] (tr 3), Q = [[12,5],[7,3]] (tr 15); iterating Q -> P*Q with
  det = 1 and the Fricke identity tr(PQ) + tr(PQ^{-1}) = tr(P)*tr(Q) checked at
  every step reproduces 5, 13, 34, 89, 233, 610, 1597, 4181 as tr/3.

## Proof / evidence

Descent lemma (proof, corrected algebra): let M(t) = max|x|,|y|,|z| and
0 <= x <= y <= z, z >= 2, (x,y,z) in S_k, k in {0,1,2}. Put
z' = 3xy - z (other root of w^2 - 3xy*w + (x^2+y^2-k) = 0, so zz' = x^2+y^2-k).
If xy = 0 then x = 0 and y^2 + z^2 = k <= 2 contradicts z >= 2; hence x, y >= 1.
If z' < 0, write d = z - 3xy >= 1; then k = x^2+y^2+z^2-3xyz = x^2+y^2+z*d.
Since k <= 2 with all terms nonnegative, x = y = 0, contradicting x, y >= 1
(already excluding the impossible (0,0,2)); so z' >= 0.
If z' >= z then x^2+y^2-k = zz' >= z^2, and 3xyz = x^2+y^2+z^2-k <= 3z^2 gives
xy <= z, so x^2+y^2-(xy)^2 >= k >= 0. But (xy)^2-x^2-y^2 = (x^2-1)(y^2-1)-1
is >= 8 > 0 for x, y >= 2, so x = 1 (as x <= y). Then 1+y^2-k >= z^2 with
0 <= y <= z gives z^2-y^2 <= 1-k <= 1, forcing z = y or (k = 0, z^2 = y^2+1,
impossible between consecutive squares); z = y gives 1+2y^2 = 3y^2+k, i.e.
y^2 = 1-k, so only (1,1,1) at k = 0 survives with z = 1, outside the z >= 2
hypothesis. Hence for every nonneg point with z >= 2, 0 <= z' < z: strict
max-decrease. Every nonneg point therefore descends to an irreducible nonneg
point; exhaustive check of {0,1}^3 shows the only ones are k = 0: (0,0,0),
(1,1,1); k = 1: (0,0,1) up to permutation; k = 2: (0,1,1) up to permutation.

Sign bookkeeping (verified by enumerating all 27 triples in {-1,0,1}^3): if
xyz < 0 with an odd number of negatives, 3xyz < 0 gives
x^2+y^2+z^2+3|x||y||z| = k <= 2, so |x|,|y|,|z| <= 1. Counts (one-/two-/
three-negative): k = 0: 0/3/0 (two-neg = permutations of (-1,-1,1)); k = 1:
3/0/0 (one-neg = permutations of (-1,0,0)); k = 2: 6/3/0 (one-neg =
permutations of (-1,0,1) up to order, two-neg = permutations of (-1,-1,0)).
Two-negative points mirror (negate two coordinates) to positive points on the
same S_k, so their descent mirrors the lemma. Finiteness of S_1: nonneg flips
of (0,0,1) give only 0 or -1, so its nonneg tree is itself; it is the only
nonneg point up to permutation, and there are no two-negative points; the full
S_1(Z) is the 6 axis points in 3 flip-pairs.

Completeness (bounded to the box): BFS floods from the listed roots following
all in-box flips are complete because every in-box solution's descent path
stays in-box (max strictly decreases) and ends at a root — computationally
confirmed by greedy descent to a root for every census point (k = 1
one-negative points join roots by an equal-max flip, confirmed by BFS
reachability) — plus an independent exhaustive exact-isqrt pair-solve
cross-check at B = 1000 matching the BFS subsets (14/1/11). Every census point
carries a logged single-flip parent from its root (spanning forest);
single-seed floods were shown pairwise disjoint with union equal to the census.

Trace replay is a certificate for the k = 0 Fibonacci branch only (exact
integer matrix arithmetic, det = 1 and Fricke identity asserted per step).

## Limitations

- Bounded census at H = 10^4 with box-graph Vieta components — not a unicity
  theorem; unicity is untouched.
- k = 0 mirror two-negative trees are counted as distinct box-components (xyz
  >= 0 is flip-invariant so they never meet nonneg trees in the box); whether
  they join outside the box is not addressed.
- Cohn/Fricke replay covers only the k = 0 Fibonacci branch.

## Reproducibility

- artifacts/census.py: generates output/artifacts/census.json by BFS from the
  canonical roots with exact integer arithmetic and on-surface assertions.
- artifacts/verify.py: independently re-floods roots (disjointness,
  union == census), rechecks equation/bound/parent-flip/component/counts,
  validates witness chains as ordered single-flip chains, validates the
  explicit ordered Fibonacci branch and extremal flip, and replays the
  Fricke identity; prints ALL VERIFY_OK.
- artifacts/census.json: all 839 ordered points with component id, parent
  single-flip link, roots, nonneg sorted lists, witness chains, maxima.
- Independent audit recomputed: fresh floods match counts/sizes/depths exactly;
  exact pair-solve at B = 1000 matches (14/1/11); 27-cube sign enumeration and
  greedy descent to root pass; Cohn replay recomputed exactly.

## References

- Ghosh–Sarnak, Integral points on Markoff type cubic surfaces,
  https://arxiv.org/abs/1706.06712 (V_k with coefficient 1; Hasse/class-number
  theory and large-k numerics; different normalization, no bounded
  Vieta-path-plus-trace census).
- Gamburd–Magee–Ronan, An asymptotic formula for integer points on
  Markoff–Hurwitz varieties, https://arxiv.org/abs/1603.06267 (asymptotic
  growth exponents, not an exact bounded census).
- OEIS A002559, Markoff numbers, https://oeis.org/A002559 (sporadic table;
  notes open unicity conjecture; no uniform Vieta-path or trace logs).
- Dao, Rational and integral points on Markoff-type K3 surfaces,
  https://arxiv.org/abs/2504.10992 (Brauer–Manin Hasse failures; no
  Vieta-orbit census for these S_k).
