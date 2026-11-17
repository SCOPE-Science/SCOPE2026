# A universal two-equilibrium ceiling for heterogeneous nonlinear public-goods mixtures

## Finding
Let a well-mixed population play geometric-return public-goods games with a fixed, strategy-independent distribution of group sizes and size-dependent nonlinearities. Even when the distribution has countably infinite support and mixes discounting and synergy, the mean-field replicator equation has **at most two isolated interior equilibria**. If its cooperation-gain function is strictly convex, two interior equilibria occur **exactly** when
\[
\min_{0\le u\le1}G(u)<\frac1r<\min\{G(0),G(1)\}.
\]
The smaller equilibrium attracts nearby interior states and the larger repels them; full cooperation is also locally attracting. This bound is sharp for a genuine mixture of three distinct group sizes, with an explicit algebraic pair of interior equilibria.

## Assumptions and scope
For each index \(j\) in a finite or countable set \(J\), let \(\ell_j\ge2\) be an integer group size, \(\delta_j>0\) its geometric marginal-return multiplier, and \(w_j>0\) the probability that an individual's game uses that size and multiplier. Suppose \(\sum_jw_j=1\). The mixing probabilities do not depend on the current cooperator frequency or on the strategy of the focal player. A cooperator pays common cost \(c>0\). The total group benefit with \(k\) cooperators is \(b\sum_{h=0}^{k-1}\delta_j^h\), shared equally by \(\ell_j\) participants; set \(r=b/c>0\). Co-players are independently cooperative with probability \(u\in[0,1]\).

For infinite \(J\), assume
\[
\sum_j\frac{w_j}{\ell_j}\max\{1,\delta_j^{\ell_j-1}\}<\infty.
\]
Define
\[
G(u)=\sum_j\frac{w_j}{\ell_j}\bigl(1+(\delta_j-1)u\bigr)^{\ell_j-1},\quad
\dot u=u(1-u)(rG(u)-1).
\]
All conclusions concern this deterministic well-mixed replicator system, not finite-population fixation, structured hypergraph simulation, or strategy-dependent participation.

## Proof
**Payoff reduction.** Against \(k\) cooperating co-players in a group of size \(\ell_j\), switching from defection to cooperation increases the group's total benefit by \(b\delta_j^k\). Its focal payoff gain is \(b\delta_j^k/\ell_j-c\). Since \(k\sim\operatorname{Bin}(\ell_j-1,u)\), the binomial identity gives
\[
\mathbb E[\delta_j^k]=(1-u+u\delta_j)^{\ell_j-1}.
\]
Averaging with the strategy-independent \(w_j\), and scaling time by \(c\), gives precisely the displayed replicator equation.

**Convexity and strictness.** Every summand \(g_j(u)=(1+(\delta_j-1)u)^{\ell_j-1}/\ell_j\) is convex on \([0,1]\): its second derivative in the interior is
\[
g_j''(u)=\frac{(\ell_j-1)(\ell_j-2)(\delta_j-1)^2}{\ell_j}
(1+(\delta_j-1)u)^{\ell_j-3}\ge0.
\]
If some positive-weight component has \(\ell_j\ge3\) and \(\delta_j\ne1\), then that component is strictly convex, hence so is \(G\). The summability condition gives uniform convergence on \([0,1]\) and continuity; finite partial sums are convex and the uniform limit is convex. If no such component exists, all contributions are affine and \(G\) is affine, possibly constant.

**Zero count and exact phase criterion.** A horizontal line intersects a strictly convex continuous function in at most two points: if three distinct intersections had the same height, strict convexity would put the middle value strictly below that height. An affine nonconstant function has at most one intersection. The only exception to an isolated-root bound is constant \(G\) at \(rG=1\), in which case every interior point is an equilibrium. Let \(m=\min_{[0,1]}G\). For strictly convex \(G\), the equation \(G(u)=1/r\) has two distinct solutions in \((0,1)\) if and only if \(m<1/r<\min\{G(0),G(1)\}\). Necessity follows from strict convexity and the outer monotone branches; sufficiency follows from an interior unique minimizer and the intermediate-value theorem on either side. The left crossing is downward and the right upward, so their scalar vector-field derivatives have opposite signs: the left is asymptotically stable and the right unstable. Since \(rG(1)>1\), the endpoint \(u=1\) is also attracting from the left; \(u=0\) is repelling to the right. At the equality \(1/r=m\) with an interior minimizer, the unique interior contact is nonhyperbolic and semistable, not two equilibria.

**Three-size sharpness.** Use \((\ell_1,\ell_2,\ell_3)=(2,3,4)\), \((w_1,w_2,w_3)=(1/2,1/4,1/4)\), \((\delta_1,\delta_2,\delta_3)=(1/4,2,1/2)\), and \(r=8/3\). Direct exact expansion yields
\[
G(u)=\frac{19}{48}-\frac{11u}{96}+\frac{25u^2}{192}-\frac{u^3}{128},\quad
rG(u)-1=-\frac{(3u-2)(u^2-16u+4)}{144}.
\]
The physical interior roots are
\[
u_-=8-2\sqrt{15}\quad\text{and}\quad u_+=\frac23.
\]
Indeed \(0<u_-<u_+<1\), while the remaining algebraic root \(8+2\sqrt{15}\) exceeds one. Here \(G''(u)=25/96-3u/64>0\) on \([0,1]\), and \(rG(u)-1\) is positive before \(u_-\), negative between \(u_-\) and \(u_+\), and positive after \(u_+\). This proves stable coexistence plus stable full cooperation for a three-order mixture and establishes sharpness of the universal bound.

## Verification
The standalone standard-library Python script `verify.py` exactly constructs the gain polynomial from the three game definitions, verifies its factorization, endpoint and midpoint signs, and checks strict convexity of the example. It also runs 640 seeded exact-rational convexity tests on other finite mixtures. The infinite-support and all-parameter assertions follow from the analytic argument above, **not** from the finite tests.

## Relationship to prior work
Llabrés, Sadekar, Malizia and Battiston (arXiv:2604.07228, first public version April 8, 2026) derive the same geometric-return payoff form and prove an at-most-two-interior-equilibria result for a mixture of **two** interaction orders, analyzing the two- and three-player instance in detail. The present result concerns **any finite or countably infinite size spectrum with independent size-specific nonlinearities**, supplies an exact general necessary-and-sufficient two-root criterion, and exhibits a three-size sharpness witness. Peña's *Group-Size Diversity in Public Goods Games* (first public November 4, 2011) analyzes random group sizes, including discounted or synergistic geometric returns, but its geometric-return examples use a common nonlinearity across group sizes; those monotone-response results do not give the heterogeneous-size-specific mixed-sign two-root classification. The analytic convexity principle itself is elementary; no novelty is claimed for convexity, binomial expectation, or scalar replicator stability in isolation.

## Limitations
The theorem relies on fixed, strategy-independent mixing, common cooperator cost and geometric marginal benefits. It does not bound equilibria of models with arbitrary nonlinear gain functions, adaptive participation weights, strategy assortativity, or feedback of group-size composition on \(u\). The sharp example establishes possible bistability but makes no empirical claim that these numerical parameters describe a specific population. Independent scientific validation has not been performed; an unindexed equivalent all-order theorem remains possible.

## References
1. J. Llabrés, O. Sadekar, F. Malizia and F. Battiston, *Emergence of cooperation in nonlinear higher-order public goods games*, arXiv:2604.07228, first posted 2026-04-08. https://arxiv.org/abs/2604.07228 ; HTML relevant equations (1), (7), (12), (20)–(25): https://arxiv.org/html/2604.07228.
2. J. Peña, *Group-Size Diversity in Public Goods Games*, *Evolution* **66** (2012), 623–636; early public record 2011-11-04. https://doi.org/10.1111/j.1558-5646.2011.01504.x.
3. J. Peña and G. Nöldeke, *Group size effects in social evolution*, preprint first posted 2018-05-10. https://doi.org/10.1101/319350 (contextual general group-size analysis, not a direct theorem for this claim).
