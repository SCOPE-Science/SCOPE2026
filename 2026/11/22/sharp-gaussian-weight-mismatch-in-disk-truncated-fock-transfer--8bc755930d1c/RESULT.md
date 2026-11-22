# Sharp Gaussian-weight mismatch in disk-truncated Fock transfer

## Finding
Let \(\mathcal F_\gamma\) be the analytic Gaussian Fock Hilbert space with normalized measure \(d\mu_\gamma(z)=(\gamma/\pi)e^{-\gamma|z|^2}\,dA(z)\), for \(\gamma>0\). Denote by \(P_\beta\) the orthogonal Fock projection in \(L^2(\mu_\beta)\). For \(\alpha,\beta,R>0\), define the **disk-truncated cross-weight transfer**
\[
D_{\alpha,\beta,R}f=P_\beta(\mathbf1_{\{|z|<R\}}f),\qquad \mathcal F_\alpha\longrightarrow\mathcal F_\beta.
\]
Set \(x=\beta R^2\), \(u=\sqrt{\alpha/\beta}\), and
\[
q_n(x)=e^{-x}\sum_{k=n+1}^\infty\frac{x^k}{k!},\qquad n\ge0.
\]
The complete *monomial-indexed* singular spectrum (not necessarily in decreasing order) is
\[
\boxed{a_n(x,u)=u^n q_n(x),\qquad n=0,1,\ldots.}
\]
Every \(D_{\alpha,\beta,R}\) is injective, compact, and in every Schatten class \(\mathcal S_p\) for \(p>0\). The sequence \(a_n\) is strictly log-concave, so the norm is attained by one monomial, or exactly two **adjacent** monomials. Writing \(r_n(x)=q_n(x)/q_{n+1}(x)\), the thresholds satisfy \(1<r_0<r_1<\cdots\to\infty\); degree \(n\ge1\) maximizes precisely when \(r_{n-1}\le u\le r_n\), with the obvious endpoint convention, and degree zero maximizes precisely when \(u\le r_0\).

The first change away from the constant monomial occurs at the *exact* ratio
\[
\boxed{\frac\alpha\beta=\left(\frac{1-e^{-x}}{1-(1+x)e^{-x}}\right)^2
=1+2xe^{-x}(1+o(1))\quad(x\to\infty).}
\]
For \(u\le1\), at **every radius**, \(\|D_{\alpha,\beta,R}\|=1-e^{-x}\). By contrast, at each fixed \(u>1\), as \(R\to\infty\),
\[
\boxed{\|D_{\alpha,\beta,R}\|
\sim\frac{\exp[x(u-1)]}{(u-1)\sqrt{2\pi u x}},\qquad
\frac{n_x}{x}\longrightarrow u,}
\]
where \(n_x\) is any maximizing monomial degree. Thus the full sharp exponential amplification, its nontrivial inverse-square-root prefactor, and the escaping maximizing degree are determined by the weight mismatch.

## Assumptions and scope
Here \(\mathcal F_\gamma=\{f\text{ entire}:\int_{\mathbb C}|f|^2\,d\mu_\gamma<\infty\}\), and \(P_\beta\) uses the *target* Gaussian measure. All three parameters \(\alpha,\beta,R\) are positive and finite. The disk cutoff makes \(\mathbf1_{\{|z|<R\}}f\in L^2(\mu_\beta)\) for every \(f\in\mathcal F_\alpha\), even when the unrestricted inclusion into \(\mathcal F_\beta\) is unbounded. The monomial-indexed numbers \(a_n\) are the singular values counted with multiplicity before decreasing rearrangement. No statement identifies the ordered \(n\)-th singular value with \(a_n\). The final large-radius formula fixes \(\alpha,\beta\) (equivalently fixes \(u>1\)); it is not uniform as \(u\downarrow1\).

## Proof
**1. Exact diagonalization and compactness.** The normalized monomials \(e_n^\gamma(z)=\sqrt{\gamma^n/n!}\,z^n\) are an orthonormal basis of \(\mathcal F_\gamma\). Angular orthogonality implies
\[
D_{\alpha,\beta,R}e_n^\alpha
=\langle \mathbf1_{\{|z|<R\}}e_n^\alpha,e_n^\beta\rangle_{L^2(\mu_\beta)}e_n^\beta
=u^n\left(\frac1{n!}\int_0^x t^n e^{-t}\,dt\right)e_n^\beta.
\]
Integration by parts gives \(n!^{-1}\int_0^x t^ne^{-t}\,dt=q_n(x)>0\). Hence the exact diagonal transfer. For all \(n\) with \(n+2>x\), bounding successive terms of the Poisson tail gives
\[
0<q_n(x)\le e^{-x}\frac{x^{n+1}}{(n+1)!}\frac{1}{1-x/(n+2)}.
\]
The right side times \(u^n\) is superfactorially summable to every positive power, proving compactness, injectivity and all \(\mathcal S_p\) assertions.

**2. Strict modal staircase.** Put \(p_k(x)=e^{-x}x^k/k!\). For all \(n\ge0\),
\[
\frac{q_n(x)}{p_{n+1}(x)}
=\sum_{j=0}^\infty\frac{x^j}{(n+2)(n+3)\cdots(n+j+1)}.
\]
For \(j=0\) the empty product is one. Each positive-index term decreases strictly with \(n\), hence \(p_{n+1}/q_n\) increases strictly. Since \(q_{n+1}=q_n-p_{n+1}\), the ratio \(q_{n+1}/q_n\) strictly decreases with \(n\). It is positive and tends to zero. Consequently \(a_{n+1}/a_n=u\,q_{n+1}/q_n\) decreases strictly to zero, establishing strict log-concavity and the full ordered sequence of adjacent-mode thresholds. The degree-zero threshold follows from \(q_0=1-e^{-x}\), \(q_1=1-(1+x)e^{-x}\). Expansion as \(x\to\infty\) yields \(r_0(x)^2=1+2xe^{-x}(1+o(1))\). For \(u\le1\), since \(q_{n+1}<q_n\), all \(a_n\) decrease strictly and the norm equals \(q_0\).

**3. Sharp large-radius norm.** Fix \(u>1\), and let \(x\to\infty\). Write \(v=n/x\), \(I(v)=v\log v-v+1\). For \(v\) in any compact subinterval of \((1,\infty)\), Poisson-tail summation and Stirling's formula give the uniform equivalent
\[
q_n(x)=\frac{1+o(1)}{(v-1)\sqrt{2\pi vx}}\exp[-xI(v)].
\]
Indeed, \(q_n/p_n=\sum_{j\ge1}x^j/[(n+1)\cdots(n+j)]\to\sum_{j\ge1}v^{-j}=1/(v-1)\), uniformly away from \(v=1\); Stirling supplies the Gaussian prefactor. Thus
\[
a_n(x,u)=\frac{1+o(1)}{(v-1)\sqrt{2\pi vx}}
\exp\{xF_u(v)\},\qquad F_u(v)=v\log u-I(v).
\]
For \(v>1\), \(F_u\) is strictly concave, with unique maximum at \(v=u\) and \(F_u(u)=u-1\). For \(n\le x\), the elementary bound \(q_n\le1\) yields \(a_n\le\exp(x\log u)\), exponentially smaller than \(\exp[x(u-1)]\). For \(n\ge x\), the Poisson Chernoff bound \(q_n(x)\le\exp[-xI(n/x)]\) bounds \(a_n\le e^{xF_u(n/x)}\). On the complement of every fixed neighborhood of \(u\) in \([1,\infty)\), strict concavity and \(F_u(v)\to-\infty\) as \(v\to\infty\) give a uniform exponential gap. Hence every maximizing \(n_x\) has \(n_x/x\to u\). Within a small fixed neighborhood of \(u\), the uniform equivalent above and \(F_u(v)\le F_u(u)\) show
\[
\limsup_{x\to\infty}(u-1)\sqrt{2\pi ux}\,e^{-x(u-1)}\sup_n a_n\le1.
\]
Choosing \(n=\lfloor ux\rfloor\), for which \(F_u(n/x)=u-1+O(x^{-2})\), proves the corresponding lower bound and the displayed sharp norm equivalent.

**4. Same-weight Toeplitz equivalence.** The unitary \(U:\mathcal F_\alpha\to\mathcal F_\beta\) given by \((Uf)(z)=f(\sqrt{\beta/\alpha}\,z)\) maps monomial basis to monomial basis. Thus \(D_{\alpha,\beta,R}U^{-1}\) is the ordinary positive radial Fock Toeplitz operator with compactly supported symbol
\[
\phi_{u,x}(z)=u^{-1}\exp[(1-u^{-1})\beta|z|^2]\,
\mathbf1_{\{\beta|z|^2\le ux\}}.
\]
Its monomial eigenvalues equal \(u^nq_n(x)\) by the substitution \(t\mapsto ut\). This equivalence is included explicitly because it is relevant when comparing prior Toeplitz theorems.

## Verification
The standalone standard-library Python program `verify.py` checks the Poisson-tail formula against the finite incomplete-gamma expansion, strict modal ratios in numerically resolvable ranges, adjacent-mode ties at exact symbolic threshold ratios, the degree-zero norm in the nonamplifying regime, and convergence to the full sharp prefactor for three fixed mismatches and increasing radii. Run `python3 verify.py`. The program's finite assertions are supplementary only; the proof above establishes the statements for all admissible parameters.

## Relationship to prior work
Kisil (arXiv:2108.13710, first posted 2021-08-31) develops cross-Toeplitz calculus between Gaussian Fock–Segal–Bargmann representations, but the inspected main results address two-sided convolutions and symbol representations, not the displayed disk-truncation modal spectrum or sharp norm asymptotic. Galbis (arXiv:2102.02031, first posted 2021-02-03) proves norm bounds for radial Fock Toeplitz symbols, and Ma–Yan–Zheng–Zhu (arXiv:2603.04051, first posted 2026-03-04) give a sharp norm bound attaining equality for *unweighted* disk indicators. The present formula recovers their ordinary disk value at \(u=1\); the asserted new phenomenon is for different Gaussian weights, or equivalently the growing truncated exponential Toeplitz symbol in step 4. General radial Toeplitz diagonalization is known and is used as an ingredient, not claimed as novel. Existing published results for Gaussian full-space anisotropic Fock projections and for transfers between distinct Landau levels have different kernels and their spectra do not imply the mismatch law for a disk-truncated analytic-to-analytic transfer. The sharp \(x^{-1/2}\) prefactor and exponentially small threshold require the present Poisson-tail and saddle-point analysis.

## Limitations
The result is in one complex dimension, with concentric disk observation and constant Gaussian weights. The large-radius norm equivalent fixes \(u>1\); a joint asymptotic at \(u\downarrow1\) is not asserted. The modal numbers are not the decreasing rearrangement. Other Fock norms, nonradial masks, and higher dimensions are not classified. Explicit statements in the inspected literature do not imply the claimed sharp transfer norm, but a previously unnoticed equivalent radial-symbol calculation remains a historical-priority risk. The result has not received independent validation.

## References
1. V. V. Kisil, *Cross-Toeplitz Operators on the Fock–Segal–Bargmann Spaces and Two-Sided Convolutions on the Heisenberg Group*, arXiv:2108.13710 (first posted 2021-08-31), https://arxiv.org/abs/2108.13710; Ann. Funct. Anal. 14 (2023), article 38, https://doi.org/10.1007/s43034-022-00249-7.
2. A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031 (first posted 2021-02-03), https://arxiv.org/abs/2102.02031.
3. P. Ma, F. Yan, D. Zheng and K. Zhu, *Localization operators on Bergman and Fock spaces*, arXiv:2603.04051 (first posted 2026-03-04), https://arxiv.org/html/2603.04051.
4. X. Fang and P. T. Tien, *Fock Projections between Gaussian Mixed-Norm Spaces: Full-Range Boundedness and Compactness*, arXiv:2610.41461 (first posted 2026-10-30), https://arxiv.org/abs/2610.41461. Its full text was not available for inspection in this review.
5. K. Esmeral García and E. A. Maximenko, *Constructive approximation of convergent sequences by eigenvalue sequences of radial Toeplitz–Fock operators*, arXiv:2503.23276 (first posted 2025-03-30), https://arxiv.org/abs/2503.23276.
