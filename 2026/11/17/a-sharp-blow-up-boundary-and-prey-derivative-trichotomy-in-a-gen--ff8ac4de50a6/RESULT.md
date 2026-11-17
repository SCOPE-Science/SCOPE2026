# A sharp blow-up boundary and prey-derivative trichotomy in a generalist predator flow

## Finding

Consider the undelayed group-defence predator–prey flow
\[
\dot x=Rx\left(1-\frac{x}{K}\right)-\frac{Mxy}{x^p+C},\qquad
\dot y=\left(D-\frac{E}{x+A}\right)y^2.
\]
For **every** choice of \(R,K,M,C,D,E,A>0\), every real \(p\geq1\), and every initial state \(x(0),y(0)>0\), the following sharp alternative holds.

1. If \(E\geq AD\), the solution exists for all \(t\geq0\), remains strictly positive, and both populations are uniformly bounded in time.
2. If \(E<AD\), the maximal positive solution has a finite terminal time \(T\), with \(x(t)\to0\) and \(y(t)\to+\infty\). Put \(\delta=D-E/A>0\) and \(\nu=M/(C\delta)>0\). There is a trajectory-dependent number \(c>0\) for which
\[
\lim_{t\uparrow T}(T-t)y(t)=\frac1\delta,
\quad\lim_{t\uparrow T}\frac{x(t)}{(T-t)^\nu}=c,
\quad\lim_{t\uparrow T}\frac{\dot x(t)}{(T-t)^{\nu-1}}=-\nu c.
\]
Consequently, a singular prey derivative \(\dot x(t)\to-\infty\) occurs **if and only if** \(0<\nu<1\). At \(\nu=1\), \(\dot x(t)\to-c\); at \(\nu>1\), \(\dot x(t)\to0\), despite predator blow-up in both cases. This is a classification of the undelayed ordinary differential equation only.

## Assumptions and scope

All seven coefficients are strictly positive, \(p\geq1\) is real, and both initial populations are strictly positive. Solutions are classical on their maximal forward existence interval. The claim is global over this full parameter and initial-data domain; no smallness, equilibrium stability, or invariant-simplex restriction is imposed. The conclusion about \(\dot x\) concerns its finite-time limit, not an assertion that the prey stays bounded away from zero.

The distinction \(E=AD\) is included in the global branch. Strict positivity persists for every time at which the solution exists, by the scalar multiplicative forms of both equations. Finite-time terminal behavior is not described for delayed or spatially extended variants.

## Proof

Write
\[
 f(x)=Rx(1-x/K),\quad q(x)=\frac{Mx}{x^p+C},\quad
 g(x)=D-\frac E{x+A},\quad g_+(x)=\max\{g(x),0\}.
\]
The equations become \(\dot x=f(x)-q(x)y\) and \(\dot y=g(x)y^2\). Prey comparison with logistic growth gives
\[
 0<x(t)\leq B:=\max\{x(0),K\}
\]
throughout the maximal existence interval. Boundedness of \(x\) rules out any finite-time singularity except possible unboundedness of \(y\).

**The global branch \(E\ge AD\).** Define
\[
 h(x)=2\int_0^x\frac{g_+(u)}{q(u)}\,du\qquad(0\leq x\leq B).
\]
This is finite and nonnegative. When \(E>AD\), \(g_+=0\) on a neighborhood of zero. At \(E=AD\),
\[
 \frac{g(x)}{q(x)}=\frac{D(x^p+C)}{M(x+A)},
\]
so the integrand extends continuously to zero with value \(DC/(MA)\). Thus \(h\) is continuous and bounded on \([0,B]\).

Set \(Y_*=2R(B^p+C)/M\). Whenever \(y\geq Y_*\),
\[
 q(x)y\geq2Rx,\qquad \dot x\leq-\frac12q(x)y.
\]
It follows, at all times with \(y\geq Y_*\), that
\[
 \frac d{dt}\{\log y+h(x)\}
 =g(x)y+\frac{2g_+(x)}{q(x)}\dot x
 \leq(g(x)-g_+(x))y\leq0.
\]
Apply this inequality to each excursion above \(Y_*\), starting either at \(t=0\) or at an upward threshold crossing. Since \(0\leq h(x)\leq h(B)\),
\[
 y(t)\leq \max\{y(0),Y_*\}\exp(h(B))
\]
for all times in the maximal interval. Both state variables therefore remain bounded, and the smooth vector field on the nonnegative quadrant extends the solution globally. In particular, equality \(E=AD\) does **not** cause finite-time blow-up.

**The blow-up branch \(E<AD\).** Set \(\delta=D-E/A>0\). For all \(x\geq0\),
\[
 \delta\leq g(x)<D.
\]
Thus \(\dot y\geq\delta y^2\), so the maximal lifetime is finite and \(T\leq1/(\delta y(0))\). The prey bound and the continuation alternative imply \(y(t)\to\infty\) as \(t\uparrow T\). The reciprocal identity gives
\[
 \frac1{y(t)}=\int_t^T g(x(s))\,ds\leq D(T-t),
\]
so \(y(t)\geq[D(T-t)]^{-1}\). Consequently
\[
 \frac{\dot x(t)}{x(t)}
 \leq R-\frac{M}{D(B^p+C)(T-t)}.
\]
On integration, for some \(c_0>0\) and \(\kappa=M/[D(B^p+C)]>0\),
\[
 0<x(t)\leq c_0(T-t)^\kappa
\]
near \(T\). In particular, \(x(t)\to0\).

Since
\[
 g(x)=\delta+\frac{Ex}{A(x+A)}=\delta+O(x),
\]
the reciprocal identity, the preceding power bound, and \(\tau=T-t\) yield
\[
 \frac1{y(t)}=\delta\tau+O(\tau^{1+\kappa}),\qquad
 y(t)=\frac1{\delta\tau}\bigl(1+O(\tau^\kappa)\bigr).
\]
Also, because \(p\geq1\),
\[
 \frac{M}{x(t)^p+C}=\frac{M}{C}+O(\tau^{p\kappa}).
\]
Together with the bounded logistic term, these imply
\[
 \frac{\dot x(t)}{x(t)}=-\frac\nu\tau+O(1+\tau^{\kappa-1}),
 \qquad\nu=\frac{M}{C\delta}.
\]
The error is integrable at \(T\). Since \(d(\log\tau)/dt=-1/\tau\), it follows that
\[
 \frac d{dt}\left(\log x(t)-\nu\log\tau\right)
 =O(1+\tau^{\kappa-1}).
\]
Therefore the bracket has a **finite real limit**, proving
\[
 c:=\lim_{t\uparrow T}\frac{x(t)}{\tau^\nu}\in(0,\infty).
\]
Finally, substitute the two leading asymptotics back into the prey equation to get \(\dot x(t)=-\nu c\tau^{\nu-1}(1+o(1))\). The claimed three-way derivative classification follows. This completes the proof.

## Verification

A reproducible standalone Python script, `checker.py`, uses exact fractions for 90 parameter/state checks across three polynomial response powers and both sides of the threshold. It verifies the compensating derivative inequality in the high-predator region, and the critical cancellation identity. Numerical diagnostics integrate in inverse-predator coordinates for \(\nu=1/2,1,2\), confirming the limiting rescaled prey amplitudes and the respective divergent, finite, and vanishing prey derivatives. These finite checks test the algebra and illustrate the theorem; the global and asymptotic statements are established by the proof above, not by extrapolating numerical experiments. Replay using `python checker.py` with Python, SciPy, and the standard library.

## Relationship to prior work

Patra, Kundu and Maitra introduced the model in a 2021 preprint and studied positivity, delay, stability, and a conditional boundedness criterion. Srivastava, Antwi-Fordjour and Parshad studied finite-time predator blow-up and simultaneous prey-derivative quenching in 2023; their preprint's Theorem 3 and figures concern large initial data and include examples with \(E>AD\). A separate 2024 paper by Patra, Maitra and Kundu explicitly derived the **sufficient** blow-up condition \(D>E/A\). This sufficient part is **not claimed as new** here. The additional results are the converse uniform bound for \(D\leq E/A\), the sharp global-versus-finite-time dichotomy, and the exact blow-up exponents and derivative trichotomy on the finite-time side. In particular the present theorem excludes genuine finite-time blow-up of the printed undelayed equation at the 2023 example parameters \(D=0.5,E=0.2,A=0.2\), since \(D<E/A\); it does not make a claim about the numerical integration procedure used in that publication.

## Limitations

No claim is made about time delays, diffusion, control terms, negative or zero initial states, singular limits \(C=0\) or \(A=0\), or finite-time continuation past the predator singularity. The time \(T\) and amplitude \(c\) depend on the trajectory and are not given by elementary closed formulas. The originality assessment is conditional on the inspected public sources and indexed records; unavailable or unindexed equivalent results may exist. There has been no independent mathematical audit.

## References

1. R. R. Patra, S. Kundu and S. Maitra, *Effect of delay and control on a predator-prey ecosystem with generalist predator and group defence in the prey species*, arXiv:2104.09166 (first posted 2021-04-19), https://arxiv.org/abs/2104.09166 .
2. V. Srivastava, K. Antwi-Fordjour and R. D. Parshad, *Exploring unique dynamics in a predator-prey model with generalist predator and group defence in prey*, arXiv:2306.13666 (first posted 2023-06-14), https://arxiv.org/abs/2306.13666 . Journal publication: *Chaos* 34, 013107 (2024), DOI:10.1063/5.0171950.
3. R. R. Patra, S. Maitra and S. Kundu, *Dynamics and blow-up control of a Leslie–Gower predator–prey model with group defence in prey*, *Journal of Biological Systems* 32 (2024), DOI:10.1142/S0218339024500165. Section 8.1 states the sufficient condition \(D>E/A\).
