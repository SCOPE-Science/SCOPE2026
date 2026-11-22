# Sharp strict-positivity frontier and vacuum-touchdown laws for power-entropy advection fluxes

## Finding

For the entire one-parameter family of two-point entropy-conservative means for positive scalar advection, **global strict positivity on every periodic mesh and for every positive initial vector holds exactly for entropy exponent \(p\leq 0\)**. For every \(p>0\), a strictly positive initial vector on **three** periodic cells reaches the boundary in finite forward time. With one initially small component \(\varepsilon\), the three sharp first-touchdown time scales are \(\varepsilon^p\) for \(0<p<1\), \(\varepsilon\log(1/\varepsilon)\) for \(p=1\), and \(\varepsilon\) for \(p>1\); their constants are given below. This separates boundary invariance from strict interior invariance, even for entropy-conservative semidiscretizations.

## Assumptions and scope

Fix \(p\in\mathbb R\), a periodic mesh of \(N\geq3\) cells of width \(h>0\), and an initial vector \(u(0)\in(0,\infty)^N\). All indices are periodic. Define the symmetric, positive, consistent two-point flux, for \(a,b>0\), by

\[
F_p(a,b)=\frac{\int_a^b t^{p-1}\,dt}{\int_a^b t^{p-2}\,dt},\qquad F_p(a,a)=a.
\]

For \(a\neq b\), the expression is \(\frac{p-1}{p}\frac{b^p-a^p}{b^{p-1}-a^{p-1}}\) when \(p\notin\{0,1\}\), and has the continuous limiting formulas

\[
F_0(a,b)=\frac{ab\log(b/a)}{b-a},\qquad
F_1(a,b)=\frac{b-a}{\log(b/a)}.
\]

It is a weighted average between its arguments. Use the positive-state semidiscrete initial-value problem

\[
\dot u_i=\frac{F_p(u_i,u_{i+1})-F_p(u_{i-1},u_i)}h.\tag{1}
\]

This is the entropy-conservative two-point flux of the scalar conservation law \(u_t+u_x=0\) associated with the strictly convex entropy

\[
U_p(u)=\begin{cases}u^p/[p(p-1)],&p\notin\{0,1\},\\-\log u,&p=0,\\u\log u-u,&p=1.\end{cases}
\]

Affine differences in entropy normalization have no effect. In all cases \(U_p''(u)=u^{p-2}>0\). The assertion concerns only the unique maximal solution while all components are strictly positive; no unique continuation after a boundary touchdown is presumed.

**Theorem (sharp global frontier and small-data touchdown laws).** The following statements hold.

1. If \(p\leq0\), every positive initial state admits a unique solution that stays strictly positive for all \(t\geq0\). Writing \(M=\sum_i u_i(0)\), for \(p<0\) every component obeys \(u_i(t)\geq(\sum_j u_j(0)^p)^{1/p}>0\). For \(p=0\), every component obeys \(u_i(t)\geq\prod_j u_j(0)/M^{N-1}>0\).
2. Fix any \(p>0\) and \(0<a<b\). For all sufficiently small \(\varepsilon>0\), the three-cell positive state \((\varepsilon,a,b)\) has a unique solution until a first finite boundary time \(T_\varepsilon\), where its **first component** reaches zero while the other two stay positive. As \(\varepsilon\downarrow0\),

\[
T_\varepsilon\sim\begin{cases}
\displaystyle\frac{h\varepsilon^p}{(1-p)(b^p-a^p)},&0<p<1,\\[5pt]
\displaystyle\frac{h\varepsilon\log(1/\varepsilon)}{b-a},&p=1,\\[5pt]
\displaystyle\frac{hp\varepsilon}{(p-1)(b-a)},&p>1.
\end{cases}\tag{2}
\]

The entire exponent range is sharp. For \(0<p\leq1\), \(F_p(0,b)=0\) by continuous extension, so loss of *strict* positivity is compatible with a nonnegative (boundary-invariant) flux. For \(p>1\), \(F_p(0,b)=(p-1)b/p\), and even nonnegative boundary invariance can fail.

**Geometric-mean illustration (not a separate novelty claim).** At \(p=1/2\), the established geometric flux \(F_{1/2}(a,b)=\sqrt{ab}\) gives \(x_i=\sqrt{u_i}\) and the exact linear equation \(\dot x_i=(x_{i+1}-x_{i-1})/(2h)\). For three cells put \(m=(x_1+x_2+x_3)/3\) and \(R=[(2/3)\sum_i(x_i-m)^2]^{1/2}\). The positive orbit stays strictly positive for all forward time if and only if \(m>R\), equivalently \((\sum_i\sqrt{u_i(0)})^2>2\sum_i u_i(0)\). At equality a component touches zero tangentially. For \(x(0)=(1/10,1,2)\), \(h=1\), first touchdown occurs exactly at

\[
T=\frac4{\sqrt3}\arctan\!\left(\frac{10\sqrt3-\sqrt{123}}{59}\right)
=0.24295568190109698\ldots.
\]

The square-root linearization is already a known representation of geometric entropy fluxes and is used here solely as an exact witness.

## Proof

**Entropy conservation.** Write \(w_p=U_p'\) and \(\psi_p=uU_p'-U_p\). Then \(w_p'=u^{p-2}\), \(\psi_p'=uw_p'=u^{p-1}\), so the definition gives

\[
F_p(a,b)[w_p(b)-w_p(a)]=\psi_p(b)-\psi_p(a).\tag{3}
\]

The flux is symmetric. Summing equation (1) gives the conserved mass \(\sum_i u_i=M\). For the entropy, by periodic index shifting,

\[
\frac{d}{dt}\sum_i U_p(u_i)
=\frac1h\sum_i\big(w_p(u_i)-w_p(u_{i+1})\big)F_p(u_i,u_{i+1})
=\frac1h\sum_i[\psi_p(u_i)-\psi_p(u_{i+1})]=0.
\]

For \(p<0\), this fixes \(S=\sum_i u_i^p>0\). Since each term is nonnegative, \(u_i^p\leq S\), hence \(u_i\geq S^{1/p}\). For \(p=0\), it fixes \(P=\prod_i u_i>0\); mass positivity implies \(u_j\leq M\), hence \(u_i\geq P/M^{N-1}\). The orbit remains in a compact subset of the strictly positive orthant. The smooth interior vector field then extends its unique solution indefinitely. This proves part 1.

**Boundary scaling.** For \(p>0\), fix \(0<a<b\), with \(x=u_1\), \(y=u_2\), and \(z=u_3\). While \((y,z)\) lies in a fixed small neighborhood of \((a,b)\), the first equation is

\[
h\dot x=F_p(x,y)-F_p(x,z).
\]

Elementary expansion of the explicit means, uniformly for \(y,z\) in compact positive intervals, yields

\[
h\dot x=\begin{cases}
-\dfrac{1-p}{p}(z^p-y^p)x^{1-p}[1+o(1)],&0<p<1,\\[5pt]
-\dfrac{z-y}{\log(1/x)}[1+o(1)],&p=1,\\[5pt]
-\dfrac{p-1}{p}(z-y)+o(1),&p>1,
\end{cases}\tag{4}
\]

as \(x\downarrow0\), with \(o(1)\) uniform in those compact intervals. In particular, \(\dot x<0\) for sufficiently small positive \(x\). Set the vanishing state variable \(W_p(x)=x^p\) when \(0<p<1\), \(W_1(x)=x\log(1/x)\) for small \(x\), and \(W_p(x)=x\) when \(p>1\). Then, along any orbit with \(x\downarrow0\) and \((y,z)\to(a,b)\),

\[
\dot W_p(x)\longrightarrow -K_p,
\quad K_p=\begin{cases}
(1-p)(b^p-a^p)/h,&0<p<1,\\
(b-a)/h,&p=1,\\
(p-1)(b-a)/(ph),&p>1.
\end{cases}\tag{5}
\]

By the weighted-mean property, all fluxes are between their arguments. Hence on the positive interval \(0<u_i\leq M=a+b+\varepsilon\), every coordinate speed is at most \(M/h\) in magnitude. Choose a fixed neighborhood of \((a,b)\) for which \(z>y>0\). The negative limits in (5), uniformly on that neighborhood, imply that for sufficiently small \(\varepsilon\), the decreasing variable \(W_p(x)\) reaches zero in time at most \(2W_p(\varepsilon)/K_p\). This time tends to zero, so the bounded speeds prevent either neighbor from leaving the neighborhood before touchdown. Thus the solution's first loss of strict positivity is exactly \(x=0\), and \(y,z\to(a,b)\) uniformly over its lifetime. Integrating (5) between \(0\) and \(T_\varepsilon\) yields \(T_\varepsilon\sim W_p(\varepsilon)/K_p\), proving (2). No local uniqueness assertion at the boundary is used.

**Geometric example.** On positive coordinates, \(\dot u_i=(\sqrt{u_i u_{i+1}}-\sqrt{u_{i-1}u_i})/h\) implies \(\dot x_i=(x_{i+1}-x_{i-1})/(2h)\). Its three-state skew matrix has eigenvalues \(0,\pm i\sqrt3/(2h)\), conserves \(\sum x_i\) and \(\sum x_i^2\), and gives

\[
x_i(t)=m+(x_i(0)-m)\cos(\omega t)+\frac{x_{i+1}(0)-x_{i-1}(0)}{\sqrt3}\sin(\omega t),\quad\omega=\frac{\sqrt3}{2h}.
\]

Each coordinate has harmonic amplitude \(R\), so strict positivity holds for all time exactly when \(m>R\). At equality the minimum reaches zero, and below equality it crosses zero during a period. For \((1/10,1,2)\), the first coordinate's zero equation, with \(q=\tan(\omega t/2)\), is \(59q^2-20\sqrt3q+3=0\). Its smaller positive root gives the displayed first-touchdown time, and the other two components remain positive there. This completes the proof.

## Verification

The standalone \(\texttt{verify.py}\) is self-contained and uses only Python's standard library. Running \(\texttt{python verify.py}\) produced **PASS: 4387 finite diagnostics**, including exact-rational entropy identities for integer power parameters, strict weighted-mean tests, geometric-mean evaluations, three-site trigonometric differential identities, exact touchdown-root checks, and small-state leading-order checks. These are independent finite checks of the displayed formulas; the statements for arbitrary real \(p\), arbitrary \(N\), and the asymptotic limits are proved analytically above and are not inferred from testing.

## Relationship to prior work

The two-point entropy-conservative flux identity, log/geometric/harmonic examples, and periodic conservative advection model appear in Izgin–Ranocha–Shu, *A Positivity-Preserving Relaxation Algorithm*, arXiv:2604.02308 (2026), especially equations (49)–(56). The present theorem **does not claim novelty for Tadmor's flux, its means, entropy conservation, or the square-root conjugacy**. Bercik–Zingg, *On the Practical Impact of Local Linear Instabilities in Entropy-Stable Schemes*, arXiv:2605.02081 (2026), already analyze geometric and logarithmic entropy fluxes for linear advection and their near-vacuum characteristics. The assessed contribution is the global necessary-and-sufficient **strict interior positivity threshold** over the full real power-entropy family, together with the sharp three-regime first-boundary-time laws (2). The published discussion of nonnegative invariance is not an assertion of never reaching zero in finite time. Related upwind fully discrete entropy-flux envelopes and Patankar positivity corrections concern different algorithms and do not imply (2).

## Limitations

The family is a one-dimensional scalar, periodic, **semidiscrete** finite-volume model with strictly positive starting data. It is not a theorem for fully discrete relaxation methods, Runge–Kutta time integration, discontinuous Galerkin schemes, spatially variable advection, nonlinear physical fluxes, or systems. For \(p>0\) the constructed solution is asserted only up to its first zero; no particular extension beyond it is canonical. The geometric example exploits a previously known transformation and is not treated as an independent discovery. A relevant 2026 Bercik–Zingg full text could not be accessed for paragraph-by-paragraph comparison; overlapping unindexed formulations remain a residual priority risk requiring independent scholarly assessment.

## References

1. T. Izgin, H. Ranocha, C.-W. Shu, *A Positivity-Preserving Relaxation Algorithm*, arXiv:2604.02308v1, publicly posted 2026-04-02, https://arxiv.org/abs/2604.02308 (full text, equations 49–56 inspected).
2. A. Bercik, D. W. Zingg, *On the Practical Impact of Local Linear Instabilities in Entropy-Stable Schemes*, arXiv:2605.02081, publicly posted 2026-05-03, https://arxiv.org/abs/2605.02081 (abstract and accessible detailed secondary discussion; full text unavailable).
3. E. Tadmor, *Entropy stability theory for difference approximations of nonlinear conservation laws and related time-dependent problems*, Acta Numerica 12 (2003), https://doi.org/10.1017/S0962492902000156 (background general entropy-conservative flux framework).
