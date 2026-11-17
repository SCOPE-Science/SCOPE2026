# Critical multipartite simplicial tuplings split into complete bipartite graphs

## Finding
Let \(r\ge2\), let \(A_1,\ldots,A_{2r}\) be disjoint nonempty finite sets with sizes \(a_i\), and let \(X=A_1*\cdots*A_{2r}\), where each \(A_i\) is a zero-dimensional simplicial complex. The Lesh–Schreiner–Wahl simplicial \(r\)-tupling admits an exact graph decomposition
\[
D^r(X)\cong\coprod_{\{I,I^c\},\ |I|=r}K_{p_I,p_{I^c}},\qquad p_I=\prod_{i\in I}a_i,
\]
where the index runs over *unordered* complementary pairs of \(r\)-element subsets of \([2r]\). Consequently it has exactly \(c_r=\frac12\binom{2r}{r}\) connected components, and each component is homotopy equivalent to a wedge of \((p_I-1)(p_{I^c}-1)\) circles, including the case of zero circles. Its reduced integral homology is concentrated in degrees zero and one, with
\[
\widetilde H_0(D^r(X);\mathbb Z)\cong\mathbb Z^{c_r-1},\qquad
H_1(D^r(X);\mathbb Z)\cong\mathbb Z^{c_r(1+\prod_i a_i)-e_r(a_1,\ldots,a_{2r})},
\]
where \(e_r\) is the degree-\(r\) elementary symmetric polynomial. These are torsion-free groups.

The classification is integral and naturally equivariant. Orient the edges of each component from its \(I\)-side to its \(I^c\)-side. If \(U_I=\prod_{i\in I}A_i\) is the set of transversals of those parts and \(L_I=\ker(\mathbb Z[U_I]\xrightarrow{\epsilon}\mathbb Z)\) its augmentation lattice, then
\[
H_1(D^r(X);\mathbb Z)\cong
\bigoplus_{\{I,I^c\}}L_I\otimes_{\mathbb Z}L_{I^c}.
\]
Partwise vertex permutations and permutations of equally sized parts act on these summands by their natural transversal permutations; whenever a permutation exchanges the two sides of a component, it acts by **minus the tensor-factor swap**. This specifies the integral representation for the natural part-permutation symmetry group, not merely its rational character.

For the boundary \(X=\partial C_{2r}\) of the \(2r\)-dimensional cross-polytope, every \(a_i=2\), and hence
\[
D^r(\partial C_{2r})\cong
\coprod^{\frac12\binom{2r}{r}}K_{2^r,2^r},\qquad
H_1\cong\mathbb Z^{\frac12\binom{2r}{r}(2^r-1)^2}.
\]
The tetrahedral-dimensional instance \(r=2\), comprising three copies of \(K_{4,4}\), is an earlier calculation; the all-arity and arbitrarily weighted multipartite classification above is the claimed scope.

## Assumptions and scope
Each discrete complex \(A_i\) has exactly its singletons and the empty simplex as faces. Thus a face of \(X\) contains at most one vertex from each part. In the convention of Lesh, Schreiner and Wahl, vertices of \(D^r(X)\) are the \(r\)-element faces of \(X\), and \(p+1\) of them form a \(p\)-simplex if their union is a face of cardinality \(r(p+1)\). The sets \(A_i\) need not have equal cardinalities; they may also be singletons. The construction is ordinary abstract simplicial tupling, not a quotient or a multicomplex.

The natural symmetries consist of arbitrary permutations within each part, together with permutations among parts having equal sizes and their induced bijections. No classification of possible additional abstract graph automorphisms is claimed.

## Proof
**1. Graph dimension and vertex supports.** A vertex \(\tau\) of \(D^r(X)\) chooses one element from each of exactly \(r\) distinct color parts. Its support \(I(\tau)\) is an \(r\)-element subset of \([2r]\). A collection of three such vertices would use \(3r>2r\) different part indices if it were a face, impossible. Hence \(D^r(X)\) has dimension one. Two distinct vertices \(\tau,\sigma\) are joined by an edge precisely when their union has \(2r\) vertices and at most one comes from each part. This is equivalent to \(I(\sigma)=I(\tau)^c\). There are no edges joining any other two supports.

**2. Exact connected components.** Fix an unordered complementary pair \(\{I,I^c\}\). There are exactly \(p_I\) transversal choices above support \(I\) and \(p_{I^c}\) above support \(I^c\). Every transversal of the first support and every transversal of the complementary support have union a face of \(X\), so every cross-edge is present. There are no edges within one support. Thus their full induced graph is exactly \(K_{p_I,p_{I^c}}\), which is connected because both integers are positive. All edges lie in precisely one such component, and the number of unordered complementary support pairs is \(\binom{2r}{r}/2\). This proves the graph isomorphism without using homology computations.

**3. Homotopy and global ranks.** A connected finite graph with \(p+q\) vertices and \(pq\) edges has fundamental group free of rank \(pq-p-q+1=(p-1)(q-1)\), proved by contracting a spanning tree. Apply this to each component. Summing the ranks over unordered partitions gives
\[
\sum_{\{I,I^c\}}(p_I-1)(p_{I^c}-1)
=c_r\left(1+\prod_{i=1}^{2r}a_i\right)-\sum_{|I|=r}p_I.
\]
The final sum is \(e_r(a_1,\dots,a_{2r})\). There are \(c_r\) components, so reduced zeroth homology has rank \(c_r-1\), while all homology above degree one vanishes. These are integral statements because cellular chains of graphs are free and have no torsion in homology.

**4. Exact integral symmetry module.** For one component choose the orientation from side \(U_I\) to \(U_{I^c}\). Its integral edge-chain group is \(\mathbb Z[U_I]\otimes\mathbb Z[U_{I^c}]\), with boundary \(\partial(u\otimes v)=v-u\). Hence a cycle is an integer matrix with all row sums and all column sums zero. Choose basepoints \(u_0\in U_I\) and \(v_0\in U_{I^c}\). The elementary matrices \((u-u_0)\otimes(v-v_0)\), for nonbasepoint \(u,v\), form a \(\mathbb Z\)-basis for this cycle lattice: each is an oriented four-cycle, and any zero-margin matrix reduces uniquely using its nonbasepoint entries. It follows canonically that \(H_1\cong L_I\otimes L_{I^c}\). Part-preserving symmetries act through the permutation actions on these integral lattices. Exchanging the support sides reverses every edge orientation, contributing a minus sign in addition to exchanging the tensor factors. The component action permutes the direct-sum factors, proving the equivariant statement.

**5. Cross-polytope specialization and the threshold.** The boundary of the \(2r\)-cross-polytope is the join of \(2r\) two-point sets of antipodal vertices, so \(p_I=p_{I^c}=2^r\). The claimed special case follows. This contrasts with the established connectedness of the \(r\)-tupling of a join of \(2r+1\) nonempty discrete parts: adding just one extra part changes the support graph from complementary pairs into the connected odd Kneser graph. The contrast is a statement about the two exact families; no claim of a general connectedness threshold for arbitrary simplicial complexes is made.

## Verification
The included `verify.py` independently enumerates each \(r\)-element face of the multipartite join and constructs the graph's edges by the *union-is-a-face* criterion, rather than by the asserted bipartite-component formula. Breadth-first search finds every connected component; the program then checks all complete bipartite neighborhoods and both independent calculations of integral cycle ranks. Seven cases were checked, including \(r=1\) as a consistency boundary, \(r=2,3,4\), unequal part sizes, and singleton parts. The largest test, eight two-point parts, has 1,120 vertices, 8,960 edges, 35 components, and first Betti number 7,875. All seven checks passed. Finite tests corroborate but do not replace the uniform proof.

## Relationship to prior work
Lesh, Schreiner and Wahl introduced simplicial \(r\)-tupling and proved a weak Cohen–Macaulay connectivity bound. Their Definition 2.1 is used verbatim; their general connectivity theorem does not identify the present component and integral-lattice decomposition. The published result *Full homology characters of multipartite simplicial tuple graphs* treats the adjacent, **odd** number \(2r+1\) of parts and proves connectedness and a rational homology character. It does not cover the even-part hypothesis here; an induced subgraph of a connected graph need not be connected, so its theorem does not imply the present classification. The prior note *The signed-coordinate torsion character of a doubled cross-polytope boundary* explicitly identifies three \(K_{4,4}\) components in the four-dimensional cross-polytope double. That single \(r=2\) example is excluded from the novelty claim, which concerns the uniform even-part law, arbitrary part sizes, and the integral group action. The elementary fact about circle ranks of complete bipartite graphs is used as standard graph topology, not claimed as new.

## Limitations
The theorem concerns exactly \(2r\) complete multipartite color parts and the \(r\)-tupling; no homotopy classification is asserted for other part counts or arbitrary simplicial complexes. Its integral representation description is limited to the stated natural partwise symmetry group. The case \(r=2\) with all two-point parts was known. Unindexed literature or lemmas in other papers may contain equivalent even-part formulations; independent originality certification has not been performed.

## References
1. K. Lesh, B. Schreiner and N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436, initial submission June 12, 2025, Definition 2.1 and Theorem A; https://arxiv.org/html/2506.10436v2 .
2. *Full homology characters of multipartite simplicial tuple graphs*, published October 25, 2026; https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-full-homology-characters-of-multipartite-simplicial-tuple-graphs--af3240d20086/RESULT.md .
3. *The signed-coordinate torsion character of a doubled cross-polytope boundary*, published November 8, 2026; https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-signed-coordinate-torsion-character-of-a-doubled-cross-polyt--5ef24ff5245a/RESULT.md .
