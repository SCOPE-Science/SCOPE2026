# Stochastic-order basin selection and one-dimensional instability in the incremental voter mean field

## Finding

Consider the discrete-opinion incremental voter mean-field equation of Cao and Gong [1] on the \(2k+1\) opinions \(0,1,\ldots,2k\), with any integer \(k\geq2\). Write \(m=2k\), let \(q_j(t)\) be the mass on opinion \(j\), and let \(u_j=1/(m+1)\) be the uniform equilibrium.

**Stochastic-order selection theorem.** If the initial probability vector strictly first-order stochastically dominates \(u\), meaning
\[
\sum_{j=i}^{m}q_j(0)\geq\frac{m+1-i}{m+1}\quad(1\leq i\leq m),
\]
with at least one strict inequality, then \(q(t)\to(0,\ldots,0,1)\). If every inequality is reversed and at least one is strict, then \(q(t)\to(1,0,\ldots,0)\). These are global, not merely local, basin certificates.

**Threshold geometry.** Restricted to the \(m\)-dimensional probability simplex, the Jacobian at \(u\) has exactly one strictly positive eigenvalue and \(m-1\) strictly negative eigenvalues. Hence \(u\) is a hyperbolic saddle with a one-dimensional unstable manifold and a codimension-one local stable manifold.

For example, at \(k=2\), the distributions \((19,19,19,19,24)/100\) and \((24,19,19,19,19)/100\) converge respectively to the right and left consensus equilibria. Their respective initial mean opinions are \(21/10\) and \(19/10\), well inside the interval not resolved by the far-mean basin conditions of [1].

## Assumptions and scope

This is a deterministic mean-field assertion, not an almost-sure assertion for a fixed finite population. The ODE uses the original update normalization of [1]. For \(m=2k\), set \(M(q)=\sum_{j=0}^{m}j q_j\) and \(a(q)=M(q)/m\). Then
\[
\begin{aligned}
\dot q_0&=(1-a)q_1-aq_0,\\
\dot q_j&=a q_{j-1}+(1-a)q_{j+1}-q_j\quad(1\leq j<m),\\
\dot q_m&=a q_{m-1}-(1-a)q_m.
\end{aligned}
\]
For every initial \(q\) in the closed probability simplex, this system has a unique global trajectory in the simplex. All time statements mean \(t\to+\infty\). The ordering hypothesis is non-strict coordinatewise in the cumulative tails, but requires at least one genuinely strict comparison.

## Proof

**1. Cooperative cumulative-tail flow.** Put \(S_i=\sum_{j=i}^{m}q_j\) for \(1\leq i\leq m\), and define \(S_0=1\) and \(S_{m+1}=0\). The feasible region is the compact convex ordered simplex \(1\geq S_1\geq\cdots\geq S_m\geq0\). Since \(M=\sum_{i=1}^{m}S_i\), the equations become
\[
\dot S_i=F_i(S):=aS_{i-1}+(1-a)S_{i+1}-S_i,\qquad
 a=\frac1m\sum_{j=1}^{m}S_j.
\]
The uniform equilibrium corresponds to \(U_i=(m+1-i)/(m+1)\). For all different variable indices \(i\ne j\),
\[
\frac{\partial F_i}{\partial S_j}=
\frac{S_{i-1}-S_{i+1}}m
+a\,\mathbf1_{j=i-1}+(1-a)\,\mathbf1_{j=i+1}\geq0.
\]
This Metzler property on the convex feasible set yields order preservation for the flow. Comparison with \(U\) is *strict* in every cumulative-tail coordinate at every positive time whenever the initial order is strict in at least one coordinate: along the segment from \(U\) to any comparable state, the integrated Jacobian has strictly positive adjacent off-diagonal entries, because \(a(U)=1/2\). Positivity therefore propagates along the entire connected path of tail coordinates.

**2. Explicit positive and negative strict barriers.** Define \(w_i=i(m+1-i)\), for \(1\leq i\leq m\), and set \(w_0=w_{m+1}=0\). For each \(0<\varepsilon<1/[(m+1)(m+2)]\), both \(U+\varepsilon w\) and \(U-\varepsilon w\) are feasible, with strictly positive masses. Using \(w_{i-1}-2w_i+w_{i+1}=-2\) and \(\sum_{i=1}^{m}w_i=m(m+1)(m+2)/6\), direct substitution gives
\[
F_i(U\pm\varepsilon w)
=\pm\frac{m-1}{3}\varepsilon
+\frac{(m+1)(m+2)[2i-(m+1)]}{3}\varepsilon^2.
\]
Since \(\lvert2i-(m+1)\rvert\leq m-1\), every component of \(F(U+\varepsilon w)\) is strictly positive, while every component of \(F(U-\varepsilon w)\) is strictly negative. By the order-preserving flow property, the trajectory from the positive barrier is coordinatewise increasing; that from the negative barrier is decreasing. Both have limits in the compact feasible region, and their limits are equilibria.

**3. Only three equilibria.** If \(a=0\) or \(a=1\), the stationary mass is concentrated respectively at \(0\) or \(m\). For an interior stationary value \(0<a<1\), the zero stationary birth-death flux forces \(q_j\) to be proportional to \(r^j\), with \(r=a/(1-a)>0\). The mean self-consistency condition, after clearing the geometric-series denominators when \(r\ne1\), requires
\[
(m-1)r^{m+1}-(m+1)r^m+(m+1)r-(m-1)=0.
\]
Its derivative is \((m+1)[(m-1)r^m-mr^{m-1}+1]\). The bracket is positive except at \(r=1\): its derivative is \(m(m-1)r^{m-2}(r-1)\), and its minimum is zero at \(r=1\). Thus the polynomial is strictly increasing and vanishes only at \(r=1\). This yields precisely the uniform interior equilibrium. The equilibrium classification is also recorded in [1].

**4. Global selection.** The increasing positive-barrier orbit must converge to the only equilibrium strictly above \(U\), the right consensus \((S_1,\ldots,S_m)=(1,\ldots,1)\). The decreasing negative-barrier orbit similarly converges to the left consensus \((0,\ldots,0)\). Given any \(S(0)\geq U\) not equal to \(U\), strict comparison makes \(S(t_0)>U\) in all tail coordinates for any fixed \(t_0>0\). A sufficiently small positive barrier \(U+\varepsilon w\) lies below \(S(t_0)\). Comparison with its convergent trajectory and with the right consensus forces \(S(t)\to(1,\ldots,1)\). The reversed-order argument gives left consensus.

**5. Exact linear instability index.** At \(U\), the tail-coordinate Jacobian is the *symmetric* matrix
\[
J=H+\frac{2}{m(m+1)}\mathbf1\mathbf1^{\mathsf T},
\]
where \(H\) is the Dirichlet tridiagonal matrix with diagonal \(-1\) and nearest-neighbor entries \(1/2\). The matrix \(H\) is strictly negative definite, and \((-H)w=\mathbf1\). Consequently,
\[
\frac{2}{m(m+1)}\mathbf1^{\mathsf T}(-H)^{-1}\mathbf1
=\frac{m+2}{3}>1.
\]
Congruence by \((-H)^{-1/2}\) converts \(J\) into a negative identity plus a rank-one positive matrix, with exactly one positive and \(m-1\) negative inertia directions. Sylvester's law of inertia proves the eigenvalue assertion; hyperbolicity and the stable-manifold theorem give the local manifold dimensions.

## Verification

The standalone `check.py` uses exact rational arithmetic to reconstruct the tail equations, both strict barriers, their admissible probability masses, and the Jacobian identities for \(k=2,\ldots,16\). Its direct fourth-order Runge–Kutta reproducer integrates the two rational five-opinion witnesses. All checked identities and endpoint tests passed. This finite computation corroborates but does not replace the symbolic inequalities and comparison proof for every integer \(k\geq2\).

## Relationship to prior work

Cao and Gong [1] introduced this precise incremental voter rule, derived its nonlinear mean-field equations and characterized the three equilibria. They established symmetric-state convergence to the uniform equilibrium and two far-mean sufficient basin conditions, \(M(0)<1\) and \(M(0)>m-1\). They explicitly leave broad, nonsymmetric basin selection unresolved. The contribution here is a new explicit global basin certificate via first-order stochastic dominance, together with a complete local instability index at the uniform state. The standard order-preserving ODE principle is not new; the explicit cooperative tail transformation, strict sub- and supersolutions, and their consequence for this particular model are the asserted extension. Related earlier opinion models [2,3] use different microscopic update laws and do not directly yield these formulas.

## Limitations

Stochastic-order comparability with uniform is sufficient, not necessary: the result does not characterize initial distributions whose tails cross the uniform tails. It is confined to the mean-field model and does not give exact finite-population fixation probabilities, expected consensus times, or convergence rates. Global convergence from arbitrary nonsymmetric data remains open here. All originality statements are subject to the possibility of equivalent results in unindexed work; no independent scientific validation is claimed.

## References

[1] Fei Cao and Xiaoqian Gong, *The incremental voter model: mean-field analysis and convergence to equilibrium*, arXiv:2605.28984v1, first posted 2026-05-27. https://arxiv.org/html/2605.28984 ; https://arxiv.org/abs/2605.28984

[2] Fei Cao and Stephanie Reed, *The Iterative Persuasion-Polarization Opinion Dynamics and Its Mean-Field Analysis*, arXiv:2408.00148, SIAM J. Appl. Math. 85 (2025), 1596–1620. https://arxiv.org/abs/2408.00148 ; https://doi.org/10.1137/24M1700661

[3] Fei Cao and Roberto Cortez, *Fractal Opinions among Interacting Agents*, arXiv:2408.01624, SIAM J. Appl. Dyn. Syst. 24 (2025), 1529–1552. https://arxiv.org/abs/2408.01624 ; https://doi.org/10.1137/24M1682269
