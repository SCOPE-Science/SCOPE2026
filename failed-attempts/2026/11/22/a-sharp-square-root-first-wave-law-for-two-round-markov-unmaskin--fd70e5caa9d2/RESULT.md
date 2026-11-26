# A sharp square-root first-wave law for two-round Markov unmasking

## Finding

Consider an infinite stationary binary symmetric Markov chain with nearest-neighbour spin correlation \(0<\rho<1\). Generate a finite length-\(L\) word in exactly two ideal conditional-marginal rounds: each position is independently assigned to the first round with probability \(p\), and all other positions are revealed in the second round. Positions revealed together are sampled independently from their exact individual conditionals, rather than their joint conditional. Let \(B_L(p,\rho)\) be the forward path-space divergence from the exact sequentially conditioned reference process to this parallel process, averaged over the random round assignments, with natural logarithms. Let
\[
 b_\rho(p)=\lim_{L\to\infty}\frac{B_L(p,\rho)}L,
 \qquad \delta=-\log\rho,\qquad \xi=\delta^{-1}.
\]
The limit exists. Write \(p_\rho\) for its unique minimizer on \([0,1]\). In the long-correlation regime \(\xi\to\infty\), the **sharp new assertion** is
\[
 \boxed{\ p_\rho\sim\frac{1}{\sqrt{2\log2\,\xi}},\qquad
 b_\rho(p_\rho)\sim\sqrt{\frac{2\log2}{\xi}}.\ }
\]
Consequently, a uniform two-round schedule has an asymptotically unbounded relative loss:
\[
 b_\rho(1/2)\longrightarrow\frac{\log2}{2},\qquad
 \frac{b_\rho(1/2)}{b_\rho(p_\rho)}
 \sim\sqrt{\frac{\xi\log2}{8}}.
\]
The exact two-round loss formula and the existence and uniqueness of an interior optimizer are used as established starting points; their rederivation below is for a self-contained proof. The sharp near-perfect-order scaling and constants, with thermodynamic length taken first, are the contribution assessed here.

## Assumptions and scope

The spins \(X_i\in\{-1,+1\}\) have stationary initial marginal \(\Pr(X_1=+1)=1/2\) and transitions \(\Pr(X_{i+1}=X_i)=(1+\rho)/2\), with \(0<\rho<1\). Every position independently receives a round label \(1\) with probability \(p\) and otherwise label \(2\). The reference joint path law draws an entire newly selected block from its true conditional law; the parallel path law draws each selected coordinate independently from its true single-coordinate conditional. The same independent round labels are used under both laws. Divergence is \(D_{\mathrm{KL}}(P_L\Vert Q_L)\), not the marginal final-output divergence or perplexity. First take \(L\to\infty\) at each fixed \(\rho,p\); only then take \(\rho\uparrow1\). The conclusions do not assume a learned or approximate conditional predictor.

## Proof

**1. An exact finite-length accounting identity.** Let \(S\) be the random first-round set and \(H\) denote Shannon entropy in nats. The chain rule for the reference process and product conditional draws under the parallel process give
\[
 B_L= Lp\log2+\mathbb E_S\sum_{i\notin S}H(X_i\mid X_S)-H(X_1,\ldots,X_L).
\]
Put \(I_d=I(X_i;X_{i+d})\). For a Markov chain, the nearest revealed left and right spins screen all other revealed spins. If they occur at distances \(\ell,r\), then
\[
 H(X_i\mid X_{i-\ell},X_{i+r})=\log2-I_\ell-I_r+I_{\ell+r}.
\]
If a flank is absent its corresponding term is absent. Since \(H(X_1,\ldots,X_L)=L\log2-(L-1)I_1\), counting possible revealed flanks gives, for every \(L\ge2\) and \(0\le p\le1\),
\[
 \begin{split}
 B_L(p,\rho)={}&(L-1)I_1
 -2p\sum_{d=1}^{L-1}(L-d)(1-p)^dI_d\\
 &+p^2\sum_{d=2}^{L-1}(L-d)(d-1)(1-p)^{d-1}I_d.
 \end{split}
\]
Here \(I_d\) decays exponentially for fixed \(\rho<1\). Dividing by \(L\) and taking the limit yields
\[
 b_\rho(p)=I_1-2p\sum_{d\ge1}(1-p)^dI_d
  +p^2\sum_{d\ge2}(d-1)(1-p)^{d-1}I_d.
 \tag{1}
\]
All sums are absolutely convergent, including endpoint limits.

**2. Uniqueness and location of the optimizer.** For the symmetric binary chain,
\[
 I_d=\frac{(1+\rho^d)\log(1+\rho^d)+(1-\rho^d)\log(1-\rho^d)}2
 =\sum_{k\ge1}\frac{\rho^{2kd}}{2k(2k-1)}.
\]
Inserting this positive geometric expansion into (1) gives \(b_\rho(p)=\sum_{k\ge1}c_k f(p,a_k)\), where \(c_k=[2k(2k-1)]^{-1}\), \(a_k=\rho^{2k}\), and
\[
 f(p,a)=a\left(1-\frac{2p(1-p)}{1-a(1-p)}
 +\frac{a p^2(1-p)}{[1-a(1-p)]^2}\right).
\]
Direct differentiation and factorization give
\[
 \partial_p^2 f(p,a)=\frac{2a(1-a)^2[2+a(1-p)]}{[1-a(1-p)]^4}>0
 \quad(0<a<1,\ 0\le p\le1).
\]
Moreover \(\partial_pf(0,a)=-2a/(1-a)<0\) and
\(\partial_pf(1/2,a)=a^2(6-5a)/(2-a)^3>0\). Thus the exact objective is strictly convex and has one optimizer \(p_\rho\in(0,1/2)\). These finite-correlation optimizer facts are included to support the new singular limit, not presented as an independent priority claim.

**3. A conditional-entropy representation at long correlation.** Define binary entropy \(h(x)=-x\log x-(1-x)\log(1-x)\) and \(h_\delta(d)=h((1-e^{-\delta d})/2)\). Conditional on a site being revealed in round two, its nearest first-round revealed sites to the left and right are at independent geometric distances \(J,K\) with \(\Pr(J=j)=p(1-p)^{j-1}\), \(j\ge1\). Passing from the finite chain to its two-sided stationary limit in the entropy identity gives the exact expression
\[
 b_\rho(p)=p\log2+(1-p)\mathbb E\big[h_\delta(J)+h_\delta(K)-h_\delta(J+K)\big]-h_\delta(1).
 \tag{2}
\]
Indeed, the bracket equals \(H(X_0\mid X_{-J},X_K)\) by the Markov property and the entropy chain rule. This expression remains valid for every fixed \(0<p<1\), \(0<\rho<1\).

**4. Uniform square-root scaling.** Fix any \(t>0\) and put \(p=t\sqrt\delta\). For \(x\downarrow0\),
\[
 h((1-e^{-x})/2)=\frac{x}{2}\log\frac{2e}{x}
 +O(x^2(1+|\log x|)).
\]
Consequently, with \(x=\delta J\), \(y=\delta K\), the conditional-entropy bracket in (2) equals
\[
 \frac12\big[(x+y)\log(x+y)-x\log x-y\log y\big]
 +O\big((x+y)^2[1+|\log(x+y)|]\big)
\]
on \(x+y\le1/2\). The complement has exponentially small geometric probability when \(p\asymp\sqrt\delta\), and the entire bracket is bounded by \(\log2\). The expected remainder is \(O((\delta/p)^2[1+\log(p/\delta)])=o(\sqrt\delta)\), locally uniformly in \(t\) on compact positive intervals.

Let \(U=pJ\), \(V=pK\). As \(\delta\downarrow0\), \(U,V\) converge with their relevant moments to independent unit-rate exponential variables. Because the logarithmic bracket is homogeneous of degree one,
\[
 \mathbb E\big[(J+K)\log(J+K)-J\log J-K\log K\big]
 =\frac{1+o(1)}p.
\]
For the coefficient, write \(S=U+V\), \(W=U/S\): \(S\) is Gamma with shape \(2\), \(W\) is independent and uniform on \([0,1]\). Therefore
\(\mathbb E[S]=2\) and \(\mathbb E[h(W)]=1/2\), so \(\mathbb E[Sh(W)]=1\). Equation (2), together with \(h_\delta(1)=O(\delta\log(1/\delta))\), yields the locally uniform limit
\[
 \frac{b_\rho(t\sqrt\delta)}{\sqrt\delta}
 \longrightarrow g(t):=t\log2+\frac1{2t},\qquad t>0.
 \tag{3}
\]
The strictly convex \(g\) has its unique minimum at \(t_0=(2\log2)^{-1/2}\), with value \(g(t_0)=\sqrt{2\log2}\). Strict convexity of each \(b_\rho\) and local uniform convergence in (3) imply that its minimizer lies between any two fixed \(t_-\sqrt\delta\) and \(t_+\sqrt\delta\), for all sufficiently small \(\delta\), whenever \(t_-<t_0<t_+\): the limiting secant slopes are negative to the left and positive to the right. Hence \(p_\rho/\sqrt\delta\to t_0\), and the minimal values converge with the same scaling. Substituting \(\delta=1/\xi\) proves both boxed assertions.

**5. Comparison with equal-size rounds.** For fixed \(0<p<1\), dominated convergence in (2) as \(\delta\downarrow0\) gives \(b_\rho(p)\to p\log2\). At \(p=1/2\) this equals \((\log2)/2\). Combining with the sharp minimum in step 4 gives the displayed \(\sqrt\xi\) divergence of the uniform-schedule penalty.

## Verification

The accompanying standard-library script `checker.py` computes the exact finite-length path divergence in two independent ways: by enumerating all binary words, first-round subsets and conditional entropies, and by the displayed mutual-information formula. It checks \(125\) cases for lengths \(2\) through \(6\), correlations spanning positive and negative values, and five reveal probabilities; its maximal observed discrepancy is \(4.44\times10^{-15}\) nats. It separately checks positivity of the factored geometric-kernel second derivative and numerical near-perfect-order optimizers. These computations corroborate algebraic identities only; the strict convexity and singular limit are established by the proof above, not by finite sampling.

## Relationship to prior work

Baule's *Masked diffusion as random sequential adsorption* (arXiv:2611.07845v1, first public November 5, 2026) establishes the exact general finite-round path-error framework for Markov sequences and analyzes many-round thermodynamic-metric geodesic schedules. Exact two-round finite-correlation optimizer descriptions and finite-length perfect-order schedules already provide valuable comparisons; their results are treated as established, not reintroduced as new contributions. The present result concerns a **distinct nonuniform limit**: first infinitely many sites at fixed positive transition noise, then vanishing transition noise at exactly two rounds, yielding explicit square-root constants and unbounded improvement over equal-sized rounds. It is not a direct substitution into the many-round continuum geodesic expression.

Other relevant lines include general information-profile optimization (Lavenant–Zanella), unmasking schedule characterization (Chen–Cong–Li), and conditional-total-correlation/serial-depth bounds (Wen–Liang–Lu); they address broader error identities or distinct scheduling regimes. A one-round Gaussian score-based selection threshold (Li) uses a square-root *population-size* scale rather than this Markov-correlation-length scaling. No claim of absolute publication priority is made.

## Limitations

Only two rounds, independently Bernoulli-assigned positions, stationary strictly positive binary symmetric Markov sources, exact conditional-marginal predictors and forward **path** divergence are studied. The \(L\to\infty\) and \(\rho\uparrow1\) limits must be taken in the specified order; the theorem is not uniform in finite \(L\). It does not optimize adaptive, geometry-dependent or fixed-cardinality reveal schedules, nor final-output KL or perplexity. Publication-priority uncertainty remains because not all relevant specialist manuscripts were accessible in full.

## References

1. A. Baule, *Masked diffusion as random sequential adsorption: an exactly solvable model for parallel decoding*, arXiv:2611.07845v1 (first posted November 5, 2026). https://arxiv.org/html/2611.07845v1
2. H. Lavenant and G. Zanella, *Error Bounds and Optimal Schedules for Masked Diffusions with Factorized Approximations*, arXiv:2510.25544 (first posted October 29, 2025). https://arxiv.org/abs/2510.25544
3. S. Chen, K. Cong and J. Li, *Optimal Inference Schedules for Masked Diffusion Models*, Proceedings of Machine Learning Research 336 (2026), pp. 1279–1311. https://proceedings.mlr.press/v336/chen26e.html
4. C. Wen, W. Liang and J. Lu, *Conditional Total Correlation and the Serial Depth of Adaptive Parallel Sampling*, arXiv:2608.25505 (first posted August 26, 2026). https://arxiv.org/abs/2608.25505
5. L. Li, *One-step lowest-variance selection in a Gaussian random-field model motivated by masked diffusion: Total correlation and a square root collision threshold*, arXiv:2607.17522 (first posted July 20, 2026). https://arxiv.org/abs/2607.17522
