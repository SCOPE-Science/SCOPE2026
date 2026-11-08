# Gaussian high-exponent law and amplitude drift for finite Fourier apertures

## Finding
Fix an integer \(m\ge 2\) and pairwise distinct integer frequencies \(\Lambda=\{\lambda_1,\ldots,\lambda_m\}\). Write \(g=\gcd_{j\ge2}|\lambda_j-\lambda_1|\), \(\mu=m^{-1}\sum_j\lambda_j\), and \(V=m^{-1}\sum_j(\lambda_j-\mu)^2>0\). For positive even integers \(p=2q\), define the sharp Fourier-synthesis constant
\[
K_p(\Lambda)=\max_{\sum_j|c_j|^2=1}\left(\frac1{2\pi}\int_0^{2\pi}\left|\sum_{j=1}^m c_j e^{i\lambda_jt}\right|^p\,dt\right)^{1/p}.
\]
Then, as \(p\to\infty\) through even integers,
\[
\boxed{\log K_p(\Lambda)=\frac12\log m-\frac{\log p}{2p}+\frac1p\log\frac{g}{\sqrt{2\pi V}}+O_\Lambda(p^{-2}).}
\]
For every sufficiently large even \(p\), the maximizing coefficient magnitudes are unique and strictly positive. In the displayed indexing, their unit-\(\ell^2\)-normalized values satisfy, simultaneously for every \(j\),
\[
\boxed{|c_j|=\frac1{\sqrt m}-\frac{(\lambda_j-\mu)^2-V}{2p\sqrt m\,V}+O_\Lambda(p^{-2}).}
\]
Every complex maximizer is obtained from this unique positive vector by a common complex phase and a translation phase: \(c_j=e^{i(\theta+\lambda_jt_0)}|c_j|\), with real \(\theta,t_0\). Conversely each such coefficient vector is maximizing. The assertions concern all sufficiently large **even** exponents; no conclusion on exact phase rigidity for arbitrary non-even exponents is asserted.

For the classical aperture \(\Lambda=\{0,1,3\}\), \(V=14/9\) and \(g=1\). The first correction to the ordered coefficient amplitudes is exactly \((-2,13,-11)/(28\sqrt3\,p)\): the central frequency gains mass while the highest frequency loses it.

## Assumptions and scope
The circle carries Haar measure \(dt/(2\pi)\), and the coefficient norm is the unweighted Euclidean norm. The frequency set is fixed while \(p\to\infty\), with no assertion of uniformity when the number or spacing of frequencies grows. A common frequency translation, reflection, or integer dilation leaves the formula invariant, as expected from modulation, complex conjugation, and change of the circle variable. The error constants may depend on the entire finite set \(\Lambda\). Existence, uniqueness, and phases are statements about unrestricted complex coefficients, not merely nonnegative coefficients.

## Proof
**1. Majorant reduction and phase equality.** For \(p=2q\), Parseval applied to the \(q\)-th power yields
\[
\left\|\sum_jc_je^{i\lambda_jt}\right\|_{2q}^{2q}
=\sum_{n\in\mathbb Z}\left|\sum_{\substack{\alpha\in\mathbb Z_{\ge0}^m,\ |\alpha|=q\\\sum_j\alpha_j\lambda_j=n}}\frac{q!}{\prod_j\alpha_j!}\prod_jc_j^{\alpha_j}\right|^2.
\]
The triangle inequality in every inner sum shows that replacing \(c_j\) by \(|c_j|\) never decreases the norm. Therefore a maximum exists with nonnegative amplitudes \(a_j\) on the unit sphere. Equality for a complex maximizer with all amplitudes nonzero forces equal phases among every pair of monomials with the same \(q\)-fold frequency and length.

Let \(L=\{v\in\mathbb Z^m:\sum_jv_j=0,\ \sum_jv_j\lambda_j=0\}\). Choose a finite integer basis \(v^{(1)},\ldots,v^{(m-2)}\) of this lattice (the empty basis if \(m=2\)). For \(q\) at least the sum of the positive coordinates of each basis vector, its positive and negative parts can be padded by identical nonnegative counts to obtain two length-\(q\) monomials with the same frequency. Equality in the majorant then forces \(\exp(i\sum_jv_j^{(r)}\arg c_j)=1\) for every basis relation. Conversely these relations suffice for all monomial phase equalities. The quotient \(\mathbb Z^m/L\) is isomorphic to the torsion-free subgroup \(\{(\sum_jv_j,\sum_j\lambda_jv_j):v\in\mathbb Z^m\}\) of \(\mathbb Z^2\). Every circle-valued character of that subgroup extends to \(\mathbb Z^2\); hence the phase vector has precisely the form \(\arg c_j\equiv\theta+\lambda_jt_0\pmod{2\pi}\). Such phases indeed align every convolution term. Thus, for all sufficiently large \(q\), **provided all maximizing amplitudes are positive**, the phase classification is exact.

**2. All maximizing amplitudes converge to the flat vector.** The elementary bounds \(\|\sum_j a_je^{i\lambda_jt}\|_p\le\sum_j a_j\le\sqrt m\) hold on the positive unit sphere. At the flat vector \(a_j=m^{-1/2}\), the \(L^p\) norms tend to the supremum \(\sqrt m\). Therefore \(K_p\to\sqrt m\), and any maximizing \(a\) must satisfy \(\sum_j a_j\to\sqrt m\). Since \(\|a\|_2=1\), this implies \(\|a-m^{-1/2}\mathbf1\|_2^2=2-2m^{-1/2}\sum_ja_j\to0\). In particular all maximizing amplitudes are strictly positive for sufficiently large \(p\).

**3. Uniform Laplace analysis.** For a positive amplitude vector \(a\) near \(a_*=m^{-1/2}\mathbf1\), put \(S(a)=\sum_ja_j\), \(\mu(a)=\sum_ja_j\lambda_j/S(a)\), and \(V(a)=\sum_ja_j(\lambda_j-\mu(a))^2/S(a)\). The triangle inequality is strict except at the exactly \(g\) congruent points \(t=2\pi k/g\) of the circle. Taylor expansion at any such point gives
\[
\log\frac{|\sum_j a_je^{i\lambda_jt}|}{S(a)}=-\frac12V(a)t^2+O_\Lambda(t^4),
\]
where the remainder is uniform for \(a\) in a fixed positive neighborhood of \(a_*\); the absence of a cubic term follows from evenness of the modulus near each maximum. There is a strict uniform gap away from small neighborhoods of the peaks. Parameter-dependent Laplace expansion, including its first two derivatives in the amplitudes, consequently yields
\[
\log\left\|\sum_j a_je^{i\lambda_jt}\right\|_p
=\log S(a)-\frac{\log p}{2p}+\frac1p\log\frac{g}{\sqrt{2\pi V(a)}}+O_\Lambda(p^{-2})
\]
with the \(O_\Lambda(p^{-2})\) term uniform in \(C^2\) on that neighborhood. In this formula and below \(p\) need only be real and large, but the global majorant/phase conclusion uses evenness.

**4. Uniqueness and drift.** On the positive unit sphere, \(\log S(a)\) has the unique maximum \(a_*\), with tangent Hessian equal to minus the identity. The \(C^2\)-uniform expansion in step 3 makes the Hessian of the full objective strictly negative on a sufficiently small geodesic neighborhood for all large \(p\). Step 2 places every global maximizer in that neighborhood; strict local concavity proves uniqueness. The tangent gradient at \(a_*\) of the variance term is determined by
\[
\left.\frac{\partial\log V(a)}{\partial a_j}\right|_{a=a_*}=
\frac{(\lambda_j-\mu)^2-V}{\sqrt m\,V}.
\]
Its coordinate sum vanishes. Solving the stationary equation using the negative identity Hessian from \(\log S\), or equivalently the implicit function theorem in sphere coordinates, yields
\[
a_j(p)=\frac1{\sqrt m}-\frac{(\lambda_j-\mu)^2-V}{2p\sqrt m\,V}+O_\Lambda(p^{-2}).
\]
Substituting \(a(p)=a_*+O_\Lambda(1/p)\) into the Laplace expansion gives the sharp logarithmic constant with an \(O_\Lambda(p^{-2})\) remainder. Step 1 supplies all complex extremizers. This proves every stated assertion.

## Verification
A standalone standard-library checker in `artifacts/check_fourier_high_p.py` computes even moments both by exact finite convolution and by direct trapezoidal quadrature, then performs normalized positive-amplitude numerical maximization at several even exponents for \(\{0,1,3\}\), \(\{0,1,2\}\), and a nonconsecutive four-mode aperture. It compares the optimized amplitudes with the displayed drift and the optimal norm with the Gaussian Laplace prediction. These finite tests are sanity checks; the asymptotic conclusion and uniqueness for all sufficiently large exponents follow from the analytic proof, not from finite testing.

## Relationship to prior work
Jaming, Kellay, and Saba study sharp lower bounds for \(L^1\) norms of trigonometric and nonharmonic Fourier sums; their frequency-sensitive lower bounds do not give optimized large-exponent \(\ell^2\to L^p\) constants or coefficient drift. Ganzburg, Saucedo, and Tikhonov establish Bernstein–Nikolskii estimates with optimal dependence on differentiation order across bandwidth classes; their asymptotic parameter is the differentiation order and they do not supply the present fixed-aperture, growing-even-exponent expansion. Ganzburg’s 2019 sharp-constant asymptotics instead vary the spectral bandwidth within convex frequency bodies and do not track optimizer amplitudes for one fixed arbitrary finite aperture as the target exponent grows. Earlier Hardy–Littlewood majorant theory supplies the standard even-integer reduction of complex coefficients to nonnegative coefficients; that elementary reduction is explicitly treated as prior work. Exact low even-moment optimizations for particular three-frequency supports likewise do not imply the universal large-even-exponent formula or first-order amplitude drift for every fixed integer aperture.

## Limitations
The result is restricted to fixed finite one-dimensional integer-frequency sets and exponents tending to infinity along even integers. The uniqueness threshold is existential and depends on the frequency set; no uniform threshold or bounds in growing bandwidth are claimed. The \(C^2\)-uniform Laplace expansion is valid locally near strictly positive amplitudes, not on the entire coefficient sphere. The phase-rigidity statement is not asserted at low even exponents or non-even exponents. A possible earlier derivation from general asymptotic Laplace optimization in sparse Fourier norm theory remains a historical-priority risk; no broad source establishing the exact claimed drift was located in the checks documented here.

## References
1. P. Jaming, K. Kellay, C. Saba, *The Littlewood problem and non-harmonic Fourier series*, arXiv:2303.10919v1, first public 2023-03-20, Theorem 1.1 and Appendix B.
2. M. I. Ganzburg, M. Saucedo, S. Tikhonov, *Bernstein–Nikolskii Inequality: Optimality with Respect to the Smoothness Parameter*, arXiv:2403.13149v1, first public 2024-03-19, Theorems 1.1–1.4.
3. S. Krenedits, *Three-term idempotent counterexamples in the Hardy–Littlewood majorant problem*, arXiv:1006.0409v1, first public 2010-06-02 (background on the majorant problem).
4. *Sharp \(L^2\to L^6\) norm for the Hardy–Littlewood frequency triple*, publicly available mathematical result on the fixed support \(\{0,1,3\}\), \(p=6\), published 2026-10-11. (The full scientific statement and proof were examined.)
5. M. I. Ganzburg, *Sharp Constants of Approximation Theory. I. Multivariate Bernstein–Nikolskii Type Inequalities*, arXiv:1901.04400v1, first public 2019-01-14 (varying spectral bandwidth, not the fixed-aperture growing-exponent setting).
