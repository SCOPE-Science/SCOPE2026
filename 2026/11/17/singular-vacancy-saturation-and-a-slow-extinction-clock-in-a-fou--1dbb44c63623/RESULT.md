# Singular vacancy saturation and a slow extinction clock in a four-compartment flow

## Finding

Consider the four-compartment flow
\[
\begin{aligned}
\dot T&=-[a+k(V-E)]T, & \dot E&=k(V-E)T-bE,\\
\dot I&=aT+bE-\gamma I,&\dot B&=\gamma I.
\end{aligned}
\]
The variables respectively denote a temporarily employed balanced compartment, a regularly employed balanced compartment, an imbalanced compartment, and a permanently recovered balanced compartment. The transfer capacity is \(V\), the temporary and regular conflict rates are \(a\) and \(b\), and the recruitment and recovery rates are \(k\) and \(\gamma\).

The following exact **zero-regular-conflict selection and singular-limit theorem** holds.

Let \(a,k,V,\gamma>0\), \(b\ge0\), and take nonnegative initial populations satisfying \(E_0\le V\); write \(N=T_0+E_0+I_0+B_0\), and \(Z_0=V-E_0\).

**(1) Exact selected equilibrium.** At \(b=0\), every orbit converges to \((T,E,I,B)=(0,E_*,0,N-E_*)\). For \(Z_0>0\), the selected regular-employment level is
\[
 E_*=V-\frac ak\operatorname{W}_0\!\left(\frac{kZ_0}{a}\exp\!\left[\frac{k}{a}(Z_0-T_0)\right]\right),
\]
where \(\operatorname{W}_0\) is the nonnegative real inverse of \(u\mapsto ue^u\). At \(Z_0=0\), \(E_*=V\). If \(Z_0>0\), the map \(T_0\mapsto E_*\), with the other parameters and \(E_0\) fixed, is strictly increasing and strictly concave for \(T_0\ge0\), with
\[
\frac{\partial E_*}{\partial T_0}=\frac{k(V-E_*)}{a+k(V-E_*)},\qquad
\frac{\partial^2 E_*}{\partial T_0^2}=-\frac{ak^2(V-E_*)}{[a+k(V-E_*)]^3}<0.
\]

**(2) Sharp vacancy-saturation trichotomy.** Fix \(a,V,E_0,T_0\) with \(Z_0>0\), and let \(k\to\infty\), keeping the other quantities fixed. The asymptotics are
\[
\begin{array}{ll}
T_0<Z_0:& E_*=E_0+T_0-\dfrac ak\log\dfrac{Z_0}{Z_0-T_0}+o(k^{-1});\\[5pt]
T_0=Z_0:& V-E_*=\dfrac ak\operatorname{W}_0\!\left(\dfrac{kZ_0}{a}\right)\sim\dfrac ak\log\dfrac{kZ_0}{a};\\[5pt]
T_0>Z_0:&V-E_*\sim Z_0\exp\!\left[-\dfrac ka(T_0-Z_0)\right].
\end{array}
\]
In particular, the *unfilled vacancy* has an inverse-transfer-rate correction below capacity, a logarithmically enhanced inverse-rate boundary layer at exact capacity, and exponential suppression above capacity. For \(T_0=0\), the first formula is exact: \(E_*=E_0\).

**(3) Weak-regular-conflict clock.** For every \(b>0\) the same flow instead converges to \((0,0,0,N)\). If \(0<b<a\), there is an exact positive slow-mode amplitude (provided \(T_0+E_0>0\))
\[
 A_b:=E_0+k\int_0^\infty e^{bs}[V-E_b(s)]T_b(s)\,ds\in(0,\infty),
 \qquad\lim_{t\to\infty} e^{bt}E_b(t)=A_b.
\]
It satisfies \(\lim_{b\downarrow0}A_b=E_*\). More strongly, for every fixed \(\delta>0\), uniformly over the entire range \(\tau\ge\delta\),
\[
(T_b(\tau/b),E_b(\tau/b),I_b(\tau/b),B_b(\tau/b))
\longrightarrow (0,E_*e^{-\tau},0,N-E_*e^{-\tau})
\quad\text{as }b\downarrow0.
\]
Thus, if \(T_0+E_0>0\), the two orders of the long-time and zero-regular-conflict limits of \(E_b\) disagree: they yield \(0\) and \(E_*>0\), respectively. These are separate limits for fixed \(k\); no joint \(b\downarrow0,k\to\infty\) limit is asserted.

## Assumptions and scope

All four variables are real and nonnegative initially. The initial condition must satisfy \(E_0\le V\), and \(a,k,V,\gamma\) must be strictly positive. The parameter \(b\) is the nonnegative regular-conflict rate; the sharp weak-conflict scaling is considered as \(b\downarrow0\) with all other rates and initial values fixed. The zero-conflict boundary is studied as a nonnegative-rate boundary of the displayed vector field. The large-recruitment asymptotics require \(Z_0>0\) and concern \(k\to\infty\) at fixed \(a\), with \(b=0\). The expression \(o(k^{-1})\) is pointwise in the fixed initial data, not claimed uniform as \(T_0\to Z_0\).

The original notation of Singla--Kumar is \(T=S_T\), \(E=S_r\), \(B=R\), \(V=S_{ra}\), \(k=k_1\), \(a=nq_Tc_T\), and \(b=nq_rc_r\). The mathematical theorem does not require a social-science interpretation of these compartments.

## Proof

**Positive invariance and convergence.** The vector field preserves the total \(T+E+I+B=N\). On \(T=0\) it is tangent; on \(E=0\) the regular-employment derivative is \(kVT\ge0\); on \(E=V\) the derivative is \(-bV\le0\); and on \(I=0\), \(B=0\) the respective outward derivatives are nonpositive. Hence the compact region \(T,E,I,B\ge0\), \(E\le V\), and fixed sum \(N\) is forward invariant and all solutions exist globally. For every \(b\ge0\),
\[
 0\le T_b(t)\le T_0e^{-at},\qquad
 E_b(t)=e^{-bt}\left[E_0+k\int_0^t e^{bs}(V-E_b(s))T_b(s)\,ds\right].\tag{1}
\]
If \(b>0\), the integral equation and \(0\le E_b\le V\) give \(E_b(t)\to0\) (a convolution of the decaying temporary population with \(e^{-bt}\)). Then the variation-of-constants formula for \(\dot I=aT+bE-\gamma I\) gives \(I_b(t)\to0\), and conservation yields \(B_b(t)\to N\).

**Exact invariant and Lambert inversion at \(b=0\).** Set \(Z=V-E\). Then at \(b=0\), \(\dot Z=-kZT\) and \(\dot T=-(a+kZ)T\). For \(Z_0>0\), the quantity
\[
 \mathcal J=T-Z-\frac ak\log Z\tag{2}
\]
is constant because its derivative equals \(-(a+kZ)T+kZT+aT=0\). Since \(T(t)\le T_0e^{-at}\), the integral \(\int_0^\infty T(t)dt\) is finite and \(Z(t)=Z_0\exp[-k\int_0^tT(s)ds]\) decreases to a strictly positive \(Z_*\). Equation (2) at infinity yields
\[
 Z_*+\frac ak\log Z_*=Z_0-T_0+\frac ak\log Z_0.\tag{3}
\]
The left side is strictly increasing on the positive half-line, so its positive solution is unique. Multiply by \(k/a\), exponentiate, and invert \(u\mapsto ue^u\) to obtain the displayed \(Z_*=V-E_*\). If \(Z_0=0\), the equation \(\dot Z=-kZT\) gives \(Z(t)\equiv0\) and hence \(E_*=V\). In either case \(I(t)\to0\) by variation of constants, and \(B\to N-E_*\). Equation (3) differentiated in \(T_0\) yields the stated first derivative; differentiating it again yields the strictly negative second derivative.

**Large-recruitment asymptotics.** Put \(\lambda=k/a\) and \(d=Z_0-T_0\). Equation (3) is equivalent to
\[
 Z_*+\lambda^{-1}\log(Z_*/Z_0)=d.\tag{4}
\]
When \(d>0\), it follows that \(Z_*\to d\); multiplying (4) by \(\lambda\) then gives \(\lambda(Z_*-d)\to\log(Z_0/d)\), producing the first expansion. When \(d=0\), the Lambert formula gives exactly \(Z_*=\lambda^{-1}\operatorname{W}_0(\lambda Z_0)\), and the elementary asymptotic \(\operatorname{W}_0(x)\sim\log x\) yields the logarithmic boundary layer. For \(d<0\), the positive argument \(\lambda Z_0e^{\lambda d}\to0\), and \(\operatorname{W}_0(x)\sim x\) at zero gives \(Z_*\sim Z_0e^{\lambda d}\). These cases exhaust all \(T_0\ge0\) with \(Z_0>0\).

**Singular small-\(b\) time profile.** For \(0<b<a\), multiplying (1) by \(e^{bt}\) and using \(0\le V-E_b(s)\le V\) and \(T_b(s)\le T_0e^{-as}\) shows the integral has finite limit \(A_b\); the tail after time \(t\) is bounded by
\[
 0\le A_b-e^{bt}E_b(t)\le \frac{kVT_0}{a-b}e^{-(a-b)t}.\tag{5}
\]
For each finite \(s\), continuous dependence on the parameter implies \((T_b(s),E_b(s))\to(T_0(s),E_0(s))\) as \(b\downarrow0\), where the subscript \(0\) now denotes the zero-regular-conflict trajectory. On \(0\le b\le a/2\) the integrand in \(A_b\) is dominated by \(kVT_0e^{-as/2}\). Dominated convergence and \(\dot E_0=k(V-E_0)T_0\) therefore yield
\[
 A_b\to E_0+k\int_0^\infty[V-E_0(s)]T_0(s)\,ds=E_*.\tag{6}
\]
For every \(\delta>0\), substitute \(t=\tau/b\), \(\tau\ge\delta\), in (5). The tail tends to zero uniformly over all such \(\tau\), while \(e^{-\tau}A_b\to e^{-\tau}E_*\) uniformly, proving the assertion for \(E\). The temporary coordinate is bounded by \(T_0e^{-a\delta/b}\). Finally,
\[
 I_b(t)\le I_0e^{-\gamma t}
 +aT_0\int_0^te^{-\gamma(t-s)}e^{-as}\,ds+\frac{bV}{\gamma},\tag{7}
\]
whose right side tends to zero uniformly for \(t\ge\delta/b\), as \(b\downarrow0\). Conservation supplies the limit of \(B\). If \(T_0+E_0>0\), then \(E_*>0\): this is clear from \(E_*\ge E_0\) and strict recruitment for \(T_0>0,E_0<V\) (or \(E_*=V>0\) if \(E_0=V\)). Thus the iterated limits differ. All statements follow.

## Verification

The proof is analytical and uses an exact first integral, monotone Lambert inversion, bounded exponential kernels, and dominated convergence; finite experiments are not invoked as infinite proofs. A standalone checker `verify_selection.py` evaluates the exact first integral and Lambert-selected endpoints in three nontrivial parameter sets, numerically checks twelve positive-\(b\) slow-time values, and checks the three sharp large-\(k\) regimes. Run `python verify_selection.py` with Python 3, NumPy and SciPy installed. It prints the tested counts after assertions pass. Numerical integration errors and finite values do not establish the quantified theorem; they provide error-catching checks of the formulas and parameter convention.

## Relationship to prior work

The four-compartment equations and their modeling interpretation are those of Singla and Kumar, *Understanding Work/Life Balance Through Mathematical Model*, arXiv:2611.01091, first posted 2026-10-31. The paper analyzes equilibria, local stability, feasible-region invariance and finite numerical trajectories, but does not give an initial-data-dependent nonisolated equilibrium selection, a fast-transfer vacancy-saturation trichotomy or a weak-regular-conflict slow-time law. Misra and Singh's earlier unemployment model motivates the vacancy-limited transfer term but additionally includes an inflow of unemployed persons, direct employment from that class and attrition; its general equations are not the same closed four-compartment model. Lambert inversion and singular-limit arguments are standard techniques; the mathematical addition here is their complete quantified combination for this precise nonlinear transfer flow, not the techniques themselves.

## Limitations

The conclusions are conditional on \(a,k,V,\gamma>0\), initial \(E_0\le V\), and a closed four-compartment population. In particular, the limiting line at \(b=0\) relies on irreversible recovery and no exogenous workforce inflow. The limit \(b\downarrow0\) is not uniform down to scaled time \(\tau=0\), and the large-\(k\) expansions are not uniform through \(T_0=V-E_0\). No double-scaling \(b,k\) theorem is asserted. This result gives mathematical properties of the stated model, not empirical validation of its social assumptions or predictive accuracy. Historical priority relative to unindexed equivalent compartmental calculations remains a possible risk.

## References

1. F. Singla and V. Kumar, *Understanding Work/Life Balance Through Mathematical Model*, arXiv:2611.01091v1 (first public version: 2026-10-31), https://arxiv.org/abs/2611.01091.
2. A. K. Misra and A. K. Singh, *A mathematical model for unemployment*, Nonlinear Analysis: Real World Applications 12 (2011), 128--136, DOI: 10.1016/j.nonrwa.2010.06.002.
3. R. M. Corless et al., *On the Lambert W function*, Advances in Computational Mathematics 5 (1996), 329--359, DOI: 10.1007/BF02124750 (standard inverse-function background).
