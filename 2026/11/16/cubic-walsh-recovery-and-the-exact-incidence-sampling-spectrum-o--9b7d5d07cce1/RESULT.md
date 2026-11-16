# Cubic Walsh recovery and the exact incidence-sampling spectrum of labelled affine planes of order three

## Finding

Let \(\mathcal S\) be the set of all \(840\) labelled Steiner triple systems on \(X=\{0,1,\ldots,8\}\); equivalently, all labelled affine planes of order three. Regard each system as a Boolean incidence vector indexed by the \(84\) triples in \(\binom X3\). For each \(d\in\{0,1,2,3\}\), let \(V_d\) be the span, as functions on \(\mathcal S\), of all Boolean Walsh characters \(\chi_A(s)=(-1)^{\sum_{t\in A}s_t}\) with \(|A|\le d\). Then

\[
(\dim V_0,\dim V_1,\dim V_2,\dim V_3)=(1,49,469,840).
\]

Thus degree-three character observations identify every signed measure, hence every probability distribution, on \(\mathcal S\), while degree-two observations leave a \(371\)-dimensional ambiguity space.

There is also a complete exact spectral certificate for the unnormalized **membership-monomial** sampling matrices. Let \(F_d\) have rows indexed by \(s\in\mathcal S\), columns by subsets \(A\subseteq\binom X3\) of cardinality at most \(d\), and entries \(F_d(s,A)=\prod_{t\in A}s_t\). Its row Gram matrix \(G_d=F_dF_d^{\mathsf T}\) has the following distinct eigenvalues with multiplicities (superscripts indicate multiplicity):

\[
\begin{aligned}
\operatorname{Spec}(G_0)&=\{840^{[1]},0^{[839]}\},\\
\operatorname{Spec}(G_1)&=\{2280^{[1]},180^{[48]},0^{[791]}\},\\
\operatorname{Spec}(G_2)&=\{3720^{[1]},570^{[48]},120^{[84]},102^{[120]},60^{[216]},0^{[371]}\},\\
\operatorname{Spec}(G_3)&=\{4920^{[1]},1133^{[48]},440^{[84]},422^{[120]},275^{[216]},168^{[42]},128^{[189]},120^{[84]},63^{[56]}\}.
\end{aligned}
\]

Consequently the nonzero singular values of the cubic membership-monomial sampling operator lie between \(\sqrt{63}\) and \(\sqrt{4920}\), both attained. Its sharp squared condition number is \(4920/63=1640/21\), and its inverse on the image has operator norm \(1/\sqrt{63}\) in the stated unnormalized Euclidean coordinates. The eigenvalues above are **not** claimed as the Gram eigenvalues of the character basis; the character and monomial families have the same span by an invertible degree-filtered change of basis.

## Assumptions and scope

A labelled Steiner triple system of order nine is a set of twelve distinct triples of \(X\) in which every two-element subset of \(X\) occurs in exactly one triple. It is not a quotient under relabelling. All scalar ranks and spectra in this statement are over \(\mathbb R\), and the Fourier characters use the elementary abelian group \((\mathbb Z/2\mathbb Z)^{84}\). The sampling rows are not normalized by \(840\) or by the number of columns. Monomial observation degree counts distinct lines, not the three point incidences inside a line.

## Proof

**1. Incidence versus Fourier observables.** Write \(s_t\in\{0,1\}\) for the indicator of the triple \(t\) in a labelled system. For each subset of triples \(A\),
\[
\chi_A(s)=\prod_{t\in A}(1-2s_t).
\]
Möbius inversion in the Boolean subset lattice expresses each monomial \(\prod_{t\in A}s_t\) as a linear combination of the characters \(\chi_B\) with \(B\subseteq A\). Both transformations preserve the degree filtration and are invertible. Hence \(\dim V_d=\operatorname{rank}(F_d)=\operatorname{rank}(G_d)\).

**2. Intersection kernel.** The matrix entry \((G_d)_{s,s'}\) counts subsets \(A\) of at most \(d\) triples simultaneously in \(s\) and \(s'\). With \(h=|s\cap s'|\),
\[
(G_d)_{s,s'}=\sum_{j=0}^{d}\binom hj.
\]
This expression is valid with \(\binom hj=0\) for \(j>h\).

**3. Exhaustive, non-heuristic enumeration.** The supplied exact-cover implementation selects the first uncovered pair of points (or any pair with the smallest number of legal completions), adds a triple covering it, and recurses until all \(36\) pairs are covered. Every valid system is reached once because at each stage a triple containing the selected pair must be chosen, no pair may be repeated, and the final collection covers every pair. It produces exactly \(840\) distinct systems. An independently implemented relabelling orbit of the twelve lines of \(\operatorname{AG}(2,3)\) also contains exactly \(840\) systems; because each orbit element satisfies the Steiner condition and the independent exact-cover enumeration has only \(840\), the orbit is the entire set. In particular the symmetric group \(S_9\) acts transitively on the \(840\) rows.

**4. Exact spectral certification.** For each of the four degrees, let \(E_d\) be the set of distinct integer eigenvalues shown in the Finding. Compute the integer vector
\[
\left(\prod_{\lambda\in E_d}(G_d-\lambda I)\right)e_{s_0}
\]
by successive exact matrix-vector products for the first enumerated system \(s_0\); the supplied checker verifies every coordinate equals zero. The kernel is invariant under the \(S_9\) relabelling action, so the same vector identity holds for each basis vector. Therefore the polynomial annihilates the entire real symmetric matrix \(G_d\); all its eigenvalues belong to \(E_d\).

For \(0\le k<|E_d|\), the same integer computation checks the trace identities
\[
\operatorname{tr}(G_d^k)=840\,(G_d^k)_{s_0,s_0}=\sum_{\lambda\in E_d}m_{d,\lambda}\lambda^k,
\]
using the multiplicities \(m_{d,\lambda}\) displayed above. Transitivity proves the first equality. The Vandermonde matrix on the distinct roots is invertible, so these are the **unique** multiplicities. All multiplicities are positive, so all listed levels occur. Counting positive levels proves the four rank values, and the minimum and maximum positive cubic eigenvalues give the sharp stability bounds.

**5. Distinguishable distributions.** For degree two, any nonzero vector in the \(371\)-dimensional kernel of \(F_2^{\mathsf T}\) has zero total mass because the constant column is present. Perturbing the strictly positive uniform distribution by sufficiently small positive and negative multiples of such a vector gives distinct probability distributions with the same degree-two moments, hence with the same joint membership probabilities for any two specified triples. The full rank of \(F_3\) proves degree-three injectivity.

## Verification

Run `python verify_exact.py` using the Python standard library. This constructs all \(840\) systems by exact cover, checks all four integer annihilating-polynomial identities and all trace moments, and asserts every displayed eigenvalue and multiplicity. Independently, run `python verify_orbit.py`, which constructs the complete relabelling orbit and performs modular Gaussian elimination at prime \(10007\), confirming ranks \(1,49,469,840\). The latter checker uses NumPy. The two methods obtain their systems independently and use different rank certificates. The supplied `spectra.json` is a machine-readable restatement of the exact levels, not independent evidence. The exact-cover plus characteristic-polynomial/trace proof already certifies the rational and real spectra; the modular check is additional corroboration.

## Relationship to prior work

The uniqueness and labelled count of the order-nine Steiner system, the affine-plane description, and much of its intersection combinatorics are classical. Bryant, Grannell and Griggs (2003 preprint) explicitly describe the \(840\) labelled systems, their symmetry group of order \(432\), and partitions into large sets. Chee, Ling and Shen (2008 preprint) study the fine intersection problem and cite the possible common-block counts \(\{0,1,2,3,4,6,12\}\) at order nine. Assmus (1995) studies **point/block incidence-code ranks of individual Steiner systems**, not the degree-filtered sampling rank across all labelled systems. A separately indexed result on six-cycle switch distances between labelled order-nine systems uses the common-block count to determine a switching metric, a different matrix operator. The distinct assertion here is the exact Fourier sampling threshold and the complete spectra of the degree-zero through degree-three membership-monomial Gram matrices. Knowing the possible intersection numbers or the number of systems alone does not determine their full Gram spectral multiplicities.

## Limitations

The statement concerns only fully labelled order-nine Steiner triple systems, not an all-order interpolation theorem. The cubic spectrum uses the unnormalized membership-monomial frame, not the unnormalized Walsh frame, although their ranks agree. The proof is exact and finite, with a fully reproducible exhaustive enumeration; it does not give a conceptual irreducible-representation decomposition of the nine cubic spectral levels. Earlier unpublished computations of these same incidence-sampling spectra have not been ruled out, and the full text of one relevant chapter on uniformly intersecting order-nine systems was not accessible for comparison.

## References

1. E. F. Assmus Jr., *On 2-ranks of Steiner triple systems*, Electronic Journal of Combinatorics **2** (1995), #R9, published 1995-04-17. https://doi.org/10.37236/1203
2. D. Bryant, M. Grannell, T. Griggs, *Large sets of large sets of Steiner triple systems of order 9*, author preprint accepted 2003. https://grannell.net/Papers/lsls9.pdf
3. Y. M. Chee, A. C. H. Ling, H. Shen, *The fine intersection problem for Steiner triple systems*, first arXiv posting 2008-07-16. https://arxiv.org/abs/0807.2500
4. T. S. Griggs, A. Rosa, *Sets of Steiner Triple Systems of Order 9 Revisited*, in *Designs 2002* (2003), pp. 255–276. https://doi.org/10.1007/978-1-4613-0245-2_10
