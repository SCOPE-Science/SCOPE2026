# Integral symmetry modules and automorphism quotients of multipartite higher independence complexes

## Finding

Let \(G=K_{m_1,\ldots,m_s}\) be a complete multipartite graph with \(s\ge3\) nonempty parts \(V_i\) of sizes \(m_i\ge1\), and let \(r\ge1\). Write \(V=\coprod_iV_i\), \(\Gamma=\operatorname{Aut}(G)\), and define the canonical augmentation lattices
\[
U=\ker(\varepsilon:\mathbb Z[V]\longrightarrow\mathbb Z),\qquad U_i=\ker(\varepsilon_i:\mathbb Z[V_i]\longrightarrow\mathbb Z).
\]
The \(r\)-independence complex \(K=\operatorname{Ind}_r(G)\) contains exactly those vertex subsets whose induced connected components have at most \(r\) vertices. Its only possible nonzero reduced integral homology is in degree \(r-1\), and there is a natural integral \(\Gamma\)-module isomorphism
\[
\boxed{\widetilde H_{r-1}(K;\mathbb Z)\cong_{\mathbb Z[\Gamma]}\frac{\bigwedge^r U}{\sum_{i=1}^{s}\bigwedge^r U_i}.}
\]
The denominator consists of the natural exterior-power sublattices and the quotient is **free over the integers**. In particular, for \(N=\sum_i m_i\), the already known ordinary Betti rank is recovered as
\[
\operatorname{rank}\widetilde H_{r-1}(K;\mathbb Z)=\binom{N-1}{r}-\sum_i\binom{m_i-1}{r},
\]
with out-of-range binomial coefficients interpreted as zero.

For each automorphism \(g\in\Gamma\), write \(\operatorname{Cyc}(g|S)\) for the cycle set of its permutation on a preserved vertex set \(S\). The full rational character of the integral module is given by
\[
\boxed{\operatorname{tr}(g_*|\widetilde H_{r-1})=[z^r]\left(\frac{\prod_{C\in\operatorname{Cyc}(g|V)}(1-(-z)^{|C|})}{1+z}-\sum_{i:g(V_i)=V_i}\frac{\prod_{C\in\operatorname{Cyc}(g|V_i)}(1-(-z)^{|C|})}{1+z}\right).}
\]
Here coefficient extraction is in formal power series, and the formula is interpreted as zero if the relevant homology vanishes.

Let \(t=|\{m_1,\ldots,m_s\}|\), the number of **distinct** part sizes. Then the geometric quotient \(Y=|K|/\Gamma\) satisfies
\[
\boxed{\widetilde H_j(Y;\mathbb Q)\cong\begin{cases}\mathbb Q^{\binom{t-1}{r}},&j=r-1,\\0,&j\ne r-1.\end{cases}}
\]
For example, \(K_{2,3,4}\) has \(\dim_{\mathbb Q}\widetilde H_1(Y;\mathbb Q)=1\) at \(r=2\), whereas every complete multipartite graph with all parts equally sized has rationally acyclic automorphism quotient in every positive \(r\). These are statements about rational quotient homology, **not** contractibility or integral quotient torsion.

## Assumptions and scope

All graphs are finite and simple. There are at least three part classes, all with positive size. The automorphism group includes all permutations within each part and all exchanges between equal-sized parts; the displayed module isomorphism is natural for this full group. Exterior powers past the lattice rank and binomial coefficients outside their standard range are zero. Reduced homology follows the augmented chain convention; \(r\ge1\), so all nonzero degrees under discussion are nonnegative. For \(r\ge N\), the complex is a simplex and every displayed reduced homology group is zero.

## Proof

**1. Exact decomposition.** A subset meeting two distinct parts induces a complete multipartite connected graph. Thus if its size exceeds \(r\), it is forbidden; a subset contained in one part is always allowed. Set \(L=\operatorname{skel}_{r-1}\Delta_V\). Exactly,
\[
K=L\cup\bigcup_{i=1}^s\Delta_{V_i},\qquad L\cap\Delta_{V_i}=\operatorname{skel}_{r-1}\Delta_{V_i}.
\]
The full simplices have disjoint nonempty vertex sets and do not meet each other geometrically.

**2. Augmentation and relative chains.** For a finite nonempty vertex set \(S\), the augmented chain complex of its simplex is exact. The top cycle group of its \((r-1)\)-skeleton is naturally \(\bigwedge^r\ker(\mathbb Z[S]\to\mathbb Z)\). To see this over the integers, fix \(v_0\in S\); the boundaries of the \(r\)-simplices with \(v_0\) as a vertex form a \(\mathbb Z\)-basis and correspond to the exterior products of differences \(e_v-e_{v_0}\). This identification is canonical, being induced by the augmented simplicial boundary, and hence equivariant under permutations of \(S\).

The relative chain complex \(C_*(K,L)\) is the direct sum of \(C_*(\Delta_{V_i},\operatorname{skel}_{r-1}\Delta_{V_i})\). Therefore its only possible nonzero relative homology is \(H_r(K,L)\cong\bigoplus_i\bigwedge^r U_i\). The connecting homomorphism in the reduced long exact sequence is exactly the sum of natural inclusions of these exterior powers into \(\bigwedge^r U\). These assertions remain valid if some skeleton is already a full simplex, since the corresponding exterior power is zero.

**3. Integral injectivity and torsion.** Choose a representative \(v_i\in V_i\). The differences \(e_v-e_{v_i}\) within every part, together with the \(s-1\) differences \(e_{v_i}-e_{v_s}\) for \(i<s\), form an integral basis of \(U\). Consequently \(\bigoplus_i U_i\) is a direct summand of \(U\). In the exterior-power basis, each \(\bigwedge^r U_i\) is spanned by disjoint pure-part basis wedges. Their direct sum is therefore a primitive direct summand of \(\bigwedge^r U\). The long exact sequence gives zero higher reduced homology, the stated integral quotient in degree \(r-1\), no homology elsewhere, and a torsion-free quotient. Choices of representatives establish primitivity only: the quotient-module isomorphism itself is the canonical equivariant one induced by the chain map.

**4. Character.** For a permutation \(g\) acting on a finite set \(S\),
\[
\det(1+z g\mid\mathbb Q[S])=\prod_{C\in\operatorname{Cyc}(g|S)}(1-(-z)^{|C|}).
\]
The rational permutation representation splits into its trivial line and augmentation subspace, giving \(\det(1+zg\mid U_{\mathbb Q})\) by division by \(1+z\). The degree-\(r\) coefficient is the trace on \(\bigwedge^r U_{\mathbb Q}\). The direct sum of block-exterior modules is permuted by \(g\); a block contributes to its trace only if it is preserved setwise. Subtracting gives the character formula.

**5. Rational quotient homology.** For a finite group acting simplicially on a finite complex, barycentric subdivision makes the action admissible; its invariant rational chain complex computes the rational homology of the geometric orbit space. Equivalently, finite-group invariants are exact in characteristic zero, so
\[
\widetilde H_j(|K|/\Gamma;\mathbb Q)\cong\widetilde H_j(K;\mathbb Q)^\Gamma.
\]
Let \(H=\prod_i S_{m_i}\) act within the parts and let \(P=\Gamma/H\) exchange equal-sized parts. Rationally, \(U\) decomposes \(H\)-equivariantly as
\[
U_{\mathbb Q}\cong W\oplus\bigoplus_i(U_i)_{\mathbb Q},\qquad W=\left\{(x_i)\in\mathbb Q^s:\sum_i m_i x_i=0\right\},
\]
where \(W\) represents block-constant functions and \(H\) is trivial on \(W\). For \(1\le a\le m_i-1\), the nonzero exterior powers \(\bigwedge^a(U_i)_{\mathbb Q}\) are nontrivial hook irreducibles for \(S_{m_i}\); hence no exterior monomial involving a positive-degree factor from any \(U_i\) is \(H\)-invariant. The removed pure-block summands also have no \(H\)-invariants. Thus the entire \(H\)-invariant homology is \(\bigwedge^r W\). Now \(P\) acts by permuting the \(c_d\) blocks of each given size \(d\), and
\[
W\cong\mathbb Q^{t-1}\oplus\bigoplus_d U_{c_d,\mathbb Q}
\]
as \(P\)-modules, where \(U_{c_d,\mathbb Q}\) is the standard augmentation representation on the \(c_d\) equal-size blocks (zero if \(c_d=1\)). Every positive-degree exterior power of a nonzero standard summand has no invariants under its corresponding symmetric-group factor. Therefore \((\bigwedge^r W)^P\cong\bigwedge^r\mathbb Q^{t-1}\), whose dimension is \(\binom{t-1}{r}\). This proves the quotient classification for all permitted parameters.

## Verification

A standalone Python script `verify.py` performs exact, independent finite-face and group-action checks for ten multipartite parameter sets. It enumerates all vertices, all graph automorphisms (including part exchanges), all permitted faces, and the orientation sign of every invariant face. It verifies the predicted top homology character by signed reduced Lefschetz traces, in 9,030 group-and-threshold comparisons. It also constructs **actual invariant signed chain complexes** over the prime field of order 1009, with 26 separate checks of the quotient homology degrees and ranks; all agree. The saved `verify_output.txt` records successful execution. The proof above, not finite computation, establishes every integral statement and arbitrary parameter range.

## Relationship to prior work

Deshpande and Singh (2020, Theorem 3.5) already compute the complete multipartite \(r\)-independence **ordinary homotopy type and sphere count**, including precisely the nonequivariant rank reproduced above. Those are not claimed as new. Bayer et al., *Topology of Cut Complexes of Graphs* (2023/2024), analyze related Alexander-dual cut complexes, including equivariant results for a different multipartite construction. Bayer et al., *Topology of Cut Complexes II* (2024, Section 6.1, Theorem 6.2), give an equivariant analysis for cut complexes of the disjoint union of **two** complete graphs; this is a closely related Alexander-dual, two-part case, and the stated new theorem is therefore limited to **three or more parts**. Sawant's May 2026 paper develops higher independence complexes of trees by vertex-decomposability methods, not full multipartite homology representations or automorphism quotients. The present additional content is a canonical **integral full-automorphism module**, its full character, and a uniform classification of rational automorphism-quotient homology depending only on the number of distinct part sizes.

## Limitations

The new claims require at least three parts and concern the full multipartite graph automorphism group. The ordinary nonequivariant ranks were previously known. The quotient homology formula has rational coefficients only: it makes no assertion about integral quotient torsion, quotient contractibility, fundamental groups, or equivariant homotopy type. Equivalent unindexed work remains possible; the present originality assessment is based on inspected closely relevant sources and comparison of the theorems rather than guaranteed exhaustive coverage.

## References

1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1, first posted 2026-05-24, https://arxiv.org/abs/2605.25150.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first posted 2020-01-15, https://arxiv.org/abs/2001.05448.
3. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first posted 2023-04-26, https://arxiv.org/abs/2304.13675.
4. M. Bayer and collaborators, *Topology of Cut Complexes II*, arXiv:2407.08158, first posted 2024-07-11, https://arxiv.org/abs/2407.08158.
