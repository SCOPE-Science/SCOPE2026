# A sharp Jensen threshold for random-step third-order Runge–Kutta damping

## Finding

Write \(A=\begin{pmatrix}-a&-b\\b&-a\end{pmatrix}\), where \(a>0\) and \(b\geq0\), and let \(R_j(z)=\sum_{k=0}^{j}z^k/k!\) for \(j=1,2,3\). Put \(G_j(h)=\|R_j(hA)\|_2^2\) for nonnegative real step length \(h\). This is the exact squared Euclidean amplification, independent of the initial direction.

There is a sharp algebraic constant \(\omega_*=1.904257074337731\ldots\), defined below, such that:

1. For \(j=1,2\), for every \(a>0,b\geq0\), every integrable nonnegative random step \(H\) and \(\bar h=\mathbb EH\), one has \(\mathbb E G_j(H)\geq G_j(\bar h)\), with equality only when \(H=\bar h\) almost surely.
2. For \(j=3\), the same universal statement for **all** means \(\bar h\) and all admissible laws holds if and only if \(b/a\leq\omega_*\); equality is again restricted to deterministic laws. If \(b/a>\omega_*\), there is a nonempty open set of mean timesteps for which a two-point, equal-probability random law has strictly smaller expected squared amplification than the deterministic mean step.

For an exact witness, at \(a=1\), \(b=3\), \(\bar h=3/10\) and \(H\in\{1/5,2/5\}\) equiprobably, the deterministic-minus-randomized amplification equals \(401/36000>0\).

To define the threshold without floating-point approximation, set
\[
P(t)=\frac{t(5t^3-20t^2+48t-48)}6,\qquad
Q(t)=5t^5-10t^4-40t^3+144t^2-192t+96.
\]
Let \(t_*\) be the unique real root of \(Q(t)=0\) with \(t>2\), and define
\[
v_* = \frac{t_*^2-4}{P(t_*)},\qquad
\omega_* = \sqrt{\frac{1-v_*}{v_*}}.
\]
Numerically \(t_*=2.57584803206939\ldots\) and \(v_*=0.2161603648102745\ldots\).

## Assumptions and scope

The operator \(A\) is the specified **normal** real planar damped rotation. The step law is any Borel probability on \([0,\infty)\) with finite prescribed mean \(\bar h\), and expected amplification is allowed to equal \(+\infty\) (so no hidden bounded-support or finite-sixth-moment assumption is needed). The result compares a **single** RK update with a random actual duration to a deterministic update at the same **expected** duration. It concerns numerical energy damping, not physical-time error or accuracy for a fixed terminal time. The exact scalar stability polynomials apply to every explicit order-\(j\), \(j\)-stage RK method for \(j\leq3\).

## Proof

Identify the plane with \(\mathbb C\), so that \(A\) acts by multiplication with \(-a+ib\). Put \(r^2=a^2+b^2\). The squared amplification for degree three expands exactly as
\[
G_3(h)=1-2ah+2a^2h^2-\frac43a^3h^3
+\frac{r^2(8a^2-r^2)}{12}h^4
-\frac{ar^4}{6}h^5+\frac{r^6}{36}h^6.
\]
With \(v=a^2/r^2\in(0,1]\) and \(t=r^2h/a\), direct differentiation gives the key identity
\[
\frac{G_3''(h)}{a^2}=4-t^2+vP(t).
\]
For \(0\leq t\leq2\), this is the convex combination of \(4-t^2\geq0\) and \(4-t^2+P(t)\), because \(0<v\leq1\). The latter is strictly positive for all real \(t\): setting \(y=t-1\),
\[
6\bigl(4-t^2+P(t)\bigr)
=5y^4+12y^2-4y+3
=5y^4+12(y-1/6)^2+8/3>0.
\]
Consequently \(G_3''(h)>0\) for \(0\leq t\leq2\), for every \(a>0\).

For \(t>2\), \(P(t)>0\): its cubic factor is positive at \(2\) and has derivative \(15t^2-40t+48>0\) for all real \(t\). Hence \(G_3''\geq0\) at \(t>2\) exactly when
\[
v\geq F(t):=\frac{t^2-4}{P(t)}.
\]
The function \(F\) tends to zero at \(2^+\) and at infinity, and differentiating gives
\[
F'(t)=\frac{-12Q(t)}{t^2(5t^3-20t^2+48t-48)^2}.
\]
The shifted polynomial is
\[
Q(2+s)=5s^5+40s^4+80s^3+64s^2-16s-32.
\]
For \(s>0\) its coefficient sequence has exactly one sign change, hence Descartes' rule of signs permits at most one positive root, counted with multiplicity. Since \(Q(2)=-32<0\) and \(Q(3)=141>0\), it has exactly one, namely \(t_*\). Thus \(F\) rises strictly to \(v_*=F(t_*)\) and falls strictly thereafter; in particular \(0<v_*<1\).

Therefore \(G_3\) is convex on the whole nonnegative axis exactly when \(v\geq v_*\), equivalently \(b/a\leq\omega_*\). In that case the curvature is strictly positive except possibly at one isolated point at the threshold, so \(G_3\) is strictly convex. Jensen's inequality (including extended expectations) yields the claimed inequality and deterministic equality case. If \(v<v_*\), then \(G_3''(h)<0\) at \(h=at_*/r^2\), and in an open neighborhood. Taking two distinct, sufficiently close, symmetric positive steps around such a mean produces a strict reversed Jensen inequality. This proves both directions of the sharp classification.

For comparison, direct polynomial expansion gives
\[
G_1''(h)=2r^2>0,\qquad
G_2''(h)=a^2+3r^4\bigl(h-a/r^2\bigr)^2>0.
\]
Strict Jensen then proves the degree-one and degree-two assertions. Finally, substituting the rational witness values into the exact degree-three polynomial gives \(G_3(3/10)=2041/4000\) and \(\bigl(G_3(1/5)+G_3(2/5)\bigr)/2=2246/4500\), whose difference is \(401/36000\). All calculations are algebraic.

## Verification

Run \(\texttt{python3 verify.py}\) using Python 3 and the standard library. The verifier independently multiplies complex rational RK polynomials, checks the curvature identities for several rational parameters, the exact derivative and Descartes-shift identities, the explicit rational witness, and supplementary finite-grid inequalities at and above the threshold. It prints `VERIFICATION_OK`. The exact global arguments are the positivity identity and the one-positive-root proof above; numerical grids are corroboration, not proof.

## Relationship to prior work

Kruse and Wu (2017) study randomized RK evaluation of time-irregular vector fields and associated convergence errors, not changing the full third-order RK timestep according to an arbitrary fixed-mean law. Sun and Shu (2019) analyze and enforce strong stability of explicit RK schemes by deterministic superviscosity/filtering; their energy estimates do not provide the present probability-law Jensen threshold. Bochacik and collaborators (2020) investigate stochastic *stage coefficients* in a second-degree RK stability polynomial at a fixed timestep, not fixed-mean timestep randomization for the degree-three polynomial. A related published exact RK2 damping frontier treats deterministic single-step contraction for a distinct rank-one-damped oscillator matrix, rather than convex order of random timesteps for the normal scalar-damped rotation considered here. No implication from those inspected results to the statement here was identified.

## Limitations

This is not a theorem on global discretization error, stochastic convergence of random-time grids, or optimal laws at each individual mean in the nonconvex regime. A sufficiently large fixed mean may favor determinism even above the threshold. Random actual time differs among realizations, and lower expected numerical energy is not necessarily desirable accuracy. The result is for a normal planar generator; nonnormal dynamics and arbitrary higher-order stability polynomials are not covered. Publication priority remains subject to independent, more exhaustive historical-literature examination.

## References

1. R. Kruse and Y. Wu, *Error analysis of randomized Runge-Kutta methods for differential equations with time-irregular coefficients*, arXiv:1701.03444 (first public 2017-01-12), https://arxiv.org/abs/1701.03444.
2. Z. Sun and C.-W. Shu, *Enforcing strong stability of explicit Runge-Kutta methods with superviscosity*, arXiv:1912.11596 (first public 2019-12-25), https://arxiv.org/abs/1912.11596.
3. T. Bochacik, M. Goćwin, P. M. Morkisz and P. Przybyłowicz, *Randomized Runge–Kutta method—stability and convergence under inexact information*, arXiv:2006.12131 (first public 2020-06-22), https://arxiv.org/abs/2006.12131.
4. *A sharp energy-contraction frontier for explicit RK2 on damped oscillators*, public indexed finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-energy-contraction-frontier-for-explicit-rk2-on-damped-o--c4ff16d39c20.
