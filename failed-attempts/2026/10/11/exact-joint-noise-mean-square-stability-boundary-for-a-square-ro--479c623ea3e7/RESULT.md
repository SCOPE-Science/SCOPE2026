# Exact joint-noise mean-square stability boundary for a square-root predator–prey equilibrium

## Finding

The positive coexistence equilibrium of the square-root-response predator–prey model has an **exact two-noise stability frontier**. Put \(u=s/c\), \(z=(3u^2-1)/2\), \(b=u\), \(d=c(1-u^2)/2\), and \(P=\sigma_1^2\), \(Q=\sigma_2^2\). The centered linear Itô system is exponentially stable in mean square **if and only if**
\[
\frac1{\sqrt3}<u<1,\qquad 0\le P<2z,\qquad
0\le Q<\frac{2bd(2z-P)}{2bd+z(2z-P)}.
\]
Both displayed upper inequalities are strict; at their boundary the claimed exponential mean-square stability fails. In particular, the prey-only and predator-only critical noise variances obey
\[
P_*=2z,\qquad Q_*=\frac{2bdz}{bd+z^2}<P_*.
\]
Thus equally scaled predator-only stochastic disturbances always reach the mean-square instability boundary before prey-only disturbances in this specific linearized model.

## Assumptions and scope

Take real parameters \(c>0\), \(0<s<c\), independent standard one-dimensional Brownian motions \(W_1,W_2\), and nonnegative \(\sigma_1,\sigma_2\). The original deterministic model and its positive equilibrium are
\[
\dot x=x(1-x)-\sqrt{x}\,y,\qquad
\dot y=(c\sqrt{x}-s)y,\qquad
(x_*,y_*)=(u^2,u(1-u^2)),\quad u=\frac{s}{c}.
\]
Only the *centered linear Itô perturbation* about this equilibrium is studied:
\[
\begin{aligned}
\mathrm{d}X_t&=(-zX_t-bY_t)\,\mathrm{d}t+\sigma_1 X_t\,\mathrm{d}W_{1,t},\\
\mathrm{d}Y_t&=d\,X_t\,\mathrm{d}t+\sigma_2Y_t\,\mathrm{d}W_{2,t},\qquad
z=\frac{3u^2-1}{2},\ b=u,\ d=\frac{c(1-u^2)}2.
\end{aligned}
\] Exponential mean-square stability means that there exist \(C,\gamma>0\), independent of the deterministic initial state, such that \(\mathbb E[X_t^2+Y_t^2]\le C e^{-\gamma t}(X_0^2+Y_0^2)\) for all \(t\ge0\). This statement is not about global properties of the nonlinear stochastic system, nor about almost-sure stability.

## Proof

**Step 1: deterministic stability is necessary.** For a linear Itô system with the indicated multiplicative noises, the mean obeys \(\dot m=A m\) with
\[
A=\begin{pmatrix}-z&-b\\d&0\end{pmatrix},\qquad \det A=bd>0,\quad\operatorname{tr}A=-z.
\]
Exponential mean-square decay forces exponential decay of all means by Jensen's inequality, hence \(A\) must be Hurwitz. Thus \(z>0\), equivalently \(u>1/\sqrt3\). The existence of the strictly positive coexistence equilibrium already imposes \(u<1\). In the rest of the proof \(z,b,d>0\).

**Step 2: exact moment equations.** Itô's formula and independence of the Brownian motions give, for \(M_1=\mathbb E[X^2]\), \(M_2=\mathbb E[XY]\), \(M_3=\mathbb E[Y^2]\),
\[
\frac{d}{dt}\begin{pmatrix}M_1\\M_2\\M_3\end{pmatrix}
=K\begin{pmatrix}M_1\\M_2\\M_3\end{pmatrix},\quad
K=\begin{pmatrix}P-2z&-2b&0\\d&-z&-b\\0&2d&Q\end{pmatrix}.
\]
Writing \(\delta=2z-P\), the characteristic polynomial of \(K\) is
\[
\lambda^3+(z+\delta-Q)\lambda^2+
\left(4bd+z\delta-(z+\delta)Q\right)\lambda+
2bd\delta-Q(2bd+z\delta).
\]
This identity is an independent algebraic check of the stability frontier; the following argument provides necessity and sufficiency without assuming that any one coefficient alone determines stability.

**Step 3: necessity of both strict noise inequalities.** Suppose the origin is exponentially mean-square stable. Its random linear flow \(\Phi_t\) then yields a symmetric positive-definite quadratic matrix
\[
H_0=\int_0^\infty \mathbb E[\Phi_t^{\mathsf T}\Phi_t]dt,
\]
which satisfies the stochastic Lyapunov identity
\[
A^{\mathsf T}H_0+H_0A+P E_{11}H_0E_{11}+Q E_{22}H_0E_{22}=-I.
\]
Here \(E_{11}\) and \(E_{22}\) are the coordinate projectors. Divide by \(\xi=(H_0)_{11}>0\); write \(\eta=(H_0)_{12}/\xi\) and \(\zeta=(H_0)_{22}/\xi>0\). Comparing the three entries gives
\[
\delta-2d\eta=\frac1\xi>0,\qquad
2b\eta-Q\zeta=\frac1\xi>0,\qquad
d\zeta=b+z\eta.
\]
The middle inequality implies \(\eta>0\). Consequently \(\delta>0\) and \(2bd-Qz>0\); substituting \(\zeta=(b+z\eta)/d\) yields
\[
\frac{Qb}{2bd-Qz}<\eta<\frac{\delta}{2d}.
\]
This nonempty interval forces \(Q(2bd+z\delta)<2bd\delta\), exactly the claimed strict bound on \(Q\), as well as \(P<2z\).

**Step 4: sufficiency by an explicit quadratic Lyapunov function.** Conversely assume \(z>0\), \(0\le P<2z\), and \(0\le Q<2bd\delta/(2bd+z\delta)\). In particular \(2bd-Qz>0\). Choose any real \(\eta\) in the nonempty interval
\[
\frac{Qb}{2bd-Qz}<\eta<\frac{\delta}{2d}
\]
and put \(\zeta=(b+z\eta)/d\). Let \(H=\bigl(\begin{smallmatrix}1&\eta\\\eta&\zeta\end{smallmatrix}\bigr)\). Since \(0<\eta<\delta/(2d)\le z/d\), one has
\[
\det H=\frac bd+\eta\left(\frac zd-\eta\right)>0.
\]
Thus \(H\) is positive definite. The mixed coefficient cancels exactly, and the Itô generator of \(\mathcal V(X,Y)=(X,Y)H(X,Y)^{\mathsf T}\) is
\[
\mathcal L\mathcal V=-(\delta-2d\eta)X^2-(2b\eta-Q\zeta)Y^2.
\]
Both coefficients are strictly positive. By comparison of \(\mathcal V\) with the squared Euclidean norm and Dynkin's formula, a uniform exponential decay bound on \(\mathbb E\mathcal V\), and hence on \(\mathbb E[X_t^2+Y_t^2]\), follows. Combining with Step 3 proves the if-and-only-if assertion including its boundary.

Setting \(Q=0\) gives the critical prey variance \(P_*=2z\). Setting \(P=0\) gives \(Q_*=2bdz/(bd+z^2)\). Because \(bd,z>0\), their strict ordering \(Q_*<P_*\) follows from \(bd/(bd+z^2)<1\).

## Verification

The self-contained script `check_threshold.py` requires Python with SymPy and NumPy. Run `python check_threshold.py` from this package directory. It symbolically recomputes the three moment-characteristic coefficients and the stochastic Lyapunov cancellation and separately checks 1260 sampled parameter configurations against the eigenvalues of the moment generator and the positive-definiteness of the chosen quadratic form. Its symbolic identities are exact; the finite parameter checks are supplementary stress tests, not a substitute for the quantified proof above. For \(u=4/5\), \(c=1\), the exact one-noise variance thresholds are \(P_*=0.92\) and \(Q_*\approx0.372553430821\), explaining why noise of amplitude \(0.7\) lies below the prey-only threshold but above the predator-only threshold.

## Relationship to prior work

Tan, Wang, and Feng (2022), Sections 3–4, construct the mean-square stability matrix for this square-root-response model and illustrate how predator versus prey perturbations affect numerical resilience and stability ranges; they do not state the exact joint-noise **if-and-only-if** curve. Buckwar and Kelly (2014), especially Sections 2.3 and 3.3, provide the general Kronecker-moment method and a numerically studied Holling-II predator–prey example with the same structural pattern of Jacobian and diagonal noises. That generic spectral criterion supplies the analytical background but does not print the present closed-form two-noise trade-off or its strict single-species ordering. Senosiain and Tocino (2023) derive other exact mean-square stability regions for explicitly specified upper-triangular nonnormal drift and noise families, not this square-root-response coexistence Jacobian. The distinct contribution asserted here is the explicit, model-parametric, sharp and constructive frontier, not invention of mean-square covariance or Lyapunov theory.

## Limitations

The result assumes an *Itô*, independent-two-noise, equilibrium-centered linear system and \(0<s<c\). It does not characterize nonlinear stochastic survival, extinction, positivity, sample-path Lyapunov exponents, or finite-time amplification. The strict critical boundary is not exponentially mean-square stable; no statement is made about its finer polynomial moment behavior. The comparison with the existing literature does not exclude all unindexed applications of the general stochastic Lyapunov criterion to the same equations. Independent external validation is not claimed.

## References

1. J. Tan, W. Wang, and J. Feng, “Transient Dynamics Analysis of a Predator–Prey System with Square Root Functional Responses and Random Perturbation,” *Mathematics* **10** (2022), 4087. DOI: 10.3390/math10214087. First online: 2022-11-02.
2. E. Buckwar and C. Kelly, “Asymptotic and Transient Mean-Square Properties of Stochastic Systems Arising in Ecology, Fluid Dynamics, and System Control,” *SIAM Journal on Applied Mathematics* **74** (2014), 411–433. DOI: 10.1137/120893859.
3. M. J. Senosiain and A. Tocino, “A survey of mean-square destabilization of multidimensional linear stochastic differential systems with non-normal drift,” *Numerical Algorithms* **93** (2023), 1543–1559. DOI: 10.1007/s11075-022-01478-6.
