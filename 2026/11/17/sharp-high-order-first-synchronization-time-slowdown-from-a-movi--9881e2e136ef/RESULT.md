# Sharp high-order first-synchronization-time slowdown from a moving target

## Finding

For the higher-order Ott–Antonsen amplitude equation, positive high-order coupling eventually **delays** entry into a fixed-radius neighborhood of its *own* attracting steady state, even though it **accelerates** crossing of every fixed lower target. The two effects have different sharp exponential rates as interaction order grows.

Under the hypotheses below, as the integer \(d\to\infty\),
\[
\tau_d-\tau_0\sim C\,s^{d-1},\qquad C=\frac{H(1-s)(1-\delta/\sqrt{s})}{P^2 t(s-t)}>0,
\]
whereas at a fixed target,
\[
T_0(t)-T_d(t)\sim D\frac{t^{d-1}}{d-1},\qquad D=\frac{H(1-t)}{P^2(s-t)^2}>0.
\]
Consequently \(\tau_d>\tau_0\) for all sufficiently large interaction orders, while \(T_d(t)<T_0(t)\) for **every** integer order \(d\ge2\).

## Assumptions and scope

Choose fixed real parameters \(P>2\Delta>0\), \(0<H<P\), \(\delta>0\), and \(r_0>0\), and write
\[
s=1-\frac{2\Delta}{P},\quad u_0=r_0^2,\quad t=(\sqrt s-\delta)^2.
\]
Assume \(r_0<\sqrt s-\delta\). Hence \(0<u_0<t<s<1\). For each integer \(d\ge2\), consider
\[
\dot u=F_d(u)=P u(s-u)+H u^d(1-u),\qquad u(0)=u_0.
\]
The pairwise equation has \(F_0(u)=Pu(s-u)\) and equilibrium \(s\). Let \(u_d\in(s,1)\) denote the unique positive attracting equilibrium of the higher-order equation. The moving first-arrival level is \(t_d=(\sqrt{u_d}-\delta)^2\), and the corresponding times are
\[
\tau_d=\int_{u_0}^{t_d}\frac{du}{F_d(u)},\qquad
\tau_0=\int_{u_0}^{t}\frac{du}{F_0(u)},\qquad
T_d(t)=\int_{u_0}^{t}\frac{du}{F_d(u)}.
\]
All parameters except \(d\) are held fixed. The equation comes from the continuum-limit Ott–Antonsen reduction, with \(P=\epsilon_1\), \(H=\epsilon_d\). The result is conditional on that reduced equation, and makes no claim about finite-population stochastic fluctuations.

## Proof

**1. Unique steady state and exponential displacement.** Write \(F_d(u)=u g_d(u)\), where \(g_d(u)=P(s-u)+H u^{d-1}(1-u)\). For \(0<u<1\),
\[
g_d'(u)=-P+H\left[(d-1)u^{d-2}(1-u)-u^{d-1}\right]<0.
\]
Indeed, \((d-1)u^{d-2}(1-u)\le1\) for all integers \(d\ge2\) (for \(d=2\) this is immediate; for larger \(d\), maximize the product on \([0,1]\)). The strict inequality follows from \(H<P\). Since \(g_d(s)>0\), \(g_d(1)<0\), exactly one zero \(u_d\in(s,1)\) exists. Its sign change makes it attracting, and the trajectory from \(u_0\) increases monotonically to it.

The equilibrium identity is
\[
P(u_d-s)=H u_d^{d-1}(1-u_d).
\]
The maximum of \(u^{d-1}(1-u)\) on \([0,1]\) is no more than \(1/d\), so \(0<u_d-s\le H/(Pd)\). Fix any \(q\in(s,1)\). Eventually \(u_d<q\), and the same equation gives \(u_d-s\le(H/P)q^{d-1}\). Thus \(d(u_d-s)\to0\), and hence \((u_d/s)^{d-1}\to1\). Dividing the equilibrium identity by \(s^{d-1}\) proves
\[
\frac{u_d-s}{s^{d-1}}\longrightarrow\frac HP(1-s).
\]

**2. Motion of the first-arrival threshold.** Since \(t_d=(\sqrt{u_d}-\delta)^2\) and \(0<\delta<\sqrt s\), Taylor's theorem at \(s\) gives
\[
\frac{t_d-t}{s^{d-1}}\longrightarrow
\left(1-\frac\delta{\sqrt s}\right)\frac HP(1-s).
\]
In particular \(t_d>t>u_0\) for all \(d\), and \(t_d\to t<s\).

**3. Fixed-target acceleration.** For \(u\in[u_0,t]\), the difference of the reciprocal velocities is exactly
\[
\frac1{F_0(u)}-\frac1{F_d(u)}=
\frac{H u^{d-2}(1-u)}{P(s-u)[P(s-u)+H u^{d-1}(1-u)]}>0.
\]
It follows immediately that \(T_d(t)<T_0(t)\) for every \(d\ge2\). Since \(t<s\), the denominator converges uniformly to \(P^2(s-u)^2\) on \([u_0,t]\). The standard endpoint integral identity, valid for continuous \(a\) with \(a(t)>0\),
\[
\int_{u_0}^t u^{d-2}a(u)\,du\sim a(t)\frac{t^{d-1}}{d-1},
\]
then yields
\[
T_0(t)-T_d(t)\sim\frac{H(1-t)}{P^2(s-t)^2}\frac{t^{d-1}}{d-1}.
\]
For clarity, the endpoint identity follows by substituting \(u=tv\), splitting the resulting integral at any \(v=1-\eta\), and using continuity on the remaining short interval; no finite-order numerical observation is used.

**4. Dominance of the moving threshold.** Decompose exactly
\[
\tau_d-\tau_0
=\int_t^{t_d}\frac{du}{F_d(u)}-
\left(T_0(t)-T_d(t)\right).
\]
Because \(t_d\to t<s\), the reciprocal velocities converge uniformly to \(1/F_0(t)\) throughout the shrinking interval \([t,t_d]\). Thus
\[
\int_t^{t_d}\frac{du}{F_d(u)}\sim\frac{t_d-t}{P t(s-t)}.
\]
The fixed-target term has order \(t^{d-1}/d=o(s^{d-1})\). Inserting Step 2 establishes the claimed positive coefficient \(C\). This also proves the stated eventual sign, not merely numerical agreement.

## Verification

Run `python3 verify_fst.py` from the directory containing this document. The checker uses only the Python standard library, solves the positive-equilibrium equation by bisection, and evaluates the nonsingular *difference* of reciprocal travel-time integrands by adaptive Simpson quadrature. It tests three parameter configurations and eight distinct interaction orders, checking both asymptotic normalizations and the opposite fixed-target versus moving-target effects. The expected final line begins with `VERIFY_OK`. Numerical checks sample finitely many parameter values; the proof above, not the checker, covers all admissible real parameters and all sufficiently large integer orders.

## Relationship to prior work

Biswas, Patra and Banerjee derive this reduced amplitude equation and its first-synchronization-time quadrature, demonstrate numerically that increasing interaction order can retard a steady-state-referenced arrival, and observe convergence to pairwise behavior at very large order. Their discussion does not give the sharp signed large-order asymptotic coefficient or distinguish its scale from a fixed-target comparison. The present theorem obtains those two asymptotics from the moving equilibrium and endpoint integral, without claiming novelty for the reduction or the numerical observation. Sinha and Ghosh study synchronization-time statistics in the pairwise Kuramoto model; their distributional setting does not provide this higher-order moving-threshold law.

## Limitations

This theorem is about deterministic travel times of the continuum-limit reduced amplitude equation, not finite-size Kuramoto realization times, stochastic first-passage distributions, or arbitrary interaction strengths. It assumes \(0<H<P\) to ensure a unique positive steady state, fixes a positive \(r_0\) and a positive \(\delta\), and takes \(d\to\infty\) with those parameters unchanged. It does not claim that every finite interaction order yields a slowdown. The explicit coefficient becomes singular in a separate vanishing-\(\delta\) limit; uniform double-scaling behavior is not established.

## References

- D. Biswas, P. Patra and A. Banerjee, *On the role of higher-order interactions towards first synchronization time*, first public 2026-04-09, arXiv:2604.07707, https://arxiv.org/html/2604.07707v2 ; published in *Chaos* 36, 071102 (2026), https://doi.org/10.1063/5.0337306.
- A. Sinha and A. Ghosh, *Statistics of synchronization times in Kuramoto oscillators*, *Europhysics Letters* 141 (2023), 53001, https://doi.org/10.1209/0295-5075/acbdba.
