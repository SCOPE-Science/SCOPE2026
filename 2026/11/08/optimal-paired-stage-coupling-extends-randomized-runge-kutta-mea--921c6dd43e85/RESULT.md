# Optimal paired-stage coupling extends randomized Runge–Kutta mean-square stability past the midpoint barrier

## Finding
For the explicit randomized two-stage Runge–Kutta scheme of Bochacik, Goćwin, Morkisz and Przybyłowicz applied to the scalar test equation \(y'=-\lambda y\) with \(\lambda>0\) and constant step \(h>0\), let \(z=h\lambda\). Every step has an independent Uniform\([0,1]\) stage in the usual construction. Replace this by independent **pairs** of stages, with each stage still Uniform\([0,1]\) but unrestricted dependence between the two members of a pair. Over every such pair law, the exact minimum of the two-step mean-square amplification is
\[
H_*(z)=\begin{cases}
 c(z)^4-\dfrac{c(z)^2z^4}{6}+\dfrac{z^8}{80},&0<z\le1,\\[3pt]
 \dfrac{z^8}{30}\left(72a^5-10a^4-60a^3+40a^2-10a+1\right),&z>1,
\end{cases}
\qquad c(z)=1-z+\frac{z^2}{2},\quad a=\frac{z-1}{z^2}.
\]
The minimum is **attained** by an explicit dependent coupling. The best achievable mean-square convergence from every nonzero deterministic initial scalar is exactly
\[
0<z<z_*,\qquad z_*=2.05632994121192\ldots,
\]
where \(z_*\) is the unique \(z>2\) satisfying \(H_*(z)=1\). In contrast, independent uniform stages have ceiling \(z_{\rm iid}=1.59607163798332\ldots\). At \(z=2\), \(H_*(2)=4/5\), whereas pairing raw stages antithetically gives \(23/15\), and independent stages give \(49/9\). Thus optimal pair dependence produces mean-square decay beyond the deterministic midpoint method's negative-real-axis endpoint \(z=2\).

## Assumptions and scope
The ODE is \(y'=-\lambda y\) with \(\lambda>0\) and deterministic \(y_0\ne0\). At each step the randomized method is
\[
Y^{\rm stage}_j=Y_{j-1}+hU_j(-\lambda Y_{j-1}),\qquad
Y_j=Y_{j-1}+h(-\lambda Y^{\rm stage}_j).
\]
The random variables \((U_{2k+1},U_{2k+2})\), \(k\ge0\), are independent and identically distributed pairs, with both one-dimensional marginals uniform on \([0,1]\). No within-pair independence, symmetry, or fixed copula is assumed. The coupling is permitted to depend on the known test parameter \(z\); any auxiliary fair coins are independent of the paired uniforms and of other epochs. All expectations are over these stage draws. The stability conclusion concerns \(\mathbb E|Y_n|^2\to0\) for every deterministic initial \(Y_0\), not a general nonlinear-ODE error estimate.

## Proof
**1. Two-step reduction.** Each step multiplies its input by \(R_z(U)=1-z+z^2U\). Thus for any admissible pair law \(\pi\),
\[
\mathbb E|Y_{2k}|^2=|Y_0|^2 H_\pi(z)^k,
\qquad H_\pi(z)=\mathbb E_\pi[R_z(U)^2R_z(V)^2].
\]
Moreover \(\mathbb E|Y_{2k+1}|^2=|Y_0|^2 H_\pi(z)^k g(z)\), where \(g(z)=\mathbb E R_z(U)^2=c(z)^2+z^4/12\). Consequently convergence at all indices is equivalent to \(H_\pi(z)<1\); \(H_\pi(z)=1\) is not convergence for nonzero \(Y_0\).

**2. Globally optimal coupling.** The rearrangement inequality for nonnegative random variables gives
\[
\inf_{\pi}\mathbb E_\pi[R_z(U)^2 R_z(V)^2]
=\int_0^1 Q_z(t)^2 Q_z(1-t)^2\,dt,
\]
where \(Q_z\) is the quantile function of \(|R_z(U)|\). This is attainable by countermonotone **magnitudes**, though the original uniform stages need not themselves be antithetic. When \(0<z\le1\), \(R_z(u)\ge0\) and increases in \(u\); taking \(V=1-U\) yields \(R_z(U)R_z(V)=c(z)^2-z^4(U-1/2)^2\). Since \(\mathbb E(U-1/2)^2=1/12\), \(\mathbb E(U-1/2)^4=1/80\), the first displayed formula follows.

When \(z>1\), set \(a=(z-1)/z^2\in(0,1/4]\). Since \(|R_z(U)|=z^2|U-a|\), the quantile of \(|U-a|\) is
\[
q_a(t)=\begin{cases}t/2,&0\le t\le2a,\\ t-a,&2a\le t\le1.\end{cases}
\]
Because \(a\le1/4\), splitting the integral at \(2a\) and \(1-2a\) and integrating polynomials yields
\[
\int_0^1 q_a(t)^2q_a(1-t)^2\,dt
=\frac{72a^5-10a^4-60a^3+40a^2-10a+1}{30}.
\]
To realize the optimal joint law, sample \(U\sim\operatorname{Unif}[0,1]\), put \(S=F_a(|U-a|)\) with \(F_a(w)=2w\) for \(0\le w\le a\) and \(F_a(w)=w+a\) for \(a\le w\le1-a\). Then \(S\) is uniform. Put \(W'=q_a(1-S)\). If \(W'>a\), take \(V=a+W'\). If \(W'\le a\), take \(V=a+W'\) or \(a-W'\), each with probability \(1/2\), using an independent fair coin. The inverse-density calculation gives \(V\sim\operatorname{Unif}[0,1]\), and its absolute multiplier has the required countermonotone quantile. The optimizer's absolute-multiplier joint law is uniquely determined up to null sets, but the original stage coupling need not be unique.

**3. Exact global frontier.** For \(0<z\le4/3\), the independent-stage upper bound \(H_*(z)\le g(z)^2<1\) suffices: direct expansion gives
\[
g(z)-1=\frac{z}{3}(z^3-3z^2+6z-6),
\]
and the cubic is strictly increasing (its derivative is \(3((z-1)^2+1)\)) yet remains negative at \(z=4/3\). For \(z\ge4/3\), the quantile \(Q_z(t)\) is \(z^2t/2\) on \(t\le2a\), with derivative \(zt>0\), and \(z^2t-z+1\) above that cutoff, with derivative \(2zt-1\ge3-4/z\ge0\). The formulas match continuously across the moving cutoff. Hence for almost every \(t\in(0,1)\), \(Q_z(t)\) increases strictly with \(z\ge4/3\), and so does \(H_*(z)=\int Q_z(t)^2Q_z(1-t)^2dt\). Direct substitution yields \(H_*(2)=4/5<1\), while \(H_*(z)\to\infty\) as \(z\to\infty\). There is exactly one crossing of 1, beyond 2.

For \(z>1\), substituting \(a=(z-1)/z^2\) and clearing the positive denominator yields the exact equivalence
\[
H_*(z)-1=\frac{P(z)}{30z^2},\quad
P(z)=z^{10}-10z^9+50z^8-140z^7+210z^6-68z^5-360z^4+760z^3-760z^2+360z-72.
\]
Exact rational evaluation gives \(H_*(20563/10000)<1<H_*(20564/10000)\), and bisection gives the stated decimal. For independent stages \(H_{\rm iid}=g(z)^2\), so the strictly increasing cubic \(z^3-3z^2+6z-6\) gives the quoted unique positive threshold. At \(z=2\), \(c=1\), the antithetic raw-stage expression from step 2 gives \(23/15\), while \(g(2)^2=49/9\); the optimal second formula gives \(4/5\).

## Verification
A reproducible Python standard-library script `checker.py` checks the displayed rational identities, exact-root bracketing, nonnegative moment inequalities, the piecewise quantile formula, and independent midpoint-quadrature evaluations over rational grids. It uses exact `fractions.Fraction` arithmetic for algebraic claims and for 90 bisection stages; quadrature tests are finite cross-checks only. Its recorded execution is in `checker_output.txt`. The continuous-parameter optimality, inequality and uniqueness conclusions follow from the analytic rearrangement and monotonicity arguments above, not finite enumeration.

## Relationship to prior work
Bochacik, Goćwin, Morkisz and Przybyłowicz (2020), especially their construction and mean-square stability section, analyze the same randomized explicit two-stage RK map with **independent** uniform stage draws; their independent-stage scalar stability domain is recovered by \(g(z)<1\). Kruse and Wu (2017) analyze random-stage RK schemes and their approximation error with independent random stages. In contrast, the present statement optimizes **temporal dependence of two consecutive stages** while preserving each stage's exact uniform marginal and pairing epochs independently. The Fréchet–Hoeffding rearrangement inequality and countermonotone quantile construction used in the proof are classical; the claimed contribution is the explicit distribution-level optimum and sharp scalar test-equation stability frontier for this scheme. Deterministic stabilized two-step RK constructions are different methods and do not establish this coupling result.

## Limitations
The result is specific to the scalar constant-coefficient test problem, real negative axis, fixed step size, and adjacent two-stage copulas. The best coupling requires knowledge of \(z\) and may require an auxiliary fair coin; it is not necessarily beneficial for general systems, nonlinear ODEs, arbitrary longer-range couplings, or full-path strong/weak accuracy. The statement optimizes mean-square amplification across two-step blocks, not one-step errors, overall computational work or almost-sure stability. The general rearrangement principle is established mathematics; unidentified older applications to randomized integrators remain a precedence risk. No independent external validation is claimed.

## References
1. T. Bochacik, M. Goćwin, P. M. Morkisz and P. Przybyłowicz, *Randomized Runge–Kutta method—stability and convergence under inexact information*, arXiv:2006.12131v1 (first public June 22, 2020), https://arxiv.org/html/2006.12131v1.
2. R. Kruse and Y. Wu, *Error analysis of randomized Runge–Kutta methods for differential equations with time-irregular coefficients*, arXiv:1701.03444 (2017), https://arxiv.org/abs/1701.03444.
3. A. Moisa and B. Faleichik, *Second order stabilized two-step Runge–Kutta methods*, arXiv:2303.16267 (2023), https://arxiv.org/abs/2303.16267 (distinguished comparator, not a claimed prior exact coupling result).
4. Classical Fréchet–Hoeffding rearrangement/quantile coupling inequality for nonnegative random variables; standard probability result, invoked explicitly rather than claimed as novel.
