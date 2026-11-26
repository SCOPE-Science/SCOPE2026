# Angular Fourier Hessian of Fock Toeplitz Ky Fan sums

## Finding
Let \(N\ge2\) be an integer and let \(s>0\). For a real smooth function \(h\) on the circle with zero mean, consider the exactly area-preserving star-shaped perturbation
\[
\Omega_{\varepsilon,h}=\{r e^{i\theta}:\pi r^2<s+\varepsilon h(\theta)\},
\qquad \varepsilon\in\mathbb R,\quad |\varepsilon|\|h\|_\infty<s.
\]
Write \(\Sigma_N(\Omega)\) for the sum of the \(N\) largest eigenvalues of the Fock Toeplitz operator \(T_{\mathbf1_\Omega}\). Set
\[
b_j(s)=e^{-s}\frac{s^j}{j!},\qquad
\widehat h_m=\frac1{2\pi}\int_0^{2\pi}h(\theta)e^{-im\theta}\,d\theta.
\]
For every \(m\ge1\), define the **angular Hessian coefficient**
\[
L_{N,m}(s)=b_{N-1}(s)-
\sum_{j=\max(0,N-m)}^{N-1}
\frac{b_j(s)b_{j+m}(s)}{\sum_{r=j+1}^{j+m}b_r(s)}.
\]
Then the full area-constrained second variation is diagonal in angular Fourier modes:
\[
\boxed{\quad
\Sigma_N(D_s)-\Sigma_N(\Omega_{\varepsilon,h})
=\varepsilon^2\sum_{m\ge1}L_{N,m}(s)|\widehat h_m|^2
+O_{N,s,h}(\varepsilon^3).\quad}
\]
Here \(D_s=\{z:\pi|z|^2<s\}\). The first angular coefficient vanishes exactly, \(L_{N,1}(s)=0\), as required by translation symmetry. The first genuine shape mode has the **strictly positive, closed-form curvature**
\[
\boxed{\quad L_{N,2}(s)
=\frac{e^{-s}s^{N-1}}{(N-1)!}
\frac{2s+N+1}{(s+N)(s+N+1)}>0.\quad}
\]
In particular, for the quadrupolar domains \(\Omega_\varepsilon=\{r e^{i\theta}:\pi r^2<s+\varepsilon\cos(2\theta)\}\),
\[
\boxed{\quad
\Sigma_N(D_s)-\Sigma_N(\Omega_\varepsilon)
=\frac{\varepsilon^2 e^{-s}s^{N-1}(2s+N+1)}
{4(N-1)!(s+N)(s+N+1)}+O_{N,s}(\varepsilon^4).\quad}
\]
The same identities also hold at \(N=1\); the rank-\(N\) statement above emphasizes \(N\ge2\).

## Assumptions and scope
The Fock Hilbert space is
\[
\mathcal F^2(\mathbb C)=\left\{f\text{ entire}:\int_\mathbb C|f(z)|^2e^{-\pi|z|^2}\,dA(z)<\infty\right\},
\]
with orthonormal monomials \(e_j(z)=(\pi^j/j!)^{1/2}z^j\). The positive compact Toeplitz operator \(T_{\mathbf1_\Omega}\) is defined by its quadratic form \(\langle T_{\mathbf1_\Omega}f,f\rangle=\int_\Omega|f(z)|^2e^{-\pi|z|^2}\,dA(z)\). It is trace class for finite-area \(\Omega\). Smoothness is assumed only to make the Fourier-series expansion and trace-norm Taylor remainder immediate; the assertion is local as \(\varepsilon\to0\) at fixed positive \(s\) and fixed \(N\). Since \(t=\pi r^2\) gives \(dA=dt\,d\theta/(2\pi)\), the mean-zero condition makes \(|\Omega_{\varepsilon,h}|=s\) exactly for all allowed \(\varepsilon\).

## Proof
**1. Disc spectrum and spectral gap.** In the monomial basis the disc operator is diagonal, with eigenvalues indexed from zero by
\[
\lambda_j(s)=\frac1{j!}\int_0^s e^{-t}t^j\,dt
=1-e^{-s}\sum_{r=0}^j\frac{s^r}{r!}.
\]
They are strictly decreasing, since \(\lambda_j(s)-\lambda_{j+1}(s)=b_{j+1}(s)>0\). Thus the top-\(N\) spectral subspace is separated from the rest by the positive gap \(b_N(s)\). More generally,
\[
\lambda_j(s)-\lambda_{j+m}(s)=\sum_{r=j+1}^{j+m}b_r(s)>0.
\]

**2. Trace-norm shape derivatives.** Let \(A(\varepsilon)=T_{\mathbf1_{\Omega_{\varepsilon,h}}}\), and write \(A_{jk}(\varepsilon)=\langle A(\varepsilon)e_k,e_j\rangle\). Direct polar integration yields
\[
A_{jk}(\varepsilon)=\frac1{2\pi\sqrt{j!k!}}\int_0^{2\pi}e^{i(k-j)\theta}
\int_0^{s+\varepsilon h(\theta)}e^{-t}t^{(j+k)/2}\,dt\,d\theta.
\]
For \(t\) in a compact interval about \(s>0\), the rank-one coherent-state density \(|k_{\sqrt{t/\pi}e^{i\theta}}\rangle\langle k_{\sqrt{t/\pi}e^{i\theta}}|\) has bounded derivatives in trace norm of any fixed order. Hence integrating its variable upper limit gives a trace-norm \(C^4\) family near \(\varepsilon=0\); all matrix differentiations below are legitimate. In particular,
\[
A'_{jk}(0)=\sqrt{b_j(s)b_k(s)}\,\widehat h_{j-k},
\qquad
A''_{jj}(0)=b_j'(s)\frac1{2\pi}\int_0^{2\pi}h(\theta)^2\,d\theta.
\]
The Poisson recurrence \(b_j'(s)=b_{j-1}(s)-b_j(s)\), with \(b_{-1}(s)=0\), gives
\[
\sum_{j=0}^{N-1}A''_{jj}(0)
=-b_{N-1}(s)\frac1{2\pi}\int_0^{2\pi}h(\theta)^2\,d\theta.
\]

**3. Ky Fan spectral perturbation.** Because of the gap established in step 1, the Riesz projection onto the top \(N\) eigenvalues varies \(C^4\) in trace norm, and so does their sum \(\Sigma_N(\Omega_{\varepsilon,h})\). Differentiation of the Riesz-projection contour formula (or ordinary second-order perturbation, with cancellations among pairs both inside the top block) gives
\[
\frac{d^2}{d\varepsilon^2}\Sigma_N(\Omega_{\varepsilon,h})\bigg|_{\varepsilon=0}
=\sum_{j<N}A''_{jj}(0)
+2\sum_{j<N}\sum_{k\ge N}
\frac{|A'_{jk}(0)|^2}{\lambda_j(s)-\lambda_k(s)}.
\]
For completeness: the contour formula for the isolated top spectral projection is \(P(\varepsilon)=(2\pi i)^{-1}\oint(z-A(\varepsilon))^{-1}\,dz\). Differentiating \(\operatorname{Tr}(A(\varepsilon)P(\varepsilon))\), expanding the diagonal resolvent of \(A(0)\) and evaluating residues gives the displayed expression; terms involving \(j,k<N\) cancel pairwise, while only \(j<N\le k\) survive. The first derivative equals \(\sum_{j<N}b_j(s)\widehat h_0=0\).

**4. Fourier diagonalization.** For real zero-mean \(h\), Parseval gives \((2\pi)^{-1}\int h^2=2\sum_{m\ge1}|\widehat h_m|^2\). Substituting step 2 into step 3, grouping the pairs \(k=j+m\ge N\), and using the positive differences in step 1 yields precisely the coefficients \(L_{N,m}(s)\) and the claimed second-order expansion. The infinite series converges absolutely: \(h\) has rapidly decaying Fourier coefficients, and for fixed \(N,s\) each coefficient is bounded uniformly in \(m\); for instance the summands are bounded by \(b_j(s)\) because the denominator includes \(b_{j+m}(s)\).

**5. The translation and quadrupole modes.** For \(m=1\), only \(j=N-1\) contributes, and
\[
\frac{b_{N-1}(s)b_N(s)}{\lambda_{N-1}(s)-\lambda_N(s)}=b_{N-1}(s),
\]
so \(L_{N,1}(s)=0\). For \(m=2\), use the elementary Poisson identity
\[
\frac{b_j(s)b_{j+2}(s)}{b_{j+1}(s)+b_{j+2}(s)}
=\frac{s}{s+j+2}b_j(s).
\]
Only \(j=N-2,N-1\) can occur (omit the negative index when \(N=1\)). Using \(b_{N-2}(s)=\frac{N-1}{s}b_{N-1}(s)\) for \(N\ge2\) gives
\[
L_{N,2}(s)=b_{N-1}(s)\left[1-\frac{N-1}{s+N}-\frac{s}{s+N+1}\right]
=b_{N-1}(s)\frac{2s+N+1}{(s+N)(s+N+1)}.
\]
For \(h(\theta)=\cos(2\theta)\), the only nonzero positive-frequency Fourier coefficient is \(\widehat h_2=1/2\). Rotating the domain by \(\pi/2\) exchanges \(\varepsilon\) and \(-\varepsilon\), so its Ky Fan sum is even. The trace-norm \(C^4\) dependence then improves the general cubic remainder to \(O(\varepsilon^4)\). This proves the claimed exact positive curvature.

## Verification
The included standard-library script `verify.py` evaluates the Poisson identities with exact rational arithmetic for multiple ranks, areas, and angular frequencies. It checks the translation coefficient \(L_{N,1}=0\), the exact rational quadrupole coefficient, and the nonzero spectral differences. The optional independent finite-matrix numerical script `check_numeric.py` integrates the perturbed Fock Toeplitz matrix using SciPy and checks convergence of the normalized deficit to the analytical coefficient. Both scripts verify finite identities, not infinite-dimensional completeness; the trace-norm and spectral perturbation proof above establishes the full theorem.

## Relationship to prior work
Abreu's July 2026 Fock-space Ky Fan isoperimetric theorem [1] proves the global bound \(\Sigma_N(\Omega)\le\Sigma_N(D_s)\) and supplies the disc eigenvalue formula. The new result concerns a different, more quantitative assertion: the complete second shape derivative at a disc and the exact positive quadrupolar coefficient for all ranks \(N\ge2\). The global inequality alone yields only the sign of possible second derivatives, not the explicit Fourier coefficients. Nicola, Riccardi, and Tilli [2] treated radial sets, which do not contain the nonradial Fourier perturbations calculated here; [3] proves existence of maximizers. The established quantitative concentration stability result [4] concerns the rank-one setting and is not asserted here to be new. The full text of [1] was inspected, including its theorem, proof and references; [2] and [3] were compared using their public statements and bibliographic descriptions, with incomplete full-text access recorded as a residual priority for independent checking.

## Limitations
This is a local, fixed-\(N\), fixed-area theorem. It does not prove global uniqueness of discs, a uniform quantitative stability inequality, or strict positivity of \(L_{N,m}\) at every \(m\ge3\). In fact the already known global isoperimetric inequality implies their nonnegativity but not the exact value. The quadratic-order asymptotics do not control finite deformations without remainder bounds. No claim of independent verification or comprehensive novelty certification is made. Some related papers could not be inspected in full, and the formula should be checked against additional spectral shape-derivative literature before publication.

## References
1. L. D. Abreu, *The isoperimetric inequality for the Ky Fan norm*, arXiv:2607.28376 (first public version July 30, 2026), https://arxiv.org/abs/2607.28376 .
2. F. Nicola, F. Riccardi, P. Tilli, *The Faber–Krahn inequality for partial sums of eigenvalues of Toeplitz operators*, arXiv:2503.07069 (first public version March 10, 2025), https://arxiv.org/abs/2503.07069 .
3. F. Nicola, F. Riccardi, P. Tilli, *On the existence of extremizers for the sum of eigenvalues of Toeplitz operators*, arXiv:2607.20965 (first public version July 23, 2026), https://arxiv.org/abs/2607.20965 .
4. J. Gómez, A. Guerra, J. P. G. Ramos, P. Tilli, *Stability of the Faber–Krahn inequality for the short-time Fourier transform*, Invent. Math. 236 (2024), 779–836.
