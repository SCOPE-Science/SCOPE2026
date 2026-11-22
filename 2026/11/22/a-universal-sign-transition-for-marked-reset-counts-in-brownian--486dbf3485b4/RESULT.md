# A universal sign transition for marked reset counts in Brownian target search

## Finding

Let a Brownian searcher start at distance \(x_0>0\) from an absorbing origin on \((0,\infty)\), diffuse with generator \(D\partial_x^2\), and reset at Poisson rate \(r>0\) to one of \(m\ge2\) fixed positive distances \(x_j\), sampled independently at every reset with probabilities \(p_j>0\), \(\sum_{j=1}^m p_j=1\). Write \(N_j\) for the total number of resets **to destination** \(x_j\) before absorption, with destinations individually labelled even if two locations coincide. Define \(k=\sqrt{r/D}\), \(g_0=e^{-kx_0}\), \(g_j=e^{-kx_j}\), and \(G=\sum_{j=1}^m p_jg_j\).

The complete multivariate probability generating function is
\[
\mathbb E\left[\prod_{j=1}^m z_j^{N_j}\right]
=g_0+(1-g_0)\frac{\sum_{j=1}^m p_jg_j z_j}{1-\sum_{j=1}^m p_j(1-g_j)z_j},\qquad |z_j|\le1.
\]
In particular, for every distinct pair \(i\ne j\),
\[
\mathbb E N_i=\frac{(1-g_0)p_i}{G},\qquad
\operatorname{Cov}(N_i,N_j)
=\frac{(1-g_0)p_ip_j}{G^2}\left(1+g_0-g_i-g_j\right).
\]
The sign of this covariance is **independent of the mixing probabilities and every other reset location**. If \(x_0\le x_i+x_j\), it is strictly positive at all \(r>0\). If \(x_0>x_i+x_j\), it is strictly negative for all sufficiently small positive \(r\), strictly positive for all sufficiently large \(r\), and has **exactly one** zero, at \(r_{ij}^*=Dk_{ij}^{*2}\), where \(k_{ij}^*>0\) is the unique positive solution to
\[
1+e^{-kx_0}=e^{-kx_i}+e^{-kx_j}.
\]
Consequently, for each \(r>0\), the graph connecting negatively correlated destination pairs is a threshold graph, and its edge sets decrease monotonically under increasing \(r\), becoming empty after finitely many crossings. As \(r\downarrow0\), with \(x_0\ne x_i+x_j\),
\[
\operatorname{Cov}(N_i,N_j)
\sim p_ip_j x_0(x_i+x_j-x_0)\frac{r}{D}.
\]
On the critical geometry \(x_0=x_i+x_j\), the covariance is positive with the sharper leading law
\[
\operatorname{Cov}(N_i,N_j)\sim
p_ip_j x_0x_ix_j\left(\frac rD\right)^{3/2}.
\]

## Assumptions and scope

All parameters obey \(D,r,x_0,x_1,\ldots,x_m>0\), \(m\in\mathbb N\), \(m\ge2\), and \(p_j>0\) with sum one. Brownian motion is standard one-dimensional driftless diffusion with variance \(2Dt\). The resetting clock is independent of the Brownian motion and reset labels. Every reset is counted, including a reset back to the current location; it is an actual Poisson event. The path is absorbed upon first hitting zero; there is no reset directly into the absorbing target. Every finite positive rate yields almost-sure absorption and moments of all finite orders of the reset counts. The result is an infinite-half-line statement; no finite interval or reset-site ordering is assumed.

## Proof

**1. One-excursion absorption.** The Laplace transform of the target hitting time \(\tau_0\) for Brownian motion started at \(x>0\) is \(\mathbb E_x[e^{-r\tau_0}]=e^{-x\sqrt{r/D}}\). Hence the probability of absorption before the next Poisson reset is \(g(x)=e^{-kx}\). At the original starting location this is \(g_0\); after a reset of label \(j\) it is \(g_j\).

**2. Marked renewal law.** For a fresh excursion beginning at reset destination \(j\), let \(F_j(\boldsymbol z)\) denote the joint generating function of all *future* reset counts. Let \(H=\sum_j p_jz_j F_j\) be the generating function after recording a new randomly labelled reset. By the strong Markov property and the exponential clock,
\[
F_j=g_j+(1-g_j)H,
\qquad
H=\sum_jp_jz_jg_j+H\sum_jp_j(1-g_j)z_j.
\]
Solving gives \(H=S/(1-R)\), where \(S=\sum_jp_jg_jz_j\) and \(R=\sum_jp_j(1-g_j)z_j\). Before the first reset the particle starts at \(x_0\), so \(\Phi=g_0+(1-g_0)H\), proving the stated joint generating function. As \(R(\boldsymbol1)=1-G<1\), it is analytic in a neighbourhood of \(\boldsymbol1\) and all necessary derivatives exist.

**3. Exact mixed moments.** Differentiation at \(\boldsymbol z=\boldsymbol1\), noting \(S(\boldsymbol1)=1-R(\boldsymbol1)=G\), gives
\[
\partial_i\Phi(\boldsymbol1)=\frac{(1-g_0)p_i}{G},\quad
\partial_i\partial_j\Phi(\boldsymbol1)
=\frac{(1-g_0)p_ip_j(2-g_i-g_j)}{G^2}\quad(i\ne j).
\]
Subtracting the product of the first derivatives gives the covariance formula. Its prefactor is strictly positive. Thus its sign is that of \(C_{ij}(k)=1+e^{-kx_0}-e^{-kx_i}-e^{-kx_j}\), independent of reset-site probabilities and other locations.

**4. Sharp geometric dichotomy and uniqueness.** Put \(a=x_i\), \(b=x_j\). If \(x_0\le a+b\),
\[
C_{ij}(k)=(1-e^{-ka})(1-e^{-kb})+e^{-kx_0}-e^{-k(a+b)}>0.
\]
If \(x_0>a+b\), write \(\delta=x_0-a-b>0\). Multiplication by \(e^{k(a+b)}\) transforms \(C_{ij}\) into
\[
(e^{ka}-1)(e^{kb}-1)-(1-e^{-k\delta}).
\]
The ratio of its two positive terms,
\[
R_*(k)=\frac{(e^{ka}-1)(e^{kb}-1)}{1-e^{-k\delta}},
\]
starts at zero as \(k\downarrow0\), diverges as \(k\to\infty\), and has strictly positive logarithmic derivative:
\[
\frac{d}{dk}\log R_*(k)
=\frac a{1-e^{-ka}}+\frac b{1-e^{-kb}}-\frac\delta{e^{k\delta}-1}
>\frac1k+\frac1k-\frac1k>0.
\]
The strict bounds use \(1-e^{-u}<u<e^u-1\) for every \(u>0\). Therefore \(R_*(k)=1\) at exactly one positive \(k\), and the covariance changes from negative to positive there. Since \(k=\sqrt{r/D}\) increases strictly with \(r\), every negative edge is removed at most once as the resetting rate increases. At fixed \(k\), negative edges are exactly the pairs satisfying \(e^{-kx_i}+e^{-kx_j}>1+e^{-kx_0}\), the defining weight-sum rule of a finite threshold graph.

**5. Weak-reset boundaries.** The expansions \(1-g_0=x_0k+O(k^2)\), \(G=1+O(k)\), and \(C_{ij}(k)=(a+b-x_0)k+O(k^2)\) prove the noncritical expansion. At \(x_0=a+b\), the factorization in step 4 gives \(C_{ij}(k)=abk^2+O(k^3)\), yielding the positive critical \(k^3\) law. Replacing \(k^2\) with \(r/D\) yields the displayed forms.

## Verification

The self-contained Python 3 standard-library checker `check_reset_counts.py` uses exact rational Gauss–Jordan elimination for finite Markov-reward equations, independently computes the first and pairwise mixed moments, and compares them with the formulas above. It passed 184 exact-rational model instances and 3297 exact assertions. For Brownian settings it uses \(r=(\log2)^2D\) and integer distances, so that all one-excursion absorption probabilities are exact rationals \(2^{-x}\). Separately, a bisection check for \(D=1\), \(x_0=4\), \(x_i=1\), \(x_j=2\) gives \(k_{ij}^*\approx0.28119957432296\), \(r_{ij}^*\approx0.07907320059942\). These checks are diagnostic and do not replace the all-parameter analytic proof.

## Relationship to prior work

Toledo-Marín and Boyer (arXiv:2206.14387, first posted 2022-06-29), Section II, give the general reset-cycle survival products and distribution of the **total** number of resets for position distributions that may vary by cycle, including their mean; those expressions motivate the regenerative framework. Julián-Salgado, Dagdug and Boyer (arXiv:2311.11897, first posted 2023-11-20), Sections II–III, explicitly study two-site Brownian resetting and its mean first-passage time with arbitrary positive reset rates. Sunil and collaborators (arXiv:2304.09348, 2023-04-19), Section 2, derive a joint first-passage and **total** reset count/cost transform under fixed-site resetting. Méndez, Flaquer-Galmés and Campos (arXiv:2401.01125, 2024-01-02), study first-passage times and their fluctuations for random reset positions. None of the inspected statements presents the **destination-labelled** joint count generating function, pairwise covariance sign transition independent of mixture weights, or threshold-graph nesting proved here. This is a distinction of stated results, not a claim that existing renewal methods could not be adapted to derive them. Published related results on local-time/reset-count conjugacy and distributed-reset first-passage moments were also compared as different observables.

## Limitations

The reset destinations must be strictly inside the positive half-line; target landing at a reset, partial resetting, state-dependent clocks and non-Poisson waiting times are not treated. Two different reset labels may point to the same location, but their event counts remain distinguishable by label. The graph classification is about *pairwise reset-count covariance*, not covariance of physical spatial occupancies or trajectory times. The exact joint PGF is a straightforward regenerative reduction once a marked model is specified, so the strongest originality claim is the all-rate geometric sign classification, sharp single-crossing theorem and mixture-invariant threshold graph. General marked renewal machinery could implicitly imply these identities; independent publication-priority assessment is still needed.

## References

1. J. Quetzalcoatl Toledo-Marín and D. Boyer, *First passage time and information of a one-dimensional Brownian particle with stochastic resetting to random positions*, arXiv:2206.14387 (2022), https://arxiv.org/abs/2206.14387.
2. P. Julián-Salgado, L. Dagdug and D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897 (2023), https://arxiv.org/abs/2311.11897.
3. J. C. Sunil, R. A. Blythe, M. R. Evans and S. N. Majumdar, *The cost of stochastic resetting*, arXiv:2304.09348 (2023), https://arxiv.org/abs/2304.09348.
4. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125 (2024), https://arxiv.org/abs/2401.01125.
