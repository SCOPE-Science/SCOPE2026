# The first conjugation-fixed circle in partition transfer clique complexes

## Finding

For a positive integer \(n\), let \(G_n\) be the graph on integer partitions of \(n\), in which two distinct partitions are adjacent when one is obtained from the other by transferring one unit from a part to another part (possibly a newly added zero part) and reordering. Let \(K_n=\operatorname{Cl}(G_n)\) be its clique complex. Ferrers transposition \(\iota(\lambda)=\lambda'\) induces an involution on \(K_n\).

**Theorem (sharp first fixed loop).** For every \(1\le n\le17\), every path component of the **geometric** fixed-point space \(|K_n|^{\langle\iota\rangle}\) is contractible. At the next value,
\[
|K_{18}|^{\langle\iota\rangle}\simeq S^1\sqcup\{\ast\}.
\]
Consequently, \(18\) is the smallest positive integer for which a component of the conjugation-fixed space has nontrivial fundamental group. This is a statement about geometric fixed points, not just the subcomplex on self-conjugate partitions.

## Assumptions and scope

Partitions are nonincreasing finite sequences of positive integers whose sum is \(n\). A unit transfer selects a source part, subtracts one, chooses a different destination part or a newly adjoined zero part, adds one there, deletes zero entries, and sorts. Equal resulting partitions and self-loops are excluded. The full flag complex, not its two-skeleton, is used. Fixed points refer to the induced simplicial involution on the geometric realization. The classification and minimality assertion are restricted to the **complete finite range** \(1\le n\le18\); nothing is claimed about all larger \(n\).

## Proof

**1. Exact geometric fixed-point model.** Transposition is an automorphism of the unit-transfer graph: a nontrivial boundary-cell transfer between rows transposes to a boundary-cell transfer between columns; the reverse move is obtained by transposing again. A geometric point fixed by \(\iota\) has a unique minimal supporting simplex invariant under \(\iota\), and its barycentric coefficients are constant on each vertex orbit. Thus a transposition orbit \(O\) supplies one fixed-space vertex precisely when \(O\) is itself a clique of \(G_n\). Two eligible orbits \(O,P\) supply an edge precisely when every member of \(O\) is adjacent to every member of \(P\). Because \(K_n\) is a flag complex, the clique complex \(F_n\) of this orbit-compatibility graph is naturally homeomorphic to \(|K_n|^{\langle\iota\rangle}\). The homeomorphism sends each orbit vertex to the barycenter of its original orbit simplex. This step is valid for fixed orbits of size one and exchanged pairs, including the axial-free case \(n=2\).

**2. Exhaustive and reproducible finite constructions.** All partitions are generated once by the recursion: for a partition of \(n\) with permitted maximum part \(m\), choose every first part \(k\) with \(1\le k\le\min(n,m)\), followed by each partition of \(n-k\) with maximum at most \(k\). This is a disjoint, exhaustive enumeration of nonincreasing partitions. The exhaustive source/destination transfer operation generates every edge by definition. The checker independently enumerates all cliques of \(G_n\), retains exactly the \(\iota\)-invariant cliques, and confirms they correspond to *exactly* all faces of \(F_n\); it does not rely solely on the orbit-graph construction. Each elementary collapse pairs a face with its unique strict coface; that combinatorial uniqueness is checked against the **entire currently remaining complex** before deletion. These pairs give ordinary elementary simplicial collapses and preserve geometric homotopy type.

The following complete face and collapse census is for \(1\le n\le18\). Here \(f_i\) counts \(i\)-faces of \(F_n\), \(c\) is the number of connected components after the collapses, and \(\rho\) is the cycle rank of the final graph.

| \(n\) | \(f_0\) | \(f_1\) | \(f_2\) | higher faces | collapse pairs | \(c\) | \(\rho\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
|1|1|0|0|0|0|1|0|
|2|1|0|0|0|0|1|0|
|3|1|0|0|0|0|1|0|
|4|2|1|0|0|0|1|0|
|5|2|1|0|0|0|1|0|
|6|2|1|0|0|0|1|0|
|7|3|2|0|0|0|1|0|
|8|3|1|0|0|0|2|0|
|9|5|4|0|0|0|1|0|
|10|4|2|0|0|0|2|0|
|11|6|6|1|0|1|1|0|
|12|6|4|0|0|0|2|0|
|13|8|8|1|0|1|1|0|
|14|8|7|1|0|1|2|0|
|15|10|10|2|0|2|2|0|
|16|12|12|2|0|2|2|0|
|17|13|13|2|0|2|2|0|
|18|15|18|4|0|4|2|1|

**3. Explicit terminal case.** For \(n=18\), order the original integer partitions lexicographically in descending order and retain eligible transposition orbits in their first-occurrence order, numbered from zero. The orbit complex has \(15\) vertices, \(18\) edges, and precisely four triangles. The four independently verified elementary-collapse pairs (free edge, containing triangle) are
\[
(5,6)\subset(4,5,6),\quad (8,11)\subset(4,8,11),\quad
(8,9)\subset(7,8,9),\quad (12,14)\subset(10,12,14).
\]
The remaining graph has \(15\) vertices, \(14\) edges, and two components, with vertex sets \(\{0,1\}\) and \(\{2,3,\dots,14\}\). Its unique cycle is represented by
\[
12\to13\to7\to8\to4\to11\to10\to12.
\]
The first component is a single edge. The second is a connected graph with \(13\) vertices and \(13\) edges, so its fundamental group is free of rank one and it deformation retracts onto a circle. Therefore the fixed space has homotopy type \(S^1\sqcup\{\ast\}\).

**4. Sharpness.** In every earlier row, the displayed valid collapses leave a graph with cycle rank zero. Every connected component of a finite graph of cycle rank zero is a tree, hence contractible. Exhaustiveness of the partition enumeration, orbit model, clique enumeration and collapse checks proves the finite universal quantifier over every \(1\le n\le17\), not a sample-based extrapolation. This proves the threshold.

## Verification

Run `python3 verify.py` with Python 3.9 or newer. The standalone program generates all underlying integer partitions, unit-transfer edges, transposition orbits, original invariant cliques, orbit-complex faces, and collapse pairs without external data or nonstandard packages. It asserts the exact match of invariant original cliques with orbit-complex faces, validates every free-face pair, and checks every component and graph cycle rank for the full stated range. The complete execution record is `verification_output.txt`, ending with `PARTITION_CONJUGATION_FIRST_CIRCLE_EXACT_CHECKS_OK`. For \(n=18\), the same computation independently reproduces \(\chi(K_{18})=311\), consistent with the published table. The program is a finite exhaustive proof certificate, not an assertion about larger parameters.

## Relationship to prior work

Lyudogovskiy, *The homotopy type of the clique complex of the partition graph* (arXiv:2603.14370, first submitted 2026-03-15), studies the ordinary nonequivariant wedge of two-spheres and records Euler characteristics through \(n=25\); the geometric transposition-fixed spaces are not classified there. Lyudogovskiy, *Axial Morphology of the Partition Graph* (arXiv:2603.22546, 2026-03-23), proves conjugation is an automorphism, that distinct self-conjugate **graph vertices** are nonadjacent, and studies axial neighborhoods and a thin spine; its vertex-fixed axis is not the geometric fixed-point space of the clique complex. The local-morphology paper arXiv:2603.18696 (2026-03-19) classifies neighborhoods and local cliques, not their conjugation-fixed homotopy. The present threshold distinguishes the topology of geometric fixed points from that of the fixed-vertex subgraph and from the ordinary homotopy type.

## Limitations

This is an exact finite cutoff theorem through \(n=18\). No assertion is made about fixed-space topology for \(n>18\), canonical equivariant splittings, integral equivariant cohomology, or other partition-graph automorphisms. The finding has not received independent mathematical review. Unindexed treatments of the same geometric fixed locus could pose an originality risk; no absolute uniqueness is asserted.

## References

1. F. B. Lyudogovskiy, *The homotopy type of the clique complex of the partition graph*, arXiv:2603.14370 (submitted 2026-03-15). https://arxiv.org/abs/2603.14370
2. F. B. Lyudogovskiy, *Axial Morphology of the Partition Graph: Self-Conjugate Axis, Spine, and Concentration*, arXiv:2603.22546 (submitted 2026-03-23). https://arxiv.org/html/2603.22546v1
3. F. B. Lyudogovskiy, *Local Morphology of the Partition Graph*, arXiv:2603.18696 (submitted 2026-03-19). https://arxiv.org/abs/2603.18696
