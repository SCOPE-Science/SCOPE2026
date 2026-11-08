# Gaussian-mixture Fock kernels: global zeros under smooth positive-curvature perturbations

## Finding
Let \(d\ge 1\), \(0<a<b\), and \(0<\varepsilon<1\). On \(\mathbb C^d\) consider the probability measure
\[
d\nu_\varepsilon=(1-\varepsilon)(a/\pi)^d e^{-a|z|^2}\,dV+\varepsilon(b/\pi)^d e^{-b|z|^2}\,dV.
\]
Its entire-function \(L^2\) reproducing kernel is \(K_\varepsilon(z,w)=F_\varepsilon(\langle z,w\rangle)\), where
\[
F_\varepsilon(t)=\sum_{n=0}^\infty\frac{t^n}{n![(1-\varepsilon)a^{-n}+\varepsilon b^{-n}]}.
\]
For **every** nontrivial mixture \(0<\varepsilon<1\), the entire function \(F_\varepsilon\) has infinitely many complex zeros. Both endpoint Gaussian kernels are zero-free.

Put \(r=a/b\), \(q=\varepsilon/(1-\varepsilon)\), and let \(R_\varepsilon\) be the modulus of the nearest zero of \(F_\varepsilon\). As \(\varepsilon\downarrow0\), there is a simple negative real zero \(t_\varepsilon\) with
\[
a t_\varepsilon=\frac{\log q-q^{1-r}+O_r(q^{2(1-r)})}{1-r},
\qquad
R_\varepsilon=\frac{\log(1/\varepsilon)}{a(1-r)}+O_{a,b}(1).
\]
Thus the first kernel zero escapes at a sharp logarithmic rate under an arbitrarily small admixture of a faster-decaying Gaussian.

Moreover, after removing its irrelevant additive normalization constant, the negative logarithm of the mixture density converges to \(a|z|^2\) in uniform \(C^m(\mathbb C^d)\) for every fixed nonnegative integer \(m\). For all sufficiently small positive \(\varepsilon\), its complex Hessian is bounded below by \((a/2)I\) throughout \(\mathbb C^d\). Hence global reproducing-kernel zero-freeness is not stable even among smooth uniformly strictly plurisubharmonic Gaussian-near weights.

## Assumptions and scope
The monomial multiindex notation is \(|\alpha|=\sum_j\alpha_j\), \(\alpha!=\prod_j\alpha_j!\). The Hermitian product is \(\langle z,w\rangle=\sum_j z_j\overline{w_j}\). All zero statements concern the **off-diagonal reproducing kernel**; its diagonal is strictly positive. Every scalar \(t\in\mathbb C\) is realized as \(\langle z,w\rangle\) in \(\mathbb C^d\). The error constants may depend on the fixed Gaussian parameters and dimension but not on \(\varepsilon\). The zero-location estimates apply as \(\varepsilon\downarrow0\), whereas infinitude of zeros applies for every \(0<\varepsilon<1\).

## Proof
### 1. Kernel and growth
For every multiindex \(\alpha\), Gaussian integration gives
\[
\|z^\alpha\|_{L^2(\nu_\varepsilon)}^2
=\alpha![(1-\varepsilon)a^{-|\alpha|}+\varepsilon b^{-|\alpha|}].
\]
Angular invariance makes distinct monomials orthogonal. Polynomial Taylor truncations converge in the holomorphic \(L^2\) space by angular orthogonality and Parseval; summing the reciprocal squared norms by total degree gives the displayed kernel series. Its coefficients are positive, and
\[
|F_\varepsilon(t)|\leq (1-\varepsilon)^{-1}e^{a|t|}.
\]
Write \(b_n=n![t^n]F_\varepsilon\). Then
\[
\frac{b_{n+1}}{b_n}\longrightarrow a,
\qquad
\frac{b_n}{a^n}\longrightarrow\frac1{1-\varepsilon}.
\]
If \(F_\varepsilon\) had finitely many zeros, the order-one case of the classical Hadamard factorization theorem would give \(F_\varepsilon(t)=P(t)e^{At+B}\) for a polynomial \(P\). The eventual nonvanishing Taylor coefficients rule out \(A=0\). Expanding this expression and taking ratios of its factorially scaled coefficients forces \(A=a\). Their convergence to a finite nonzero multiple of \(a^n\) forces \(\deg P=0\). Hence \(F_\varepsilon(t)=Ce^{at}\). Since \(F_\varepsilon(0)=1\), we have \(C=1\), contradicting the second displayed coefficient limit for \(0<\varepsilon<1\). Therefore infinitely many zeros exist. For \(\varepsilon=0\) and \(\varepsilon=1\), the kernel is respectively \(e^{a\langle z,w\rangle}\) and \(e^{b\langle z,w\rangle}\), which are zero-free.

### 2. Quantitative first-zero scale
For \(q<1\), expansion of the moment denominator gives the locally uniformly convergent exponential series
\[
(1-\varepsilon)F_\varepsilon(t)=H_q(at),
\qquad H_q(z)=\sum_{k=0}^\infty(-q)^k e^{r^k z}.
\]
Let \(L=\log(1/q)\), \(s_k=(1-r^k)/(1-r)\), and \(h_q(z)=e^{-z}H_q(z)\). Since \(k-s_k\ge(k-1)(1-r)\) for all \(k\ge1\), for each fixed \(C>0\) and all \(\operatorname{Re}z\ge-L/(1-r)+C\),
\[
|h_q(z)-1|\leq\sum_{k\ge1}q^{k-s_k}e^{-(1-r^k)C}
\leq\frac{e^{-(1-r)C}}{1-q^{1-r}}.
\]
Choose \(C=\log 4/(1-r)\) and \(q\) sufficiently small. The bound is at most \(1/2\). Thus every zero \(z\) of \(H_q\) satisfies \(\operatorname{Re}z<-L/(1-r)+C\), so \(|z|\ge L/(1-r)-C\).

Set \(z_0=\log q/(1-r)=-L/(1-r)\), which is real. For bounded complex \(u\),
\[
h_q(z_0+u)=1-e^{-(1-r)u}+E_q(u),
\qquad
E_q(u)=\sum_{k\ge2}(-q)^k e^{(r^k-1)(z_0+u)}.
\]
The remainder and its derivative are \(O_r(q^{1-r})\) uniformly for \(|u|\le1\). On the circle \(|u|=K_r q^{1-r}\), with fixed sufficiently large \(K_r\), the first two terms dominate the remainder. Rouché's theorem gives exactly one zero \(u_q\) in this circle. Its conjugate is another zero in the same circle; uniqueness therefore implies that \(u_q\) is real. Its derivative is \((1-r)+O_r(q^{1-r})\), so the zero is simple. Finally,
\[
E_q(0)=q^{1-r}+O_r(q^{(1-r)(2+r)}),
\qquad
u_q=-\frac{q^{1-r}}{1-r}+O_r(q^{2(1-r)}),
\]
where \(u_q=\nu_q\). Dividing \(z_0+u_q\) by \(a\) gives the stated real zero expansion. Combined with the half-plane zero exclusion, this yields \(R_\varepsilon=L/[a(1-r)]+O_{a,b}(1)\), and \(L=\log(1/\varepsilon)+O(\varepsilon)\).

### 3. Smooth positive-curvature proximity
Set \(\Delta=b-a>0\), \(\eta=q(b/a)^d\), and \(s=|z|^2\). Up to a scalar factor, the mixture density equals \(e^{-\Phi_\varepsilon(z)}\), where
\[
\Phi_\varepsilon(z)=as-\log(1+\eta e^{-\Delta s}).
\]
With \(p(s)=\eta e^{-\Delta s}/(1+\eta e^{-\Delta s})\), the tangential complex-Hessian eigenvalues are \(a+\Delta p(s)\), and the radial eigenvalue is \(a+\Delta p(s)-\Delta^2s p(s)(1-p(s))\). Therefore every eigenvalue is at least
\[
a-\Delta^2\eta \sup_{s\ge0}s e^{-\Delta s}=a-\Delta\eta/e.
\]
For small \(\varepsilon\) this exceeds \(a/2\). Repeated real partial derivatives of \(\Phi_\varepsilon-a|z|^2\) are bounded by \(O_{m,a,b,d}(\eta)\) because derivatives of \(e^{-\Delta |z|^2}\) are polynomial-times-Gaussian and \(\eta\to0\). This proves uniform \(C^m\) convergence of the normalized potentials.

## Verification
`CHECK.py` uses only the Python standard library. It compares the moment-series and exponential-series kernel representations, tests exact rational monomial moments, brackets the predicted simple real zero and measures its displacement for several small mixture weights, and checks numerical Hessian bounds against the analytic lower estimate. It is a finite consistency test; Hadamard factorization, Rouché's theorem, and the global curvature inequality are the infinite-dimensional proof.

## Relationship to prior work
Liu, Wang, and Zeng (2026) prove global off-diagonal upper and **near-diagonal** lower kernel estimates for a class of weighted Fock spaces. Their Theorem 1.2 does not supply a global zero-free statement or a logarithmic first-zero location; the present construction illustrates the distinction. Marzo and Ortega-Cerdà (2008/2009) derive off-diagonal decay bounds in one complex variable, without classifying global kernel zeros of Gaussian mixtures. Zeytuncu (2010) studies kernel zeros for bounded radial disk weights, a different domain and weight geometry. The 2026 weighted-Fock-kernel estimates of Hu, Lv, and Schuster are a plausible nearby source; only their abstract was accessible and no complete negative claim about their text is made. The elementary Gaussian moment and Hadamard ingredients are classical. The new point asserted here is their combined complete nontrivial-mixture zero instability with a sharp logarithmic escape law under uniform smooth curvature control.

## Limitations
The zero count is proved infinite but no global angular distribution of those zeros is claimed. A simple negative real zero is localized only in the small-mixture limit, not for every mixture parameter. The nearest-zero estimate has an additive \(O(1)\) uncertainty; the explicit sharper expansion applies to a specified real zero, not necessarily the global nearest zero. The result concerns a two-Gaussian probability mixture and does not classify arbitrary radial or nonradial Fock weights. Publication priority requires broader expert verification, especially of historical zero-theoretic work and the inaccessible complete 2026 comparison paper.

## References
1. G. Liu, X. Wang, Z. Zeng, *Bergman Kernels and Hankel Operators on Weighted Fock Spaces in Several Complex Variables*, arXiv:2609.26810 (first public 2026-09-16), https://arxiv.org/abs/2609.26810.
2. J. Marzo, J. Ortega-Cerdà, *Pointwise estimates for the Bergman kernel of the weighted Fock space*, arXiv:0810.0388 (2008), https://arxiv.org/html/0810.0388v1.
3. Y. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, arXiv:1009.2806 (2010), https://arxiv.org/html/1009.2806v1.
4. Z. Hu, X. Lv, A. P. Schuster, *Reproducing kernel functions in weighted Fock spaces*, Ann. Funct. Anal. 17 (2026), DOI:10.1007/s43034-026-00533-w (abstract examined; complete text not accessed).
