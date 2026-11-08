# Total-visibility complexes of clique substitutions are iterated simplicial wedges

## Finding

For a finite connected simple graph \(G\) on \(h\ge2\) vertices, replace each vertex \(i\) with a clique \(V_i\) of size \(m_i\ge2\), and put all edges between \(V_i\) and \(V_j\) precisely when \(ij\) is an edge of \(G\). Write \(H\) for the resulting graph. Let \(\Delta_t(G)\) denote the abstract simplicial complex of total mutual-visibility sets: a face \(F\subseteq V(G)\) requires that every two graph vertices admit a shortest path without internal vertices of \(F\). Set \(M=\sum_i m_i\), \(R=M-h\), and \(F(S)=\{i:V_i\subseteq S\}\).

**Full-fiber and composition theorem.** For every \(S\subseteq V(H)\),
\[
S\in\Delta_t(H)\quad\Longleftrightarrow\quad F(S)\in\Delta_t(G).
\]
Thus \(\Delta_t(H)\) is exactly the simplicial composition \(\Delta_t(G)(\partial\Delta^{m_1-1},\ldots,\partial\Delta^{m_h-1})\), also called the iterated simplicial wedge with these multiplicities. As a consequence of the established composition homotopy theorem,
\[
\Delta_t(H)\simeq \Delta_t(G)*\partial\Delta^{m_1-1}*\cdots*\partial\Delta^{m_h-1}.
\]
Here \(*\) denotes simplicial join. When \(\Delta_t(G)\) has nonempty geometric realization, this is the \(R\)-fold suspension of its realization. In the augmented complex convention, integral reduced homology shifts by \(R\):
\[
\widetilde H_q(\Delta_t(H);\mathbb Z)\cong\widetilde H_{q-R}(\Delta_t(G);\mathbb Z).
\]
For the base consisting only of the empty face, its augmented homology in degree \(-1\) is \(\mathbb Z\), giving a sphere of dimension \(R-1\) after composition. In particular the construction preserves integral torsion, shifted in degree.

**Exact enumerators.** Let \(\mathcal T_H(z)\) count all total mutual-visibility sets of \(H\) by cardinality, and let \(\mathcal Q_H(z)\) count its inclusion-maximal such sets. Then
\[
\mathcal T_H(z)=\sum_{F\in\Delta_t(G)}\left(\prod_{i\in F}z^{m_i}\right)\left(\prod_{i\notin F}((1+z)^{m_i}-z^{m_i})\right),
\]
\[
\mathcal Q_H(z)=\sum_{F\in\operatorname{Facets}(\Delta_t(G))}\left(\prod_{i\notin F}m_i\right)z^{R+|F|}.
\]
If \(\mathcal B(G)\) is the set of inclusion-minimal index sets among \(N_G(u)\cap N_G(v)\) for all pairs with graph distance \(2\), the minimal nonfaces of \(\Delta_t(H)\) are exactly \(\bigcup_{i\in B}V_i\) for \(B\in\mathcal B(G)\). This identifies its Stanley--Reisner ideal by the corresponding squarefree monomials.

**Cycle consequence, including unequal fibers.** For \(G=C_n\), with \(n\ge3\) and all \(m_i\ge2\), the complex \(\Delta_t(H)\) is a simplex when \(n=3\). When \(n=4\), it is combinatorially the join
\[
\partial\Delta^{m_0+m_2-1}*\partial\Delta^{m_1+m_3-1},
\]
so it is a PL sphere of dimension \(M-3\), and
\[
\mathcal T_H(z)=\big((1+z)^{m_0+m_2}-z^{m_0+m_2}\big)\big((1+z)^{m_1+m_3}-z^{m_1+m_3}\big),\quad
\mathcal Q_H(z)=(m_0+m_2)(m_1+m_3)z^{M-2}.
\]
For \(n\ge5\), it is the join \(\bigast_{i=0}^{n-1}\partial\Delta^{m_i-1}\), a PL sphere of dimension \(M-n-1\), and
\[
\mathcal T_H(z)=\prod_{i=0}^{n-1}\big((1+z)^{m_i}-z^{m_i}\big),\qquad
\mathcal Q_H(z)=\big(\prod_{i=0}^{n-1}m_i\big)z^{M-n}.
\]
All maximal faces in these cycle cases have the displayed common cardinality, while the homology jump between the four-cycle and longer cycles is determined exactly.

## Assumptions and scope

Graphs are finite, simple, undirected and connected, with at least two base vertices. Clique fibers are pairwise disjoint, labeled, and have positive integer sizes at least \(2\). Graph distances and shortest paths are taken in the whole graph. The empty set is a total mutual-visibility set. For a finite abstract simplicial complex consisting only of the empty face, the convention \(\widetilde H_{-1}=\mathbb Z\) is used when formulating augmented homology. The cycle case is labeled modulo \(n\).

## Proof

**Step 1: the metric projection lemma.** Distinct vertices in the same clique fiber are adjacent, as are any two vertices in adjacent fibers. If \(i\ne j\) are nonadjacent base vertices, the distance between any \(x\in V_i\) and \(y\in V_j\) equals \(d_G(i,j)\). A shortest \(x,y\)-path projects to a base shortest \(i,j\)-path; it cannot contain two consecutive vertices from one fiber, since that step could be removed to shorten the path. Conversely, any base shortest path lifts to a path of the same length by freely choosing one vertex from each internal fiber. Such a lifted geodesic avoids \(S\) internally exactly when the chosen base geodesic has each internal fiber containing some vertex outside \(S\). The internal fiber condition is equivalent to its base vertex lying outside \(F(S)\). Since adjacent and same-fiber vertex pairs impose no internal-vertex restriction, the claimed all-set equivalence follows for every pair of graph vertices.

**Step 2: composition and homotopy.** The boundary complex \(\partial\Delta^{m_i-1}\) consists of all proper subsets of \(V_i\). In the simplicial composition with base \(K=\Delta_t(G)\), a union of within-fiber subsets is allowed exactly when the indices whose within-fiber subsets are *nonfaces* of these boundary complexes form a face of \(K\). The only nonface contained in \(V_i\) is \(V_i\) itself, so the index set is exactly \(F(S)\). This proves equality of the complexes, not just a homology coincidence.

Ayzenberg's composition theorem (2013, Proposition 6.1 and Corollary 6.2) gives \(K(K_i)\simeq K*K_1*\cdots*K_h\) for this construction. Each boundary \(K_i\) is \(S^{m_i-2}\), and their join is \(S^{R-1}\). The stated suspension and integral-homology formulas follow from the standard join suspension identity; the empty-realization case is interpreted in augmented simplicial chains. The cited abstract homotopy theorem is prior work, not an independent theorem proved here.

**Step 3: face, facet, and obstruction formulas.** Prescribe the full-fiber index set \(F\). For \(i\in F\), the entire fiber is selected, contributing \(z^{m_i}\). For \(i\notin F\), any proper subset is allowed, contributing \((1+z)^{m_i}-z^{m_i}\). Summing over exactly the feasible \(F\) gives \(\mathcal T_H\).

In a maximal face, each nonfull fiber contains exactly \(m_i-1\) vertices: otherwise a vertex can be added without altering \(F\). The full-fiber index set must be a facet of \(K\), or the last omitted vertex in some other fiber can be added. Conversely, both conditions prevent every addition. There are \(m_i\) choices of the single omitted vertex in each nonfull fiber, yielding \(\mathcal Q_H\).

For any connected graph, total mutual visibility is equivalent to the condition that no common-neighbor set \(N_G(u)\cap N_G(v)\), for a pair at distance \(2\), be fully selected; this follows by replacing internal vertices of a geodesic via an unselected common neighbor, or from the published distance-two characterization. Thus the inclusion-minimal obstructions on the base are exactly the inclusion-minimal such common-neighbor sets. Step 1 lifts a forbidden base index set precisely to the union of its whole fibers, proving the minimal-nonface assertion.

**Step 4: cycles.** In \(C_3\) all vertices are mutually adjacent, so every subset is total mutual-visible and the clique substitution is complete. In \(C_4\), the two opposite vertex pairs have common-neighbor index sets \(\{0,2\}\) and \(\{1,3\}\). Hence the only forbidden full-fiber pairs are opposite pairs, equivalently the selected vertices in the union of each pair of opposite fibers must form a proper subset. Those are exactly the two boundary complexes displayed; the formula and sphere dimension follow by taking their join. For every \(n\ge5\), vertices \(i-1\) and \(i+1\) have unique common neighbor \(i\) for each index \(i\). No nonempty full-fiber set is feasible. Consequently every fiber must be proper, giving the stated join of \(n\) boundaries, the enumerators, and the sphere dimension. The expressions hold for every allowed fiber-size vector, without periodicity assumptions.

## Verification

Run `python3 verify.py` in the directory containing this file and the standalone verifier. The script independently builds each substitution graph and checks total visibility via graph distance-two common neighborhoods for all vertex subsets of \(814\) connected labeled graph-and-fiber profiles, representing \(775472\) subsets in all. It checks the full-fiber equivalence, face polynomial, and inclusion-maximal-set polynomial. An independent BFS geodesic-based implementation checks \(5632\) additional subset instances. Reduced mod-two Betti numbers are also calculated by simplicial boundary matrices for six small cycle substitutions, including \(C_4[K_3]\). The script does not prove the unrestricted integral homotopy theorem, for which the exact composition identification and cited homotopy theorem are the evidence.

## Relationship to prior work

Afkhami, Klavžar, Shahmiri and Tavakoli (2026) give a generalized-lexicographic-product formula for the scalar total \(k\)-clique visibility number when all replacement graphs are **edgeless** (Section 3, Theorem 3.1); their result does not concern clique replacements or identify a total-visibility simplicial composition. Kuziak and Rodríguez-Velázquez (first public preprint June 27, 2023; journal 2023) establish a scalar formula for the maximum total mutual-visibility number of certain lexicographic products. That formula is recovered here, but does not by itself enumerate all feasible sets, characterize all facets and minimal nonfaces, or determine the corresponding simplicial-complex homotopy type. Bujtás, Klavžar and Tian (2025) introduce the total-visibility polynomial and prove an all-graphs distance-two characterization. Their general condition is used explicitly here; the graph-specific full-fiber composition identification is not stated in that work. Ayzenberg (2013) already proves the abstract composition homotopy theorem used in Step 2, including sphere preservation. The novelty claimed here is the identification of total-visibility complexes of *graph clique substitutions* with that abstract construction, and its exact configuration/topology consequences, not the abstract topological theorem or the published scalar product formula.

## Limitations

No claim of publication priority beyond the cited and searched literature is made. The full-fiber characterization can also be derived by applying the previously published general distance-two criterion to graph substitutions; an unindexed treatment could contain this specialization or the complete topological consequences. The family result concerns clique fibers, not arbitrary replacement graphs; its integral homotopy assertion relies on the cited abstract composition result. Exhaustive tests are finite and do not replace the mathematical proof. The explicit cycle calculation is not a classification for other base graphs.

## References

1. D. Kuziak and J. A. Rodríguez-Velázquez, *Total Mutual-Visibility in Graphs with Emphasis on Lexicographic and Cartesian Products*, first public preprint June 27, 2023, arXiv:2306.15818; Bull. Malays. Math. Sci. Soc. **46**, article 197 (2023), DOI:10.1007/s40840-023-01590-3. Section 4 and Theorem 4.4.
2. C. Bujtás, S. Klavžar and J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, Aequationes Math. **99** (2025), 1883–1901, DOI:10.1007/s00010-025-01197-y. Definition 3.1 and Theorem 5.2.
3. M. Afkhami, S. Klavžar, Z. Shahmiri and M. Tavakoli, *Total k-clique mutual-visibility of graphs*, Discuss. Math. Graph Theory **46** (2026), 1151–1169, DOI:10.7151/dmgt.2646, Section 3, Theorem 3.1 (edgeless generalized lexicographic fibers, scalar result).
4. A. Ayzenberg, *Composition of simplicial complexes, polytopes and multigraded Betti numbers*, arXiv:1301.4459 (2013), Proposition 6.1 and Corollary 6.2.

