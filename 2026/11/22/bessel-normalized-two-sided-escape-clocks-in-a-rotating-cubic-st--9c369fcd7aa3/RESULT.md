# Bessel-normalized two-sided escape clocks in a rotating cubic star-node flow

## Finding

For every \(\lambda>0\), \(\omega>0\), \(\kappa\in\mathbb R\setminus\{0\}\), and \(\sigma\in\mathbb R\), consider the polynomial planar differential equation
\[
\begin{aligned}
\dot x&=\lambda x+\{\sigma(x^2+y^2)+\kappa(x^2-y^2)\}x-\omega(x^2+y^2)y,\\
\dot y&=\lambda y+\{\sigma(x^2+y^2)+\kappa(x^2-y^2)\}y+\omega(x^2+y^2)x.
\end{aligned}
\]
Fix a nonzero initial condition with polar coordinates \((r_0,\theta_0)\), where \(r_0>0\), and take \(\theta(t)\) as a continuous increasing real-valued lift of polar angle. Define \(\beta=\kappa/\omega\), \(\alpha=2\sigma/\omega\),
\[
F_\sigma(s)=\exp(\alpha s+\beta\sin(2s)),\qquad
I_0(\beta)=\frac1\pi\int_0^\pi e^{-\beta\sin(2s)}\,ds.
\]
Then the following is an exact, exhaustive forward-time trichotomy.

**Negative side.** For every \(\sigma<0\), all nonzero solutions are forward global and converge to the unique positive, attracting periodic radial graph
\[
R_*(\theta)=\frac{2\lambda}{\omega}F_\sigma(\theta)
\int_{-\infty}^{\theta}F_\sigma(s)^{-1}\,ds,\qquad R_*(\theta)=r_*(\theta)^2.
\]
For the singular cycle expansion, uniformly in \(\theta\) as \(\sigma\uparrow0\),
\[
|\sigma|R_*(\theta)\longrightarrow
\lambda I_0(\beta)e^{\beta\sin(2\theta)}.
\]

**Critical side.** At \(\sigma=0\), every nonzero solution is forward global and unbounded, with the exact exponential-phase relation
\[
r(t)^2e^{-\beta\sin(2\theta(t))}
=r_0^2e^{-\beta\sin(2\theta_0)}e^{2\lambda t},
\]
and the exact angular growth constant
\[
\lim_{t\to\infty}\theta(t)e^{-2\lambda t}
=\frac{\omega r_0^2 e^{-\beta\sin(2\theta_0)}}{2\lambda I_0(\beta)}.
\]
In particular, \(\lim_{t\to\infty}t^{-1}\log r(t)=\lambda\), but \(r(t)^2e^{-2\lambda t}\) has no limit for \(\kappa\ne0\).

**Positive side.** For every \(\sigma>0\), every nonzero solution escapes to infinity at a finite original physical time, exactly
\[
T_\sigma(r_0,\theta_0)=\frac1{2\lambda}\log\!\left[
1+\frac{2\lambda F_\sigma(\theta_0)}{\omega r_0^2}
\int_{\theta_0}^\infty F_\sigma(s)^{-1}\,ds\right].
\]
As \(\sigma\downarrow0\) for fixed \((r_0,\theta_0)\), the sharp time law is
\[
T_\sigma(r_0,\theta_0)
=\frac1{2\lambda}\log\!\left[
\frac{\lambda I_0(\beta)e^{\beta\sin(2\theta_0)}}{\sigma r_0^2}
\right]+o(1).
\]
For fixed \(\sigma>0\), define the strictly positive, \(\pi\)-periodic phase profile
\[
P_\sigma(\phi)=\frac1\omega\int_0^\infty
\exp\!\left[-\frac{2\sigma}{\omega}v+
\beta\{\sin(2\phi)-\sin(2\phi+2v)\}\right]dv.
\]
Then the **original-time blow-up profile** obeys
\[
\lim_{t\uparrow T_\sigma}\left[(T_\sigma-t)r(t)^2-P_\sigma(\theta(t))\right]=0.
\]
The profile depends on \(\sigma,\kappa,\omega\) but not on the linear growth rate \(\lambda\) or initial condition. The function \(P_\sigma\) is nonconstant whenever \(\kappa\ne0\). Consequently \((T_\sigma-t)r(t)^2\) has a genuine interval of accumulation values, precisely \(P_\sigma([0,\pi])\), rather than a single blow-up coefficient; nevertheless \(r(t)\asymp(T_\sigma-t)^{-1/2}\). All limiting statements use forward physical time, not the desingularized angular clock.

## Assumptions and scope

The coefficients \(\lambda,\omega\) are strictly positive, \(\kappa\) is fixed nonzero, \(\sigma\) is any real parameter, and the initial state is any point of \(\mathbb R^2\setminus\{0\}\). The zero solution remains stationary. All assertions concern the maximal forward solution, with no assumption that the homogeneous cubic term is pointwise contracting. The initial angle is a real lift; changing its value by \(2\pi\) leaves the physical conclusions unchanged. There are no nonzero equilibria since the angular velocity never vanishes.

## Proof

**1. Exact angular and physical-time identities.** Let \(R=r^2\). The polynomial vector field is equivalent, for \(r>0\), to
\[
\dot r=\lambda r+(\sigma+\kappa\cos2\theta)r^3,
\qquad\dot\theta=\omega r^2.
\]
Eliminating time yields a *linear* equation for \(R\):
\[
\frac{dR}{d\theta}=\frac{2\lambda}{\omega}
+\left(\alpha+2\beta\cos2\theta\right)R.
\]
Set \(W(\theta)=R(\theta)/F_\sigma(\theta)\). The integrating factor gives
\[
W(\theta)=\frac{r_0^2}{F_\sigma(\theta_0)}+
\frac{2\lambda}{\omega}\int_{\theta_0}^{\theta}F_\sigma(s)^{-1}ds>0,
\]
which is defined for every finite \(\theta\ge\theta_0\). Since
\(dt/d\theta=1/(\omega R)\) and
\(dW/d\theta=2\lambda/(\omega F_\sigma)\), one obtains the *exact* relation
\[
\frac{dW}{dt}=2\lambda W,
\qquad t(\theta)=\frac1{2\lambda}
\log\frac{W(\theta)}{W(\theta_0)}.
\]
Thus angular time reaches \(+\infty\) precisely at the maximal physical-time endpoint, which is finite exactly when \(\int_{\theta_0}^\infty F_\sigma(s)^{-1}ds\) is finite.

**2. Three regimes and cycle uniqueness.** The factor \(e^{-\beta\sin2s}\) is bounded above and below by positive constants. Hence the integral to positive infinity converges exactly when \(\alpha>0\). This proves all finite-time/global assertions and the explicit \(T_\sigma\). If \(\alpha<0\), the integral from negative infinity to \(\theta\) converges. The stated \(R_*\) is positive, \(\pi\)-periodic by a shift of the integration variable, and solves the radial equation. All other solutions satisfy
\[
R(\theta)-R_*(\theta)=C F_\sigma(\theta)
\]
for a real constant \(C\), so their radial deviations vanish exponentially as \(\theta\to\infty\), establishing attraction and uniqueness. Their physical time tends to infinity; angular position is unbounded because all finite \(\theta\) have finite time.

**3. Sharp Bessel constants on both sides.** The function \(h(s)=e^{-\beta\sin2s}\) is \(\pi\)-periodic, has mean \(I_0(\beta)\), and is strictly positive. Uniformly in the starting phase, the geometric-series identity
\[
\int_0^\infty e^{-\epsilon v}h(\phi\pm v)dv
=\frac{\int_0^\pi e^{-\epsilon v}h(\phi\pm v)dv}
{1-e^{-\epsilon\pi}}
=\frac{I_0(\beta)}{\epsilon}+O(1)
\quad(\epsilon\downarrow0)
\]
proves the claimed uniform cycle amplitude after inserting \(\epsilon=-\alpha\), and the logarithmic escape-time constant after inserting \(\epsilon=\alpha\). In the second case the argument of the logarithm diverges like \(\lambda I_0(\beta)e^{\beta\sin2\theta_0}/(\sigma r_0^2)\), so the additive \(1\) has no effect on the stated \(o(1)\) error.

**4. Critical angular growth.** At \(\alpha=0\), \(W(t)=W(\theta_0)e^{2\lambda t}\), immediately giving the exact phase-normalized radial identity. Also,
\[
\int_{\theta_0}^{\theta(t)}h(s)ds
=\frac{\omega r_0^2e^{-\beta\sin2\theta_0}}{2\lambda}
(e^{2\lambda t}-1).
\]
The integral on the left is \(I_0(\beta)\theta(t)+O(1)\) by periodicity, proving the angular constant. Since \(\theta(t)\to\infty\), its continuous path traverses each angular phase infinitely often; hence the factor \(e^{\beta\sin2\theta(t)}\) has distinct subsequential limits for \(\beta\ne0\).

**5. Phase-resolved type-I blow-up.** Fix \(\alpha>0\), put
\(W_\infty=\lim_{\theta\to\infty}W(\theta)>0\), and define
\(u(\theta)=(W_\infty-W(\theta))/W_\infty\to0\).
The identities in Step 1 give
\[
T_\sigma-t=\frac{-\log(1-u)}{2\lambda},
\quad R=F_\sigma W_\infty(1-u),
\quad \frac{F_\sigma(\theta)}{\omega}
\int_\theta^\infty F_\sigma(s)^{-1}ds
=\frac{F_\sigma W_\infty u}{2\lambda}.
\]
The last expression equals \(P_\sigma(\theta)\) after substituting \(s=\theta+v\). Their ratio shows
\[
\frac{(T_\sigma-t)R}{P_\sigma(\theta)}
=\frac{(1-u)[-\log(1-u)]}{u}\longrightarrow1.
\]
Because \(P_\sigma\) is positive, continuous and periodic, this implies the stated difference tends to zero and yields the two-sided \((T-t)^{-1/2}\) radial bounds. Finally direct differentiation gives
\[
P_\sigma'(\phi)=\left(\alpha+2\beta\cos2\phi\right)
P_\sigma(\phi)-\frac1\omega.
\]
If \(P_\sigma\) were constant, this identity would force \(\beta=0\), contrary to assumption. Since \(\theta(t)\to\infty\), the accumulation set is the entire connected image \(P_\sigma([0,\pi])\). This completes the proof.

## Verification

The accompanying `check.py` checks the polar-coordinate reduction symbolically, the integrating-factor solution and original-time reconstruction against direct high-accuracy numerical ODE integration for parameters on both sides of the threshold. It also checks the Bessel-normalized constants on sequences approaching zero, the nonconstant periodic blow-up profile, and the exact profile differential equation. These numerical tests are consistency checks: the proof of every all-parameter claim is the analytic argument above.

## Relationship to prior work

The star-node framework, the polar radial/angular representation, the qualitative averaging criterion for existence of a limit cycle, and the classification of the cycle at infinity are established in Alarcón–Castro–Labouriau (2021 preprint, 2026 version) and in the related 2023/2024 contracting-nonlinearity article. The pointwise-contracting article does not cover the positive-mean escape regime. The exact affine radial return and physical-time Floquet rigidity for contracting star-node cycles are also documented in the published record listed below. The newer general theory of periodic type-I blow-up profiles by Matsue (2026) covers the qualitative framework for periodic blow-up; its general existence theorem is not claimed here. The present contribution is the explicit, phase-resolved **original-time** trichotomy, the matched Bessel constants on both sides, and the nonconstant exact coefficient at finite-time blow-up in this single cubic family. These are not obtained from the cited qualitative phase portraits or cycle multipliers without a separate physical-time analysis.

## Limitations

This is an exact theorem for one three-parameter cubic structure with one varying mean-radial coefficient; it makes no genericity assertion for all star-node systems. The nonzero-anisotropy hypothesis is essential for the *nonconstant* phase limits. We do not establish any general theorem for nonhomogeneous perturbations, nor independent publication-priority certification. The 2026 general type-I framework and potentially unindexed earlier formulas remain originality risks; the disclosed checks do not establish that no equivalent calculation exists elsewhere.

## References

1. B. Alarcón, S. B. S. D. Castro, I. S. Labouriau, *Global planar dynamics with a star node and contracting nonlinearity*, arXiv:2307.16020, first public version 29 July 2023; *Research in the Mathematical Sciences* 11 (2024), 21, DOI:10.1007/s40687-024-00427-0. https://arxiv.org/abs/2307.16020
2. B. Alarcón, S. B. S. D. Castro, I. S. Labouriau, *Qualitative planar dynamics with star nodes and homogeneous nonlinearities: beyond Hilbert's 16th problem*, arXiv:2106.07516, first public version 14 June 2021; revised 2026. https://arxiv.org/abs/2106.07516
3. K. Matsue, *On Algebraic-Dynamical Correspondence of Oscillatory Blow-Up Solutions for ODEs*, arXiv:2610.05354 (4 October 2026). https://arxiv.org/abs/2610.05354
4. *Exact angular return and physical-time Floquet rigidity for contracting homogeneous star-node cycles*, published 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-angular-return-and-physical-time-floquet-rigidity-for-cont--7c00337eaa41
