# A sharp fixed-mean renewal-clock transition for random-acceleration level crossings

## Finding
For an undamped randomly accelerated particle reset simultaneously to position and velocity zero at independent positive renewal intervals, a fixed mean reset interval has a **sharp and complete** effect on the maximum achievable long-run crossing frequency of any nonzero level. At short prescribed mean intervals, the optimal crossing flux is a nonattained, finite constant approached by increasingly bursty two-point reset clocks; at long mean intervals, **the unique optimizer is periodic resetting**. The transition has one universal scale and a uniquely determined dimensionless constant.

Fix \(k>0\) and target \(u\ne0\), and write \(\tau=(|u|/k)^{2/3}\). Define for \(s>0\)
\[
 z(s)=\frac3{\sqrt2\,s^{3/2}},\qquad
 g(s)=\frac{\sqrt3}{2\pi s}e^{-z(s)^2/3}\left(e^{-z(s)^2}+\sqrt\pi\,z(s)\operatorname{erf}z(s)\right),\qquad
 H(s)=\int_0^s g(w)\,dw.
\]
There is a **unique** \(a>0\) satisfying \(a g(a)=H(a)\); numerically \(a=2.317884873319\ldots\) and \(g(a)=0.141393298605\ldots\). Every strictly positive, finite-mean iid resetting clock \(T\), independent of the driving Brownian motions, gives the almost-sure long-run total *continuous* level-crossing frequency
\[
 J(T)=\frac{\mathbb E H(T/\tau)}{\mathbb ET/\tau}\,\frac1\tau.
\]
For a prescribed mean \(m=\mathbb ET\in(0,\infty)\), the exact supremum across **all** such renewal clocks is
\[
 \boxed{\sup_{\mathbb ET=m}\,J(T)=\frac1\tau
 \begin{cases}g(a),&0<m\le a\tau,\\[2pt]
 H(m/\tau)/(m/\tau),&m\ge a\tau.\end{cases}}
\]
For \(m\ge a\tau\), the unique maximizer is the deterministic clock \(T=m\) almost surely. For \(0<m<a\tau\), no strictly positive clock attains the supremum; it is approached by the two-point clocks on \(\{\varepsilon,a\tau\}\), where \(\varepsilon\downarrow0\) and the weights give mean \(m\). A maximal interval cap or nonzero reset overhead changes that limiting idealization.

The globally maximal renewal-clock crossing frequency \(0.141393298605\ldots/\tau\) exceeds the best completely Poisson-reset frequency \(0.104670262107\ldots/\tau\) by approximately \(35.0845\%\), although at a *fixed* mean \(m\) the best Poisson protocol is not necessarily the same one as the globally optimized Poisson protocol.

## Assumptions and scope
Each cycle starts from \((X_0,V_0)=(0,0)\) and evolves according to \(dV_t=k\,dW_t\), \(dX_t=V_t\,dt\) with standard Brownian motion \(W_t\). Reset intervals \(T_i\) are iid, satisfy \(\Pr(T_i>0)=1\) and \(\mathbb E T_i=m\in(0,\infty)\), and are independent of all excursion noises. At reset times *both* \(X\) and \(V\) jump instantaneously to zero, with fresh independent noise for the next cycle. A crossing of the fixed level \(u\ne0\) is counted only when it occurs **continuously during an excursion**; reset jumps across the level are excluded. Both upward and downward crossings count. There is no constraint on the clock beyond strict positivity and fixed finite mean, and there is no physical reset overhead. The objective is a long-run rate per unit physical time, not the mean first-passage time, a stationary density or a phase-resolved deterministic-clock statistic.

## Proof
**1. Reconstruct the free crossing kernel.** Since \(V_t=kW_t\) and \(X_t=k\int_0^t W_s\,ds\), the joint centered Gaussian vector has
\[
\operatorname{Var}X_t=\frac{k^2t^3}3,\qquad
\operatorname{Cov}(X_t,V_t)=\frac{k^2t^2}2,\qquad
\operatorname{Var}V_t=k^2t.
\]
Conditionally on \(X_t=u\), the velocity is normal with mean \(3u/(2t)\) and variance \(k^2t/4\). Hence its absolute expectation, multiplied by the Gaussian density of \(X_t\) at \(u\), gives the Kac--Rice crossing intensity \(h_u(t)=g(t/\tau)/\tau\). Explicitly the standard Gaussian identity \(\mathbb E|N(\mu,\sigma^2)|=\sigma\sqrt{2/\pi}e^{-\mu^2/(2\sigma^2)}+|\mu|\operatorname{erf}(|\mu|/(\sqrt2\sigma))\) gives exactly \(g\) above. This also verifies all normalization constants without relying on a potentially different noise-intensity convention. The intensity is bounded, tends to zero at \(t\downarrow0\), and is \(\sqrt3/(2\pi t)+o(t^{-1})\) as \(t\to\infty\).

**2. Prove that the free crossing kernel has one and only one peak.** Put \(A(z)=e^{-z^2}+\sqrt\pi\,z\operatorname{erf}z\) and \(R(z)=e^{-z^2}/A(z)\). Differentiation gives \(A'(z)=\sqrt\pi\operatorname{erf}z\), hence
\[
 R'(z)=-R(z)\left(2z+\frac{1-R(z)}z\right)<0,\quad
 -2\frac{d\log g(s)}{d\log s}=D(z(s)),\quad D(z)=5-2z^2-3R(z).
\]
For \(0<z\le1\), \(D(z)>5-2-3=0\). Since \(\sqrt\pi\operatorname{erf}(1)=2\int_0^1e^{-q^2}dq>2/e\), one has \(R(1)<1/3\); strict decrease of \(R\) yields \(R(z)<1/3\) for all \(z\ge1\). Thus, for \(z\ge1\),
\[
D'(z)=-4z+3R(z)\left(2z+\frac{1-R(z)}z\right)
<-2z+\frac1z<0.
\]
For \(z\ge\sqrt{5/2}\), \(D(z)<0\). Hence \(D\) has exactly one zero (between \(1\) and \(\sqrt{5/2}\)), and since \(z(s)\) decreases with \(s\), the function \(g(s)\) strictly increases up to a single peak \(s_0\), then strictly decreases. Numerically \(s_0\approx1.224035815762\); the proof of uniqueness is analytic.

**3. Establish a unique tangent from the origin.** Define \(Q(s)=s g(s)-H(s)\), extended continuously by \(Q(0)=0\). Direct differentiation gives \(Q'(s)=s g'(s)\). Thus \(Q\) first strictly rises to a positive value on \((0,s_0)\), then strictly decreases on \((s_0,\infty)\). As \(s\to\infty\), \(g(s)\sim c/s\) with \(c=\sqrt3/(2\pi)\) and \(H(s)\sim c\log s\), so \(Q(s)\to-\infty\). There is exactly one zero \(a>s_0\). It is the unique maximizer of \(H(s)/s\), since the derivative of this ratio is \(Q(s)/s^2\).

**4. Regenerative crossing-frequency identity.** Let \(N_i\) count continuous crossings during cycle \(i\). The Kac--Rice formula and Tonelli yield \(\mathbb E[N_i\mid T_i=t]=\int_0^t h_u(s)ds=H(t/\tau)\). Because \(g\) is bounded, \(\mathbb E N_i\le(\sup g)\mathbb ET_i/\tau<\infty\). Standard renewal reward therefore gives, almost surely, the long-run crossing frequency
\[
 J(T)=\frac{\mathbb EN_i}{\mathbb ET_i}=\frac{\mathbb E H(T/\tau)}m.
\]
This identity holds for lattice clocks, including deterministic periods, and does not require a stationary phase-resolved distribution.

**5. Sharp fixed-mean concave envelope.** Let \(C(s)=s g(a)\) for \(0\le s\le a\), and \(C(s)=H(s)\) for \(s\ge a\). The maximality of \(H(s)/s\) implies \(H(s)\le C(s)\), with strict inequality for \(0<s<a\). Both branches join in value and derivative at \(a\), because \(H(a)=ag(a)\) and \(H'(a)=g(a)\). As \(H''(s)=g'(s)<0\) for \(s>a>s_0\), \(C\) is concave, linear precisely on \([0,a]\), and strictly concave beyond. Jensen therefore gives
\[
 J(T)\le\frac{\mathbb EC(T/\tau)}m\le\frac{C(m/\tau)}m.
\]
The bound is attained by \(T=m\) for \(m\ge a\tau\). The equality conditions force deterministic \(T=m\), since any positive mass below \(a\tau\) creates strict first inequality, while distinct durations at or above \(a\tau\) create strict concavity in Jensen. For \(0<m<a\tau\), equality requires support simultaneously inside the affine region \([0,a\tau]\) and at the contacts \(\{0,a\tau\}\); because \(T>0\) almost surely it cannot happen at this mean. Explicitly choose \(0<\varepsilon<m\) and
\[
\Pr(T=a\tau)=\frac{m-\varepsilon}{a\tau-\varepsilon},\qquad
\Pr(T=\varepsilon)=\frac{a\tau-m}{a\tau-\varepsilon}.
\]
Then \(\mathbb E T=m\), and letting \(\varepsilon\downarrow0\) gives \(J(T)\to H(a)/(a\tau)=g(a)/\tau\). These are finite, strictly positive renewal intervals for every fixed \(\varepsilon>0\).

**6. Comparison with Poisson resetting.** For exponential intervals of rate \(r\), equilibrium reset age is also exponential and \(J_{\mathrm P}(r)=r\int_0^\infty e^{-rt}h_u(t)dt\). Its unique global maximum \(0.104670262107\ldots/\tau\), calculated from the prior Poisson-reset level-crossing law, is strictly less than \(g(a)/\tau\). Strictness also follows abstractly because a nondegenerate exponential law cannot attain the concave-envelope equality conditions; existence of its finite optimal rate is established in the cited Poisson study and later strict-unimodality refinement. The displayed percentage gain is numerical, not a certified interval enclosure.

## Verification
The standalone `check_crossing_envelope.py` rederives the Gaussian Kac--Rice intensity and computes the dimensionless tangent root by quadrature and a bracketed root solve, checks the derivative sign and asymptotic regime on a dense positive grid, tests the concave majorant against many two-point clocks at fixed means, and checks the limiting bursty clock. All numerical assertions are diagnostics: the all-clock optimum, nonattainment and uniqueness are consequences of the analytic arguments above. No numerical grid is treated as a proof of universal inequalities.

## Relationship to prior work
Masoliver and Palassini, *Counting of level crossings for inertial random processes: Generalization of the Rice formula* (arXiv:2301.06608, first public January 16, 2023), derive the free inertial Rice intensities. Montero, Palassini and Masoliver, *The effect of stochastic resettings on the counting of level crossings for inertial random processes* (arXiv:2312.13968, first public December 21, 2023), derive the Poisson-reset crossing identity and optimize within the one-parameter Poisson-clock family. Neither the renewal-level crossing objective over *arbitrary* positive iid interval laws at fixed mean nor its sharp universal tangent constant is covered in those inspected sections. Published work on the **same model** proves strict unimodality of the unreset crossing kernel and the Poisson-optimal rate; those facts and general renewal-reward/Jensen concave-envelope techniques are explicitly prior, not claimed as new.

The mathematically analogous renewal-clock envelope for harmonically trapped active-Brownian *alignment* and the separate Brownian *stationary point-density* envelope are known. They involve different physical observables and free-time kernels. The present specific sharp transition, unique dimensional constant, attainability classification, and quantitative improvement in the **random-acceleration crossing-flux** observable are not implied by their numerical thresholds or claimed as generic new envelope techniques.

## Limitations
Only fully independent complete resets of both position and velocity, iid strictly positive finite-mean durations, undamped integrated Brownian motion and crossings at a nonzero level are covered. Instantaneous reset displacements are not counted as crossings. An asymptotically bursty clock requires arbitrarily short intervals; the positive-clock optimum is a supremum rather than a feasible maximizer in the low-mean regime. A positive reset overhead, minimum reset separation, adaptive resetting, biased initial velocity, zero-level crossings, a restoring force, or a first-passage objective may lead to different optimization laws. The decimal constants are numerical approximations rather than interval certificates. General convex-analytic renewal-clock optimization methods are previously established, and unindexed model-specific work or more general existing results could affect historical publication priority; independent scientific audit remains unperformed.

## References
1. J. Masoliver and M. Palassini, *Counting of level crossings for inertial random processes: Generalization of the Rice formula*, arXiv:2301.06608 (first public 2023-01-16), https://arxiv.org/abs/2301.06608 ; Phys. Rev. E 107, 024111 (2023), with published erratum Phys. Rev. E 107, 069902.
2. M. Montero, M. Palassini and J. Masoliver, *The effect of stochastic resettings on the counting of level crossings for inertial random processes*, arXiv:2312.13968 (first public 2023-12-21), https://arxiv.org/abs/2312.13968 ; Phys. Rev. E 110, 014116 (2024).
3. *Unique optimal resetting in two random-acceleration level-crossing experiments*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-unique-optimal-resetting-in-two-random-acceleration-level-crossi--4aef38b21273 .
4. *A sharp fixed-mean reset-clock transition for active Brownian alignment*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-fixed-mean-reset-clock-transition-for-active-brownian-al--9af371fa60df .
5. *Sharp fixed-mean stationary occupancy under Brownian renewal resetting*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-fixed-mean-stationary-occupancy-under-brownian-renewal-res--a1a5c9c420de .
