# Integral homology in two nonadjacent degrees for the four-cube dominance complex

## Finding

Let \(Q_4\) denote the graph of the four-dimensional cube, with the sixteen vertices \(V=\{0,1\}^{4}\), where two vertices are adjacent exactly when their Hamming distance is one. The **dominance complex** \(\operatorname{Dom}(Q_4)\) is the simplicial complex
\[
\operatorname{Dom}(Q_4)=\{\sigma\subseteq V:V\setminus\sigma\text{ is a dominating set of }Q_4\}.
\]
Its complete **reduced integral homology** is
\[
\boxed{\widetilde H_k(\operatorname{Dom}(Q_4);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{10},&k=7,\\
\mathbb Z,&k=9,\\
0,&\text{otherwise.}
\end{cases}}
\]
In particular it is exactly \(6\)-connected, its reduced integral homology is torsion-free, and its nonzero groups occur in two **nonadjacent** degrees. The result does **not** identify the complete homotopy type: the attaching map of the Morse nine-cell may be nontrivial.

## Assumptions and scope

Graphs are finite, simple, unweighted, and loopless. A set \(D\subseteq V\) is dominating if every vertex lies in \(D\) or has a neighbor in \(D\). The definition includes the empty simplex in the abstract simplicial complex. For computation, label the sixteen vertices by the integers \(0,\dots,15\), interpreted as four-bit words, and write \(v\oplus2^j\) for toggling bit \(j\in\{0,1,2,3\}\). Its closed neighborhood is
\[
N[v]=\{v,v\oplus1,v\oplus2,v\oplus4,v\oplus8\}.
\]
A vertex subset \(\sigma\) is a face if and only if **no** \(N[v]\) is contained in \(\sigma\), equivalently the complementary set intersects every \(N[v]\). For an integer mask \(s\in\{0,\dots,2^{16}-1\}\), the corresponding face is its set of selected bit positions. The ordinary face poset used for discrete Morse theory contains the **nonempty** faces only.

## Proof

**Exhaustive face universe.** For each of the \(2^{16}=65{,}536\) subset masks, test the defining forbidden-neighborhood criterion and, separately, the complementary domination criterion. Both exact predicates agree on every subset, giving exactly \(45{,}706\) nonempty faces. The face vector, in dimensions \(0\) through \(11\), is
\[
(f_0,\ldots,f_{11})=(16,120,560,1820,4352,7832,10560,10310,6800,2736,560,40).
\]
These are all possible faces, not a sample. The maximal-face dimensions and multiplicities are respectively \(7:10\), \(10:80\), and \(11:40\).

**Explicit Morse matching.** Let \(F\) be the set of all nonempty face masks. Start with \(U=F\) unmatched. Process pivot vertices \(v=0,1,\ldots,15\) in that order. For every \(s\in U\) not containing bit \(v\), if \(s\cup\{v\}\in U\), match the covering pair \((s,s\cup\{v\})\) and remove both from \(U\), simultaneously within this pivot stage. The pairs are disjoint at a fixed pivot because precisely one member contains that pivot bit. The algorithm is deterministic as a set-valued rule, independent of order within each stage. It produces \(22{,}847\) pairs, leaving exactly twelve critical faces: **one zero-cell, ten seven-cells, and one nine-cell**.

**Complete acyclicity certificate.** For every codimension-one incidence \(a\subset b\) in the nonempty face poset, direct it \(b\to a\), except reverse the matched covers to \(a\to b\). Constructing all such incidences from the face masks gives exactly \(329{,}552\) arrows. The standalone checker builds the **entire** directed graph and performs Kahn topological sorting, removing all \(45{,}706\) vertices. Thus the matching is acyclic, with no untested covering relation. As an additional full computation, the alternative pivot ordering
\[
(2,3,10,4,15,12,9,8,5,11,14,7,1,0,13,6)
\]
produces another acyclic matching with the same critical dimension multiplicities; its entire directed Hasse diagram also topologically sorts.

**Integral conclusion.** By the finite acyclic-matching theorem of discrete Morse theory, the geometric realization of \(\operatorname{Dom}(Q_4)\) is homotopy equivalent to a CW complex having precisely one zero-cell, ten seven-cells, and one nine-cell. There are no cells in dimensions one through six or eight. The seven-skeleton is therefore \(\bigvee^{10}S^7\). Its integral cellular boundary maps are zero, since there is no eight-cell for the nine-cell to map into, and no six-cell for the seven-cells to map into. The cellular chain complex consequently has the displayed integral homology groups, with no possible torsion or hidden extensions. The resulting CW model is six-connected, and its nonzero seventh homology shows it is not seven-connected.

This proves the integral homology statement, but does not assert that the nine-cell attaches trivially: a map \(S^8\to\bigvee^{10}S^7\) can have vanishing homological boundary while remaining non-nullhomotopic. Consequently a sphere-wedge homotopy equivalence is not claimed.

## Verification

Run `python3 CHECK_DOM_Q4.py` with Python 3 standard library only. The embedded `CHECK_OUTPUT.txt` is the expected complete output. The program enumerates every subset of the sixteen vertices; proves by exhaustion the equivalence of two separate face definitions; verifies the dual alternating domination-set count; constructs the staged matching; confirms disjointness and complete partition of the face poset; topologically sorts all \(329{,}552\) oriented incidences for **each of two independent pivot orders**; checks the Euler characteristic \(\widetilde\chi=-11\), minimum dominating-set size \(4\), and all \(130\) maximal faces.

For context, the same verifier analyzes dimensions \(1,2,3\): their respective Morse critical vectors are \((2\text{ zero-cells})\), \((1\text{ zero-cell},3\text{ one-cells})\), and \((1\text{ zero-cell},7\text{ three-cells})\). These yield reduced homology concentrated in one degree in each smaller case; the four-cube is the first dimension in this sequence with multiple nonzero reduced homology degrees. The actual checker output terminates with `FOUR_CUBE_DOMINANCE_EXHAUSTIVE_CHECK_PASS`.

## Relationship to prior work

Marietti and Testa [1], building on earlier graph-complex methods, give a homotopy classification of **dominance complexes of forests**. The four-cube is not a forest, so those results do not give the claim. Taylan [2, Section 5] proves a sphere result for **chordal graphs**, whereas the four-cube contains induced four-cycles and is not chordal. Matsushita and Wakatsuki [3] prove the general combinatorial Alexander-duality identity between a dominance complex of a graph and the Lovász neighborhood complex of its **complement**, and compute selected path, cycle, and ladder families. Their general identity does not supply the relevant complement-neighborhood homology computation for the four-cube.

The closest publicly indexed same-graph classification is the ordinary independence complex \(\operatorname{Ind}(Q_4)\simeq\bigvee^{7}S^3\) [4]. An independent set forbids selected graph edges, while \(\operatorname{Dom}(Q_4)\) forbids selected **five-vertex closed neighborhoods**. The independence result therefore neither equals nor implies the present integral homology. Likewise, the inspected Lovász neighborhood complex of \(Q_4\) [5] is not the needed neighborhood complex of the **complement graph**, and the total three-cut complex [6] has a different face criterion. The similarly named bounded-domination **graph** complex [7] has graph edges, not fixed-graph vertices, as simplicial vertices. These precise object differences rule out direct implication by the inspected results; unindexed equivalences remain possible.

## Limitations

The theorem classifies the complete **integral homology**, not the full homotopy type or an automorphism-group homology module. The attaching homotopy class of the nine-cell is unresolved. There is no claimed general formula for higher hypercubes and no extrapolation from the finite calculations. Bibliographic checks cannot exclude an equivalent unindexed result; the literature comparison is not a proof of global publication priority. No independent human verification is claimed.

## References

[1] M. Marietti and D. Testa, *A simple uniform approach to complexes arising from forests*, arXiv:0705.1461, first publicly posted 2007-05-10. https://arxiv.org/abs/0705.1461

[2] D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754, first publicly posted 2015-01-27. https://arxiv.org/abs/1501.06754

[3] T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, first publicly posted 2023-12-05. https://arxiv.org/abs/2312.02639

[4] *The four-cube independence complex is a wedge of seven three-spheres*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-four-cube-independence-complex-is-a-wedge-of-seven-three-sph--9947aaad144c

[5] *Neighborhood complexes of hypercubes collapse to explicit two-sphere wedges*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-neighborhood-complexes-of-hypercubes-collapse-to-explicit-2-sphe--344271f4218a

[6] *The total three-cut complex of the four-cube: a 129-sphere wedge and its hyperoctahedral character*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-total-3-cut-complex-of-the-4-cube-a-129-sphere-wedge-and-its--ccb644c2e2a2

[7] *The domination complex of graphs on seven vertices with domination number at least four*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-domination-complex-d-7-4-is-bigvee-811-s-4-vee-bigvee-84-s-5--e4e894a65756
