# Two-torsion hidden in the integral symmetry coinvariants of cross-polytope simplicial tuplings

## Finding
Let \(r\ge2\), and let \(X_r=\partial C_{2r}=A_1*\cdots*A_{2r}\), where each \(A_i\) is a two-point discrete simplicial complex. Let \(Y_r=D_r(X_r)\) be its simplicial \(r\)-tupling, with vertices the \(r\)-element faces of \(X_r\) and faces the families of pairwise disjoint such faces whose union is a face of \(X_r\). Define \(k_r=\frac12\binom{2r}{r}\), \(T_r=(C_2)^{2r}\), and the full signed-coordinate group \(B_{2r}=T_r\rtimes S_{2r}\).

Then there is a simplicial decomposition, and the following **integral equivariant coinvariant calculation**:
\[
Y_r\cong\bigsqcup^{k_r}K_{2^r,2^r},\qquad
\widetilde H_0(Y_r;\mathbb Z)\cong\mathbb Z^{k_r-1},\qquad H_1(Y_r;\mathbb Z)\cong\mathbb Z^{k_r(2^r-1)^2},
\]
\[
\boxed{H_1(Y_r;\mathbb Z)_{T_r}\cong (\mathbb Z/2)^{k_r r^2},\qquad H_1(Y_r;\mathbb Z)_{B_{2r}}\cong\mathbb Z/2.}
\]
The entire first homology is free before taking coinvariants; the order-two class survives **all** signed-coordinate symmetries for every \(r\ge2\). Nevertheless, \(|Y_r|/T_r\) is a disjoint union of \(k_r\) intervals and \(|Y_r|/B_{2r}\) is one interval, so the torsion in homology coinvariants is not torsion in the geometric orbit space.

A more general, structurally useful statement holds when the \(2r\) vertex classes are arbitrary nonempty finite sets \(A_i\). Put \(P_I=\prod_{i\in I}A_i\) and \(L(P)=\ker(\mathbb Z[P]\xrightarrow{\varepsilon}\mathbb Z)\). There is a canonical graph decomposition
\[
D_r(A_1*\cdots*A_{2r})\cong\bigsqcup_{\{I,I^c\},\ |I|=r}K_{|P_I|,|P_{I^c}|},
\]
and, with an orientation chosen for each pair of shores, an integral first-homology lattice decomposition
\[
H_1\cong\bigoplus_{\{I,I^c\}} L(P_I)\otimes_{\mathbb Z}L(P_{I^c}).
\]
This identifies the within-class permutation action integrally, and a color permutation exchanging the two shores acts by **minus** the exchange of tensor factors.

## Assumptions and scope
The join contains exactly those vertex sets using at most one vertex from each of the \(2r\) color classes. Each \(A_i\) is finite and nonempty for the general decomposition. For the coinvariant formulas, every \(A_i\) consists of exactly two elements. The group \(T_r\) flips each pair independently; the group \(S_{2r}\) permutes entire pairs, so that \(B_{2r}\) acts simplicially on \(Y_r\). Homology is ordinary degree-one integral homology, and \(M_G=M/\langle gm-m:g\in G,m\in M\rangle\) denotes **integral coinvariants**. This is not the homology of a topological quotient, and no integral equivariant homotopy splitting is claimed.

## Proof
**1. Exhaustive description of faces and components.** Each vertex of \(Y=D_r(A_1*\cdots*A_{2r})\) chooses an \(r\)-subset \(I\subset[2r]\) of color classes and an assignment of an element of \(A_i\) for each \(i\in I\). It is thus a member of \(P_I\). Two vertices form an edge exactly when their supports are disjoint. Because both supports have cardinality \(r\), disjointness is equivalent to being complementary in the \(2r\) available colors. Their assignments are then unrestricted and produce precisely \(K_{|P_I|,|P_{I^c}|}\). Three pairwise disjoint supports would use \(3r>2r\) colors, so there are no two-simplices. Each unordered complementary support pair gives one component and no two different pairs connect. There are \(k_r\) components.

**2. Integral cycles and orientations.** For a complete bipartite component with shores \(P,Q\), orient each edge from \(P\) to \(Q\). Then the integral edge-chain group is \(\mathbb Z[P]\otimes\mathbb Z[Q]\), and its boundary sends \([p]\otimes[q]\) to \([q]-[p]\). The kernel is exactly \(L(P)\otimes L(Q)\): it consists of integer matrices with every row and column sum zero. A basis is formed by the four-term cycles
\[
([p]-[p_0])\otimes([q]-[q_0]),\qquad p\ne p_0,\quad q\ne q_0.
\]
Hence the free rank is \((|P|-1)(|Q|-1)\). Summing over components proves the general integral module formula, the rank formula at \(|A_i|=2\), and \(\widetilde H_0\cong\mathbb Z^{k_r-1}\). Permutations of the chosen color values act on the two lattice factors. Exchanging shore order reverses the orientation of every edge, hence acts as the **negative** of tensor-factor transposition; this is an actual integral sign, not just a rational character convention.

**3. Independent-flip coinvariants.** For the cross-polytope, within each support pair the two assignment sets are the groups \(T_I=(C_2)^r\) and \(T_{I^c}=(C_2)^r\), acting regularly on themselves by independent bit translations. Their augmentation lattices are the augmentation ideals \(J_I\subset\mathbb Z[T_I]\) and \(J_{I^c}\subset\mathbb Z[T_{I^c}]\). For any group \(G\), \((J_G)_G=J_G/J_G^2\cong G_{\mathrm{ab}}\), with the isomorphism induced by \(g\mapsto g-1\); indeed \((gh-1)\equiv(g-1)+(h-1)\pmod{J_G^2}\), and these are its complete relations. Coinvariants under the product of the two independently acting subgroups commute with tensor products over \(\mathbb Z\), giving
\[
(J_I\otimes J_{I^c})_{T_I\times T_{I^c}}
\cong (J_I)_{T_I}\otimes(J_{I^c})_{T_{I^c}}
\cong (\mathbb Z/2)^r\otimes(\mathbb Z/2)^r
\cong(\mathbb Z/2)^{r^2}.
\]
The full group \(T_r\) fixes each complementary support pair and restricts on that pair to the indicated product of translations. Taking direct sums over all \(k_r\) components yields the first boxed formula.

**4. All signed-coordinate symmetries.** Passing from \(T_r\) coinvariants to \(B_{2r}\) coinvariants amounts to taking \(S_{2r}\) coinvariants of the elementary-two-group computed in Step 3. The basis elements can be indexed by a complementary support pair together with one coordinate in each of its two shores; changing shore order contributes the sign from Step 2, which is immaterial modulo two. The symmetric group is transitive on this set of cross-shore coordinate pairs: first send one partition to another, then send the two distinguished colors to the target colors, swapping sides if necessary. Therefore the remaining module is the coinvariant module of a **single transitive permutation action on a nonempty set over** \(\mathbb F_2\), namely \(\mathbb F_2\), viewed integrally as \(\mathbb Z/2\). This proves the second boxed formula without a rational-semisimplicity assumption.

**5. Geometric orbit-space contrast.** The independent translations act transitively on each shore of every component, so the geometric quotient of each bipartite component by \(T_r\) is an interval. The symmetric color permutations act transitively on complementary support partitions and include permutations that exchange the shores, hence the full quotient is the quotient of one interval by endpoint exchange, again an interval. Both geometric quotient spaces have zero first integral homology despite the nonzero integral homology coinvariants established above.

## Verification
The accompanying standalone `verify.py` independently constructs every vertex and edge of \(Y_r\) from disjoint color supports, enumerates connected components, checks the four-cycle basis and first Betti ranks for \(r=2\) and \(r=3\), and performs **exact integer Smith normal form** on the coordinate-flip relations in the integral cycle basis. At \(r=2\), it also constructs the complete \(27\)-dimensional integral action of all four flips and adjacent coordinate transpositions and computes the Smith form of the full coinvariant presentation. Observed results:
\[
(r,k_r,f_0,f_1,b_1,\dim_{\mathbb F_2} H_1{}_{T_r})=(2,3,24,48,27,12),(3,10,160,640,490,90).
\]
For \(r=2\), the full signed-coordinate coinvariant presentation has \(26\) unit Smith factors and one factor \(2\); the resulting quotient is exactly \(\mathbb Z/2\). Run `python3 verify.py` in an environment with SymPy installed, compare stdout byte-for-byte with `verification_output.txt`, and inspect the direct construction and exact arithmetic. These finite instances corroborate, but do not replace, the all-parameter proof in Steps 1--5.

## Relationship to prior work
Lesh, Schreiner and Wahl introduced simplicial \(r\)-tuplings in *The double of a simplicial complex*, arXiv:2506.10436 (first public June 12, 2025). Their full paper gives general definitions and connectivity bounds, but no statement of these integral signed-coordinate coinvariants. The October 2026 published calculation *Full homology characters of multipartite simplicial tuple graphs* treats **\(2r+1\)** color classes, for which the tuple graph is connected, and computes rational characters; it does not include the \(2r\)-class disconnected threshold or its integral coinvariants. The November 2026 *Integral top-homology lattice of doubled six-partite joins* computes \(H_2\) for a six-color **double** \(D_2\), which is two-dimensional; the present family has \(2r\) colors and uses \(D_r\), producing a graph. The November 2026 *Partition inflation and a composition law for iterated simplicial doubles* treats iterated operations, not the single critical-color tuple's integral coinvariants. Classical vertex-inflation wedge formulas (Björner--Wachs--Welker, 2005), generalized by Ayzenberg and Khoroshavkina (2026), cover the ordinary homotopy information in principle; that part is not presented as novel. The group-ring identity \(J_G/J_G^2\cong G_{\rm ab}\) is standard, and the contribution is the exact **family-specific integral equivariant** calculation, including the persistence of one torsion coinvariant under all signed-coordinate symmetries and the contrast with the contractible orbit space. No claim of global literature uniqueness is made.

## Limitations
These statements concern \(r\ge2\), a join of exactly \(2r\) color classes, the indicated full signed-coordinate group, and ordinary first homology. They do not determine integral homology of arbitrary tuplings, equivariant stable homotopy types, higher-degree classes, or homology of orbit spaces beyond the explicitly described interval quotient. The original homology is torsion-free: **the order-two groups occur only after taking integral coinvariants**. Finite computations do not establish the infinite result, which follows instead from the exact graph and augmentation-ideal arguments. The literature comparison is extensive but cannot exclude unindexed equivalents; independent mathematical audit remains outstanding.

## References
1. Kathryn Lesh, Bridget Schreiner and Nathalie Wahl, *The double of a simplicial complex*, arXiv:2506.10436v1 (2025-06-12). https://arxiv.org/abs/2506.10436.
2. Anton Ayzenberg and Nadya Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694v1 (2026-02-09). https://arxiv.org/html/2602.08694v1.
3. *Full homology characters of multipartite simplicial tuple graphs* (2026-10-25). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-full-homology-characters-of-multipartite-simplicial-tuple-graphs--af3240d20086.
4. *Integral top-homology lattice of doubled six-partite joins* (2026-11-08). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-integral-top-homology-lattice-of-doubled-six-partite-joins--4f512ff206de.
5. *Partition inflation and a composition law for iterated simplicial doubles* (2026-11-08). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-partition-inflation-and-a-composition-law-for-iterated-simplicia--c33689e940ec.
6. Anders Björner, Michelle Wachs and Volkmar Welker, *Poset fiber theorems*, Trans. Amer. Math. Soc. 357 (2005), Theorem 6.2 and Corollary 8.5. https://doi.org/10.1090/S0002-9947-04-03496-8.
7. Romyar Sharifi, *Homological Algebra*, Chapter 3, on coinvariants and augmentation ideals. https://www.math.ucla.edu/~sharifi/notes/homalg-ch03.html.
