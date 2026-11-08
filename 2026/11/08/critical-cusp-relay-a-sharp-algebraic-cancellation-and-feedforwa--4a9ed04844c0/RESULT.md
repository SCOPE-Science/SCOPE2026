# Critical cusp relay: a sharp algebraic cancellation and feedforward crossover

## Finding

For the critical logistic threshold-response network with two autonomous terminal agents feeding one relay, exact balance of the two opposing terminal inputs increases the relay's extinction exponent from \(1/2\) to \(3/2\). Exact equality of the terminal magnitudes makes the relay decay exponentially instead. The coefficient of the intermediate algebraic law is a convergent finite quadrature of the initial terminal magnitudes, and the narrow weight-imbalance transition has an explicit crossover.

Set \(F(s)=1/(1+e^{-s})\). The network model is
\[
\dot x=-x+\mathcal F(-2\mathbf 1+4Wx),\qquad
W=\begin{pmatrix}0&p&1-p\\0&1&0\\0&0&1\end{pmatrix},\qquad0<p<1,
\]
where \(\mathcal F\) applies \(F\) componentwise. Define \(y_i=2x_i-1\), and suppose \(y_1(0)=a_0>0\) and \(y_2(0)=-b_0<0\), where \(0<a_0,b_0<1\); the relay starts from any \(y_0(0)\in[-1,1]\). Put
\[
 A=\sqrt{3/2},\qquad \tau(a_0,b_0)=\int_{b_0}^{a_0}\frac{dr}{r-\tanh r}.
\]
The integral is signed and finite for every allowed pair of initial magnitudes. Every component converges to zero. The two terminal magnitudes satisfy \(\sqrt t\,y_1(t)\to A\) and \(\sqrt t\,[-y_2(t)]\to A\). The relay obeys the exact alternatives
\[
\begin{aligned}
 p\ne\frac12&:\quad \sqrt t\,y_0(t)\longrightarrow (2p-1)A,\\
 p=\frac12&:\quad t^{3/2}y_0(t)\longrightarrow \frac{A}{4}\tau(a_0,b_0).
\end{aligned}
\]
At \(p=1/2\), this limit is nonzero if and only if \(a_0\ne b_0\); for \(a_0=b_0\) the identity \(y_0(t)=y_0(0)e^{-t}\) holds at all times.

In the critical crossover, fix \(\lambda\in\mathbb R\), and for each sufficiently large observation horizon \(T\) solve a different constant-parameter system with \(p_T=1/2+\lambda/T\). Then
\[
 \lim_{T\to\infty} T^{3/2}y_0^{(p_T)}(T)
 =A\left(2\lambda+\frac{\tau(a_0,b_0)}4\right).
\]
The initial condition is held fixed across this parameter family.

## Assumptions and scope

The feedback matrix is nonnegative and row stochastic but reducible. Its second and third vertices are autonomous recurrent classes; the first receives their convex combination. The logistic parameters are fixed at the nonhyperbolic scalar cusp \(\beta=4\) and external field \(-2\). Time is physical ODE time without rescaling. Initial conditions lie in the invariant cube \([0,1]^3\), with terminal states strictly on opposite sides of the critical half-activation level. The theorem does not assume small deviations from the cusp or restrict the initial relay activation beyond the cube.

## Proof

**Exact normalization.** Since \(2F(2s)-1=\tanh s\) and \(W\mathbf1=\mathbf1\), writing \(y=2x-\mathbf1\) gives
\[
\dot y=-y+\tanh(Wy).
\]
Thus with \(u=y_0\), \(a=y_1>0\), and \(b=-y_2>0\),
\[
 \dot a=-g(a),\qquad\dot b=-g(b),\qquad
 \dot u=-u+\tanh(h_p),\qquad
 h_p=pa-(1-p)b,
\]
where \(g(s)=s-\tanh s\). The function \(g\) is positive for \(s>0\), so \(a,b\) remain positive and decrease to zero. Consequently \(h_p\to0\); variation of constants gives \(u\to0\). This establishes global convergence for all specified initial states.

**Critical terminal amplitude.** Since \(g(s)=s^3/3+O(s^5)\) as \(s\downarrow0\), the inverse-square variable \(q=s^{-2}\) for a positive scalar solution satisfies
\[
 \dot q=\frac{2g(s)}{s^3}\longrightarrow \frac23.
\]
Hence \(q(t)/t\to2/3\) and \(\sqrt t\,s(t)\to A=\sqrt{3/2}\). Moreover \(t^{3/2}g(s(t))\to A/2\).

**Exact time-shift memory.** The scalar flow is strictly monotone, so its solutions starting from \(a_0\) and \(b_0\) satisfy the exact identity
\[
 a(t)=b(t-\tau),\qquad
 \tau=\int_{b_0}^{a_0}\frac{dr}{g(r)},
\]
whenever the right-hand time is nonnegative. This holds with signed \(\tau\), including negative values. Therefore
\[
 a(t)-b(t)=\int_{t-\tau}^{t}g(b(s))\,ds,
\]
with the usual orientation for an integral whose upper endpoint is smaller. The critical scalar amplitude gives
\[
 \lim_{t\to\infty}t^{3/2}[a(t)-b(t)]=\frac{A\tau}{2}.
\]
In particular \(\tau=0\) exactly when \(a_0=b_0\), and then \(a=b\) identically.

**Relay filter.** The forcing is \(h_p=\frac12(a-b)+(p-\frac12)(a+b)\). For each fixed \(p\ne1/2\), its leading term is \((2p-1)A t^{-1/2}\). At \(p=1/2\), the leading term is \(A\tau t^{-3/2}/4\). The variation-of-constants identity
\[
 u(t)=e^{-t}u(0)+\int_0^t e^{-(t-s)}\tanh(h_p(s))\,ds
\]
transfers each polynomial leading coefficient from \(h_p\) to \(u\): for any exponent \(\nu>0\), if \(h_p(t)=Lt^{-\nu}+o(t^{-\nu})\), the unit-rate exponential kernel concentrates on \(s=t-O(1)\), while \(\tanh h_p=h_p+O(h_p^3)\); hence \(u(t)=Lt^{-\nu}+o(t^{-\nu})\). These estimates are uniform for \(p\) in a shrinking \(O(T^{-1})\) neighborhood of \(1/2\) when evaluated at time \(T\). If \(p=1/2\) and \(a_0=b_0\), the forcing vanishes exactly, leaving \(u(t)=e^{-t}u(0)\).

**Crossover.** For \(p_T=1/2+\lambda/T\), the two terminal scalar solutions do not depend on \(p_T\). At time \(T\), uniformly over times within a bounded distance of \(T\),
\[
 T^{3/2} h_{p_T}(T)\longrightarrow
 A\left(\frac\tau4+2\lambda\right).
\]
Applying the same exponential filter argument gives the claimed limit for \(u^{(p_T)}(T)\). If the leading coefficient happens to vanish for one \(\lambda\), the asserted limit is zero; no higher-order rate is claimed there.

## Verification

The symbolic identities \(2F(2s)-1=\tanh s\), \(g(s)=s^3/3+O(s^5)\), and the exact time-shift relation give a fully analytic proof. The standalone file `verify_relay.py` numerically integrates the three-dimensional ODE independently, evaluates the signed quadrature, verifies the scalar time shift, checks balanced and unbalanced asymptotics at three observation horizons, and tests the exact exponential case. Executing it in Python with NumPy and SciPy produces the terminal line `VERIFY_OK critical_relay=1 symmetric_exact=1 signed_quadrature=1 balanced_samples=3 unbalanced_samples=6 time_shift_samples=2 crossover_samples=6`. Numerical runs check representative states only and are not substitutes for the universal proof.

For \(a_0=0.8\), \(b_0=0.5\), the quadrature is \(\tau\approx4.2191616180280\) and the balanced coefficient is \(A\tau/4\approx1.2918491383130\). The program confirms convergence of the rescaled relay amplitude to this coefficient. It also numerically checks the double scaling for several fixed values of \(\lambda\).

## Relationship to prior work

Boudourides, *Collective Hysteresis and Multistability in Threshold Networks* (arXiv:2609.10580, first posted 2026-09-05), defines precisely this row-stochastic response-network family. Its Section 3 identifies the scalar cusp and the possibility of multiple neutral directions when \(W\) is reducible; Sections 4–5 address stable heterogeneous equilibria and cusp bifurcations away from the critical homogeneous point. The paper's main theorems and appendices do not give the present opposite-sign, feedforward, time-dependent decay classification. This theorem concerns the transient dynamics *at* the critical equilibrium and its input-cancellation geometry rather than the paper's bifurcation-location laws.

Kaye, *From individual thresholds to collective hysteresis* (doi:10.1098/rsif.2026.0267), develops the scalar threshold mechanism and spatial modeling, not the three-agent reducible feedback relay. Classical scalar parabolic relaxation and positivity of cooperative flows are used, not claimed as new. The distinct contribution is the exact exponent jump, signed time-shift coefficient, and crossover for the reducible network. Priority beyond the inspected sources is not certified.

## Limitations

The closed formulas require logistic feedback, the exact scalar cusp, and the specified feedforward matrix. The terminal signs are opposing and nonzero. At equal coupling, equal terminal magnitudes imply exact exponential convergence; without this equality the relay is algebraic. The result concerns deterministic activation fractions, not stochastic finite-agent populations. It neither establishes comparable powers for arbitrary nonlinear threshold distributions nor makes claims about irreducible networks or robustness to feedback into the terminal classes.

## References

1. M. Boudourides, *Collective Hysteresis and Multistability in Threshold Networks*, arXiv:2609.10580 (2026-09-05). https://arxiv.org/abs/2609.10580
2. A. R. Kaye, *From individual thresholds to collective hysteresis: a mechanistic model of the dawn chorus*, *Journal of the Royal Society Interface* **23** (2026), article 20260267. doi:10.1098/rsif.2026.0267.
3. G. A. Enciso, *Fixed points and convergence in monotone systems under positive or negative feedback*, *International Journal of Control* **87** (2014), 301–311. doi:10.1080/00207179.2013.830336.
