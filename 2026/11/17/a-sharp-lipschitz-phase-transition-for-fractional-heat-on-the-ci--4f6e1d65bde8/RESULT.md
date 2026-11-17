# A sharp Lipschitz phase transition for fractional heat on the circle

## Finding

On the real Lipschitz space modulo constants of the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), let \(S_{\alpha,t}=\exp[-t(-\partial_\theta^2)^\alpha]\), for \(0<\alpha\le1\), \(t\ge0\). Its exact Lipschitz-seminorm operator norm is
\[
L_\alpha(t)=\frac4\pi\sum_{j=0}^\infty\frac{(-1)^j}{2j+1}\exp[-t(2j+1)^{2\alpha}],\qquad t>0,
\]
with \(L_\alpha(0)=1\). One fixed triangular-wave Lipschitz function, independent of \(\alpha\) and \(t\), attains the norm for all \(\alpha,t>0\). All real norm-attainers for fixed \(\alpha,t>0\) are its translations, signs, additive constants and nonzero scalings.

The short-time deficit has two different sharp regimes. Set
\[
c_\alpha=\frac{4^\alpha\Gamma(\alpha+1/2)}{\sqrt\pi\,|\Gamma(-\alpha)|},\quad
\beta(s)=\sum_{m=0}^\infty\big[(4m+1)^{-s}-(4m+3)^{-s}\big]\quad(s>0).
\]
For every fixed \(0<\alpha<1\),
\[
1-L_\alpha(t)=\kappa_\alpha t+o(t),\qquad
\kappa_\alpha=\frac{2c_\alpha}{\alpha}\left(\frac2\pi\right)^{2\alpha}\beta(2\alpha)>0.
\]
For the local endpoint \(\alpha=1\), instead,
\[
1-L_1(t)\sim\frac{8\sqrt t}{\pi\sqrt\pi}\exp\!\left(-\frac{\pi^2}{16t}\right),\qquad t\downarrow0.
\]
Therefore the exact first-order contraction loss is strictly positive for every nonlocal exponent but zero to every algebraic order at the classical heat endpoint. At \(\alpha=1/2\), the complete formula reduces to \(L_{1/2}(t)=\frac4\pi\arctan(e^{-t})\); for every fixed \(\alpha>0\), \(L_\alpha(t)\sim(4/\pi)e^{-t}\) as \(t\to\infty\).

## Assumptions and scope

All functions are real, \(2\pi\)-periodic and Lipschitz for the geodesic arc metric. The seminorm is \(\operatorname{Lip}(f)=\operatorname*{ess\,sup}|f'|\), with constants factored out. The fractional generator is the Fourier multiplier \(|m|^{2\alpha}\) on mode \(m\in\mathbb Z\). At \(t>0\), the convolution kernel \(k_{\alpha,t}\) is smooth, positive, even, and normalized by \(\int_{-\pi}^\pi k_{\alpha,t}(x)\,dx=1\). Every asymptotic is for a fixed exponent, not uniform as \(\alpha\uparrow1\) or \(\alpha\downarrow0\).

## Proof

**1. Exact dual norm.** A periodic real Lipschitz function has derivative \(g\in L^\infty(\mathbb T)\) with \(\|g\|_\infty=\operatorname{Lip}(f)\) and \(\int_{-\pi}^\pi g=0\), and conversely every mean-zero bounded real \(g\) is such a derivative. Differentiation commutes with convolution. Consequently, at each evaluation point, by the duality of \(L^\infty\) modulo mean zero and \(L^1\) modulo constants,
\[
\sup_{\|g\|_\infty\le1,\ \int g=0}\left|\int k_{\alpha,t}(x-y)g(y)\,dy\right|=\inf_{c\in\mathbb R}\int_{-\pi}^\pi|k_{\alpha,t}(y)-c|\,dy.
\]
The right-hand side is independent of \(x\).

**2. Strict radial unimodality.** Write \(q=e^{-s}\). The ordinary circular heat density has Jacobi product
\[
2\pi k_{1,s}(x)=\prod_{m=1}^\infty(1-q^{2m})(1+2q^{2m-1}\cos x+q^{4m-2}),\qquad s>0.
\]
All factors are positive, and the second factor is strictly increasing in \(\cos x\); their convergent product is strictly decreasing on \(0<x<\pi\). For \(0<\alpha<1\), positive stable subordination gives \(k_{\alpha,t}(x)=\int_0^\infty k_{1,s}(x)\,\mu_{\alpha,t}(ds)\), where \(\int e^{-\lambda s}\mu_{\alpha,t}(ds)=e^{-t\lambda^\alpha}\). Therefore every \(k_{\alpha,t}\) is strictly decreasing with geodesic distance on \((0,\pi)\). Its unique median level is \(k_{\alpha,t}(\pi/2)\): the sets above and below this level both have length \(\pi\). The dual-norm identity becomes
\[
L_\alpha(t)=2\int_{-\pi/2}^{\pi/2}k_{\alpha,t}(y)\,dy-1.
\]
Take \(g(y)=+1\) on \((-\pi/2,\pi/2)\) and \(g(y)=-1\) on its complementary semicircle and integrate once to obtain the common triangular-wave extremizer. Strict radial monotonicity and the equality condition in the \(L^1\)-\(L^\infty\) dual bound force any norm-attaining derivative to equal its translated signed pattern a.e. This proves the rigidity statement, including both signs.

**3. Full profile.** The normalized Fourier expansion is \(k_{\alpha,t}(y)=(2\pi)^{-1}[1+2\sum_{m\ge1}e^{-tm^{2\alpha}}\cos(my)]\). Integrating over the half-circle yields the claimed absolutely convergent alternating odd-mode series for \(t>0\). Its first mode gives the long-time asymptotic, since \(3^{2\alpha}>1\). The elementary arctangent series yields the explicit Poisson case \(\alpha=1/2\).

**4. Nonlocal short-time slope.** For \(0<\alpha<1\), the Lévy kernel of the generator, relative to Lebesgue measure on the \(2\pi\)-circle, is
\[
\nu_\alpha(y)=c_\alpha\sum_{\ell\in\mathbb Z}|y+2\pi\ell|^{-1-2\alpha},\qquad y\not\equiv0\pmod{2\pi}.
\]
The normalization follows by integrating the subordinated ordinary Gaussian kernel and multiplying by the subordinator coefficient \(1/|\Gamma(-\alpha)|\): \(\int_0^\infty(4\pi s)^{-1/2}e^{-z^2/(4s)}s^{-1-\alpha}ds=4^\alpha\Gamma(\alpha+1/2)|z|^{-1-2\alpha}/\sqrt\pi\). Let \(A=(-\pi/2,\pi/2)\) modulo \(2\pi\). The elementary Lévy small-time jump limit for sets bounded away from the starting point, obtained here by approximating \(\mathbf1_{A^c}\) from inside/outside by smooth functions in the generator formula, gives
\[
\lim_{t\downarrow0}\frac{1}{t}\int_{A^c}k_{\alpha,t}(y)\,dy=\int_{A^c}\nu_\alpha(y)\,dy.
\]
The boundary points have zero Lévy mass. Unfolding the complement into positive real intervals \([\pi/2+2\pi m,3\pi/2+2\pi m]\), \(m\ge0\), and their negatives, shows
\[
\int_{A^c}\nu_\alpha(y)\,dy
=\frac{c_\alpha}{\alpha}\left(\frac2\pi\right)^{2\alpha}\sum_{m=0}^\infty[(4m+1)^{-2\alpha}-(4m+3)^{-2\alpha}].
\]
Because \(1-L_\alpha(t)=2\int_{A^c}k_{\alpha,t}\), this yields precisely \(\kappa_\alpha\), with strict positivity and convergence of the paired Dirichlet-beta series for all \(\alpha>0\).

**5. Local short-time boundary layer.** At \(\alpha=1\) the heat density is the periodized Gaussian
\[
k_{1,t}(y)=\sum_{\ell\in\mathbb Z}(4\pi t)^{-1/2}\exp[-(y+2\pi\ell)^2/(4t)].
\]
Its mass outside \(A\) is \(2\Phi[-\pi/(2\sqrt{2t})]\) up to errors exponentially smaller than \(\exp[-\pi^2/(16t)]\), since the next closest wrapped interval begins at distance \(3\pi/2\). Thus \(1-L_1(t)=4\Phi[-\pi/(2\sqrt{2t})](1+o(1))\). The Gaussian Mills asymptotic \(\Phi(-z)\sim e^{-z^2/2}/(z\sqrt{2\pi})\) gives the displayed constant and exponent.

## Verification

`check.py` uses independent periodized-Gaussian quadrature, two Fourier series, the exact Poisson arctangent identity, the gamma--Dirichlet-beta coefficient, and asymptotic Gaussian comparisons. Its successful checks are reported in `VERIFICATION.md`. These finite numerical checks do not establish universal or limiting assertions; the proof above does.

## Relationship to prior work

Roncal--Stinga give the fractional-torus generator and its correctly normalized positive singular kernel and Poisson kernel; these are used as premises, not claimed new. Bolley--Gentil--Guillin study semigroup contraction in a transportation metric without the sharp \(\operatorname{Lip}\to\operatorname{Lip}\) fractional-circle constants. The known finite-cycle heat and Fejér norm calculations use similar median geometry, but their statements concern different kernels or discrete state spaces. Aldous--Fill's antipodal Brownian-circle total-variation calculation covers the classical \(\alpha=1\) endpoint; no novelty is claimed for that isolated endpoint or for the classical Poisson formula. The claim is the unified exact fractional-family norm, common extremizer/equality classification and strictly positive Dirichlet-beta jump-loss law together with the singular local endpoint.

## Limitations

The result is restricted to one-dimensional circles of circumference \(2\pi\), real Lipschitz seminorms and isotropic fractional powers with \(0<\alpha\le1\). It does not assert analogous formulas in higher dimensions, for nonsymmetric generators, or uniform short-time asymptotics when \(\alpha\) depends on \(t\). Independent mathematical review remains outstanding; historical priority beyond the inspected literature is not established.

## References

1. L. Roncal and P. R. Stinga, *Fractional Laplacian on the torus*, arXiv:1209.6104, first public arXiv record 2012-09-27. Relevant material: the Fourier multiplier, Theorem 3.4 and Section 5. https://arxiv.org/abs/1209.6104
2. F. Bolley, I. Gentil and A. Guillin, *Dimensional contraction via Markov transportation distance*, arXiv:1304.1929, first public arXiv record 2013-04-06. Relevant material: Introduction, Sections 2 and 4. https://arxiv.org/html/1304.1929v3
3. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, continuous-state chapter, Section 13.1; Brownian circle coupling and antipodal total-variation formulas. https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch13.S1.html
4. Jacobi triple-product identity for the circular heat theta kernel (classical identity). https://en.wikipedia.org/wiki/Jacobi_triple_product
