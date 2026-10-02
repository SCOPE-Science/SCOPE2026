# Borel 7-coloring of the Z^2 king-move Schreier graph: collapse of the 8-vs-9 gap via power-graph transfer

## Context

Let Z^2 act on the free part F(2,Z^2) of the Bernoulli shift and let G_king be its
Schreier graph for the eight king moves S = {(+-1,0),(0,+-1),(+-1,+-1)}.
G_king is an 8-regular Borel graph with ordinary chromatic number 4 and no K_9.
The admitted question was whether chi_B(G_king) = 9 (Borel attains the greedy
Delta+1 bound) against measurable/Baire/LOCAL 8-colorability, or whether the gap
collapses via an explicit Borel 8-coloring rule. No verified source decided this
cell: Marks (JAMS 2015) requires free-product-of-involutions structure that abelian
Z^2 violates; Gao-Jackson-Krohne-Seward (arXiv:2401.13866) treats only standard
generators (chi = 2, Borel 3); measurable Brooks certifies only the 8-color upper
bound side.

## Definitions

- X = F(2,Z^2): free part of the Bernoulli shift, standard Polish space.
- G_grid: Schreier graph for {(+-1,0),(0,+-1)} (4-regular, bipartite, chi = 2).
- G_king: Schreier graph for the eight king moves on the same X.
- rho_grid, rho_king: shortest-path metrics on orbits.
- Gamma^{(d)}: d-th power graph (distinct vertices at Gamma-distance <= d).
- chi(G): ordinary chromatic number; chi_B(G): least k admitting a Borel proper
  k-coloring.

## Result

**Theorem.** For G_king, the 8-regular king-move Schreier graph of F(2,Z^2),
chi_B(G_king) <= 7 (hence <= 8). In particular there is no Borel 8-vs-9
separation, indeed no 7-vs-8 separation, for this cell. The admitted 8-vs-9
question decides negatively via the collapse disjunct, strengthened from 8 to 7
colors.

Finite facts: |S| = 8 with pairwise distinct neighbors on the free part
(8-regular); omega(G_king) = 4 (2x2 block is K_4; every clique has Chebyshev
diameter <= 1 so sits in a 2x2 block; no K_5, hence no K_9); chi(G_king) = 4
(K_4 lower bound; (x mod 2, y mod 2) proper upper bound); commuting 4-cycles
present, so the Marks free-product game hypothesis fails.

## Proof / Evidence

Imported theorem (Gao-Jackson-Krohne-Seward, arXiv:2401.13866):
- Corollary 3.2: G_grid admits bounded-geometry weakly orthogonal decompositions
  with polygonal bound P = 3 and orthogonality constant Q = eps*d_1/2, where
  eps = eps(2) > 0 is fixed and d_1 is freely choosable (arbitrarily large).
- Theorem 4.8: if a Borel locally-finite graph admits such a decomposition with
  (2d+1)*P <= Q, there is Borel Y with finite Gamma^{(d)}-components on Y and X\Y.
- Corollary 4.9 proof method (Conley-Miller): from finite-component structure at
  d = 2, color Y with chi(Gamma) colors, delete one color class I, recolor
  (X\Y) union I with chi(Gamma) fresh colors sharing exactly the deleted color,
  total 2*chi(Gamma) - 1.

Transfer lemma (new):
- Metric comparison: every king step has Manhattan length <= 2, so
  rho_king <= rho_grid <= 2*rho_king globally (generator comparison; BFS-illustrated
  on 11x11 patch). Consequences as spanning edge inclusions:
  (E1) every G_king edge is a G_grid^{(2)} edge (king grid-distances 1 x4, 2 x4);
  (E2) every G_king^{(2)} edge is a G_grid^{(4)} edge (two king steps total at most
  4 in Manhattan length; king-ball radius 2 has max Manhattan 4).
- Decomposition at d = 4: apply Theorem 4.8 to G_grid at d = 4, needing
  (2*4+1)*3 = 27 <= Q = eps*d_1/2, i.e. d_1 >= 54/eps, satisfiable since d_1 is
  freely choosable (same freedom Cor 4.10 uses for d = 2). Get Borel Y with
  finite G_grid^{(4)}-components on both sides. By (E2),
  G_king^{(2)}|Y and G_king^{(2)}|(X\Y) have finite components.
- Conley-Miller step for G_king (covering lemma): finite-component G_king^{(2)}
  structure implies finite-component G_king structure. Color each finite
  G_king-component of Y with {1,...,4} by least-index choice (Borel by
  Lusin-Novikov; finite subgraphs 4-colorable by inheritance from mod-2 coloring).
  Let I = c_Y^{-1}(4), an independent set; Y' = Y \ I uses {1,2,3}. Each
  G_king-component of (X\Y) union I is covered by one G_king^{(2)}|(X\Y)-component
  plus its neighbors, hence finite (local finiteness). Color each finite component
  with {4,5,6,7} by least choice. Union is a Borel proper 7-coloring (palettes
  disjoint across the partition).

The decomposition yields a Borel unlayered toast by the paper's Theorem 4.12, so
the coloring is toast-driven, satisfying the collapse disjunct's toast-lemma
expectation.

## Limitations

- Proof, not computation: the Borel construction (orthogonal decomposition,
  Lusin-Novikov selection) is imported from the cited paper; artifacts verify
  only finite/graph-theoretic transfer ingredients.
- Constant eps not made explicit (as in source); satisfiability uses the source's
  own "d_1 arbitrarily large" freedom.
- Exact chi_B(G_king) in 4..7 remains open; only the 8-vs-9 (and 7-vs-8) gap is
  closed. Measurable/Baire/LOCAL 8-colorability side stands as admitted.
- Target chi_B >= 9 is refuted; preset toast-obstruction fallback not pursued and
  now presumably false (a 7-coloring is an 8-coloring).

## Reproducibility

- `output/artifacts/verify.py` -> VERIFY_OK (degree, clique, chi = 4, Marks
  4-cycles, boxes, 5x5 torus chi = 5 wrap artifact).
- `output/artifacts/transfer_demo.py` -> TRANSFER_OK (M1 metric comparison;
  M2/M3 edge inclusions; M4 Conley-Miller covering on 200 random graphs;
  M5 40 random finite king subgraphs 4-colorable; M6 constant arithmetic).
- Stdlib only: `python3 output/artifacts/verify.py`,
  `python3 output/artifacts/transfer_demo.py`.

## References

- S. Gao, S. Jackson, E. Krohne, B. Seward, Borel Combinatorics of Abelian Group
  Actions, arXiv:2401.13866 (Cor 3.2, Thm 4.8, Cor 4.9, Thm 4.12).
- A. Marks, A determinacy approach to Borel combinatorics, JAMS 2015
  (free-product game lower bounds; hypothesis fails for Z^2).
- C. Conley, A. Marks, R. Tucker-Drob, Brooks' theorem for measurable colorings,
  Forum Math. Sigma 2016 (measurable/Baire 8-coloring upper bound only).
