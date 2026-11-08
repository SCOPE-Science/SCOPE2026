# Radial Fock Toeplitz phase-speed transition: filtered spectra and all-Schatten collapse

## Finding
Let \(d\ge1\) be an integer, let \(\beta>0\), and take a real, strictly positive, nonconstant trigonometric polynomial
\[
p(\theta)=\sum_{m=-M}^{M}c_m e^{im\theta},\qquad c_{-m}=\overline{c_m},\quad \min_\theta p(\theta)>0.
\]
On standard Gaussian Fock space \(\mathcal F_d\), let \(T_\beta\) be the Toeplitz operator with bounded radial symbol \(a_\beta(z)=p(|z|^\beta)\). Define the average \(\bar p=c_0\) and the Gaussian Fourier filter
\[
(Hp)(\theta)=\sum_{m=-M}^M c_m e^{-m^2/8}e^{im\theta}.
\]
Then, for the Fredholm essential spectrum,
\[
\boxed{\sigma_{\mathrm{ess}}(T_\beta)=
\begin{cases}
[\min p,\max p],&0<\beta<1,\\
[\min Hp,\max Hp],&\beta=1,\\
\{\bar p\},&\beta>1.
\end{cases}}
\]
The middle interval is strictly smaller than the first in the sense that \(\min Hp>\min p\) and \(\max Hp<\max p\) (strict heat-kernel averaging for nonconstant \(p\)). There is a sharp centered compactness and operator-ideal transition:
\[
\boxed{T_\beta-\bar p I\in\bigcap_{s>0}\mathcal S_s\quad\text{if }\beta>1,\qquad
T_\beta-\bar p I\text{ is noncompact if }0<\beta\le1.}
\]
For each \(N\ge0\), write \(\lambda_n(\beta)\) for the eigenvalue of \(T_\beta\) in total homogeneous degree \(n\), and define the probability measure
\[
\nu_N=\binom{N+d}{d}^{-1}\sum_{n=0}^{N}\binom{n+d-1}{d-1}\delta_{\lambda_n(\beta)}.
\]
These empirical measures converge weakly, respectively, to \(p_*m_{\mathbb T}\), \((Hp)_*m_{\mathbb T}\), and \(\delta_{\bar p}\), where \(m_{\mathbb T}\) is normalized Haar measure on the circle. In the concrete case \(p(\theta)=2+\cos\theta\), the three essential spectra are \([1,3]\), \([2-e^{-1/8},2+e^{-1/8}]\), and \(\{2\}\); the first two limiting spectral distributions are the corresponding arcsine laws.

## Assumptions and scope
The Hilbert space is
\[
\mathcal F_d=\left\{f:\mathbb C^d\to\mathbb C\text{ entire}:\ \|f\|^2=\pi^{-d}\int_{\mathbb C^d}|f(z)|^2e^{-|z|^2}\,dV(z)<\infty\right\}.
\]
The Toeplitz operator is \(T_\beta f=P(a_\beta f)\) with \(P\) the orthogonal Fock projection. It is bounded, self-adjoint and positive because \(p\) is positive. For \(0<s<1\), \(\mathcal S_s\) denotes the usual Schatten quasi-ideal defined by summability of the \(s\)-th powers of singular values. Each complex dimension is fixed before the asymptotic limit; no uniformity in \(d\) is claimed. The symbol class is deliberately restricted to trigonometric polynomials, so all Fourier manipulations below are finite sums.

## Proof
**1. Exact diagonalization.** The normalized monomials \(e_\alpha(z)=z^\alpha/\sqrt{\alpha!}\), \(\alpha\in\mathbb N_0^d\), form an orthonormal basis. Radiality gives \(\langle T_\beta e_\alpha,e_\gamma\rangle=0\) when \(\alpha\ne\gamma\). For total degree \(n=|\alpha|\), polar integration gives
\[
\lambda_n(\beta)=\frac1{\Gamma(n+d)}\int_0^\infty p(t^{\beta/2})t^{n+d-1}e^{-t}\,dt
=\mathbb E\,p(U_q^\gamma),\qquad q=n+d,\quad \gamma=\beta/2,
\]
where \(U_q\) has Gamma distribution of shape \(q\) and unit scale. The multiplicity is \(m_n=\binom{n+d-1}{d-1}\). Its characteristic integral at Fourier frequency \(m\in\mathbb Z\) is \(I_{q,m}=\mathbb E e^{imU_q^\gamma}\), with \(I_{q,0}=1\).

**2. Subcritical phase velocities.** When \(0<\gamma<1/2\), Gamma concentration and the mean-value theorem on \([q/2,2q]\) show
\[
\mathbb E|U_q^\gamma-q^\gamma|\le C_\gamma q^{\gamma-1}\mathbb E|U_q-q|+O(e^{-cq}q^\gamma)=O(q^{\gamma-1/2})=o(1).
\]
Here \(\mathbb E|U_q-q|\le\sqrt q\); the omitted tails are bounded by Gamma Chernoff estimates and Gamma moments. Since \(p\) is Lipschitz, \(\lambda_n(\beta)=p(q^\gamma)+o(1)\).

**3. Critical heat filtering.** At \(\gamma=1/2\), write \(U_q\) as the sum of \(q\) independent unit exponentials (\(q\) is an integer). The central limit theorem and the delta method give
\[
\sqrt{U_q}-\sqrt q\ \Longrightarrow\ \mathcal N(0,1/4).
\]
For each fixed Fourier mode \(m\), bounded continuity of the exponential yields
\[
\mathbb E e^{im\sqrt{U_q}}=e^{im\sqrt q}\big(e^{-m^2/8}+o(1)\big).
\]
Summing finitely many modes proves \(\lambda_n(1)=(Hp)(\sqrt{n+d})+o(1)\). The wrapped heat kernel of variance \(1/4\) is strictly positive, so averaging any nonconstant continuous periodic function strictly raises its minimum and lowers its maximum. Its Fourier multipliers are nonzero; consequently \(Hp\) remains nonconstant.

**4. Supercritical rapid decay.** Suppose \(\gamma>1/2\). Fix \(m\ne0\) and integer \(J>0\). With \(t=(u-q)/\sqrt q\), let \(f_q(t)\) be the transformed Gamma density, and insert a smooth cutoff \(\chi(u/q)\) equal to one for \(u/q\in[3/4,5/4]\) and supported inside \([1/2,2]\). Gamma large-deviation bounds make the discarded integral \(O(e^{-cq})\). On the cutoff, the phase \(\phi_q(t)=m(q+\sqrt q t)^\gamma\) obeys
\[
|\phi'_q(t)|\asymp_{m,\gamma}q^{\gamma-1/2},\qquad
|\partial_t^j(\phi'_q(t)^{-1})|\le C_{j,m,\gamma}q^{-(\gamma-1/2)-j/2}.
\]
For every fixed \(j\), the \(L^1\) norm of \(\partial_t^j[f_q(t)\chi((q+\sqrt q t)/q)]\) is bounded uniformly in sufficiently large \(q\): derivatives of \(\log f_q\) are bounded by fixed polynomials in \(|t|\) on the cutoff, and the standardized Gamma variables have uniformly bounded moments. Repeated integration by parts using \(L=(i\phi'_q)^{-1}\partial_t\) therefore gives
\[
|I_{q,m}|\le C_{J,m,\gamma}q^{-J(\gamma-1/2)}+O(e^{-cq}).
\]
As \(J\) is arbitrary, \(\lambda_n(\beta)-\bar p=O_A((n+d)^{-A})\) for every \(A>0\). Thus \(T_\beta-\bar p I\) is compact. More strongly, for every \(s>0\), choose \(A>d/s\) and use \(m_n=O(n^{d-1})\) to obtain
\[
\sum_{n\ge0}m_n|\lambda_n(\beta)-\bar p|^s<\infty,
\]
which is exactly \(\mathcal S_s\) membership. The special case \(\beta=2\) can also be checked exactly: \(\mathbb E e^{imU_q}=(1-im)^{-q}\), so all nonzero Fourier modes decay geometrically.

**5. Phase density, weighted distribution, and essential spectra.** For \(0<\gamma\le1/2\), the real sequence \((n+d)^\gamma\) tends to infinity and its successive increments tend to zero; hence its residues modulo \(2\pi\) have every circle phase as a limit point. In fact the phases are equidistributed even under degree multiplicity weights. For every nonzero integer \(\ell\), partial summation and a sum–integral comparison yield
\[
\sum_{n=1}^{N}n^{d-1}e^{i\ell(n+d)^\gamma}
=O_{\ell,d,\gamma}(N^{d-\gamma}+N^{d-1+\gamma})=o(N^d).
\]
The integral estimate comes from one integration by parts using phase derivative \(\ell\gamma(x+d)^{\gamma-1}\); the sum–integral error is bounded by the integral of the absolute derivative. Replacing \(n^{d-1}\) by \(m_n\), a polynomial of degree \(d-1\), does not alter the normalized limit. Weyl's criterion implies convergence of the weighted empirical phase measures to circle Haar measure. Since the preceding eigenvalue asymptotics hold uniformly along the tail and the finite initial degrees have vanishing relative weight, the stated weak eigenvalue-distribution limits follow for all three regimes.

The essential spectrum of a bounded diagonal self-adjoint operator consists of its eigenvalue limits at infinity together with any eigenvalues of infinite multiplicity. Here each homogeneous degree has finite multiplicity, and the phase cluster set is the full circle for \(\gamma\le1/2\); hence the first two essential spectra are precisely the images of \(p\) and \(Hp\), respectively. For \(\gamma>1/2\) all eigenvalues tend to \(\bar p\), yielding the singleton. Since \(p\) and \(Hp\) are nonconstant, the centered operators in the first two regimes are not compact. This completes the proof.

## Verification
The degree-multiplicity identity \(\sum_{n=0}^N\binom{n+d-1}{d-1}=\binom{N+d}{d}\) and the exact Gamma integral at \(\beta=2\) offer independent finite checks. Numerical quadrature with standardized Gamma densities was additionally performed for \(d=1,3\), \(n=100,400,1200\) and \(\beta=0.6,1,1.4\), on a symmetric ten-standard-deviation window. For example, for \(d=1,n=1200\), the computed cosine moment was approximately \(-0.51041\) at \(\beta=0.6\), compared with the subcritical prediction \(-0.51239\); \(-0.87861\) at \(\beta=1\), compared with the heat-filter prediction \(-0.87827\); and \(0.00047\) at \(\beta=1.4\), compared with the supercritical limit zero. These computations corroborate, but are not used to prove, the all-degree assertions. Every analytic step is specified above and is reproducible directly from Gamma moments, the central limit theorem, integration by parts, and Weyl's criterion.

## Relationship to prior work
Dileep, Fang and Tien (arXiv:2610.40236v1, 2026) determine mixed-norm boundedness, compactness, and essential-norm conditions for positive Toeplitz measures on Gaussian Fock spaces, but their full paper does not state this periodized phase-speed spectral trichotomy or its all-Schatten endpoint. Looi (arXiv:2603.10879, 2026) gives the critical cosine example \(\frac12+\cos(2|z|)\) and its Gaussian attenuation on Fock spaces in arbitrary dimension. Thus the single-frequency critical phenomenon is **prior art**, not claimed new in isolation. Grudsky and Vasilevski (2002), Example 1 and Theorem 4.3, prove compactness for certain rapidly oscillating radial symbols and Example 2 treats a linear phase exactly. This covers qualitative aspects of the supercritical case but not the complete all-\(\beta\), all-finite-periodic-profile essential-spectrum and weighted spectral-distribution laws or the common all-Schatten assertion.

Bdarneh (arXiv:2609.20652) provides the general radial representation framework, not these asymptotics. Xu and Dong (arXiv:2609.16970) give Schatten–Lorentz criteria and other singular-value results; their stated conditions do not directly yield the explicit three-regime spectral laws for a bounded oscillatory radial symbol. The published result *The logarithmic spectral filter for smooth radial Fock Toeplitz operators* treats decaying log–log-periodic symbols and their Dixmier means, not the nondecaying fast-periodic family here. The novelty is the combined phase-speed classification, exact spectral measures across all complex dimensions, and supercritical membership in every Schatten quasi-ideal.

## Limitations
The claim requires a **fixed finite** dimension and a strictly positive real nonconstant trigonometric-polynomial profile; extension to arbitrary continuous, nonperiodic, signed, or slowly varying profiles is not asserted. Spectral conclusions concern the Gaussian Hilbert Fock space, not general mixed-norm transfer spaces. The all-Schatten result concerns the centered operator, not the noncompact positive operator itself. The critical single-cosine attenuation and qualitative supercritical compactness were previously known. A more general theorem for gamma oscillatory integrals or radial Toeplitz eigenvalue sequences might imply portions of this result and remains a priority risk; the cited search and source comparisons are not an independent originality certification. No independent mathematical audit has been performed.

## References
1. D. K. Dileep, X. Fang and P. T. Tien, *Positive Toeplitz Operators Between Gaussian Mixed-Norm Fock Spaces*, arXiv:2610.40236v1, first posted 2026-10-29, https://arxiv.org/html/2610.40236v1.
2. S. Looi, *Positive Berezin liminf does not imply essential positivity for radial Toeplitz operators on Bergman and Fock spaces*, arXiv:2603.10879, first posted 2026-03-11, https://arxiv.org/html/2603.10879.
3. S. M. Grudsky and N. L. Vasilevski, *Toeplitz operators on the Fock space: Radial component effects*, Integral Equations and Operator Theory 44 (2002), 10–37, DOI 10.1007/BF01197858; author-uploaded full text at https://www.researchgate.net/publication/226507689_Toeplitz_operators_on_the_Fock_space_Radial_component_effects.
4. K. Bdarneh, *Toeplitz C*-algebras on radially weighted Fock spaces: commutativity and spectral representation*, arXiv:2609.20652, https://arxiv.org/abs/2609.20652.
5. C. Xu and J. Dong, *IDA symbols and Schatten--Lorentz theory for Toeplitz operators on weighted Fock spaces*, arXiv:2609.16970, https://arxiv.org/abs/2609.16970.
6. *The logarithmic spectral filter for smooth radial Fock Toeplitz operators*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-logarithmic-spectral-filter-for-smooth-radial-fock-toeplitz--0bc5b54dc8b5.
