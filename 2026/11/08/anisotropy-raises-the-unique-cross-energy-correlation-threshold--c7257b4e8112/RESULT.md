# Anisotropy raises the unique cross-energy correlation threshold for a trapped run-and-tumble particle

## Finding

Fix an integer \(d\geq2\) and distinct coordinate indices \(i\neq j\). For the stationary run-and-tumble particle in an anisotropic quadratic trap defined below, set \(A=\mu_i>0\), \(B=\mu_j>0\), \(s=A+B\), \(p=AB\), and let \(g=\gamma>0\) be its complete orientation-redraw rate. Define

\[
\begin{aligned}
U(g)&=2g^4+7sg^3+(6s^2+8p)g^2+12psg,\\
V(g)&=8g^4+34sg^3+(54s^2-4p)g^2+36s^3g+8s^4+4s^2p,\\
H_d(g)&=dU(g)-V(g).
\end{aligned}
\]

The exact covariance of coordinate energies is

\[
\boxed{\operatorname{Cov}(X_i^2,X_j^2)=\frac{2v_0^4 H_d(g)}{d^2(d+2)s(A+g)(2A+g)(B+g)(2B+g)(s+g)(A+2B+g)(2A+B+g)}.}
\]

Its sign has a complete classification:

- For every \(2\leq d\leq4\), it is strictly negative for all finite \(g>0\).
- For every \(d\geq5\), there is exactly one finite \(g_c=g_c(A,B,d)>0\), the positive root of \(H_d(g)=0\). The covariance is negative for \(0<g<g_c\), zero at \(g=g_c\), and positive for \(g>g_c\).
- At fixed \(s=A+B\) and \(d\geq5\), the threshold \(g_c\) increases strictly with \(|A-B|\). In particular,

\[
\boxed{g_c(A,B,d)\geq\frac{3(A+B)}{d-4},}
\]

with equality precisely when \(A=B\). For \(d=5\), \(A=1\), and \(B=2\), the threshold is approximately \(9.32548584904244\), compared with \(9\) at equal stiffness having the same sum.

The dimension-five threshold in the equal-stiffness case is previously implied by the isotropic fourth-moment identity; the anisotropic strict shift and the full unequal-stiffness classification are the claims here.

## Assumptions and scope

Let \(n_t\in S^{d-1}\) be a stationary piecewise-constant orientation process, independently redrawn from the uniform measure on the sphere at every event of a rate-\(g\) Poisson clock. Let the position follow the deterministic equation between events

\[
\dot X_k(t)=-\mu_k X_k(t)+v_0 n_k(t),\qquad k=1,\dots,d,
\]

where \(v_0>0\) and all \(\mu_k>0\). There is no translational Brownian forcing, reorientation memory, velocity dependence, or interaction between particles. The common Poisson clock and unit-length orientation are essential. Exponential stability and bounded forcing yield a unique stationary position process by convolution from the infinite past, with \(|X_k|\leq v_0/\mu_k\). Only the two chosen trap rates affect their joint marginal; other rates may be arbitrary positive numbers. All expectations are taken in the stationary state.

The term *coordinate energy* refers to \(X_k^2\), without an additional stiffness factor. Multiplying the two energies by their positive stiffnesses would leave the covariance sign unchanged.

## Proof

**1. Stationary Poisson-interval representation.** Set \(t_0=0\) and let \(0<t_1<t_2<\cdots\) be the backward recurrence times of successive points of the stationary Poisson clock. The increments are independent \(\operatorname{Exp}(g)\) variables. Let \(n^{(m)}\) be the independent uniform orientations on these intervals. Put

\[
w_{A,m}=\frac{e^{-At_m}-e^{-At_{m+1}}}{A},\qquad w_{B,m}=\frac{e^{-Bt_m}-e^{-Bt_{m+1}}}{B}.
\]

Then, absolutely almost surely,

\[
X_i=v_0\sum_{m\geq0}w_{A,m}n_i^{(m)},\qquad X_j=v_0\sum_{m\geq0}w_{B,m}n_j^{(m)}.
\]

Set \(S_A=\sum_m w_{A,m}^2\), \(S_B=\sum_m w_{B,m}^2\), and \(J_{AB}=\sum_m w_{A,m}^2w_{B,m}^2\). For distinct coordinates of a uniform unit vector,

\[
\mathbb E[n_i^2]=\frac1d,\quad \mathbb E[n_i n_j]=0,\quad
\mathbb E[n_i^2n_j^2]=\frac1{d(d+2)}.
\]

Conditional on the Poisson times, expanding the four orientation factors, all odd terms and cross-index contractions vanish. Terms using distinct clock intervals contribute the independent product \(1/d^2\), whereas the same-interval contribution differs by \(-2/[d^2(d+2)]\). Consequently,

\[
\mathbb E[X_i^2 X_j^2\mid(t_m)]=\frac{v_0^4}{d^2}\left(S_AS_B-\frac{2J_{AB}}{d+2}\right),
\]

and \(\mathbb E[X_i^2]=v_0^2\mathbb E[S_A]/d\). Hence the covariance equals

\[
\frac{v_0^4}{d^2}\left(\operatorname{Cov}(S_A,S_B)-\frac{2\mathbb E[J_{AB}]}{d+2}\right).
\]

**2. Closed renewal equations.** Let \(T\sim\operatorname{Exp}(g)\) denote the first backward interval, set \(a(T)=(1-e^{-AT})/A\) and \(b(T)=(1-e^{-BT})/B\), and write \(\phi(z)=\mathbb E[e^{-zT}]=g/(g+z)\). After the first interval, the remaining weighted sums are independent copies scaled by \(e^{-2AT}\), \(e^{-2BT}\), or \(e^{-2(A+B)T}\) as appropriate. Therefore

\[
\mathbb E[S_A]=\frac{\mathbb E[a(T)^2]}{1-\phi(2A)}=\frac1{A(A+g)},\qquad
\mathbb E[S_B]=\frac1{B(B+g)}.
\]

With \(C=\mathbb E[a(T)^2b(T)^2]\), \(P_A=\mathbb E[a(T)^2e^{-2BT}]\), and \(P_B=\mathbb E[b(T)^2e^{-2AT}]\), the shared-interval quantities obey

\[
\mathbb E[J_{AB}]=\frac{C}{1-\phi(2s)},\qquad
\mathbb E[S_AS_B]=\frac{C+P_A\mathbb E[S_B]+P_B\mathbb E[S_A]}{1-\phi(2s)}.
\]

These are exact. Each term is a finite sum of rational Laplace transforms; for example,

\[
\begin{aligned}
C&=\frac1{A^2B^2}\sum_{r=0}^2\sum_{q=0}^2c_rc_q\phi(rA+qB),\\
P_A&=\frac{\phi(2B)-2\phi(A+2B)+\phi(2A+2B)}{A^2},\qquad(c_0,c_1,c_2)=(1,-2,1).
\end{aligned}
\]

The formula for \(P_B\) follows by exchanging \(A\) and \(B\). Substitution into the preceding covariance identity and cancellation give exactly the displayed rational expression \(2v_0^4H_d(g)/\mathrm{denominator}\). This cancellation can be reproduced symbolically using the independent generator and interval calculations in `verify.py`; the explicit renewal equations establish the result for all positive real rates and every integer \(d\geq2\), not just tested parameter values.

**3. Unique sign reversal.** In increasing powers of \(g\), the coefficients of \(U\) are

\[
(u_0,u_1,u_2,u_3,u_4)=(0,12ps,6s^2+8p,7s,2),
\]

and those of \(V\) are

\[
(v_0,v_1,v_2,v_3,v_4)=(8s^4+4s^2p,36s^3,54s^2-4p,34s,8).
\]

All nonzero coefficients are positive and satisfy the strict ordering

\[
\frac{v_1}{u_1}\geq12>\frac{v_2}{u_2}>\frac{34}{7}>4,
\]

because \(s^2\geq4p>0\), \(9u_2-v_2=76p>0\), and \(7v_2-34u_2=174s^2-300p>0\). For \(g>0\), expanding the derivative of \(V(g)/U(g)\) as a sum over pairs of coefficients proves it is strictly negative: the positive constant term \(v_0\) supplies an additional strictly decreasing contribution, and the ratios \(v_k/u_k\) decrease with \(k\). Moreover,

\[
\lim_{g\downarrow0}\frac{V(g)}{U(g)}=+\infty,
\qquad
\lim_{g\to\infty}\frac{V(g)}{U(g)}=4.
\]

Thus \(H_d(g)=U(g)(d-V(g)/U(g))\) is strictly negative for \(d\leq4\), and has exactly one simple positive zero for every \(d\geq5\), with the asserted signs.

**4. Strict anisotropy enhancement.** For \(d>4\), write \(g_0=3s/(d-4)\). Direct polynomial evaluation yields the exact identity

\[
H_d(g_0)=-\frac{(A-B)^2s^2(2d+1)(4d-7)}{(d-4)^2}.
\]

Therefore the unique root satisfies \(g_c\geq g_0\), strictly for \(A\neq B\). At fixed \(s\), treat \(H_d\) as a polynomial in \(p\). Its derivative is

\[
\frac{\partial H_d}{\partial p}=4\bigl((2d+1)g^2+3dsg-s^2\bigr)>0\qquad(g\geq g_0),
\]

since at \(g=g_0\), the bracket divided by \(s^2\) equals \(8+54/(d-4)+81/(d-4)^2>0\) and grows in \(g\). At the simple root, \(\partial_g H_d=-U\,\partial_g(V/U)>0\). Hence the root decreases strictly with \(p=AB=(s^2-(A-B)^2)/4\), proving that it increases strictly with \(|A-B|\) at fixed \(s\). This proves the entire claim.

## Verification

Run `python verify.py` with Python 3 and SymPy. The checker computes the symbolic generator moment hierarchy and an independent Poisson-interval renewal derivation, verifies both equal the displayed rational covariance for symbolic positive \(A,B,g,d\), verifies the coefficient and anisotropy identities, and checks three numerical examples. No numerical sampling is used to infer universal validity. An additional independent stationary Poisson-interval simulation was performed for representative parameter regimes, consistent with the exact formula; the simulation itself is supplementary and not part of the proof.

## Relationship to prior work

Guéneau, Majumdar and Schehr (first public preprint February 9, 2026; later *Physical Review E* 114, 014144) derive the stationary law and projected moments in an **isotropic** trap. Their conclusion explicitly names anisotropic quadratic confinement as a natural extension and explains that individual coordinate marginals do not reconstruct the full radial or joint distribution in that case. The present cross-coordinate covariance and monotonic unequal-stiffness threshold are not given by separate marginals; they use the common Poisson orientation history.

Sun, Ye and Podgornik (first preprint September 2024) derive exact moment schemes for an isotropic harmonic trap with finite tumble durations. The zero-duration, equal-stiffness specialization is relevant background but does not establish the unequal-stiffness covariance sign diagram. Existing isotropic coordinate fourth-moment results already imply the \(A=B\) threshold, which is cited as a boundary and is not presented as new. The proof here uses elementary common-clock renewal and sphere-moment identities; a more general prior multivariate renewal-moment theorem could imply the displayed formula without identical wording, so publication-priority verification remains warranted.

## Limitations

The classification requires a common Poisson clock with complete independent isotropic heading redraws and a diagonal stable quadratic potential; it does not cover continuous angular diffusion, anisotropic heading laws, correlated redraws, nonlinear traps, finite tumble durations, thermal Brownian forcing, or interacting particles. It describes the sign of a **stationary squared-coordinate covariance**, not a dynamical phase transition or a singularity in the stationary distribution. Anisotropy changes the threshold quantitatively, and there is no claim that its observation alone proves nonequilibrium behavior. Source comparisons support originality to the extent of the inspected literature and accessible index, not exhaustive priority certification. Independent external validation has not been performed.

## References

1. M. Guéneau, S. N. Majumdar and G. Schehr, “Exact stationary state of a \(d\)-dimensional run-and-tumble particle in a harmonic potential,” arXiv:2602.08436 (first public February 9, 2026), *Phys. Rev. E* **114**, 014144 (2026), DOI: 10.1103/mlkm-vgbd, https://arxiv.org/abs/2602.08436.
2. A. Sun, F. Ye and R. Podgornik, “Exact moments for a run-and-tumble particle with a finite tumble time in a harmonic trap,” arXiv:2409.00578 (first public September 2024), *Phys. Rev. E* **111**, 044136 (2025), https://arxiv.org/abs/2409.00578.
3. “Anisotropic run-and-tumble-turn dynamics,” *Soft Matter* (2024), https://pubs.rsc.org/en/content/articlehtml/2024/sm/d3sm00589e (different free-space anisotropic turning dynamics, not anisotropic harmonic confinement).
