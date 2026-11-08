# Length-profile invariance and integral symmetry in higher independence complexes of spider trees

## Finding

For an integer \(k\geq3\), take a spider tree \(T=T(\ell_1,\ldots,\ell_k)\) with a central vertex \(v\) and \(k\) internally disjoint paths of lengths \(\ell_i\geq2\) from \(v\). Assume at least one arm has length at least three. Put
\[
B=\sum_{i=1}^k(\ell_i-1),\qquad L=\max_i\ell_i.
\]
For every integer \(r\geq L\), let \(\operatorname{Ind}_r(T)\) be the simplicial complex of vertex sets all of whose induced connected components contain at most \(r\) vertices. Then
\[
\boxed{\operatorname{Ind}_r(T)\simeq
\begin{cases}
\mathrm{point},&L\leq r\leq B,\\
\displaystyle\bigvee^{\binom{k-1}{r-B-1}}S^{r-1},&B+1\leq r\leq B+k,\\
\mathrm{point},&r\geq B+k+1.
\end{cases}}
\]
The equivalences are ordinary integral homotopy equivalences. In particular, in this range the homotopy type depends on the profile \((\ell_1,\ldots,\ell_k)\) only through \(k\) and \(B\); the individual arm lengths do not matter.

Let \(\Gamma=\prod_{d\geq2}S_{m_d}\) permute the \(m_d\) arms of length \(d\). Let \(P=\mathbb Z^k\) be the arm permutation lattice, \(W=\ker(P\xrightarrow{\mathrm{sum}}\mathbb Z)\), and \(\varepsilon_B=\det(\mathbb Z[U])\), the rank-one sign lattice for the induced permutation of the \(B\) noncentral, nonterminal arm vertices \(U\). For \(B+1\leq r\leq B+k\), with \(t=r-B-1\), the complete nonzero reduced integral homology module is
\[
\boxed{\widetilde H_{r-1}(\operatorname{Ind}_r(T);\mathbb Z)
\cong_{\mathbb Z[\Gamma]}\varepsilon_B\otimes\bigwedge^t W.}
\]
All other reduced integral homology groups vanish. Explicitly, if \(\sigma_d\in S_{m_d}\), then \(\varepsilon_B(\sigma)=\prod_{d\geq2}\operatorname{sgn}(\sigma_d)^{d-1}\). These are homology-module isomorphisms; no equivariant homotopy splitting is asserted.

## Assumptions and scope

The arms are vertex-disjoint except at the hub; arm \(i\) has ordered vertices \(a_{i,1},\ldots,a_{i,\ell_i}\) from hub to leaf. The definition of an induced connected component uses the underlying simple graph and counts vertices, not edges. We require \(k\geq3\), every \(\ell_i\geq2\), at least one \(\ell_i\geq3\), and \(r\geq L\). With these assumptions \(B\geq L\) and the three ranges above are consistent. The convention \(\binom{k-1}{t}=0\) applies outside \(0\leq t\leq k-1\), although the displayed noncontractible range avoids that ambiguity. The symmetry group preserves the central vertex and each arm length; for \(k\geq3\) this is the complete graph automorphism group.

## Proof

**1. Reduce to the hub link.** Let \(D\) be the deletion of the hub \(v\) in \(\operatorname{Ind}_r(T)\). Since deleting \(v\) produces disjoint paths with at most \(L\leq r\) vertices each, every subset of the remaining vertices is allowed: \(D\) is a full simplex. Let \(K=\operatorname{lk}_{\operatorname{Ind}_r(T)}(v)\). The complex is \(D\cup(v*K)\), with intersection \(K\), and the inclusion of \(K\) in the contractible simplex \(D\) is nullhomotopic. Therefore \(|\operatorname{Ind}_r(T)|\simeq\Sigma|K|\), naturally on reduced homology for the hub-preserving action.

For any face \(F\) on the arm vertices let \(q_i(F)\) be the length of the longest initial segment \(a_{i,1},\ldots,a_{i,q_i}\) entirely in \(F\), taking \(q_i=0\) when the first vertex is absent. The component containing \(v\) in \(T[F\cup\{v\}]\) has exactly \(1+\sum_i q_i(F)\) vertices. All other components are contained in individual arms and have at most \(L\leq r\) vertices. Consequently
\[
F\in K\quad\Longleftrightarrow\quad\sum_iq_i(F)\leq r-1.
\]

**2. Collapse the deficient-internal-vertex subcomplex.** Set \(U=\{a_{i,j}:1\leq j<\ell_i\}\), of cardinality \(B\), and let \(b_i=a_{i,\ell_i}\) be the terminal leaf. Let \(A\subseteq K\) consist of all faces not containing all of \(U\). This is a subcomplex. For each \(F\in A\), choose the first arm \(i\) for which its internal vertices are not all in \(F\). Adding or removing \(b_i\) leaves \(q_i(F)\) unchanged, because \(q_i(F)\leq\ell_i-2\), and cannot create an oversized component disconnected from \(v\) because \(\ell_i\leq r\). Thus \(F\leftrightarrow F\triangle\{b_i\}\) is a legal matching pair. Partitioning faces by their selected internal-vertex set shows acyclicity: in each fiber the chosen toggle is a perfect, acyclic coordinate matching, and the fiber labels form an order-preserving map to a Boolean face poset. On the nonempty face poset, exactly the singleton \(\{b_1\}\) remains critical, so \(A\) is collapsible and hence contractible.

**3. Identify a relative exterior chain complex.** Every face of \(K\setminus A\) is \(U\cup\{b_i:i\in J\}\), where \(J\subseteq[k]\). Its hub-component size is \(1+B+|J|\). Thus these relative faces exist exactly when \(0\leq|J|\leq t:=r-B-1\). Let \(P=\mathbb Z\langle e_1,\ldots,e_k\rangle\) and orient each relative face by first orienting \(U\), then writing its leaves in increasing arm order. The relative simplicial chain group in dimension \(B+j-1\) identifies with
\[
C_{B+j-1}(K,A;\mathbb Z)=\det(\mathbb Z[U])\otimes\bigwedge^jP,\qquad 0\leq j\leq\min(t,k).
\]
Deleting an internal vertex gives a face in \(A\) and so vanishes in the relative chain complex; deleting a leaf gives \((-1)^B\) times the alternating boundary \(\iota_{\varepsilon}:\bigwedge^jP\to\bigwedge^{j-1}P\), contraction with \(\varepsilon(e_i)=1\). Rescaling the degree-\(j\) generators by \((-1)^{Bj}\) identifies the relative differential exactly with contraction. This integral chain isomorphism is equivariant for \(\Gamma\). Writing \(P=W\oplus\mathbb Ze_1\) gives a contracting homotopy for the untruncated augmented simplex chain complex. If \(0\leq t<k\), its truncation has homology only in the top relative degree, namely
\[
H_{B+t-1}(K,A;\mathbb Z)=\det(\mathbb Z[U])\otimes\ker(\iota_{\varepsilon}:\bigwedge^tP\to\bigwedge^{t-1}P)
=\varepsilon_B\otimes\bigwedge^tW.
\]
For \(t=0\) the kernel is understood to be \(\bigwedge^0W=\mathbb Z\). For \(t<0\), \(K=A\). For \(t\geq k\), the full relative complex is acyclic; also \(r\geq B+k+1=|V(T)|\) makes \(\operatorname{Ind}_r(T)\) a simplex. Since \(A\) is contractible, the long exact sequence identifies \(\widetilde H_*(K)\) with \(H_*(K,A)\) naturally for \(\Gamma\). The Mayer--Vietoris connecting map for Step 1 gives the asserted \(\Gamma\)-module in degree \(r-1\).

**4. Upgrade homology to homotopy.** Collapsing the contractible subcomplex \(A\) to a point is an ordinary homotopy equivalence \(K\simeq K/A\). For \(0\leq t<k\), \(K/A\) has a single vertex and its other cells have dimensions \(B-1,B,\ldots,B+t-1\), all at least two because \(B\geq3\). Hence \(K/A\) is simply connected. Its reduced integral homology is free of rank \(\binom{k-1}{t}\) in the single degree \(B+t-1\geq2\), so Hurewicz plus Whitehead gives \(K/A\simeq\bigvee^{\binom{k-1}{t}}S^{B+t-1}\). Suspending proves the displayed homotopy classification. If \(r\leq B\), then \(K=A\) is contractible, so the suspension is contractible. The full-simplex range was treated above.

## Verification

Run `python3 verify.py`. It directly enumerates every allowed induced-component face of the full spider (including the hub), computes reduced mod-two homology by exact bit-matrix elimination, checks acyclicity of the explicit directed Hasse matching on the hub link, and checks integral signed Lefschetz traces against the proposed exterior-character formula for arm-length-preserving permutations. The independent finite calculations report `ALL_VERIFY_OK cases=59 face_instances=62408 matching_cases=42 matching_faces=13896 signed_character_checks=85`. They include unequal arm profiles with the same \(k\) and \(B\), and both contractible and noncontractible ranges. The all-parameter theorem is mathematical, not inferred from these finite tests.

For instance, both length profiles \((2,2,4)\) and \((2,3,3)\) have \(k=3\) and \(B=5\), so at \(r=6\) each complex is homotopy equivalent to \(S^5\). Under interchange of the two equal-length arms, the first has orientation character \(-1\) while the second has orientation character \(+1\) on its top integral homology; the sign is \((-1)^{\ell_i-1}\). This exhibits equality of ordinary homotopy types but distinguishable integral symmetry actions.

## Relationship to prior work

R. Sawant (arXiv:2605.25150, first submitted 24 May 2026) proves vertex decomposability of higher independence complexes for all trees. This establishes a qualitative wedge-of-spheres property but does not give the displayed length-profile-invariant ranks or the integral arm-permutation module. P. Deshpande and A. Singh (arXiv:2001.05448) compute explicit homotopy types for fully whiskered graphs, cycles, paths, complete multipartite graphs, and perfect regular rooted trees. The present spiders have a hub with no neighboring terminal leaf and need not be fully whiskered or perfect rooted trees. Abdelmalek et al. (arXiv:2106.10863) develop earlier shellability methods for related tree families, without this numerical and equivariant classification. The relationship is a specific quantitative refinement for a distinct, motivated family, not a reproof of the general qualitative theorem.

## Limitations

The theorem is restricted to spiders with at least three arms, all of length at least two, at least one of length at least three, and parameters \(r\geq L\). It does not classify the smaller-component regime \(r<L\), arbitrary rooted trees, or equivariant homotopy splittings. The integral module isomorphism does not imply torsion-free integral homology for quotient spaces. Literature comparisons cannot prove historical priority against every unindexed source.

## References

- R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150 (first public version 2026-05-24), https://arxiv.org/abs/2605.25150.
- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (2020), https://arxiv.org/abs/2001.05448.
- F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (2021), https://arxiv.org/abs/2106.10863.
