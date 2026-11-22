# Near-square isolated components and the first three-component conjugation-fixed partition complex

## Finding
For the partition-transfer clique complex \(K_n\) equipped with Ferrers conjugation \(\tau\), the geometric fixed-point space \(F_n=|K_n|^\tau\) acquires an isolated point at every near-square size \(n=m^2-1\), \(m\ge3\), namely the self-conjugate partition \(\lambda_m=(m^{m-1},m-1)\). The first positive integer \(n\) for which \(F_n\) has at least three connected components is \(n=24\). Its canonical orbit-clique triangulation has 32 vertices and three connected components with 1, 2 and 29 orbit vertices. For every \(1\le n\le23\), it has at most two connected components.

## Assumptions and scope
A partition is a nonincreasing sequence of positive integers with sum \(n\). Its Ferrers conjugate is \(\lambda^\top\). Two distinct partitions are adjacent in \(G_n\) if one is obtained from the other by reducing one part by one and increasing another (possibly a newly introduced zero part) by one, then deleting zero parts and sorting. Let \(K_n\) be the flag/clique complex of this simple graph. Conjugation is a simplicial involution \(\tau\), and \(F_n\) means fixed points in the geometric realization, **not merely the graph induced by self-conjugate partitions**. The notation \(a^k\) within a partition means \(k\) repetitions of \(a\). All topological statements concern finite CW/simplicial complexes with their usual topology.

## Proof
**Fixed-orbit triangulation.** For any finite simplicial complex \(K\) with a simplicial involution \(\tau\), barycentric coordinates of a fixed point are constant on each vertex orbit. Its support is a \(\tau\)-invariant simplex. Construct a new abstract complex with vertices the \(\tau\)-orbits \(O\) of original vertices such that \(O\) itself is a simplex, and with faces the orbit collections whose unions are simplices. A fixed point corresponds uniquely to the associated orbit barycentric coordinates; the coordinate rescaling by orbit size is affine on each face and gives a PL homeomorphism with \(|K|^\tau\). Because \(K_n\) is flag, this new complex is also flag: a collection of admissible orbits spans a face precisely when every vertex of one orbit is adjacent to every vertex of every other orbit. Thus connected components are exactly those of this finite orbit-compatibility graph.

**Near-square family.** Fix an integer \(m\ge3\) and set \(\lambda=(m^{m-1},m-1)\), which has \(m^2-1\) cells and is self-conjugate (an \(m\times m\) square missing its southeast corner). All distinct neighbors of \(\lambda\) under one-cell transfers are exactly
\[
\begin{aligned}
 A&=(m+1,m^{m-3},(m-1)^2),\\
 B&=(m^{m-2},(m-1)^2,1),\\
 C&=(m+1,m^{m-2},m-2),\\
 D&=(m^{m-1},m-2,1).
\end{aligned}
\]
Indeed, a removable cell comes from a row of length \(m\) or the final row of length \(m-1\). An addable cell may go to a row in either preexisting length class or to a new row; moves among identical rows do not change the partition, and the remaining distinct possibilities are precisely the displayed four. Conjugation swaps \(A\leftrightarrow D\) and \(B\leftrightarrow C\). The sum of absolute row-length differences between each of \(A,D\) and \(B,C\) is 4; a single-cell transfer can change the Ferrers row-length vector by total \(\ell^1\)-distance only 2. Hence neither conjugate pair is adjacent. In particular no \(\tau\)-orbit of size two is an admissible orbit-vertex adjacent to \(\lambda\); no other self-conjugate neighbor exists. In the orbit-compatibility triangulation \(\{\lambda\}\) therefore has no incident edge, and is an isolated component of \(F_{m^2-1}\). This holds for **every** integer \(m\ge3\), not merely the tested orders.

**Sharp first three-component threshold.** The finite range \(1\le n\le24\) is treated exhaustively by `checker.py`. For each \(n\), its recursive integer-partition generator enumerates every partition of \(n\). It constructs two independent edge sets: one by explicit transfers and one by testing Ferrers row-length \(\ell^1\)-distance equal to 2. The edge sets agree for every vertex and every \(n\) in the range; conjugation preserves all edges. It then enumerates every one- or two-element conjugation orbit, keeps exactly those whose union is a clique, and builds every pairwise complete compatibility edge. Breadth-first connected-component enumeration yields the counts, in increasing order for \(n=1,\ldots,24\),
\[
(1,1,1,1,1,1,1,2,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,3).
\]
For \(n=24\) the three component sizes are \(1,2,29\), with 32 total admissible orbits. Thus no smaller positive \(n\) has three components, and \(n=24\) does. As a separate check, \((5,5,5,5,4)\) is the isolated orbit-vertex of the one-vertex component at \(n=24\), as predicted by the infinite-family argument.

## Verification
Run `python3 checker.py` with Python 3.9 or later; the code uses only the standard library. It checks complete partition enumeration, both independent adjacency constructions, conjugation equivariance, the complete orbit-clique one-skeleton, and component counts through \(n=24\). It additionally tests the local four-neighbor formula and conjugate-pair distances for \(3\le m\le30\). The finite census supports exactly the finite threshold statement, while the all-\(m\) assertion is proved combinatorially above. The code is not a proof of any untested asymptotic component-count formula.

## Relationship to prior work
Lyudogovskiy's partition-transfer clique-complex theorem [1] gives the **ambient** nonequivariant homotopy type as a bouquet of two-spheres, not the topology of the geometric conjugation-fixed locus. His local-morphology theorem [2] classifies transfer neighborhoods in a more general setting, while the axial-morphology papers [3,4] study self-conjugate vertices and a graph-theoretic spine. In particular [4] shows distinct self-conjugate vertices are nonadjacent, but that does **not** classify the geometric fixed space, which includes midpoints of swapped graph edges and higher invariant simplices. The synthesis [5] raises conjugation-equivariant topology as a further direction. A related published fixed-locus calculation for this partition complex models compatible conjugation-orbit cliques and establishes earlier sharp homological thresholds through \(n=22\); its general model is acknowledged here, while the precise \(n=24\) three-component threshold and the all-\(m\) isolated-near-square family are separate assertions. Priority relative to any fuller unpublished or unindexed calculations remains uncertain.

## Limitations
The result classifies one infinite family of isolated fixed components and the *first* triple-disconnection threshold; it does **not** give a closed formula for the number of connected components for all \(n\), nor complete homotopy types or higher homology of \(F_n\). The finite component census is exhaustive only for \(n\le24\), and the infinite proof applies specifically to the described near-square family. Independent mathematical audit has not been performed.

## References
1. F. B. Lyudogovskiy, *The homotopy type of the clique complex of the partition graph*, arXiv:2603.14370 (first public March 15, 2026), https://arxiv.org/abs/2603.14370.
2. F. B. Lyudogovskiy, *Local Morphology of the Partition Graph*, arXiv:2603.18696 (March 19, 2026), https://arxiv.org/abs/2603.18696.
3. F. B. Lyudogovskiy, *The Partition Graph as a Growing Discrete Geometric Object*, arXiv:2603.21221 (March 22, 2026), https://arxiv.org/abs/2603.21221.
4. F. B. Lyudogovskiy, *Axial Morphology of the Partition Graph: Self-Conjugate Axis, Spine, and Concentration*, arXiv:2603.22546 (March 23, 2026), https://arxiv.org/abs/2603.22546.
5. F. B. Lyudogovskiy, *Local Complexity, Overlap Control, and Global Simplicity in Partition Graphs*, arXiv:2606.20773 (June 18, 2026), https://arxiv.org/abs/2606.20773.
