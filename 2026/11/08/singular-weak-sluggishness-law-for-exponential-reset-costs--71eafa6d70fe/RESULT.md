# Singular weak-sluggishness law for exponential reset costs

## Finding

Consider the stationary continuum sluggish diffusion with Poisson resetting to the origin, diffusivity \(D(x)=|x|^{-\alpha}\), reset rate \(r>0\), and exponential distance cost \(c(x)=\exp(\lambda |x|)\), with \(\lambda>0\). Let \(Q_\alpha(r,\lambda)=r\mathbb E_\alpha[\exp(\lambda|X|)]\) be the stationary mean reset cost per unit time. The known fixed-\(\alpha\) results show that this is finite for all \(\alpha>0\), but at \(\alpha=0\) is infinite for \(\lambda\ge\sqrt r\). The following **three-regime singular limit** quantifies the crossover, for fixed \(r,\lambda>0\) as \(\alpha\downarrow0\):

1. If \(\lambda<\sqrt r\), then
   \[
   Q_\alpha(r,\lambda)\longrightarrow\frac{r\sqrt r}{\sqrt r-\lambda}.
   \]
2. If \(\lambda=\sqrt r\), then
   \[
   \boxed{Q_\alpha(r,\sqrt r)\sim\frac{2r}{\alpha\log(1/\alpha)}.}
   \]
3. If \(\lambda>\sqrt r\), put \(z=\lambda/\sqrt r>1\), \(p=\alpha+2\), and \(x_*=z^{2/\alpha}\). Let
   \[
   A_{\alpha,r}=\frac{r^{(2\alpha+3)/(2p)}}{\Gamma((\alpha+1)/p)p^{(\alpha+1)/p}},\qquad
   B_{\alpha,r}=A_{\alpha,r}\sqrt{\frac{\pi p}{\sqrt r}}.
   \]
   Then the **full equivalent**, rather than merely its logarithm, is
   \[
   \boxed{Q_\alpha(r,\lambda)\sim
   r B_{\alpha,r}x_*^{3\alpha/4}
   \sqrt{\frac{4\pi x_*}{\alpha\lambda}}
   \exp\!\left(\frac{\alpha\lambda x_*}{\alpha+2}\right).}
   \]
   In particular, \(B_{\alpha,r}\to\sqrt r\) and
   \[
   \log Q_\alpha(r,\lambda)\sim
   \frac{\alpha\lambda}{\alpha+2}\left(\frac{\lambda}{\sqrt r}\right)^{2/\alpha}.
   \]
   The saddle-point reset distance \(x_*\) diverges exponentially in \(1/\alpha\). All assertions hold for each fixed \(r,\lambda\); no uniformity as the ratio \(\lambda/\sqrt r\) approaches one is claimed.

## Assumptions and scope

Fix dimensionless \(r>0\), \(\lambda>0\). For \(\alpha\ge0\), the continuum limit of a one-dimensional sluggish random walk has the generator \(Lf(x)=|x|^{-\alpha}f''(x)\) away from the origin. Independent Poisson reset events of rate \(r\) send its position to zero. We use its stationary density (an established result in the primary source): for \(x\ne0\),
\[
p_{\alpha,r}(x)=A_{\alpha,r}|x|^{\alpha+1/2} K_{1/p}\!\left(\frac{2\sqrt r}{p}|x|^{p/2}\right),\quad p=2+\alpha.
\]
Here \(K_\nu\) is the modified Bessel \(K\)-function and \(A_{\alpha,r}\) is as defined above. The density is even and integrates to one, including at \(\alpha=0\), where \(p_{0,r}(x)=(\sqrt r/2)e^{-\sqrt r|x|}\). This is a continuum stationary cost-rate statement, not a first-passage or finite lattice cost statement.

## Proof

**Uniform large-position reduction.** For \(0\le\alpha\le\alpha_0\) with fixed sufficiently small \(\alpha_0\), \(1/p\) stays in a compact subinterval of \((0,1)\). The standard Bessel asymptotic \(K_\nu(t)=\sqrt{\pi/(2t)}e^{-t}(1+O(t^{-1}))\) is uniform over such \(\nu\). Consequently, for \(x\ge1\) with \(t_\alpha(x)=(2\sqrt r/p)x^{p/2}\) tending to infinity,
\[
2p_{\alpha,r}(x)=B_{\alpha,r}x^{3\alpha/4}e^{-t_\alpha(x)}(1+O(t_\alpha(x)^{-1})),
\]
where \(B_{\alpha,r}\to\sqrt r\). At finite \(x\), the explicit density converges to the Brownian density. The small-position Bessel expansion also bounds the densities uniformly by an integrable function on \((0,1)\).

**Subcritical regime.** At \(\lambda<\sqrt r\), for all sufficiently small \(\alpha>0\) and \(x\ge1\),
\[
 t_\alpha(x)\ge\frac{2\sqrt r}{2+\alpha}x\ge (\lambda+\varepsilon)x
\]
for a fixed \(\varepsilon>0\). The polynomial prefactor \(x^{3\alpha/4}\) is harmless. Dominated convergence therefore permits passing to the \(\alpha=0\) bilateral-exponential law inside \(Q_\alpha\), giving the asserted finite value.

**Exactly critical regime.** Set \(L_\alpha=\log(1/\alpha)\) and \(b_\alpha=2/(\sqrt r\,\alpha L_\alpha)\). Define
\[
 G_\alpha(x)=\frac{2\sqrt r}{2+\alpha}x^{1+\alpha/2}-\sqrt r\,x.
\]
For every fixed \(u>0\), Taylor expansion with \(\alpha\log(b_\alpha u)\to0\) yields
\[
 G_\alpha(b_\alpha u)=u\left(\frac{\log(b_\alpha u)-1}{L_\alpha}+o(1)\right)\longrightarrow u.
\]
Also \((b_\alpha u)^{3\alpha/4}\to1\), \(B_{\alpha,r}\to\sqrt r\), and \(t_\alpha(b_\alpha u)\to\infty\). Thus
\[
\frac{\mathbb E_\alpha e^{\sqrt r|X|}}{b_\alpha}\longrightarrow
\sqrt r\int_0^\infty e^{-u}\,du=\sqrt r.
\]
To justify the integral limit, the interval \(x\in(0,1)\) contributes \(O(1)=o(b_\alpha)\). Over \(1\le x\le b_\alpha\), the Bessel bound and \(G_\alpha(x)\ge-\sqrt r\alpha/(2+\alpha)\) give a uniform bound after rescaling. For \(x\ge b_\alpha\), the exact identity \(G_\alpha'(x)=\sqrt r(x^{\alpha/2}-1)\) implies \(b_\alpha G_\alpha'(b_\alpha)\to1\). Therefore the rescaled tail is bounded by \(C e^{-u/2}u^c\) for \(u\ge1\) and sufficiently small \(\alpha\) (with a fixed \(c\)), which is integrable. Dominated convergence proves the displayed integral limit. Multiplying by \(r\) proves the critical law.

**Supercritical regime, with the prefactor.** For \(\lambda>\sqrt r\), set
\[
 f_\alpha(x)=\lambda x-\frac{2\sqrt r}{2+\alpha}x^{1+\alpha/2}.
\]
The derivative vanishes precisely at \(x_*=z^{2/\alpha}\), the unique global maximizer of \(f_\alpha\). Direct differentiation gives
\[
 f_\alpha(x_*)=\frac{\alpha\lambda}{2+\alpha}x_*,\qquad
 -f_\alpha''(x_*)=\frac{\alpha\lambda}{2x_*}.
\]
Since \(\alpha x_*\to\infty\), the Gaussian saddle width \(\sqrt{2x_*/(\alpha\lambda)}\) is negligible relative to \(x_*\). More precisely, for fixed \(u>0\),
\[
\frac{f_\alpha(x_*u)-f_\alpha(x_*)}{\alpha\lambda x_*/2}
\longrightarrow -(u\log u-u+1),
\]
whose unique zero is at \(u=1\) and which is strictly negative elsewhere. This furnishes uniform exponential suppression away from the saddle. On the shrinking saddle neighborhood, the Bessel approximation is uniform, the amplitude \(x^{3\alpha/4}\) is asymptotically constant relative to its saddle value, and the cubic Taylor remainder is smaller than the quadratic term by \(O((\alpha x_*)^{-1/2})\). Laplace's method, including both spatial signs, gives
\[
\mathbb E_\alpha e^{\lambda|X|}\sim
B_{\alpha,r}x_*^{3\alpha/4}\sqrt{\frac{4\pi x_*}{\alpha\lambda}}e^{f_\alpha(x_*)},
\]
which is the required full equivalent. Taking logarithms yields the further formula because the saddle height grows faster than \(\log x_*\), \(|\log\alpha|\), and all logarithms of the prefactors.

## Verification

The standalone numerical implementation in `verify.py` evaluates the published stationary density directly using exponentially scaled Bessel functions and quadrature, and compares it with the formulas above. It tests stationary normalization, the Brownian limiting formula, the critical slowly converging ratio, supercritical full-prefactor saddle ratios, and derivative identities. These finite checks are supplementary: the analytic proof supplies the infinite-parameter conclusions.

To reproduce, use Python 3 with `numpy` and `scipy`, and run `python verify.py` from the directory containing the files.

## Relationship to prior work

Frimpong, Bresque and Roldán (2026), sections 4.1 and 7.1.3–7.1.4, derive the exact Bessel stationary density, its fixed-\(\alpha\) spatial tail, and the fact that exponential-cost rates are finite for each \(\alpha>0\) but cease to be finite at \(\alpha=0\) when \(\lambda\ge\sqrt r\). These foundational statements are taken as known. The present theorem is instead a simultaneous \(\alpha\downarrow0\), large-distance analysis, determining the exact critical logarithmic divergence and the supercritical **full asymptotic equivalent** with its exponentially remote saddle. The paper's fixed-parameter tail bound alone does not justify the required uniform singular limit. Sunil, Blythe, Evans and Majumdar (2023) establish the Brownian exponential-reset-cost threshold for first-passage total costs and discuss stationary cost rates; they do not give this weak-sluggishness crossover.

## Limitations

The stochastic model and the Bessel stationary density come from prior work. The result describes the continuum cost rate \(r\mathbb E[c(X)]\), not the distribution of total cost up to an absorbing target. The limits keep \(r\) and \(\lambda\) fixed; a critical window with \(\lambda/\sqrt r-1\) depending on \(\alpha\), discrete-lattice regularization, and finite-time effects are not treated. The original Bessel tail and standard Laplace asymptotics are known mathematical tools. Unindexed general singular-Laplace results could cover a broader abstract class, though no directly implying model-specific theorem was identified in the inspected sources. No independent validation is claimed.

## References

1. T. D. Frimpong, L. Bresque and E. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962v1 (first posted 2026-10-15), https://arxiv.org/abs/2610.21962. In particular, equations (21), (79), (86) and section 7.1.4.
2. J. C. Sunil, R. A. Blythe, M. R. Evans and S. N. Majumdar, *The cost of stochastic resetting*, J. Phys. A 56 (2023), 395001, arXiv:2304.09348, https://arxiv.org/abs/2304.09348. In particular, section 6 and equations (60)–(61).
3. NIST Digital Library of Mathematical Functions, §10.40, asymptotics of modified Bessel functions, https://dlmf.nist.gov/10.40.
