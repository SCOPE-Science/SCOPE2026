# Unique mortality peak and reentrant mean-field viability under clipped Gaussian habitat noise

## Finding
Fix a lower habitat-quality floor \(\varepsilon>0\), a baseline quality \(A>\varepsilon\), a payoff multiplier \(t>0\), and a standard normal variable \(Z\). For \(\sigma\geq0\), define the exact annealed death probability
\[
D_{A,\varepsilon,t}(\sigma)=\mathbb E\left[\frac{1}{1+t\max\{\varepsilon,A+\sigma Z\}}\right].
\]
For every such parameter triple, \(D_{A,\varepsilon,t}\) has **exactly one strict maximum** on \((0,\infty)\): it strictly increases before the maximum and strictly decreases afterwards. Moreover,
\[
D_{A,\varepsilon,t}(0)=\frac{1}{1+tA},\qquad
\lim_{\sigma\to\infty}D_{A,\varepsilon,t}(\sigma)=\frac{1}{2(1+t\varepsilon)}.
\]
The death probability therefore crosses its zero-noise level exactly once at a finite positive intensity if and only if \(A<2\varepsilon+1/t\). The crossing is downward and occurs after the unique maximum. At equality the large-noise limit equals the initial value, but there is no finite positive crossing; above equality there is no downward crossing.

In the pure-defector mean-field habitat-growth approximation defined below, take \(\varepsilon=1/100\), \(t=1\), \(A=18/25\). The predicted boundary velocity is **positive at zero noise, negative at \(\sigma=1\), and positive again for all sufficiently large \(\sigma\)**. There are exactly two positive threshold intensities \(0<\sigma_1<\sigma_2\), with predicted growth precisely when \(0\leq\sigma<\sigma_1\) or \(\sigma>\sigma_2\), and predicted decline when \(\sigma_1<\sigma<\sigma_2\). Supplementary numerical quadrature gives \(\sigma_1\approx0.14778817547\) and \(\sigma_2\approx6.48017158127\), but their existence and uniqueness are proved without those approximations.

## Assumptions and scope
The quality sampled at each independent environmental draw is \(Q_\sigma=\max\{\varepsilon,A+\sigma Z\}\). This implements the positive floor used in Kim, Son and Park's 2026 annealed-noise simulation rule. All calculations concern the **exact expectation of the microscopic mortality rule**, without a small-noise Taylor approximation. The ecological corollary concerns the pure-defector, no-mutation, mean-field occupancy approximation of Park et al., with environmental mortality replaced by this exact expectation. It does **not** assert growth or extinction of the original stochastic spatial lattice, and the post-clipping mean quality \(\mathbb EQ_\sigma\) is not held fixed as \(\sigma\) varies.

Let \(d\in(0,1)\) denote the resulting effective death probability. The mean-field occupied fraction and one-sided boundary velocity are
\[
\rho(d)=\frac{3-\sqrt{1+4d}}2,\qquad
V(d)=1-\frac{d}{\rho(d)}.
\]
A conventional two-sided velocity differs only by a positive factor of two and hence has the same sign. The exact sign threshold is
\[
V(d)>0\ \Longleftrightarrow\ d<d_c,\qquad d_c=2-\sqrt2.
\]

## Proof
Put \(f(x)=1/(1+tx)\), \(d_0=A-\varepsilon>0\), and \(g(x)=-f'(x)=t/(1+tx)^2\), which is strictly positive and strictly decreasing for \(x\ge\varepsilon\). Differentiating the continuous clipped integrand for \(\sigma>0\), then changing variables \(u=\sigma|Z|\), yields the exact identity
\[
\sqrt{2\pi}\,\sigma^2D'(\sigma)=P(\sigma)-N(\sigma),
\]
where
\[
P(\sigma)=\int_0^{d_0}u\bigl(g(A-u)-g(A+u)\bigr)e^{-u^2/(2\sigma^2)}\,du,
\]
\[
N(\sigma)=\int_{d_0}^{\infty}u g(A+u)e^{-u^2/(2\sigma^2)}\,du.
\]
Both are strictly positive. On the support of \(P\), \(u<d_0\); on the support of \(N\), \(u>d_0\). Writing \(\lambda=1/(2\sigma^2)\), logarithmic differentiation gives
\[
\frac{d}{d\lambda}\log\frac{N}{P}
=-\mathbb E_N[u^2]+\mathbb E_P[u^2]<0,
\]
where the expectations are under the respectively normalized integral weights. Therefore \(N/P\) increases strictly with \(\sigma\). As \(\sigma\downarrow0\), the Gaussian tail beyond \(d_0\) is exponentially smaller than the positive contribution from \(u\) near zero, so \(N/P\to0\). As \(\sigma\to\infty\), \(P\) tends to a positive finite limit, while \(N\to\infty\) because \(u g(A+u)\sim1/(tu)\). Hence \(N/P\) crosses one exactly once; this proves the strict single-peak statement.

For each \(Z<0\), \(Q_\sigma\to\varepsilon\) as \(\sigma\to\infty\); for each \(Z>0\), \(Q_\sigma\to\infty\). Dominated convergence proves the stated half-floor mortality limit. The single-peak profile then gives the complete zero-noise crossing classification by comparison of \(f(A)\) with \(f(\varepsilon)/2\): the strict inequality \(f(\varepsilon)/2<f(A)\) is equivalent to \(A<2\varepsilon+1/t\).

For the mean-field corollary, substituting \(\rho(d)\) into \(V(d)\) and squaring only positive quantities proves \(V(d)>0\) exactly when \(d<2-\sqrt2\). In the stated rational example,
\[
D(0)=\frac{25}{43}<2-\sqrt2,\qquad
D(\infty)=\frac{50}{101}<2-\sqrt2.
\]
It remains to certify \(D(1)>2-\sqrt2\). Put \(x=71/100\), \(p=\Phi(-x)\) and \(\varphi=(2\pi)^{-1/2}e^{-x^2/2}\). Elementary alternating Taylor bounds for the Gaussian integral and exponential give the rationally verified bounds \(0.238<p<0.240\), \(0<\varphi<0.312\). Conditioning on \(Z>-x\) and applying Jensen's inequality to the convex function \(f(y)=1/(1+y)\) yields
\[
D(1)\ge\frac{p}{1+\varepsilon}
+\frac{(1-p)^2}{(1+A)(1-p)+\varphi}
>\frac{6059777}{10242915}>\frac{59}{100}>2-\sqrt2.
\]
The displayed strict lower bound uses the rational endpoints \(0.238\), \(0.240\), \(0.312\). Since \(D\) has only one peak, the three strict signs imply exactly two crossings of \(d_c\), one on either side of its maximum. Their order and the corresponding signs of \(V(D(\sigma))\) follow.

## Verification
The standalone `check_reentrant.py` checks the rational interval enclosure of \(1/\sqrt{2\pi}\), alternating Gaussian-integral bounds, conditional-Jensen lower bound, and strict endpoint inequalities using exact rational arithmetic. Its optional high-precision quadrature independently locates the two crossings for diagnostic purposes; the proof does not rely on quadrature. Run `python check_reentrant.py` with Python 3; `mpmath` is optional.

## Relationship to prior work
Kim, Son and Park (2026, arXiv:2606.18660v1, Sections II–IV) introduce Gaussian environmental quality, truncate it below at \(\varepsilon=0.01\), and analyze annealed mortality with a second-order small-noise expansion. Their noise-dependent phase figures cover \(\sigma\le0.5\), not the exact all-intensity question here. Park et al. (2023, Journal of Theoretical Biology 575, 111629, pp. 2–3) supply the deterministic pure-defector mean-field density and growth proxy but not fluctuating Gaussian quality. General rectified-Gaussian formulas and older noise-induced reentrant transitions are prior knowledge; the specific global single-peak mortality theorem and the two-crossing corollary are not claimed to be a general discovery of reentrance in stochastic systems.

## Limitations
The ecological boundary is a **formal mean-field sign**, not a proven stochastic survival threshold. The exact finite-noise correction depends on a fixed pre-clipping Gaussian mean; changing variance also changes the actual mean quality after clipping. Large-noise behavior relies decisively on retaining the floor while allowing an unbounded positive tail. The originating small-noise phase boundaries should not be extrapolated unchanged. Independent historical-priority evaluation of broad censored-normal response theorems and noise-induced transition literature remains worthwhile. The reported numerical transition values are only supporting diagnostics.

## References
1. J. Kim, S.-W. Son and H. J. Park, *Effects of spatial environmental noise on evolution of cooperation*, arXiv:2606.18660v1 (first publicly released 2026-06-17), https://arxiv.org/abs/2606.18660.
2. H. J. Park, C. Hilbe, M. A. Nowak, B. J. Kim and H.-C. Jeong, *Vacancies in growing habitats promote the evolution of cooperation*, Journal of Theoretical Biology **575**, 111629 (2023), https://christian-hilbe.github.io/files/2023_park.pdf.
3. C. Van den Broeck, J. M. R. Parrondo, R. Toral and R. Kawai, *Nonequilibrium phase transitions induced by multiplicative noise*, Physical Review E **55**, 4084 (1997), https://doi.org/10.1103/PhysRevE.55.4084.
