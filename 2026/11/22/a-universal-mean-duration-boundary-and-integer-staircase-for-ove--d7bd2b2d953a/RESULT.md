# A universal mean-duration boundary and integer staircase for overhead-limited recording windows

## Finding
Fix a circular monitoring horizon \(P>B>h>0\), an activation energy expressed in live-time equivalents \(h\), and event duration \(L\) of finite mean \(m\) with a strictly positive continuous density on \((0,\infty)\). An event has a uniform independent starting phase and is detected if and only if any positive portion of its presence intersects recording time. Each newly opened window costs \(h\) against an available live-time-equivalent budget \(B\). Define
\[
S(t)=\Pr(L>t),\qquad H(g)=\int_0^g S(u)\,du=\mathbb E\min\{L,g\},\qquad c=P-B>0.
\]
There are exactly \(N=\lceil B/h\rceil-1\) feasible positive window counts \(n=1,\ldots,N\). The sharp maximum single-event capture probability among all schedules with \(n\) windows is
\[
Q_n=\frac{B-nh+nH(h+c/n)}{P}.\tag{1}
\]
Every attaining schedule has exactly equal **silent gaps** \(h+c/n\). Equal lengths of active windows are sufficient but not necessary: any strictly positive allocation of total active length \(B-nh\) among \(n\) windows with those equal gaps attains (1).

**Universal single-window boundary.** If \(h\ge m\), one window is the uniquely optimal *window count* for every admissible budget and horizon. For every \(0<h<m\) and \(B>2h\), there are sufficiently long horizons for which two windows strictly outperform one. Thus the mean-event-duration boundary is exact.

**Integer staircase.** For \(0<h<m\), put \(c=P-B\). For each \(n=1,\ldots,N-1\) there is exactly one positive number \(c_n\) satisfying
\[
(n+1)H\left(h+\frac{c_n}{n+1}\right)-nH\left(h+\frac{c_n}{n}\right)=h.
\tag{2}
\]
These satisfy \(0<c_1<\cdots<c_{N-1}\). The unique maximizing count is \(1\) for \(0<c<c_1\), \(n\) for \(c_{n-1}<c<c_n\), and \(N\) for \(c>c_{N-1}\); at \(c=c_n\) exactly counts \(n,n+1\) tie (the other counts are inferior). If \(N=1\), the count \(1\) is necessarily optimal and there are no switching thresholds.

Define \(d_h>0\) as the unique solution of
\[
H(h+d_h)-d_h S(h+d_h)=h.\tag{3}
\]
The continuous relaxation has a unique optimal count \(x_*(c)=c/d_h\); the integer optimizer must be one of the feasible integers adjacent to this value, with the endpoints clipped to \([1,N]\). Furthermore
\[
nd_h<c_n<(n+1)d_h,\qquad\lim_{n\to\infty}\frac{c_n}{n+1/2}=d_h.
\tag{4}
\]
These thresholds depend on \(h\) and the event-duration law, but not on \(B\) apart from which counts are feasible.

## Assumptions and scope
A recording schedule consists of finitely many nonoverlapping positive-length active arcs on a circle of circumference \(P\). Each connected active arc incurs a fixed energy-equivalent overhead \(h\), which reduces *available live time* rather than imposing an actual temporal dead time; total energy used is active length plus \(nh\), not more than \(B\). Adjacent positive arcs without a silent gap are one activation, not two. The period \(P\) is longer than the entire budget \(B\). Event-start phases are uniform and durations independent of phase; durations need not be exponential, but their mean must be finite and their density strictly positive and continuous on \((0,\infty)\). Detection requires only strictly positive overlap, not an entire recognisable call or a minimum audible fraction. The result maximizes a random event's capture probability, not an estimator's precision, population abundance, true species-detection probability with changing call rate, or energetic costs of signal processing.

## Proof
**1. Exact gap functional and budget saturation.** With \(n\) active arcs of lengths \(a_i>0\) and following gaps \(g_i\ge0\), write \(A=\sum_i a_i\) and \(\sum_i g_i=P-A\). A uniform event start within active time is captured. For a start in a gap, capture occurs exactly when the event persists until the following active arc; integrating over the gap gives \(H(g_i)\). Consequently
\[
PQ=A+\sum_{i=1}^n H(g_i).\tag{5}
\]
If \(A<B-nh\), at least one silent gap is positive because \(P>B\); extending an adjacent active arc by \(\varepsilon>0\) decreases that gap and changes \(PQ\) by \(\varepsilon-\int_{g-\varepsilon}^g S(u)\,du=\int_{g-\varepsilon}^g[1-S(u)]\,du>0\), for sufficiently small \(\varepsilon\). Hence every optimum exhausts the budget: \(A=B-nh\). Feasibility of positive live time is precisely \(1\le n< B/h\), or \(1\le n\le\lceil B/h\rceil-1\).

**2. Unique equal gaps.** Since \(H'(g)=S(g)\) and \(H''(g)=-f(g)<0\) for positive \(g\), \(H\) is strictly concave on \([0,\infty)\). At fixed \(n\), the gaps sum to \(P-(B-nh)=c+nh\). Strict Jensen inequality makes \(\sum_i H(g_i)\) largest precisely when every gap equals \(h+c/n\). This proves (1) and the stated equality cases. The individual positive active lengths do not appear in (5) once their sum is fixed.

**3. Strictly concave real-count envelope.** Extend the numerator of (1) to every real \(x>0\):
\[
F_c(x)=B-hx+xH(h+c/x),\quad
F'_c(x)=-h+H(g)-(g-h)S(g),\quad
F''_c(x)=-\frac{c^2}{x^3}f(g)<0,\quad g=h+c/x.
\tag{6}
\]
For \(g>h\), set \(M_h(g)=H(g)-(g-h)S(g)\). Then
\[
M_h'(g)=(g-h)f(g)>0,\qquad M_h(h)=H(h)<h,
\qquad \lim_{g\to\infty}M_h(g)=m.
\tag{7}
\]
The last limit follows from \(H(g)\uparrow\mathbb E L=m\) and \(gS(g)\to0\), valid for nonnegative random durations of finite mean. If \(h\ge m\), (6)-(7) imply \(F'_c(x)<0\) for all \(x>0\). Therefore the unique feasible maximizing count is \(1\). If \(0<h<m\), the intermediate-value theorem and strict monotonicity give a unique \(g_h=h+d_h>h\) with \(M_h(g_h)=h\), proving (3). Equation (6) then has its sole stationary point at \(x=c/d_h\), and strict concavity makes it the unique global maximum on \((0,\infty)\).

**4. Every integer transition, once and in order.** For \(1\le n<N\), the numerator difference between counts \(n+1\) and \(n\) is
\[
\Delta_n(c)=-h+(n+1)H\left(h+\frac c{n+1}\right)-nH\left(h+\frac cn\right).
\tag{8}
\]
Direct differentiation gives
\[
\Delta_n'(c)=S\left(h+\frac c{n+1}\right)-S\left(h+\frac cn\right)>0.
\tag{9}
\]
Its limits are \(\lim_{c\downarrow0}\Delta_n(c)=H(h)-h<0\) and \(\lim_{c\to\infty}\Delta_n(c)=m-h\). When \(h<m\), the intermediate-value theorem gives exactly one zero \(c_n>0\). Strict concavity in (6) gives \(\Delta_{n+1}(c)<\Delta_n(c)\) for each fixed \(c>0\). Thus the zeros satisfy \(c_{n+1}>c_n\). The signs of consecutive differences classify every maximizing integer count and show that only adjacent counts tie at a boundary. At a zero \(c=c_n\), the mean-value theorem applied to \(F_c\) on \([n,n+1]\) finds some \(\xi\in(n,n+1)\) with \(F'_c(\xi)=0\). Hence \(\xi=c_n/d_h\), proving the strict bracket in (4) and its asymptotic consequence. For \(h<m\), \(\Delta_1(c)\to m-h>0\) as \(c\to\infty\), establishing sharpness provided two windows are feasible.

## Verification
The included standalone standard-library `verify.py` checks the explicit formula, positive curvature gap, ordered transition roots and their analytic brackets, the boundary \(h=m\), the gamma-distributed event-duration extension, the constrained real-count candidate rule, and equal-gap optimality against unequal gaps. Running `python verify.py` produces `CHECKS_PASSED 67326`. These are finite arithmetic and random stress tests, not substitutes for the preceding proof.

For \(L\sim\mathrm{Exp}(1)\), \(P=12\), \(B=8\), and \(h=1/2\), one optimal schedule has five equal active windows of length \(1.1\) interleaved with five equal gaps of length \(1.3\). Its capture probability is \(Q_5=0.7614450862358281\ldots\), whereas \(Q_1=0.7074075836218131\ldots\). Among the feasible counts \(1\le n\le15\), \(n=5\) uniquely maximizes (1). For \(h\ge1\), the same duration law universally prefers a single activation whenever feasible.

## Relationship to prior work
Michel, Torterotot, Royer and Samaran (2024) empirically assess passive acoustic sampling duty cycles and listening-window lengths, motivating a precise energy-limited idealization; their actual call-detection algorithm requires a *whole* call, unlike the partial-overlap objective here. Yau, Yip, Ma, Rao and Shankar (2010), especially Theorems 4.2 and 5.2, already derive the fundamental survival-integral formula for capture under periodic event surveillance, and discuss travel overhead and optimization across multiple monitoring locations. That capture identity is **not claimed as new**. The result established here addresses the distinct all-count optimization under a single recorder's per-activation energy cost, giving the distribution-universal boundary \(h=m\), unique ordered integer switches, and bounded switch locations, none of which is asserted in the inspected prior theorems. Teixeira and colleagues (2024) survey relevant ecological monitoring practicalities. General sensor scheduling and renewal optimization may contain stronger statements; historical priority remains provisional.

## Limitations
The fixed overhead is modeled as additive energy-equivalent budget consumption; real wake-up latency may also block portions of time. The mathematical detector triggers on any positive overlap, while some bioacoustic recognition systems require a complete signal. Uniform event timing, phase independence, independent durations, no changing acoustic intensity, negligible false positives, and a cyclic idealization may not describe field data. Counts of captured events and detection of at least one random bout are not equivalent to accurate call-rate estimation or biodiversity inference. Only the specified model and hypotheses are proved. A full historical literature search outside the inspected sources was not possible; the 2010 survival formula implies the elementary building block but not an explicit solution to this added activation-budget problem.

## References
- Michel, M., Torterotot, M., Royer, J.-Y., and Samaran, F. (2024). *Effects of duty cycle on passive acoustic monitoring metrics: The case of blue whale songs*. Journal of the Acoustical Society of America 155, 2538–2548. First public online: 2024-04-09. https://doi.org/10.1121/10.0025545 ; full text https://archimer.ifremer.fr/doc/00886/99790/109885.pdf
- Yau, D. K. Y., Yip, N. K., Ma, J., Rao, N. S. V., and Shankar, M. (2010). *Quality of Monitoring of Stochastic Events by Periodic and Proportional-Share Scheduling of Sensor Coverage*. ACM Transactions on Sensor Networks 7(2), Article 18. https://doi.org/10.1145/1824766.1824774 ; lawful full text https://www.math.purdue.edu/~yipn/papers/qomTOSN2010.pdf
- Teixeira, D. et al. (2024). *Effective ecological monitoring using passive acoustic sensors*. Conservation Science and Practice. https://doi.org/10.1111/csp2.13132
