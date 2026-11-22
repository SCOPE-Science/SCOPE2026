# An integral coordinate-equivariant splitting at a puncture of the scale-two hypercube Rips complex

## Finding

For each integer \(n\ge3\), consider the scale-two Vietoris–Rips complex \(K_n=\operatorname{VR}_{\le2}(Q_n)\) of the binary Hamming cube and its full subcomplex \(D_n=K_n\setminus\{0^n\}\). Coordinate permutations fixing the zero vertex act through \(S_n\). The **new statement** is a specified, integral, symmetry-equivariant split exact sequence

\[
0\longrightarrow\widetilde H_3(D_n;\mathbb Z)
\overset{\iota_*}{\longrightarrow}\widetilde H_3(K_n;\mathbb Z)
\overset{\partial_0}{\longrightarrow}\bigwedge^3\mathbb Z^n
\longrightarrow0.
\]

For every ordered triple \(i<j<k\), a right inverse to \(\partial_0\) takes \(e_i\wedge e_j\wedge e_k\) to the **integral fundamental cycle** of the eight-vertex coordinate three-cube through zero, viewed as the four-dimensional crosspolytope boundary inside \(K_n\). This section commutes with every coordinate permutation. Thus the coordinate-cube homology classes form a primitive integral \(S_n\)-submodule, not merely a rational representation or independent set.

If a permutation has \(f\) fixed coordinates, \(c_2\) two-cycles, and \(c_3\) three-cycles, the lost module has integral character
\[\operatorname{tr}(\sigma\mid\bigwedge^3\mathbb Z^n)=\binom{f}{3}-f c_2+c_3.\]
Its invariant rational subspace is zero, so puncturing does **not** change third rational homology after quotienting by the whole coordinate-permutation group:
\[H_3(|D_n|/S_n;\mathbb Q)\cong H_3(|K_n|/S_n;\mathbb Q).\]

## Assumptions and scope

The vertex set of \(Q_n\) is \(\{0,1\}^n\); its metric is the original Hamming distance \(d_H\). A set is a face iff every two of its vertices have Hamming distance at most two. Removing \(0^n\) means taking the induced simplicial subcomplex **without recomputing graph distances**. Homology has integral coefficients unless explicitly specified. The \(S_n\)-action only permutes the \(n\) coordinates and fixes \(0^n\). For \(n=3\) the kernel vanishes, a genuine boundary case included in the theorem.

## Proof

**1. An integral basis for the vertex link.** Let \(L_n=\operatorname{lk}_{K_n}(0^n)\). Its vertices are the weight-one words \(a_i\) and the weight-two words \(b_{ij}\). Adjacency is determined exactly by \(a_i\sim a_j\) for distinct indices, \(a_i\sim b_{jk}\) iff \(i\in\{j,k\}\), and \(b_{ij}\sim b_{kl}\) iff the pairs intersect. These rules identify all maximal faces as faces of: the simplex \(A=\langle a_1,\ldots,a_n\rangle\); each star simplex \(B_i=\langle a_i,b_{ij}:j\ne i\rangle\); each bridge triangle \(T_{ij}=\langle a_i,a_j,b_{ij}\rangle\); and each triple triangle \(U_{ijk}=\langle b_{ij},b_{ik},b_{jk}\rangle\).

The subcomplex \(S=A\cup\bigcup_{i<j}T_{ij}\cup\bigcup_i B_i\) is contractible. Indeed attach all \(T_{ij}\) to \(A\) first: each attaches a triangular disk along its base edge and brings a new apex \(b_{ij}\), preserving homotopy type. Then attach the \(B_i\) in any order: each intersects the union already constructed in the tree consisting of the edges \(a_i b_{ij}\) for \(j\ne i\) and their endpoints (any earlier \(B_j\) contributes only the already present shared vertex \(b_{ij}\)). Attaching a simplex along this nonempty contractible subcomplex preserves contractibility. Each \(U_{ijk}\) now attaches a triangular disk along a loop in \(S\), with a new interior two-cell, and distinct \(U_{ijk}\) have no common interior two-simplex. Thus
\[L_n\simeq\bigvee^{\binom n3}S^2,\qquad H_2(L_n;\mathbb Z)\cong\mathbb Z^{\binom n3},\]
with the coefficients on the \(U_{ijk}\) giving integral coordinates. In particular the oriented octahedral link sphere \(\ell_{ijk}\) supported on words using only coordinates \(i,j,k\) has coefficient \(\pm1\) on its own \(U_{ijk}\) and zero on the other distinguished triangles. The signs are fixed coherently by ordering \(i<j<k\). Therefore \(\{\ell_{ijk}\}\) is an integral basis. Under coordinate relabeling it transforms by the sign of the induced permutation on a triple, identifying \(H_2(L_n;\mathbb Z)\) with \(\bigwedge^3\mathbb Z^n\) as integral \(S_n\)-modules.

**2. Explicit equivariant section of the relative boundary.** The induced Rips complex on each coordinate three-cube \(Q_{\{i,j,k\}}\) is the boundary of the four-dimensional crosspolytope, because its eight vertices split into four antipodal pairs at distance three and all other distinct pairs have distance at most two. Let \(z_{ijk}\in Z_3(K_n;\mathbb Z)\) be its fundamental oriented three-cycle: order the antipodal pairs as \((0^n,a_i+a_j+a_k)\), then the three pairs \((a_i,a_j+a_k)\), \((a_j,a_i+a_k)\), \((a_k,a_i+a_j)\), and take the alternating sum of their sixteen oriented facets. Its simplicial boundary is exactly zero.

The relative chain complex for \((K_n,D_n)\) is the reduced cone chain complex on \(L_n\), shifted by one. The connecting homomorphism \(\partial_0:H_3(K_n;\mathbb Z)\to H_2(L_n;\mathbb Z)\) takes \([z_{ijk}]\) to \([\ell_{ijk}]\): delete the vertex zero in the eight oriented tetrahedra containing it. The coefficient on \(U_{ijk}\) is a unit, and no other \(z_{abc}\) has a coefficient on this triangle. Therefore the homomorphism
\[s:\bigwedge^3\mathbb Z^n\longrightarrow H_3(K_n;\mathbb Z),\qquad e_i\wedge e_j\wedge e_k\longmapsto[z_{ijk}]\]
is a right inverse of \(\partial_0\). A coordinate permutation carries ordered antipodal pairs to the corresponding pairs with sign equal to the permutation's restriction to the three chosen coordinates. Hence \(s\) is \(S_n\)-equivariant **over \(\mathbb Z\)**.

**3. Exactness and topology of the puncture.** The previously established scale-two cube theorem gives \(K_n\simeq\bigvee^{c_n}S^3\), where
\[c_n=\sum_{0\le j<i<n}(j+1)(2^{n-2}-2^{i-1}).\]
The pair sequence and the link classification show that \(H_4(K_n,D_n)\cong\widetilde H_3(L_n)=0\), so \(H_3(D_n)\to H_3(K_n)\) is injective. The explicit section above makes the map to \(H_3(K_n,D_n)\cong H_2(L_n)\) split-surjective, proving the claimed integral \(\mathbb Z[S_n]\)-module direct sum.

For context, \(\pi_1(D_n)=0\) because \(K_n=D_n\cup\operatorname{cone}(L_n)\), the link is simply connected, and \(K_n\) is simply connected. The long exact sequence also gives \(\widetilde H_2(D_n)=0\); all reduced homology outside degree three vanishes. Hurewicz and the homology version of Whitehead's theorem consequently recover the already known nonequivariant type \(D_n\simeq\bigvee^{c_n-\binom n3}S^3\). This type is included to specify ranks and is **not** asserted as new.

**4. Symmetry of the removed lattice.** The character of an exterior power of the coordinate-permutation module is obtained from
\[\det(I+t\sigma)=\prod_{C\text{ cycle of }\sigma}(1-(-t)^{|C|}).\]
Its coefficient in degree three is \(\binom f3-fc_2+c_3\). The stabilizer of a chosen unordered triple contains a transposition of two elements of that triple which negates its exterior basis vector; therefore the invariant subspace of \(\bigwedge^3\mathbb Q^n\) is zero. Rational homology of a finite-group quotient is the fixed subspace of rational homology, proving the quotient consequence.

## Verification

The standalone standard-library script `verify_puncture.py` enumerates every face of \(K_n\), \(D_n\), and \(L_n\) for \(3\le n\le6\), checks the three predicted Euler characteristics, constructs all sixteen-tetrahedron coordinate-cube fundamental cycles, tests their integer boundaries and relative link cycles, verifies that every distinguished triangle has coefficient \(\pm1\) for exactly one cube, and checks the signed \(S_n\)-equivariance under all adjacent transpositions. The extracted script was executed and its complete output is supplied in `EXPECTED.txt`. The proof for arbitrary \(n\) is the preceding combinatorial chain argument, not an extrapolation from these finite tests.

## Relationship to prior work

Adamaszek–Adams (2021/2022), Theorem 8, **already determines** the homotopy types of all initial binary-segment scale-two Rips complexes, including the one-point puncture by complementing all bits; their Theorem 1 gives \(c_n\). Adams–Virk (2024), Theorem 4.1, **already constructs independent crosspolytopal cube homology classes** (more than the origin-containing family used here). A later published study also establishes the two-sphere-wedge type of the once-subdivided complete-graph Rips complex, equivalent to the vertex-link description. These results are not being reintroduced as novel. The present claim is the inclusion-induced **integral, \(S_n\)-equivariant relative sequence with its explicit unit section and invariant-quotient consequence**. Bendersky–Elia–Grbić (first posted May 1, 2026) studies crosspolytopal cohomology representatives and independent classes using the Tor algebra and ghost vertices, not this relative integral equivariant map in inspected sections. Galetto–Montaño–Wellner (first posted June 18, 2026) describes characteristic-zero representations of the unpunctured complexes; its accessible abstract does not decide the integral puncture sequence, and its complete text could not be inspected.

## Limitations

Only inclusive Hamming scale two, a **single removed vertex**, the stabilizer's coordinate permutations, and the degree-three integral homology map are classified. The theorem does not give an irreducible decomposition of the kernel or claim an equivariant homotopy wedge. Full-source priority uncertainty remains for the inaccessible representation paper; an independently indexed equivalent integral-relative theorem cannot be ruled out. Independent mathematical validation has not occurred.

## References

1. Michał Adamaszek and Henry Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first posted 2021), Theorems 1 and 8. https://arxiv.org/abs/2103.01040
2. Henry Adams and Žiga Virk, *Lower Bounds on the Homology of Vietoris–Rips Complexes of Hypercube Graphs*, 2024, Theorem 4.1, DOI 10.1007/s40840-024-01663-x. https://link.springer.com/article/10.1007/s40840-024-01663-x
3. Martin Bendersky, Salvatore Elia and Jelena Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705, first posted May 1, 2026. https://arxiv.org/abs/2605.00705
4. Federico Galetto, Jonathan Montaño and Zoe Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, first posted June 18, 2026. https://arxiv.org/abs/2606.20784
5. *The Rips filtration of the complete-graph subdivision has two consecutive sphere wedges*, publicly indexed October 11, 2026; source summary consulted, full text inaccessible. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-rips-filtration-of-the-complete-graph-subdivision-has-two-co--fb5f0359b702
