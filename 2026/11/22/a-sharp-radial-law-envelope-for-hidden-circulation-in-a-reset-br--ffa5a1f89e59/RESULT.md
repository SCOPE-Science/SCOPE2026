# A sharp radial-law envelope for hidden circulation in a reset Brownian gyrator

## Finding

For a stable two-temperature planar Brownian gyrator with full Poisson resetting, fixing the **entire radial law of the reset marks** and their isotropic second moment fixes **every stationary two-time position covariance**, but need not fix even the sign of the stationary mean specific angular velocity. The exact asymptotic range of that angular velocity, over all centered isotropic reset laws with a prescribed radial law, is the closed interval

\[
[-u A_\nu,u A_\nu],\qquad A_\nu=\min_{a\geq0}\mathbb E_\nu|1-aR^2|.
\]

In particular, let \(u=1/2\), \(T_x=1\), \(T_y=3\), and let the reset radius be \(1\) with probability \(9/10\) and \(3\) with probability \(1/10\). Two antipodally symmetric reset laws supported on the coordinate axes have identical reset radial laws, identical means and covariance \((9/10)I_2\), hence identical full stationary position covariance functions for **every** resetting rate. Yet at resetting rate \(r=5000\) their stationary mean specific angular velocities have rigorously opposite signs, while both have strictly positive mean specific angular momenta. The asymptotic angular-velocity interval is exactly \([-2/5,2/5]\) for this coupling, with both endpoints attained. One of these reset laws undergoes at least one angular-velocity reversal as the rate grows from zero.

## Assumptions and scope

Let \(0<u<1\), \(0<T_x<T_y\), \(A=\begin{psmallmatrix}1&u\\u&1\end{psmallmatrix}\), and \(D=\operatorname{diag}(T_x,T_y)\). Between Poisson resetting events, the position \(Z_t=(X_t,Y_t)^\top\) evolves by

\[
\mathrm dZ_t=-AZ_t\,\mathrm dt+\sqrt{2D}\,\mathrm dB_t.
\]

At rate \(r>0\), the full position is instantaneously replaced by a new independent mark \(M\sim\mu\), independently of the past and the Brownian driving. Its radial variable \(R=|M|\) has a specified probability distribution \(\nu\) on \((0,\infty)\), with \(0<\mathbb E_\nu R^2<\infty\). We allow all reset laws \(\mu\) satisfying

\[
\mathbb E M=0,\qquad \mathbb E(MM^\top)=mI_2,\qquad m=\tfrac12\mathbb E_\nu R^2.
\]

For \(r>0\), write \(C_r=\mathbb E(Z_tZ_t^\top)\) at stationarity and \(C_r(\tau)=\mathbb E(Z_tZ_{t+\tau}^\top)\) for \(\tau\ge0\). Define the *continuous-flight* (reset jumps excluded), forward-discretized mean specific angular momentum and angular velocity by

\[
L_r=u\mathbb E(Y^2-X^2),\qquad \Omega_r=u\mathbb E g(Z),\qquad
 g(x,y)=\begin{cases}(y^2-x^2)/(x^2+y^2),&(x,y)\ne0,\\0,&(x,y)=0.\end{cases}
\]

These are ensemble averages of the drift part of \(X\dot Y-Y\dot X\) and its radius-normalized analogue; they do not incorporate the angular jumps caused by resetting. Under positive diffusion the stationary law has no atom at the origin. The cited source fixes this same forward-noise convention. The limit \(r\downarrow0\) is the standard stationary Ornstein–Uhlenbeck gyrator.

## Proof

**1. Complete two-time covariance blindness.** The process has a unique stationary law for every \(r>0\), obtained by starting from a fresh reset mark a time \(S\sim\mathrm{Exp}(r)\) ago:

\[
Z_r\overset d=e^{-AS}M+\int_0^S e^{-Av}\sqrt{2D}\,\mathrm dB_v,
\]

with independent components on the right. It is centered. Applying the stationary generator to \(ZZ^\top\) yields the matrix Lyapunov relation

\[
AC_r+C_rA+rC_r=2D+rmI_2.
\]

Because \(A\) is positive definite and \(r>0\), this equation has a unique symmetric solution. It depends only on \(m\) and the physical rates, not on any higher moments or orientation of \(\mu\). Subtracting the two diagonal equations gives

\[
(C_r)_{yy}-(C_r)_{xx}=\frac{2(T_y-T_x)}{r+2},
\qquad L_r=\frac{2u(T_y-T_x)}{r+2}>0.
\]

Conditional on a present position \(z\), the future centered mean at lag \(\tau\) is \(e^{-(A+rI_2)\tau}z\): either no reset occurred, or the first reset erases all dependence on \(z\) and later reset marks have mean zero. Therefore

\[
\boxed{C_r(\tau)=C_r e^{-(A+rI_2)\tau},\qquad \tau\ge0.}
\]

Negative lags are transposes, and the full matrix-valued Fourier spectral density is determined by these functions. Hence **all** stationary means, position variances, cross-covariances, all time-lag covariance matrices and power spectra coincide whenever the reset laws satisfy the displayed restrictions.

**2. The sharp radial-law angular envelope.** The function \(g\) is bounded by one and is continuous off zero. Since \(S\to0\) in probability as \(r\to\infty\) and the diffusion integral vanishes in probability, \(Z_r\to M\) in probability. As \(\mathbb P(R>0)=1\), bounded convergence in probability implies

\[
\lim_{r\to\infty}\Omega_r=u\,\mathbb E_\mu g(M).
\]

Write \(M=R(\cos\Theta,\sin\Theta)\), \(W=R^2>0\), and \(f(W)=\mathbb E[\cos(2\Theta)\mid W]\). Then \(|f|\le1\), while isotropic covariance forces

\[
\mathbb E[W f(W)]=0,\qquad \mathbb E g(M)=-\mathbb E f(W).
\]

For every \(a\ge0\), this gives the dual bound

\[
\mathbb E f=\mathbb E[(1-aW)f]\le\mathbb E|1-aW|.
\]

The convex, continuous function \(a\mapsto\mathbb E|1-aW|\) attains a minimum at a strictly positive \(a_*\) because its right derivative at zero is \(-\mathbb EW<0\) and it diverges as \(a\to\infty\). Set \(f_*(w)=\operatorname{sgn}(1-a_*w)\) except at a possible atom \(w=1/a_*\), where choose an intermediate value in \([-1,1]\) so that \(\mathbb E[Wf_*(W)]=0\). Such a choice exists from the one-sided subgradient inequalities at the minimizer. Consequently

\[
\mathbb E f_*=\mathbb E|1-a_*W|=A_\nu.
\]

The other endpoint follows from \(-f_*\). For every \(f\) with \(|f|\le1\), realize the required conditional angular cosine by placing a reset mark, with equal antipodal signs, on the \(x\)-axis with conditional probability \((1+f(W))/2\), and on the \(y\)-axis with probability \((1-f(W))/2\). This realizes zero mean and isotropic covariance. Scaling \(f_*\) by any factor between \(-1\) and \(1\) fills the complete interval. Thus the exact attainable limiting angular-velocity interval is \([-uA_\nu,uA_\nu]\), *including* both endpoints. A single-radius reset law gives \(A_\nu=0\); radius heterogeneity gives \(A_\nu>0\).

**3. Explicit identical-radial-law opposite-sign protocols.** Let \(\nu(R=1)=9/10\), \(\nu(R=3)=1/10\). Define \(\mu_-\) by equal antipodal splitting of mass \(9/10\) over \((\pm1,0)\) and mass \(1/10\) over \((0,\pm3)\). Define \(\mu_+\) by swapping the axes at each radius: mass \(9/10\) over \((0,\pm1)\), mass \(1/10\) over \((\pm3,0)\). Both have mean zero, covariance \((9/10)I_2\), and exactly the same reset-radius distribution. Their respective expectations \(\mathbb E g(M)\) are \(-4/5\) and \(+4/5\). Moreover, in the dual formula

\[
A_\nu=\min_{a\ge0}\left(\tfrac9{10}|1-a|+\tfrac1{10}|1-9a|\right)=\tfrac45,
\]

with equality for every \(1/9\le a\le1\). These are sharp endpoints under this fixed radial law.

There is also a certified **finite-rate** separation. For every \(|M|\ge1\), set \(\Delta=Z_r-M\). The gradient bound \(|\nabla g(z)|\le2/|z|\) implies \(|g(Z_r)-g(M)|\le4|\Delta|\) when \(|\Delta|<1/2\); otherwise the difference is at most two and Markov's inequality yields \(\mathbb E|g(Z_r)-g(M)|\le8\mathbb E|\Delta|\). The OU propagator is contractive and \(\|A\|=1+u\), so the renewal representation and Cauchy–Schwarz give

\[
\mathbb E|\Delta|\le\frac{(1+u)\mathbb E|M|}{r}+\sqrt{\frac{4T_y}{r}}
\le\frac{3(1+u)}{r}+\sqrt{\frac{4T_y}{r}}.
\]

For \(u=1/2\), \(T_x=1\), \(T_y=3\), \(r=5000\), the inequality \(12/5000<1/400\) proves

\[
|\mathbb E g(Z_r)-\mathbb E g(M)|
<8\left(\frac9{10000}+\frac1{20}\right)=\frac{509}{1250}<\frac45.
\]

Therefore the two mean angular velocities at this one **same** finite resetting rate satisfy

\[
\boxed{\Omega_{5000}^{(-)}<-\frac{491}{2500}<0<\frac{491}{2500}<\Omega_{5000}^{(+)}.}
\]

Both simultaneously have \(L_{5000}=2/5002>0\), and their stationary two-time covariance matrices coincide for *all* lags, not merely at a sampled set.

**4. A genuine angular-velocity sign reversal in one protocol.** For \(r\downarrow0\), the stationary position tends to a centered Gaussian with covariance \(\Sigma\) solving \(A\Sigma+\Sigma A=2D\). Its diagonal difference equals \(\Sigma_{yy}-\Sigma_{xx}=T_y-T_x>0\). A Gaussian Laplace transform gives

\[
\mathbb E_\Sigma g(Z)=(T_y-T_x)\int_0^\infty\det(I_2+2s\Sigma)^{-3/2}\,\mathrm ds>0.
\]

The law of \(Z_r\) varies continuously in \(r\) in distribution for positive rates, and bounded \(g\) is continuous almost everywhere under its smooth density, so \(\Omega_r\) is continuous. Since the minus protocol has \(\Omega_{5000}^{(-)}<0\) but positive zero-reset limit, it has at least one strict-sign crossing. No claim is made of uniqueness or a precise crossing threshold.

## Verification

The accompanying \(\texttt{proof_check.py}\) checks with exact rational arithmetic and symbolic matrix algebra: the two reset laws' common isotropic covariance; the dual-envelope value \(4/5\); the general stationary covariance balance and its diagonal difference; a rational parameter instance; and the finite-rate angular-sign bound. Run with \(\texttt{python proof_check.py}\) with SymPy installed. These checks support, but do not replace, the general analytic arguments above. The proof's only infinite-domain steps are bounded convergence in probability, convex one-variable duality, and the Gaussian integral, each justified in the displayed hypotheses.

## Relationship to prior work

Majumdar, Schehr, Viot and Oshanin (2026) derive the reset-gyrator renewal law, the exact fixed-point mean angular momentum (their Eq. 44), and the nonlinear mean angular velocity (Eq. 49), and discuss uniform-circle resetting. Those formulas and the general distinction between second moments and angular velocity are **prior**. Their conclusion expressly identifies more general, nonuniform reset distributions as an extension. The present claim is the exact **fixed-radial-law constrained range**, its size-biased radius-median extremizers, the complete second-order temporal indistinguishability under the same physical parameters, and a certified same-radial-law sign reversal at finite rate; those conclusions are not contained in the inspected special-case calculations.

Olsen (2023) establishes general moment closure under resetting to distributions in a one-coordinate harmonic model; that supports the background observation that low moments depend only on reset low moments, but not this two-dimensional angular-velocity extremization. Viot and colleagues (2023) analyze ordinary gyrator angular observable fluctuations without Poisson-reset mark optimization. Rose and collaborators (2018) establish general generator spectral shifts under resetting. Existing covariance-matched reset models and circulation-reversal examples concern distinct observables or protocols; second-moment indistinguishability by itself is not claimed to be unprecedented.

## Limitations

The result concerns **continuous-flight forward-discretized mean angular velocity**, not winding number, reset-jump chord angular area, mean heat, or the full stationary angular-velocity distribution. Coincidence is shown for the reset **radial law**, *not* for the entire stationary radial density. The sharp interval is for the **high-reset limit** at fixed physical parameters; the finite-rate result certifies a pair of signs at \(r=5000\) but does not classify the full finite-rate attainable interval. The exact covariance theorem needs centered isotropic reset marks and fixed physical coefficients. The Gaussian zero-reset positivity uses \(T_y>T_x\) and \(u>0\). Results are mathematical consequences within the idealized overdamped, instantaneous full-reset model, not experimental validation or independent peer review.

## References

1. S. N. Majumdar, G. Schehr, P. Viot and G. Oshanin, *Brownian gyrator model with stochastic resetting*, arXiv:2611.06322v1, first submitted 4 November 2026, https://arxiv.org/abs/2611.06322 (Sections 3.1, 3.7, 3.8, 4.4, 4.5 and conclusion).
2. K. S. Olsen, *Steady-state moments under resetting to a distribution*, Physical Review E 108, 044120 (2023), arXiv:2310.04840, https://arxiv.org/abs/2310.04840.
3. P. Viot et al., *Destructive effect of fluctuations on the performance of a Brownian gyrator*, arXiv:2307.05248 (2023), https://arxiv.org/abs/2307.05248.
4. D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, Physical Review E 98, 022129 (2018), https://doi.org/10.1103/PhysRevE.98.022129.
