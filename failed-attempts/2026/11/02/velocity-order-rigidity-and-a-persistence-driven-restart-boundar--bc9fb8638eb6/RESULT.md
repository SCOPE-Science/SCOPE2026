# Velocity-order rigidity and a persistence-driven restart-boundary reversal in active Ornstein–Uhlenbeck search

## Finding

For an active Ornstein–Uhlenbeck searcher on an absorbing–reflecting interval, independently resetting both position and propulsion velocity to a fixed state, increasing the reset velocity **always** delays target absorption in the strong sample-path order, at every activity strength and every Poisson reset rate. Nevertheless, the *effect of that same velocity bias on the onset of beneficial resetting* changes sign between short and long persistence. The signed displacement of the critical starting position has an exact resolvent formula and opposite sharp persistence limits.

More precisely, fix \(D,L,\tau,\Sigma>0\), a starting/resetting position \(x\in(0,L)\), and a deterministic resetting velocity \(v\in\mathbb R\). Between resets, define the position \(X_t\in[0,L]\) and propulsion velocity \(V_t\in\mathbb R\) by
\[
 dX_t=\varepsilon V_t\,dt+\sqrt{2D}\,dB_t-dK_t,
 \qquad dV_t=-\tau^{-1}V_t\,dt+\sqrt{2\Sigma/\tau}\,dW_t,
\]
where \(B,W\) are independent Brownian motions, \(K\) is the minimal upper-reflection regulator at \(L\), and the trajectory is absorbed at its first visit to zero. Independent rate-\(r\) Poisson resets replace \((X,V)\) by \((x,v)\). Write \(T_r^{\varepsilon,v}\) for the resulting absorption time, allowing \(r=0\), and assume \(\varepsilon\ge0\).

**(1) Exact nonperturbative orientation order.** For \(v_-\le v_+\), every \(\varepsilon\ge0\) and \(r\ge0\) admit a common-noise coupling with
\[
 T_r^{\varepsilon,v_-}\le T_r^{\varepsilon,v_+}\quad\text{almost surely}.
\]
The inequality is strict with positive probability if \(\varepsilon>0\) and \(v_-<v_+\). The same coupling extends to reset-velocity distributions ordered in first-order stochastic order. This is a statement about **absolute completion times**; it does not imply that the improvement due to restarting has the same order.

**(2) Exact weak-activity response for every resetting rate.** Put \(k=\sqrt{s/D}\) and
\[
 f_s(x)=\frac{\cosh(k(L-x))}{\cosh(kL)}.
\]
For \(s>0\), let \(g_s\) be the unique solution of
\[
 -Dg_s''+(s+\tau^{-1})g_s=f_s',\qquad
 g_s(0)=g_s'(L)=0.
\]
The positive Green kernel makes \(g_s(x)<0\) for all \(x\in(0,L)\). If \(F_r^{\varepsilon,v}(s)=\mathbb E[e^{-sT_r^{\varepsilon,v}}]\), then
\[
 \left.\partial_\varepsilon F_r^{\varepsilon,v}(s)\right|_{\varepsilon=0}
 =\frac{s(s+r)}{[s+r f_{s+r}(x)]^2}\,v\,g_{s+r}(x),
 \qquad s>0,\quad r\ge0.
\]
For every \(r>0\), the mean-time susceptibility is
\[
 \left.\partial_\varepsilon\mathbb E T_r^{\varepsilon,v}\right|_{\varepsilon=0}
 =-\frac{v\,g_r(x)}{r f_r(x)^2}.
\]
In particular, the first-order velocity effect has the same strict sign for **all** positive resetting rates. Its high-reset logarithmic sensitivity obeys
\[
 \lim_{r\to\infty}
 \left.\partial_\varepsilon\log\mathbb E T_r^{\varepsilon,v}\right|_{\varepsilon=0}
 =\frac{vx}{2D},\qquad 0<x<L.
\]
The active OU noise strength \(\Sigma\) does not enter these *first-order* formulas.

**(3) Reversal of the onset-of-beneficial-resetting boundary.** Define
\[
 m_1(x)=\frac{Lx-x^2/2}{D},\quad
 m_2(x)=\frac{2L^3x/3-Lx^3/3+x^4/12}{D^2},
 \quad x_c=L\left(1-\frac1{\sqrt5}\right).
\]
Let \(\mathcal R_\tau=(-D\partial_x^2+\tau^{-1})^{-1}\), with Dirichlet condition at zero and Neumann condition at \(L\), and set
\[
 a_\tau=\mathcal R_\tau m_1',\qquad
 b_\tau=\mathcal R_\tau(2a_\tau+m_2'),
\]
\[
 \delta(\tau)=-\frac{2m_1(x_c)a_\tau(x_c)-b_\tau(x_c)/2}
 {\sqrt5 L^3/(15D^2)}.
\]
For each fixed \(\tau>0\) and \(v\ne0\), there is a locally unique critical position \(x_c(\varepsilon;v,\tau)\) near \(x_c\), where the derivative of mean absorption time with respect to restarting rate at \(r=0+\) vanishes, and
\[
 x_c(\varepsilon;v,\tau)
 =x_c+\varepsilon v\,\delta(\tau)+o(\varepsilon)
 \quad(\varepsilon\downarrow0).
\]
The *exact* persistence limits of its coefficient are
\[
 \boxed{\lim_{\tau\downarrow0}\frac{\delta(\tau)}{\tau}=-1,
 \qquad \lim_{\tau\to\infty}\delta(\tau)=\frac{4L^2}{125D}>0.}
\]
Consequently the first-order boundary shift is negative for sufficiently short persistence and positive for sufficiently long persistence when \(v>0\), with signs reversed for \(v<0\). By continuity at least one intermediate persistence time has zero first-order shift; uniqueness of that crossover is **not** asserted. The limits are sequential: \(\varepsilon\downarrow0\) at fixed \(\tau\), followed by the stated persistence limit.

## Assumptions and scope

The result concerns a one-dimensional interval with a perfectly absorbing boundary at zero, instantaneous normal reflection at \(L\), nondegenerate thermal diffusion \(D>0\), a linearly relaxing OU propulsion variable with finite noise variance \(\Sigma>0\), a reset site strictly between the endpoints, independent homogeneous Poisson resetting, and full resetting of both position and velocity. Velocities and OU noise are physical, unscaled quantities; \(\varepsilon\) multiplies propulsion in the position equation. The perturbation and critical shift keep \(D,L,\tau,\Sigma,v\) fixed as \(\varepsilon\downarrow0\). Expectations are over both Brownian motions and resetting; for \(r=0\) only the initial state is imposed.

For distributions of reset velocity, first-order stochastic ordering means there exists a coupling with one reset draw everywhere no larger than the other; the full ordering holds without moment hypotheses, while mean-time or first-order derivative statements require their indicated moments. The quantitative formulas above are for a deterministic \(v\), except the linear response can replace \(v\) by the mean of an integrable reset-velocity distribution.

## Proof

**A. Pathwise velocity comparison.** Use identical Brownian noises and reset times for two processes with \(v_-\le v_+\). On each excursion after reset, their OU velocities differ by the deterministic nonnegative function \((v_+-v_-)e^{-t/\tau}\). Before absorption their unreflected position drivers differ by
\[
 h(t)=\varepsilon(v_+-v_-)\tau(1-e^{-t/\tau}),
\]
which is nonnegative and nondecreasing. The one-sided upper Skorokhod regulator of a continuous driver \(Y\) is \(K_Y(t)=\sup_{0\le u\le t}(Y_u-L)_+\). Since \(h(u)\le h(t)\),
\[
 K_{Y+h}(t)-K_Y(t)\le h(t).
\]
Therefore the two reflected positions are ordered up to the first absorption; the upper-velocity process cannot be absorbed first. Reset both simultaneously and iterate. For strictness, there is positive probability of no reset and a Brownian path for which the lower-velocity process hits zero while the other remains positive. Ordered random velocity protocols are obtained by quantile coupling at every reset. This proof uses neither weak activity nor an approximation.

**B. Resolvent response.** Let \(\tau_0\) denote the no-reset absorption time, and put \(f_s^\varepsilon(x,v)=\mathbb E_{x,v}e^{-s\tau_0}\). Its backward boundary problem is
\[
 (D\partial_x^2+\varepsilon v\partial_x-\tau^{-1}v\partial_v
 +\Sigma\tau^{-1}\partial_v^2-s)f_s^\varepsilon=0,
 \quad f_s^\varepsilon(0,v)=1,\quad \partial_x f_s^\varepsilon(L,v)=0.
\]
At \(\varepsilon=0\), the solution is \(f_s(x)\) as above. Differentiation at zero produces \(\partial_\varepsilon f_s^\varepsilon|_0=v g_s(x)\): the OU generator acts on the linear function \(v\) as multiplication by \(-\tau^{-1}\). Differentiability can be justified first on bounded time horizons by Gaussian change of measure for the independent translational Brownian noise, then by the exponential killed resolvent; the analogous moment derivatives follow from the finite-interval moment equations. The inhomogeneous mixed-boundary problem has a unique solution. Its Green kernel, for \(q=\sqrt{(s+\tau^{-1})/D}\), is
\[
 G(x,y)=\frac{\sinh(q\min(x,y))\cosh(q[L-\max(x,y)])}
 {Dq\cosh(qL)}>0,
\]
so \(g_s(x)=\int_0^L G(x,y)f_s'(y)\,dy<0\) in the open interval. Equivalently,
\[
 g_s(x)=\tau f_s'(x)+A\sinh(qx)+B\cosh(qx),
\]
\[
 B=\tau k\tanh(kL),\qquad
 A=-\frac{\tau k^2/\cosh(kL)+Bq\sinh(qL)}{q\cosh(qL)}.
\]
These equations fix every sign, normalization and boundary term explicitly.

A renewal decomposition at the first reset yields the *exact* transform
\[
 F_r^{\varepsilon,v}(s)
 =\frac{(s+r)f_{s+r}^{\varepsilon}(x,v)}
 {s+r f_{s+r}^{\varepsilon}(x,v)}.
\]
Differentiation gives the asserted response, and the mean formula follows by \(s\downarrow0\). At large \(s\), a local absorbing-boundary expansion gives \(g_s(x)/f_s(x)\to-x/(2D)\), since the two spatial exponents differ by
\(\sqrt{(s+\tau^{-1})/D}-\sqrt{s/D}\sim(2\tau\sqrt{Ds})^{-1}\); the remote reflecting boundary contributes exponentially smaller terms at fixed \(x<L\). Substitution into the mean derivative gives the stated high-reset limit.

**C. Resetting-benefit boundary.** For the no-reset first-passage moments \(M_j^\varepsilon=\mathbb E\tau_0^j\), expand
\[
 M_1^\varepsilon(x,v)=m_1(x)+\varepsilon v a_\tau(x)+o(\varepsilon),\qquad
 M_2^\varepsilon(x,v)=m_2(x)+\varepsilon v b_\tau(x)+o(\varepsilon).
\]
The backward recursions \(\mathcal L_\varepsilon M_1^\varepsilon=-1\) and \(\mathcal L_\varepsilon M_2^\varepsilon=-2M_1^\varepsilon\), with zero at the absorbing endpoint and Neumann at the reflecting endpoint, give precisely
\[
 (-D\partial_x^2+\tau^{-1})a_\tau=m_1',\qquad
 (-D\partial_x^2+\tau^{-1})b_\tau=2a_\tau+m_2'.
\]
The mean under resetting is \((1-f_r^\varepsilon)/(rf_r^\varepsilon)\), so its small-resetting-rate derivative is
\[
 \left.\partial_r\mathbb E T_r^{\varepsilon,v}\right|_{r=0+}
 =(M_1^\varepsilon)^2-\tfrac12M_2^\varepsilon.
\]
At zero activity the right-hand side factorizes as
\[
 H_0(x)=\frac{x(x-2L)(4L^2-10Lx+5x^2)}{24D^2}.
\]
It has the single interior root \(x_c\), with \(H_0'(x_c)=\sqrt5L^3/(15D^2)>0\). The implicit function theorem therefore gives the locally unique root at weak activity and the expression for \(\delta(\tau)\). For sufficiently small \(\varepsilon\), restarting initially helps on the side below the local root and hurts just above it.

For \(\tau\downarrow0\), the mixed-boundary resolvent acts on smooth data at the interior point \(x_c\) as \(\mathcal R_\tau h(x_c)=\tau h(x_c)+o(\tau)\). Hence
\[
 a_\tau(x_c)=\tau m_1'(x_c)+o(\tau),\qquad
 b_\tau(x_c)=\tau m_2'(x_c)+o(\tau),
\]
and the numerator in \(\delta\) equals \(\tau H_0'(x_c)+o(\tau)\), proving the short-persistence limit.

For \(\tau\to\infty\), the resolvent converges to the mixed inverse of \(-D\partial_x^2\). Direct integration gives
\[
 a_\infty(x)=\frac{x(3L^2-3Lx+x^2)}{6D^2},
\]
\[
 b_\infty(x)=\frac{x(20L^4-10L^3x-5L^2x^2+5Lx^3-x^4)}{30D^3}.
\]
Evaluation at \(x_c\) yields
\[
 2m_1(x_c)a_\infty(x_c)-\tfrac12b_\infty(x_c)
 =-\frac{4\sqrt5 L^5}{1875D^3},
\]
which gives \(\delta(\tau)\to4L^2/(125D)\). Positivity of the Green kernel and continuity in \(\tau>0\) guarantee at least one sign crossover, without proving uniqueness.

## Verification

Run `python3 verify.py` using only the standard Python library. The verification program checks the inhomogeneous mixed-boundary equation against finite differences, signs and boundary conditions of \(g_s\), its constant-drift limit against an independent exact drifted-Brownian Laplace transform, the passive restart-onset polynomial, the two opposite persistence-limit coefficients, the differentiated renewal sign, and discrete same-noise order checks. On the packaged version it reports **1,226 passed finite checks**. An independent symbolic calculation of the constant-drift limit recovers \(4L^2/(125D)\), also checked numerically using the exact drifted-Brownian transform. Finite checks cannot prove stochastic ordering, uniqueness of the local root or the asymptotic limits; the arguments above establish those assertions.

## Relationship to prior work

Georgiou, Bressloff and Bertrand (2026, arXiv:2609.21124, first public September 17) study the same finite absorbing–reflecting geometry, active OU dynamics and Poisson resetting. Their fixed reset-velocity phase diagrams are obtained by simulation; their analytic perturbation uses Gaussian zero-mean reset velocities. The present result supplies the exact fixed-velocity first-order formulas, a pathwise ordering for *all* activity strengths, and the persistence-dependent sign reversal of the **resetting-benefit boundary**. This does not overturn their reported numerical regimes for their specific parameter choices: the reversal is an ordered weak-activity/persistence limiting statement, and absolute absorption times remain velocity-ordered.

Shankari and Sahoo (2025, arXiv:2509.18515) analyze resetting in active OU transport through displacement distributions and moments, not the present absorbing first-passage boundary. Bressloff and Linn (2026, arXiv:2602.02446) treat an RTP with a sticky boundary and multiple desorption protocols, so their renewal relations concern another internal state and a different boundary mechanism. Ray, Mondal and Reuveni (2018, arXiv:1811.08239) establish restart transitions for *constant* drift on a half-line: their drift theory motivates the persistent-velocity limit, but does not cover a stochastically evolving OU velocity with an upper reflecting boundary. Standard first-passage renewal identities and one-dimensional Skorokhod comparison principles are used as tools, not claimed as new.

## Limitations

The threshold is **local** in weak activity: uniqueness of the first-order boundary near the passive root is proved, not global uniqueness of a finite-activity critical position. The existence, but not uniqueness, of an intermediate persistence where the first-order shift vanishes is proved. The sharp persistence limits are sequential and should not be read as uniform error bounds for fixed finite activity. The result assumes complete velocity resets, positive thermal diffusion, one reflecting endpoint, OU propulsion with linear relaxation, and independent Poisson restart. It does not treat nonrenewing velocity, partial absorption, state-dependent restart or finite-sample parameter inference. It does not claim that the sign of the restart *benefit* equals the sign of the absolute FPT response.

## References

1. D. K. Georgiou, P. C. Bressloff and T. Bertrand, *Persistence, resetting, and first-passage times of an active Ornstein–Uhlenbeck particle*, arXiv:2609.21124 (first version September 17, 2026), https://arxiv.org/abs/2609.21124.
2. U. Shankari and M. Sahoo, *Active Ornstein-Uhlenbeck particle under stochastic resetting*, arXiv:2509.18515 (first version September 23, 2025), https://arxiv.org/abs/2509.18515.
3. P. C. Bressloff and S. Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary*, arXiv:2602.02446 (first version February 2, 2026), https://arxiv.org/abs/2602.02446.
4. S. Ray, D. Mondal and S. Reuveni, *Péclet number governs transition to acceleratory restart in drift-diffusion*, arXiv:1811.08239 (first version November 20, 2018), https://arxiv.org/abs/1811.08239.
