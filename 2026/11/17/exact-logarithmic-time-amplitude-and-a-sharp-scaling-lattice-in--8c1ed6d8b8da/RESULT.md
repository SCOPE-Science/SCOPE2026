# Exact logarithmic-time amplitude and a sharp scaling lattice in a stable cubic flow

## Finding

Consider the planar homogeneous cubic family
\[
\begin{aligned}
\dot x&=\bigl((-a+b)x^2+(-a-b)y^2\bigr)x-(x^2+y^2)y,\\
\dot y&=\bigl((-a+b)x^2+(-a-b)y^2\bigr)y+(x^2+y^2)x,
\end{aligned}
\]
with \(a>0\), \(b\in\mathbb R\). For every nonzero initial condition, put \(r(t)=\sqrt{x(t)^2+y(t)^2}\) and choose the continuous lifted polar angle \(\theta(t)\). There is an explicit positive, universal, smooth function \(P_{a,b}\), of period \(2\pi a\), and an initial-condition-dependent \(C>0\) and phase \(\phi\), such that the **exact physical-time identity**
\[
\boxed{(t+C)r(t)^2=P_{a,b}\!\left(\log\frac{t+C}{C}+\phi\right)}
\qquad(t\ge0)
\]
holds. When \(b\ne0\), \(P_{a,b}\) is nonconstant and has **least** positive period \(2\pi a\). Consequently \(t r(t)^2\) has a nondegenerate interval of accumulation values, and, for every \(c>0\),
\[
\boxed{\lim_{t\to\infty}\frac{r(ct)^2}{r(t)^2}\text{ exists }
\iff \log c\in 2\pi a\mathbb Z}
\]
when \(b\ne0\). At those scales the limit is \(1/c\). When \(b=0\), the limit exists at every scale and equals \(1/c\), with \(t r(t)^2\to1/(2a)\). For any \(b\), the times \(t_n\) of successive half-turn returns to the initial polar ray modulo \(\pi\) obey the **exact** formulas
\[
t_n=C\bigl(e^{2\pi an}-1\bigr),\qquad
r(t_n)=r(0)e^{-\pi an},\qquad n=0,1,2,\ldots.
\]
This gives the sharp scaling-lattice transition from ordinary inverse-time squared-radius decay to persistent log-periodic modulation. In the small-anisotropy limit,
\[
\max P_{a,b}-\min P_{a,b}=\frac{|b|}{a\sqrt{1+a^2}}+O(b^2),\qquad b\to0,
\]
with \(a>0\) fixed.

## Assumptions and scope

All assertions concern the forward-complete classical solutions of the **specified** polynomial vector field on \(\mathbb R^2\), for arbitrary real \(b\), strictly positive \(a\), and nonzero initial state. The origin is a stationary equilibrium and is excluded from all radial quotients and polar-angle definitions. The angular coordinate is a real continuous lift, not an angle modulo \(2\pi\). Physical time starts at \(t=0\). Let
\[
Q_{a,b}(\theta)=e^{b\sin2\theta}
\int_0^\infty e^{-2av-b\sin2(\theta-v)}\,dv.
\]
This is positive, real analytic and \(\pi\)-periodic. Define
\[
\Psi_{a,b}(\theta)=\int_0^\theta\frac{du}{Q_{a,b}(u)},
\quad P_{a,b}(s)=Q_{a,b}\!\bigl(\Psi_{a,b}^{-1}(s)\bigr),
\quad C=\frac{Q_{a,b}(\theta(0))}{r(0)^2},
\quad \phi=\Psi_{a,b}(\theta(0)).
\]
The inverse exists globally because \(Q_{a,b}>0\), and \(\Psi_{a,b}\) grows without bound in both directions. These formulas define the previously stated universal profile and all constants without ambiguity. The case \(a=1,b=5\) is the specific cubic counterexample of Liu and Fitzsimmons (2026).

## Proof

**Polar reduction and completeness.** Direct computation gives
\[
\dot r=r^3(-a+b\cos2\theta),\qquad \dot\theta=r^2.
\]
Thus \(d\log r/d\theta=-a+b\cos2\theta\) and
\[
r(\theta)=r_0\exp\!\left[-a(\theta-\theta_0)
+\frac b2(\sin2\theta-\sin2\theta_0)\right].
\]
Because \(a>0\), this radius remains positive and bounded for increasing angle, while \(dt/d\theta=1/r(\theta)^2\) integrates to infinity as \(\theta\to\infty\). Hence every nonzero forward trajectory exists for all \(t\ge0\), approaches the origin, and winds infinitely often. Alternatively \(H=r^2e^{-b\sin2\theta}\) satisfies \(\dot H=-2ar^2H<0\) away from the origin.

**Periodic amplitude equation.** Differentiating the defining integral and using its exponential kernel, or integrating the scalar linear equation over the infinite past, yields
\[
Q_{a,b}'(\theta)=1+\bigl(-2a+2b\cos2\theta\bigr)Q_{a,b}(\theta).
\]
The solution is the **unique** \(\pi\)-periodic solution: two such solutions differ by a constant times \(\exp(-2a\theta+b\sin2\theta)\), which cannot be periodic unless that constant is zero. It is strictly positive by its integral formula. Dividing its differential equation by \(Q\) and integrating over one angular period yields
\[
\int_{\theta}^{\theta+\pi}\frac{du}{Q_{a,b}(u)}=2\pi a;
\]
indeed the terms \(Q'/Q\) and \(\cos2u\) have zero period integral. Thus \(P_{a,b}\) is a positive smooth function with period \(2\pi a\).

**Exact time-renormalization identity.** Set \(S(t)=(t+C)r(t)^2-Q_{a,b}(\theta(t))\). Using the polar equations and the displayed equation for \(Q\) gives
\[
\dot S=2r^2(-a+b\cos2\theta)S.
\]
Our choice of \(C\) gives \(S(0)=0\), so uniqueness for this scalar linear equation proves \((t+C)r(t)^2=Q_{a,b}(\theta(t))\) exactly. Consequently
\[
\frac{d}{dt}\Psi_{a,b}(\theta(t))=
\frac{r(t)^2}{Q_{a,b}(\theta(t))}=\frac1{t+C}.
\]
Integration gives \(\Psi(\theta(t))=\phi+\log((t+C)/C)\), proving the stated identity for \(P\).

**Sharp least period and scale classification.** If \(b=0\), the periodic equation gives \(Q\equiv1/(2a)\), so the ordinary scalar decay follows. Conversely, if \(b\ne0\), the identity
\[
2b\cos2\theta=\frac{Q'(\theta)-1+2aQ(\theta)}{Q(\theta)}
\]
shows that every period of \(Q\) must be a period of \(\cos2\theta\). As \(Q\) already has period \(\pi\), its least positive period is precisely \(\pi\). The strictly increasing change of coordinate \(\Psi\) sends this period to \(2\pi a\). To prove **minimality** after reparametrization, suppose \(P\) had a smaller positive period \(T<2\pi a\). Because \(\frac{d}{ds}\Psi^{-1}(s)=P(s)\), periodicity would imply \(\Psi^{-1}(s+T)=\Psi^{-1}(s)+D\), where \(D=\int_0^T P(s)\,ds\) is independent of \(s\) and satisfies \(0<D<\int_0^{2\pi a}P(s)\,ds=\pi\). Then \(Q(\theta+D)=Q(\theta)\) for every \(\theta\), contradicting the least period \(\pi\) of \(Q\). Thus \(P\) has least positive period \(2\pi a\) and is nonconstant. Since \(\theta(t)\to\infty\) continuously, \(t r(t)^2\) has precisely the cluster set \(Q([0,\pi])=[\min Q,\max Q]\), with distinct endpoints. From the exact \(P\)-formula,
\[
\frac{r(ct)^2}{r(t)^2}=
\frac{t+C}{ct+C}\,
\frac{P\bigl(s(t)+\log((ct+C)/(t+C))\bigr)}{P(s(t))},
\qquad s(t)=\phi+\log((t+C)/C).
\]
If the ratio has a limit, periodicity and the continuous sweep of \(s(t)\) imply \(P(s+\log c)/P(s)\) is a constant in \(s\). Averaging its logarithm over one period forces that constant to equal one; the least-period result then forces \(\log c\in2\pi a\mathbb Z\). Conversely, these scales give the limit \(1/c\) by uniform continuity and periodicity. This proves the necessary-and-sufficient scaling lattice.

**Exact return clocks.** At the first time \(t_n\) with \(\theta(t_n)=\theta_0+n\pi\), the angular integral of \(1/Q\) gives \(\log((t_n+C)/C)=2\pi an\); the radial formula gives \(r(t_n)=r_0e^{-\pi an}\). Both are exact for all nonnegative integers \(n\).

**Anisotropy onset.** Differentiating the unique periodic equation with respect to \(b\) at \(b=0\) gives
\[
Q_{a,b}(\theta)=\frac1{2a}
+\frac{b}{2(1+a^2)}\left(\cos2\theta+\frac1a\sin2\theta\right)+O(b^2)
\]
uniformly in \(\theta\) for fixed \(a>0\). Its sinusoidal first-order part has peak-to-peak amplitude \(|b|/(a\sqrt{1+a^2})\), and uniformity of the remainder completes the last claim.

## Verification

The argument above is analytic and is not inferred from finite computation. The accompanying standard-library Python checker independently tests exact Cartesian-to-polar polynomial identities on integer inputs, the periodic profile integral and scalar equation by quadrature, the angular return-time formula, the exact time-shift identity and the nonconstant profile for representative positive \(a\) and nonzero \(b\). Reproduce with `python3 checker.py`. The small-anisotropy coefficient is also checked numerically, but its proof is the analytic expansion above. No infinite claim relies on numerical tolerances.

## Relationship to prior work

Liu and Fitzsimmons (arXiv:2607.16171v1, first posted 17 July 2026) give the explicit \(a=1,b=5\) cubic system, its polar equations, a non-polynomial strict Lyapunov function and the absence of analytic Lyapunov certificates. These established statements are **premises**, not new claims here. The present result determines the exact original-time amplitude, its minimal logarithmic period, the sharp multiplicative scaling subgroup, the geometric angular return clock and the anisotropy onset; none of these is stated in the inspected principal theorem or polar-analysis portion of that paper. Published work on homogeneous-vector-field scaling and on other nonlinear oscillators supplies relevant general context but does not directly identify this exact stable-cubic scaling lattice in the sources inspected. The origin and a general homogeneous scaling identity are not claimed as new.

## Limitations

This theorem is specific to the displayed planar two-parameter homogeneous cubic family with \(a>0\). It does not classify perturbations, stochastic systems, higher-dimensional flows or arbitrary homogeneous vector fields. It does not establish an independent priority certificate; older general homogeneous-flow literature could contain an equivalent formulation not uncovered by the searches. The numerical profile bounds are reproducibility checks rather than rigorous enclosure certificates. The mathematics does not require a polynomial Lyapunov function, and the theorem does not itself prove the prior nonexistence result.

## References

1. J. Liu and M. Fitzsimmons, *A Globally Asymptotically Stable Planar Homogeneous Polynomial Vector Field With No Polynomial Lyapunov Function*, arXiv:2607.16171v1, 17 July 2026, https://arxiv.org/abs/2607.16171 and https://arxiv.org/html/2607.16171.
2. A. Cima and J. Llibre, *Algebraic and topological classification of the homogeneous cubic vector fields in the plane*, Journal of Mathematical Analysis and Applications 147 (1990), 420–448 (general homogeneous planar classification; no full-text priority determination made here).
3. *Probability of Occurrence of Some Planar Random Quasi-homogeneous Vector Fields*, Mediterranean Journal of Mathematics (2022), https://link.springer.com/article/10.1007/s00009-022-02198-w (general quasi-homogeneous scaling context).
