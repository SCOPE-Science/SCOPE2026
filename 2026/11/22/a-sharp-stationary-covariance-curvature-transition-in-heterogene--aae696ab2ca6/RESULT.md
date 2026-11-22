# A sharp stationary covariance-curvature transition in heterogeneous telegraph resetting

## Finding

For a spatially heterogeneous finite-speed persistent particle with complete Poisson resets, the normalized *right-hand initial slope* of the physical-position stationary autocovariance is universal, while its *right-hand curvature* changes sign at one exact ratio of reset to tumbling rates. This gives an inverse rule recovering both rates and the propulsion scale from short-lag measurements and a single stationary variance.

Fix a heterogeneity exponent \(0<\alpha<2\), particle speed coefficient \(v>0\), velocity-flip rate \(\nu>0\), and reset rate \(r>0\). The physical position obeys the canonical Lamperti-flow interpretation of \(\dot X_t=v|X_t|^{\alpha/2}\Sigma_t\), where \(\Sigma_t\in\{-1,+1\}\) flips at rate \(\nu\). Independent Poisson resets of rate \(r\) set the position to zero and redraw the sign fairly and independently. Write \(C(t)=\operatorname{Cov}(X_0,X_t)\) in the unique stationary law. Then \(C(0)>0\), and the first two right derivatives exist, with
\[
\boxed{\frac{C'(0+)}{C(0)}=-\frac r2,\qquad
       \frac{C''(0+)}{C(0)}=\frac{r(\alpha r-4\nu)}{2(\alpha+2)}.}
\]
Thus at fixed \(\alpha,\nu>0\) the covariance is locally concave when \(r<4\nu/\alpha\), has zero curvature at equality, and is locally convex when \(r>4\nu/\alpha\). This is a **unique sharp curvature transition** for all positive reset rates; it is independent of \(v\). At the homogeneous boundary \(\alpha=0\), the formula remains valid and the curvature is always negative, \(C''(0+)/C(0)=-r\nu\).

More quantitatively, set \(\beta=1-\alpha/2\) and \(p=1/\beta\). If the exponent \(\alpha\) is known, the observed triple \((M,A,B)=(C(0),C'(0+),C''(0+))\) uniquely reconstructs all three positive dynamical parameters on their admissible range:
\[
\boxed{r=-\frac{2A}{M},\quad
\nu=\frac14\left(\alpha r-\frac{2(\alpha+2)B}{rM}\right),\quad
v=\sqrt{r(r+2\nu)}\left(\frac{M}{\beta^{2p}\Gamma(2p+1)}\right)^{1/(2p)}.}
\]
The formulas are statements of exact population-level identifiability, not finite-sample statistical guarantees.

## Assumptions and scope

The process is continuous in physical time, nonabsorbing and defined on the full real line. All three rates/scales \(r,\nu,v\) are strictly positive; the heterogeneity exponent is fixed in \(0<\alpha<2\). The sign flips according to an independent symmetric continuous-time Markov chain between resets. Each reset simultaneously resets position to zero and independently chooses a new equally likely velocity sign. The zero-crossing convention is essential: letting
\[
Y_t=\operatorname{sgn}(X_t)|X_t|^\beta/\beta,
\qquad X_t=g(Y_t)=\operatorname{sgn}(Y_t)(\beta|Y_t|)^p,
\]
we **define** the physical motion by taking \(Y\) as an ordinary velocity-jump process of velocities \(\pm v\) with the above complete resets and applying \(g\). In particular, it crosses the origin rather than remaining in a nonunique, indefinitely stuck solution of the pointwise nonlinear ODE at zero. This is the same signed-coordinate branch underlying the heterogeneous telegrapher density in the motivating literature. There is no translational Brownian term and no partial or position-only resetting.

The stationary mean position vanishes by reflection symmetry, so \(C(t)=\mathbb E[X_0X_t]\). Right derivatives are used because reset jumps can generate a cusp at time zero when the stationary covariance is extended to negative lags.

## Proof

**1. Reduction and stationary distribution.** The Lamperti transformation gives \(\dot Y_t=v\Sigma_t\) between resets. It has regenerative cycles, because after each Poisson reset the state is independently fixed at \((Y,\Sigma)=(0,\pm1)\) with fair sign. Coupling at the first reset proves uniqueness of the stationary law. Let
\[
\lambda=\frac{\sqrt{r(r+2\nu)}}{v}.
\]
The stationary distribution of \(Y\) is exactly the bilateral exponential density \(f(y)=(\lambda/2)e^{-\lambda|y|}\), as follows either from the exponential-age resolvent of the telegraph equation or from solving the stationary two-velocity forward equations. Its stationary absolute moments are
\[
\mathbb E|Y|^s=\frac{\Gamma(s+1)}{\lambda^s}\quad(s>-1),
\quad M=\mathbb E[X^2]=\frac{\beta^{2p}\Gamma(2p+1)}{\lambda^{2p}}>0.
\]
All moment integrals in the proof are finite since \(p>1\).

**2. First derivative by stationary moment balance.** For the unreset process in the transformed coordinate let \(\mathcal A=v\sigma\partial_y+\nu(\mathcal F-I)\), where \(\mathcal F f(y,\sigma)=f(y,-\sigma)\). The complete-reset generator is \(\mathcal L=\mathcal A+r(\mathcal R-I)\), with \(\mathcal R f\) the average of \(f(0,\pm1)\). Because \(g(0)=0\), stationarity of \(g^2(Y)\) gives
\[
0=\mathbb E\mathcal L(g^2)=2v\,\mathbb E[g(Y)\Sigma g'(Y)]-rM,
\]
so \(v\mathbb E[g(Y)\Sigma g'(Y)]=rM/2\).

The no-reset evolution from the stationary state is denoted \(Y_t^{(0)}\). If a reset occurs during \((0,t]\), the future position has zero conditional mean independently of the pre-reset state; therefore
\[
C(t)=e^{-rt}H(t),\qquad H(t)=\mathbb E[g(Y_0)g(Y_t^{(0)})].
\]
Here \(H(0)=M\) and \(H'(0+)=v\mathbb E[g(Y)\Sigma g'(Y)]=rM/2\). Product differentiation yields \(C'(0+)=-rM/2\).

**3. Second derivative and sharp sign.** The no-reset generator satisfies
\[
\mathcal A g=v\sigma g',\qquad \mathcal A^2g=v^2g''-2\nu v\sigma g'.
\]
For \(p>1\), \(g'\) is continuous, \(g''\) is locally integrable, and the product \(g(y)g''(y)=\beta^{2p}p(p-1)|y|^{2p-2}\) has a finite stationary expectation. Consequently the two right derivatives of \(H\) follow by differentiating the telegraph semigroup, or by smoothing \(g\) at the origin and applying the bounded-velocity translation formula before dominated convergence:
\[
H''(0+)=v^2\mathbb E[g(Y)g''(Y)]-2\nu v\mathbb E[g(Y)\Sigma g'(Y)].
\]
Combining with \(C(t)=e^{-rt}H(t)\), the balance in step 2 cancels the reset contributions and gives
\[
C''(0+)=v^2\mathbb E[g(Y)g''(Y)]-r\nu M.
\]
Direct Gamma integration yields
\[
\frac{v^2\mathbb E[g(Y)g''(Y)]}{M}
=\frac{v^2p(p-1)\lambda^2}{(2p)(2p-1)}
=\frac{(p-1)r(r+2\nu)}{2(2p-1)}.
\]
Using \(p=2/(2-\alpha)\) proves the claimed curvature formula. As its denominator and \(r\) are strictly positive, the sign is exactly the sign of \(\alpha r-4\nu\). For \(\alpha=0\), \(g\) is linear and its second derivative vanishes, yielding \(-r\nu\) without taking any singular limit.

**4. Inverse identification.** The first jet yields the unique positive \(r\); the second jet then determines \(\nu\) algebraically; finally the stationary Gamma-moment identity in step 1 uniquely gives positive \(v\). Substitution proves the displayed inverse formula, with no additional branches when these inferred parameters are positive. The inference is conditional on a known exponent and on the specified model, not an inverse theorem for all possible stochastic processes.

## Verification

The standalone Python 3 standard-library program `checker.py` reproduces the curvature and inverse formulas. In three polynomial Lamperti cases (\(p=3,5,7\)), it builds the full two-state Markov generator on polynomial observables and verifies both derivatives **exactly using rational arithmetic** on a 45-case grid per degree (135 model instances). It additionally evaluates the noninteger-power Gamma integrals and reconstructs \(r,\nu,v\) on a positive-parameter grid. A finite checker is supporting evidence only; the proof applies to the full parameter continuum.

Run: `python checker.py`. The expected output reports 1,343 passed exact-rational and floating-point assertions.

## Relationship to prior work

Sandev, Kocarev, Metzler and Chechkin (arXiv:2211.01909v1, first submitted 2022-11-03), particularly Sections II, III and V, establish the heterogeneous telegrapher model, signed-coordinate density, mean-square displacement and resetting stationary marginal. Those are the foundations, not the new contribution. The assertion here instead concerns the **physical-position stationary two-time covariance**, its exact curvature phase boundary and the resulting short-lag inverse map; the inspected source sections do not provide these identities.

Evans and Majumdar (arXiv:1808.06450) address Poisson resetting of a homogeneous run-and-tumble particle. The published mathematical result *Static-state blindness and a sharp temporal-memory crossover under run-and-tumble resetting* analyzes the homogeneous **linear-coordinate** stationary covariance, including optional thermal noise and reset-flip behavior, but does not imply the sign-changing curvature of the nonlinear physical coordinate for \(0<\alpha<2\). Sandev and Iomin (Phys. Rev. E 110, 024101, 2024) investigate fractional heterogeneous telegraph marginals and mean squared displacements; their abstract does not provide an equivalent stationary two-time curvature formula. A broader generator or semigroup result could rederive the underlying identities, so this source-specific originality comparison does not constitute an independent priority certification.

## Limitations

The model's signed-origin crossing convention matters because the nonlinear velocity field vanishes at zero. The result is not asserted for negative heterogeneous exponents, \(\alpha\ge2\), partial resets, asymmetrically chosen headings, non-Poisson clocks, or thermal diffusion. A positive initial right curvature is **not** a claim that the covariance initially increases: its slope is always strictly negative. The inverse rule assumes exact population-level derivatives, a known \(\alpha\), and strictly positive inferred parameters; noise sensitivity and optimal estimation are open practical questions. The finding has not undergone independent mathematical audit.

## References

1. T. Sandev, L. Kocarev, R. Metzler and A. Chechkin, *Stochastic dynamics with multiplicative dichotomic noise: heterogeneous telegrapher's equation, anomalous crossovers and resetting*, arXiv:2211.01909v1, first submitted 2022-11-03, https://arxiv.org/html/2211.01909v1.
2. M. R. Evans and S. N. Majumdar, *Run and tumble particle under resetting: a renewal approach*, arXiv:1808.06450, 2018, https://arxiv.org/abs/1808.06450.
3. T. Sandev and A. Iomin, *Fractional heterogeneous telegraph processes: Interplay between heterogeneity, memory, and stochastic resetting*, Physical Review E **110**, 024101 (2024), https://doi.org/10.1103/PhysRevE.110.024101.
4. *Static-state blindness and a sharp temporal-memory crossover under run-and-tumble resetting*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-static-state-blindness-and-a-sharp-temporal-memory-crossover-und--f3cc5401e836.
