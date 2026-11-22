# Diophantine Sobolev thresholds for compactly supported circle tent kernels

## Finding
On the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), set \(d(t)=\min_{m\in\mathbb Z}|t-2\pi m|\) and, for \(0<c\le\pi\), \(k_c(t)=(c-d(t))_+\). Let \(\mathcal H_c\) be the reproducing-kernel Hilbert space of the translation-invariant kernel \(K_c(x,y)=k_c(x-y)\), with \(L^2\) and Fourier coefficients normalized by \(dt/(2\pi)\). Put \(\alpha=c/(2\pi)\). The following classification is exact.

**Rational supports.** If \(\alpha=p/q\) in lowest terms, \(\mathcal H_c\) consists exactly of the functions in \(H^1(\mathbb T)\) whose Fourier coefficients vanish at every nonzero multiple of \(q\), with equivalent \(H^1\) and RKHS norms on this subspace. The kernel is positive semidefinite but neither strictly positive definite on distinct sites nor universal for continuous functions.

**Irrational supports.** If \(\alpha\) is irrational, the kernel is strictly positive definite and \(C(\mathbb T)\)-universal, and \(\mathcal H_c\) is a proper dense subspace of \(H^1(\mathbb T)\). More precisely, for each real \(s\ge0\),
\[
\boxed{\quad H^s(\mathbb T)\hookrightarrow\mathcal H_c\quad\Longleftrightarrow\quad\inf_{n\ge1}n^{s-1}\|n\alpha\|_{\mathbb R/\mathbb Z}>0.\quad}
\]
Here the arrow means continuous inclusion, and \(\|u\|_{\mathbb R/\mathbb Z}=\min_{k\in\mathbb Z}|u-k|\). Consequently, if the irrationality exponent is \(\mu(\alpha)\in[2,\infty]\), inclusion fails for every finite \(s<\mu(\alpha)\), holds for every \(s>\mu(\alpha)\), and at the critical exponent \(s=\mu(\alpha)<\infty\) holds **if and only if** \(\inf_n n^{\mu(\alpha)-1}\|n\alpha\|>0\). In particular, for badly approximable \(\alpha\), \(H^2\hookrightarrow\mathcal H_c\), whereas for Liouville \(\alpha\) there is no continuous inclusion \(H^s\hookrightarrow\mathcal H_c\) for any finite \(s\).

**Exact cohomological interpretation.** For irrational \(\alpha\), a function \(f\in H^1(\mathbb T)\) belongs to \(\mathcal H_c\) precisely when there is a unique mean-zero \(g\in L^2(\mathbb T)\) with
\[
f'(t)=g(t)-g(t+c)\quad\text{in distributions}.
\]
The norm is exactly
\[
\boxed{\quad\|f\|_{\mathcal H_c}^2=\frac{2\pi}{c^2}|\widehat f(0)|^2+2\pi\|g\|_{L^2}^2.\quad}
\]
Thus the native-space regularity transition is the small-divisor obstruction for the rotation coboundary equation.

## Assumptions and scope
Use Fourier coefficients \(\widehat f(n)=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)e^{-int}\,dt\). The spectral weight at each integer is \(a_n=(2\pi)^{-1}\int_{-\pi}^{\pi}k_c(t)e^{-int}\,dt\); an RKHS member must have zero coefficients where \(a_n=0\), and its squared norm is \(\sum_{a_n>0}|\widehat f(n)|^2/a_n\). Periodic \(H^s\) has norm squared \(\sum_n(1+n^2)^s|\widehat f(n)|^2\). Positive definiteness is understood on all finite distinct-site configurations; universality means uniform density of the RKHS in complex continuous functions. For irrational \(\alpha\), \(\mu(\alpha)=\sup\{r:|\alpha-p/q|<q^{-r}\text{ for infinitely many coprime }p,q\}\), allowing infinity.

## Proof
**Fourier spectrum.** Integrating the triangle exactly gives
\[
a_0=\frac{c^2}{2\pi},\qquad a_n=\frac{1-\cos(nc)}{\pi n^2}=\frac{|1-e^{inc}|^2}{2\pi n^2},\quad n\ne0.
\]
All weights are nonnegative. Fourier-Bochner positivity follows from absolute convergence. In particular \(a_n=0\) for nonzero \(n\) if and only if \(n\alpha\in\mathbb Z\).

**Rational dichotomy.** For \(\alpha=p/q\), the nonzero forbidden frequencies are exactly multiples of \(q\). On allowed residue classes, \(1-\cos(2\pi np/q)\) has a positive minimum and finite maximum; hence \(a_n\asymp_q n^{-2}\), yielding the stated exact Fourier-support characterization and norm equivalence. Trigonometric characters at the forbidden modes are outside the RKHS, so it is not universal. To witness failure of strict positive definiteness, take two disjoint orbits \(\{x+2\pi j/q:0\le j<q\}\) and \(\{y+2\pi j/q:0\le j<q\}\), with nonzero weights \(+1\) and \(-1\), respectively. All allowed-frequency Fourier sums vanish, including at frequency zero. Therefore the Gram quadratic form vanishes for a nonzero vector on distinct sites.

**Irrational spectral density and strictness.** For irrational \(\alpha\), every \(a_n\) is positive. Finite trigonometric polynomials lie in \(\mathcal H_c\), hence the RKHS is dense in \(C(\mathbb T)\). If a nonzero finite atomic measure had zero Gram energy, every Fourier coefficient of that measure would vanish by positivity of all \(a_n\), contradicting uniqueness of Fourier coefficients of finite measures. Thus strict positive definiteness holds. Since \(a_n\le2/(\pi n^2)\), membership in \(\mathcal H_c\) implies \(H^1\). Density in \(H^1\) holds because finite trigonometric polynomials belong to \(\mathcal H_c\). The inclusion is proper: density of irrational rotations provides a subsequence of distinct \(n_j\to\infty\) with \(n_j^2a_{n_j}<2^{-2j}\). Defining \(\widehat f(n_j)=\sqrt{a_{n_j}}\), all other Fourier coefficients zero, gives \(\sum n_j^2|\widehat f(n_j)|^2<\infty\), but \(\sum|\widehat f(n_j)|^2/a_{n_j}=\sum1=\infty\).

**Sharp Sobolev inclusion.** For irrational \(\alpha\), the inclusion \(H^s\hookrightarrow\mathcal H_c\) is bounded precisely when the spectral diagonal ratio \(\sup_n[(1+n^2)^s a_n]^{-1}\) is finite; this is both necessary (single Fourier characters) and sufficient (weighted Parseval). For all real \(u\),
\[
8\|u\|_{\mathbb R/\mathbb Z}^2\le |1-e^{2\pi iu}|^2\le4\pi^2\|u\|_{\mathbb R/\mathbb Z}^2.
\]
Combining these with the spectrum gives exactly the boxed infimum condition, including the finitely many low frequencies. The identity \(\mu(\alpha)=1+\limsup_{n\to\infty}[-\log\|n\alpha\|]/\log n\) proves the strict inequalities in \(s\) and identifies the critical endpoint. For badly approximable \(\alpha\), \(\inf_n n\|n\alpha\|>0\) by definition. For Liouville numbers the limsup is infinite, so every fixed \(s\) violates the infimum condition.

**Coboundary isometry.** Write \(U_c g(t)=g(t+c)\), so its \(n\)-th Fourier multiplier is \(e^{inc}\). For mean-zero \(f\in H^1\), the distributional equation \(f'=(I-U_c)g\) has the unique formal mean-zero solution \(\widehat g(n)=in\widehat f(n)/(1-e^{inc})\), \(n\ne0\). This solution lies in \(L^2\) exactly when \(\sum_{n\ne0}|\widehat f(n)|^2/a_n<\infty\). Parseval gives \(\sum_{n\ne0}|\widehat f(n)|^2/a_n=2\pi\sum_{n\ne0}|\widehat g(n)|^2\); the constant coefficient contributes \(2\pi|\widehat f(0)|^2/c^2\). This proves the exact range and norm claims.

## Verification
The accompanying standalone `verify.py` checks the Fourier spectrum against analytic integration at rational support and high-precision numerical integration at an irrational support, constructs a vanishing Gram quadratic form from disjoint rational rotation orbits, verifies the exact coboundary spectral norm on a finite Fourier polynomial, and tests two continued-fraction regimes. These finite calculations are diagnostics only; the infinite-dimensional and Diophantine assertions follow from the proof.

## Relationship to prior work
Gneiting's circle Pólya criterion already proves positivity of convex nonincreasing geodesic profiles and strict positivity away from piecewise linearity; neither the basic positivity of a tent nor the general Fourier-RKHS spectral norm is claimed as new. Steinert and coauthors give general harmonic-spectral universality and native-space methods, primarily for symmetric spaces of noncompact type. An earlier calculation for **asymmetric triangular densities on the real line** gives an exact Diophantine conditioning exponent for their Fourier transforms, but concerns a different object and real-frequency transform, not the discrete native space of the compact-circle geodesic tent. The contribution here is the complete rational/irrational native-space and finite-site classification, an exact rotation-coboundary isometry, and the sharp all-Sobolev-space inclusion frontier including its arithmetic endpoint.

## Limitations
The Sobolev-inclusion statement does not assert the reverse inclusion \(\mathcal H_c\subset H^s\) for \(s>1\); indeed its top regularity is uniformly \(H^1\). Spectral coefficients at irrational supports can approach zero arbitrarily rapidly depending on Diophantine approximation. The result does not provide bounded inverse rotation cohomology on all of \(L^2\), nor a finite-site Gram condition-number estimate. Known cohomological-equation and small-divisor literature may contain equivalent RKHS interpretations not located in the sources examined; independent assessment remains necessary.

## References
1. T. Gneiting, “Strictly and non-strictly positive definite functions on spheres,” *Bernoulli* **19** (2013), 1327–1349; arXiv:1111.7077, especially §4.2, Theorem 4. https://arxiv.org/abs/1111.7077
2. F. Steinert et al., “Universal kernels via harmonic analysis on Riemannian symmetric spaces,” arXiv:2506.19245, first public 24 June 2025, especially §§3.1–3.2. https://arxiv.org/abs/2506.19245
3. D. K. Dimitrov and Y. Xu, “Wronskians of Fourier and Laplace Transforms,” arXiv:1606.05011, especially the symmetric triangular Fourier transform in Proposition 2.15 and §4. https://arxiv.org/abs/1606.05011
4. Standard irrationality-exponent/continued-fraction identity and Fourier uniqueness on the circle; used as classical input.
