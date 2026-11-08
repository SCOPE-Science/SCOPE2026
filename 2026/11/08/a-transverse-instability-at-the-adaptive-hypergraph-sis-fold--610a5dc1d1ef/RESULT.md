# A transverse instability at the adaptive hypergraph SIS fold

## Finding

For the homogeneous three-person-group adaptive SIS closure with one group per vertex, the saddle-node of positive stationary infections can carry a **second, strictly unstable multiplier**. In a nonempty open set of physically admissible parameters, **two positive fixed points exist, but neither is locally asymptotically stable**, while the disease-free fixed point is locally asymptotically stable. Thus stationary endemic existence need not imply endemic-state bistability.

For recovery probability \(0<\mu<1/4\), define
\[
 r_* = 1-\sqrt{1-3\mu},\qquad
 h_* = \frac{1-2r_*}{3\mu r_*^2},\qquad
 \gamma_c=\frac{\mu^2(1-2r_*)}{r_*(1-r_*)^2}.
\]
At the positive-equilibrium fold with transmission probability \(\beta=1\), activity-recovery probability \(\gamma>0\), and activity-suppression probability \(\eta=h_*\gamma\), the two Jacobian eigenvalues are exactly
\[
 \lambda_1=1,\qquad
 \lambda_2=1+\frac{\mu(1-2r_*)}{1-r_*}-\gamma(1+h_*r_*^3).
\]
In particular, \(\lambda_2>1\) whenever \(0<\gamma<\gamma_c\). The condition \(\gamma(1+h_*)<1\) can also be imposed, keeping \(\gamma+\eta<1\).

A fully rational instance is
\[
 \mu=\frac{11}{108},\quad \beta=1,\quad
 \gamma=\frac1{100},\quad \eta=\frac{216}{275},\quad
 (r_*,\theta_*)=\left(\frac16,\frac{11}{15}\right).
\]
Its exact Jacobian and spectrum are
\[
 J_* = \begin{pmatrix}146/135&5/216\\-6/125&217/220\end{pmatrix},
 \qquad \operatorname{spec}(J_*)=\left\{1,\frac{6343}{5940}\right\}.
\]
The second eigenvalue is greater than one. Holding \(\mu\) and \(\gamma\) fixed and taking \(\eta\) slightly below \(216/275\) creates two distinct positive equilibria near this fold; both retain an eigenvalue greater than one. Their hyperbolic instability persists for transmission probabilities slightly below one, giving an open parameter set entirely inside the admissible parameter domain.

## Assumptions and scope

Consider only the two-dimensional *homogeneous deterministic mean-field closure* of an adaptive three-uniform susceptible–infected–susceptible system, without extra intervention or rewiring. There is one hyperedge per vertex in the homogeneous degree approximation. Infection prevalence \(r_t\in[0,1]\) and mean hyperedge activity \(\theta_t\in[0,1]\) obey
\[
 r_{t+1}=(1-\mu)r_t+\beta\theta_t r_t^2(1-r_t),\qquad
 \theta_{t+1}=\theta_t(1-\eta r_t^3)+\gamma(1-\theta_t).
\]
Assume \(0<\mu<1\), \(0<\gamma<1\), and \(0\le\eta,\beta\le1\). The map preserves the unit square. A positive stationary infection necessarily obeys \(0<r<1/(1+\mu)\), while \(\theta=1/(1+(\eta/\gamma)r^3)\). The main family specializes to \(0<\mu<1/4\).

## Proof

Write \(h=\eta/\gamma\). With \(\beta=1\), the positive stationary equation reduces, without approximation beyond the stated closure, to
\[
 F_h(r):=\mu h r^3+r^2-r+\mu=0.
\]
For \(h\ge0\), \(F_h''(r)=6\mu h r+2>0\) on the positive axis. At a positive double root, \(F_h(r)=F_h'(r)=0\) imply
\[
 h=\frac{1-2r}{3\mu r^2},\qquad 3\mu=2r-r^2.
\]
For \(0<\mu<1/4\), the unique solution with \(r<1/2\) is \(r=r_*\), and it satisfies \(0<r_*<1/(1+\mu)\), \(h=h_*>0\). Strict convexity, positivity of \(F_h\) at zero and at \(1/(1+\mu)\), and continuity give two distinct positive roots for all \(h<h_*\) sufficiently close to \(h_*\), and their coalescence at \(h_*\).

At a positive fixed point, use \(\beta\theta r(1-r)=\mu\) to obtain the exact linearization
\[
 J=\begin{pmatrix}
 1+\mu\dfrac{1-2r}{1-r}&\dfrac{\mu r}{\theta}\\
 -3\eta\theta r^2&1-\gamma-\eta r^3
 \end{pmatrix}.
\]
A double root of the stationary equations gives a unit multiplier: differentiating the stationary curve at the fold produces a nonzero null vector of \(J-I\). The remaining eigenvalue is \(\operatorname{tr}(J)-1\), namely the displayed \(\lambda_2\). At the fold, \(\mu(1+h_*r_*^3)=r_*(1-r_*)\), so
\[
 \lambda_2-1=\frac{\mu(1-2r_*)}{1-r_*}
       -\frac{\gamma r_*(1-r_*)}{\mu},
\]
whose sign is positive exactly when \(\gamma<\gamma_c\). Both \(\gamma_c\) and \(1/(1+h_*)\) are strictly positive, so there are admissible choices of \(\gamma\).

For the rational instance, substitution gives the displayed matrix. Its characteristic polynomial factors as \((z-1)(z-6343/5940)\), proving a second unstable multiplier exactly, without numerical approximations. For \(h<h_*\) sufficiently close to the fold, both simple positive roots tend to \(r_*\); their Jacobians tend to \(J_*\). Continuity of matrix eigenvalues preserves a multiplier greater than one on both branches. Because the two roots are simple, they and their unstable multipliers persist under small changes of \(\beta\), including \(\beta<1\). Finally the disease-free state is \((0,1)\) with Jacobian eigenvalues \(1-\mu\) and \(1-\gamma\), both strictly inside the unit circle. This proves the claimed local-stability contrast and its open-parameter persistence.

## Verification

The accompanying `fold_check.py` uses exact rational symbolic calculations to verify the stationary fold conditions, exact Jacobian and its eigenvalues. It also numerically locates the two stationary roots for three values of \(\eta/\eta_*<1\) and checks that each has spectral radius greater than one. The analytical continuity argument, not the finite checks, establishes the open set.

## Relationship to prior work

Li, Xie, Li, Feng and Perc (2026), in Section 2.3, derive the homogeneous adaptive hypergraph SIS fixed-point equation and an implicit saddle-node transmission threshold. Their theorem and simulations address stationary epidemic branches and observed bistability but do not establish the additional Jacobian multiplier at a physical fold or exclude stability of both emerging endemic branches. The present result uses their actual two-variable update rules, retains the activity variable during linearization, and supplies a different conclusion: the existence of endemic branches can coexist with their simultaneous linear instability. Earlier general hypergraph SIS threshold analyses concern different dynamical contact laws and do not directly settle this fold's transverse multiplier.

## Limitations

This is not a theorem about the exact stochastic SIS process, about heterogeneous trajectories, or global convergence. It does not claim that no other attracting invariant sets (including cycles) exist. It proves local instability of two nearby positive fixed points. The rational fold is at the boundary \(\beta=1\), but the two unstable positive equilibria occur in an open regime with \(\beta<1\) by the stated perturbation argument. No independent scientific audit has been performed.

## References

- Y. Li, M. Xie, Q. Li, M. Feng and M. Perc, *Adaptive Epidemic Dynamics on Hypergraphs with Group-Level Immunization and Rewiring*, arXiv:2606.15578, first public June 14, 2026, https://arxiv.org/abs/2606.15578, especially Section 2.1 equations (2)–(5), Section 2.3 equations (14)–(18), and Section 4.
- B. Jhun, M. Jo and B. Kahng, *Simplicial SIS model in scale-free uniform hypergraph*, arXiv:1910.00375 (2019), https://arxiv.org/abs/1910.00375.
- D. J. Higham and H.-L. de Kergorlay, *Disease extinction for susceptible–infected–susceptible models on dynamic graphs and hypergraphs*, *Chaos* 32, 083131 (2022), https://doi.org/10.1063/5.0093776.
