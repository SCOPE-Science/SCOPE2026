# Protocol-independent extreme-direction bias and its unique reset-rate optimum in intermittent transport

## Finding

A particle alternating between unbiased diffusion and left/right ballistic relocation, with full Poisson restarting, has a stationary *far-field directional bias* that is **exactly independent of which motility phase is restored at resets**. This bias is nonmonotone in the restart frequency, with exactly one positive global maximizer for **every** choice of positive transport parameters.

Let \(p_0(x),p_+(x),p_-(x)\) be the stationary densities in diffusion, right-moving relocation, and left-moving relocation. Fix \(D,v,\delta,\beta,r>0\), where \(\delta\) is the diffusion-to-relocation rate, \(\beta\) the relocation-to-diffusion rate, and \(r\) the restart rate. Define \(t=r+\beta\). Let \(\lambda\in(0,t/v)\) be the unique small positive spatial decay root of
\[
(r+\delta-D\lambda^2)(t^2-v^2\lambda^2)=\beta\delta t.
\]
For either reset preparation—\(J=0\), or equiprobable \(J=+,J=-\)—the same strict tail limit holds:
\[
\boxed{\lim_{x\to+\infty}\frac{p_+(x)-p_-(x)}{p_+(x)+p_-(x)}=\mathcal P(r):=\frac{v\lambda}{r+\beta}\in(0,1).}
\]
The corresponding limit as \(x\to-\infty\) is \(-\mathcal P(r)\), and the limiting ratio of total relocating to diffusing density on the right is \(\delta/[t(1-\mathcal P(r)^2)]\), also common to both protocols.

This polarization increases from zero, reaches one **unique** maximum at \(r_*>0\), and decreases to zero. Write \(R=r/\beta\), \(a=D\beta/v^2\), and \(b=\delta/\beta\). The maximizing \(R_*\) is the unique physically admissible root of the explicit cubic equation
\[
\boxed{\big[3a(R+1)^2-(2R+b+1)\big](R+2b-1)=9ab(R+1),}
\]
subject to \(R>\max\{0,1-2b\}\) and \(0<(2R+b+1)/[3a(R+1)^2]<1\). The maximum is exactly
\[
\mathcal P(\beta R_*)=\sqrt{\frac{2R_*+b+1}{3a(R_*+1)^2}}.
\]
For small and large reset frequency respectively,
\[
\mathcal P(r)^2\sim\frac{1+b}{a+b}\frac r\beta,\qquad
\mathcal P(r)^2\sim\frac{v^2}{Dr}.
\]
For \(D=v=\beta=\delta=1\), the optimum is \(r_*=1.0971675407097277\ldots\) and \(\mathcal P(r_*)=0.5638165332097669\ldots\).

## Assumptions and scope

The state is \((X_t,J_t)\in\mathbb R\times\{0,+,-\}\). In phase \(0\), \(dX_t=\sqrt{2D}\,dW_t\); in phases \(+,-\), its deterministic velocity is \(+v,-v\). Switching \(0\to\pm\) occurs with rate \(\delta/2\) each, and \(\pm\to0\) at rate \(\beta\). An independent rate-\(r\) Poisson process instantaneously resets position to zero and renews the motility phase. Preparation \(\mathcal D\) chooses phase \(0\) at every reset; preparation \(\mathcal B\) chooses \(+\) or \(-\) with equal probabilities. All parameters are fixed and strictly positive. The unique stationary law is regenerative, and its phase densities are continuous for \(x\ne0\). Ratios are taken at fixed positive parameters before any small- or large-\(r\) limit.

## Proof

**Stationary resolvent and positive slow mode.** The stationary equations on \(x\ne0\), with \(t=r+\beta\), are
\[
\begin{aligned}
0&=Dp_0''-(r+\delta)p_0+\beta(p_++p_-),\\
0&=-vp_+'-tp_++\tfrac\delta2 p_0,\\
0&=+vp_-'-tp_-+\tfrac\delta2 p_0.
\end{aligned}
\]
At \(x=0\), reset injections have weights \(w_0,w_b\), where \((w_0,w_b)=(1,0)\) or \((0,1)\), and ballistic injection is split evenly. Fourier transformation gives
\[
\widehat p_0(k)=\frac{r\{w_0(t^2+v^2k^2)+w_b\beta t\}}{Q(k)},\qquad
Q(k)=(r+\delta+Dk^2)(t^2+v^2k^2)-\beta\delta t.
\]
The spatial characteristic polynomial
\[
g(y)=(r+\delta-Dy)(t^2-v^2y)-\beta\delta t
\]
satisfies \(g(0)=rt(t+\delta)>0\), \(g(t^2/v^2)=-\beta\delta t<0\), and \(g(y)\to+\infty\) as \(y\to+\infty\). Because \(g\) is quadratic, its two simple positive roots \(\lambda_-^2,\lambda_+^2\) satisfy \(0<\lambda_-<t/v<\lambda_+\), with \(\lambda=\lambda_-\). Thus \(Q(k)=Dv^2(k^2+\lambda_-^2)(k^2+\lambda_+^2)\). The positive coefficient of \(e^{-\lambda_-x}\) in \(p_0(x)\), for \(x>0\), is
\[
A_0=\frac{r\big[w_0(t^2-v^2\lambda_-^2)+w_b\beta t\big]}{2Dv^2\lambda_-(\lambda_+^2-\lambda_-^2)}>0.
\]
The other diffusing contribution decays at rate \(\lambda_+\); hence \(p_0(x)\sim A_0e^{-\lambda_-x}\) in both preparations. The strict inequality \(\lambda_-<t/v\) also makes every ballistic homogeneous solution, with rate \(t/v\), subleading.

**Universal conditional phases.** Substituting this positive slow mode into the two first-order relocation equations yields
\[
p_+(x)\sim\frac{\delta A_0}{2(t-v\lambda_-)}e^{-\lambda_-x},\qquad
p_-(x)\sim\frac{\delta A_0}{2(t+v\lambda_-)}e^{-\lambda_-x}.
\]
The common amplitude cancels from the two indicated ratios. Reflection symmetry supplies the left-tail statement. Importantly, these are **phase-conditioned** limits, not a claim that the two protocols have the same full stationary spatial law.

**Uniqueness of the optimum.** Set \(z=\mathcal P(r)^2\). The small-root characteristic equation becomes
\[
F(R,z)=(R+1)(1-z)\big[R+b-a(R+1)^2z\big]-b=0,\qquad0<z<1.
\]
At every physical solution the last bracket equals \(b/[(R+1)(1-z)]>0\); therefore \(F_z<0\), and the implicit branch \(z(R)\) is smooth. At a stationary point, \(F_R=0\) gives
\[
z=z_1(R):=\frac{2R+b+1}{3a(R+1)^2}.
\]
Inserting this into \(F=0\) gives the simultaneous condition
\[
z=z_2(R):=1-\frac{3b}{(R+1)(R+2b-1)}.
\]
Every physical stationary point must have \(R>\max\{0,1-2b\}\). On that interval, \(z_1\) is strictly decreasing because \(z_1'=-2(R+b)/[3a(R+1)^3]<0\), while \(z_2\) is strictly increasing. At its left endpoint \(z_2<z_1\) (or \(z_2\to-\infty\)), and at infinity \(z_2\to1>z_1\to0\). Hence exactly one crossing exists, and it necessarily lies on the physical branch since there \(0<z_1=z_2<1\) and \(F=0\). Its cleared-denominator equation is the displayed cubic. Finally, at \(R\downarrow0\), implicit differentiation at \((0,0)\) gives \(z(R)\sim(1+b)R/(a+b)\); at infinity the small root obeys \(\lambda_-^2\sim r/D\), giving \(z(R)\sim1/(aR)\). Both boundary limits vanish. The unique interior stationary point is therefore the strict global maximum, establishing the claimed sign pattern.

## Verification

Run `python CHECK.py` with Python 3, NumPy, SciPy and SymPy. The standalone program checks 363 assertions: symbolic differentiation and cubic elimination, ordering and residual identities of the spatial roots, strict positivity of leading residues for both reset protocols, numerical Fourier inversion at the origin, far-tail phase ratios calculated from independently inverted phase kernels, agreement of the unique cubic-selected optimum with a separate scalar optimizer across eight diverse parameter choices, and weak/strong reset asymptotics. For stable extreme-tail tests, a common exponential factor is divided out analytically. The checker reports `PASS 363 independent symbolic/numerical assertions`. The all-parameter claims follow from the proof, not from the finite parameter grid.

## Relationship to prior work

Flaquer-Galmés, Campos and Méndez (2024, Sections II–III and Appendix A) introduce these exact switching rates and full-reset protocols, and derive the unconditioned stationary spatial density and search-time statistics. That work is the starting point, not the claimed novelty. The additional conclusion here is the **protocol-independent far-field phase composition together with the global, unique polarization-optimal reset frequency**, which is not a stationary positional density or a mean-first-arrival optimum. The published study *Exact spatial aliasing and strict temporal separation in intermittent resetting transport* analyzes when the two protocols have identical *unconditioned* position distributions and when their lagged position covariances separate; it does not claim or imply the full reset-rate optimization of conditional outward relocation in the far field. Santra, Olsen and Gupta (2024) discuss general dynamical switching with transport and cumulants but do not include this Poisson restart and conditional-tail optimizer. Zhou, Xu and Deng (2019) study pure Lévy walks and CTRWs with resetting rather than this three-phase diffusive–ballistic model. Datta, Beta and Großmann (2024) consider intermittent self-propelled transport but do not impose full Poisson restarts. Deriving spatial phase densities from the original forward equations is standard; the universal cancellation and strict global optimum are the assessed contribution.

## Limitations

The claim applies only to a one-dimensional symmetric three-phase model with positive diffusion, speed, switching and full-reset rates, and resetting to the origin with either of the two specified phase preparations. It does not cover biased direction choice, partial motility reset, non-Poisson restart, bounded domains, interacting searchers or first-passage optimization. The rate \(r=0\) itself has no normalizable stationary law, so endpoint formulas are asymptotic limits. The cubic may have additional algebraic roots outside the physically admissible interval. Numerical benchmarks are not formally interval-certified. Equivalent results in unindexed specialist literature remain possible and independent publication-priority validation has not been performed.

## References

1. R. Flaquer-Galmés, D. Campos and V. Méndez, *Intermittent random walks under stochastic resetting*, Physical Review E **109**, 034103 (2024), arXiv:2401.16849, first publicly posted 2024-01-30. https://arxiv.org/abs/2401.16849 ; https://doi.org/10.1103/PhysRevE.109.034103
2. *Exact spatial aliasing and strict temporal separation in intermittent resetting transport* (2026), public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-spatial-aliasing-and-strict-temporal-separation-in-intermi--a1ab52a1b12f
3. T. Zhou, P. Xu and W. Deng, *Continuous time random walks and Lévy walks with stochastic resetting* (2019), arXiv:1909.07213. https://arxiv.org/abs/1909.07213
4. I. Santra, K. S. Olsen and D. Gupta, *Dynamics of switching processes: general results and applications to intermittent active motion* (2024), arXiv:2408.16643. https://arxiv.org/abs/2408.16643
5. A. Datta, C. Beta and R. Großmann, *The random walk of intermittently self-propelled particles* (2024), arXiv:2406.15277. https://arxiv.org/abs/2406.15277
