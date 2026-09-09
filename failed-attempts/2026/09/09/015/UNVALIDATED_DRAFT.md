# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified facet description of STAB(C5) with maximal-gap witness

## Claim
Let G* = C5 (vertices 0..4, edges 01,12,23,34,40). STAB(G*) = conv of the 11
stable-set incidence vectors has the complete irredundant H-description

- x_i >= 0 (5 nonnegativity facets),
- x_i + x_{i+1} <= 1 for each edge (5 edge/clique facets),
- x_0+x_1+x_2+x_3+x_4 <= 2 (odd-hole facet),

certified by exact-rational replay: validity + 5 affinely independent tight
vertices per constraint + irredundancy witnesses + vertex-completeness.
The fractional-vs-integral gap for c=(1,...,1) over the edge/nonnegativity
relaxation is LP=5/2 at x*=(1/2)^5 vs integer alpha=2 (absolute gap 1/2,
ratio 5/4), separated by the odd-hole cut with violation 1/2.

## Proof (machine-checked, replayable)
Run `python3 verify.py` in `output/artifacts/` (stdlib only, Fractions).
1. Vertex source: brute force over 2^5 subsets gives 11 stable sets
   (empty, 5 singletons, 5 nonadjacent pairs 02,03,13,14,24); alpha=2.
2. Validity: all 11 incidence vectors satisfy all 11 constraints.
3. Facet dimension: tight-vertex counts are 8 (nonnegativity), 6 (edge),
   5 (odd-hole: the 5 size-2 stable sets); each tight set has affine rank 4
   in R^5, so each constraint defines a facet.
4. Completeness: exact basic-point enumeration (C(11,5) systems) shows the
   polytope Q cut out by the 11 constraints has exactly 11 vertices, all 0/1
   stable-set vectors; hence Q = STAB(C5).
5. Irredundancy: 11 witnesses, each satisfying all constraints but one:
   (1/2)^5 violates only odd-hole; (1,1,0,0,0)-type points violate only
   their edge; (-1/2,1,0,0,0)-type points violate only their nonnegativity.
6. Gap: exact enumeration of Q0 = {x>=0, edge<=1} vertices gives 12 vertices
   (11 integral + (1/2)^5); max 1.x = 5/2 vs alpha 2.

## What is proved vs conjectured
Proved: complete irredundant facet list of STAB(C5), gap witness above.
Computed evidence only: Q0/Q vertex tables (Q0verts.json, Qverts.json).
Not claimed: full census over all non-perfect n<=7 graphs (topic target);
C5 is the fallback extremal (maximal-gap witness family representative).
Originality: C5 odd-hole inequality itself is textbook; contribution is the
machine-replayable certificate bundle (tight-vertex logs, irredundancy
witnesses, exact vertex tables) usable as a cutting-plane benchmark instance.

## Reproduction
```
cd output/artifacts
python3 enumerate.py   # 11 stable sets, alpha 2
python3 q0verts.py     # 12 verts of Q0 incl. (1/2)^5
python3 qverts.py      # 11 integral verts of Q
python3 verify.py      # VERIFY_OK
```
