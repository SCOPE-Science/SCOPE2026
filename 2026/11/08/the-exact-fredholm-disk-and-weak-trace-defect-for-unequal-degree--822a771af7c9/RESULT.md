# The exact Fredholm disk and weak-trace defect for unequal-degree monomial Bergman products

## Finding
For every real \(\alpha>-1\) and distinct positive integers \(m\ne n\), the Bergman composition product \(T_{m,n}=C_{z^m}C_{z^n}^{*}\) is a compact perturbation of a canonical partial permutation \(J_{m,n}\). Put \(\beta=\alpha+1\), \(c=(mn)^{-\beta/2}\), and
\[
\kappa=\frac{\beta(\beta+1)}2(mn)^{-\beta/2}\left(1-\frac1{2m}-\frac1{2n}\right).
\]
The defect \(D_{m,n}=T_{m,n}-cJ_{m,n}\) has exact nonzero singular values given by the nonzero entries of \(\lvert w_k-c\rvert\), where
\[
w_k=\frac{B_k}{\sqrt{B_{mk}B_{nk}}},\qquad
B_k=\frac{\Gamma(k+\beta+1)}{\Gamma(\beta+1)\Gamma(k+1)}
\quad(k\geq0).
\]
For these unequal positive degrees, the defect is compact and has sharp weak-trace asymptotics
\[
\lim_{j\to\infty}j\,s_j(D_{m,n})
=\lim_{N\to\infty}\frac1{\log N}\sum_{j=1}^{N}s_j(D_{m,n})
=\kappa>0,
\]
where the second limit is for \(N\geq2\). In particular, for every \(p>0\), \(D_{m,n}\in S_p\) exactly when \(p>1\). The positive compact operator \(\lvert D_{m,n}\rvert\) is measurable in the logarithmic singular-trace sense, with coefficient \(\kappa\).

For unequal degrees \(m\ne n\), there is an exact spectral phase:
\[
\sigma_{\mathrm{ess}}(T_{m,n})=\{\lambda\in\mathbb C:|\lambda|\le c\},\qquad
\sigma(T_{m,n})=\{1\}\cup\{\lambda\in\mathbb C:|\lambda|\le c\}.
\]
Here \(\sigma_{\mathrm{ess}}\) is the Fredholm essential spectrum, and \(1\) is an isolated simple eigenvalue. In particular, \(\|T_{m,n}\|_{\mathrm e}=c\).

## Assumptions and scope
The Hilbert space is the weighted analytic Bergman space \(A_\alpha^2(\mathbb D)\), with normalized measure \((\alpha+1)(1-|z|^2)^\alpha dA(z)/\pi\). All composition operators are bounded on this space. The vectors \(e_k=\sqrt{B_k}\,z^k\), \(k\geq0\), form an orthonormal basis. Define the partial permutation on this basis by \(J_{m,n}e_{nk}=e_{mk}\) and \(J_{m,n}e_j=0\) when \(n\) does not divide \(j\), with \(k,j\geq0\). The constants are included in the index \(k=0\); the argument separates the constant vector from positive degrees. Singular values are arranged in nonincreasing order, and \(S_p\) denotes the Schatten ideal, including \(0<p<1\).

## Proof
**Matrix and singular values.** Because \(C_{z^m}e_k=\sqrt{B_k/B_{mk}}\,e_{mk}\) and \(C_{z^n}^*e_{nk}=\sqrt{B_k/B_{nk}}\,e_k\), direct multiplication gives \(T_{m,n}e_{nk}=w_k e_{mk}\), with zero on all other basis vectors. The sources and destinations of distinct nonzero entries are disjoint; hence the singular-value multiset of \(D_{m,n}\) is exactly \(\{|w_k-c|:k\geq0\}\), supplemented by zeros as appropriate. The common constant vector has \(w_0=1\).

**Sharp compact remainder.** Gamma-ratio asymptotics, valid for every fixed \(\beta>0\), give
\[
B_k=\frac{k^\beta}{\Gamma(\beta+1)}\left(1+\frac{\beta(\beta+1)}{2k}+O(k^{-2})\right).
\]
Substitution into the exact weights yields \(w_k=c+\kappa/k+O(k^{-2})\). Thus \(w_k\to c\), proving compactness. The coefficient \(\kappa\) is strictly positive for unequal positive degrees, since \(1/(2m)+1/(2n)<1\). Standard counting of an asymptotic \(\kappa/k\) singular sequence gives \(j s_j\to\kappa\) and the stated logarithmic limit, together with the sharp \(S_p\) threshold.

**Unequal-degree essential spectrum.** On the positive-index basis, the partial permutation \(J_{m,n}\) sends \(e_j\) to \(e_{(m/n)j}\) when \(n\mid j\), and to zero otherwise. Its directed graph is a disjoint union of chains (never cycles), since each nonzero step multiplies the positive integer label by the fixed ratio \(m/n\ne1\). If \(m>n\), every chain has an initial vertex; if \(m<n\), every chain has a terminal vertex. Chains with arbitrarily many edges exist: for each \(L\geq1\), the distinct labels \(n^L t,n^{L-1}mt,\ldots,m^Lt\) form a directed segment of length \(L\). Choosing infinitely many pairwise distinct primes \(t\) that divide neither \(m\) nor \(n\) makes disjoint chains; for each fixed \(L\) these yield infinite orthogonal repetitions of long segments. If \(m>n\), a length-\(L\) chain starting at its initial vertex supplies a truncated geometric approximate eigenvector for \(J_{m,n}^*\) with spectral parameter \(\overline\lambda\), whose residual after unit normalization tends to zero for any \(|\lambda|<1\). For \(m<n\), use the reversed construction at terminal vertices to obtain an approximate eigenvector for \(J_{m,n}\). For \(|\lambda|=1\), phase-aligned vectors uniformly distributed on long segments give residual norm at most \(2/\sqrt{L+1}\). Disjoint-support constructions (or arbitrarily high multiplicity in the finite-chain case) rule out Fredholmness throughout the closed unit disk. For \(|\lambda|>1\), the Neumann series for \(J_{m,n}\) provides a bounded inverse. Therefore the positive-degree restriction has Fredholm essential spectrum the closed unit disk. Adding the one-dimensional constant component does not change it; the compact difference \(T_{m,n}-cJ_{m,n}\) transfers this disk to radius \(c\).

**No additional spectrum outside the disk.** The positive-degree part is a weighted partial permutation with \(w_k\to c\). For any \(\varepsilon>0\), only finitely many entries exceed \(c+\varepsilon\). Along any orbit in positive indices, distinct steps have distinct source labels, since \(m/n\ne1\). Hence a product of \(L\) weights contains at most finitely many exceptional factors, uniformly in the orbit. Its \(L\)-th norm root is at most \(c+\varepsilon\) asymptotically, so the positive-degree spectral radius is at most \(c\). The essential disk already lies in its spectrum, making the spectrum exactly that disk. The constant vector is a reducing one-dimensional eigenspace with eigenvalue \(1\), which lies outside the disk because \(c<1\) for unequal degrees. Since \(J_{m,n}\) has essential norm one, \(T_{m,n}\) has essential norm \(c\).

## Verification
An independent finite exact-arithmetic checker `verify_monomial_products.py` verifies the monomial matrix entries, gamma-ratio coefficient identities for several integral weights, and long directed segments. It reports `MONOMIAL_COMPOSITION_EXACT_FINITE_CHECKS_OK 8460`. Such finite checks neither establish Fredholm essential spectra nor prove the asymptotic assertions; those conclusions follow from the preceding analytic and chain arguments.

## Relationship to prior work
Leng and Zhao (2026) study the qualitative Schatten-class membership of products of composition operators and adjoints on Hardy and Bergman spaces. Their Section 4 treats Bergman products via composition symbols, integral sufficient conditions, and trace-class necessary conditions, not a monomial-product spectral disk or the exact compact-correction singular-value coefficient. Clifford and Zheng (2003) give compactness criteria for Bergman composition products; the present noncompact operators and their compact remainder are a different quantitative question. For equal-degree one-symbol self-products on the unweighted Bergman space, the published abstract of Abdollahi, Mehrangiz, and Roientan (2015) explicitly reports the spectra, essential spectra, and norms. That previously established case is excluded from the present theorem. Standard weighted-shift and gamma-asymptotic calculations are tools, not the quantitative mixed-degree disk and compact-defect classification. Publication priority of the unequal-degree cross-product and exact weak-trace defect remains subject to comparison with older spectral formulations of mixed composition products.

## Limitations
The symbols are monomials with distinct positive integral exponents, the domain is a single disk, and the Bergman weight is radial and of classical power type. The weak trace coefficient applies to the canonical compact defect \(T_{m,n}-cJ_{m,n}\), not the noncompact product itself. The statement does not classify arbitrary finite Blaschke symbols, general composition symbols, or their cross-products. Independent external mathematical verification has not been performed.

## References
- Q. Leng and X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472v1, publicly submitted 11 October 2026, especially Section 4. https://arxiv.org/abs/2610.15472
- J. H. Clifford and D. Zheng, *Composition operators on Bergman spaces*, Chinese Annals of Mathematics 24B (2003), 433–448. The author's publication list provides a public copy: https://as.vanderbilt.edu/math/bio/dechao-zheng/
- A. Abdollahi, S. Mehrangiz, and T. Roientan, *Self-commutators of composition operators with monomial symbols on the Bergman space*, Bulletin of the Iranian Mathematical Society 41(7) (2015), 65–76. Its stated exact same-symbol spectral results are prior work: https://eurekamag.com/research/109/906/109906911.php
