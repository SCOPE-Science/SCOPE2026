# Two-edge faults eliminate Moore torsion in the dodecahedral perfect-matching complex

## Finding

Let \(D=\operatorname{GP}(10,2)\) be the dodecahedral graph. For a graph \(G\) with perfect matchings, define its *perfect-matching complex* \(\mathcal P(G)\) to be the simplicial complex of edge sets contained in a perfect matching of \(G\). For any **two distinct** graph edges \(e,f\), the integral homotopy type of \(\mathcal P(D-\{e,f\})\) is always a wedge of spheres, or a point. More precisely:

\[
\mathcal P(D-\{e,f\})\simeq
\begin{cases}
\mathrm{pt},&e\cap f\ne\varnothing,\\
S^2\vee\bigvee^{k(e,f)}S^3,&e\cap f=\varnothing,
\end{cases}
\]

where \(k(e,f)\in\{0,1,2\}\). Among the \(435\) unordered edge pairs, exactly \(60\) give contractible complexes, \(120\) give \(S^2\), \(240\) give \(S^2\vee S^3\), and \(15\) give \(S^2\vee S^3\vee S^3\).

In particular, every two-edge deletion destroys all integral homology torsion. This is a sharp two-fault transition relative to the previously established intact and single-edge dodecahedral complexes, whose reduced second integral homology is \(\mathbb Z/2\mathbb Z\). **This is a statement about the groups after deletion, not a claim that the inclusion-induced homomorphism from the new free group to the old torsion group vanishes.**

## Assumptions and scope

Use vertices \(u_i=i\) and \(v_i=10+i\) for \(i\in\mathbb Z/10\mathbb Z\), with graph edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\), subscripts modulo ten. Sort all thirty unordered endpoint pairs lexicographically, beginning with \((0,1)\) at edge index zero. The result concerns the *extension-restricted* perfect-matching complex, not the ordinary matching complex of all partial matchings.

All edge pairs fall into the following eight orbits of the full automorphism group. Each representative is listed by its two zero-based lexicographic edge indices; the next column gives its actual two graph edges. The last column describes the complete homotopy type.

| Indices | Graph edges | Orbit size | Homotopy type |
|:--|:--|--:|:--|
| \((0,1)\) | \((0,1),(0,9)\) | 60 | contractible |
| \((0,5)\) | \((0,1),(2,3)\) | 60 | \(S^2\vee S^3\) |
| \((0,6)\) | \((0,1),(2,12)\) | 60 | \(S^2\vee S^3\) |
| \((0,7)\) | \((0,1),(3,4)\) | 60 | \(S^2\) |
| \((0,8)\) | \((0,1),(3,13)\) | 60 | \(S^2\) |
| \((0,9)\) | \((0,1),(4,5)\) | 60 | \(S^2\vee S^3\) |
| \((0,10)\) | \((0,1),(4,14)\) | 60 | \(S^2\vee S^3\) |
| \((0,11)\) | \((0,1),(5,6)\) | 15 | \(S^2\vee S^3\vee S^3\) |

## Proof

**Finite exhaustion and orbit completeness.** An explicit depth-first recursion always matches the smallest uncovered graph vertex to one of its currently uncovered neighbors. It obtains exactly \(36\) perfect matchings, without duplication, each containing ten graph edges. For a deleted pair, keep only perfect matchings disjoint from it; every simplex of \(\mathcal P(D-\{e,f\})\) is then a subset of one of these surviving ten-edge sets. A second backtracking recursion constructs all adjacency-preserving bijections of the twenty graph vertices, finding exactly \(120\) automorphisms. Their induced action on unordered graph-edge pairs gives eight disjoint orbits of sizes \(60,60,60,60,60,60,60,15\), totaling all \(\binom{30}{2}=435\) pairs. Thus it is enough to verify the eight representatives in the table.

**Acyclic discrete Morse matchings.** For each representative, enumerate every simplex as a bitmask, including the empty face. On the remaining face poset, repeatedly choose the graph-edge index maximizing the number of still-available pairs \((\sigma,\sigma\cup\{v\})\), then remove all such pairs, until none remain. The verifier explicitly builds the entire directed Hasse graph, orienting the paired incidences upward and all other incidences downward. Its topological sort visits every vertex for all eight representatives. Therefore these are genuine acyclic discrete Morse matchings, not just heuristic reductions. Pairing the empty face yields an implicit basepoint in the resulting CW model.

The numbers of critical two- and three-cells for representatives \((0,1),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11)\) are respectively
\[
(0,0),\ (2,2),\ (1,1),\ (1,0),\ (1,0),\ (1,1),\ (1,1),\ (1,2).
\]
No other critical cells remain. In particular the CW models are simply connected.

**Exact signed Morse differentials.** Order each oriented simplex by its graph-edge indices. The differential of a face is the alternating sum obtained by deleting one index. Recursively eliminate each lower member \(\sigma\) of a paired incidence with upper member \(\tau\) using its *unit* boundary coefficient: project \(\sigma\) to the negative signed sum of the other codimension-one faces of \(\tau\). Matched upper cells project to zero and critical cells to themselves. Acyclicity ensures recursion terminates. The resulting integral boundary \(C_3^{\mathrm{Morse}}\to C_2^{\mathrm{Morse}}\) is zero in every orbit except \((0,5)\), where the exact matrix, with the verifier's ordered critical bases, is
\[
\begin{pmatrix}0&1\\0&-1\end{pmatrix}.
\]
Its nonzero column is primitive, hence admits a unit Smith reduction. The other matrices are zero of the indicated sizes. Since the two-skeleton is a wedge of two-spheres and \(\pi_2\) is identified with its free integral second homology by Hurewicz, all three-cell attachments are determined by their degree vectors. Integral elementary changes of the two- and three-cell bases correspond to homotopy equivalences; the one unit incidence cancels a two/three-cell pair. The stated wedges follow, with no hidden torsion or other homology groups.

## Verification

Run `python3 verify_two_fault.py` with Python 3.10 or newer; no third-party modules are needed. The script regenerates the full graph, all matchings, every simplex, all automorphisms, all edge-pair orbits, each acyclic Morse pairing and its complete directed-Hasse acyclicity test, and the exact signed Morse differential. It independently computes the full simplicial second homology ranks over \(\mathbb F_2\) and \(\mathbb F_3\), and verifies agreement with the reduced integral Morse models. `VERIFIER_OUTPUT.txt` records the successful run. The computations are exhaustive for the specified finite graph and all of its unordered two-edge deletion patterns, not a sample extrapolated to arbitrary graphs.

## Relationship to prior work

Bayer, Jelić Milutinović and Vega introduce and systematically study perfect-matching complexes of honeycomb graphs in their 2022 preprint (published 2023); Chandrakar and Singh classify different polygonal line-tiling families in a 2024 preprint. The published intact dodecahedral calculation gives \(\mathcal P(D)\simeq M(\mathbb Z/2\mathbb Z,2)\vee\bigvee^{20}S^3\). A separate one-edge calculation determines \(\mathcal P(D-e)\) for every single edge. Neither statement specifies the homotopy types of the subcomplexes formed after deleting a *pair* of edges; single-edge and intact homotopy types do not imply the pair-deletion orbit census or the loss of torsion. This result makes no claim of rediscovering the original Moore-space calculation.

## Limitations

The theorem is exact for this one canonical twenty-vertex graph; it does not classify larger generalized Petersen graphs, arbitrary fullerene graphs, or deletions of three or more edges. Although the resulting homotopy groups are determined, no assertion is made about the inclusion-induced maps among the intact, one-edge and two-edge complexes. The finite verification is reproducible, but independent external validation and a proof of priority relative to all unindexed literature have not been obtained.

## References

1. Margaret Bayer, Marija Jelić Milutinović, Julianne Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803, first public 2022-09-06, https://arxiv.org/html/2209.02803v1.
2. Himanshu Chandrakar, Anurag Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, first public 2024-07-08, https://arxiv.org/abs/2407.05809.
3. *Order-two torsion and a Moore-space decomposition for the dodecahedral perfect-matching complex*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-order-two-torsion-and-a-moore-space-decomposition-for-the-dodeca--2c09902bba79.
