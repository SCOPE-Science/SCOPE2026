# Exact marked-excursion decoupling and opposite endpoint selection in Brownian resetting

## Finding

**Theorem (marked threshold excursion and terminal capture).** Consider a Brownian particle on the positive half-line with generator \(D\partial_{xx}\), where \(D>0\), killed on its first visit to zero. At independent Poisson times of rate \(r>0\), its position is instantly replaced by an independent sample from a probability measure \(\mu\) supported in \([a,b]\), where \(0<a<b<\infty\) are the actual infimum and supremum of the support. Its initial position is independently sampled from the **same** measure \(\mu\). Put \(\kappa=\sqrt{r/D}\) and fix any threshold \(m>b\).

Let \(T\) be the absorption time, \(M=\sup_{0\le t\le T}X_t\), and \(H_m=\{M\ge m\}\). On \(H_m\), define \(U_m\) to be the *starting reset-location mark* of the first Brownian excursion that reaches \(m\). Define \(V_m\) to be the starting reset-location mark of the final excursion that ends in absorption at zero. (An excursion starts at time zero or immediately after a reset; the mark is its starting position, not its instantaneous location when a threshold is reached.) Define probability measures on \([a,b]\):

\[
\mu_\uparrow(dx)=\frac{\sinh(\kappa x)}{\int\sinh(\kappa z)\,\mu(dz)}\,\mu(dx),\qquad
\mu_\downarrow(dx)=\frac{e^{-\kappa x}}{\int e^{-\kappa z}\,\mu(dz)}\,\mu(dx).
\]

Then the **complete conditional joint law** is, for every measurable \(E,F\subseteq[a,b]\),

\[
\boxed{\begin{aligned}
\Pr(U_m\in E,V_m\in F\mid H_m)
={}&e^{-\kappa m}\,\mu_\uparrow(E\cap F)\\
&+(1-e^{-\kappa m})\,\mu_\uparrow(E)\mu_\downarrow(F).
\end{aligned}}
\]

In particular, the origin of the first threshold-reaching excursion has **exactly the same law** \(\mu_\uparrow\) for *all* thresholds \(m>b\). The terminal absorption-origin law conditioned on \(H_m\) is \(e^{-\kappa m}\mu_\uparrow+(1-e^{-\kappa m})\mu_\downarrow\). For any bounded real measurable test functions \(f,g\), the conditional covariance satisfies the exact identity

\[
\boxed{\operatorname{Cov}(f(U_m),g(V_m)\mid H_m)
=e^{-\kappa m}\operatorname{Cov}_{\mu_\uparrow}(f,g).}
\]

The total-variation distance between this conditional joint law and the independent product \(\mu_\uparrow\otimes\mu_\downarrow\) is at most \(e^{-\kappa m}\), with equality for any non-atomic \(\mu\). For every non-point-mass \(\mu\), \(\mu_\uparrow\) strictly dominates \(\mu_\downarrow\) in monotone-likelihood-ratio order; hence the origin of a threshold-reaching excursion is stochastically larger than the final absorbing origin, with strict inequality in expectations for bounded nondecreasing observables that are not \(\mu\)-almost surely constant.

**Endpoint boundary-layer classification.** Suppose further that \(\mu\) has a density \(w\) on \([a,b]\) with the asymptotics

\[
w(a+t)\sim c_-t^{\alpha-1},\qquad
w(b-t)\sim c_+t^{\beta-1}\quad(t\downarrow0),
\]

for \(c_-,c_+,\alpha,\beta>0\). For *any* selection of thresholds \(m_\kappa>b\), as \(\kappa\to\infty\), conditionally on \(H_{m_\kappa}\),

\[
\boxed{\left(\kappa(b-U_{m_\kappa}),\ \kappa(V_{m_\kappa}-a)\right)
\ \Longrightarrow\ (G_\beta,G_\alpha),}
\]

where \(G_\beta,G_\alpha\) are **independent Gamma variables** with respective shapes \(\beta,\alpha\) and unit rate. With arbitrary compactly supported \(\mu\), the unscaled marks instead converge jointly in probability to the opposite endpoints \((b,a)\); atoms at the endpoints lead to degenerate components rather than Gamma limits.

These formulas concern the *marked* histories of extreme excursions and eventual capture, not merely the marginal law of the maximum.

## Assumptions and scope

All reset epochs are independent of the Brownian motion and of all sampled reset positions. Every new excursion restarts with a fresh Brownian path and an independent exponential reset clock. The initial position follows \(\mu\), as do all subsequent reset positions; this equal-initial-law hypothesis is essential for the simple threshold-independent mark distribution. The threshold strictly exceeds the entire reset support, so a reset jump never itself reaches \(m\). Every fresh excursion has a probability at least \(e^{-\kappa b}>0\) of absorption before resetting, ensuring almost-sure finite termination and an almost-surely defined final mark. The event \(H_m\) has strictly positive probability for every finite \(m>b\).

A first visit to \(m\), a reset, and absorption are taken in chronological order; their time ties have probability zero. In the exceptional case that the particle, after first reaching \(m\), reaches zero without another reset, the two marks coincide by definition. The probability of this exceptional case is exactly \(e^{-\kappa m}\). The Gamma claim applies only to densities having the indicated genuine positive endpoint asymptotics; it is not asserted for arbitrary singular or oscillatory endpoint measures.

## Proof

**1. A killed-excursion boundary-value problem.** Let \(R\sim\operatorname{Exp}(r)\) be independent of a fresh Brownian motion started from \(x\in(0,m)\), and denote the first free hitting times of \(0,m\) by \(\tau_0,\tau_m\). The functions

\[
A_m(x)=\Pr_x(\tau_0<\tau_m\wedge R),\qquad
B_m(x)=\Pr_x(\tau_m<\tau_0\wedge R)
\]

solve \(Df''=rf\) on \((0,m)\) with boundary values \((1,0)\) and \((0,1)\), respectively. Solving the two Dirichlet problems yields

\[
A_m(x)=\frac{\sinh(\kappa(m-x))}{\sinh(\kappa m)},\qquad
B_m(x)=\frac{\sinh(\kappa x)}{\sinh(\kappa m)}.
\]

Set \(C_m(x)=1-A_m(x)-B_m(x)\), the probability that the reset clock rings before either boundary. The denominator \(\sinh(\kappa m)\) is positive since \(r,m>0\); all three quantities are probabilities and their cases are exhaustive.

**2. The mark of the first threshold-reaching excursion.** Write \(\bar A=\int A_m\,d\mu\), \(\bar B=\int B_m\,d\mu\), and \(\bar C=1-\bar A-\bar B\). A history in which exactly \(n\ge0\) excursions reset without touching either boundary, followed by an excursion starting in \(E\) that first touches \(m\), has probability

\[
\bar C^{\,n}\int_E B_m(x)\,\mu(dx).
\]

These are disjoint histories, and \(\bar A+\bar B>0\), so the sum is an actual geometric series. Therefore

\[
\Pr(H_m,U_m\in E)
=\frac{\int_EB_m\,d\mu}{\bar A+\bar B},\qquad
\Pr(H_m)=\frac{\bar B}{\bar A+\bar B}.
\]

Division gives \(\Pr(U_m\in E\mid H_m)=\int_E B_m\,d\mu/\bar B=\mu_\uparrow(E)\). The factor \(1/\sinh(\kappa m)\) cancels, proving **exact threshold independence** throughout \(m>b\). In particular, this result does not follow simply by conditioning on the distribution of the maximum: it records the spatial mark of the winning excursion.

**3. The mark of an eventually successful absorption cycle.** On the unbounded half-line, the probability that an excursion from \(x>0\) reaches zero before its reset clock equals \(\mathbb E_x e^{-r\tau_0}=e^{-\kappa x}\), the unique bounded solution of \(Df''=rf\), \(f(0)=1\), \(f(\infty)=0\). Repeating i.i.d. excursions until the first absorption, the final excursion's starting mark consequently has distribution \(\mu_\downarrow\). This is true starting from a fresh independent draw from \(\mu\) after any reset; the number of preceding failed excursions changes neither its law nor the normalization.

**4. Strong Markov splitting at the first threshold visit.** On \(H_m\), let \(\sigma_m\) be the first visit to \(m\), whose corresponding cycle origin is \(U_m\). By the Brownian strong Markov property and exponential memorylessness, from position \(m\) the probability of absorbing at zero before another reset is exactly \(h_m=e^{-\kappa m}\). With this probability the final origin remains \(U_m\), so \(V_m=U_m\). With complementary probability there is at least one further reset; the very next reset samples an independent \(\mu\)-distributed position and starts a new search whose eventual successful absorption mark is \(\mu_\downarrow\), independent of \(U_m\). Consequently

\[
\mathcal L(U_m,V_m\mid H_m)
=h_m\,\mathcal L(Z,Z)_{Z\sim\mu_\uparrow}
+(1-h_m)(\mu_\uparrow\otimes\mu_\downarrow).
\]

This proves the announced joint law. Expanding \(\mathbb E[f(U_m)g(V_m)]\) and subtracting its marginal-product expectation cancels the independent part and gives exactly \(h_m\operatorname{Cov}_{\mu_\uparrow}(f,g)\). The total-variation bound follows from the mixture, while in the non-atomic case the diagonal measure is singular to the product, giving equality. This establishes the quantitative dependence statement without assuming Gaussianity or using finite-state experimentation.

**5. Strict spatial ordering.** On the common support of \(\mu\), the Radon–Nikodym derivative satisfies

\[
\frac{d\mu_\uparrow}{d\mu_\downarrow}(x)
=\frac{\int e^{-\kappa z}\,\mu(dz)}{\int\sinh(\kappa z)\,\mu(dz)}
\,e^{\kappa x}\sinh(\kappa x)
=K\,(e^{2\kappa x}-1),\qquad K>0.
\]

It is strictly increasing in \(x>0\). For any bounded nondecreasing observable \(f\) the expectation difference \(\int f\,d\mu_\uparrow-\int f\,d\mu_\downarrow\) is the covariance of \(f\) and this derivative under \(\mu_\downarrow\). Writing that covariance as half the expected product of the two differences at independent points shows it is nonnegative, and strictly positive if \(f\) is not \(\mu_\downarrow\)-almost surely constant: the product is positive whenever the two \(f\)-values differ. Since \(\mu_\downarrow\) and \(\mu\) are equivalent, this is precisely the nonconstancy condition stated above. The conditional terminal law is \(h_m\mu_\uparrow+(1-h_m)\mu_\downarrow\) with \(0<h_m<1\), so the strict expectation difference against the terminal law is \(1-h_m\) times that against \(\mu_\downarrow\).

**6. Opposite endpoint Gamma laws.** For an arbitrary compactly supported law with genuine support endpoints \(a,b\), elementary Laplace concentration shows \(\mu_\downarrow\Rightarrow\delta_a\) and \(\mu_\uparrow\Rightarrow\delta_b\). For example, every neighborhood of \(b\) has positive \(\mu\)-mass by the definition of the support, while the contribution from \([a,b-\varepsilon]\) to \(\int\sinh(\kappa x)\,d\mu\) is exponentially smaller than that from a fixed sufficiently narrow interval immediately below \(b\). The lower endpoint statement is analogous. The mixture parameter \(h_{m_\kappa}\le e^{-\kappa b}\to0\); therefore the conditional joint law converges to \(\delta_b\otimes\delta_a\).

Under the stated density asymptotics, one-sided Laplace's method gives

\[
\int e^{-\kappa x}\,\mu(dx)
\sim c_-\Gamma(\alpha)e^{-\kappa a}\kappa^{-\alpha},\qquad
\int\sinh(\kappa x)\,\mu(dx)
\sim\tfrac12c_+\Gamma(\beta)e^{\kappa b}\kappa^{-\beta}.
\]

For every bounded continuous \(\phi\) on \([0,\infty)\), substituting \(s=\kappa(x-a)\) into the numerator defining \(\mathbb E_{\mu_\downarrow}[\phi(\kappa(X-a))]\) and using these asymptotics yields the Gamma(\(\alpha\),1) expectation; a corresponding substitution \(s=\kappa(b-x)\) gives Gamma(\(\beta\),1) for \(\mu_\uparrow\). The endpoint asymptotics and compact support justify restricting to a fixed small endpoint neighborhood before applying dominated convergence, with the remaining mass exponentially negligible. Finally, the exact joint mixture and \(h_{m_\kappa}\to0\) imply the **independent** joint Gamma limit, for every permitted threshold choice. \(\square\)

## Verification

The standalone standard-library script `verify.py` checks (i) the finite-parameter two-atom joint law, including the nonzero mark covariance; (ii) a separately enumerated finite-state random walk with repeated independent resetting, computing its full marked absorption events up to a small residual transient mass and comparing those probabilities against its independently computed one-cycle transition probabilities; (iii) the convergence of discrete killed-walk boundary probabilities toward the Brownian hyperbolic boundary solution; and (iv) the Gamma boundary-layer means for a nonuniform Beta-type reset density. The continuous Brownian theorem and endpoint asymptotics are proved above; no finite experiment is used to infer an infinite statement.

As a transparent numeric diagnostic, for \(D=r=1\), \(\mu=0.4\delta_1+0.6\delta_2\), and \(m=3\), the conditional threshold-origin weights at \(1\) and \(2\) are approximately \((0.177643813674,0.822356186326)\); the unconditioned final absorption-origin weights are \((0.644404982645,0.355595017355)\). The covariance of the two coordinate marks conditioned on reaching \(3\) is \(0.0072732180223\ldots\), exactly \(e^{-3}\) times the variance under the threshold-origin law. The finite-state checks use their own discrete dynamics and do not claim to simulate infinitely many Brownian paths exactly.

## Relationship to prior work

The model of resetting to independently sampled positions and renewal descriptions of first passage were developed by Toledo-Marín and Boyer (2022), and by Méndez, Flaquer-Galmés and Campos (2024). Guo, Yan and Chen (2023) calculated the maximum before first passage for deterministic resetting positions. A 2026 public result entitled *Sharp excursion-risk envelope at fixed Brownian search time under distributed resetting* already supplies the unmarked maximum exceedance formula and sharp fixed-mean envelope for a reset distribution. **Neither that maximum formula nor the existing first-passage-time formulas are claimed as novel here.**

The present theorem tracks two distinct **cycle-origin marks** and proves an exact joint diagonal/product-mixture identity, threshold invariance of the first extreme's origin, strict opposite exponential tilting, a sharp conditional covariance factor, and independent endpoint Gamma layers. These are not implications about the *unmarked maximum law* alone: two path ensembles can have the same scalar maximum distribution but different origin markings. The cited unmarked paper uses a single fixed initial location; the present marked theorem requires an independently resampled initial location and a different two-event strong-Markov calculation. These are substantive overlaps in the underlying model and renewal technique, and priority remains subject to independent expert investigation.

A separate public result on Erlang resetting and preabsorptive extremes concerns the maximum and completed reset count rather than the spatial origins of first-threshold and terminal-absorption cycles. No claim of originality is made for its reset-count formulas or the general Dirichlet boundary solution.

## Limitations

The result is not a claim about which *individual Brownian excursion achieves the global final maximum*: the marked high excursion is the first one to reach a specified barrier. The origin of the last absorbing excursion is not the path's location of absorption (which is zero). For thresholds at or below the reset support, instantaneous reset jumps can cross the barrier and the threshold-invariant formula need not hold. Initial and post-reset laws must coincide; non-Poisson clocks, drift, spatially dependent hazards, and state-correlated resets are not covered. The Gamma boundary layer requires the stated endpoint regular variation; exotic singular laws may have different fine scales. The result gives a conditional joint law of two location marks, not the joint distribution of all reset epochs, the actual maximum location, or first-passage time. It has been subjected to self-review only, not independent scientific validation or a publication-priority certification.

## References

1. J. Q. Toledo-Marín and D. Boyer, *First passage time and information of a one-dimensional Brownian particle with stochastic resetting to random positions*, arXiv:2206.14387 (first public June 29, 2022), https://arxiv.org/abs/2206.14387 .
2. W. Guo, H. Yan and H. Chen, *Extremal statistics for a resetting Brownian motion before its first-passage time*, arXiv:2306.15929 (first public June 28, 2023), https://arxiv.org/abs/2306.15929 .
3. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125 (first public January 2, 2024), https://arxiv.org/abs/2401.01125 .
4. *Sharp excursion-risk envelope at fixed Brownian search time under distributed resetting*, public result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-excursion-risk-envelope-at-fixed-brownian-search-time-unde--7863fbd17fff/RESULT.md .
5. *Erlang resetting creates a clock-order logarithmic correction in first-passage spatial extremes*, public result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-erlang-resetting-creates-a-clock-order-logarithmic-correction-in--28e1e568a79f/RESULT.md .
