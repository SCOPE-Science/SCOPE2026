# A sharp Gaussian-reset separation threshold for modal survival

## Finding
Consider free one-dimensional Brownian diffusion with independent Poisson resets. At each reset the new position is drawn afresh, with equal probability, from either \(N(-a,\sigma^2)\) or \(N(a,\sigma^2)\). Fix \(D,r,\sigma>0\), put \(b=\sqrt{D/r}\), and allow \(a\geq0\). Write \(\phi_\sigma\) for the centered Gaussian density with standard deviation \(\sigma\), \(L_b(x)=e^{-|x|/b}/(2b)\), and \(g_b=\phi_\sigma*L_b\). The invariant position density is
\[
p_a(x)=\frac{g_b(x-a)+g_b(x+a)}2.
\]
There is exactly **one** critical separation \(a_c=a_c(b,\sigma)>\sigma\), characterized by the scalar equation
\[
\boxed{g_b(a_c)=\phi_\sigma(a_c).}
\]
The entire stationary-modal phase diagram is as follows: for \(0\leq a<a_c\), the unique mode is a strict maximum at the origin; for \(a=a_c\), the origin is still the unique strict maximum but is quartically flat; for \(a>a_c\), the origin is a strict minimum and there are exactly two strict modes \(\pm m(a)\), with \(0<m(a)<a\). There are no other stationary points in any case. At the boundary,
\[
p_{a_c}''(0)=0,\qquad p_{a_c}^{(4)}(0)=-\frac{\phi_\sigma''(a_c)}{b^2}<0.
\]
The two peaks open continuously with an exact square-root law,
\[
\boxed{m(a)=\left(\frac{-6g_b'''(a_c)}{g_b^{(4)}(a_c)}\right)^{1/2}(a-a_c)^{1/2}+O((a-a_c)^{3/2}),\qquad a\downarrow a_c\ \text{from above}.}
\]
Both derivatives determining this positive coefficient are explicit through the resolvent equation. The limiting thresholds, with \(\sigma\) fixed, are
\[
\boxed{a_c=\sigma+\frac{b^2}{\sigma}+O\!\left(\frac{b^4}{\sigma^3}\right)\quad (b/\sigma\downarrow0),}
\]
\[
\boxed{\frac{a_c^2}{2\sigma^2}=\log\!\left(\sqrt{\frac2\pi}\frac b\sigma\right)+o(1)\quad(b/\sigma\to\infty).}
\]
In particular, the reset-location law is already bimodal when \(a>\sigma\), but Brownian excursions erase those two modes until \(a>a_c\). Infrequent resetting requires a separation of order \(\sigma\sqrt{2\log(b/\sigma)}\) to retain bimodality in stationarity.

## Assumptions and scope
The particle follows \(dX_t=\sqrt{2D}\,dW_t\) between resets. Resets occur according to an independent rate-\(r\) Poisson process, instantaneously replace the entire position, and independently select \(\frac12N(-a,\sigma^2)+\frac12N(a,\sigma^2)\) at every event. There is no absorption, confinement, interaction, finite observation window, or position-dependent resetting. All modal statements concern the unique invariant real-line probability density. In this theorem, a *mode* means a local maximum of the stationary spatial density; an *additional stationary point* means a real zero of its derivative. The width parameter \(\sigma\) is strictly positive, so the density is smooth. The no-reset limit \(r=0\) is excluded. The asymptotics hold at fixed positive \(\sigma\), with the other parameters varied through \(b=\sqrt{D/r}\).

## Proof
**1. Exact renewal kernel.** At stationarity, the backward time since the last Poisson reset is exponentially distributed with density \(re^{-rt}\). Conditional on that time, the particle's displacement is Gaussian with variance \(2Dt\), independent of its freshly drawn reset position. Hence
\[
p_a(x)=\frac r2\int_0^\infty e^{-rt}\bigl[\phi_{\sqrt{\sigma^2+2Dt}}(x-a)+\phi_{\sqrt{\sigma^2+2Dt}}(x+a)\bigr]dt.
\]
The centered displacement accumulated since the last reset has characteristic function \(r/(r+Dk^2)=1/(1+b^2k^2)\), which is the transform of \(L_b\). Thus the displayed formula for \(p_a\) follows and proves normalizability, uniqueness and smoothness. Equivalently, \(g_b\) obeys the resolvent identity
\[
\boxed{g_b-b^2g_b''=\phi_\sigma.}\tag{1}
\]
Since a Laplace random variable is a Gaussian variance mixture, the same kernel also has the *positive* representation
\[
g_b(x)=\int_0^\infty e^{-u}\phi_{\sqrt{\sigma^2+2b^2u}}(x)\,du.\tag{2}
\]
All derivatives used below exist by Gaussian smoothing.

**2. Exactly one positive inflection point, strictly beyond the Gaussian threshold.** Divide (2) by \(\phi_\sigma(x)\). For every \(u>0\),
\[
\frac{\phi_{\sqrt{\sigma^2+2b^2u}}(x)}{\phi_\sigma(x)}=\frac{\sigma}{\sqrt{\sigma^2+2b^2u}}\exp\!\left[\frac{x^2}2\left(\frac1{\sigma^2}-\frac1{\sigma^2+2b^2u}\right)\right]
\]
is strictly increasing in \(x>0\). Therefore \(R(x)=g_b(x)/\phi_\sigma(x)\) is strictly increasing for \(x>0\). It satisfies \(R(0)<1\), while \(R(x)\to\infty\) because \(g_b\) has exponential tails and \(\phi_\sigma\) Gaussian tails. A unique positive solution \(a_c\) of \(R(a_c)=1\) follows. Equation (1) gives
\[
g_b''(x)<0\quad(0\le x<a_c),\qquad g_b''(x)>0\quad(x>a_c).\tag{3}
\]
Every wider Gaussian in (2) has \(\phi_s''(\sigma)=(\sigma^2-s^2)\phi_s(\sigma)/s^4<0\) when \(s>\sigma\), so \(g_b''(\sigma)<0\), and consequently \(a_c>\sigma\). At the crossing, \(R'(a_c)>0\) implies
\[
g_b'''(a_c)=\frac{g_b'(a_c)-\phi_\sigma'(a_c)}{b^2}>0.\tag{4}
\]
Differentiating (1) twice and using \(g_b''(a_c)=0\) yields
\[
g_b^{(4)}(a_c)=-\frac{\phi_\sigma''(a_c)}{b^2}<0,\tag{5}
\]
because \(a_c>\sigma\). Formula (2) also implies \(g_b'(x)<0\) for all \(x>0\).

**3. Global mode count, not merely a local curvature test.** Let \(h_a(x)=[L_b(x-a)+L_b(x+a)]/2\), so \(p_a=\phi_\sigma*h_a\). For \(a>0\), its ordinary derivative \(h_a'\), away from the finitely many cusp points, has the successive strict sign pattern \(+,-,+,-\) on the intervals cut by \(-a,0,a\). It is integrable and has exactly three sign changes. The Gaussian convolution is strictly variation diminishing: convolution with a Gaussian cannot increase the number of zeros of such a derivative, counted with multiplicity, beyond the number of sign changes of its input. For completeness, this standard fact here reduces to the generalized Descartes argument: after multiplication by the positive function \(e^{x^2/(2\sigma^2)}\), \(p_a'(x)\) is an exponential transform \(F(x)=\int e^{xy/\sigma^2}\,d\mu(y)\), where \(d\mu(y)=e^{-y^2/(2\sigma^2)}h_a'(y)dy\) has three ordered sign changes. Induct on their number. At a sign boundary \(c\), differentiating \(e^{-cx/\sigma^2}F(x)\) multiplies its representing signed measure by \((y-c)/\sigma^2\), deleting that sign change. Rolle's theorem, with multiplicities, bounds the real zero count by the number of input sign changes. For zero sign changes the transform has a fixed sign. Thus \(p_a'\) has at most three real zeros counted with multiplicity. For \(a=0\), \(p_0=g_b\) and \(g_b'<0\) on the positive half-line.

By symmetry \(p_a'(0)=0\) and \(p_a''(0)=g_b''(a)\). If \(a<a_c\), the derivative is negative just to the right of zero, and the derivative is also negative for \(x>a\), since both translated derivatives \(g_b'(x-a),g_b'(x+a)\) are negative. Any extra positive zero would require another zero farther right to restore the negative tail sign, accounting with its symmetric counterpart for at least five real zeros in total (and tangent zeros count twice). This contradicts the three-zero bound. If \(a>a_c\), the derivative is positive just to the right of zero and negative beyond \(a\), forcing a positive root. The three-zero bound permits exactly one simple positive root and its negative reflection. At \(a=a_c\), equations (3) and (5) show a cubic zero of \(p_a'\) at the origin with negative cubic coefficient; the zero bound excludes any others. This proves the complete mode classification and strictness, including the critical quartic maximum.

**4. Peak-opening law.** Set \(\delta=a-a_c\). Even analyticity around the origin gives, uniformly for small \(\delta\) and \(x\),
\[
\frac{p_a'(x)}x=g_b'''(a_c)\delta+\frac{g_b^{(4)}(a_c)}6x^2+O(\delta^2+|\delta|x^2+x^4).\tag{6}
\]
Since the linear coefficient is positive by (4) and the coefficient of \(x^2\) is negative by (5), the implicit-function theorem in variables \((\delta,x^2)\) gives \(x^2=[-6g_b'''(a_c)/g_b^{(4)}(a_c)]\delta+O(\delta^2)\) for the unique positive stationary point when \(\delta>0\). Taking its positive square root proves the stated coefficient and error. The derivative is negative for \(x>a\), so that point lies in \((0,a)\).

**5. Strong- and weak-reset limits.** The Laplace kernel has centered second moment \(2b^2\) and fourth moment \(24b^4\). Taylor expansion of the convolution, with Gaussian derivatives uniformly controlled near \(x=\sigma\), yields \(g_b''(x)=\phi_\sigma''(x)+b^2\phi_\sigma^{(4)}(x)+O(b^4/\sigma^7)\). The needed Gaussian derivative identities are \(\phi_\sigma'''(\sigma)=2\phi_\sigma(\sigma)/\sigma^3\) and \(\phi_\sigma^{(4)}(\sigma)=-2\phi_\sigma(\sigma)/\sigma^4\). By the nonzero derivative of the unperturbed curvature at \(\sigma\), the unique zero shifts by \(b^2/\sigma+O(b^4/\sigma^3)\), proving the first expansion.

For the opposite limit, write \(g_b(x)=\mathbb E[e^{-|x-Y|/b}]/(2b)\), with \(Y\sim N(0,\sigma^2)\). The triangle inequality and Jensen's inequality give, for \(x\ge0\),
\[
\frac{e^{-(x+\sigma\sqrt{2/\pi})/b}}{2b}\le g_b(x)\le\frac1{2b}.\tag{7}
\]
At \(x=a_c\), substituting \(g_b(a_c)=\phi_\sigma(a_c)\) and taking logarithms yields, with \(H=\log(\sqrt{2/\pi}\,b/\sigma)\),
\[
H\le \frac{a_c^2}{2\sigma^2}\le H+\frac{a_c+\sigma\sqrt{2/\pi}}b.\tag{8}
\]
The right inequality first gives \(a_c=O(\sigma\sqrt{\log(b/\sigma)})\) as \(b/\sigma\to\infty\). Consequently its remainder tends to zero and (8) gives the asserted logarithmic law.

## Verification
The standalone program `checker.py` (Python 3.10 or later with SciPy and SymPy) independently evaluates the Gaussian variance-mixture derivative, the original Poisson renewal-age integral, the exact Fourier resolvent, selected strict derivative signs and off-center peaks, the nondegenerate peak-opening coefficient and both endpoint expansions. Run `python checker.py` from the directory containing this result. It passed 213 deterministic formula, sign and asymptotic assertions. For \(b=\sigma=1\), the critical separation is approximately \(1.300922293201194\). These are numerical reproducibility checks, not proofs of the global zero count or the limiting asymptotic statements; the analytic argument above supplies those.

## Relationship to prior work
Toledo-Marín and Boyer [1] develop stochastic resetting to random Gaussian-distributed positions and analyze first-passage time, entropy, and parity-dependent Gaussian protocols. Besga and collaborators [2] likewise investigate Gaussian reset-position randomness and first-passage optimization. The present question concerns the *number of stationary spatial modes* for a symmetric two-Gaussian reset distribution; none of those cited first-passage analyses is claimed here as supplying the threshold or its proof. Reed [3] derives the one-component normal-Laplace law, which is exactly the building-block density \(g_b\); no novelty is claimed for that convolution. The equal-weight two-normal mixture has its classical modal threshold at \(a=\sigma\) [4], recovered here only as a singular strong-reset limit. The finite-\(b\) unique root, global two-mode classification, square-root splitting and weak-reset logarithmic suppression are the proposed additions. The Gaussian variation-diminishing property and exponential-transform zero-count arguments are standard mathematical tools, not newly invented principles. Published results for harmonic confinement with symmetric point resetting and for Gaussian-smoothed run-and-tumble laws address different stationary kernels and do not imply this theorem without new analysis.

## Limitations
The claims require exactly two equally weighted Gaussian reset-location components with the same variance and free Brownian motion. They do not cover arbitrary reset measures, unequal weights, non-Poisson clocks, absorbing targets, or general confinement. The result is an exact stationary theorem, not a claim about finite-sample detectability. Earlier general formulas for stochastic resetting and normal-Laplace densities make implicit or unindexed prior coverage a genuine publication-priority risk; mathematical originality is judged against the specifically inspected sources, not certified globally. Independent scientific validation has not been performed.

## References
1. J. Q. Toledo-Marín and D. Boyer, *First passage time and information of a one-dimensional Brownian particle with stochastic resetting to random positions*, arXiv:2206.14387, first posted 2022-06-29. https://arxiv.org/abs/2206.14387
2. B. Besga et al., *Optimal mean first-passage time for a Brownian searcher subjected to resetting: experimental and theoretical results*, arXiv:2004.11311, first posted 2020-04-21. https://arxiv.org/abs/2004.11311
3. W. J. Reed, *The Normal-Laplace Distribution and Its Relatives*, 2006 book chapter (author manuscript circulated earlier). https://www.researchgate.net/publication/227147267_The_Normal-Laplace_Distribution_and_Its_Relatives
4. Classical symmetric equal-variance two-Gaussian mixture mode criterion; see R. S. Ray and B. G. Lindsay, *The topography of multivariate normal mixtures*, Annals of Statistics 33 (2005), 2042–2065. https://doi.org/10.1214/009053605000000417
