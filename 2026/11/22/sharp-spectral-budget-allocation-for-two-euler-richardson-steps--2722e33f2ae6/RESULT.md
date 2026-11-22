# Sharp spectral-budget allocation for two Euler–Richardson steps

## Finding

Let \(0<\mu<L\), set \(\kappa=L/\mu>1\), and prescribe a nonnegative total step budget \(H>0\). Apply exactly two (possibly zero-length) explicit Euler / Richardson updates \(e\mapsto (I-h_jA)e\) to an arbitrary real symmetric positive-definite matrix \(A\) whose spectrum is contained in \([\mu,L]\), where \(h_1,h_2\ge0\) and \(h_1+h_2=H\). The sharp *spectrally robust* two-step amplification is
\[
 \mathcal M_*(H;\mu,L)=\min_{h_1+h_2=H}\max_{\lambda\in[\mu,L]}|(1-h_1\lambda)(1-h_2\lambda)|.
\]
Define the dimensionless budget \(t=\mu H\) and product \(u=\mu^2h_1h_2\). The unique minimizing product \(u_*(t,\kappa)\), and therefore the unique unordered optimal pair, has an explicit piecewise formula. Put
\[
 t_0=\frac2{1+\kappa},\qquad
 t_1=\frac{4\kappa}{\kappa^2+2\kappa-1},\qquad
 t_2=\frac{8(\kappa+1)}{\kappa^2+6\kappa+1},
\]
\[
 t_3=\begin{cases}\dfrac4{1+2\kappa-\kappa^2},&1<\kappa<1+\sqrt2,\\+\infty,&\kappa\ge1+\sqrt2.\end{cases}
\]
Then \(0<t_0<t_1<t_2<t_3\) (interpreting the last inequality with \(+\infty\)), and
\[
 u_*=\begin{cases}
 0,&0<t\le t_0,\\
 \dfrac{t(1+\kappa)-2}{1+\kappa^2},&t_0<t\le t_1,\\
 \dfrac{t-2+\sqrt{(t-2)^2+t^2}}2,&t_1<t\le t_2,\\
 \dfrac{\kappa t-2+\sqrt{(\kappa t-2)^2+(\kappa t)^2}}{2\kappa^2},&t_2<t\le t_3,\\
 \dfrac{t(1+\kappa)-2}{1+\kappa^2},&t_3<t<\infty\quad(1<\kappa<1+\sqrt2).
 \end{cases}
\]
The associated dimensionless steps are \(\{\mu h_1,\mu h_2\}=\{(t-\sqrt{t^2-4u_*})/2,(t+\sqrt{t^2-4u_*})/2\}\). For \(t>t_0\) both are strictly positive and unequal. For \(t\le t_0\), the optimal nonnegative pair has one zero step; under strictly positive steps the same sharp value is only an unattained infimum.

A further sharp conclusion is the **maximum robustly nonexpansive total time**:
\[
\boxed{\ \mathcal M_*(H;\mu,L)\le1\quad\Longleftrightarrow\quad
 \mu H\le t_{\rm safe}(\kappa):=
 \begin{cases}
 \dfrac{2\kappa}{\kappa-1},&1<\kappa\le2,\\[3pt]
 \dfrac8\kappa,&\kappa\ge2.
 \end{cases}\ }
\]
For every \(0<t<t_{\rm safe}\) the sharp factor is strictly below one. By contrast, two equal Euler steps are robustly nonexpansive only for \(t\le4/\kappa\). Hence a suitable unequal pair can extend the robust two-step admissible total time by a factor \(\kappa^2/[2(\kappa-1)]\) for \(1<\kappa\le2\), and exactly by a factor \(2\) for \(\kappa\ge2\). The criterion concerns final two-step amplification, not intermediate stability or integration accuracy.

## Assumptions and scope

The matrix is real symmetric positive definite; the interval \([\mu,L]\) is an uncertainty envelope, not necessarily the exact two-point spectrum of a given matrix. The objective is the supremum over the *whole* interval, equivalent to a worst-case norm over all matrices with spectra in that interval. Step sizes are real nonnegative, and the order of two updates is irrelevant in exact arithmetic. No estimate is asserted for nonnormal matrices, nonlinear dynamics, additive noise or local truncation error.

## Proof

**1. Exact one-variable reduction.** Put \(x=\lambda/\mu\in[1,\kappa]\) and \(u=\mu^2h_1h_2\). By the nonnegative-root condition for \(z^2-tz+u\), the feasible products are exactly \(0\le u\le t^2/4\), and the residual polynomial is
\[
 p_u(x)=1-tx+ux^2.
\]
For fixed \(t\), every \(p_u(x)\) increases *strictly* with \(u\) at every \(x\in[1,\kappa]\). Consequently
\[
 P(u)=\max\{p_u(1),p_u(\kappa)\},\qquad
 N(u)=-\min_{x\in[1,\kappa]}p_u(x)
\]
are continuous with \(P\) strictly increasing and \(N\) strictly decreasing. The objective \(\max\{P(u),N(u)\}\) is therefore uniquely minimized at \(u=0\) when \(P(0)\ge N(0)\), otherwise at the unique crossing \(P(u_*)=N(u_*)\). A crossing exists strictly below \(t^2/4\), because \(p_{t^2/4}(x)=(1-tx/2)^2\ge0\) while \(P(t^2/4)>0\) for the nondegenerate interval. As \(p_0(x)=1-tx\), the initial condition is precisely \(2-t(1+\kappa)\ge0\), proving the first threshold and uniqueness.

**2. Locating the active extrema.** Since \(p_u\) is convex in \(x\), its positive maximum is always attained at \(1\) or \(\kappa\). The former is active precisely when \(u\le t/(1+\kappa)\). The negative minimum occurs at \(\kappa\) when \(u\le t/(2\kappa)\), at the vertex \(v=t/(2u)\in(1,\kappa)\) when \(t/(2\kappa)<u<t/2\), and at \(1\) when \(u\ge t/2\).

Evaluate \(P+\min p_u\), which is strictly increasing in \(u\), at the three transition products \(t/(2\kappa)\), \(t/(1+\kappa)\) and \(t/2\). The resulting zero conditions are respectively
\[
 2-\frac{t(\kappa^2+2\kappa-1)}{2\kappa}=0,\quad
 2-\frac{t(\kappa^2+6\kappa+1)}{4(1+\kappa)}=0,\quad
 2+\frac{t(\kappa^2-2\kappa-1)}2=0.
\]
These are exactly \(t_1,t_2,t_3\). The last equation has a positive solution only when \(\kappa<1+\sqrt2\). One checks
\[
 t_1-t_0=\frac{2(\kappa^2+1)}{(\kappa+1)(\kappa^2+2\kappa-1)}>0,\quad
 t_2-t_1=\frac{4(\kappa-1)(\kappa^2+\kappa+2)}{(\kappa^2+2\kappa-1)(\kappa^2+6\kappa+1)}>0,
\]
and, whenever finite,
\[
 t_3-t_2=\frac{4(\kappa-1)(2\kappa^2+\kappa+1)}{(1+2\kappa-\kappa^2)(\kappa^2+6\kappa+1)}>0.
\]
Thus no other active-extremum regimes are possible.

**3. Solving each balance.** When the minimum is at the upper endpoint and the maximum at the lower endpoint, \(p_u(1)+p_u(\kappa)=0\), giving \(u=[t(1+\kappa)-2]/(1+\kappa^2)\). The same balance holds after the vertex has left through the lower endpoint, with the maximum/minimum exchanged. When the minimum is the interior vertex, \(\min p_u=1-t^2/(4u)\). Balancing it against the upper positive maximum at \(x=a\), where \(a=1\) in the middle regime and \(a=\kappa\) in the next regime, gives
\[
 a^2u^2+(2-ta)u-\frac{t^2}{4}=0.
\]
Its unique positive root is \([ta-2+\sqrt{(2-ta)^2+(ta)^2}]/(2a^2)\), proving the displayed formula. Continuity across every threshold follows from the common balancing equation. Strict increase/decrease of \(P,N\) proves global uniqueness, rather than only stationarity.

**4. Sharp robust stability horizon.** The minimum factor is continuous and strictly below \(1\) at small \(t>0\). In the upper-endpoint/interior-vertex regime, equality to \(1\) forces \(p_u(\kappa)=1\) and \(p_u(t/(2u))=-1\), hence \(u=t/\kappa\) and \(t=8/\kappa\). This lies in that regime precisely for \(\kappa\ge2\). In the post-vertex lower-endpoint regime, equality forces \(p_u(1)=-1\) and \(p_u(\kappa)=1\), yielding \(t=2\kappa/(\kappa-1)\), feasible in that regime precisely for \(1<\kappa\le2\). At \(\kappa=2\) the two constructions coincide. Before \(t_2<2\), the balanced factor is decreasing: on the endpoint-balance branch it is \((\kappa-1)(\kappa+1-\kappa t)/(1+\kappa^2)\), and on the lower-endpoint/vertex branch it is \((\sqrt{(2-t)^2+t^2}-t)/2\), strictly decreasing for \(t<2\). After \(t_2\), the balanced factor is \(p_u(\kappa)\), strictly increasing: in the upper-endpoint/vertex branch it equals \((\sqrt{(\kappa t-2)^2+(\kappa t)^2}-\kappa t)/2\), whose derivative is positive for \(\kappa t>2\); on the final endpoint branch its derivative is \(\kappa(\kappa-1)/(1+\kappa^2)>0\). Thus the sharp factor crosses one exactly once and the displayed boundary is global. This proves necessity, sufficiency and strictness. Equal steps yield \(p(x)=(1-tx/2)^2\), and \(\max_{x\in[1,\kappa]}p(x)\le1\) exactly when \(t\le4/\kappa\).

## Verification

The standalone standard-Python script `check.py` evaluates all possible polynomial extrema directly and compares the proposed formula against a separate one-dimensional golden-section minimization on 1,886 parameter configurations. It also tests exact rational endpoint balances and the sharp stability boundary. It is a supporting finite check, not the proof of the universal quantifiers in the theorem.

Run from the package directory with `python3 check.py`. No third-party Python package is required.

## Relationship to prior work

Classical Chebyshev iteration minimizes over all degree-two residual polynomials normalized by \(p(0)=1\), without prescribing their first derivative. In the present problem, \(p'(0)=-t\) is fixed, so the classical unique unconstrained minimizer is feasible only at \(t=t_2\). There the theorem recovers the degree-two Chebyshev polynomial, but it does not obtain the other budget regimes from unconstrained optimality. Agarwal–Goel–Zhang (2021) examine Chebyshev step schedules and the stability of their orderings; Takabe–Wadayama (2020) examine Chebyshev steps and learned gradient-descent step sizes. Neither reported result states the full minimax classification for an externally prescribed two-step sum. The related published stagewise-safe two-Richardson-step frontier restricts each update separately, whereas this result permits transient amplification and imposes a sum budget. Classical maximal real-axis stability polynomials do cover the \(\kappa\ge2\) stability endpoint, but not the full fixed-budget minimax classification or the finite-band \(1<\kappa<2\) stability frontier. Zolotarev's first problem fixes *leading* coefficients of a monic polynomial, not the two *lowest* coefficients fixed here, so it is not a direct statement of this theorem.

## Limitations

The analysis is for two updates only, real spectral intervals, and final-time worst-case amplification. It does not show that deliberately unequal steps improve approximation of \(e^{-HA}\), roundoff robustness, intermediate-step behavior, or stochastic-gradient performance. The constant-budget feasibility condition is essential. Classical approximation-theory equivalences beyond those inspected may affect historical priority; independent literature verification has not been performed.

## References

- N. Agarwal, S. Goel, C. Zhang, *Acceleration via Fractal Learning Rate Schedules*, first arXiv version 2021-03-01, arXiv:2103.01338; PMLR 139 (2021), 87–99, https://proceedings.mlr.press/v139/agarwal21a.html.
- S. Takabe, T. Wadayama, *Convergence Acceleration via Chebyshev Step: Plausible Interpretation of Deep-Unfolded Gradient Descent*, first arXiv version 2020-10-26, arXiv:2010.13335, https://arxiv.org/abs/2010.13335.
- J. Schöberl, *Interactive Finite Elements*, Chapter 77, *The Chebyshev Method*, https://jschoeberl.github.io/iFEM/iterative/Chebyshev.html.
- H.-J. Rack, R. Vajda, *Explicit algebraic solution of Zolotarev's First Problem for low-degree polynomials*, Journal of Numerical Analysis, Approximation Theory and Applications, https://doi.org/10.33993/jnaat482-1173 (background on a distinct coefficient-constrained approximation problem).
