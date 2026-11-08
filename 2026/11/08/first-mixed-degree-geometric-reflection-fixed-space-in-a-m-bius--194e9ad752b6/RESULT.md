# First mixed-degree geometric reflection fixed space in a Möbius-ladder perfect-matching complex

## Finding

Let \(M_{2n}\) be the simple graph on \(\mathbb Z/(2n)\) whose edges are \(\{i,i+1\}\) and \(\{i,i+n\}\), with arithmetic modulo \(2n\). Let \(X_n=\mathcal M_p(M_{2n})\) be the simplicial complex whose vertices are graph edges and whose faces are the edge collections contained in at least one *perfect matching* of the graph. For \(a\in\{0,1\}\), define the reflection \(s_a(i)=a-i\pmod{2n}\). Then, for every integer \(2\le n\le8\), the geometric fixed spaces have the following **integral homotopy types**:

| \(n\) | Vertex-axis fixed space \(|X_n|^{s_0}\) | Edge-axis fixed space \(|X_n|^{s_1}\) |
| ---: | --- | --- |
| \(2\) | point | three discrete points |
| \(3\) | point | point |
| \(4\) | point | \(S^1\sqcup\{\ast\}\) |
| \(5\) | point | \(S^1\vee S^1\) |
| \(6\) | point | \(S^1\vee S^1\) |
| \(7\) | point | \(S^1\vee S^1\) |
| \(8\) | point | \(S^1\vee S^2\) |

In particular, \(n=8\) is the **first parameter** for which a reflection-fixed space has nonzero second integral homology. Its edge-axis fixed space has one free integral homology generator in each of degrees one and two, even though the nonequivariant perfect-matching complex is \(X_8\simeq S^3\vee S^3\), by Agarwal–Basak [1]. The occurrence of two distinct positive homological degrees in the *geometric fixed space* is not determined by a rational character or a Lefschetz trace.

## Assumptions and scope

All graphs and complexes are finite. At \(n=2\), duplicate descriptions of edges are identified: \(M_4\) is \(K_4\). The involutions \(s_a\) act on graph edges and hence simplicially on \(X_n\). The notation \(|X_n|^{s_a}\) means points of the geometric realization fixed **pointwise** by the reflection, not merely the induced complex on individually invariant graph edges and not a quotient space. The statement covers only the two conjugacy classes of reflections, and only \(2\le n\le8\). No monotonicity in \(n\) is asserted.

For an orbit \(O\) of graph edges under the reflection, retain it as a vertex of a new simplicial complex precisely if its constituent graph edges form a face of \(X_n\). A collection of these orbit-vertices spans a simplex precisely when their union forms a face of \(X_n\). Call this finite simplicial complex \(F_{n,a}\).

## Proof

**Geometric orbit lemma.** On each abstract simplex, a fixed geometric point has equal barycentric coordinates at the members of every orbit of its vertices. Conversely, any nonnegative barycentric weight on complete vertex-orbits with a union constituting a face determines such a fixed point. The identifications on common faces agree. Thus the orbit construction gives a piecewise-linear homeomorphism \(|X_n|^{s_a}\cong_{\mathrm{PL}}|F_{n,a}|\). This holds whether or not the members of an orbit are individually fixed.

**Complete finite construction.** For each \(2\le n\le8\), enumerate all graph perfect matchings recursively by matching the smallest still-unmatched graph vertex to each available neighbor. Enumerate every edge-subset of each perfect matching, retain those invariant under \(s_a\), and compare their exact sets with the unions of faces of \(F_{n,a}\). These two constructions agree in all fourteen cases. Therefore the finite enumerations are exhaustive—not sampled matchings or guessed orbit extensions. All certificates are recomputed and checked by the accompanying standalone program [3].

**Elementary simplicial reductions.** Repeatedly choose a nonempty face having exactly one immediate coface and delete that free face together with the unique coface. Check the free-face condition before every deletion. For the vertex-axis reflections these moves leave precisely one vertex in every case. For the edge-axis reflection, the numbers of elementary pairs for \(n=2,3,4,5,6,7,8\) are respectively \(1,6,4,12,20,46,65\). The surviving complexes are: three isolated vertices at \(n=2\); one vertex at \(n=3\); a graph with five vertices, four edges, two components and cycle rank one at \(n=4\); connected graphs with two independent cycles at \(n=5,6,7\); and, at \(n=8\), a two-dimensional simplicial complex with \(8\) vertices, \(15\) edges and \(8\) triangles.

**The mixed-degree case.** For \(n=8,a=1\), the original fixed orbit complex has face vector \((13,49,63,31,5)\), in dimensions zero through four. The 65 verified collapses leave a connected two-complex with face vector \((8,15,8)\). Collapse a spanning tree consisting of seven edges. The resulting CW presentation has eight oriented circle generators \(g_1,\ldots,g_8\) and exactly eight two-cell attaching words:
\[
 g_1,\quad g_2,\quad g_3,\quad g_5,\quad
 g_1g_4,\quad g_2g_6,\quad g_3g_8g_4^{-1},\quad g_5g_8g_6^{-1}.
\]
These words come directly from the oriented triangular boundaries, with tree edges assigned the constant path. Successive elementary one-cell/two-cell cancellations remove the pairs indexed by \(g_1,g_2,g_3,g_5,g_4,g_6,g_8\) in that order; a generator occurs exactly once in its selected attaching word at every step. Equivalently, one performs the induced substitutions in the other attaching maps before deleting the cancelling pair. One circle generator \(g_7\) and one two-cell with *trivial attaching word* remain. This CW complex is \(S^1\vee S^2\), giving the exact integral homotopy classification. The program independently reconstructs the eight attaching words and verifies all seven cancellations and the empty remaining attaching word.

Combining the fourteen reductions proves the entire table. The entries for \(n<8\) have no second homology, while the \(n=8\) edge-axis entry has \(H_2\cong\mathbb Z\), proving first occurrence.

## Verification

Run `python3 mobius_reflection_fixed_verify.py` (Python standard library only). It enumerates every perfect matching, independently re-enumerates every setwise invariant original face, verifies equality with the orbit model, checks each free-face collapse in the *actual* complex, computes all residual graph component and cycle ranks, then reconstructs and simplifies the eight two-cell attaching words. The successful execution is recorded in `mobius_reflection_fixed_checks.txt`, ending `MOBIUS_REFLECTION_FIRST_MIXED_FIXED_TYPE_OK`. The full script and its recorded output are supplied, rather than relying on an externally stored run path.

## Relationship to prior work

Agarwal and Basak [1] classify the *nonequivariant* perfect-matching complex, in particular \(X_8\simeq S^3\vee S^3\); their full-text perfect-matching section does not calculate pointwise geometric reflection-fixed spaces. The published Möbius-ladder dihedral homology studies [2] compute homological characters and Lefschetz traces, including the reflection character for even \(n\), but those alternating rational traces do not specify the integral homotopy type of \(|X_n|^{s_a}\). The present claim concerns a finite sharp first mixed-degree fixed-space occurrence, not a new nonequivariant homotopy classification or another character computation. A related all-graph prism-layer-swap theorem concerns a different group action and has only one positive homological degree in its noncontractible fixed spaces. Exact implications were compared, not just titles.

## Limitations

Only \(2\le n\le8\) and the two specified reflection classes are classified. The result does not give a formula for larger Möbius ladders, simultaneous fixed points of subgroups, or equivariant homotopy equivalences. Algebraic cell cancellations were validated for the actual reduced two-complex, but no independent mathematical audit has been performed. The literature comparison cannot exclude an unindexed equivalent computation.

## References

1. Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (first posted 2026-08-31; revised 2026-09-14), especially Section 5.1, Theorem 21 and the main theorem. https://arxiv.org/html/2608.30601v2
2. Published mathematical computations: *Complete dihedral rational homology representations of odd Möbius-ladder perfect-matching complexes*; *Rotation has order two or four on Möbius-ladder perfect-matching homology*; *The antipodal half-turn representation on Möbius-ladder perfect-matching homology*; and the corresponding complete even-dihedral character record. The first three are retrievable under the public published-finding corpus 2026/10/11 research collection; their claims concern rational representations rather than geometric fixed-point homotopy types.
3. Accompanying standalone code `mobius_reflection_fixed_verify.py` and its execution record `mobius_reflection_fixed_checks.txt`; both are embedded in the same research package.
