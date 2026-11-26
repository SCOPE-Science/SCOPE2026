# A parameter-free temporal direction ratio in Brownian motion with diffusing diffusivity under resetting

## Finding

For the stationary completely-reset diffusing-diffusivity model defined below, let the positional energy be \(Q_t=\sum_{j=1}^d X_j(t)^2\) and the instantaneous diffusion coefficient be \(V_t=\omega_t^2\). For every real lag \(t\geq0\),

\[
\begin{aligned}
C_{QV}(t)&:=\operatorname{Cov}(Q_t,V_0)
=\frac{48d\Lambda^4}{r^3}e^{-rt}\left(1+\frac{5rt}{6}\right),\\
C_{VQ}(t)&:=\operatorname{Cov}(V_t,Q_0)
=\frac{48d\Lambda^4}{r^3}e^{-rt}.
\end{aligned}
\]

In particular, for every \(t>0\), the directed temporal asymmetry is strictly positive and its **ratio is independent of both dimension and diffusivity scale**:

\[
\frac{C_{QV}(t)}{C_{VQ}(t)}=1+\frac56rt,
\qquad
C_{QV}(t)-C_{VQ}(t)=\frac{40d\Lambda^4}{r^2}t e^{-rt}>0.
\]

Thus the reset rate can be recovered from the two opposite-order square-correlations at any one positive lag, assuming exact stationary ensemble measurements:

\[
r=\frac{6}{5t}\left(\frac{C_{QV}(t)}{C_{VQ}(t)}-1\right).
\]

After normalization by the simultaneous covariance \(C_{QV}(0)=C_{VQ}(0)\), the asymmetry equals \(\tfrac56(rt)e^{-rt}\), with its **unique positive-lag maximum** \(5/(6e)\) at \(t=1/r\).

All ordinary two-time covariances of the coordinates \((X_1,\ldots,X_d,\omega)\) match those of independent, variance-matched stationary Gaussian Ornstein–Uhlenbeck coordinates with relaxation rate \(r\). The unequal ordered square-correlations therefore detect temporal structure invisible to the full ordinary second-order covariance matrix.

## Assumptions and scope

Fix an integer \(d\geq1\), diffusivity parameter \(\Lambda>0\), and Poisson reset rate \(r>0\). Between resets the process on \(\mathbb R^{d+1}\) obeys

\[
d\omega_t=\sqrt{2}\Lambda\,dB_t,
\qquad
dX_j(t)=\sqrt{2}|\omega_t|\,dW_j(t),\quad 1\le j\le d,
\]

where \(B,W_1,\dots,W_d\) are mutually independent standard Brownian motions. A separate independent rate-\(r\) Poisson process simultaneously maps every \(X_j\) and \(\omega\) to zero at each event. The coefficient \(|\omega|\) may equivalently be replaced by \(\omega\), without changing the joint law of \((X_1,\ldots,X_d,\omega)\). Work in the unique stationary regenerative version, not an arbitrary transient initial law. The observable \(V=\omega^2\) is the physical instantaneous diffusivity; \(Q\) is squared displacement from the reset origin. All covariance statements refer to centered stationary observables.

## Proof

**Stationary law and finite moments.** Coupling any two initial states at their first common Poisson reset gives uniqueness of the stationary law. Regenerating a free trajectory from the origin at a backward age \(A\sim\operatorname{Exp}(r)\), independent of the post-reset Brownian drivers, constructs this law. All polynomial moments used below are finite because free Brownian moments grow polynomially in age and \(A\) has moments of every order.

At a fixed reset-free age \(a\), Brownian covariance and Wick's identity give, for \(0\le s\le a\),

\[
\mathbb E[\omega_s^2]=2\Lambda^2s,
\qquad
\mathbb E[\omega_s^2\omega_a^2]
=4\Lambda^4sa+8\Lambda^4s^2.
\]

Because \(W_j\) is independent of the whole \(\omega\)-trajectory, conditional Itô isometry yields

\[
\mathbb E[Q_a]=2d\Lambda^2a^2,
\quad
\mathbb E[Q_a\omega_a^2]
=2d\int_0^a\mathbb E[\omega_s^2\omega_a^2]ds
=\frac{28d\Lambda^4}{3}a^3.
\]

Also \(\mathbb E[\omega_a^2]=2\Lambda^2a\) and \(\mathbb E[\omega_a^4]=12\Lambda^4a^2\). Since \(\mathbb E[A^k]=k!/r^k\), averaging over the stationary age gives

\[
\begin{aligned}
\mathbb E V&=\frac{2\Lambda^2}{r},&
\mathbb E Q&=\frac{4d\Lambda^2}{r^2},\\
\mathbb E V^2&=\frac{24\Lambda^4}{r^2},&
\mathbb E(QV)&=\frac{56d\Lambda^4}{r^3}.
\end{aligned}
\]

Consequently,

\[
\operatorname{Var}(V)=\frac{20\Lambda^4}{r^2},
\qquad
\operatorname{Cov}(Q,V)=\frac{48d\Lambda^4}{r^3}.
\]

**Forward and backward temporal orders.** For a stationary observation at time zero, the probability of **no reset** during \((0,t]\) is \(e^{-rt}\), independent of the state at zero. If at least one reset occurs, the terminal state is independent of the state at zero, conditional on the reset schedule, so it contributes zero to the centered cross-covariance. On a reset-free interval, the Brownian conditional expectations are

\[
\mathbb E[V_t\mid X_0,\omega_0;\ \text{no reset}]
=V_0+2\Lambda^2t,
\]

\[
\mathbb E[Q_t\mid X_0,\omega_0;\ \text{no reset}]
=Q_0+2dtV_0+2d\Lambda^2t^2.
\]

The constants disappear when multiplied by a centered time-zero observable. Thus the *exact* stationary covariances satisfy

\[
C_{VQ}(t)=e^{-rt}\operatorname{Cov}(V,Q),
\quad
C_{QV}(t)=e^{-rt}\bigl[\operatorname{Cov}(Q,V)+2dt\operatorname{Var}(V)\bigr].
\]

Substitution of the stationary moments proves both formulas, strict ordering, the universal ratio, and rate recovery for every \(t>0\). The normalized difference is \((5/6)u e^{-u}\) with \(u=rt\). Its derivative has the sign of \(1-u\), establishing the unique maximum at \(u=1\).

**Why second-order coordinates do not see it.** The same reset-free conditioning and centered Itô increments yield, for \(t\geq0\),

\[
\operatorname{Cov}(X_i(t),X_j(0))
=\delta_{ij}\frac{4\Lambda^2}{r^2}e^{-rt},
\qquad
\operatorname{Cov}(\omega_t,\omega_0)=\frac{2\Lambda^2}{r}e^{-rt},
\]

with all \(X_i\)-to-\(\omega\) and off-diagonal \(X_i\)-to-\(X_j\) covariances zero. These are exactly the covariance functions of a diagonal stationary Gaussian Ornstein–Uhlenbeck vector with damping \(r\) and matching variances. The claimed square-correlations refer to different observables, and need not match that Gaussian comparison.

## Verification

Run `python check.py` from the directory containing this document, with NumPy and SciPy installed. This standalone checker independently evaluates all four stationary moments by (i) a polynomial Markov-generator linear system and (ii) exponential-age/Wick quadrature. It then computes the two ordered lag covariances using the matrix exponential of the exact reset generator and compares them with the closed formulas for multiple dimensions, scales, rates, and lags. The checked version produced `PASS 321 independent generator/age/semigroup checks`. These tests validate algebra and normalization; the proof above supplies all-lag and all-parameter quantifiers.

## Relationship to prior work

Santra, Basu and Sabhapandit (2022) defined exactly this simultaneously-reset stochastic-diffusivity model and determined its time-dependent and stationary **position** distributions and radial scaling laws. Their joint free Fokker–Planck and renewal equations provide the starting dynamics, not a new derivation claimed here. In their accessible first-version full text, Sections 4–6 evaluate stationary marginals and their approach, rather than the two ordered stationary mixed moments \(C_{QV}\) and \(C_{VQ}\), the parameter-free ratio, or rate identification.

Sposini and collaborators (2018) analyze stochastic-diffusivity models without the present simultaneous Poisson-reset protocol. Sokolov (2023) establishes resetting fluctuation–dissipation relations for ordinary Brownian motion with a fixed diffusivity, rather than the square-displacement/volatility cross-ordering in this model. General resetting renewal machinery is applicable to the *method*, but does not by itself supply the evaluated universal ratio unless these specific mixed moments are computed. Analogous fourth-order temporal asymmetries in other reset-driven systems have different generators and do not imply the displayed positive two-way ratio by substitution.

## Limitations

The theorem requires independent Wiener drivers and simultaneous complete **Poisson** resets of position and diffusion-amplitude state. It does not cover partial resets, state-dependent reset rates, deterministic or non-Poisson renewal times, correlated drivers, or measured finite-sample inference. The rate-identification formula presumes exact access to instantaneous diffusivity and both ordered stationary covariance functions. The Gaussian comparator shares only ordinary two-time coordinate covariances, not full stationary distributions. No claim is made concerning thermodynamic entropy production or finite-sample estimator performance. General diffusion/renewal identities make further previously unlocated exact specializations possible; independent priority examination remains appropriate.

## References

1. I. Santra, U. Basu, and S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient*, arXiv:2205.00549v1 (first posted 2022-05-01), J. Phys. A 55, 414002 (2022), DOI 10.1088/1751-8121/ac8dcc. Source: https://arxiv.org/html/2205.00549v1.
2. V. Sposini, A. V. Chechkin, F. Seno, G. Pagnini, and R. Metzler, *Random diffusivity from stochastic equations: comparison of two models for Brownian yet non-Gaussian diffusion*, arXiv:1811.09531 (2018). Source: https://arxiv.org/abs/1811.09531.
3. I. M. Sokolov, *Linear Response and Fluctuation-Dissipation Relations for Brownian Motion under Resetting*, Phys. Rev. Lett. 130, 067101 (2023), DOI 10.1103/PhysRevLett.130.067101.
4. N. Mesquita, S. N. Majumdar, and S. Sabhapandit, *Dynamically emergent correlations in a Brownian gas with diffusing diffusivity*, arXiv:2506.20859 (2025), comparison context for shared stochastic diffusivity without the present resetting cross-time theorem.
