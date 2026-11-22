# The full symmetry quotient of the Tietze matching complex is a homotopy three-sphere

## Finding
Let \(T\) be the twelve-vertex cubic Tietze graph, obtained by replacing one vertex of the Petersen graph with a triangle and attaching the three former neighbors to the three distinct triangle vertices. Let \(\mathcal M(T)\) be the **ordinary matching complex**, with one simplicial vertex for each graph edge and with a simplex for each set of mutually vertex-disjoint graph edges. For the complete twelve-element graph automorphism group \(G=\operatorname{Aut}(T)\cong S_2\times S_3\cong D_6\), the **ordinary geometric orbit space** satisfies

\[
\boxed{|\mathcal M(T)|/G\simeq S^3.}
\]

It follows that the quotient is simply connected, has \(H_0\cong H_3\cong\mathbb Z\) and no other nonzero integral homology, and has no torsion. The result is a homotopy equivalence, **not** a claim of a sphere homeomorphism, manifold structure, or equivariant equivalence. It concerns ordinary orbits, not the Borel construction.

## Assumptions and scope
Start with \(\operatorname{KG}(5,2)\), whose ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), adjacent exactly when disjoint. Delete the vertex \(\{0,1\}\), replace it by a three-cycle, and attach its three old neighbors \(\{2,3\},\{2,4\},\{3,4\}\) bijectively to the new triangle vertices. All remaining Petersen edges persist. This defines a simple graph with twelve vertices, eighteen edges, and one triangle. Relabel vertices and lexicographically sort edges as in `code/verify_tietze_full_quotient.py`; all simplex masks use the resulting indices zero through seventeen.

The group acts by graph-edge permutations. It is the full graph automorphism group: the unique triangle is invariant, its contraction gives the vertex-stabilizing Petersen automorphisms, and the verifier independently enumerates exactly twelve graph automorphisms. Every finite computation below is exhaustive for this one specified graph; there is no quantification over a family of graphs.

## Proof
**1. The actual quotient cell structure.** A matching is any subset of the eighteen graph edges with no shared graph endpoint. Exhaustive enumeration gives precisely \(1051\) nonempty matchings, by simplex dimension zero through five:

\[
(18,117,335,408,165,8).
\]

Write \(P\) for their inclusion poset. The first barycentric subdivision is the order complex \(\Delta(P)\), whose simplices are strict chains \(F_0\subsetneq\cdots\subsetneq F_d\) of nonempty matching faces. There are \(162053\) such chains. Each automorphism preserves face cardinality, so a group element stabilizing a chain fixes all its vertices, without any simplex inversion. In particular, the ordinary quotient has a regular simplicial orbit-cell (\(\Delta\)-complex) structure with one cell for each orbit of strict chains. The counts of orbit cells in degrees zero through five are

\[
(121,1250,3981,5222,2850,480).
\]

For a representative chain, the cellular boundary is the integer alternating sum of the orbit cells obtained by deleting one entry. Different missing positions have distinct rank sets, so there are no orientation reversals or artificial stabilizer-divisions. The verifier enumerates every orbit, independently checks the total by Burnside's lemma, constructs all \(52461\) nonzero incidences, and checks \(\partial^2=0\) exactly over \(\mathbb Z\).

**2. Integral homology without a field inference.** On this regular cell structure, the verifier repeatedly deletes a codimension-one free facet and its unique maximal coface. Each deletion is an elementary cellular collapse and preserves homotopy type. An explicitly deterministic greedy sequence performs \(6524\) such collapses, leaving a subcomplex with cell counts \((43,235,385,193)\) in dimensions zero through three. Its integral cellular chain complex then undergoes \(427\) **unimodular algebraic cancellations**: at each step a boundary coefficient \(\pm1\) is pivoted out by exact integer column operations and the corresponding pair of chain generators is removed. Unlike the preceding free-face deletions, these are chain-level cancellations only; no assertion of topological collapse is made for them. They leave exactly one generator in degree zero and one in degree three, with zero boundary, and exhaust all chains. Consequently

\[
H_k(|\mathcal M(T)|/G;\mathbb Z)=
\begin{cases}\mathbb Z,& k=0,3,\\0,&\text{otherwise}.\end{cases}
\]

Because every algebraic pivot is a unit, the computation proves the **integral** groups and excludes torsion, rather than merely determining rational ranks or modular homology.

**3. Fundamental group independent of the integral reductions.** Use only the actual remaining topological subcomplex after the \(6524\) free-face collapses, not the chain-reduced complex. Its one-skeleton is connected, with \(43\) vertices and \(235\) edges. A reproducible spanning tree has \(42\) edges, leaving \(193\) generators. Its \(385\) triangular cells give the oriented relators \(e_{01}e_{12}e_{02}^{-1}\), with tree edges set to the identity and all edges oriented from lower to higher face cardinality. Exact free reduction and cyclic rotation, followed by generator elimination whenever that generator occurs once in a relator, eliminate **all** \(193\) generators. At each step the generator is substituted into every remaining relator by an equivalent Tietze move. Every residual relator becomes empty. This is an explicit nonabelian presentation proof that \(\pi_1=1\), not an inference from vanishing first homology.

**4. Homotopy conclusion.** The quotient is a connected simply connected CW complex with \(H_2=0\) and \(H_3\cong\mathbb Z\), with all other positive-degree integral homology zero. Hurewicz therefore gives \(\pi_2=0\) and \(\pi_3\cong\mathbb Z\). Represent a generator by a map \(S^3\to|\mathcal M(T)|/G\). This map is an integral homology isomorphism. By the homological Whitehead theorem for simply connected CW complexes, it is a homotopy equivalence.

## Verification
Run `python3 code/verify_tietze_full_quotient.py` from the extracted package root, using only the Python standard library. It regenerates the graph, the **complete** automorphism group by both a constructive action and independent adjacency backtracking, all matchings and strict flags, the full orbit-cell boundary, an independent Burnside count, all free-face deletions, exact integer unit cancellations, and every fundamental-group relator substitution. The recorded execution output is in `verification/output.txt`. No precomputed boundary matrices or external scripts are needed. Critical assertions terminate the verifier upon a mismatch.

## Relationship to prior work
Marietti and Testa's 2007 work treats matching complexes of **forests**, not this triangle-inflated Petersen graph, which contains cycles. Jonsson's exact-sequence work treats complete-graph matching complexes \(\mathcal M(K_n)\), not \(\mathcal M(T)\), and does not determine this quotient. The most relevant previously published **exact-object** result gives \(\mathcal M(T)\simeq\bigvee^{16}S^3\) and the full twelve-element rational symmetry character, including a one-dimensional invariant subspace in third homology. That rational invariant line implies at most the rational quotient Betti number, **not** integral torsion-freeness, trivial fundamental group, or the homotopy equivalence established here. Its result text does not assert an orbit-space homotopy type.

A separate published calculation of the Tietze **perfect-matching extendibility** complex treats a different simplicial complex, whose homotopy type is a wedge of circles. Other known three-sphere matching-quotient classifications concern different graphs, including an eleven-vertex wheel and a pentagonal prism; neither is a theorem covering Tietze by substitution. The equivalent description \(\mathcal M(T)=\operatorname{Ind}(L(T))\), where \(L(T)\) is the line graph, was also considered in the novelty checks. No inspected result implies the displayed integral orbit-space classification.

## Limitations
The computation covers this single graph and its complete automorphism group; it does not establish a parameter-family theorem or determine any proper-subgroup quotient. It establishes homotopy equivalence only, not a homeomorphism or a manifold classification. Exact machine-reproducible finite evidence is necessary for its integral and fundamental-group calculations. Bounded literature searches cannot exclude equivalent work that is unindexed, inaccessible or formulated differently.

## References
1. M. Marietti and D. Testa, *A simple uniform approach to complexes arising from forests*, arXiv:0705.1461v1, first public 2007-05-10. https://arxiv.org/abs/0705.1461
2. J. Jonsson, *Exact sequences for the homology of the matching complex*, arXiv:1203.5641v1, first public arXiv 2012-03-26; journal version earlier (2008). https://arxiv.org/abs/1203.5641
3. *Sixteen three-spheres and the full dihedral character of the Tietze matching complex*, published mathematical result, 2026-11-08. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sixteen-three-spheres-and-the-full-dihedral-character-of-the-tie--6f93a3f35ff0/RESULT.md
4. *The Tietze perfect-matching complex: six circles and its full rational symmetry character*, published mathematical result, 2026-11-01. https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-the-tietze-perfect-matching-complex-six-circles-and-its-full-rat--66b3f7013d3d/RESULT.md
5. *A three-sphere homotopy quotient of the eleven-vertex wheel matching complex*, published mathematical result, 2026-11-17. https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-a-three-sphere-homotopy-quotient-of-the-eleven-vertex-wheel-matc--55474f75fdcd/RESULT.md
6. *The full-symmetry quotient of the pentagonal-prism matching complex is a three-sphere*, published mathematical result, 2026-11-17. https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-the-full-symmetry-quotient-of-the-pentagonal-prism-matching-comp--5d7c581e07d3/RESULT.md
