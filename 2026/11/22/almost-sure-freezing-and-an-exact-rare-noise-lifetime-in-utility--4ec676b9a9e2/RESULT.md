# Almost-sure freezing and an exact rare-noise lifetime in utility-weighted bounded-confidence dynamics

## Finding

For any finite population of at least two agents, strictly positive utility weights, a finite positive confidence radius, and independent Gaussian opinion innovations occurring **only when a selected pair is receptive**, the exact unbounded-opinion, utility-weighted bounded-confidence chain almost surely reaches a state in which **no pair can interact**. More strongly, its time to complete freezing has a parameter-explicit geometric tail, and its invariant probability measures are precisely the probability measures supported on completely incompatible configurations. For two agents at half-compromise, the time to freeze is exactly geometric, with a sharp exponential weak-noise lifetime.

Let \(\mathcal A=\{x\in\mathbb R^N:|x_i-x_j|\ge\varepsilon\ \text{for all }i\ne j\}\) and \(T=\inf\{t\ge0:X(t)\in\mathcal A\}\), with time measured in attempted pair selections. For \(N\ge2\), \(\varepsilon>0\), \(\sigma>0\), and \(0<\mu<1\), set

\[
M=\binom N2,\quad m=\lfloor N/2\rfloor,\quad
q=\frac{\varepsilon}{\sqrt{2\pi}\sigma}
\exp\!\left[-\frac{(5N+4)^2\varepsilon^2}{2\sigma^2}\right],\quad
p=\frac{q^2}{M}.
\]

Then for every deterministic initial configuration and every integer \(k\ge0\),

\[
\boxed{\Pr_x(T>mk)\le(1-p^m)^k,\qquad \mathbb E_x T\le\frac{m}{p^m}.}
\]

Every invariant probability distribution is supported on \(\mathcal A\), and every probability distribution supported on \(\mathcal A\) is invariant. If \(N=2\), \(\mu=1/2\), and the initial pair is receptive, then, irrespective of its initial gap and its strictly positive utility weights,

\[
\boxed{\Pr(T=t)=(1-r)^{t-1}r\ (t=1,2,\ldots),\quad
r=\operatorname{erfc}\!\left(\frac{\varepsilon}{2\sigma}\right),\quad
\mathbb E T=\frac1r.}
\]

In particular, as \(\sigma\downarrow0\) with \(\varepsilon\) fixed,

\[
\boxed{\mathbb E T\sim \frac{\sqrt\pi\,\varepsilon}{2\sigma}
\exp\!\left(\frac{\varepsilon^2}{4\sigma^2}\right).}
\]

## Assumptions and scope

Fix \(N\ge2\), opinions \(x_i\in\mathbb R\), a confidence threshold \(\varepsilon>0\), and learning rate \(0<\mu<1\). Each discrete attempt selects an unordered pair \(\{i,j\}\) uniformly from the \(M=\binom N2\) pairs, independently of prior selections. The pair interacts exactly if \(|x_i-x_j|<\varepsilon\). If it is not receptive, **all opinions remain unchanged and no noise is added**. If it is receptive, the two selected opinions become

\[
 x_i^+=x_i+2\mu\frac{U_j(x)}{U_i(x)+U_j(x)}(x_j-x_i)+\eta_i,\qquad
 x_j^+=x_j+2\mu\frac{U_i(x)}{U_i(x)+U_j(x)}(x_i-x_j)+\eta_j,
\]

where each \(U_i(x)>0\) is finite and measurable, and the fresh noises on each accepted interaction are independent \(N(0,\sigma^2)\), also independent of pair choice and history. Nonselected opinions stay fixed. The utility may depend on the whole opinion vector; no smoothness, boundedness, or normalization of positive utilities is required. This is the unprojected interpretation of the interaction rule of Siebenmorgen and Restrepo; the source denotes the innovation standard deviation by \(\Delta\), whereas here \(\sigma\) denotes it throughout.

The absorbing set \(\mathcal A\) allows equality at the confidence boundary because the interaction condition is strict. All times count **attempted pair choices**, not successful interactions; the originating model uses physical time increment \(1/N\) per attempt, so corresponding physical mean times are divided by \(N\). Gaussian full support and the absence of innovations on rejected interactions are essential to the claimed almost-sure freezing mechanism.

## Proof

**1. A uniformly favorable two-agent relocation.** Suppose \(x\notin\mathcal A\). Select any fixed receptive pair \(i,j\), for example the lexicographically first. Since both utility ratios are strictly between zero and one and \(0<\mu<1\), the deterministic pre-noise positions \(y_i,y_j\) obey

\[
 |y_i-x_i|<2\varepsilon,\qquad |y_j-x_i|<3\varepsilon.
\]

The second estimate follows from \(|x_j-x_i|<\varepsilon\) and the deterministic motion of \(j\) by less than \(2\varepsilon\). Consider the \(N\) target centers \(c_\ell=x_i+5\ell\varepsilon\), for \(\ell=1,\ldots,N\). Because distinct centers are \(5\varepsilon\) apart, each of the \(N-2\) nonselected opinions lies within \(2\varepsilon\) of **at most one** target center. Consequently at least two distinct centers, say \(c_a,c_b\), have distance greater than \(2\varepsilon\) from every nonselected opinion.

Require the updated opinions to fall into \((c_a-\varepsilon/2,c_a+\varepsilon/2)\) and \((c_b-\varepsilon/2,c_b+\varepsilon/2)\). On this event both selected agents are more than \(3\varepsilon/2\) away from every nonselected agent and at least \(4\varepsilon\) apart from one another. They are therefore both isolated in the new confidence graph. Also, an agent already isolated before this update could not have been selected, and it remains isolated: only the two moved agents have changed, and both end more than \(\varepsilon\) from all others. Thus the number of isolated vertices increases by at least two on such a *favorable* move.

For either target interval, the required noise belongs to an interval of length \(\varepsilon\), whose points all have absolute value below \((5N+4)\varepsilon\): the target center is at most \(5N\varepsilon\) from \(x_i\), both pre-noise positions are within \(3\varepsilon\) of \(x_i\), and the target half-width is \(\varepsilon/2\). The Gaussian density throughout this interval is at least

\[
\frac1{\sqrt{2\pi}\sigma}
\exp\!\left[-\frac{(5N+4)^2\varepsilon^2}{2\sigma^2}\right].
\]

Each target interval therefore receives probability at least \(q\); the two independent noises give joint probability at least \(q^2\). The required pair is selected with probability \(1/M\). Hence from every nonabsorbing state the probability of a favorable move is at least \(p=q^2/M\). This lower bound is valid regardless of the positions' magnitudes, the utility function, or the state history.

**2. Uniform finite-block absorption.** From any nonabsorbing configuration, repeatedly choose the above favorable move. At each such move two previously nonisolated agents become isolated, while the isolated agents from earlier favorable moves stay isolated. After at most \(m=\lfloor N/2\rfloor\) favorable moves, no receptive pair is possible. Indeed, if at most one nonisolated vertex remains, it has no receptive partner and is isolated by definition. The conditional probability of this consecutive favorable path is at least \(p^m\). If absorption happens earlier, the remaining attempted updates do not change the state, so \(\Pr_x(T\le m)\ge p^m\) for every \(x\notin\mathcal A\).

Apply this uniform bound after each successive block of \(m\) attempted selections, using the Markov property. It yields \(\Pr_x(T>mk)\le(1-p^m)^k\). Summation of the survival probabilities over the integer time steps gives \(\mathbb E_x T\le m/p^m\). In particular, \(T<\infty\) almost surely from every initial configuration.

**3. All invariant laws.** Every point of \(\mathcal A\) is absorbing by the no-update rule, so every probability distribution on \(\mathcal A\) is invariant. If \(\pi\) is any invariant probability measure, then for all integers \(t\ge0\),

\[
\pi(\mathcal A^c)=\Pr_\pi(X(t)\notin\mathcal A)=\Pr_\pi(T>t).
\]

The right side tends to zero by the uniform geometric bound (or bounded convergence), proving \(\pi(\mathcal A^c)=0\). No irreducible stationary density supported inside a permanently interacting cluster exists for the exact chain under these assumptions.

**4. Exact two-agent clock.** When \(N=2\), the only pair is always selected. Subtracting its updates gives the utility-independent identity

\[
 x_1^+-x_2^+=(1-2\mu)(x_1-x_2)+\eta_1-\eta_2.
\]

At \(\mu=1/2\), the post-update difference is fresh \(N(0,2\sigma^2)\), independently at every receptive attempt. Its chance of leaving the strict confidence interval is \(r=\operatorname{erfc}(\varepsilon/(2\sigma))\). This constant hazard proves the stated geometric law, including its expectation. The standard large-argument complementary-error-function asymptotic gives the sharp weak-noise equivalent. If the initial pair is already incompatible, \(T=0\) instead.

## Verification

The accompanying `verify.py` uses only the Python standard library. It checks the exact utility-cancellation identity with rational inputs, validates the empty-target-center construction on generated rational opinion configurations, verifies the uniform noise-displacement bound and associated positive minorization, and tests the stated Gaussian two-agent tail and its small-noise equivalent numerically. These computations are independent spot checks, **not** the proof of the all-population, infinite-time result, which is provided above. The script exits unsuccessfully on any failed assertion and reports a fixed-seed summary when all checks pass.

## Relationship to prior work

Siebenmorgen and Restrepo (2026) introduced this precise utility-weighted pair rule, including its strict confidence condition, conditional noise, and an approximate single-cluster stochastic differential equation with Gibbs-like stationary density. That Gibbs law is an approximation **within a persistent-cluster assumption**, not claimed in that paper as the exact infinite-horizon invariant measure of the microscopic chain. The current finding addresses the noncommuting infinite-time and weak-noise questions for a specified Gaussian instance of the exact conditional-noise rule, and provides a finite-agent almost-sure absorption guarantee with quantitative tails and an exact two-agent escape law.

Steiglechner and coauthors (2024) study the separate effects of several noise placements in bounded-confidence models, principally in an opinion interval with clipping or truncated messages; their finite-horizon noise-induced consensus results do not imply this unbounded-opinion conditional-noise absorption classification. Shree, Chatterjee and Jagannathan (2023) study finite-time stochastic bounded-confidence behavior under different bounded or distance-dependent stochastic assumptions, not the present Gaussian relocation argument. A published finite-population treatment of utility-weighted noisy averaging studies a weak-noise diffusion process but explicitly does not claim a microscopic stationary-law limit. Another published treatment of noisy compromise studies a permanently interacting population; the absence of a hard confidence gate prevents its stationary laws from covering the present absorbing-state result. A separate exact calculation for the source's **noiseless** two-agent case concerns consensus overshoot, not positive-noise absorption.

## Limitations

The geometric upper bound for general \(N\) is deliberately conservative and does not determine the typical weak-noise lifetime for a many-agent cluster. The exact waiting-time formula requires two agents, half-compromise, independent Gaussian noises, and initial receptivity. With a different noise distribution, restricted opinion space, background noise on rejected pairs, confidence resetting, forced contacts, or a permanently imposed single-cluster condition, the conclusion can fail. The theorem says nothing about empirical human behavior, nor about any approximate quasi-stationary distribution observed before freezing. The novelty comparison is literature-bounded; an unindexed general result on noise-activated absorbing sets could imply the geometric-tail theorem after specialization.

## References

- A. Siebenmorgen and J. G. Restrepo, *A Utility-Driven Bounded-Confidence Model for Opinion Dynamics*, arXiv:2605.21844v1 (first public May 21, 2026), https://arxiv.org/abs/2605.21844. Main-text equations (1), (2), and (15); Supplementary Material.
- P. Steiglechner, M. A. Keijzer, P. E. Smaldino, D. Moser, and A. Merico, *Noise and opinion dynamics: how ambiguity promotes pro-majority consensus in the presence of confirmation bias*, Royal Society Open Science 11 (2024), 231071, https://doi.org/10.1098/rsos.231071.
- S. S. Shree, D. Chatterjee, and K. Jagannathan, *Finite Time Bounds for Stochastic Bounded Confidence Dynamics*, IEEE Transactions on Network Science and Engineering (2023), https://doi.org/10.1109/TNSE.2023.3340255.
- *The finite-population Gibbs exponent for noisy utility-weighted opinion averaging*, publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-the-finite-population-gibbs-exponent-for-noisy-utility-weighted--8f1089ea0c11.
- *The first non-Gaussian noisy-compromise population and its exact fourth moment*, publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-first-non-gaussian-noisy-compromise-population-and-its-exact--1905b42cd00e.
- *Almost-sure finite-time stabilization of the effective graph in adaptive-confidence Deffuant–Weisbuch dynamics*, publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-almost-sure-finite-time-stabilization-of-the-effective-graph-in--89f7f0a6c87c.
