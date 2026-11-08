# Sharp condition-number envelopes and block-size cutoff for volume-sampled projections

## Finding
Let \(d\ge2\), \(1\le r\le d\), and \(K\ge1\). Let \(G\) be a real \(d\times d\) positive definite Gram matrix with \(\kappa_2(G)\le K\). In an eigencoordinate representation of \(G\), select a size-\(r\) coordinate subspace with probability proportional to the product of its selected eigenvalues, and write \(M_r\) for the expected orthogonal projector. Equivalently, \(M_r\) is the expected projector in the volume-sampled projection method of Entezari–Banerjee–Kalantari (2026). Then the following two bounds are sharp simultaneously:
\[
\lambda_{\min}(M_r)\ge\frac{r}{r+(d-r)K},\qquad
\kappa_2(M_r)\le\frac{r-1+(d-r)K}{d-1}.
\]
For \(K>1\) and \(r<d\), the first equality is attained precisely (up to common scaling and permutation) by the Gram spectrum \((1,K,\ldots,K)\). For \(2\le r<d\), this spectrum also uniquely attains the second bound up to scaling and permutation; at \(r=1\), equality in the second bound merely requires \(\kappa_2(G)=K\). At \(r=d\), \(M_d=I\); at \(K=1\) both bounds are identities. Thus the smallest block size guaranteeing \(\lambda_{\min}(M_r)\ge\theta\) for every such Gram matrix, for any \(0<\theta\le1\), is exactly
\[
 r_{\mathrm{guaranteed}}=\left\lceil\frac{\theta dK}{1+\theta(K-1)}\right\rceil.
\]

## Assumptions and scope
The ambient space is real Euclidean dimension \(d\). The matrix \(G\) is positive definite; \(K\) bounds its **spectral** condition number (ratio of largest to smallest Gram eigenvalue). The volume-sampled subset is of cardinality \(r\), where the elementary-symmetric weights are strictly positive. For a consistent least-squares projection algorithm using \(d\) independent vectors with Gram spectrum as above, \(M_r\) is precisely the mean projector, and the sharp worst-case conditional expected squared-error contraction is \(1-r/[r+(d-r)K]\). No uniform claim is made for arbitrary unequal sampling laws, incompatible subspace geometries, or inconsistent linear systems.

## Proof
Let \(0<\lambda_1\le\cdots\le\lambda_d\) be the Gram eigenvalues. The volume-sampling spectral identity (Entezari–Banerjee–Kalantari, Theorem 1) gives eigenvalues of the mean projector
\[
 p_i=\frac{\lambda_i e_{r-1}(\lambda_{-i})}{e_r(\lambda_1,\ldots,\lambda_d)},
\]
where \(e_j\) is the degree-\(j\) elementary symmetric polynomial, \(e_0=1\), and \(e_j=0\) outside its natural range. This also follows directly by summing \(\prod_{i\in S}\lambda_i\) over all \(r\)-element subsets \(S\) containing \(i\). In particular, \(0<p_i\le1\) and \(\sum_i p_i=r\).

For distinct \(i,j\), with \(T\) the remaining eigenvalues, cancellation yields
\[
 p_j-p_i=\frac{(\lambda_j-\lambda_i)e_{r-1}(T)}{e_r(\lambda)}.
\]
Hence the ordered extreme eigenvalues of \(M_r\) are \(p_1,p_d\). Rescale so \(\lambda_1=1\), \(1\le\lambda_j\le K\). Then
\[
 p_1=\frac{1}{1+e_r(\lambda_2,\ldots,\lambda_d)/e_{r-1}(\lambda_2,\ldots,\lambda_d)}.
\]
The ratio \(e_j/e_{j-1}\) is nondecreasing in each positive argument. Indeed, replacing one argument by \(t\) makes this ratio \([e_j(U)+t e_{j-1}(U)]/[e_{j-1}(U)+t e_{j-2}(U)]\), whose derivative has numerator \(e_{j-1}(U)^2-e_j(U)e_{j-2}(U)\ge0\) by Newton's inequalities; the endpoint ranges follow by continuity. Thus \(p_1\) is minimized when every other eigenvalue equals \(K\). Since \(e_r(K,\ldots,K)/e_{r-1}(K,\ldots,K)=(d-r)K/r\), the first claimed bound follows. In the nondegenerate case \(K>1,r<d\), strict positivity of the relevant derivatives forces the stated equality spectrum.

For \(r=1\), \(p_d/p_1=\lambda_d/\lambda_1\le K\), the advertised expression. For \(2\le r<d\), set \(h=\lambda_d\in[1,K]\), and let \(T=(\lambda_2,\ldots,\lambda_{d-1})\). Direct cancellation gives
\[
 \frac{p_d}{p_1}=h\frac{s+1}{s+h},\qquad s=\frac{e_{r-1}(T)}{e_{r-2}(T)}.
\]
The right-hand side is nondecreasing in \(s\), strictly increasing when \(h>1\). Newton's inequalities make \(s\) nondecreasing in each intermediate eigenvalue, so its largest possible value is \((d-r)h/(r-1)\), when all of them equal \(h\). Consequently
\[
 \frac{p_d}{p_1}\le\frac{(d-r)h+r-1}{d-1}\le\frac{(d-r)K+r-1}{d-1}.
\]
Strictness yields the equality description. For \(r=d\), the only subset is the full set, so \(M_d=I\). Finally the sharp lower bound is increasing in \(r\), and solving \(r/[r+(d-r)K]\ge\theta\) for integer \(r\) proves the cutoff formula; its failure for every smaller integer \(r\) is witnessed by \((1,K,\ldots,K)\).

## Verification
`check_envelope.py` uses exact integer combinatorics and rational arithmetic. It exhaustively evaluates every integer spectrum with entries in \(\{1,\ldots,K\}\), minimum 1 and maximum \(K\), for \(d=2,\ldots,7\), \(K=2,3,4\), and each admissible block size. It tests normalization, both sharp inequalities and equality on the one-low-rest-high family. The completed execution reported 497,970 assertions passing. This is a finite cross-check, not proof of the general theorem.

## Relationship to prior work
Entezari, Banerjee and Kalantari (arXiv:2610.12346, Theorem 1) obtained the underlying exact spectral transform and qualitative spectral equalization. Rodomanov and Kropotov (arXiv:1904.04587) studied volume-sampled coordinate descent with related elementary-symmetric formulas. Neither cited result, in the sections inspected, presents the **sharp uniform extremization over all spectra with a fixed Gram condition-number cap**, both extremizer classifications, and the exact worst-case block-size cutoff derived here. The spectral transform is prior work; the constrained extremal envelope is the mathematical assertion of this note.

## Limitations
The result is a worst-case guarantee, not an expected runtime or practical recommendation when enumerating volume-sampled blocks is computationally expensive. It uses the Gram condition number, not its square root, and proves no improvement for approximate volume sampling. The novel component is a sharp optimization of a known spectral formula, not discovery of that formula. Related older results on elementary-symmetric polynomial inequalities and determinantal inclusion probabilities may provide alternative or equivalent proofs; comprehensive historical priority is not certified.

## References
1. A. Entezari, A. Banerjee and L. Kalantari, *Volume Sampling and Spectral Equalization in Randomized Alternating Projections*, arXiv:2610.12346 (first posted October 8, 2026), https://arxiv.org/abs/2610.12346.
2. A. Rodomanov and P. Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, arXiv:1904.04587 (2019), https://arxiv.org/abs/1904.04587.
3. Y. Yu, *On the inclusion probabilities in some unequal probability sampling plans without replacement*, Bernoulli 18 (2012), arXiv:1005.4107, https://arxiv.org/abs/1005.4107 (related inclusion-probability majorization, not the present spectral cap optimization).
