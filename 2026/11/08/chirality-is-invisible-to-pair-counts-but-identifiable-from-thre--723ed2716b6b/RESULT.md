# Chirality is invisible to pair counts but identifiable from three-time count cumulants

## Finding

For a homogeneous gas of independent planar chiral active Brownian particles, **every** two-time covariance of particle counts in arbitrary bounded observation windows is unchanged when the angular drift \(\omega\) is replaced by \(-\omega\). Nonetheless, time-ordered three-window count cumulants recover a signed displacement-triangle statistic

\[
\mathcal H(t,s)=v^2\operatorname{Im}\!\left[\frac{(1-e^{-(D_r-i\omega)t})(1-e^{-(D_r-i\omega)s})}{(D_r-i\omega)^2}\right],\qquad t,s>0,
\]

with the continuous value zero at \(D_r=\omega=0\). In particular,

\[
\mathcal H(h,h)=v^2\omega h^3-\frac76v^2D_r\omega h^4+O(h^5),\qquad h\downarrow0.
\]

Thus, if \(v>0\), any nonzero handedness is detectable from a three-time count statistic, while it is fundamentally indistinguishable by all two-time count covariances. More strongly, the collection of all spatially resolved two-time count covariances and three-time cumulants uniquely determines \(D_t,v,D_r,\omega\) (including the sign of \(\omega\)), without particle tracking.

## Assumptions and scope

Take \(\rho>0\), \(v>0\), \(D_t>0\), \(D_r\geq0\), and \(\omega\in\mathbb R\). Initial positions form a homogeneous Poisson point process of intensity \(\rho\) on \(\mathbb R^2\). Each particle independently receives an initial heading uniform on \([0,2\pi)\), independent planar Brownian motion \(B\), and independent real Brownian motion \(W\). Its position and heading solve

\[
 dX_t=v(\cos\theta_t,\sin\theta_t)\,dt+\sqrt{2D_t}\,dB_t,
 \qquad d\theta_t=\omega\,dt+\sqrt{2D_r}\,dW_t.
\]

For every bounded Borel window \(A\subset\mathbb R^2\), let \(N_t(A)\) be the count at time \(t\). The observations are ideal ensemble covariances and joint cumulants over arbitrarily placed and sized spatial windows; no labels, trajectories, or headings are observed. Set \(U=X_t-X_0\), \(V=X_{t+s}-X_t\) for one particle. Write \(u\wedge v=u_1v_2-u_2v_1\), and \(M(t)=\mathbb E|X_t-X_0|^2\). Derivatives at zero are right derivatives. The identifiability assertion concerns the exact continuum observables, not statistical consistency at finite sample size or a finite field of view.

## Proof

**1. Poisson cumulant identities.** Regard the independent trajectories as marks of the initial Poisson point process. Its exponential formula gives, for bounded windows \(A,B,C\),

\[
\log\mathbb E e^{aN_0(A)+bN_t(B)+cN_{t+s}(C)}
=\rho\int_{\mathbb R^2}\left(\mathbb E e^{a\mathbf1_A(x)+b\mathbf1_B(x+U)+c\mathbf1_C(x+U+V)}-1\right)dx.
\]

Differentiate once in each indicated variable at zero. By finite-window integrability and finite displacement moments, this yields

\[
\operatorname{Cov}(N_0(A),N_t(B))
=\rho\int_A dx\,\mathbb P(x+U\in B),
\]

and

\[
\operatorname{cum}(N_0(A),N_t(B),N_{t+s}(C))
=\rho\int_A dx\,\mathbb P(x+U\in B,\ x+U+V\in C).
\]

In measure form, the three-time cumulant has density/disintegration

\[
 C_3(dx,dy,dz)=\rho\,dx\,p_{t,s}(d(y-x),d(z-y)),
\]

where \(p_{t,s}\) is the joint probability law of \((U,V)\). The two-time counterpart uses only the single-displacement law \(p_t\). These formulas do not require the projected position process itself to be Markovian.

**2. Exact two-time blindness.** Simultaneously rotating all headings, position noise, and displacements leaves the law unchanged because the initial heading is uniform. Hence \(p_t\) is rotation invariant and thus radial. Reflection \(R(x_1,x_2)=(x_1,-x_2)\) converts the dynamics at drift \(\omega\) to those at drift \(-\omega\) without changing the initial ensemble. Consequently \(p_t^{-\omega}=R_{\#}p_t^{\omega}=p_t^{\omega}\). The first Poisson identity proves that **every** two-time count covariance, including between distinct noncongruent windows, is identical at opposite angular drifts. The same holds for all single-time count statistics, which are Poisson with mean \(\rho|A|\).

**3. A signed observable assembled from three-time counts.** For any bounded measurable \(A\) of positive area, define the spatially weighted cumulant moment

\[
 \mathcal H(t,s)=\frac{1}{\rho|A|}
 \int_{x\in A}\int_{y\in\mathbb R^2}\int_{z\in\mathbb R^2}
 (y-x)\wedge(z-y)\, C_3(dx,dy,dz).
\]

This expression is independent of \(A\) and equals \(\mathbb E[U\wedge V]\) by the preceding disintegration. It is determined by the family of count cumulants on bounded windows: partition the spatial integrals into pixels and then enlarge their covered region. Dominated convergence applies because \(\mathbb E|U||V|<\infty\). It need not be computed by labeling particles.

Expanding both active displacements into integrals of heading vectors gives

\[
\mathbb E[U\wedge V]
=v^2\int_0^t da\int_t^{t+s} db\,
\mathbb E\sin(\theta_b-\theta_a).
\]

The independent translational Brownian increments have zero cross expectation and are independent of heading. Since \(b\ge a\),

\[
\mathbb E e^{i(\theta_b-\theta_a)}
=e^{-D_r(b-a)+i\omega(b-a)}.
\]

The double integral factors into

\[
\mathcal H(t,s)
=v^2\operatorname{Im}\left[\frac{(1-e^{-\lambda t})(1-e^{-\lambda s})}{\lambda^2}\right],
\qquad \lambda=D_r-i\omega,
\]

with the continuous extension at \(\lambda=0\). For equal short lags, use \((1-e^{-\lambda h})/\lambda=h-\lambda h^2/2+\lambda^2h^3/6+O(h^4)\). Taking the imaginary part gives

\[
\mathcal H(h,h)=v^2\left(\omega h^3-\frac76 D_r\omega h^4+O(h^5)\right).
\]

Therefore, for \(\omega\neq0\), this statistic is nonzero for all sufficiently small positive \(h\) and changes sign under chirality reversal. Because \(C_3\) determines this moment, the two three-time cumulant measures must differ. In particular, some triple of bounded observation windows has different third cumulant under the two drifts.

**4. Exact recovery of all four parameters.** The two-time count covariance measures determine \(p_t\) by localization of the windows, hence \(M(t)\). The heading dot-correlation is \(e^{-D_r u}\cos(\omega u)\), giving

\[
 M(t)=4D_t t+2v^2\int_0^t(t-u)e^{-D_ru}\cos(\omega u)\,du.
\]

Consequently,

\[
\begin{aligned}
 M'(0+)&=4D_t, & M''(0+)&=2v^2,\\
 M'''(0+)&=-2v^2D_r, & M''''(0+)&=2v^2(D_r^2-\omega^2).
\end{aligned}
\]

The parameters are recovered without ambiguity by

\[
 D_t=\frac{M'(0+)}4,\quad
 v=\sqrt{\frac{M''(0+)}2},\quad
 D_r=-\frac{M'''(0+)}{M''(0+)},\quad
 \omega=\lim_{h\downarrow0}\frac{2\mathcal H(h,h)}{M''(0+)h^3}.
\]

The even two-time data separately recover \(\omega^2=D_r^2-M''''(0+)/M''(0+)\), but cannot select its sign. The formula for \(\omega\) remains valid at zero angular drift and at zero angular diffusivity. This proves both the precise information loss at second order and its recovery at third order.

## Verification

The accompanying standalone `verify.py` checks the complex closed form against independent two-dimensional quadrature, checks the mean-square-displacement formula against quadrature, verifies the signed small-lag expansion using high-precision arithmetic, and checks the reflection parity and the derivative-based recovery identities. Run `python verify.py` with Python and mpmath installed. These tests are consistency checks; the continuum theorem is proved above, without relying on sampling or a finite grid.

## Relationship to prior work

Cerdin, Calazans, Douarche and Marbach (2026) derive two-time count correlations through the self intermediate scattering function for noninteracting active particles, primarily ordinary nonchiral models. The present result concerns *what two-time counts cannot identify* for uniformly oriented chiral swimmers and the exact additional information in their **three-time count cumulants**. The single-particle model and the two-time count construction are prior work, not new inventions.

Pattanayak, Shee, Chaudhuri and Chaudhuri (2024) already derive the exact mean-square displacement and chirality-sensitive **position–orientation** correlations. Their short-time displacement expansion implies the derivative identities for \(M\) used here. The new observation is the signed, tracking-free **three-count cumulant** construction, not a new model or a new formula for the ordinary mean-square displacement.

Kurzthaler and Franosch (2017) give the exact one-lag intermediate scattering function of Brownian circle swimmers. It supplies a more general two-time characterization but does not by itself distinguish opposite angular drifts in the isotropically initialized positional ensemble. Velenich, Chamon, Cugliandolo and Kreimer (2008) establish multi-time density-correlation combinatorics for an independent nonchiral Brownian gas. Their higher-correlation framework is relevant precedent for the Poisson cumulant identity, which is not claimed as a new general theorem. Neither source supplies the stated signed three-time count identification for a persistent chiral active gas in the material examined.

## Limitations

The theorem assumes independent identical particles, homogeneous Poisson initialization, uniform initial headings, isotropic translational noise, constant positive speed, and complete spatially resolved count-cumulant information. Arbitrary interactions, density-dependent responses, wall effects, nonuniform headings, instrumental blur, finite-pixel bias, sampling uncertainty, and unknown particle heterogeneity are not covered. The weighted spatial moment requires access to expanding observation regions for exact recovery, so the proof does not establish an unbiased finite-field estimator or finite-sample detection power. The third-order statistic is an ensemble connected correlation rather than an individual-particle triangle reconstructed by tracking. General Poisson cumulant identities and chiral single-particle moments are known; publication-priority risk remains for the specific combination with three-time count observability.

## References

1. T. Cerdin, T. Calazans, C. Douarche, S. Marbach, *The Countoscope for self-propelled particles*, arXiv:2604.02907, first posted 2026-04-03, https://arxiv.org/abs/2604.02907.
2. A. Pattanayak, A. Shee, D. Chaudhuri, A. Chaudhuri, *Impact of chirality on active Brownian particle: Exact moments in two and three dimensions*, arXiv:2404.09650, first posted 2024-04-15, https://arxiv.org/abs/2404.09650.
3. C. Kurzthaler, T. Franosch, *Intermediate scattering function of an anisotropic Brownian circle swimmer*, Soft Matter **13** (2017), 6396–6406, https://doi.org/10.1039/C7SM00873B.
4. A. Velenich, C. Chamon, L. F. Cugliandolo, D. Kreimer, *On the Brownian gas: a field theory with a Poissonian ground state*, J. Phys. A **41** (2008), 235002, arXiv:0802.3212, https://arxiv.org/abs/0802.3212.
