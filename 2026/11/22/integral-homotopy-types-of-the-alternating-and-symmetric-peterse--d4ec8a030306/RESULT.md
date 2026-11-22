# Integral homotopy types of the alternating and symmetric Petersen matching quotients

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, whose vertices are the two-element subsets of \(\{0,1,2,3,4\}\) and whose edges join disjoint pairs. Let \(X=\mathcal M(P)\) be the **ordinary matching complex**: its simplicial vertices are the fifteen edges of \(P\), and its faces are graph matchings of any size, including nonperfect ones. The label permutations act on \(X\) through \(\operatorname{Aut}(P)\cong S_5\), with alternating subgroup \(A_5\).

**Theorem.** The ordinary geometric orbit spaces satisfy
\[
|X|/A_5\simeq S^2,\qquad |X|/S_5\simeq *.
\]
More precisely, the quotient of the barycentric subdivision by \(S_5\) admits exactly 62 elementary free-face collapses to a point. The corresponding \(A_5\) quotient admits 100 elementary free-face collapses to a two-dimensional CW complex with 8 vertices, 18 edges, and 12 triangles; after contracting a maximal tree, eleven legitimate one-/two-cell cancellations leave one zero-cell and one two-cell with constant attaching map.

In particular, the \(A_5\) quotient is simply connected with \(\widetilde H_2\cong\mathbb Z\), whereas the \(S_5\) quotient is contractible; these integral homotopy assertions are stronger than the previously available rational orbit-homology computations.

## Assumptions and scope
The graph and both group actions are exactly as defined above. For \(H\in\{A_5,S_5\}\), \(|X|/H\) means the quotient of the *geometric realization* by the actual finite group action, not its fixed-point set, a Borel homotopy quotient, or the simplicial complex on face-orbit classes. The proof uses the genuine quotient cell structure of the barycentric subdivision. No conclusion is asserted for other graphs, other subgroups, or integral equivariant representation lattices.

Every original nonempty matching is a vertex of the barycentric subdivision \(\operatorname{sd}X\). A simplex is a strict flag of nonempty matchings. Since a group element preserves the matching cardinality, it cannot nontrivially permute the vertices of one flag. Consequently the action on flags has no inversions. Every flag orbit gives a valid quotient simplex with its rank-distinct boundary facets, so ordinary elementary free-face collapses are topologically legitimate.

## Proof
**1. Exhaustive finite starting complex.** Number the ten graph vertices by lexicographically ordered two-subsets of the five labels, and number the fifteen Petersen edges by lexicographically ordered disjoint vertex-pairs. Enumerate every edge subset of cardinality at most five, retaining it precisely when its members are vertex-disjoint. This yields the complete face vector, by dimensions zero through four,
\[
(15,75,145,90,6).
\]
The resulting barycentric subdivision has \((331,2460,5010,3600,720)\) simplices in dimensions zero through four, for 12,121 nonempty flags overall. These are exhaustive counts, not samples.

**2. Genuine orbit structures.** For each permutation of the five labels, calculate the induced permutation of the fifteen edges, every matching, and every flag. Partition all flags into group orbits, and form the quotient face incidence by deleting each member of a flag. Rank separation ensures that its distinct facets do not acquire identifications within the same quotient cell. The complete quotient face vectors, by dimensions zero through four, are
\[
\begin{array}{c|rrrrr}
 H&0&1&2&3&4\\\hline
 A_5&14&58&94&60&12\\
 S_5&10&32&47&30&6
\end{array}.
\]
For a live quotient cell \(\sigma\), a facet \(\tau\) is a free face exactly when \(\sigma\) is its unique live coface. Pairing the first such facet and coface in the deterministic ordered enumeration and repeating gives 100 elementary collapses for \(A_5\) and 62 for \(S_5\). The \(S_5\) quotient then has exactly one vertex and no higher cells, proving its contractibility. The \(A_5\) quotient has precisely eight vertices, eighteen edges and twelve triangles.

**3. Fundamental-group-and-homotopy reduction of the alternating quotient.** Contract the first available spanning tree of the remaining one-skeleton (seven edges). This is a homotopy equivalence and leaves one vertex with eleven oriented loop generators \(x_1,\ldots,x_{11}\), corresponding to the non-tree edges in sorted quotient-cell order. The twelve oriented two-cell attaching words, obtained from the *ordered* boundaries \((a,b)+(b,c)-(a,c)\) of rank-increasing flags \(a<b<c\), are
\[
\begin{aligned}
&x_4,\quad x_7,\quad x_1x_4,\quad x_1x_6,\\
&x_9x_2^{-1},\quad x_8x_3^{-1},\quad x_{10},\quad x_{10}x_3^{-1},\\
&x_{11},\quad x_{11}x_2^{-1},\quad x_5x_8x_6^{-1},\quad x_5x_9x_7^{-1}.
\end{aligned}
\]
Every one of the eleven generators is eliminated by a relator in which it occurs exactly once (with exponent \(+1\) or \(-1\)). Such a relator permits the standard homotopy-preserving cellular cancellation of its loop against its two-cell after the indicated attaching-word substitutions; it is not merely an abelian chain reduction. One possible generator-elimination order is \(4,1,6,7,10,3,8,5,9,2,11\). The sole unpaired two-cell ultimately has the empty attaching word, so the reduced CW complex consists of a point and a two-cell attached constantly. It is \(S^2\). This proves the second homotopy assertion and also verifies the claimed integral homology and simple connectivity.

**4. Exhaustiveness of the certificate.** Every input matching, flag, label permutation, quotient cell, boundary facet, free-face cancellation, maximal-tree edge, and relation substitution is built from the displayed definitions. The attached executable verifies all counts and both complete cancellation sequences without precomputed matrices or external code/data. These computations constitute finite, exact proofs for this fixed graph and these two groups; no parameter extrapolation or claim about an unexamined infinite family is involved.

## Verification
Run `python3 verify.py` in a directory containing the standalone attached verifier (Python standard library only). It reconstructs all 12,121 original flags, all 120 label permutations, each quotient cell and incidence, and checks the entire sequence of topological free-face collapses. It then constructs the one-skeleton and oriented triangle words of the reduced alternating quotient, verifies a spanning tree and eleven homotopy-preserving one-/two-cell cancellations, and checks that exactly one spherical two-cell remains. The terminal success marker is `PETERSEN_ORBIT_HOMOTOPY_OK`.

This verifier is a directly reproducible finite mathematical certificate, not an independent mathematical audit. No unreplayed log is relied upon for the proof.

## Relationship to prior work
Zaslavsky [1], §3.2, classifies Petersen graph matchings up to automorphisms and proves there are one, two, four, two and one full-symmetric-group orbit types in matching cardinalities one through five. This gives essential combinatorial context but does not compute the homotopy of geometric matching-complex orbit spaces, whose cells depend on *flags*, not only face orbits.

Published Petersen-matching-complex results [2] establish the unquotiented integral homotopy type \(X\simeq\bigvee^5 S^2\vee\bigvee^5 S^3\) and the natural rational \(S_5\) representations on those groups. A separate full-text published calculation [3] already states that \(|X|/S_5\) has no positive rational homology and that \(|X|/A_5\) has one rational degree-two class. Those results are credited, not reclaimed. Crucially, neither a rationally acyclic quotient nor the rational homology of a sphere determines its integral homotopy type; possible torsion, nontrivial fundamental groups and attaching maps remain. The explicit **ordinary quotient** CW reductions above establish the stronger homotopy conclusions.

The Petersen perfect-matching complex, the two-matching complex, and \(\mathcal M(K_5)\) are different simplicial complexes. Results about these objects cannot be substituted for the ordinary matching complex of the Petersen graph.

## Limitations
This is an exact finite classification for two canonical subgroup actions on one graph. It does not provide a general classification for every subgroup of \(S_5\) or every cubic graph. Literature and published-result searches under Petersen matching, line-graph independence, alternating/symmetric orbit spaces, attaching maps and barycentric quotients did not disclose an equivalent published integral homotopy theorem, but incomplete indexing or an unstated deduction in related work remains possible. The scientific review is not independently audited.

## References
[1] T. Zaslavsky, *Six signed Petersen graphs, and their automorphisms*, *Discrete Mathematics* **312** (2012), 1558–1583, §3.2, https://doi.org/10.1016/j.disc.2011.12.010; archived preprint first posted 2013-03-14, https://arxiv.org/abs/1303.3347.

[2] *The Petersen matching complex: two sphere dimensions and distinct symmetric-group modules*, published research record dated 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-the-petersen-matching-complex-two-sphere-dimensions-and-distinct--36a1043f768e.

[3] *Full symmetric-group homology of the Petersen ordinary matching complex*, published research record dated 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-full-symmetric-group-homology-of-the-petersen-ordinary-matching--a2f5d30f54a6.

[4] R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* **134** (1998), 90–145, for homotopy-preserving cellular cancellations.
