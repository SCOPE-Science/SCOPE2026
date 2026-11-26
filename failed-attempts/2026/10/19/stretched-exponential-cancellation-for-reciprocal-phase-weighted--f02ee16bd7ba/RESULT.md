# Stretched-exponential cancellation for reciprocal-phase weighted Bergman moments

## Finding
For each fixed real \(\alpha>-1\), the canonical reciprocal-boundary-phase function
\[
\phi(z)=\exp\!\left(\frac{i}{1-|z|^2}\right),\qquad z\in\mathbb D,
\]
has modulus one yet produces weighted Bergman monomial moments with **stretched-exponential complex cancellation**. The sharp asymptotic of its Toeplitz eigenvalues is
\[
\boxed{\lambda_{n,\alpha}=\frac{\sqrt\pi}{\Gamma(\alpha+1)}n^{\alpha/2+1/4}
  \exp[-(1-i)\sqrt{2n}]
  \exp\!\left(i\left[\frac12-\frac{\pi(2\alpha+1)}8\right]\right)
  \bigl(1+O_\alpha(n^{-1/2})\bigr).}
\]
Consequently, \(\lim_{n\to\infty}\log|\lambda_{n,\alpha}|/\sqrt n=-\sqrt2\), and the corresponding bounded Toeplitz operator lies in \(\mathcal S_p\) for **every** \(p>0\). The complex phase, power prefactor, and exponential coefficient are specified, not just a qualitative compactness assertion.

## Assumptions and scope
Set \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and use the normalized measure \(dA_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha dA(z)/\pi\), with \(dA\) ordinary planar Lebesgue measure. The weighted analytic Bergman space \(A^2_\alpha(\mathbb D)\) is the analytic subspace of \(L^2(dA_\alpha)\), and \(P_\alpha\) is its orthogonal projection. The Toeplitz operator is \(T_\phi=P_\alpha M_\phi\); it is bounded since \(|\phi|=1\).

The orthonormal monomials are
\[
e_{n,\alpha}(z)=\left[\frac{\Gamma(n+\alpha+2)}{\Gamma(\alpha+2)\Gamma(n+1)}\right]^{1/2}z^n,
\qquad n=0,1,2,\ldots.
\]
For each fixed \(\alpha>-1\), radiality and angular orthogonality yield \(T_\phi e_{n,\alpha}=\lambda_{n,\alpha}e_{n,\alpha}\) with
\[
\lambda_{n,\alpha}=\frac{1}{B(n+1,\alpha+1)}\int_0^1 t^n(1-t)^\alpha e^{i/(1-t)}\,dt,
\]
where \(B\) is Euler's beta function. The integral is an ordinary improper integral: its absolute value is integrable for \(\alpha>-1\).

## Proof
Write \(s=1-t\) and define
\[
I_{n,\alpha}=\int_0^1 s^\alpha(1-s)^n e^{i/s}\,ds,\qquad
\zeta=e^{-i\pi/4}=\frac{1-i}{\sqrt2}.
\]
Take the principal branch of \(s^\alpha\) on the closed sector \(-\pi/4\le\arg s\le0\). Deforming the contour from \([0,1]\) to the two segments \([0,\zeta]\cup[\zeta,1]\) is justified at \(s=0\): on a small circular arc in that sector, \(|e^{i/s}|=\exp(\sin(\arg s)/|s|)\le1\), while \(|s^\alpha ds|\) is \(O(\varepsilon^{\alpha+1})\). The second segment has \(|1-s|\le|1-\zeta|<1\) and stays away from zero. Therefore its contribution is \(O_\alpha(\rho^n)\) for some \(\rho<1\).

On the first segment, substitute \(s=\zeta u/\sqrt n\), noting \(i/\zeta=-\zeta\):
\[
I_{n,\alpha}=\zeta^{\alpha+1}n^{-(\alpha+1)/2}
\int_0^{\sqrt n} u^\alpha \left(1-\frac{\zeta u}{\sqrt n}\right)^n
\exp\!\left(-\frac{\zeta\sqrt n}{u}\right)du+O_\alpha(\rho^n).
\]
For \(u\) in a fixed compact neighborhood of \(1\), expansion of the analytic logarithm gives
\[
n\log\!\left(1-\frac{\zeta u}{\sqrt n}\right)
=-\zeta\sqrt n\,u-\frac{\zeta^2u^2}{2}+O(n^{-1/2}),
\]
uniformly there. The unique global minimum of \(u+u^{-1}\) for \(u>0\) is \(u=1\), with \(u+u^{-1}=2+(u-1)^2+O((u-1)^3)\). Because \(\operatorname{Re}\zeta>0\), the real part of the leading exponent decreases strictly away from this point. To justify localization, restrict first to \(u\in[\delta,R]\) for \(0<\delta<1<R\). On its complement, the factor \(e^{-\operatorname{Re}\zeta\sqrt n/u}\) controls \(u<\delta\), while \(|1-\zeta u/\sqrt n|^n\le\exp(-c\sqrt n\,u)\) controls \(R<u\le c'\sqrt n\), and the remaining section \(u\asymp\sqrt n\) is \(O(e^{-cn})\). These estimates leave an exponentially small remainder relative to the saddle contribution after \(\delta\downarrow0\) and \(R\uparrow\infty\).

Rescale \(u=1+n^{-1/4}v\). The Gaussian factor becomes \(e^{-\zeta v^2}\), while the non-leading factor evaluates to \(\exp(-\zeta^2/2)=e^{i/2}\). The branch-compatible complex Gaussian integral is \(\int_{\mathbb R}e^{-\zeta v^2}\,dv=\sqrt\pi\,\zeta^{-1/2}\). Expanding the analytic amplitude and phase through quadratic order, the nominal \(n^{-1/4}\) correction is odd in \(v\) and integrates to zero; the remaining relative error is \(O_\alpha(n^{-1/2})\). Thus
\[
I_{n,\alpha}=\sqrt\pi\,\zeta^{\alpha+1/2}e^{i/2}
n^{-\alpha/2-3/4} e^{-2\zeta\sqrt n}
\left(1+O_\alpha(n^{-1/2})\right).
\]
Finally, \(B(n+1,\alpha+1)=\Gamma(\alpha+1)n^{-\alpha-1}\left(1+O_\alpha(n^{-1})\right)\), \(2\zeta=(1-i)\sqrt2\), and \(\zeta^{\alpha+1/2}=\exp[-i\pi(2\alpha+1)/8]\). Dividing by the beta factor proves the displayed complex asymptotic. Its nonzero leading constant yields \(|\lambda_{n,\alpha}|=O_\alpha(n^{\alpha/2+1/4}e^{-\sqrt{2n}})\). Since the normalized monomials diagonalize \(T_\phi\), \(\sum_{n\ge0}|\lambda_{n,\alpha}|^p<\infty\) for every \(p>0\), which proves the Schatten claim. No sign, positivity, or pointwise vanishing hypothesis on \(\phi\) was used.

## Verification
The accompanying `verify.py` performs high-precision contour quadrature on the deformed path and compares the exact beta-normalized moments to the analytic leading term for four different Bergman weights and three degrees each. It also checks decay of the relative error as the degree increases. The executed checker returned: `VERIFY_OK 16 deformed-contour/asymptotic comparisons and decay checks; four weights; n=50,200,800`. This is supplementary finite evidence: the all-degree result is proved by contour deformation and complex Laplace's method, not by numerical extrapolation. Run `python verify.py`; the only nonstandard Python dependency is `mpmath`.

## Relationship to prior work
Cao, He, and Zhang (2026, arXiv:2609.24614) characterize compactness of unweighted Bergman Toeplitz operators by local averages. Their criteria do not specify complex spectral asymptotics or all-Schatten decay for this canonical radial chirp. Bendaoud, Kupin, Toumache, Touré, and Zarouf (2020, doi:10.15407/mag16.01.003, §3) study radial oscillatory symbols of the form \((1-r)^{-\beta}\sin((1-r)^{-\gamma})\) and provide polynomial Schatten criteria. That construction is related but does not give the exact reciprocal-phase weighted Bergman moment, its sharp complex leading term, or the resulting all-Schatten membership at the fixed reciprocal oscillation exponent. Looi (2026, arXiv:2603.10879, §3) studies logarithmic-phase Bergman symbols with nondecaying eigenvalue oscillation, a contrasting asymptotic regime. Rozenblum (2010, arXiv:1012.3528) studies radial Toeplitz spectral behavior and oscillatory examples predominantly with real symbols, rather than the present complex boundary singularity. The classical diagonal moment formula and complex steepest-descent method are not claimed as original.

## Limitations
The weight parameter \(\alpha\) is fixed as degree increases; uniformity in a growing \(\alpha\) is not established. Only the one-dimensional weighted analytic disk Bergman space and the stated bounded radial symbol are treated. The Schatten assertion follows from the asymptotic and does not imply similar regularity for arbitrary unimodular or nonradial symbols. Historical priority for the exact special-function asymptotic remains conditional on wider literature comparison, particularly the not-fully-inspected 2001 Grudsky–Vasilevski article. There has been no independent scientific audit.

## References
Cao, G., He, L., and Zhang, S. (2026). *Compactness of Toeplitz Operators on the Bergman Space*. arXiv:2609.24614. https://arxiv.org/abs/2609.24614

Bendaoud, Z., Kupin, S., Toumache, K., Touré, B., and Zarouf, R. (2020). *Toeplitz Operators with Radial Symbols on Bergman Space and Schatten-von Neumann Classes*. Journal of Mathematical Physics, Analysis, Geometry 16, 3–26. https://doi.org/10.15407/mag16.01.003

Looi, S. (2026). *The Berezin liminf criterion fails for radial Toeplitz operators*. arXiv:2603.10879. https://arxiv.org/abs/2603.10879

Rozenblum, G. (2010). *On Lower Eigenvalue Bounds for Toeplitz Operators with Radial Symbols in Bergman Spaces*. arXiv:1012.3528. https://arxiv.org/abs/1012.3528

Grudsky, S., and Vasilevski, V. (2001). *Bergman–Toeplitz operators: radial component influence*. Integral Equations and Operator Theory 40, 16–33. https://doi.org/10.1007/BF01202952
