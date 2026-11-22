# Sub-Poisson first-passage uncertainty at the mean-optimal rate for retained boundary contact

## Finding

For a reflected Brownian particle on the half-line, complete Poisson *position* relocations do not erase accumulated boundary-contact local time. This distinction leads to a sharp and experimentally interpretable departure from the coefficient-of-variation-one law for complete renewal resetting.

Let \(D,x_0,h>0\). Start a reflected Brownian motion at \(x_0\) with generator \(D\partial_{xx}\), relocate its position to \(x_0\) at rate \(r>0\), and **retain** its cumulative boundary local time \(L_t\). Stop at \(T_h=\inf\{t:L_t\ge h\}\). Put \(\lambda=h/x_0\), \(z=x_0\sqrt{r/D}\), and let \(z_0\in(1,2)\) be the unique positive root of
\[
2-z_0-2e^{-z_0}=0,\qquad z_0=1.593624260040040\ldots.
\]

The mean reaction time has one and only one global minimizer \(r_*(h)>0\). Its dimensionless coordinate \(z_*(\lambda)=x_0\sqrt{r_*(h)/D}\in(1,z_0)\) is the unique solution of
\[
\boxed{2-z-2e^{-z}=\lambda z(z-1).}
\]
The optimum decreases strictly with the contact threshold and obeys
\[
\frac{D}{x_0^2}<r_*(h)<\frac{Dz_0^2}{x_0^2},\quad
\lim_{h\downarrow0}r_*(h)=\frac{Dz_0^2}{x_0^2},\quad
\lim_{h\to\infty}r_*(h)=\frac{D}{x_0^2}.
\]

**Exact uncertainty identity at the optimum.** For every \(h>0\), at \(r=r_*(h)\),
\[
\boxed{\operatorname{Var}(T_h)
=(\mathbb E T_h)^2-\left(\frac{h e^{z_*(\lambda)}}{\sqrt{r_*(h)D}}\right)^2.}
\]
In particular, \(0<\operatorname{Var}(T_h)<(\mathbb ET_h)^2\), so the optimal reaction-time coefficient of variation is **strictly below one**. This contrasts with the coefficient of variation exactly one for mean-optimal *complete* Poisson restart of a first-passage process. It quantifies the statistical signature of surface-reaction progress retained across relocations.

The full-reset comparison is sharp: if every position relocation instead also erases the accumulated local time, its minimizing rate is \(r_{\rm erase}=Dz_0^2/(x_0+h)^2\), and
\[
\boxed{r_*(h)>r_{\rm erase}\quad\text{for every }h>0.}
\]
For small positive \(\lambda\), the two optimal square-root rates agree to first order and separate at second order:
\[
z_*(\lambda)-\frac{z_0}{1+\lambda}
=\frac{z_0^3}{2(z_0-1)}\lambda^2+O(\lambda^3).
\]
As \(\lambda\to\infty\), \(z_*(\lambda)=1+(1-2/e)/\lambda+O(\lambda^{-2})\).

## Assumptions and scope

Between jumps the particle satisfies the reflected SDE \(dX_t=\sqrt{2D}\,dB_t+dL_t\) on \([0,\infty)\), with the minimal nondecreasing continuous regulator \(L_t\) increasing only at \(X_t=0\). Equivalently, its normalization is \(L_t=\lim_{\epsilon\downarrow0}(D/\epsilon)\int_0^t\mathbf 1_{[0,\epsilon]}(X_s)\,ds\) in the standard local-time sense. At Poisson reset times only \(X_t\) is replaced by \(x_0\); \(L_t\) is not replaced, decreased, or randomized. The Brownian noise and Poisson clock are independent. The threshold \(h>0\) is deterministic, and the process begins with \(X_0=x_0\), \(L_0=0\). At each positive \(r\), \(T_h\) has finite first and second moments.

The result concerns one-dimensional reflection and deterministic positive reset distance; no result is claimed for general reset-position mixtures, stochastic reaction thresholds, non-Poisson relocations, or higher-dimensional surface local times. The zero-threshold value is used only as a limiting comparison; the claimed strict dispersion inequality requires \(h>0\).

## Proof

**1. Exact stopping-time transform.** For \(s\ge0\), put \(q_s=\sqrt{(r+s)/D}\). Let \(H\) be the first time the *position* hits zero, starting from \(x_0\). Prior to \(H\) the reflecting wall is immaterial. Solving the backward equation
\[
D u''-(r+s)u+ru(x_0)=0\quad(x>0),\qquad u(0)=1,
\]
for a bounded \(u\) gives
\[
G(s):=\mathbb E_{x_0}e^{-sH}
=\frac{r+s}{r+s e^{x_0q_s}}.
\]
The derivative of the same solution at zero is \(-\phi(s)\), where
\[
\phi(s)=\frac{s q_s e^{x_0q_s}}{r+s e^{x_0q_s}}.
\]
By the strong Markov property at boundary local-time levels, the inverse local time starting from the reflecting boundary is a subordinator. The reflecting SDE normalization implies its Laplace exponent is \(-u'(0)=\phi(s)\). One may equivalently verify this by taking \(F(x,\ell)=u(x)e^{-(h-\ell)\phi(s)}\) and checking the interior backward equation together with the oblique boundary condition \(F_x(0,\ell)+F_\ell(0,\ell)=0\). Since \(H\) ends at the boundary, the post-hitting inverse-local-time increment is independent of \(H\). Thus, for \(h>0\),
\[
\boxed{\mathbb E_{x_0}e^{-sT_h}
=\frac{r+s}{r+s e^{x_0q_s}}
\exp\!\left[-h\frac{s q_s e^{x_0q_s}}{r+s e^{x_0q_s}}\right].}
\]
The transform equals one at zero, and is analytic around zero for \(r>0\), ensuring finite moments. This transform itself follows from known retained-local-time formulas; it is included as an input to the new optimality/uncertainty calculation, not claimed as new.

**2. First two cumulants.** Write \(E=e^z\), \(\lambda=h/x_0\), \(z=x_0\sqrt{r/D}\). Differentiation of the logarithm of the transform at \(s=0\) yields
\[
M(z,\lambda):=\mathbb ET_h
=\frac{x_0^2}{D}\left[\frac{E-1}{z^2}+\frac{\lambda E}{z}\right],
\]
\[
V(z,\lambda):=\operatorname{Var}(T_h)
=\frac{x_0^4}{D^2}\left[\frac{E^2-1-zE}{z^4}+\frac{\lambda E(2E-z-1)}{z^3}\right].
\]
These formulas can also be obtained by adding the independent first-hitting-time cumulants and the cumulants of the inverse-local-time subordinator.

**3. Global uniqueness and monotonicity.** Apart from the positive prefactor, the derivative of the mean with respect to \(z\) has sign
\[
\operatorname{sgn}\partial_zM
=\operatorname{sgn}\{E(z-2)+2+\lambda z E(z-1)\}.
\]
For \(0<z\le1\) both terms are strictly negative; for \(z\ge z_0\) both are nonnegative and at least one is positive. In the remaining interval \((1,z_0)\), the stationary equation reads
\[
\lambda=\Lambda(z):=\frac{2-z-2e^{-z}}{z(z-1)}.
\]
Its numerator is positive and strictly decreasing on \((1,z_0)\), its denominator strictly increasing, and its endpoint limits are \(+\infty\) and \(0\). Thus \(\Lambda\) is a strictly decreasing bijection from \((1,z_0)\) to \((0,\infty)\); the derivative changes once from negative to positive. This proves unique global minimality, strict threshold monotonicity, and the rate bounds. The implicit-function theorem gives smooth dependence and the stated small/large \(\lambda\) expansions. At \(z=z_0\), \(\Lambda'(z_0)=-1/z_0\) and \(\Lambda''(z_0)=(z_0^2+2z_0-2)/[z_0^2(z_0-1)]\), giving the displayed second-order coefficient.

**4. Exact optimal uncertainty cancellation.** Subtracting \(M^2\) from \(V\) and factoring gives
\[
V-M^2=\frac{x_0^4}{D^2z^4}
\left[E(2-z)-2+\lambda zE(1-z)-\lambda^2 z^2E^2\right].
\]
At the unique optimum, the mean-derivative equation says \(E(2-z)-2=\lambda zE(z-1)\). Therefore the first two terms cancel *exactly*, leaving \(V-M^2=-(x_0^4/D^2)\lambda^2E^2/z^2=-[hE/\sqrt{rD}]^2\). Strict positivity of the variance follows from the nondegenerate Brownian/Poisson evolution. This proves the asserted strictly subunit coefficient of variation.

**5. Separation from complete state resetting.** Erasing the local-time progress at every reset gives the classical renewal mean \(M_{\rm erase}(r)=[\exp((x_0+h)\sqrt{r/D})-1]/r\). Its unique optimizer is \(z_{\rm erase}=z_0/(1+\lambda)\). If this value is at most one, then \(z_*(\lambda)>z_{\rm erase}\) is immediate. Otherwise set \(q=z_{\rm erase}\in(1,z_0)\). The inequality \(\Lambda(q)>\lambda=(z_0-q)/q\) is equivalent to \(N(q)>0\), where
\[
N(q)=q^2-(z_0+2)q+z_0+2-2e^{-q}.
\]
Here \(N(z_0)=N'(z_0)=0\) and \(N''(q)=2-2e^{-q}>0\) for \(q>0\). Thus \(N(q)>0\) for \(q<z_0\), and since \(\Lambda\) is strictly decreasing, \(z_*(\lambda)>q\). Squaring gives the strict rate comparison. Taylor expansion at \(\lambda=0\) gives the sharp second-order gap. This completes the theorem.

## Verification

Run `python check.py` using Python 3 and no third-party packages. The checker independently differentiates the exact Laplace transform using 64-digit decimal arithmetic; compares the resulting mean and variance against the closed forms for 32 deterministic pseudo-random positive parameter choices; brackets the unique optimizer in 60 additional parameter cases; tests the exact optimal variance identity and reset-protocol inequality; and checks both asymptotic regimes. It prints `PASS 549 ...` on success. Its finite tests do not prove uniqueness, the all-parameter strict inequalities, or the process-level transform; those are established by the preceding argument.

## Relationship to prior work

Bressloff (arXiv:2203.04868, 2022), sections 2.3 and 3, derives the *position-only* resetting mean reaction time, exactly the formula used in step 2, and gives plots of optimal-rate shifts. No novelty is claimed for that mean or the retained-local-time transform. A published related analysis, *A sharp two-site cusp for boundary-reaction throughput under position-only resetting* (2026), supplies the general inverse-local-time Laplace transform for distributed reset sites, and even contains the single-site case here. That full-transform contribution is also acknowledged as prior, not credited here. Reuveni (arXiv:1512.01600, 2015/2016) establishes coefficient of variation one at optimal *complete renewal* restart. The present contribution is the finite positive contact-threshold **global optimizer classification together with its exact optimal-variance deficit**, and the strict second-order separation of optimal rates for protocols that preserve versus erase reaction progress. These statements require optimizing and relating both cumulants, and are not explicit in the inspected comparison results.

## Limitations

The result is a theorem about this fully specified reflected Brownian model. It is not a new derivation of known contact-time transforms or mean first-passage formulas, and does not assert a comparable exact deficit for arbitrary reset locations or boundary geometries. It does not give finite-sample statistical power or experimental efficiencies. Although direct matching results were not identified in the comparisons, a sufficiently general published renewal/subordinator optimization theorem could still imply the optimal-variance identity; literature-priority verification remains qualified and independent review has not been performed.

## References

1. P. C. Bressloff, *Threshold surface reactions and local time resetting*, arXiv:2203.04868, initially public 2022-03-09. https://arxiv.org/abs/2203.04868 (especially sections 2.3 and 3, equations (3.11)--(3.17)).
2. *A sharp two-site cusp for boundary-reaction throughput under position-only resetting*, public mathematical result, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-sharp-two-site-cusp-for-boundary-reaction-throughput-under-pos--f0edb8ae038d/RESULT.md
3. *Power-law survival versus exponential rescue for retained and refreshed surface-reaction thresholds*, public mathematical result, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-power-law-survival-versus-exponential-rescue-for-retained-and-re--f7a7f8b3a2be/RESULT.md
4. S. Reuveni, *Optimal stochastic restart renders fluctuations in first passage times universal*, arXiv:1512.01600 (first public 2015-12-05), Phys. Rev. Lett. 116, 170601 (2016). https://arxiv.org/abs/1512.01600
