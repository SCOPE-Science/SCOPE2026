# A sharp one-ninth duty-cycle threshold for weak flashing-potential diffusion enhancement

## Finding

Consider a one-dimensional Brownian particle in a periodically flashing sinusoidal force, with a randomly refreshed on/off state. A sufficiently weak force enhances effective diffusion above the free diffusivity only if the on-state duty fraction is strictly below \(1/9\), and then only for a bounded interval of redraw rates. This occurs despite the absence of any mean drift. In particular, equal on/off flashing has a strictly *negative* leading diffusivity correction at every positive redraw rate.

Precisely, write \(a=Dk^2\) and \(z=r/a\). For fixed \(D,k,r>0\) and \(0<q<1\),

\[
D_{\mathrm{eff}}(\varepsilon)=D+\frac{\varepsilon^2q}{2a}\left[-q+\frac{(1-q)(z-1)}{(z+1)^2}\right]+O_{D,k,r,q}(\varepsilon^4).
\]

The coefficient is maximized over \(z>0\) uniquely at \(z=3\), and its maximum equals \(q(1-9q)/(16a)\). Thus for \(0<q<1/9\), it is positive if and only if

\[
z_-<z<z_+,\qquad
z_\pm=\frac{1-3q\pm\sqrt{(1-q)(1-9q)}}{2q}.
\]

It is strictly negative outside the closed interval. For \(q>1/9\) it is strictly negative at every \(z>0\). At the boundary \(q=1/9\), the second-order coefficient is nonpositive, vanishing only at \(z=3\). These are classifications of the **quadratic weak-force coefficient**, and determine the sign of \(D_{\mathrm{eff}}-D\) for sufficiently small nonzero \(\varepsilon\) whenever that coefficient is nonzero. No finite-amplitude assertion is made at the equality points.

## Assumptions and scope

Fix \(D>0\), \(k>0\), \(r>0\), \(0<q<1\), and \(\varepsilon\in\mathbb R\). Let \(B_t\) be standard Brownian motion and let the autonomous two-state process \(S_t\in\{0,1\}\) be independently redrawn at the times of a Poisson clock of rate \(r\), with each fresh state equal to one with probability \(q\). An alarm is counted even if the new state equals the previous state. The two-state chain has rates \(0\to1\) equal to \(rq\) and \(1\to0\) equal to \(r(1-q)\), and its stationary law is Bernoulli\((q)\). The particle obeys

\[
dX_t=\varepsilon S_t\sin(kX_t)\,dt+\sqrt{2D}\,dB_t.
\]

The effective diffusivity is \(D_{\mathrm{eff}}=\lim_{t\to\infty}\operatorname{Var}(X_t)/(2t)\); the limit exists and does not depend on the initial state. The forced system is periodic with spatial period \(L=2\pi/k\). The drift vanishes exactly by reflection symmetry. Weak force means \(\varepsilon\to0\) with all the other parameters held fixed, not a simultaneous switching or duty-factor limit. The designation \(82C31\) concerns stochastic diffusion in a fluctuating statistical-mechanics environment.

## Proof

**1. Ergodicity and analytic expansion.** Fold position modulo \(L\), and let \(\pi_0=1-q\), \(\pi_1=q\). For functions \(g=(g_0,g_1)\) on the circle, the backward generator is

\[
(\mathcal L_\varepsilon g)_s=D\partial_x^2g_s+\varepsilon s\sin(kx)\partial_xg_s+r\left(\sum_{u=0}^1\pi_ug_u-g_s\right).
\]

Ellipticity and irreducible switching give a unique smooth invariant probability density \(\rho_{\varepsilon,s}(x)\). At \(\varepsilon=0\) the generator has a simple zero eigenvalue and a spectral gap on its complementary subspace; the stationary densities and centered Poisson corrector are therefore analytic near \(\varepsilon=0\). Reflection \(x\mapsto-x\) reverses position increments, proving zero effective drift. Translation \(x\mapsto x+\pi/k\) changes \(\varepsilon\) to \(-\varepsilon\), leaving the asymptotic variance unchanged. Thus the diffusivity is even analytic in \(\varepsilon\).

**2. First-order invariant measure and corrector.** Define

\[
C_s=\frac q a+\frac{s-q}{a+r},\qquad a=Dk^2.
\]

These constants solve \(aC_s+r(C_s-\sum_u\pi_uC_u)=s\). Substitution into the stationary forward equation and the cell Poisson equation gives the *same* first-order amplitude:

\[
\rho_{\varepsilon,s}(x)=\frac{\pi_s}{L}\left[1-\varepsilon kC_s\cos(kx)\right]+O(\varepsilon^2),
\]

\[
\chi_{\varepsilon,s}(x)=\varepsilon C_s\sin(kx)+O(\varepsilon^2),\qquad
-\mathcal L_\varepsilon\chi_{\varepsilon,s}=\varepsilon s\sin(kx).
\]

The expansion holds in smooth periodic norms. The corrector is defined up to a common additive constant, which does not affect any displayed expression.

**3. Martingale variance formula and cancellation.** The corrected unwrapped coordinate \(X_t+\chi_{\varepsilon,S_t}(X_t)\) is a martingale. Its continuous quadratic variation gives \(2D(1+\partial_x\chi)^2\), and Poisson redraws give squared jumps \((\chi_u-\chi_s)^2\) at rate \(r\pi_u\). Consequently the exact cell formula is

\[
D_{\mathrm{eff}}=D\sum_s\int_0^L\rho_{\varepsilon,s}(1+\partial_x\chi_{\varepsilon,s})^2\,dx
+\frac r2\sum_{s,u}\pi_u\int_0^L\rho_{\varepsilon,s}(\chi_{\varepsilon,u}-\chi_{\varepsilon,s})^2\,dx.
\]

The order-two contribution of \(2D\partial_x\chi\) against the order-one invariant density is \(-Dk^2\varepsilon^2\mathbb E[C_S^2]\), while the order-two squared derivative contributes \(+Dk^2\varepsilon^2\mathbb E[C_S^2]/2\). All first-order and zero-state-measure integrals of periodic derivatives vanish. The jump term contributes \(+r\varepsilon^2\operatorname{Var}(C_S)/2\). Thus

\[
D_{\mathrm{eff}}=D+\frac{\varepsilon^2}{2}\left[-a\mathbb E(C_S^2)+r\operatorname{Var}(C_S)\right]+O(\varepsilon^4).
\]

Here \(\mathbb EC_S=q/a\), \(\operatorname{Var}(C_S)=q(1-q)/(a+r)^2\), and \(\mathbb E(C_S^2)=q^2/a^2+q(1-q)/(a+r)^2\). Direct substitution yields the coefficient in the Finding. The cubic term vanishes by the translation symmetry in step 1.

**4. Sharp global classification.** After multiplying by the strictly positive factor \((1+z)^2\), the bracket's numerator is

\[
-P_q(z),\qquad P_q(z)=qz^2+(3q-1)z+1.
\]

Its discriminant is \((1-q)(1-9q)\). If \(0<q<1/9\), both roots are positive, with midpoint of the positive-coefficient interval containing \(z=3\), and the bracket is positive exactly between those roots. For \(q>1/9\), the discriminant is negative and the leading coefficient is negative everywhere. At \(q=1/9\), \(P_q(z)=(z-3)^2/9\). Finally,

\[
\frac d{dz}\left[-q+\frac{(1-q)(z-1)}{(z+1)^2}\right]
=\frac{(1-q)(3-z)}{(z+1)^3},
\]

so the maximum is unique at \(z=3\) and equals \((1-9q)/8\) for the bracket. Multiplying by \(q/(2a)\) gives the stated maximum \(q(1-9q)/(16a)\). This completes the proof.

## Verification

The standalone `CHECK.py` independently discretizes the two-state stationary forward generator and the backward cell Poisson problem by Fourier collocation. It computes the *full* homogenized diffusivity (including jump quadratic variation), not merely the proposed Taylor coefficient. `python CHECK.py` passed 45 numerical/algebraic cases, including weak-force extrapolation at \(q=1/20\), \(q=1/9\), \(q=1/5\), and \(q=1/2\), multiple redraw rates, and both enhancement and suppression regimes. At \(D=k=1\), \(q=1/20\), \(r=3\), the exact quadratic coefficient is \(0.00171875\), while finite-amplitude quotients at \(\varepsilon=0.10,0.05,0.025\) approach this value. These checks are finite dimensional and do not replace the analytic proof.

## Relationship to prior work

Frydel (2026, arXiv:2611.13526) develops the Poisson-redraw generator, homogenization corrector and dual representation for arbitrary force-state distributions; Sec. XI analyzes an **equally likely** on/off *triangular* potential and reports no diffusivity enhancement for its studied parameters. The present finding applies the established cell methodology, but classifies the quadratic diffusivity coefficient under an **unequal** duty fraction for the distinct smooth sinusoidal force, exposing a sharp enhancement threshold absent from that calculation. Spagnolo and Dubkov (2005/2006, arXiv:cond-mat/0510170) study random switches between **opposite signed** supersymmetric potentials and obtain enhancement; opposite-sign switching is not equivalent to the present asymmetric zero/one flashing. No prior claim is made for the general homogenization method, the Poisson martingale formula, or supersymmetric potential enhancement itself.

## Limitations

The enhancement theorem concerns the coefficient at fixed positive \(r\) and \(q\), not a uniform finite-amplitude phase diagram. At the quadratic zero loci \(z=z_\pm\), and at \(q=1/9,z=3\), fourth-order and higher terms are not classified. The threshold \(1/9\) belongs to the sine profile and independently redrawn on/off state; other potential shapes, renewal clocks, and rate-coupled feedback are not covered. Exact mathematical signs for small amplitude need not translate into measurable enhancement above experimental noise. The investigation is subject to residual publication-priority risk from general two-state perturbation frameworks or unindexed equivalent results. Independent validation has not been performed.

## References

1. D. Frydel, *A new representation of effective diffusion in fluctuating periodic potentials through stochastic duality*, arXiv:2611.13526 (first public submission 2026-11-10), https://arxiv.org/abs/2611.13526, especially Secs. II–III and XI.
2. B. Spagnolo and A. Dubkov, *Diffusion in Flashing Periodic Potentials*, arXiv:cond-mat/0510170 (2005), https://arxiv.org/abs/cond-mat/0510170, especially Sec. III and Eq. (9).
3. S. Lifson and J. L. Jackson, *On the self-diffusion of ions in a polyelectrolyte solution*, J. Chem. Phys. 36, 2410 (1962), classical fixed-potential comparison.
