# A sharp two-point reset-clock transition for finite-width Gaussian cycles

## Finding

For a one-dimensional Ornstein–Uhlenbeck relaxation repeatedly restarted from a fixed centered Gaussian state of strictly smaller variance, the conditional endpoint symmetric Kullback–Leibler divergence has a unique change from convexity to concavity. This curvature change determines **the complete maximizing renewal-clock law at a prescribed average interval** and minimum admissible interval.

Let \(\lambda,D>0\), \(0<q<1\), \(\omega=2\lambda\), and \(c=(1-q)/q\). For \(t\geq0\) set
\[
y(t)=1-e^{-\omega t},\qquad f(t)=\frac{c^2}{2}\frac{y(t)^2}{1+c y(t)}.\]
Write \(t_{\rm inf}\) for the sole inflection time of \(f\). Given a positive minimum reset interval \(\delta>0\), the sharp optimization of \(\mathbb E[f(T)]/\mathbb E[T]\) over **every** independent, identically distributed renewal waiting time \(T\geq\delta\) with \(\mathbb E[T]=\mu\geq\delta\) is as follows.

If \(\delta\geq t_{\rm inf}\), the unique optimal law is the deterministic clock \(T=\mu\). If \(0<\delta<t_{\rm inf}\), there is exactly one \(b_\delta>t_{\rm inf}\) satisfying
\[
(b_\delta-\delta)f'(b_\delta)=f(b_\delta)-f(\delta).
\]
For \(\delta<\mu<b_\delta\), the **unique** maximizing clock has
\[
\Pr(T=\delta)=\frac{b_\delta-\mu}{b_\delta-\delta},\qquad
\Pr(T=b_\delta)=\frac{\mu-\delta}{b_\delta-\delta}.
\]
Its divergence rate is strictly greater than the rate of deterministic resetting at the same mean interval. For \(\mu\geq b_\delta\) (and at the endpoint \(\mu=\delta\)) the unique maximizer is the deterministic clock \(T=\mu\). Thus the exact parameter condition for a genuinely random optimal clock is \(0<\delta<t_{\rm inf}\) and \(\delta<\mu<b_\delta\).

The inflection point is not a numerical convention: putting \(y_\mathrm{inf}=1-e^{-\omega t_{\rm inf}}\), it is the unique root in \((0,1)\) of
\[
2-4y_\mathrm{inf}-3c y_\mathrm{inf}^2-c^2 y_\mathrm{inf}^3=0.
\]
The tangency threshold \(b_\delta\) decreases strictly as \(\delta\) increases toward \(t_{\rm inf}\), and converges to \(t_{\rm inf}\). As \(\delta\downarrow0\), it converges to the unique positive maximizer of \(f(t)/t\).

## Assumptions and scope

Between resets, \(X\) satisfies \(dX_t=-\lambda X_t\,dt+\sqrt{2D}\,dB_t\). Each reset draws a new independent \(X_0\sim\mathcal N(0,qD/\lambda)\), and resets occur after independent copies of \(T\), independent of Brownian noise and reset draws. The admissible renewal laws are all probability measures on \([\delta,\infty)\) with finite prescribed mean \(\mu\geq\delta\), without a density or moment assumption beyond that mean. The reset operation is modeled as instantaneous, and the minimum interval \(\delta\) constrains the time *between* reset events, not an implementation duration.

Conditional on an interval \(t\), the pre-reset Gaussian has variance
\[
\sigma_t^2=\frac D\lambda\big[1-(1-q)e^{-\omega t}\big],\qquad
\sigma_c^2=\frac{qD}{\lambda}.
\]
The reward \(f(t)\) is the **symmetric endpoint relative entropy in nats**
\[
f(t)=D_{\rm KL}\big(\mathcal N(0,\sigma_t^2)\,\|\,\mathcal N(0,\sigma_c^2)\big)
+D_{\rm KL}\big(\mathcal N(0,\sigma_c^2)\,\|\,\mathcal N(0,\sigma_t^2)\big).
\]
It is not asserted to be the full physical pathwise entropy production or the work required by a particular resetting device. Its long-run conditional endpoint-divergence reward per unit time is the renewal-reward value \(\mathcal R(T)=\mathbb E[f(T)]/\mu\).

## Proof

**1. Gaussian reward identity.** The Ornstein–Uhlenbeck variance formula above follows by solving \(v'(t)=-2\lambda v(t)+2D\), \(v(0)=qD/\lambda\). For centered one-dimensional normal distributions with variance ratio \(z\), the sum of the two directed KL divergences equals \((z+z^{-1}-2)/2\). Here \(z=1+c(1-e^{-\omega t})\); substitution yields the displayed \(f(t)\). In particular, \(f(0)=f'(0)=0\), \(f'(t)>0\) for every \(t>0\), and \(f(t)\uparrow c^2/[2(1+c)]<\infty\).

**2. A unique curvature change.** Put \(y=1-e^{-\omega t}\), so \(0<y<1\) when \(t>0\). Differentiating without an asymptotic approximation gives
\[
f'(t)=\frac{c^2\omega}{2}\frac{(1-y)y(2+cy)}{(1+cy)^2},
\]
\[
f''(t)=\frac{c^2\omega^2}{2}\frac{1-y}{(1+cy)^3}\big(2-4y-3cy^2-c^2y^3\big).
\]
The cubic in parentheses is strictly decreasing on \([0,1]\), begins at \(2\), and ends at \(-2-3c-c^2\). Consequently it has exactly one zero \(y_{\rm inf}\in(0,1)\). The curvature is strictly positive before \(t_{\rm inf}\) and strictly negative afterward; there is no second inflection or missing boundary case.

**3. Unique tangent from the minimum interval.** Fix \(0<\delta<t_{\rm inf}\) and set
\[
h_\delta(t)=(t-\delta)f'(t)-f(t)+f(\delta),\qquad t>\delta.
\]
Then \(h_\delta(\delta)=0\) and \(h_\delta'(t)=(t-\delta)f''(t)\). Hence \(h_\delta\) increases strictly up to \(t_{\rm inf}\) and decreases strictly thereafter. It is positive at \(t_{\rm inf}\), whereas \(\lim_{t\to\infty}h_\delta(t)=-[f(\infty)-f(\delta)]<0\), because \(tf'(t)\to0\). There is exactly one root \(b_\delta>t_{\rm inf}\). The secant slope \((f(t)-f(\delta))/(t-\delta)\) is strictly increasing up to \(b_\delta\) and strictly decreasing afterward. It follows that the line through \((\delta,f(\delta))\) tangent at \(b_\delta\) lies strictly above \(f(t)\) at all interior points \(\delta<t<b_\delta\).

**4. Exact concavification and attainment.** Define
\[
\widehat f_\delta(t)=
\begin{cases}
f(\delta)+(t-\delta)\dfrac{f(b_\delta)-f(\delta)}{b_\delta-\delta},&\delta\leq t\leq b_\delta,\\
f(t),&t\geq b_\delta.
\end{cases}
\]
The tangency equation makes the two pieces continuously differentiable. The first piece is linear and the second is strictly concave; thus \(\widehat f_\delta\) is concave on \([\delta,\infty)\) and dominates \(f\). For any admissible \(T\), Jensen's inequality yields
\[
\mathbb E[f(T)]\leq\mathbb E[\widehat f_\delta(T)]\leq\widehat f_\delta(\mathbb E[T])=\widehat f_\delta(\mu).
\]
When \(\delta<\mu<b_\delta\), equality is attained by the stated two-atom law with mean \(\mu\). It is the only equality case: \(\widehat f_\delta>f\) inside \((\delta,b_\delta)\), and the concave envelope has no other linear segment. For \(\mu>b_\delta\), strict concavity to the right and the common tangent imply equality only at \(T=\mu\); the same holds at the endpoints. If \(\delta\geq t_{\rm inf}\), \(f\) is strictly concave on \((\delta,\infty)\) and ordinary strict Jensen proves deterministic uniqueness. Dividing by the fixed \(\mu\) completes the optimization. The renewal-reward theorem identifies this ratio with the long-run reward rate, since intervals are iid, \(\mathbb E T=\mu<\infty\), and \(f\) is bounded.

**5. Dependence on the minimum interval.** For \(0<\delta<t_{\rm inf}\), the root is simple because \(\partial_t h_\delta(b_\delta)=(b_\delta-\delta)f''(b_\delta)<0\). At this root, the maximum secant slope is strictly larger than \(f'(\delta)\), so \(\partial_\delta h_\delta(b_\delta)=f'(\delta)-f'(b_\delta)<0\). Implicit differentiation therefore gives \(db_\delta/d\delta<0\). By monotonicity and continuity, \(b_\delta\to t_{\rm inf}\) as \(\delta\uparrow t_{\rm inf}\). As \(\delta\downarrow0\), the tangency condition becomes \(t f'(t)=f(t)\); the same single-change derivative argument proves this has exactly one strictly positive root, which is the unique maximum of \(f(t)/t\).

## Verification

The standalone `CHECK.py` evaluates the analytic derivative and cubic-inflection expressions, finds tangencies by bracketing, checks concave majorization across a deterministic grid, and compares the predicted optimum against thousands of feasible two-point competitors. It executes without nonstandard Python libraries. In the included run, it passed 11,424 deterministic checks.

For \(c=1\), \(\omega=1\), \(\delta=0.2\), and \(\mu=0.4\), the inflection and tangency times are
\[
t_{\rm inf}=0.476096875631\ldots,\qquad b_\delta=0.661755102085\ldots.
\]
The optimal two-point law gives probability \(0.433130027361\ldots\) to the longer interval. It increases the endpoint-divergence reward rate over deterministic \(T=0.4\) by \(2.9509253746\ldots\) percent. These finite checks and decimals are illustrative, not the source of the universal proof.

## Relationship to prior work

Farago (arXiv:2605.28445, first released May 27, 2026) formulated the harmonic Gaussian resetting-cycle endpoint KL comparison and analyzed periodic and Poisson resetting, including limiting-rate expressions. The Gaussian endpoint formula and the thermodynamic motivation are prior work. The claim here is the **complete fixed-mean optimization over all renewal interval distributions subject to a positive minimum interval**, its unique stochastic-to-deterministic optimizer transition, and its parameter-exact tangency boundary.

Olsen, Gupta, Mori, and Krishnamurthy (arXiv:2310.11267; Phys. Rev. Research 6, 033343, 2024) analyze work incurred by finite-time resetting traps and permit arbitrary waiting-time distributions, but their cost objective and physical control variables differ. Gupta, Olsen, and Krishnamurthy (Communications Physics 8, 355, 2025) optimize finite-time trap-stiffness protocols and actual work, not fixed-mean renewal laws maximizing conditional Gaussian endpoint symmetric KL. Mori, Olsen, and Krishnamurthy (Phys. Rev. Research 5, 023103, 2023) study stochastic entropy production under position-distributed resets, a distinct pathwise observable.

The use of concave envelopes and Jensen's inequality is classical optimization machinery. This proof does not claim those methods as new. The asserted mathematical specialization consists of the **unique cubic curvature transition of this specific physical reward**, the resulting full clock classification, and the explicit critical tangency equations. Published statements known to cover periodic/Poisson clock comparisons, as well as analogous first-passage restart objectives, do not themselves determine this constrained optimum.

## Limitations

The optimized quantity is a conditional endpoint Jeffreys divergence per time, **not** a statement about total dissipation, path-space entropy production, finite-time mechanical work, or a fully specified physical reset apparatus. The reset draw is independent and instantly achieves the specified Gaussian width; actual mechanisms with state-dependent cost, positive duration, or carryover memory can have a different optimum. The minimum admissible interarrival time is an explicit modeling constraint. The result proves a global optimum within iid renewal laws of prescribed finite mean, not for feedback clocks depending on the observed trajectory. As usual, exhaustive prior-art coverage cannot be guaranteed from the searched sources; a broad pre-existing concavification theorem specialized to this reward might reduce publication-level novelty.

## References

1. O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression*, arXiv:2605.28445 (first submitted May 27, 2026), https://arxiv.org/html/2605.28445v1.
2. K. Stølevik Olsen, D. Gupta, F. Mori, and S. Krishnamurthy, *Thermodynamic cost of finite-time stochastic resetting*, Phys. Rev. Research 6, 033343 (2024), arXiv:2310.11267, https://arxiv.org/html/2310.11267v5.
3. D. Gupta, K. Stølevik Olsen, and S. Krishnamurthy, *Thermodynamic cost of recurrent erasure*, Communications Physics 8, 355 (2025), https://www.nature.com/articles/s42005-025-02277-w.
4. F. Mori, K. Stølevik Olsen, and S. Krishnamurthy, *Entropy production of resetting processes*, Phys. Rev. Research 5, 023103 (2023), https://doi.org/10.1103/PhysRevResearch.5.023103.
5. M. R. Evans and S. Ray, *Stochastic resetting prevails over sharp restart for broad target distributions*, arXiv:2410.01941 (2024), https://arxiv.org/abs/2410.01941 (different objective: first-passage completion time).
