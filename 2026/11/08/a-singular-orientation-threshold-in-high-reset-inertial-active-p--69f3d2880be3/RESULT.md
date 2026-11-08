# A singular orientation threshold in high-reset inertial active-particle tails

## Finding

The far-from-typical stationary spatial fluctuations of a *completely reset inertial active Brownian particle* have a universal singular-reset crossover. At fixed propulsion speed, a growing reset rate selects an atypically old excursion and its Gaussian thermal displacement. Neither finite propulsion nor the orientational dynamics modifies the leading exponential rate, despite potentially changing the finite-rate angular distribution.

Let \(D,\tau>0\), \(v_0\ge0\), and write \(R=r\tau\). For every fixed \(z>0\) and unit direction \(e\) in the plane, define the stationary position density \(p_r\). Then
\[
\lim_{R\to\infty}-\frac1R\log\!\left(D\tau\,p_r\bigl(\sqrt{D\tau R}\,z e\bigr)\right)=J(z),
\quad
J(z)=\min_{u>0}\left\{u+\frac{z^2}{4F(u)}\right\},
\]
where
\[
F(u)=\int_0^u(1-e^{-s})^2\,ds
=u-\frac32+2e^{-u}-\frac12e^{-2u}.
\]
The minimum occurs at the **unique** positive \(u(z)\) determined by
\[
z=\frac{2F(u(z))}{1-e^{-u(z)}}.
\]
Furthermore, the reset age, conditioned on the specified location (via the regular conditional density), concentrates in probability at \(u(z)\tau\).

**Singular active correction and orientational threshold.** Define \(g(u)=u-1+e^{-u}\) and
\[
c(z)=v_0\sqrt{\frac{\tau}{D}}\,
\frac{g(u(z))}{1-e^{-u(z)}}.
\]
For strictly positive *fixed* rotational diffusivity \(D_{\mathrm r}>0\), every fixed reset heading \(U_0\) and observation direction \(e\) satisfy
\[
\log\!\left(D\tau\,p_r(\sqrt{D\tau R}\,ze)\right)
=-RJ(z)+\sqrt R\,c(z)+o(\sqrt R).
\]
For exactly zero rotational diffusivity, the deterministic orientation \(U_t=U_0\) instead gives
\[
\log\!\left(D\tau\,p_r(\sqrt{D\tau R}\,ze)\right)
=-RJ(z)+\sqrt R\,c(z)(e\cdot U_0)+o(\sqrt R).
\]
For \(v_0>0\), this is a sharp singular difference: arbitrarily slow but positive rotation isotropizes the first active logarithmic correction through rare, directionally selected orientation histories, whereas a perfectly frozen heading retains the reset-direction anisotropy. No claim of uniformity as \(D_{\mathrm r}\downarrow0\) is made.

There is a single smooth, strictly concave crossover rate. It satisfies
\[
J'(z)=\frac1{1-e^{-u(z)}}>1,\qquad J''(z)<0,
\]
and the exact universal corridor
\[
0<J(z)-z<\frac32,\qquad
\lim_{z\downarrow0}[J(z)-z]=0,\quad
\lim_{z\to\infty}[J(z)-z]=\frac32.
\]
In the two endpoint regimes,
\[
J(z)\sim\frac43\sqrt{\frac{3z}{2}}\quad(z\downarrow0),
\qquad
J(z)=z+\frac32+o(1)\quad(z\to\infty).
\]
The theorem is a *joint rare-event/high-reset asymptotic*. The first active logarithmic correction distinguishes rotating and frozen reset headings. It must not be substituted for a fixed-reset-rate far-tail formula, or for an asymptotic describing typical high-reset displacements.

## Assumptions and scope

The two-dimensional particle starts each excursion at \(X=V=0\). Within an excursion,
\[
dX_t=V_t\,dt,\quad
dV_t=-\frac{V_t-v_0U_t}{\tau}\,dt
+\frac{\sqrt{2D}}{\tau}\,dW_t .
\]
Here \(W\) is planar standard Brownian motion, independent of the unit-length orientation process \(U\), and the latter is restarted from the same initial orientation at every reset. The main motivating instance is \(U=(\cos\theta,\sin\theta)\) with \(d\theta_t=\sqrt{2D_{\mathrm r}}\,dB_t\) and \(D_{\mathrm r}\ge0\) fixed. Reset times form an independent rate-\(r\) Poisson process, and all three state components are reset. Parameters \(D,\tau,v_0,D_{\mathrm r}\) stay fixed while \(R=r\tau\to\infty\). Thermal diffusion is strictly positive.

The density limit holds pointwise for each fixed \(z>0\) and unit \(e\); the displayed limit is uniform in \(e\) because the orientation contribution is uniformly bounded. No full large-deviation principle for arbitrary varying spatial arguments, or corresponding result for partial resetting, is asserted.

## Proof

**1. Exact conditional excursion kernel.** Solving the linear velocity equation from zero gives
\[
X_t=v_0\int_0^t\bigl(1-e^{-(t-s)/\tau}\bigr)U_s\,ds
+\sqrt{2D}\int_0^t\bigl(1-e^{-(t-s)/\tau}\bigr)\,dW_s.
\]
The first summand is a conditional mean \(m_t\), bounded uniformly over orientation paths:
\[
|m_{\tau u}|\le v_0\tau\int_0^u(1-e^{-s})\,ds
\le v_0\tau u.
\]
The second summand is a centered isotropic Gaussian with coordinate variance \(2D\tau F(u)\). In particular \(F(u)>0\) for \(u>0\), \(F(u)=u^3/3+O(u^4)\) as \(u\downarrow0\), and \(F(u)=u-3/2+O(e^{-u})\) at infinity.

**2. Exact stationary resetting mixture.** At an independent stationary Poisson observation time, the age \(T\) since the most recent reset has density \(r e^{-rt}\). Conditioning on orientation paths, the exact stationary density is therefore
\[
D\tau\,p_r(\sqrt{D\tau R}\,z e)
=\frac{R}{4\pi}\int_0^\infty
\frac{e^{-Ru}}{F(u)}
\mathbb E\!\left[
\exp\!\left(-\frac{|\sqrt R\,ze-b_u|^2}{4F(u)}\right)
\right]du,
\]
with \(b_u=m_{\tau u}/\sqrt{D\tau}\), and the deterministic bound
\[
|b_u|\le \frac{v_0\tau}{\sqrt{D\tau}}\,u.
\]
This identity contains no Gaussian approximation to the orientational dynamics.

**3. The Laplace principle, including both endpoints.** On any fixed compact \(K\subset(0,\infty)\), the bound on \(b_u\) yields uniformly over \(u\in K\) and the orientation path
\[
\frac{|\sqrt R\,ze-b_u|^2}{4F(u)}
=R\frac{z^2}{4F(u)}+O_K(\sqrt R).
\]
Thus the compact contribution has logarithmic rate given by the minimum of \(\phi_z(u)=u+z^2/(4F(u))\). To justify the truncation: for \(0<u\le\varepsilon\), the thermal displacement \(\sqrt R\,ze\) eventually dominates all admissible \(b_u\), and the integrand is bounded by a constant multiple of \(R\,u^{-3}\exp[-Rz^2/(C u^3)]\), for an absolute positive constant \(C\) depending on the fixed model and \(z\). Choosing \(\varepsilon\) small makes its rate arbitrarily high. For \(u\ge M\), the Gaussian factor is at most one; \(F(u)\) is eventually of order \(u\), and hence
\[
\frac{R}{4\pi}\int_M^\infty \frac{e^{-Ru}}{F(u)}\,du
\le C_M e^{-RM}
\]
for fixed sufficiently large \(M\) and \(R\ge1\). The tails are therefore exponentially negligible relative to the unique finite minimum, and the claimed logarithmic density limit follows. The same estimates and uniqueness of the minimizing age imply conditional concentration of \(T/\tau\) at that minimizer for the regular conditional age distribution given the observed position.

**4. Unique minimizer.** Differentiation gives \(F'(u)=(1-e^{-u})^2\). Since \(\phi_z\to\infty\) at both endpoints, an interior minimum exists. With \(q=e^{-u}\), \(y=1-q\), its critical equation is
\[
z=\frac{2F(u)}y.
\]
Its derivative has the sign of \(H(u)=y^3-qF(u)\). Now
\[
H(0)=0,\qquad H'(u)=q\bigl(2y^2+F(u)\bigr)>0
\quad(u>0).
\]
Hence \(z(u)=2F(u)/y\) increases strictly from zero to infinity. Exactly one critical point exists, and it is the global minimizer.

**5. Strict concavity and gap law.** At the optimum, \(z=2F/y\), so the envelope theorem gives
\[
J'(z)=\frac{z}{2F(u(z))}=\frac1{y(u(z))}>1.
\]
Because \(u(z)\) increases strictly and \(y(u)\) increases strictly, the derivative \(J'\) decreases strictly; consequently \(J''<0\) everywhere on \((0,\infty)\). The small-\(u\) expansions \(F(u)\sim u^3/3\), \(y\sim u\) yield \(z\sim2u^2/3\), \(J\sim4u/3\), and the specified square-root law. At the other endpoint \(F=u-3/2+o(1)\) and \(y\to1\), whence \(z=2u-3+o(1)\) and \(J=2u-3/2+o(1)=z+3/2+o(1)\). Since \(J-z\) has positive derivative everywhere, starts at zero and increases to \(3/2\), the sharp strict corridor follows.

**6. Activity-independence.** The conditional propulsion mean is \(O(1)\) uniformly at the saddle age \(t=\tau u(z)\) for fixed \(z\). Its effect on the Gaussian exponent is at most \(O(\sqrt R)\), while the reset and thermal cost is of order \(R\). This establishes the same \(J\), and the same selected age, for every fixed finite \(v_0\), fixed \(D_{\mathrm r}\), and any independent unit orientation process.


**7. The first active logarithmic correction and the singular heading boundary.** Expanding the exact conditional Gaussian exponent, for any orientation path and fixed age \(u\),
\[
-\frac{|\sqrt R\,ze-b_u|^2}{4F(u)}
=-R\frac{z^2}{4F(u)}
+\sqrt R\frac{z(e\cdot b_u)}{2F(u)}
-\frac{|b_u|^2}{4F(u)}.
\]
Let \(b=v_0\sqrt{\tau/D}\). The weighted-integral form of the drift implies, uniformly over orientation paths,
\[
e\cdot b_u\le b\,g(u),\qquad
g(u)=\int_0^u(1-e^{-(u-s)})\,ds=u-1+e^{-u}.
\]
This gives a Laplace upper bound for the coefficient of \(\sqrt R\) equal to \(bz\,g(u(z))/(2F(u(z)))=c(z)\). The uniqueness and strict interior nature of the saddle guarantee that deviations in age cannot improve this coefficient: for every fixed neighborhood of \(u(z)\), ages outside it have a strictly larger order-\(R\) cost, while inside an arbitrarily small neighborhood the coefficient approaches \(c(z)\).

For \(D_{\mathrm r}>0\), consider a fixed small \(\delta,\varepsilon>0\). Planar Brownian orientation has positive probability to rotate from its prescribed initial direction to within \(\varepsilon\) of the observation direction before dimensionless age \(\delta\), then remain within \(\varepsilon\) until a neighborhood of age \(u(z)\). This is the positive-probability tube property of ordinary one-dimensional Brownian motion (on its angular lift); its probability depends on \(\delta,\varepsilon,D_{\mathrm r}\) but **not** on \(R\). On this event, \(e\cdot b_u\ge b[g(u)-O(\delta+\varepsilon^2 g(u))]\) uniformly for \(u\) close to \(u(z)\); the early interval contributes at most \(O(\delta)\) since its kernel is bounded by one. Restricting the exact stationary integral to this event and an age interval of width \(R^{-1/2}\) around the unique saddle provides the corresponding lower bound after dividing the logarithm by \(\sqrt R\): logarithmic event probabilities, polynomial prefactors, and the quadratic Gaussian mean term are negligible. First take \(R\to\infty\), then \(\delta,\varepsilon\downarrow0\), giving the coefficient \(c(z)\). This argument requires only \(D_{\mathrm r}>0\) fixed, however small.

For \(D_{\mathrm r}=0\), the orientation remains identically \(U_0\), so \(b_u=b\,g(u)U_0\) deterministically and ordinary one-dimensional Laplace expansion yields the exact coefficient \(c(z)(e\cdot U_0)\). The upper/lower bounds cover all observation directions, including those opposite to \(U_0\). They also show why the angular-diffusivity limit does not commute with the singular-reset limit.

## Verification

The accompanying standalone standard-library script `verify.py` independently integrates the variance kernel, checks its derivative and normalizations, finds the saddle by bisection, checks concavity and strict gap numerically at many arguments, verifies endpoint asymptotics, and directly integrates the exact stationary Gaussian-reset density for rates \(R=50,200,800\) at multiple positions with zero and nonzero deterministic propulsion. It also checks convergence of the normalized active/passive log-density ratio toward the deterministic-heading \(O(\sqrt R)\) coefficient. The tests are finite consistency checks; the analytical argument above establishes the infinitely quantified claims. Run `python3 verify.py`.

## Relationship to prior work

Patel and Shee, *Controlling inertial active Brownian motion via stochastic resetting* (arXiv:2602.21134, publicly available from February 24, 2026), introduce the exact full-reset inertial active process and calculate its second and fourth stationary moments, transient second moments and kurtosis behavior. In particular, their high-rate mean-square displacement scales as \(r^{-3}\). Moment formulas do not identify the stationary rare-displacement density at the different scale \(\sqrt{D\tau R}\).

Franke and Sokolov, *Resetting of underdamped Brownian motion* (Phys. Rev. E **113**, 064125, June 2026), already provide the **passive** complete-reset stationary mixture and a general saddle-point equation (their Eq. (13)). After converting variables, that saddle equation is algebraically identical to \(z=2F(u)/(1-e^{-u})\); its appearance here is not claimed novel. Their fixed-rate large-distance expansion (Eq. (14)) addresses a different ordering of limits, namely distance large relative to the reset-dependent crossover scale. The present result isolates the simultaneous \(R\to\infty\), displacement proportional to \(\sqrt R\) regime, determines the global limiting logarithmic profile and its strict concavity/sharp additive-gap law, proves the singular rotational-diffusion dependence of the first active logarithmic correction, and establishes conditional reset-age concentration. Related random-acceleration resetting and its stretched-exponential tails were analyzed by Singh (2020), but do not establish this damped high-rate crossover.

## Limitations

The two logarithmic terms do not determine polynomial prefactors or finite-rate orientation anisotropy; the latter can remain prominent even when the rate is radial. The limit is pointwise for \(z>0\), and its \(z\downarrow0\) expansion cannot be interchanged automatically with the limit in \(R\). Finite propulsion strength, positive thermal diffusivity and independent Brownian rotation for the two-term angular statement are essential: propulsion growing with \(R\), vanishing thermal noise, Maxwell-distributed reset velocity, position-only resetting, and arbitrary non-Poisson reset clocks are not covered. Conditional age concentration refers to the regular conditional density, not conditioning on a positive-probability point event. The general passive saddle equation is pre-existing, so the originality assessment is restricted to the joint limit, strict rate-profile structure, singular positive-versus-zero rotation correction, and conditional-age selection. Further unindexed literature may contain related double-scaling calculations.

## References

1. M. Patel and A. Shee, *Controlling inertial active Brownian motion via stochastic resetting*, arXiv:2602.21134v1 (first public February 24, 2026). https://arxiv.org/abs/2602.21134
2. H. Franke and I. M. Sokolov, *Resetting of underdamped Brownian motion*, Physical Review E **113**, 064125 (published June 11, 2026), DOI:10.1103/qyl8-6q9h. https://doi.org/10.1103/qyl8-6q9h
3. P. Singh, *Random acceleration process under stochastic resetting*, arXiv:2007.05576v1 (2020). https://arxiv.org/abs/2007.05576
