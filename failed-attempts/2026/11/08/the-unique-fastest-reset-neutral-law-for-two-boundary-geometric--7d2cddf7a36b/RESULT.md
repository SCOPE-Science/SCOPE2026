# The unique fastest reset-neutral law for two-boundary geometric resetting

## Finding

Fix any integer \(a\ge4\), right-step probability \(0<p<1\), and geometric reset probability \(0<\gamma<1\). Of **all** reset distributions on interior sites whose left/right absorption ratio is independent of \(\gamma\) for every reset rate, exactly one minimizes the mean absorption time from *every* fixed interior starting site: the mirror-symmetric **edge pair**, supported on \(\{1,a-1\}\) with the bias-compensated weights
\[
\pi^*_1=\frac{\lambda^{a-2}}{1+\lambda^{a-2}},\qquad
\pi^*_{a-1}=\frac1{1+\lambda^{a-2}},\qquad
\lambda=\sqrt{\frac{1-p}{p}}.
\]
(When \(a=2\), the two displayed sites coincide; the stated nontrivial uniqueness and latency comparison concern \(a\ge4\).)

Write \(q=1-p\), \(d=1-\gamma\), \(A=a/2\),
\[
\theta=|\log\lambda|,\qquad
k=\operatorname{arcosh}\left(\frac1{2d\sqrt{pq}}\right)>\theta,
\qquad
s_i=\mathbb E_i[d^\tau],
\]
where \(\tau\) is the first boundary-hitting time of the *unreset* walk. For a neutral policy concentrated on any mirror pair \(\{z,a-z\}\), \(1\le z\le\lfloor a/2\rfloor\), its first-cycle absorption probability is exactly
\[
S_z=\frac{\cosh(\theta A)}{\cosh(kA)}
\frac{\cosh(k(A-z))}{\cosh(\theta(A-z))},
\]
with the usual singleton midpoint convention. The strict ordering \(S_1>S_2>\cdots>S_{\lfloor a/2\rfloor}\) implies the unique optimality above. For any starting state \(i\in\{1,\dots,a-1\}\),
\[
\boxed{\mathbb E_i[T_{\pi^*}]=\frac{1-s_i}{\gamma S_1}.}
\]
The reset-started mean is \(\mathbb E_{\pi^*}T=(1-S_1)/(\gamma S_1)\).

When \(a\) is even, the alternative neutral rule that always resets to the midpoint gives a sharply different transport scale. Holding \(p,\gamma\) fixed as \(a\to\infty\) through even integers,
\[
\mathbb E_{\pi^*}T\longrightarrow\frac{e^{k-\theta}-1}{\gamma},
\qquad
\lim_{a\to\infty}\frac1a\log
\frac{\mathbb E_{a/2}[T_{\text{mid}}]}{\mathbb E_{\pi^*}T}
=\frac{k-\theta}{2}>0.
\]
These two means refer to **fresh draws from their respective reset distributions**, not the same starting site. Both policies nevertheless have exactly the same left-absorption probability after reset,
\[C^*=\frac{\lambda^a}{1+\lambda^a},\]
for every \(0<\gamma<1\).

## Assumptions and scope

The finite walk occupies sites \(\{0,1,\ldots,a\}\); \(0\) and \(a\) are absorbing. A nonabsorbed walker, before each unit-time ordinary step, either resets instantly to an independent draw from a fixed distribution \(\pi\) on \(\{1,\ldots,a-1\}\) with probability \(\gamma\), or steps right with probability \(p\) / left with probability \(q=1-p\), together with probability \(1-\gamma\). An event (reset or ordinary move) consumes one unit of elapsed time. This timing convention matters to the exact mean. The reset law is independent of the reset rate and the process's past. The term *reset-neutral* means the probability of eventual absorption at the left endpoint **when initialized from \(\pi\)** is constant over the entire open range of reset probabilities, not that it equals one half and not that starting from arbitrary \(i\) is rate independent.

The minimized quantity is unconditioned expected time to **either** absorbing endpoint, with \(p\) and \(\gamma\) held fixed. There are no costs for changing reset location or for an instantaneous relocation beyond the one unit counted for its event. The class of allowed distributions includes single-site midpoint mass when \(a\) is even, and zero weights at other sites. The assertion does not optimize \(\gamma\), location-dependent restarting probabilities, or an externally constrained relocation cost.

## Proof

**1. Discounted boundary fluxes.** Let \(u_i=\mathbb E_i[d^\tau\mathbf1_{\{X_\tau=0\}}]\) and \(v_i=\mathbb E_i[d^\tau\mathbf1_{\{X_\tau=a\}}]\), so \(s_i=u_i+v_i\). They solve \(f_i=d(pf_{i+1}+qf_{i-1})\) on interior sites with the respective absorbing boundary data. The two characteristic roots are \(\lambda e^{\pm k}\). Consequently, for every \(1\le i<a\),
\[
 u_i=\frac{\lambda^i\sinh(k(a-i))}{\sinh(ka)},\qquad
 v_i=\frac{\lambda^{i-a}\sinh(ki)}{\sinh(ka)}.
\]
Since \(2\sqrt{pq}\le1\) and \(0<d<1\), \(k>\theta\ge0\) including at \(p=q=1/2\). Every \(u_i,v_i,s_i\) is positive.

**2. Exhaustive description of neutral reset laws.** Put \(U_\pi=\sum_i\pi_i u_i\), \(V_\pi=\sum_i\pi_i v_i\), \(S_\pi=U_\pi+V_\pi\). The renewal equation says the left absorption probability after starting from a reset draw is \(C_\pi=U_\pi/S_\pi\). If it is constant in \(\gamma\), then \(V_\pi=R U_\pi\) for a constant \(R>0\). As \(\gamma\) ranges over \((0,1)\), the corresponding \(k\) ranges over a nonempty open interval of positive real numbers. Substitute the displayed hyperbolic functions, multiply by \(2\sinh(ka)\), and compare coefficients of the linearly independent exponentials \(e^{kj}\) for \(j=1,\ldots,a-1\). For each \(j\), the equality of coefficients forces
\[
\pi_j\lambda^{j-a}=R\pi_{a-j}\lambda^{a-j},
\quad\text{or}\quad \pi_j=R\lambda^{2a-2j}\pi_{a-j}.
\]
At least one mirror pair has positive total mass; applying the identity at both mirror sites therefore gives \(R^2\lambda^{2a}=1\), hence \(R=\lambda^{-a}\). Thus every neutral law, and only those laws, satisfy
\[
\pi_j=\lambda^{a-2j}\pi_{a-j}\quad(1\le j<a),
\qquad C_\pi=\frac1{1+R}=\frac{\lambda^a}{1+\lambda^a}.
\]
The sufficiency follows by inserting these relations into the explicit fluxes. It follows that the complete feasible family is the probability simplex of disjoint mirror-pair laws \(\eta_z\), with any unpaired midpoint as a singleton vertex when \(a\) is even. Each strict pair has weights \(\lambda^{a-2z}/(1+\lambda^{a-2z})\) and its complementary weight. This is the neutral-family structure underlying the source's spectral-duality results; it is restated explicitly to make the optimization exhaustive.

**3. Exact pair-cycle success.** Set \(t=A-z\ge0\) and \(L=\log\lambda\). The mirror weights are \(e^{Lt}/(2\cosh(Lt))\) and \(e^{-Lt}/(2\cosh(Lt))\), interpreted as one midpoint mass when \(t=0\). Symmetrically averaging the formulas in step 1 yields
\[
 U_{\eta_z}=\frac{\lambda^A\cosh(kt)}{2\cosh(kA)\cosh(Lt)},\qquad
 V_{\eta_z}=\frac{\lambda^{-A}\cosh(kt)}{2\cosh(kA)\cosh(Lt)}.
\]
Adding gives the displayed \(S_z\). For \(t>0\),
\[
\frac{d}{dt}\log\left[\frac{\cosh(kt)}{\cosh(\theta t)}\right]
=k\tanh(kt)-\theta\tanh(\theta t)>0.
\]
Indeed \(\xi\mapsto\xi\tanh(\xi t)\) is strictly increasing for \(\xi>0\), while \(k>\theta\). Therefore smaller \(z\) gives strictly larger \(S_z\); because \(S_\pi\) is affine in the simplex coordinates, \(S_1\) is its **unique** maximum, with no additional mixed maximizers.

**4. Mean-time renewal with the event-count convention.** For the unreset absorption time \(\tau\), the mean length of the first cycle (reset or absorption) from \(i\) is
\[
 w_i=\sum_{n\ge0}d^n\Pr_i(\tau>n)=\frac{1-s_i}{\gamma}.
\]
A cycle restarts with probability \(1-s_i\); averaging over a fresh reset draw shows
\[
\mathbb E_\pi T=\frac{1-S_\pi}{\gamma S_\pi},
\qquad
\mathbb E_i T=w_i+(1-s_i)\mathbb E_\pi T
=\frac{1-s_i}{\gamma S_\pi}.
\]
The numerator is independent of \(\pi\), and positive for every interior start. The unique maximizer \(S_1\) consequently uniquely minimizes every \(\mathbb E_iT\) and the reset-started mean.

**5. Asymptotic separation.** For even \(a\), midpoint resetting gives \(S_{a/2}=\cosh(\theta a/2)/\cosh(ka/2)\), with logarithm \(-(k-\theta)a/2+O(1)\). At the edge, \(t=a/2-1\) and the paired formula gives \(S_1\to e^{-(k-\theta)}\in(0,1)\), including \(\theta=0\). Substitution in the mean formulas proves the two limits, completing the proof.

## Verification

The accompanying `checker.py` evaluates finite absorbing Markov chains with exact rational algebra, including neutral splitting, mean absorption from each interior site, strict edge-pair dominance and mixtures; it additionally checks the hyperbolic formula numerically and tests the large-interval logarithmic rate. Run `python checker.py` with Python 3, SymPy and NumPy installed. A successful run reports `PASS 3666 independent exact and numerical assertions`. The proof above, rather than the finite checks, establishes all claims for every allowed interval, bias and reset probability.

For example, at \(a=10\), \(p=0.6\), \(\gamma=0.5\), starting each clock from its own reset distribution, the exact formulas give mean time approximately \(4.602142383\) for the edge pair and \(520.181818182\) for midpoint resetting, while the left-absorption probability after a reset is \(0.1163636364\) in both cases.

## Relationship to prior work

Vega Coso (2026, arXiv:2605.00657v1) establishes the exact two-boundary resetting model, the discounted absorption-channel renewal formula and the reflection-pair reset-neutrality condition, including the bias-dependent pair weights and neutral splitting probability. **None of those components is claimed as new here.** The contribution is a complete strict optimization of the *absorption time* over the whole neutral simplex, its hyperbolic monotonicity identity and the exponential-vs-bounded latency contrast.

Evans and Majumdar (2011) study optimal resetting distributions in Brownian single-target search; Julián-Salgado, Dagdug and Boyer (2023) study two-site resetting in half-line Brownian search; Méndez, Flaquer-Galmés and Campos (2024) study random reset positions for Brownian first-passage times; Julián-Salgado and coauthors (2026) study multi-site resets to a single absorbing target on a ring and optimize reset **rate**. Those works motivate the question and supply general renewal methods, but their theorems neither impose the all-rate two-boundary neutral-splitting constraint nor prove the unique discrete edge-pair optimizer. Generic renewal convexity alone gives reduction to simplex vertices, not the strict ordering of their discounted absorption probabilities.

## Limitations

The optimization applies only within reset-neutral laws for **every** reset probability, not within arbitrary reset laws and not at a single prescribed neutrality rate. Only constant-rate, iid, instantaneous resetting and unit-time events are included. Per-reset relocation distance and boundary-specific penalties are not modeled, so the fastest law could change under realistic relocation costs. The result does not assert statistical novelty as a mathematical guarantee: a prior unindexed mean-time specialization or more general comparison theorem could potentially dominate it. No independent external mathematical audit has been performed.

## References

1. J. A. Vega Coso, *Spectral Duality and Reset-Neutral Distributions in Random Walks with Multi-Site Geometric Resetting* (first public version 2026-05-01), https://arxiv.org/abs/2605.00657.
2. M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting* (2011), https://arxiv.org/abs/1107.4225.
3. P. Julián-Salgado, L. Dagdug and D. Boyer, *Diffusion with two resetting points* (2023), https://arxiv.org/abs/2311.11897.
4. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions* (2024), https://arxiv.org/abs/2401.01125.
5. P. Julián-Salgado, P. Castro-Villarreal, L. Dagdug and D. Boyer, *Mirror transitions in diffusion with stochastic resetting confined on a ring* (2026), https://arxiv.org/abs/2605.08414.
