# A sharp source-count exponent transition for luminosity scatter in finite flux-limited surveys

## Finding

Let \(q>0\) denote a radial source-count exponent: the fraction of a parent population within radius \(r\in[0,R]\) is \((r/R)^q\). Let all luminosities be independent of source distance and lognormal with the same **arithmetic** mean \(\bar L>0\), with variable log-variance \(t\ge0\):
\[
L_t=\bar L\exp(\sqrt t\,Z-t/2),\qquad Z\sim N(0,1).
\]
Sources are detected exactly when their inverse-square flux \(L_t/(4\pi r^2)\) exceeds a fixed limit \(f_{\min}>0\). Define \(L_c=4\pi R^2 f_{\min}\), \(x=\bar L/L_c\), and \(\alpha=q/2\). The fraction of the parent population detected is
\[
S_{q,x}(t)=\mathbb E\min\!\left\{1,\left(\frac{L_t}{L_c}\right)^\alpha\right\}.
\]

**Complete phase classification.** If \(0<q\le2\), or if \(q>2\) and \(x\ge1\), then \(S_{q,x}\) is strictly decreasing on \((0,\infty)\), and its unique optimum on \([0,\infty)\) is at zero scatter. If \(q>2\) and \(0<x<1\), then there is a unique \(t_*\in(0,\infty)\); the detection fraction is strictly increasing before \(t_*\) and strictly decreasing afterward. In the latter regime, writing \(d=\log x<0\), \(b=\alpha-\tfrac12\) and \(c=\alpha-1\), the unique optimum is the solution of
\[
\boxed{\int_0^\infty \exp\!\left[-\left(b+\frac d t\right)u-\frac{u^2}{2t}\right]\,du=\frac1c.}
\]
For every fixed \(q>2\), as \(x\downarrow0\) and \(h=\log(1/x)\to\infty\),
\[
t_*=2h-\frac{2}{\alpha-1}+O(h^{-1}),\qquad
S_{q,x}(t_*)\sim\frac{\alpha}{\alpha-1}\frac{x}{\sqrt{4\pi h}}.
\]
In particular the ideal homogeneous spatial case \(q=3\) has the strict scatter-benefit threshold \(\bar L<L_c\); for \(x=0.1\) the unique optimal log-variance is \(t_*=2.1511631932\ldots\), increasing the detected fraction from \(0.0316227766\ldots\) to \(0.0489697890\ldots\).

## Assumptions and scope

Fix a finite survey radius \(R>0\), an inverse-square flux law, a sharp positive flux limit, and a strictly positive radial count exponent \(q\). The radial CDF is exactly \((r/R)^q\) throughout the parent sample. Luminosity is independent of radius; the arithmetic mean \(\bar L\) is held fixed while its log-variance varies. The parent source count is fixed. The theorem optimizes the fraction detected **among this parent sample**, not an estimator of physical luminosity, distance, or total source abundance. For \(t=0\), luminosity is deterministic \(\bar L\). The argument allows noninteger effective radial exponents as mathematical power-law sampling models; it does not claim the observed universe possesses one fixed fractal dimension.

## Proof

**1. Exact reduction.** Conditional on \(L\), sources are visible out to \(r_{\max}=\sqrt{L/(4\pi f_{\min})}\), capped at \(R\). The radial count law therefore gives \(S_{q,x}(t)=\mathbb E\min\{1,X_t^\alpha\}\), where \(X_t=x\exp(\sqrt t\,Z-t/2)\). Put \(Y_t=\log X_t\) and let \(\Phi\) be the standard Gaussian CDF. Gaussian completion of squares gives, for \(t>0\),
\[
S_{q,x}(t)=x^\alpha e^{\alpha(\alpha-1)t/2}
\Phi\!\left(\frac{-d-(\alpha-\tfrac12)t}{\sqrt t}\right)
+\Phi\!\left(\frac{d-t/2}{\sqrt t}\right),\quad d=\log x.
\]
The boundary values are \(S_{q,x}(0)=\min\{1,x^\alpha\}\) and \(\lim_{t\to\infty}S_{q,x}(t)=0\). The latter follows also from \(X_t\to0\) in probability and bounded convergence in probability.

**2. Derivative.** Let \(M(t)=\mathbb E[e^{\alpha Y_t}\mathbf1_{Y_t<0}]\) and let \(p_t(0)=(2\pi t)^{-1/2}\exp[-(d-t/2)^2/(2t)]\) be the Gaussian density of \(Y_t\) at zero. Differentiation of the displayed Gaussian formula, cancelling the boundary-density terms, yields
\[
S'_{q,x}(t)=\frac\alpha2\bigl[(\alpha-1)M(t)-p_t(0)\bigr].
\]
Thus if \(\alpha\le1\) this derivative is strictly negative. For \(\alpha>1\), define \(c=\alpha-1>0\), \(b=\alpha-1/2=c+1/2\), and
\[
H(t)=\frac{M(t)}{p_t(0)}
=\int_0^\infty\exp\!\left[-\left(b+\frac d t\right)u-\frac{u^2}{2t}\right]du.
\]
The integral follows on substituting \(Y_t=-u\) and dividing by the density at zero. For \(d\ge0\), \(H(t)<1/b<1/c\), hence \(S'_{q,x}<0\).

**3. Uniqueness when \(d<0\).** In this case, Laplace's method at the positive maximizer of the integrand exponent gives \(H(t)\to\infty\) as \(t\downarrow0\), while dominated convergence gives \(H(t)\to1/b<1/c\) as \(t\to\infty\). Define \(G(t)=H(t)-1/c\). Elementary integration by parts of the first two moments of the integrand (or differentiation of the Gaussian closed form) yields
\[
2t^2H'(t)=(t+b^2t^2-d^2)H(t)+t(d-bt).
\]
Consequently,
\[
G'(t)=a(t)G(t)+\frac{Q(t)}{2ct^2},\quad
 a(t)=\frac{t+b^2t^2-d^2}{2t^2},\quad
 Q(t)=\frac b2t^2+(1+cd)t-d^2.
\]
The quadratic \(Q\) has exactly one positive root \(t_c\), because its leading coefficient is positive and \(Q(0)<0\). Let \(\rho(t)=\exp[-\int_1^t a(v)dv]>0\). Then \((\rho G)'=\rho Q/(2ct^2)\) is negative on \((0,t_c)\) and positive on \((t_c,\infty)\). Moreover \(a(t)\to b^2/2>0\), so \(\rho(t)G(t)\to0\) **from below** as \(t\to\infty\). Thus \(\rho G<0\) at and beyond \(t_c\). At sufficiently small positive \(t\), \(G>0\), and on \((0,t_c)\) the product \(\rho G\) is strictly decreasing. It therefore crosses zero exactly once. Since \(S'\) has the sign of \(G\), this proves the unique strict global maximum and the claimed rise–fall classification.

**4. Sharp faint-mean asymptotics.** Write \(d=-h\) and \(t=2h+s\), with \(s\) in a fixed bounded interval. As \(h\to\infty\), the defining integral has the uniform expansion
\[
H(2h+s)=\frac1c-\frac{1}{4h}\left(\frac{s}{c^2}+\frac2{c^3}\right)+O(h^{-2}).
\]
The expansion uses \(b-h/(2h+s)=c+s/(4h)+O(h^{-2})\), \((2t)^{-1}=(4h)^{-1}+O(h^{-2})\), and the first two moments of \(e^{-cu}\). Taking two bounded \(s\) values on either side of \(-2/c\), uniqueness brackets the root, then the same expansion implies \(s=-2/c+O(h^{-1})\). At that optimum, the defining equation gives \(M=p_t(0)/c\). Direct substitution shows \(p_t(0)\sim x/\sqrt{4\pi h}\), and the Gaussian right-tail probability is asymptotic to \(p_t(0)\), since its density ratio above zero converges pointwise to \(e^{-u}\) with a uniform integrable majorant. Hence \(S(t_*)=(1+1/c+o(1))p_t(0)\), which is the stated limiting law.

## Verification

Run `python3 verify.py` with Python 3 and no optional dependencies. The script checks the Gaussian formula independently against direct Simpson quadrature of the radius-conditioned selection probability, evaluates the derivative by symmetric differences, tests strict derivative signs and unique root bracketing for multiple parameters, and checks the three-dimensional sample and the faint-mean asymptotic. These finite numerical assertions are diagnostic only; the universal quantifiers, uniqueness and asymptotic statements are established by the four analytic proof steps above.

## Relationship to prior work

Sylos Labini, Gabrielli, Montuori and Pietronero derive general number–flux exponent and luminosity-selection integrals for power-law source counts in their 1996 analysis; in particular, their source-count exponent \(D/2\) and finite-volume formulas already give the general expectation whose **scatter-optimization problem** is studied here. The expectation's algebraic form is therefore not asserted to be new. Butkevich, Berdyugin and Teerikorpi develop classical integral, magnitude- and distance-conditioned Malmquist bias formulas for Gaussian absolute magnitudes. Nord and colleagues consider lognormal cluster luminosity scatter with flux-limited window functions, but mainly investigate selection bias and covariance at prescribed dispersion. The present claim concerns holding **arithmetic mean luminosity fixed** and optimizing observed fraction over all nonnegative log-variances, obtaining an exact threshold and unique optimizer. No priority claim is made for the classical inverse-square law, Malmquist bias, Gaussian-truncation formula or general likelihood-selection integrals.

## Limitations

The result is an idealized **conditional selection-yield** theorem. Survey volume, source count, radial exponent, flux limit and arithmetic mean luminosity remain fixed while a hypothetical distribution parameter varies. Real populations can have luminosity–distance correlation, evolving luminosity functions, dust extinction, cosmological redshift, instrumental thresholds, sky masks and non-lognormal tails. Effective power-law radial exponents need not be stable or physically literal; historical claims about observed galaxy fractality are contested. The numerical diagnostics are not exhaustive proof and the self-review is not independent validation. Historical priority, especially through mathematical-finance treatments of capped-power lognormal payoffs, is not exhaustively certified.

## References

1. Sylos Labini, F., Gabrielli, A., Montuori, M. and Pietronero, L. (1996), *Finite size effects on the galaxy number counts: evidence for fractal behavior up to the deepest scale*, first public arXiv posting 1996-05-22, https://arxiv.org/abs/astro-ph/9605135 .
2. Butkevich, A. G., Berdyugin, A. V. and Teerikorpi, P. (2005), *Statistical biases in stellar astronomy: the Malmquist bias revisited*, MNRAS 362:321–330, https://doi.org/10.1111/j.1365-2966.2005.09306.x .
3. Nord, B., Stanek, R., Rasia, E. and Evrard, A. E. (2007), *Effects of Selection and Covariance on X-ray Scaling Relations of Galaxy Clusters*, arXiv posting 2007-06-14, https://arxiv.org/abs/0706.2189 .
4. Teerikorpi, P. (1997), *Observational selection bias affecting the determination of the extragalactic distance scale*, Annual Review of Astronomy and Astrophysics 35:101–136, https://ned.ipac.caltech.edu/level5/March03/Teerikorpi/Teerikorpi2_2.html .
