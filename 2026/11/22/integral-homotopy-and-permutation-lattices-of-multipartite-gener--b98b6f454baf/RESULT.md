# Integral homotopy and permutation lattices of multipartite general-position complexes

## Finding
Let \(t\geq2\), let \(a_1,\ldots,a_t\geq1\) be integers, and let \(G=K_{a_1,\ldots,a_t}\) be the connected complete multipartite graph with labelled, pairwise disjoint parts \(V_i\) of sizes \(a_i\). Write \(\mathcal{GP}(G)\) for the simplicial complex of all ordinary geodesic general-position sets of \(G\): no shortest path contains three selected vertices. Let \(I_i=\ker(\mathbb Z[V_i]\xrightarrow{\sum}\mathbb Z)\), the integral augmentation lattice of the permutation module on the vertices of part \(V_i\).

**Theorem.** If \(t=2\), then
\[
|\mathcal{GP}(G)|\simeq\bigvee^{a_1a_2-1}S^1,
\qquad
\widetilde H_1(\mathcal{GP}(G);\mathbb Z)\cong
\ker\bigl(\mathbb Z[V_1\times V_2]\xrightarrow{\sum}\mathbb Z\bigr).
\]
The homology identification is canonical for automorphisms preserving both parts. If the two parts have the same size, interchanging them negates the oriented cross-edge permutation after exchanging coordinates.

If \(t\geq3\), then
\[
|\mathcal{GP}(G)|\simeq
\bigvee^{\sum_{i=1}^{t}(a_i-1)}S^1
\ \vee\ 
\bigvee^{\prod_{i=1}^{t}(a_i-1)}S^{t-1}.
\]
Its only possibly nonzero reduced integral homology groups are, canonically under all part-preserving vertex permutations,
\[
\widetilde H_1\cong\bigoplus_{i=1}^{t}I_i,
\qquad
\widetilde H_{t-1}\cong\bigotimes_{i=1}^{t}I_i.
\]
Permuting equal-size parts permutes the summands in degree one; in degree \(t-1\), it permutes tensor factors with the sign of that part permutation. In particular all reduced integral homology is free, and the fundamental group is free of rank \(\sum_i(a_i-1)\) if \(t\ge3\), or rank \(a_1a_2-1\) if \(t=2\). A wedge with zero summands means a point.

**Purity and shellability consequence.** For any \(t\ge2\), the complex is pure exactly when each part of size at least two has size \(t\). When \(t\ge3\) and at least one part has size \(t\), such a pure complex is not shellable in the classical pure sense. In particular, the general-position complex of the balanced graph with \(t\) parts each of size \(t\) is a pure, non-shellable \((t-1)\)-dimensional simplicial complex for every \(t\ge3\).

## Assumptions and scope
All graphs are finite, undirected, loopless, and simple. The parameter \(t\) is the number of nonempty independent partite classes, not the order. The theorem allows singleton classes. Homotopy is the ordinary, *nonequivariant* homotopy type of the geometric realization; the displayed integral homology isomorphisms separately identify the actual automorphism actions. This does not assert an equivariant homotopy equivalence of wedge spaces.

For a selected set \(S\), being in general position means there do not exist three distinct vertices \(u,v,w\in S\) with \(d(u,w)=d(u,v)+d(v,w)\). For a finite set \(V\), \(\mathbb Z[V]\) denotes its free abelian group on the vertices. The full automorphism group of the graph permutes vertices within the independent parts and permutes parts of equal sizes.

## Proof
**1. Exact simplicial decomposition.** Distinct vertices in the same part have distance two, while vertices in different parts are adjacent. Thus if a selected set contains two vertices of one part and a vertex of a different part, the latter lies on a geodesic between the former two. Conversely, every subset contained in one part is in general position, and so is every subset containing at most one vertex per part. This elementary characterization, including its counting consequences, is already known; see Rather (2026), Theorem 3.1, and the earlier general characterization of Anand et al. (2018).

Let \(D_i\) be the zero-dimensional simplicial complex whose vertices are \(V_i\) and let \(B_i=\Delta(V_i)\) be the full simplex on \(V_i\). The general-position complex is exactly
\[
X=A\cup B_1\cup\cdots\cup B_t,
\qquad A=D_1*\cdots*D_t,
\]
where \(A\cap B_i=D_i\), and different \(B_i\) have disjoint geometric realizations. This equality holds face-by-face, including singleton parts.

**2. Attachment lemma and wedge decomposition.** If \(Y\) is a path-connected CW complex and a contractible CW complex \(B\) is glued to \(Y\) along an \(s\)-point discrete subcomplex \(D\) (with both inclusions cofibrations), then
\[
Y\cup_D B\simeq Y\vee\bigvee^{s-1}S^1.
\]
Indeed, the pushout is a homotopy pushout. Replace \(B\) by a point in the homotopy pushout, thereby attaching a cone on \(D\) to \(Y\). Choose arcs in \(Y\) from the images of the \(s\) points to one fixed basepoint; the cone adds \(s-1\) free loops, with no higher attaching maps. The same argument applies successively to the disjoint \(B_i\), since all their intersections with the accumulated complex remain precisely \(D_i\). Since \(t\ge2\), the join \(A\) is path connected. Consequently
\[
X\simeq A\vee\bigvee^{\sum_i(a_i-1)}S^1.
\]
Each discrete \(D_i\), with a chosen vertex as basepoint, is a wedge of \(a_i-1\) copies of \(S^0\). The standard join/suspension identity yields
\[
A=D_1*\cdots*D_t\simeq\bigvee^{\prod_i(a_i-1)}S^{t-1}.
\]
This also covers singleton parts, for which \(A\) is contractible. If \(t=2\), both wedge dimensions are one and the total rank is \((a_1-1)(a_2-1)+(a_1-1)+(a_2-1)=a_1a_2-1\). If \(t\ge3\), they are distinct. The wedge descriptions prove the asserted free fundamental groups and torsion-free integral homology.

**3. Canonical integral symmetry modules for \(t\ge3\).** Let \(P_i=\mathbb Z[V_i]\) and \(I_i=\ker(P_i\to\mathbb Z)\). The join chain-complex identity gives the *canonical* isomorphism
\[
\widetilde H_{t-1}(A;\mathbb Z)\cong I_1\otimes\cdots\otimes I_t.
\]
For example, the tensor of \(v_i-w_i\in I_i\) corresponds to the oriented fundamental \((t-1)\)-cycle of the join of the two-point subsets \(\{v_i,w_i\}\). A transposition of two joined factors incurs the Koszul sign \((-1)^{(0+1)(0+1)}=-1\). Since attaching \(B_i\) along zero-dimensional subcomplexes changes relative homology only in degree one, inclusion \(A\hookrightarrow X\) induces an isomorphism in homology degrees at least two.

For degree one, the relative sequence for \((X,A)\), obtained by excising the disjoint simplex interiors, gives
\[
H_1(X,A;\mathbb Z)\cong\bigoplus_i H_1(B_i,D_i;\mathbb Z)
\cong\bigoplus_i\widetilde H_0(D_i;\mathbb Z)
\cong\bigoplus_i I_i.
\]
Because \(A\) is simply connected for \(t\ge3\) (it is a join of at least three nonempty discrete spaces), \(H_1(A)=0\); because \(A\) and \(X\) are connected, the long exact sequence gives \(H_1(X)\cong H_1(X,A)\). Every map is natural under automorphisms. This proves both integral module identifications, including the part-swap sign in top degree.

**4. The two-part integral module.** For \(t=2\), collapse each full simplex \(B_i\) to a distinct point. Contracting these disjoint contractible subcomplexes, one at a time, is a homotopy equivalence. The quotient is the two-vertex multigraph with one edge for each ordered pair in \(V_1\times V_2\), oriented from the first vertex class to the second. Its cellular boundary sends every oriented edge to the same difference of endpoints. Its cycle lattice is therefore exactly \(\ker(\mathbb Z[V_1\times V_2]\xrightarrow{\sum}\mathbb Z)\). Automorphisms preserving parts permute its basis cross-edges. A shore swap reverses every orientation and thus acts with a minus sign after exchanging the labels. This is an integral statement, not merely a rational character count.

**5. Pure but non-shellable cases.** The maximal faces are all \(t\)-vertex transversals (one from each part) and, for every \(a_i\ge2\), the complete part \(V_i\). All these sets are unextendible, and no other maximal faces exist by step 1. Therefore all facets have the same size precisely when \(a_i=t\) for every \(a_i\ge2\). If \(t\ge3\) and at least one such part exists, the complex has positive first Betti rank \(\sum_i(a_i-1)\) while being a pure complex of dimension \(t-1\ge2\). A pure shellable complex has reduced homology only in its top dimension. Thus these pure complexes cannot be shellable.

## Verification
The standalone standard-library program `verify.py` independently constructs all graph subsets for every part-size vector of length 2, 3, or 4 with entries 1, 2, or 3 and total size at most 10. It compares the distance-based general-position definition to the claimed face decomposition; constructs signed simplicial boundary matrices; computes ranks modulo 2 and 101; and compares all reduced Betti numbers to the predicted formulas. It also checks the sign of a part interchange and of a within-part transposition on a fundamental two-cycle for the three-part two-vertex-per-part example. Executed on the exact embedded source, it prints `VERIFY_OK cases= 112 faces_checked= 6984 primes=2,101 orientation=PASS`.

These finite-field tests are finite consistency checks, not proofs of torsion-freeness or of the all-order homotopy statement. Both follow from the attachment argument and the canonical integer chain-complex proof above.

## Relationship to prior work
The 2024 first-public general-position-polynomial study of Iršič, Klavžar, Rus and Tuite, arXiv:2401.05696, establishes the counting-polynomial context and treats many graph classes, including complete bipartite graphs. Anand et al., arXiv:1812.08460 (first public 2018), established a general characterization of ordinary general-position sets. Rather, arXiv:2603.06930 (first public March 2026), explicitly proves the **complete multipartite face characterization and entire polynomial**. Neither the face characterization nor the polynomial is claimed as new here. The present claim concerns the resulting entire integral homotopy type, the full integer automorphism modules in two different homological degrees, and the pure non-shellable cases.

Indexed related records about multipartite *total mutual visibility*, *four-path-free* complexes, and *geodesic-avoidance* complexes of different graph families concern different face predicates. No inspected accessible text or indexed result supplied the above full general-position-complex homotopy and integral symmetry theorem. Priority remains provisional, especially with respect to unindexed topological treatments and potential equivalent formulations via union-of-simplices constructions.

## Limitations
The result concerns ordinary graph-geodesic general-position sets, not mutual visibility, monophonic position, total visibility, or general position under an altered shortest-path rule. The wedge statement is nonequivariant; the homology modules carry actual automorphism actions, but no equivariant wedge decomposition is asserted. The polynomial and underlying face description are explicitly prior art. Neither independent validation nor an exhaustive publication-priority determination has been performed.

## References
1. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first posted 2024-01-11); *Results in Mathematics* 79, article 110 (2024). https://arxiv.org/abs/2401.05696 ; https://doi.org/10.1007/s00025-024-02133-3
2. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930 (first posted 2026-03-06), especially Theorems 3.1 and 3.4. https://arxiv.org/abs/2603.06930
3. B. S. Anand, U. S. V. Chandran, M. Changat, S. Klavžar and E. J. Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460 (first posted 2018-12-20), especially Theorem 3.1. https://arxiv.org/abs/1812.08460
