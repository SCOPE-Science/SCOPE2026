# Two four-spheres in the full symmetry quotient of the triangular-prism forest complex

## Finding
Let \(P=C_3\square K_2\) be the simple triangular-prism graph, and let \(\mathcal F(P)\) be its graphic-matroid independence complex: a simplex is a set of prism edges containing no cycle. Its full graph automorphism group \(G=\operatorname{Aut}(P)\cong S_3\times C_2\) acts by edge permutations. The **ordinary geometric quotient** has exact integral homotopy type
\[
\boxed{\ |\mathcal F(P)|/G\simeq S^4\vee S^4.\ }
\]
In comparison, the original labeled forest complex satisfies
\[
|\mathcal F(P)|\simeq \bigvee^{18}S^4.
\]
The quotient is therefore three-connected, has \(\widetilde H_4\cong\mathbb Z^2\), and has no other reduced integral homology.

## Assumptions and scope
The prism has two triangles on \(\{0,1,2\}\) and \(\{3,4,5\}\), with three connecting edges \(\{0,3\},\{1,4\},\{2,5\}\). Its nine undirected edges are vertices of \(\mathcal F(P)\). A face is a **graph-edge subset** with no cycle, not a vertex-induced forest or a graph-matching family. The group has all simultaneous permutations of the three vertical pairs and the involution exchanging the two triangle layers; these give all twelve automorphisms. The quotient is the topological orbit space, not the homotopy quotient or an abstract complex formed by identifying individual vertex orbits. Homology is integral throughout.

The prism and \(K_{3,3}\) are the only simple connected cubic graphs on six vertices: the complement of any such graph is two-regular on six vertices, hence either \(C_6\) or the union of two triangles. Taking complements yields the prism and \(K_{3,3}\), respectively. Thus this result supplies the missing case alongside the already determined full-symmetry quotient of the \(K_{3,3}\) forest complex.

## Proof
**1. Covering complex and full symmetry.** Exact forest enumeration by a six-vertex union-find cycle test produces the numbers of nonempty forests with \(1,2,3,4,5\) edges:
\[
(9,36,82,111,75).
\]
Every maximal forest has five edges. A graphic-matroid independence complex is shellable and has the homotopy type of a wedge of top-dimensional spheres. Its reduced Euler characteristic is
\[
-1+9-36+82-111+75=18,
\]
so \(|\mathcal F(P)|\simeq\bigvee^{18}S^4\), in particular it is simply connected. The prism's two triangles are its only graph three-cycles, so an automorphism permutes them and induces a common permutation of the three connecting pairs. Conversely all such twelve maps preserve adjacency. The verifier also enumerates all \(6!\) vertex permutations and finds precisely twelve automorphisms.

**2. Genuine quotient chains.** Barycentrically subdivide \(\mathcal F(P)\). Its simplices are strict flags \(F_0\subsetneq\cdots\subsetneq F_d\) of nonempty forests. Graph automorphisms preserve \(|F_i|\), so any group element stabilizing a flag as a simplex fixes each flag vertex: there are no inversions. Consequently the orbit of each flag gives a genuine oriented \(d\)-cell of the geometric quotient. Different flag orbits are kept distinct, even when their orbit vertices coincide. Because deleting different positions gives distinct cardinality signatures, its integral cellular differential is exactly
\[
\partial[F_0\subsetneq\cdots\subsetneq F_d]
=\sum_{i=0}^d(-1)^i[F_0\subsetneq\cdots\widehat{F_i}\cdots\subsetneq F_d],
\]
where the bracket means the group orbit of the indicated flag. There are no stabilizer multipliers.

Exhaustive flag-orbit enumeration gives quotient cell counts by dimensions \(0,1,2,3,4\):
\[
(c_0,c_1,c_2,c_3,c_4)=(41,405,1339,1722,750).
\]
As an independent count, the sum of fixed-flag numbers over all twelve group elements, dimension by dimension, is
\[
(492,4860,16068,20664,9000)=12(c_0,c_1,c_2,c_3,c_4).
\]
This is Burnside's formula, evaluated by a separate fixed-subflag recurrence.

**3. Exact integral homology.** Build all four signed integer boundary matrices from flag deletions. Their numbers of nonzero entries are \((810,4017,6888,3750)\) and both consecutive-boundary compositions vanish exactly. Eliminate a matrix entry \(u=\pm1\) by integral elementary basis changes and the Schur complement \(A-bu^{-1}c\). Every such step splits off a contractible two-term chain summand, so these are integral chain-homotopy equivalences rather than rational rank operations. The exact verifier performs \(748,974,365,40\) cancellations, respectively, in descending degrees \(4,3,2,1\), checking the chain identities after each degree. The remaining chain groups have ranks
\[
(1,0,0,0,2)
\]
with zero differentials. Thus \(H_0\cong\mathbb Z\), \(H_4\cong\mathbb Z^2\), and all other integral homology groups vanish. In particular there is no hidden torsion.

**4. Fundamental group.** Independently, contract a spanning tree of the quotient one-skeleton (forty of its 405 edges). The remaining 365 oriented edges are free generators; each of the 1339 orbit triangles supplies its actual edge-word relator. The verifier reduces all 365 generators by valid Tietze substitutions and obtains an empty presentation, proving \(\pi_1=1\). There is also a conceptual independent check using Armstrong's orbit-space theorem. The layer reflection and any transposition of two vertical pairs fix a singleton connecting edge, while cyclic rotation of the three pairs preserves the three-edge connecting matching as a simplex and fixes its barycenter. These elements generate \(S_3\times C_2\) and all have fixed points, so the quotient of the group by the normal subgroup of fixed-point elements is trivial.

**5. Homotopy type.** The orbit space is a connected finite four-dimensional CW complex. Simple connectivity and the vanishing of \(H_2\) and \(H_3\) give \(\pi_2=\pi_3=0\) by successive Hurewicz isomorphisms; then \(\pi_4\cong H_4\cong\mathbb Z^2\). Pick maps from two copies of \(S^4\) representing an integral basis. Their wedge induces isomorphisms on all integral homology groups. By the homological Whitehead theorem for simply connected CW complexes, the wedge map is a homotopy equivalence, proving the claim.

## Verification
Run `python3 verify_prism_forest.py` in a directory containing the attached standalone program; it uses only the Python standard library. It enumerates all graph edges, forests, all twelve automorphisms (independently confirmed against \(6!\) permutations), strict forest flags and their orbits. It independently counts flag orbits by Burnside, verifies all signed chain identities, performs 2127 integer unit cancellations, and derives and exhaustively eliminates the geometric quotient's complete fundamental-group presentation. The complete observed output appears in `verification_output.txt`, ending in `PRISM_FOREST_FULL_QUOTIENT_WEDGE_TWO_S4_OK`. These finite certificates apply to this graph and this full automorphism action only. The passage from algebraic invariants to the full homotopy claim uses the explicitly stated topological theorems, not finite testing alone.

## Relationship to prior work
Ardila–Castillo–Samper's matroid-shellability results determine the standard nonequivariant framework, but neither a flag-orbit chain complex nor a homotopy type for this geometric quotient. The previously published full-symmetry quotient of the nine-edge six-vertex \(K_{3,3}\) forest complex is \(S^4\); it concerns the **other** connected cubic six-vertex graph. Its orbit theorem does not imply the prism result: the prism has two triangles, unlike \(K_{3,3}\), and their forest complexes have different face counts and automorphism groups. The published \(K_5\) forest quotient is a three-sphere for another graph and rank. An octahedral forest quotient exhibits degree-three two-torsion, showing that a general rule asserting all such full-symmetry quotients are wedges of top spheres would be false. The present result, together with the published \(K_{3,3}\) result, completes the **two-isomorphism-class** cubic six-vertex comparison. The claim is not presented as an unqualified general theorem on graphic matroids.

## Limitations
This is a homotopy equivalence, not a PL homeomorphism or a manifold classification. It does not classify proper-subgroup quotients, graphs on more vertices, or the equivariant homotopy type of the covering complex. The computation has a finite exact certificate whose correctness remains subject to external inspection; no independent mathematical audit is claimed here. A differently indexed or unindexed earlier computation of precisely the same prism quotient cannot be excluded solely by search.

## References
1. F. Ardila, F. Castillo and J. A. Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870, first public 2014-10-14, https://arxiv.org/abs/1410.3870, Theorems 1.3 and 1.5 and Section 2.
2. A. Björner, *The Homology and Shellability of Matroids and Geometric Lattices*, in *Matroid Applications* (1992), pp. 226–283, https://doi.org/10.1017/CBO9780511662041.008.
3. M. A. Armstrong, *The fundamental group of the orbit space of a discontinuous group*, Proc. Cambridge Philos. Soc. 64 (1968), 299–301, https://doi.org/10.1017/S0305004100042845.
4. *A four-sphere survives both symmetry quotients of the \(K_{3,3}\) forest complex*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-four-sphere-survives-both-symmetry-quotients-of-the-k-3-3-fore--c13c504f2dfd.
5. *The full vertex-symmetry quotient of the five-vertex forest complex is a homotopy three-sphere*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-the-full-vertex-symmetry-quotient-of-the-five-vertex-forest-comp--cd140a8be8be.
6. *Three independent two-torsion classes in the full octahedral forest quotient*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-three-independent-two-torsion-classes-in-the-full-octahedral-for--3ed6f4817ade.
