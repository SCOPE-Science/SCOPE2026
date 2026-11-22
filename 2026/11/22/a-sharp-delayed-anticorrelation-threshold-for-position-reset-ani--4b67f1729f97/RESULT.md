# A sharp delayed anticorrelation threshold for position-reset anisotropic Brownian motion

## Finding

A passively diffusing planar colloid with rotating anisotropic mobility has **positive simultaneous** fluctuations of orthogonal squared positions, but may have **negative delayed** fluctuations even when its stationary spatial distribution is rotationally invariant. For the position-only Poisson-reset protocol defined below, let
\[
\bar D=\frac{D_\parallel+D_\perp}{2},\qquad
\delta=\frac{D_\parallel-D_\perp}{2},\qquad
\omega=4q,\qquad
b=\frac{|\delta|}{\bar D}.
\]
For every lag \(t\ge0\), the stationary orthogonal-energy covariance is exactly
\[
\boxed{
C_{xy}(t):=\operatorname{Cov}(X_0^2,Y_t^2)
=e^{-rt}\left[V-A\int_0^t e^{(r-\omega)s}\,ds\right],
}\quad
V=\frac{4\bar D^2}{r^2}+\frac{4\delta^2}{r(r+\omega)},\quad
A=\frac{2\delta^2}{r+\omega}.
\]
In particular \(C_{xy}(0)=V>0\). If \(D_\parallel\ne D_\perp\), define the sharp reset-rate boundary
\[
\boxed{
 r_c=\omega\,\frac{b^2+\sqrt{b^4+6b^2+4}}{2+3b^2}.
}
\]
Then for \(0<r\le r_c\), \(C_{xy}(t)>0\) at every finite lag. For \(r>r_c\), there is **exactly one** \(t_*>0\) such that \(C_{xy}(t)>0\) for \(0\le t<t_*\), \(C_{xy}(t_*)=0\), and \(C_{xy}(t)<0\) for \(t>t_*\). At the critical rate it approaches zero from above without crossing. The root is explicit:
\[
\boxed{
 t_*=\begin{cases}
\displaystyle\frac{\log\left(1+(r-\omega)V/A\right)}{r-\omega},&r\ne\omega,\\[5pt]
\displaystyle V/A,&r=\omega.
\end{cases}
}
\]
The threshold obeys the sharp, strictly anisotropy-dependent range
\[
\frac{1+\sqrt{11}}5<\frac{r_c}{\omega}<1,
\]
decreasing strictly with \(b\) and approaching the respective endpoints as \(b\uparrow1\) and \(b\downarrow0\). In the isotropic case \(\delta=0\), the covariance remains strictly positive for every finite lag and every \(r>0\). For fixed \(0<b<1\), the high-reset crossing time further satisfies
\[
\lim_{r\to\infty}rt_*=\log(3+2/b^2).
\]

## Assumptions and scope

Fix \(D_\parallel,D_\perp,q,r>0\). The orientation \(\Theta_t\) is Brownian motion on the circle with generator \(q\partial_{\theta\theta}\). Conditional on \(\Theta_t=\theta\), the two-dimensional position \((X_t,Y_t)\) has zero drift and diffusion tensor
\[
\mathcal D(\theta)=\bar D I_2+\delta
\begin{pmatrix}\cos2\theta&\sin2\theta\\\sin2\theta&-\cos2\theta\end{pmatrix},
\qquad
\mathrm d\mathbf X_t=\sqrt{2}\,\mathcal D(\Theta_t)^{1/2}\mathrm d\mathbf W_t,
\]
where the two-dimensional Brownian motion \(\mathbf W\) and the angle driver are independent. At the events of a further independent rate-\(r\) Poisson clock, \(\mathbf X\) resets to the origin while \(\Theta\) is **not** reset. Expectations refer to the unique stationary joint process, including the uniform stationary angular marginal. The time origin is arbitrary under stationarity, and the coordinates are any fixed perpendicular laboratory directions. All moment and lag statements hold for any positive parameters within this scope.

## Proof

**1. Stationarity and moments.** On a two-sided probability space, construct the stationary angular Brownian motion, the independent Poisson reset times, and the positional Itô integral over the interval since the most recent reset. Rotating the entire construction preserves its law, so the stationary position distribution is rotationally invariant. Angular mixing and eventual position reset make this the unique stationary law. With \(D_{\max}=\max(D_\parallel,D_\perp)\), the conditional spatial covariance is bounded by \(2D_{\max}TI_2\), where the backward reset age \(T\) is exponential of rate \(r\); hence all polynomial moments used below are finite.

Let \(c=\cos2\Theta\), \(s=\sin2\Theta\). The joint generator acts by
\[
\mathcal Lf=\mathcal D(\theta):\nabla_{x,y}^2f+q\partial_{\theta\theta}f
+r\bigl[f(0,0,\theta)-f(x,y,\theta)\bigr].
\]
Using \(\mathbb Ec=\mathbb Es=0\), \(\mathbb Ec^2=\mathbb Es^2=1/2\), and \(\mathbb E\mathcal Lf=0\) gives, successively,
\[
\mathbb EX^2=\mathbb EY^2=\frac{2\bar D}{r},\qquad
\mathbb E[X^2c]=\frac{\delta}{r+\omega},\qquad
\mathbb E[Y^2c]=-\frac{\delta}{r+\omega},\qquad
\mathbb E[XYs]=\frac{\delta}{r+\omega}.
\]
The crucial mixed fourth-moment equation follows *without an approximation* because
\[
\mathcal L(x^2y^2)=2y^2(\bar D+\delta c)+2x^2(\bar D-\delta c)
+8\delta xy s-rx^2y^2.
\]
Consequently,
\[
\mathbb E[X^2Y^2]=\frac{8\bar D^2}{r^2}
+\frac{4\delta^2}{r(r+\omega)},\quad
\operatorname{Cov}(X^2,Y^2)=V.
\]
These stationary one-time identities are also consistent with previously published fourth-moment calculations; their combination with the future conditional dynamics, rather than these identities alone, is the present claim.

**2. Two-time semigroup.** Starting from \((x,y,\theta)\), let \(m_y(t)=\mathbb E_{x,y,\theta}[Y_t^2]\). Since the orientation is retained at resets,
\[
\frac{\mathrm d}{\mathrm dt}m_y(t)+rm_y(t)
=2\bar D-2\delta e^{-\omega t}\cos2\theta,
\qquad m_y(0)=y^2.
\]
Variation of constants yields
\[
m_y(t)=e^{-rt}y^2+\frac{2\bar D}{r}(1-e^{-rt})
-2\delta e^{-rt}\cos2\theta\int_0^t e^{(r-\omega)s}\,ds.
\]
Taking the covariance with stationary \(X_0^2\), and using the first-step covariance \(\operatorname{Cov}(X_0^2,\cos2\Theta_0)=\delta/(r+\omega)\), proves exactly the displayed \(C_{xy}(t)\). Equivalently, its initial value is \(V\) and it solves the forced linear equation
\[
 C_{xy}'(t)+rC_{xy}(t)=-A e^{-\omega t}.
\]

**3. Unique sign threshold.** When \(\delta\ne0\), the bracket \(V-AH(t)\), with \(H(t)=\int_0^t e^{(r-\omega)s}\,ds\), is continuous and strictly decreasing from \(V>0\). If \(r\ge\omega\), its limiting value is negative infinity and it has one zero. If \(r<\omega\), its limiting value is \(V-A/(\omega-r)\); the bracket crosses zero exactly when \(A/(\omega-r)>V\). Substituting the explicit parameters and multiplying by positive denominators makes this equivalent to
\[
 (2+3b^2)(r/\omega)^2-2b^2(r/\omega)-2>0.
\]
This upward quadratic has exactly one positive root \(r_c/\omega\) as given. Equality produces the strictly positive critical tail \(C_{xy}(t)=V e^{-\omega t}\); strict inequality reverses the sign exactly once. Solving \(H(t_*)=V/A\) gives the logarithmic formula, including its continuous resonant extension at \(r=\omega\). When \(\delta=0\), \(A=0\) and \(C_{xy}(t)=4\bar D^2e^{-rt}/r^2>0\).

To establish the stated sharp threshold bounds, let \(u=b^2\in(0,1)\) and \(z=r_c/\omega\). The positive root obeys \((2+3u)z^2-2uz-2=0\), lies strictly between \((1+\sqrt{11})/5\) and \(1\), and satisfies
\[
\frac{\mathrm dz}{\mathrm du}
=-\frac{3z^2-2z}{2(2+3u)z-2u}<0
\]
since \(z>(1+\sqrt{11})/5>2/3\). Finally, letting \(r\to\infty\) at fixed \(b>0\) in \(e^{(r-\omega)t_*}=1+(r-\omega)V/A\) yields \(e^{rt_*}\to3+2/b^2\), proving the limit.

## Verification

Execute `python3 verification/VERIFY.py` using the Python standard library. It checks stationary generator balances using exact rational arithmetic, the threshold polynomial and all parameter regimes, lag zeroes, critical and resonant branches, the normalized lag ODE, and the high-reset crossing limit. The recorded execution passed **1,477 assertions**. An optional independent stochastic path experiment (`verification/MONTE_CARLO.py`, requiring NumPy) samples the stationary exponential reset age and rotational trajectories; at four representative lags it reproduces the predicted positive-to-negative crossing. Numerical tests are finite diagnostic checks, not proofs of quantification over all parameters and lags.

## Relationship to prior work

Chaki, Stølevik Olsen and Löwen's June 25, 2024 preprint supplies precisely the passive rotating-anisotropic-diffusion model and the position-only resetting protocol. Their complete Section IV derives one-time second moments and vanishing ordinary coordinate cross covariance; it does **not** calculate the stationary two-time mixed fourth quantity \(\operatorname{Cov}(X_0^2,Y_t^2)\). A separately published result, *Hidden stationary anisotropy under position-only resetting*, derives the stationary projected fourth moment and its kurtosis, supplying related **equal-time** information but not the lag-dependent sign law. Those quantities are acknowledged as prior work, not claimed as new. Other comparison results concern either orientation-only resetting, joint position-and-orientation resetting, or a separately reset Brownian diffusivity, none of which has the same retained orientation and orthogonal diffusion anticorrelation. Ghosh, Mandal and Chaki's later active-particle study derives position-only reset second moments for a self-propelled model, not the passive lagged energy sign change. The novelty assertion is confined to the exact **two-time orthogonal-energy covariance and its sharp single-crossing classification**; broader unindexed equivalent work remains possible.

## Limitations

The theorem concerns passive translation with strictly positive body-frame diffusivities and rotational diffusion, instantaneous complete **position-only** Poisson resetting, and stationary sampling. It does not treat deterministic orientation, non-Poisson resets, resets of heading, self-propulsion, torque, traps, interactions or measurement noise. \(C_{xy}(t)<0\) is an anticorrelation of the *squared* positions at different times, not of the signed positions. Neither the full joint two-time density nor finite-sample estimators are supplied. Numerical checks cannot prove an infinite-time statement. Publication priority is subject to independent literature confirmation.

## References

- S. Chaki, K. Stølevik Olsen, H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550, first public version 2024-06-25, https://arxiv.org/abs/2406.17550. Section IV, translational resetting.
- *Hidden stationary anisotropy under position-only resetting*, published mathematical result, 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-hidden-stationary-anisotropy-under-position-only-resetting--4289f97988e1. Earlier stationary fourth-moment and kurtosis statement.
- *Two-clock diffusivity resetting has a sharp spatial-memory threshold*, published mathematical result, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-two-clock-diffusivity-resetting-has-a-sharp-spatial-memory-thres--0189122e6072. Different hidden-diffusivity protocol with positive squared cross-covariances.
- *Exact angular-moment hierarchy and stationary-position tomography for reset anisotropic Brownian particles*, published mathematical result, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-angular-moment-hierarchy-and-stationary-position-tomograph--ae34d732db08. Joint position-and-heading resetting.
- *Sharp fourth-cumulant isotropy under orientation-only resetting of an anisotropic Brownian particle*, published mathematical result, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-fourth-cumulant-isotropy-under-orientation-only-resetting--403d011b461a. Orientation-resetting-only protocol.
- A. Ghosh, S. Mandal, S. Chaki, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149, first public version 2025-01-09, https://arxiv.org/abs/2501.05149. Active rather than passive motion; analyzed the model and its second moments.
