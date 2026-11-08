# The Ornstein–Uhlenbeck supremum law at the critical sink scale of complete-graph activated random walk

## Finding

Fix a sleep probability \(p\in(0,1)\) and a constant \(c\in(0,\infty)\). Consider the driven-dissipative activated random walk on a complete graph with \(n\) nonsink vertices, with loops at those vertices, as defined by Junge, Kaufman and Meisel. Each jump from a nonsink site is routed to the sink with probability \(q_n\), and otherwise to a uniformly selected nonsink site; the sleep probability is \(p\). Let \(S_n\) be the number of sleeping particles in a stationary configuration. Suppose

\[
q_n\sqrt n\longrightarrow c.
\]

Put \(\sigma=\sqrt{p(1-p)}\) and \(\theta=c/\sigma\). Let \((X_t)_{t\ge0}\) be a stationary, variance-one Ornstein–Uhlenbeck process, satisfying

\[
dX_t=-X_t\,dt+\sqrt2\,dW_t,
\qquad \operatorname{Cov}(X_s,X_t)=e^{-|t-s|}.
\]

Then the critical-window limit is

\[
\boxed{\frac{S_n-pn}{\sigma\sqrt n}\xrightarrow{\mathrm d}M_\theta:=\sup_{t\ge0}\bigl(X_t-\theta t\bigr).}
\]

The supremum is finite, attained, and has finite absolute moments of every positive order. It forms a strict continuum of stochastic laws: for every \(0<\theta_1<\theta_2\), the two maxima constructed from the same OU path satisfy \(M_{\theta_1}>M_{\theta_2}\) almost surely. Also, \(M_\theta>X_0\) almost surely for every finite \(\theta>0\), so

\[
\Pr(M_\theta\le r)<\Phi(r)\qquad(r\in\mathbb R),
\]

where \(\Phi\) is the standard normal distribution function. Finally,

\[
M_\theta\longrightarrow X_0\quad\text{almost surely as }\theta\to\infty,
\qquad
M_\theta\longrightarrow+\infty\quad\text{almost surely as }\theta\downarrow0.
\]

Thus the reciprocal-square-root sink scale admits a concrete, nontrivial crossover family rather than either the ordinary stationary Gaussian or the already established far-smaller-sink Gumbel scaling.

## Assumptions and scope

The sleep probability \(p\) does not depend on \(n\), and \(q_n\in(0,1)\) satisfies the displayed limit. The model uses the self-looped complete graph and stationary driven-dissipative occupancy convention of the cited 2026 article. It is *not* the fixed-energy process, nor the no-self-loop variant without a suitable parameter adjustment. The theorem is about weak convergence of the centered sleeping-particle count. It does not assert convergence of its moments, a quantitative convergence rate, or an explicit closed formula for the distribution function of \(M_\theta\).

The first-public source for the motivating problem is Junge, Kaufman and Meisel (arXiv:2604.04747, initially posted 2026-04-06 UTC). Their Proposition 5 is used as an existing representation: start with independent \(\operatorname{Bernoulli}(p)\) coordinates, let \(Y_n(j)\) be their number of ones after step \(j\), and let \(Z_n(j)\) count steps when the sink was chosen. At every step, independently with probability \(q_n\) increase \(Z_n\) by one without changing the coordinates; otherwise uniformly select one coordinate and refresh it to an independent \(\operatorname{Bernoulli}(p)\). With

\[
J_n=\inf\{j\ge0:Y_n(j)=n-Z_n(j)\},
\]

that representation gives \(S_n\overset d=Y_n(J_n)\). Its distributional identity, rather than a new assertion about the microscopic particle system, is the starting point of the proof.

## Proof

**1. Drift and covariance of the update count.** Conditioned on \(Y_n(j)=y\), the probabilities of an increment \(+1\) or \(-1\) are, respectively,

\[
u_n(y)=(1-q_n)p\left(1-\frac yn\right),
\qquad
 d_n(y)=(1-q_n)(1-p)\frac yn.
\]

Consequently,

\[
\mathbb E[\Delta Y_n\mid Y_n(j)=y]
=-\frac{1-q_n}{n}(y-np),
\]

and, when \(|y-np|=O(\sqrt n)\), the conditional second moment of the increment equals \(2p(1-p)+o(1)\). Every one-coordinate Bernoulli refresh preserves the full Bernoulli product distribution, even conditional on the entire sequence of sink/no-sink decisions. Therefore \(Y_n(j)\sim\operatorname{Binomial}(n,p)\) at every deterministic time, including when conditioning only on those decisions. The centered count has stationary variance \(n\sigma^2\).

**2. Joint diffusive window and moving boundary.** Put

\[
t_n=\left\lfloor\frac{(1-p)n}{q_n}\right\rfloor,
\quad
U_n(s)=\frac{Y_n(t_n+\lfloor ns\rfloor)-np}{\sigma\sqrt n},
\quad
G_n=\frac{Z_n(t_n)-q_nt_n}{\sqrt n}.
\]

For any fixed finite time interval in \(s\), the martingale functional central limit theorem and the displayed conditional moments imply

\[
(U_n,G_n)\Longrightarrow(X,G),
\quad G\sim N(0,1-p),
\]

where \(X\) is a *two-sided stationary* variance-one OU process independent of \(G\). To check independence rather than merely marginal convergence, take the left endpoint of a slightly larger finite window. Conditional on the sink decisions before that endpoint, the coordinate vector is still a Bernoulli product sample. The centered number of sink decisions in the following \(O(n)\) steps, divided by \(\sqrt n\), has variance \(O(q_n)=o(1)\). The local refresh process thus has the OU limit independently of the Gaussian fluctuation accumulated in the preceding \(\Theta(n^{3/2})\) steps. The latter has variance \(q_n(1-q_n)t_n/n\to1-p\). The predictable quadratic variations of the centered update-count martingales converge on compact windows to twice elapsed time after division by \(\sigma\sqrt n\); the bounded jumps give tightness and the Lindeberg condition.

The centered boundary is asymptotically affine: uniformly for \(s\) in a fixed compact interval,

\[
\frac{n-Z_n(t_n+\lfloor ns\rfloor)-np}{\sigma\sqrt n}
=-\frac{G_n+c s}{\sigma}+o_{\Pr}(1).
\]

Here the local fluctuation of the sink count has variance at most \(O(nq_n)=O(\sqrt n)\), and therefore vanishes after division by \(\sqrt n\).

**3. Localization of the first contact.** Set \(\tau_n=(J_n-t_n)/n\). These random times are tight. Indeed, \(Z_n(j)-q_nj\) is a bounded-increment martingale. Its maximal deviation over \(0\le j\le t_n\), divided by \(\sqrt n\), is tight by Doob's inequality because \(q_nt_n=O(n)\). In addition, there are constants \(C,a>0\), independent of \(n\), such that for every deterministic starting time \(v\) and every \(u\ge0\),

\[
\Pr\!\left(\max_{0\le k\le n}|Y_n(v+k)-np|>u\sqrt n\right)
\le C e^{-a u^2}.
\]

For completeness, let \(H_k=Y_n(v+k)-np\) and \(\rho_n=1-(1-q_n)/n\). The process \(\rho_n^{-k}H_k\) is a martingale, its increments over \(0\le k\le n\) are bounded by a universal constant, and \(H_0\) has the centered binomial law. Hoeffding's and maximal Azuma inequalities give the bound. Conditional on the sink-count maximal deviation being at most \(R\sqrt n\), in the \(k\)th length-\(n\) block to the left of \(t_n\), the boundary exceeds \(pn\) by at least \((ck-R-o(1))\sqrt n\). Summation of the preceding exponential estimate over all blocks with \(k\ge K\) makes the probability of \(\tau_n<-K\) arbitrarily small by first choosing \(R\), then \(K\). Conversely, if \(J_n>t_n+Kn\), the update count is below the boundary at that endpoint. The compact-window limit in step 2 bounds its limiting probability by

\[
\Pr\!\left(X_K+\frac{G+cK}{\sigma}\le0\right),
\]

which tends to zero as \(K\to\infty\). These two estimates establish tightness and exclude spurious contact in the remote past.

**4. Continuous first contact.** The limit of the crossing process on compact intervals is

\[
F(s)=X_s+\frac{G+c s}{\sigma},\qquad s\in\mathbb R.
\]

Its first nonnegative time over the entire real line,

\[
\tau=\inf\{s\in\mathbb R:F(s)\ge0\},
\]

is finite almost surely. Stationary OU block-maximal estimates ensure \(X_s=o(|s|)\) as \(|s|\to\infty\), so \(F(s)\) tends to the appropriate negative and positive infinities at the two ends. A nondegenerate OU path crosses a continuously differentiable boundary immediately after the first touch, by the strong Markov property and the local Brownian oscillation property. Thus compact-uniform convergence of the crossing processes, together with step 3, makes the first-hit functional continuous almost surely. It follows that \(\tau_n\Rightarrow\tau\).

At the discrete first contact \(Y_n(J_n)=n-Z_n(J_n)\) exactly: starting with a nonnegative integer gap, each individual step decreases the gap by at most one. The compact-window estimate on the sink martingale and the tightness of \(\tau_n\) therefore give

\[
\frac{Y_n(J_n)-pn}{\sigma\sqrt n}
\Longrightarrow-\frac{G+c\tau}{\sigma}.
\]

**5. Cancellation of the random boundary offset.** Condition on \(G=g\). For each real \(r\), the event that \(-(g+c\tau)/\sigma\le r\) says there was no crossing before time \(s_*=-(\sigma r+g)/c\). By shifting time by \(s_*\), that event becomes

\[
\sup_{u\ge0}\left(X_{s_*-u}-\frac c\sigma u\right)\le r.
\]

Stationarity and time reversibility of the two-sided OU process imply that, conditional on every fixed \(g\), the probability of this event equals \(\Pr(M_\theta\le r)\), with \(\theta=c/\sigma\). The conditional law does not depend on \(g\). Hence the random sink-count offset cancels from the distribution of the centered stationary sleeping count, proving the displayed weak limit.

**6. Geometry of the limit family.** The OU process has bounded unit-interval maxima with Gaussian tails. Summing these over integer intervals against the linear penalty \(\theta t\) shows that \(M_\theta\) is finite, attained, and has moments of all orders. Nondegenerate Brownian oscillations near time zero imply that \(\sup_{t>0}(X_t-\theta t)>X_0\) almost surely, so the maximizing time is strictly positive. Using a maximizing time for the larger penalty gives the strict pathwise comparison for \(\theta_1<\theta_2\). The stochastic inequality against \(X_0\) is strict at each finite threshold because a two-time Gaussian vector has a positive density. As \(\theta\to\infty\), a maximizer must approach zero, giving the almost-sure Gaussian endpoint. As \(\theta\downarrow0\), monotone convergence yields \(M_\theta\uparrow\sup_{t\ge0}X_t=+\infty\) almost surely by OU stationarity, ergodicity and its unbounded normal marginal.

## Verification

A standalone Python 3 checker, `check_finite.py`, performs 69,812 exact finite assertions using rational arithmetic. It verifies the one-step birth, death and holding probabilities, the centered drift and second-moment identity, detailed balance with the binomial law, stationary means and variances, microscopic Bernoulli-product invariance for fixed refresh coordinates, and the no-overshoot property of the positive integer boundary gap. It is run as `python check_finite.py`; the expected output is `PASS: 69812 exact finite assertions`.

The functional CLT, independent Gaussian offset, localization estimate, first-crossing continuity and limiting OU supremum representation are infinite mathematical arguments in the proof above. The checker does not certify them. Separate finite-sample simulations were used only as exploratory diagnostics, and no simulated frequencies were substituted for limit proofs.

## Relationship to prior work

Junge, Kaufman and Meisel, *Scaling limit and density conjecture for activated random walk on the complete graph* (arXiv:2604.04747), already prove the exact stationary-sampling representation and a Gumbel limit under \(n^{1/2+\varepsilon}\ll1/q_n\), together with a Gaussian endpoint when \(q_n=1\). Their Section 1.5 explicitly raises the intervening \(1/q_n=n^{1/2+o(1)}\) transition. The present theorem addresses the previously untreated finite-constant window \(q_n\sqrt n\to c\) and identifies its distribution, not merely its scaling. Járai, Mönch and Taggi (arXiv:2304.10169) establish concentration at a different sink regime, \(q_n\) of order \(1/n\), without this crossover distribution. Classical Ehrenfest-to-OU diffusion approximations and OU boundary-crossing theories supply important known mathematical ingredients, but their generic forms do not themselves identify this stationary activated-random-walk critical-window law without the moving-boundary representation, Gaussian sink-count correction and first-contact localization.

## Limitations

The result assumes fixed \(p\), the specified complete-graph sampling model, and a finite positive limit of \(q_n\sqrt n\). It does not cover the two ends where this product tends to zero or infinity as a joint \(n\)-dependent limit. Although the *limit family* has finite moments of all orders, no claim of convergence of \(\mathbb E S_n\), \(\operatorname{Var}(S_n)\) or their normalized versions is made. The Gaussian offset in the intermediate hitting-time limit is important and cannot simply be deleted before the OU time-shift argument. The law \(M_\theta\) is not claimed to be a newly discovered Gaussian-process functional; the contribution is its appearance as the exact critical-window occupancy law for this stochastic particle system. Historical priority beyond the sources checked is not definitively established.

## References

- M. Junge, H. Kaufman and J. Meisel, *Scaling limit and density conjecture for activated random walk on the complete graph*, arXiv:2604.04747 (initial version posted 2026-04-06), https://arxiv.org/html/2604.04747v2 . Theorems 1–4, Proposition 5, Sections 1.5, 2–3.
- A. A. Járai, C. Mönch and L. Taggi, *The number of particles in activated random walk on the complete graph*, arXiv:2304.10169 (initial version posted 2023-04-20), https://arxiv.org/pdf/2304.10169 . Theorems 1.1–1.2 and Section 7.1.
- J. Reed, A. R. Ward and D. Zhan, *On the generalized drift Skorokhod problem in one dimension*, Journal of Applied Probability 50 (2013), 16–28, DOI:10.1239/jap/1363784421 . Related OU hitting and reflected-process representation, not an ARW theorem.
