# The truncated-tetrahedral independence complex and its rational tetrahedral symmetry module

## Finding
Let \(T\) be the twelve-vertex edge graph of the ordinary truncated tetrahedron, described precisely below, and let \(K=\operatorname{Ind}(T)\). Then
\[
K\simeq\bigvee^{5}S^2.
\]
For its natural tetrahedral label-permutation action of \(S_4\), let \(V\) denote the three-dimensional augmentation subrepresentation of the permutation representation on four labels, and let \(\mathrm{sgn}\) be the one-dimensional sign representation. Then, as rational \(S_4\)-representations,
\[
\widetilde H_2(K;\mathbb Q)\cong
\mathbf1\oplus\mathrm{sgn}\oplus(\mathrm{sgn}\otimes V).
\]
The character on conjugacy types \((1^4),(2,1,1),(2,2),(3,1),(4)\), respectively, is \((5,-1,1,2,1)\). In particular the full symmetry quotient has
\[
\widetilde H_i(K/S_4;\mathbb Q)\cong
\begin{cases}\mathbb Q,&i=2,\\0,&i\ne2.\end{cases}
\]
These statements concern a genuine integral homotopy equivalence for \(K\), a rational linear representation for its homology, and rational quotient homology; they do not assert an equivariant homotopy decomposition.

## Assumptions and scope
The vertices of \(T\) are the ordered pairs \((a,b)\) of distinct elements of \(\{0,1,2,3\}\). Distinct pairs \((a,b)\), \((c,d)\) are adjacent exactly if \(a=c\), or if \((c,d)=(b,a)\). Thus four three-cliques contribute twelve edges, and the six reversal pairs contribute six more. This is the usual twelve-vertex, eighteen-edge graph of the truncated tetrahedron. It is also the line graph of the subdivision of every edge of \(K_4\) exactly once: \((a,b)\) corresponds to the edge incident to the original vertex \(a\) on the subdivided edge \(\{a,b\}\). Hence \(K\) is canonically the matching complex of that once-subdivided complete graph, a distinct object from the matching complex of \(T\) itself.

A simplex of \(K\) is a nonempty set of pair-vertices containing no adjacent pair; the empty set is included as the formal empty simplex. Equivalently it is a partial function on four labels without fixed points or a directed two-cycle. The group \(S_4\) acts by simultaneous permutation of both entries of each ordered pair. All homology is reduced unless expressly stated otherwise.

## Proof
**Complete face census.** Lexicographically index the twelve ordered pairs. For every nonzero twelve-bit mask, test all its pairwise adjacencies to decide whether it is a face. This inspects exactly \(2^{12}-1\) candidate nonempty subsets. Recursive generation that extends only independent prefixes produces the identical set. The face vector in dimensions zero through three is
\[
(f_0,f_1,f_2,f_3)=(12,48,72,30),
\]
so there are \(162\) nonempty faces. These numbers also give \(\chi(K)=12-48+72-30=6\). A maximal face has four vertices because every independent set contains at most one pair with each first coordinate.

**Acyclic matching and integral homotopy.** Start with the full finite nonempty face poset in lexicographic pair-vertex order. For each vertex \(j\), pair each still-unmatched face \(\sigma\) not containing \(j\) with \(\sigma\cup\{j\}\) whenever both occur among the currently unmatched faces; then remove both. Iterating through the twelve vertices yields exactly \(78\) disjoint pairs. Precisely six faces remain unmatched: one vertex and five triangles. To verify the nonstandard critical acyclicity condition, orient each of the \(432\) cover incidences from its larger face to its smaller face, except reverse the incidence for every matching pair. A full topological sort visits all \(162\) faces, so this directed Hasse diagram contains no cycle. These are exhaustive finite computations from the stated adjacency rule, reproduced in `verify.py`.

The resulting acyclic Forman matching gives a CW complex with one zero-cell, five two-cells, and no other cells. Its one-skeleton is a point, and every attaching map \(S^1\to\{\mathrm{point}\}\) is nullhomotopic. Thus this CW complex is a wedge of exactly five two-spheres, proving the claimed **integral homotopy equivalence**, not merely a Betti-number count. As an independent numerical check, exact binary rank reduction of the original simplicial boundaries gives \(\operatorname{rank}_{\mathbb F_2}(\partial_1)=11\), \(\operatorname{rank}_{\mathbb F_2}(\partial_2)=37\), and \(\operatorname{rank}_{\mathbb F_2}(\partial_3)=30\).

**Complete symmetry character.** For every permutation \(g\in S_4\) and every oriented face \(\sigma\), its contribution to the simplicial chain trace is zero unless \(g\sigma=\sigma\), in which case it is the sign of the induced permutation of its ordered vertices. Therefore the reduced Lefschetz number is
\[
\sum_{\varnothing\ne\sigma=g\sigma}(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma)-1.
\]
Since the only nonzero reduced rational homology is in dimension two, this is exactly the character value on \(\widetilde H_2(K;\mathbb Q)\). Exhaustively applying the formula to all \(24\) label permutations and all \(162\) faces yields values \(5,-1,1,2,1\) on the five cycle types, with type sizes \(1,6,3,8,6\). These are equal, type by type, to \(1+\mathrm{sgn}(g)+\mathrm{sgn}(g)(\#\operatorname{Fix}(g)-1)\), the character of \(\mathbf1\oplus\mathrm{sgn}\oplus(\mathrm{sgn}\otimes V)\). Rational representations of a finite group are semisimple, and these three constituents are absolutely irreducible and pairwise nonisomorphic, so equality of characters gives the asserted rational module decomposition.

Finally, after an equivariant barycentric subdivision the group acts cellularly without inversions. In characteristic zero the rational chain complex of the quotient identifies with the invariant cellular chain complex, and averaging makes taking invariants exact. Thus its reduced rational homology is the invariant part of that of \(K\). Only the trivial summand contributes, in dimension two.

## Verification
Run `python verify.py` in a standard Python 3 interpreter. It independently reconstructs the same graph as the line graph of a once-subdivided \(K_4\), enumerates faces by both all-mask checking and independent-prefix recursion, checks the complete directed face-incidence graph for acyclicity, and computes all \(24\) signed class traces. It also calculates the complete simplicial boundary ranks over \(\mathbb F_2\). The included `verification_output.txt` records the expected outputs, including `ALL_CHECKS_PASS`. These checks are finite exhaustive calculations; the proof of integral homotopy is the acyclic Morse matching, not the field homology ranks.

## Relationship to prior work
Engström (2005) proves general connectivity bounds for independence complexes of claw-free graphs, a family containing \(T\), but no integral homotopy classification or complete \(S_4\)-character for this graph. Barmak (2010) develops star-cluster reductions and discusses matching complexes; its triangle-free suspension theorem does not apply because \(T\) contains four triangles. Its general connectivity arguments do not determine the claimed representation.

The closest explicit same-family result, *The independence complexes of the truncated four- and five-simplices*, classifies the ordered-pair graphs on \(20\) and \(30\) vertices corresponding to five and six underlying labels. Its formula is explicitly restricted to those two input sizes and does not imply the separate twelve-vertex computation, especially its rational tetrahedral symmetry character. *Edge-orbit matching-complex homotopy of the truncated tetrahedron* instead uses pairwise-disjoint **edges of the truncated-tetrahedral graph**, whereas the present vertices are its **twelve graph vertices** (equivalently, edges of a different subdivided graph). *The graph-metric Rips filtration of the truncated tetrahedron* uses cliques at prescribed graph distance rather than independent sets, and provides neither the specified simplicial complex nor its tetrahedral homology module. Coincidental equality of sphere multiplicities for two different constructions is not an implication between their theorems.

## Limitations
This classification is specific to the truncated tetrahedron (the four-label case). It does not classify an arbitrary truncated simplex, supply an equivariant sphere-wedge decomposition, determine integral homology of the quotient, or prove the quotient is homotopy equivalent to a sphere. Literature-index searches and the inspected primary texts cannot exclude an equivalent unpublished or unindexed calculation. No independent mathematical review is asserted.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1 (17 December 2005), https://arxiv.org/abs/math/0512420 .
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (2 July 2010), https://arxiv.org/abs/1007.0418 .
3. *The independence complexes of the truncated four- and five-simplices*, published-finding corpus archival record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-independence-complexes-of-the-truncated-four-and-five-simpli--4f07444cc928 .
4. *Edge-orbit matching-complex homotopy of the truncated tetrahedron*, published-finding corpus archival record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-edge-orbit-matching-complex-homotopy-of-the-truncated-tetrahedro--f5ae4a359c83 .
5. *The graph-metric Rips filtration of the truncated tetrahedron*, published-finding corpus archival record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-graph-metric-rips-filtration-of-the-truncated-tetrahedron--51e8cc219376 .
