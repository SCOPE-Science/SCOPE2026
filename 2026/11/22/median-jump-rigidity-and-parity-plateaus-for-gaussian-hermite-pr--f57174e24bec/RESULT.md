# Median-jump rigidity and parity plateaus for Gaussian Hermite projection error

## Finding
Let \(\gamma\) denote standard Gaussian probability measure on \(\mathbb R\), with density \(\phi(x)=(2\pi)^{-1/2}e^{-x^2/2}\). Let \(\operatorname{He}_k\) be the probabilists' Hermite polynomials, normalized by \(\int \operatorname{He}_j\operatorname{He}_k\,d\gamma=k!\,\delta_{jk}\), and let \(\Pi_n\) denote the \(L^2(\gamma)\)-orthogonal projection onto polynomials of degree at most \(n\).

For every integer \(n\ge0\), the exact sharp error constant for real functions of finite ordinary total variation on the full line is
\[
 C_n=\sup_{\operatorname{TV}(f)>0}\frac{\|f-\Pi_nf\|_{L^2(\gamma)}}{\operatorname{TV}(f)}.
\]
For every integer \(m\ge1\),
\[
 \boxed{C_{2m-1}^2=C_{2m}^2=\frac14-\frac1{2\pi}\sum_{j=0}^{m-1}\frac{\binom{2j}{j}}{4^j(2j+1)}}.
\]
Also \(C_0=1/2\). Each supremum is attained, and **all** its nonconstant real extremizers, modulo equality almost everywhere, are \(f(x)=a+b\mathbf1_{(0,\infty)}(x)\) with \(a\in\mathbb R\) and \(b\in\mathbb R\setminus\{0\}\). Thus the single jump at the Gaussian median is uniquely worst at every degree; the constants have exact odd–even plateaus and strictly decrease between consecutive plateaus. Their precise asymptotic rate is
\[
 \boxed{\lim_{n\to\infty}n^{1/4}C_n=2^{-1/4}\pi^{-3/4}}.
\]

## Assumptions and scope
The class consists of bounded real functions whose distributional derivative is a finite signed measure on \(\mathbb R\). Total variation is \(\operatorname{TV}(f)=|Df|(\mathbb R)\), without a Lebesgue-integrability requirement; in particular, half-line indicators belong to the domain. Additive constants are irrelevant because \(\Pi_n\) fixes constants. A function is understood up to \(\gamma\)-almost everywhere equality. The Gaussian measure has unit variance, and every polynomial is normalized as stated above. The formula concerns one-dimensional Gaussian-weighted mean-square projection error, not unweighted Lebesgue error or the total variation of the projected polynomial.

## Proof
**1. Reduction to individual jumps.** Write \(H_t(x)=\mathbf1_{(t,\infty)}(x)\). Every member of the stated variation class has, in \(L^2(\gamma)\), a Stieltjes representation \(f=a+\int H_t\,d(Df)(t)\). The map \(t\mapsto H_t\) is bounded and continuous into \(L^2(\gamma)\). Hence the Bochner integral is legitimate and, since \((I-\Pi_n)a=0\), Minkowski's inequality yields
\[
 \|(I-\Pi_n)f\|_2\le\operatorname{TV}(f)\sup_{t\in\mathbb R}\|(I-\Pi_n)H_t\|_2.
\]
Each \(H_t\) has unit variation, so the supremum is exactly the worst single-jump error.

**2. Exact residual.** Let \(\Phi(t)=\int_{-\infty}^t\phi(x)\,dx\) and \(E_n(t)=\|(I-\Pi_n)H_t\|_2^2\). Gaussian integration by parts gives, for \(k\ge1\),
\[
 \int_t^\infty \frac{\operatorname{He}_k(x)}{\sqrt{k!}}\phi(x)\,dx=\frac{\phi(t)\operatorname{He}_{k-1}(t)}{\sqrt{k!}}.
\]
Orthogonality and Pythagoras therefore give
\[
 E_n(t)=\Phi(t)(1-\Phi(t))-\phi(t)^2\sum_{k=1}^n\frac{\operatorname{He}_{k-1}(t)^2}{k!}.
\]
The empty sum is zero. Gaussian reflection and Hermite parity imply \(E_n(-t)=E_n(t)\).

**3. A positive derivative certificate for every degree.** Set
\[
 G(t)=\frac{2\Phi(t)-1}{2\phi(t)},\qquad Q_n(t)=\sum_{k=1}^n\frac{\operatorname{He}_{k-1}(t)\operatorname{He}_k(t)}{k!}.
\]
The Hermite identities \(\operatorname{He}_k'=k\operatorname{He}_{k-1}\) and \(t\operatorname{He}_{k-1}=\operatorname{He}_k+(k-1)\operatorname{He}_{k-2}\) imply, on differentiating the residual,
\[
 E_n'(t)=-2\phi(t)^2\bigl(G(t)-Q_n(t)\bigr).
\]
Furthermore, \(G'-tG=1\), while a telescoping identity gives
\[
 Q_n'-tQ_n=\sum_{k=1}^n\left(\frac{\operatorname{He}_{k-1}^2}{(k-1)!}-\frac{\operatorname{He}_k^2}{k!}\right)=1-\frac{\operatorname{He}_n^2}{n!}.
\]
Here \(G(0)=Q_n(0)=0\). Solving the resulting first-order inhomogeneous equation proves the exact identity
\[
 \boxed{E_n'(t)=-\frac{2\phi(t)^2e^{t^2/2}}{n!}\int_0^t e^{-u^2/2}\operatorname{He}_n(u)^2\,du.}
\]
For every \(t>0\) the integral is strictly positive: a nonzero polynomial cannot vanish on an interval. Thus \(E_n\) is strictly decreasing on \((0,\infty)\), for **every** integer \(n\ge0\). By evenness, its unique global maximizer is \(t=0\). Any nonconstant extremal Stieltjes measure must be supported entirely on this unique maximizing point (otherwise the strict bound integrated against its variation is smaller). Therefore the only extremizers, up to constants and nonzero scales, are median single jumps.

**4. Parity and exact formula.** For \(k\ge0\), \(\operatorname{He}_{2k+1}(0)=0\) and \(\operatorname{He}_{2k}(0)=(-1)^k(2k)!/(2^k k!)\). Substituting into Step 2 gives \(E_{2m-1}(0)=E_{2m}(0)\) and the finite sum in the finding. The strictly positive odd-degree squared coefficient added on passing from degree \(2m\) to \(2m+1\) proves strict decrease between plateaus.

**5. Sharp limiting constant.** Completeness of the Hermite orthonormal basis and the expansion \(\arcsin(z)=\sum_{j\ge0}\binom{2j}{j}z^{2j+1}/(4^j(2j+1))\) yield
\[
 C_{2m-1}^2=C_{2m}^2=\frac1{2\pi}\sum_{j=m}^{\infty}\frac{\binom{2j}{j}}{4^j(2j+1)}.
\]
Stirling's formula yields \(\binom{2j}{j}/(4^j(2j+1))\sim (2\sqrt\pi)^{-1}j^{-3/2}\), and integral comparison gives the tail \(\sim\pi^{-1/2}m^{-1/2}\). Therefore \(C_{2m}^2\sim (2\pi^{3/2}\sqrt m)^{-1}\), equivalent to the displayed degree-\(n\) constant. This argument also handles odd degrees because the two consecutive constants coincide.

## Verification
Run `python3 verify.py` using Python's standard library. The checker confirms the crucial telescoping polynomial identity for degrees \(0\) through \(24\) exactly over integers, tests the jump-residual inequality on 159 positive thresholds at degrees \(0\) through \(13\), compares two independent finite constant formulas, and checks convergence toward the analytical asymptotic coefficient on increasing degrees. The executed checker reported `VERIFY_OK checks=2271`. Its finite tests are only corroborative; the unrestricted statements follow from Steps 1–5.

## Relationship to prior work
Hermite orthogonality, Rodrigues' rule, and the recurrence used in the proof are classical; NIST DLMF §§18.3 and 18.18 document the standard formulas. Jaming, Karoui, Kerman, and Spektor (2014), and Jaming, Karoui, and Spektor (2015) investigate Hermite-function approximation of almost time- and band-limited functions, with estimates for different input classes and projections. Davis and Hagelstein (2022) analyze pointwise Gibbs overshoot of Jacobi, Hermite, and Laguerre expansions; that local overshoot result does not control this sharp global \(BV\)-to-\(L^2(\gamma)\) error.

Published Gaussian Hermite coefficient estimates and sharp adjacent-coefficient norms determine individual or two-mode information under the same variation seminorm. They do not imply the simultaneous infinite-tail bound from the present positive integral identity: individual even-degree coefficients may have off-center extrema, while the full projection error has a unique center extremum for every degree. Published sharp BV errors for Legendre and Chebyshev projectors employ different measures and polynomial bases and do not entail this Gaussian formula. These comparisons support a distinct mathematical claim, not a guarantee of historical priority.

## Limitations
The theorem does not cover multidimensional Gaussian chaos, weighted variation, truncated spatial windows, nonlinear approximation, or unweighted Lebesgue error. A change from probabilists' to physicists' Hermite normalization requires the corresponding spatial rescaling. The exact all-degree formula and uniqueness are proved analytically, while numerical checks cannot certify novelty. Unindexed literature could contain a mathematically equivalent tail-norm inequality; no independent external mathematical audit has been performed.

## References
1. P. Jaming, A. Karoui, R. Kerman, S. Spektor, *Approximation of almost time and band limited functions I: Hermite expansions*, arXiv:1407.1293, first public July 4, 2014. https://arxiv.org/abs/1407.1293
2. P. Jaming, A. Karoui, S. Spektor, *The approximation of almost time and band limited functions by their expansion in some orthogonal polynomials bases*, arXiv:1501.03655, first public January 15, 2015. https://arxiv.org/abs/1501.03655
3. J. M. Davis and P. Hagelstein, *Gibbs phenomena for some classical orthogonal polynomials*, Journal of Mathematical Analysis and Applications 505 (2022), 125574. https://doi.org/10.1016/j.jmaa.2021.125574
4. NIST Digital Library of Mathematical Functions, §§18.3 and 18.18. https://dlmf.nist.gov/18.3 and https://dlmf.nist.gov/18.18
5. *Sharp Gaussian Hermite coefficient bounds for bounded-variation data, with parity-dependent corrections*, public mathematical record (2026), identifier `0b869f234dbe`.
6. *A no-cost adjacent Hermite coefficient theorem for bounded variation*, public mathematical record (2026), identifier `1cf206db791f`.
