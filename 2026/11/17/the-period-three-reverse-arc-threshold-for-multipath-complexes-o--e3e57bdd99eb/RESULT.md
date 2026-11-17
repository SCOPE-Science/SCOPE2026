# The period-three reverse-arc threshold for multipath complexes of directed polygons

## Finding
Let \(k\ge2\) and \(N=3k\). Write the vertices of a directed polygon as \(v_i\), with indices in \(\mathbb Z/N\mathbb Z\), and put \(f_i:v_i\to v_{i+1}\) and \(r_i:v_{i+1}\to v_i\). Begin with all \(N\) forward arcs and add the \(k\) reverse arcs \(r_0,r_3,\ldots,r_{3k-3}\), in any order. For \(0\le t\le k\), let \(G_t\) be the resulting digraph after the first \(t\) reverse arcs, and let \(X_t\) be its multipath simplicial complex (faces are sets of arcs whose connected components are vertex-disjoint directed simple paths and isolated vertices).

Then, integrally and without stabilization,
\[
|X_t|\simeq S^{N-2}\quad(0\le t<k),\qquad
|X_k|\simeq S^{k-1}\vee S^{N-2}.
\]
For \(0\le t<k\), the inclusion of the original forward-cycle complex \(X_0\hookrightarrow X_t\) is a homotopy equivalence. At the last step, \(X_0\hookrightarrow X_k\) induces an isomorphism onto a primitive direct summand in integral degree \(N-2\), and a new free generator is born in degree \(k-1\). Thus all earlier inclusion maps are homotopy equivalences, while the final map preserves the top class and introduces exactly one lower-dimensional class. All other reduced integral homology groups vanish.

More generally, for any choice of fewer than \(\lceil N/3\rceil\) reverse arcs on the coherently directed \(N\)-cycle, the inclusion of the forward-cycle multipath complex is a homotopy equivalence. When \(N=3k\), the only reverse-arc supports of cardinality \(k\) that meet every length-three cyclic interval are the three rotations of the period-three support above. These are precisely the first possible nontrivial reverse-arc homotopy transitions at the minimum arc budget.

## Assumptions and scope
Graphs are finite and loopless; opposite arcs are permitted. The term *multipath* uses the standard directed-linear-forest definition, not ordinary graph path homology. A nonempty face is a set of distinct arcs with indegree and outdegree at most one at every vertex and with no directed cycle. A two-cycle formed by both opposite arcs of an underlying edge is forbidden. Homotopy equivalences are of geometric realizations of simplicial complexes. The zero-reverse complex is the boundary of the simplex on all forward arcs. The classification requires \(k\ge2\); no conclusion is asserted here for an arbitrary support of \(k+1\) or more reverse arcs.

## Proof
**1. Local conflicts and the dominating threshold.** In an underlying simple cycle, every directed cycle of length at least three traverses the entire underlying cycle in a consistent orientation. Because all forward arcs exist but reverse arcs form a proper subset, the only possible cycles are the full forward cycle and local two-cycles. A reverse arc \(r_i\) conflicts with exactly three forward arcs: \(f_{i-1}\), which has the same target, \(f_i\), which forms a two-cycle, and \(f_{i+1}\), which has the same source. Two reverse arcs indexed at cyclic distance at least three have no degree or cycle conflicts.

For any reverse support \(S\), if some forward arc \(f_j\) lies outside all cyclic triples \(\{f_{i-1},f_i,f_{i+1}\}\) for \(i\in S\), pair every face containing at least one reverse arc and missing \(f_j\) with the face obtained by adding \(f_j\). These are valid face pairs, because \(f_j\) conflicts with no selected reverse arc, and the full forward cycle cannot occur in a face containing a reverse arc. The matching is acyclic: directed upward matching steps only add \(f_j\), whereas any other downward step deletes an arc different from \(f_j\); a closed gradient path is impossible. All unpaired faces form exactly the boundary of the full forward simplex, so the complex simplicially collapses to this boundary, and the inclusion is a homotopy equivalence. Each reverse arc blocks at most three forward arcs, so this applies whenever \(|S|<N/3\).

For \(N=3k\), a support of exactly \(k\) reverse arcs blocks every forward arc only if all its length-three blocked intervals are pairwise disjoint and cover the cycle. Their centers must therefore be spaced by exactly three modulo \(N\), yielding the stated support up to rotation. Thus the problem reduces to the minimum dominating arrangement.

**2. Factorization at the threshold.** For \(j=0,\ldots,k-1\), set \(B_j=\{f_{3j-1},f_{3j},f_{3j+1}\}\) (indices modulo \(N\)), and set \(s_j=r_{3j}\). The sets \(B_j\) partition all forward arcs. Let \(E_j\) be the disjoint union of a filled two-simplex on \(B_j\) and the isolated vertex \(s_j\), and set \(J=E_0*\cdots*E_{k-1}\). By the degree and cycle characterization in the preceding paragraph, the multipath complex is
\[
X_k=J\setminus\{F\},\qquad F=\{f_0,\ldots,f_{N-1}\}.
\]
Here only the maximal full-forward face \(F\), not its boundary, is removed. Every other face of the join is a multipath. In particular the augmented face count of \(X_k\) (including the empty face) is exactly \(9^k-1\).

**3. Relative discrete-Morse collapse.** Pick one vertex \(b_j\in B_j\) for each \(j\), and let
\[
Y=\{b_0,s_0\}*\cdots*\{b_{k-1},s_{k-1}\}\cong S^{k-1},
\]
where the braces denote a discrete two-point complex. On \(J\), match every face not in \(Y\) by toggling \(b_j\), where \(j\) is the least index for which the face contains some forward vertex of \(B_j\setminus\{b_j\}\). This is a well-defined matching: the presence of an extra forward vertex excludes \(s_j\), so toggling \(b_j\) is permitted, and the chosen index does not change upon toggling. Every face outside \(Y\) is paired.

For acyclicity, in any alternating gradient path the set of extra forward vertices \(\bigcup_j(B_j\setminus\{b_j\})\) can only decrease at unmatched downward steps and is unchanged at upward matched steps. On a hypothetical closed path it is constant, so the matched group index is fixed. Each matched upward step then adds the same \(b_j\), while an unmatched downward step cannot remove that \(b_j\) (that would reverse its matched edge); it must remove another vertex. The number of remaining other vertices strictly decreases, a contradiction. Consequently this is a relative acyclic matching collapsing \(J\) onto \(Y\).

Now delete the maximal face \(F\) to obtain \(X_k\). The same matching restricts to \(X_k\) except that the single face \(C=F\setminus\{b_0\}\) loses its partner \(F\). Thus, relative to \(Y\), the matching has exactly one critical cell \(C\), of dimension \(N-2\). Relative discrete-Morse theory gives a CW homotopy model \(Y\cup_\alpha e^{N-2}\), with the homotopy equivalence fixed on \(Y\).

**4. The attaching map vanishes.** There is an explicit simplicial retraction \(\rho:X_k\to Y\): send every forward vertex of \(B_j\) to \(b_j\) and fix \(s_j\). Any face chooses forward vertices from \(B_j\) or the isolated reverse vertex \(s_j\), never both; hence the vertex map is simplicial. It fixes every face of \(Y\). Transport the retraction through the relative CW equivalence. The resulting map from \(Y\cup_\alpha e^{N-2}\) to \(Y\) restricts to the identity on \(Y\). Its restriction to the attaching cell nullhomotopes \(\alpha\), so \(\alpha\) is nullhomotopic and \(X_k\simeq Y\vee S^{N-2}\). In particular the answer is an integral homotopy classification, not an inference from field homology.

**5. The actual filtration maps.** For the final stage, the pair \((J,X_k)\) has precisely one relative cell, the full-forward simplex \(F\) in dimension \(N-1\), so \(H_{N-1}(J,X_k;\mathbb Z)\cong\mathbb Z\). Because \(J\) collapses onto \(Y\simeq S^{k-1}\) and \(N-2>k-1\), the long exact sequence of the pair makes the connecting homomorphism \(\mathbb Z\to \widetilde H_{N-2}(X_k;\mathbb Z)\) an isomorphism. Its generator is exactly the boundary of \(F\), which is the original forward directed-cycle sphere. This establishes the primitive inclusion statement. The collapse argument in Step 1 establishes homotopy equivalence for every preceding stage.

## Verification
The standalone `verify.py` independently enumerates directed arc subsets and tests the multipath condition directly, compares the resulting faces to the factorized join description, verifies the relative matching and its acyclicity, computes the reduced Euler characteristic, and performs modular boundary-rank computations. For \(k=2,3,4\) (cycles with 6, 9, and 12 vertices) it found 80, 728, and 6,560 augmented faces, respectively, as predicted by \(9^k-1\). For \(k=2,3\), the integral formula's Betti numbers agree independently over fields of characteristics two and three; for \(k=4\) they agree over characteristic two. The finite tests only check the construction and do not prove the all-parameter theorem; the infinite proof is Steps 1–5.

Reproduce using Python 3 without third-party packages: `python verify.py`.

## Relationship to prior work
Caputi, Collari and Smith (2026), Proposition 2.13, prove that keeping all forward arcs and deleting three consecutive reverse arcs preserves the forward-cycle sphere. This explains the no-change side of the transition, and Step 1 strengthens it by identifying the inclusion as a simplicial collapse. Their Sections 2.1–3 discuss full bidirectional polygons and nearly complete reverse directions, not the minimum period-three reverse support whose missing reverse arcs occur in runs of exactly two. In particular, their proposition is inapplicable to the final threshold stage. Caputi, Collari, Di Trani and Smith (2023/2024) prove wedge/contractibility results for polygon orientations and dynamical-module decompositions; those statements neither compute this partially bidirected strongly connected polygon nor its filtration inclusions. Independent classifications of fully bidirected cycles have different arc sets; a homotopy formula for a larger complex cannot determine its proper subcomplex's homotopy type. No identical threshold classification was identified in the consulted research database and literature, subject to bibliographic residual risk.

## Limitations
The homotopy wedge and integral inclusion formula apply to \(N=3k\), \(k\ge2\), with exactly the indicated period-three reverse pattern. The stability portion applies to any subset of fewer than \(\lceil N/3\rceil\) reverse arcs. Nothing here determines the topology after extra reverse arcs beyond the minimum dominating support, nor the full equivariant homotopy type. The result has been checked by one scientific analysis and finite executable tests; it has no independent expert audit.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, first publicly posted January 9, 2026. https://arxiv.org/abs/2601.05670 (especially Definition 1.2, Proposition 2.13 and surrounding discussion).
2. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, *Mathematika* 70 (2024), e12235, first published December 9, 2023, https://doi.org/10.1112/mtk.12235 (especially Theorem 1.1 and Example 2.3).
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145; relative acyclic partial matchings are used in the elementary discrete-Morse manner described in the proof.
