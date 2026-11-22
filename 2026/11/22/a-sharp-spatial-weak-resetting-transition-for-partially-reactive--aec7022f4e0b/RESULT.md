# A sharp spatial weak-resetting transition for partially reactive run-and-tumble search

## Finding
For a one-dimensional persistent particle between two *sticky reflecting* outer walls and one partially reactive central target, infinitesimal complete Poisson restarting has a **sharp, single-crossing spatial benefit diagram**. Let \(s=\lambda L/v>0\), \(k=\kappa/(\lambda L)>0\), \(a=|x_0|/L\in(0,1]\), and \(c=\coth(ks/2)>1\). Set
\[
P(s)=3-6s^2-4s^3,\qquad Q(s)=6s^2+4s^3+2s^4.
\]
There is exactly one positive solution \(s_*(k)\) to
\[
\coth(ks/2)P(s)=Q(s).
\]
With every restart returning the particle to \(x_0\) and independently selecting either heading with probability \(1/2\), the mean first reaction time responds to a *small positive* restart rate as follows:

- If \(0<s<s_*(k)\), restarting strictly **reduces** the mean for every \(a\in(0,1]\).
- If \(s=s_*(k)\), the first derivative is strictly improving for \(0<a<1\), and equals zero for \(a=1\) (no second-order assertion at this equality).
- If \(s>s_*(k)\), there is one and only one \(a_c(s,k)\in(0,1)\) such that restarting strictly improves the mean for \(0<a<a_c\), but strictly **worsens** it for \(a_c<a\le1\); the first derivative vanishes at the unique transition \(a=a_c\).

The threshold \(s_*(k)\) is strictly decreasing in \(k\). Its weak- and strong-target limits are \(s_0=0.5979116727228\ldots\), the unique positive root of \(P(s)=0\), and \(s_\infty=0.4349478725414\ldots\), the unique positive root of \(P(s)=Q(s)\). At \(k=1\), \(s_*=0.5363289996132\ldots\). In contrast, *uniformly distributed fresh starting points* always make small restarting beneficial, for every \(s,k>0\).

## Assumptions and scope
The particle moves in \([-L,L]\) at constant speed \(v>0\) with direction \(\sigma\in\{-1,+1\}\), reversed after independent exponential times of rate \(\lambda>0\). At either outer wall it remains attached when outward-facing until its next direction reversal (rate \(\lambda\)); this wall delay counts toward first-passage time. Every crossing of the target at zero reacts independently with probability \(p=1-e^{-\kappa/v}\in(0,1)\) and, otherwise, continues its current trajectory. The initial position is any fixed \(x_0\ne0\) with \(|x_0|\le L\); the initial heading is independent and symmetric. Restart times are independent Poisson events of rate \(\rho\ge0\), and each restart renews the entire physical state (position, heading, and the target's independent reaction randomization). The first reaction time with restarting is \(T_\rho\). All moments of \(T_0\) are finite because the state space is bounded, switching and crossing probabilities are positive, and geometric attempts have exponential tails.

Spatial folding \(x=|X|/L\in[0,1]\) turns the target into a partially absorbing, non-sticking boundary at zero and retains the sticky outer wall at one. The correct folded boundary condition for a moment of the remaining absorption time is that its inward-heading value at zero is \(q=e^{-ks}\) times its outward-heading value. This must not be confused with *instantaneous* reflection at the outer wall or wall-occupation killing.

## Proof
Scale physical time by \(\lambda^{-1}\): put \(U=\lambda T_0\). Let \(m_\pm(x)=\mathbb E_{x,\pm}[U]\) for the folded problem, \(f=(m_++m_-)/2\), \(g=(m_+-m_-)/2\). Here \(+\) points away from the target. The backward equations in the bulk and boundary conditions become
\[
g'=-s,\qquad f'=2sg,\qquad g(1)=\tfrac12,\qquad g(0)=\tanh(ks/2)f(0).
\]
Indeed an outward-facing particle at \(1\) waits an independent mean-one exponential time before resuming inward motion. Solving gives
\[
g(x)=s(1-x)+\tfrac12,\quad
f(x)=c(s+\tfrac12)+sx+s^2(2x-x^2).
\]
Let \(u_\pm(x)=\mathbb E_{x,\pm}[U^2]\), \(F=(u_++u_-)/2\), \(G=(u_+-u_-)/2\). The equations and conditions are
\[
G'=-2sf,\quad F'=2s(G-g),\quad
G(1)=1+f(1)-g(1),\quad F(0)=cG(0).
\]
The wall condition follows by squaring the decomposition of an outward-wall lifetime into an independent mean-one, second-moment-two exponential wait plus the inward lifetime; the target condition follows from the same independent capture Bernoulli variable for moments. Consequently these expressions determine the second moment uniquely:
\[
G(x)=1+f(1)-g(1)+2s\int_x^1 f(y)\,dy,
\quad F(x)=cG(0)+2s\int_0^x(G(y)-g(y))\,dy.
\]
For a symmetric initial heading, \(\mathbb E[U]=f(a)\), \(\mathbb E[U^2]=F(a)\). Define the dimensionless resetting susceptibility
\[
\Delta(a;s,k)=F(a)-2f(a)^2.
\]
For a complete independent renewal at rate \(R=\rho/\lambda\), if \(\phi(R)=\mathbb E(e^{-RU})\) then the usual renewal identity is
\[
\lambda\mathbb E T_\rho=\frac{1-\phi(R)}{R\phi(R)}
=f(a)-\tfrac12\Delta(a;s,k)R+O(R^2).
\]
Thus \(\Delta>0\) is exactly the condition that sufficiently weak restarting shortens mean time.

A direct polynomial expansion, reproduced symbolically by the accompanying checker, gives
\[
\Delta(1;s,k)=\frac{cP(s)-Q(s)}6,\qquad
\Delta(0;s,k)=\frac{c(8s^3+12s^2+6s+3)}6>0.
\]
Write the quartic in the degree-four Bernstein basis
\[
\Delta(a)=\sum_{j=0}^4\binom4j b_j a^j(1-a)^{4-j}.
\]
Its coefficients satisfy
\[
\begin{aligned}
b_0&=\frac{c(8s^3+12s^2+6s+3)}6>0,\\
b_1&=\frac{4cs^3+12cs^2+9cs+6c+8s^4+12s^3}{12}>0,\\
b_1-b_2&=\frac{s(8cs^2+10cs+3c+8s^3+4s^2+2s)}{12}>0,\\
b_2-b_3&=\frac{s(2s+1)(2cs+3c+2s^2+4s)}{12}>0,\\
b_3-b_4&=\frac{s(2cs+c+2s^2+2s)}4>0.
\end{aligned}
\]
For all \(c>1,s>0\), the ordered Bernstein list \((b_0,b_1,b_2,b_3,b_4)\) has at most one change of sign, starting positive. Under \(z=a/(1-a)>0\), its values correspond to positive zeros of \(\sum_{j=0}^4\binom4j b_j z^j\). Descartes' rule of signs therefore gives **at most one** interior zero of \(\Delta\), counted with multiplicity. If the endpoint value is nonnegative, all nonzero Bernstein coefficients are positive (including when \(b_4=0\)), so \(\Delta\) is positive in the open interval. If the endpoint value is negative, continuity and uniqueness give exactly one simple interior zero with the asserted sign orientation.

Finally, \(P(s)\) decreases strictly from three to negative infinity and has a unique positive root \(s_0\); \(Q(s)\) increases strictly from zero. On \((0,s_0)\), \(\coth(ks/2)P(s)\) strictly decreases from infinity to zero, hence crosses \(Q(s)\) exactly once. Beyond \(s_0\), the endpoint sign is negative. At fixed \(s>0\), \(\coth(ks/2)\) strictly decreases with \(k\), so the root strictly decreases. Pointwise \(\coth(ks/2)\to1\) as \(k\to\infty\) and diverges as \(k\downarrow0\), giving the two limiting roots by monotonicity and continuity.

For the uniform fresh reset law (position uniform on \([-L,L]\), heading fair), the corresponding susceptibility is
\[
\Delta_{\mathrm{unif}}=c\left(\frac{s^2}{3}+\frac s2+\frac12\right)+\frac{8s^4}{45}+\frac{s^3}2-\frac{s^2}6>0
\]
by \(c>1\). This is a corollary, not a separate originality claim.

## Verification
Run `python check.py` with Python 3, SymPy, SciPy, and NumPy installed. It reconstructs both backward moment equations; independently reproduces the existing published uniform-start variance (Jeon–Go–Kim, Eq. 113); checks the quartic's Bernstein coefficients and endpoint formulas by symbolic identities; tests numerical root ordering and the one-zero diagram across several physical parameters. The delivered checker reports 61 passed analytic/polynomial assertions. Numerical root and finite tests support, but are not substitutes for, Descartes' rule and monotonicity in the proof. Separate direct event-driven trajectories were compared to moment formulas during preparation; they are stochastic spot-checks, not certified bounds or infinite proofs.

## Relationship to prior work
Jeon, Go and Kim (arXiv:2310.04016, submitted 2023-10-06) define the same finite-interval sticky-wall/interior-target dynamics and derive its uniform-launch mean and variance, including their Eq. 113. Those results are explicitly **not** claimed new. Their article studies optimal self-propulsion speed and filtering, rather than renewal restarting to an arbitrary fixed launch point and its universal unique spatial crossover. Bressloff (arXiv:2209.07293) supplies boundary-reactive RTP propagators with an instantly reflecting opposite wall, not this sticky-wall point-target weak-reset diagram. Bressloff (arXiv:2302.01158) treats sticky walls that themselves absorb particles, which changes the absorption mechanism. Bressloff (arXiv:2503.01304) studies resetting and a partially absorbing boundary on a **half-line**, including nonrenewal local-time protocols; it does not establish this bounded sticky-reflection, center-target Bernstein single-crossing. The general Poisson restart renewal expansion is standard and is used only as a step. No assertion of exhaustive literature coverage is made.

## Limitations
Only infinitesimal restart rates are classified; the result does not assert a globally optimal positive rate, and a zero first derivative does not determine the finite-rate behavior. The process is one-dimensional, stationary in its physical parameters, driftless in the bulk, has two Poisson velocity states, exponential sticky-wall holding, and independently renewed, fixed per-crossing capture probability. Other reflection, partial-velocity, refractory, nonrenewal, or multidimensional mechanisms are not covered. The statewise sign diagram is not a proof of uniqueness relative to all unindexed literature; a conceptually equivalent alternative treatment could exist.

## References
1. E. Jeon, B. Go, Y. W. Kim, *Searching for a partially absorbing target by a run-and-tumble particle in a confined space*, arXiv:2310.04016v1 (2023-10-06), https://arxiv.org/html/2310.04016v1, especially Sections II–III and Appendices A–C.
2. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle*, arXiv:2209.07293 (2022), https://arxiv.org/html/2209.07293v2.
3. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle II: absorption at sticky boundaries*, arXiv:2302.01158 (2023), https://arxiv.org/html/2302.01158v1.
4. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle with stochastic resetting*, arXiv:2503.01304 (2025), https://arxiv.org/html/2503.01304v1.
