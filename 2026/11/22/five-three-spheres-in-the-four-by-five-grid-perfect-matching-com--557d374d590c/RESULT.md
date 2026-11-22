# Five three-spheres in the four-by-five grid perfect-matching complex

## Finding

Let \(G=P_4\square P_5\) be the nonperiodic four-row, five-column Cartesian square grid. Define the *perfect-matching extendibility complex* \(\mathcal P(G)\) to have the graph edges that occur in a perfect matching as vertices, and all edge subsets contained in at least one perfect matching as its faces. Then its **integral homotopy type** is
\[
\boxed{\mathcal P(P_4\square P_5)\simeq\bigvee^5 S^3.}
\]
In particular, \(\widetilde H_3(\mathcal P(G);\mathbb Z)\cong\mathbb Z^5\), all other reduced integral homology groups vanish, and its fundamental group is trivial. The complex is pure of dimension nine yet has homology in dimension three, hence it is not pure shellable. The theorem gives a four-row odd-column case of the rectangular-grid sphere-wedge conjecture, beyond the two-row and three-row families presently treated in the cited primary literature.

## Assumptions and scope

The grid has exactly twenty vertices \((r,c)\) with \(0\le r<4\), \(0\le c<5\), and edges between vertices at Manhattan distance one. There are no wraparound edges. This *perfect-matching complex* is distinct from the ordinary matching complex of \(G\), which also contains matchings that cannot extend to a perfect matching.

For reproducible edge indices, visit vertices \((r,c)\) in row-major order, append the downward edge \((r,c)(r+1,c)\) if it exists, then the rightward edge \((r,c)(r,c+1)\) if it exists. This enumerates the 31 graph edges indexed \(0,\ldots,30\). Encode every nonempty edge subset by the corresponding integer bitmask. A face is present precisely when that subset belongs to one of the recursively enumerated perfect matchings.

## Proof

**1. Finite cell enumeration.** The included Python program `check_4x5_perfect_matching.py` enumerates perfect matchings by selecting the least uncovered graph vertex and trying each uncovered neighbor. It checks that the resulting list consists of exactly 95 ten-edge facets, and generates all 50,462 *nonempty* faces. The face counts for edge-subset sizes one through ten, respectively, are
\[
(31,383,2229,6891,12427,13815,9592,4049,950,95).
\]
The enumeration is exhaustive by induction on the number of uncovered graph vertices: every perfect matching pairs the least uncovered vertex with exactly one eligible neighbor, and each such choice is explored.

**2. Exhaustively checked acyclic face matching.** On the nonempty face poset, maintain every lower face's current set of immediate upper cofaces. Repeatedly match an available free face with its unique upper coface, remove both, and update the sets. When none remains and cells remain, declare one maximal face critical, remove it, and continue. The included implementation chooses maximal faces by the lexicographic score of their size, their number of immediate faces with two current upper cofaces, and a seeded random tie-breaker (seed zero), and computes a complete matching. It verifies 25,227 disjoint pairs and only eight unmatched cells: **one critical zero-cell, one critical two-cell, and six critical three-cells**.

A greedy matching does not automatically imply discrete-Morse acyclicity, so acyclicity is verified *separately*: orient every Hasse incidence downward except the paired incidences, which point upward; construct the complete directed graph and perform topological sorting. The program checks that all 50,462 nodes are sorted, across exactly 289,078 Hasse incidences. Thus the computed pairing is an acyclic discrete-Morse matching, and Forman's theorem gives a CW complex with exactly the stated eight cells, homotopy equivalent to \(\mathcal P(G)\).

**3. Exact integral Morse differential.** Orient each simplex by ascending indexed edges. For the unique critical two-cell \(\tau\), compute its coefficient in the reduced boundary of each critical three-cell by recursively canceling upward matched two-three-dimensional pairs with signed incidence coefficients. At a matched lower face \(\sigma\subset \eta\), replace \(\sigma\) with the negative of the sum of the other codimension-one faces of \(\eta\), divided by the incidence coefficient \(\pm1\). The recursion terminates because the entire reversed Hasse graph is acyclic. Downward matched two-faces contribute zero, while \(\tau\) contributes one. The six resulting integral coefficients, in the deterministic discovery order of critical three-cells, are
\[
\boxed{\partial^{\mathrm{Morse}}_3=(1,0,-1,-1,0,0).}
\]
This computation uses integer arithmetic throughout and is independently forced by signed face boundaries, not by finite-field rank alone.

**4. Homotopy identification.** The resulting CW complex has one zero-cell and no one-cells, so its two-skeleton is \(S^2\). The six three-cells are attached by maps in \(\pi_2(S^2)\cong\mathbb Z\). Their attaching degrees constitute the computed row. Since the first coefficient is a unit, the corresponding three-cell kills the two-sphere by a homotopy equivalence. Equivalently, a unimodular column operation sends the row to \((1,0,0,0,0,0)\); the first attaching pair cancels, and the five remaining three-cells attach trivially to a point. The final CW homotopy type is therefore \(\bigvee^5S^3\).

## Verification

Run `python3 check_4x5_perfect_matching.py` from the directory containing the standalone file. It requires only the Python standard library, and regenerates the 95 facets, 50,462 faces, 25,227 pairing edges, complete oriented Hasse graph, acyclicity check, critical-cell counts, and exact signed Morse differential. The concluding marker is `GRID_4X5_PERFECT_MATCHING_OK`. The calculation is exhaustive for this specified finite grid; it does not infer an infinite-family theorem from samples. The theoretical uses of the acyclic matching, integral attaching map and unit-degree cancellation are stated above.

## Relationship to prior work

Chandrakar, Chau, Goyal, Karki and Subhash, first publicly posted 13 November 2026, determine perfect-matching-complex homotopy types of the \(3\times2n\) grids. Their graph family has three rows, so their theorem does not determine the four-row, five-column case. Chandrakar and Singh's earlier treatment covers \(2\times n\) grids and polygonal-line tilings, and presents the general rectangular-grid sphere-wedge question (Conjecture 6.1); it does not give the claimed four-by-five homotopy type.

A separately published exact calculation for the four-by-four square grid gives \(S^2\vee S^2\vee S^3\), not the four-by-five case. A published result on the *ordinary* matching complex of the four-by-five grid concerns a strictly larger simplicial complex and does not imply this perfect-matching subcomplex's homotopy type. The matching method and discrete-Morse theory are established techniques; the asserted new result is the specific complete integral homotopy classification with an independently checkable exhaustive certificate.

## Limitations

This theorem covers only \(P_4\square P_5\) and its perfect-matching extendibility complex, not arbitrary rectangular grids, periodic grids, or all four-row strip lengths. It does not assert that the displayed finite matching is a uniform recurrence or an equivariant construction. Its correctness rests on a fully reproducible finite certificate together with standard discrete-Morse and CW arguments; no independent mathematical audit has been performed. The priority assessment cannot exclude equivalent results unavailable in indexed published sources.

## References

1. H. Chandrakar, T. Chau, S. Goyal, R. Karki and B. Subhash, *Perfect Matching Complexes of \(3\times2n\) Grid Graph*, arXiv:2611.18058v1, first public 13 November 2026, https://arxiv.org/abs/2611.18058.
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809v2, original version publicly available 8 July 2024; especially Theorem 1.1 and Conjecture 6.1, https://arxiv.org/abs/2407.05809.
3. *The four-by-four grid perfect-matching complex is a mixed-dimensional sphere wedge*, published research record and full result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-the-four-by-four-grid-perfect-matching-complex-is-a-mixed-dimens--d33d17c761d3.
4. *Forty-one six-spheres in the matching complex of the \(4\times5\) Cartesian grid*, published research record on the ordinary matching complex, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-forty-one-six-spheres-in-the-matching-complex-of-the-4-times5-ca--b95382aacf1f.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145; acyclic face matching and CW reduction.
