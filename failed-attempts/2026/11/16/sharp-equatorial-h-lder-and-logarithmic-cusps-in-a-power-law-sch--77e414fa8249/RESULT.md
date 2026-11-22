# Sharp equatorial Hölder and logarithmic cusps in a power-law Schoenberg family

## Finding

For \(\alpha>1\), let \(P_n\) be the Legendre polynomial with \(P_n(1)=1\), and define
\[
\Phi_\alpha(\theta)=\frac1{\zeta(\alpha)}\sum_{j=0}^{\infty}\frac{P_{4j+1}(\cos\theta)}{(j+1)^\alpha},\qquad 0\le\theta\le\pi.
\]
Every \(\Phi_\alpha\) is a normalized continuous isotropic positive-semidefinite kernel on \(\mathbb S^2\), and \(\Phi_\alpha(\pi/2+h)=-\Phi_\alpha(\pi/2-h)\).

Write \(\beta=\alpha-\tfrac12\). For \(1<\alpha<\tfrac32\),
\[
\Phi_\alpha(\tfrac\pi2+h)
=-K_\alpha\operatorname{sgn}(h)|h|^\beta+o(|h|^\beta),\qquad
K_\alpha=\frac{4^\beta\pi}{2\sqrt{2\pi}\,\zeta(\alpha)\Gamma(\alpha+\tfrac12)\cos(\pi\beta/2)}>0.
\]
For \(\alpha=\tfrac32\),
\[
\Phi_{3/2}(\tfrac\pi2+h)
=-\frac{\sqrt{8/\pi}}{\zeta(3/2)}h\log\frac1{|h|}+O(|h|).
\]
For \(\alpha>\tfrac32\), \(\Phi_\alpha\) is continuously differentiable on an open interval containing the equator, with strictly negative derivative
\[
\Phi_\alpha'(\tfrac\pi2)=-\frac1{\zeta(\alpha)}\sum_{j=0}^{\infty}\frac{(4j+1)\binom{4j}{2j}}{2^{4j}(j+1)^\alpha}.
\]
Thus the local Hölder exponent is exactly \(\alpha-\tfrac12\) in the subcritical regime; at the critical exponent the kernel is Hölder of every order strictly below one but is not locally Lipschitz; above it the first derivative exists and is nonzero.

For \(0<s<1\), set \(Q_s(\theta)=(1-s)(1-2s\cos\theta+s^2)^{-1/2}\). For every \(0<\varepsilon<1\), the mixture \(\Psi_{\alpha,s,\varepsilon}=(1-\varepsilon)\Phi_\alpha+\varepsilon Q_s\) is **strictly** positive definite on \(\mathbb S^2\); its subcritical and critical singular coefficients are precisely \(1-\varepsilon\) times the constants above.

## Assumptions and scope

All asymptotics concern \(h\to0\) through real nonzero values, with \(\alpha\) held fixed. The claim is limited to the round two-sphere and equatorial pointwise regularity. Normalization is the Legendre normalization \(P_n(1)=1\), with the zeta function \(\zeta\) the ordinary Riemann zeta function. For the positive-definiteness assertion, the isotropic kernel is \((x,y)\mapsto\Phi_\alpha(\arccos\langle x,y\rangle)\) on \(\mathbb S^2\). No other spherical dimensions, uniform endpoint estimates, or general coefficient sequences are included.

## Proof

**1. Positivity and parity.** By \(|P_n(t)|\le1\) for \(-1\le t\le1\), the defining series converges uniformly. Each normalized Legendre harmonic \(P_n(\langle x,y\rangle)\) is positive semidefinite by the spherical-harmonic addition formula; the coefficients are nonnegative and sum to one. Since all degrees \(4j+1\) are odd, \(P_{4j+1}(-t)=-P_{4j+1}(t)\), proving equatorial antisymmetry and vanishing there.

**2. Uniform Fourier-sine reduction.** The interior Darboux expansion for Legendre polynomials is, uniformly on \(\theta\in[\pi/3,2\pi/3]\),
\[
P_n(\cos\theta)=\left(\frac{2}{\pi(n+1/2)\sin\theta}\right)^{1/2}\cos\big((n+1/2)\theta-\pi/4\big)+R_n(\theta),\quad
|R_n(\theta)|\le Cn^{-3/2},\quad |R_n'(\theta)|\le Cn^{-1/2}.
\]
The derivative bound follows either from the next interior asymptotic term or the exact three-term adjacent-degree derivative identity, with the Darboux expansions for neighboring degrees. At \(\theta=\pi/2\) the leading cosine and the exact \(P_{4j+1}(0)\) both vanish; hence the remainder vanishes there. The mean value theorem gives \(R_{4j+1}(\pi/2+h)=O(|h|j^{-1/2})\). For \(j\ge1\), the leading expression equals
\[
-\frac1{\sqrt{2\pi}}j^{-1/2}\sin(4jh)+O\big(|h|j^{-1/2}+j^{-3/2}\min\{j|h|,1\}\big),
\]
where the last factor in the amplitude perturbation can instead be estimated using the exact vanishing at \(h=0\); the weighted sum of all errors is \(O_\alpha(|h|)\) for each fixed \(\alpha>1\). To see this without any uncontrolled differentiation of a big-O term, insert \((4j+3/2)h\) into the sine; its phase displacement from \(4jh\) is \(O(|h|)\), and replace the exact leading amplitude by \(j^{-1/2}/\sqrt{2\pi}\), whose difference is \(O(j^{-3/2})\) times \(\sin((4j+3/2)h)\). The latter sine is \(O(\min\{j|h|,1\})\). The replacement of the weight \((j+1)^{-\alpha}\) by \(j^{-\alpha}\) contributes another error \(O(j^{-\alpha-3/2}\min\{j|h|,1\})\); use \(j^{-\alpha}-(j+1)^{-\alpha}=O(j^{-\alpha-1})\). Split all weighted errors at \(j=|h|^{-1}\); their sums are \(O_\alpha(|h|)\), since \(\alpha>1\). The \(j=0\) term is analytic and \(O(|h|)\). Consequently,
\[
\boxed{\Phi_\alpha(\pi/2+h)=-\frac1{\sqrt{2\pi}\zeta(\alpha)}\sum_{j=1}^{\infty}\frac{\sin(4jh)}{j^{\alpha+1/2}}+O_\alpha(|h|).}
\]
The estimates are uniform for sufficiently small \(|h|\), for each fixed \(\alpha>1\).

**3. Subcritical exact constant.** Put \(\sigma=\alpha+1/2\in(3/2,2)\). A Riemann-sum argument, splitting near zero and at infinity using \(|\sin u|\le\min\{u,1\}\), proves for \(t\downarrow0\)
\[
\sum_{j=1}^\infty\frac{\sin(jt)}{j^\sigma}
=t^{\sigma-1}\left(\int_0^\infty\frac{\sin u}{u^\sigma}\,du+o(1)\right),\quad
\int_0^\infty\frac{\sin u}{u^\sigma}\,du=
\frac{\pi}{2\Gamma(\sigma)\sin(\pi\sigma/2)}.
\]
Substitute \(t=4|h|\), use sine oddness, and note \(\sin(\pi\sigma/2)=\cos(\pi\beta/2)>0\). Since \(|h|=o(|h|^\beta)\), the reduction error does not affect the sharp constant.

**4. Critical logarithm.** For \(0<t<2\pi\), the classical Fourier identity \(\sum_{j\ge1}\cos(jt)/j=-\log(2\sin(t/2))\) implies, upon integrating from zero,
\[
\sum_{j\ge1}\frac{\sin(jt)}{j^2}=-\int_0^t\log(2\sin(u/2))\,du
=t\log(1/t)+O(t).
\]
Put \(t=4|h|\) and use the sine reduction, giving the stated \(\sqrt{8/\pi}/\zeta(3/2)\) coefficient. A nonzero \(h\log(1/|h|)\) term forbids local Lipschitz regularity, while it obeys every smaller Hölder exponent.

**5. Supercritical slope.** Standard interior Legendre estimates give \(|\partial_\theta P_n(\cos\theta)|\le C\sqrt n\) uniformly near the equator. For \(\alpha>3/2\), the differentiated series converges uniformly there by \(\sum_j(j+1)^{-\alpha+1/2}<\infty\). The exact identity \(P_{4j+1}'(0)=(4j+1)\binom{4j}{2j}/2^{4j}\) and \(\partial_\theta\cos\theta|_{\pi/2}=-1\) yield the slope formula, whose summands are strictly positive.

**6. Strict positive definiteness without changing the cusp.** The Legendre generating function gives \(Q_s(\theta)=(1-s)\sum_{n\ge0}s^nP_n(\cos\theta)\). Thus every Schoenberg coefficient of \(Q_s\) is strictly positive, making its Gram matrix strictly positive for every set of pairwise distinct spherical points (use completeness of spherical harmonics). The mixture retains that property. Since \(Q_s\) is real analytic near the equator, its increment from the equatorial value is \(O(h)\), which is asymptotically lower order than the subcritical power or critical logarithm. This proves the stated stability.

## Verification

The accompanying standalone \(\texttt{CHECK.py}\) evaluates finite Legendre sums by stable three-term recurrence at several small angular offsets, checks qualitative convergence toward the derived constants, and checks exact derivative identities at small degrees. Run with `python CHECK.py` after installing the packages in `requirements.txt`. These finite checks are supplemental and do **not** prove the infinite-series limit, the asymptotic error bounds, or strict positivity; those rely on the analytical proof above.

## Relationship to prior work

Yan Ge's 2026 even-sphere optimal-differentiability theorem introduces the \(\alpha=3/2\) series as a nondifferentiable equatorial witness and studies dimension walks. Here that seed is placed in a continuous power-law Schoenberg family, and the previously qualitative equatorial nondifferentiability is quantitatively resolved into an exact logarithmic law, together with a sharp fractional Hölder regime and a differentiable regime. The general interior smoothness theorem of Trübner and Ziegel (2016) yields differentiability lower bounds but does not give these pointwise power-law constants. Classical Darboux and sine-series formulas are essential tools, and no novelty is claimed for those ingredients.

## Limitations

This is not a claim of a new general optimal-regularity theorem on all even spheres. It concerns the explicit two-sphere family and the neighborhood of one interior point. The Ge construction and classical special-function asymptotics make this conclusion potentially derivable by established methods; older Legendre-series literature might contain an equivalent quantitative cusp law. Strict positive definiteness does not assert any fixed positive lower Gram bound independent of sampling points. Numerical checks are finite and cannot establish the infinite asymptotics. The result has not undergone independent mathematical audit.

## References

1. Yan Ge, *Optimal differentiability of isotropic positive definite functions on even-dimensional spheres*, arXiv:2608.26092 (initially public 2026-08-26), https://arxiv.org/abs/2608.26092.
2. M. Trübner and J. F. Ziegel, *Derivatives of isotropic positive definite functions on spheres*, arXiv:1603.06727 (2016), https://arxiv.org/abs/1603.06727.
3. J. F. Ziegel, *Convolution roots and differentiability of isotropic positive definite functions on spheres*, arXiv:1201.5833 (2012), https://arxiv.org/abs/1201.5833.
4. NIST Digital Library of Mathematical Functions, §18.15(i),(iii), interior Darboux asymptotics of Jacobi and Legendre polynomials, https://dlmf.nist.gov/18.15.
