# The two-to-three opinion threshold for sparse homophilic rewiring closure

## Finding
For the discordant-edge rewiring process defined below, a sparse large-population limit has a deterministic **edge-type** evolution. With precisely two fixed opinion classes, the fraction of concordant edges has an exact scalar fluid limit: it increases at a constant rate until absorption, independently of the initial network topology. Three fixed classes are the smallest number for which that universal scalar closure can fail. Specifically, with three equally sized classes of opinions \(0,2/5,4/5\), tolerance \(r=1/5\), and initially one cross-class matching, two sequences having the same opinion multiset, the same number of edges, and the same initial concordance \(C(0)=0\) have different limiting right derivatives:
\[
 C'_{01}(0)=\frac{50}{33},\qquad C'_{02}(0)=\frac53,\qquad C'_{02}(0)-C'_{01}(0)=\frac5{33}.
\]
Therefore no scalar autonomous law \(\dot C=f(C)\), common to all sparse initial networks with these opinions, describes both trajectories. The claim is about asymptotic universal closure, not the accuracy of a representative-density approximation on typical graphs.

## Assumptions and scope
Fix an integer \(q\ge2\) and distinct class opinions \(\theta_1,\ldots,\theta_q\in[0,1]\) with \(0<r<\min_{a\ne b}|\theta_a-\theta_b|\), and \(w_{ab}:=1-|\theta_a-\theta_b|>0\) for every pair. In a simple graph on \(N\) labelled vertices, the opinion labels are fixed; class \(a\) has \(N_a\) vertices with \(N_a/N\to\mu_a>0\), \(\sum_a\mu_a=1\). There are \(K_N\) edges, \(K_N/N\to\kappa\in(0,1)\), and the initial maximum degree is \(o(N)\).

At the event times of a rate-\(N\) Poisson process, if any discordant edge exists, select one uniformly, retain either endpoint with probability \(1/2\), and replace its edge to the other endpoint by an edge to a new, distinct *nonneighbor* (excluding the retained vertex itself). The new target is sampled with weights \(w_{ac}\), where \(a\) and \(c\) are the retained and target opinion classes. The sampling is from the graph **before** deletion of the old edge. If every edge is concordant, the process is absorbing. An edge is concordant precisely when its two endpoints have the same opinion class. The no-self-loop convention is imposed explicitly for a simple graph; it does not alter the fluid limit.

Let \(E_{ab}^{(N)}(t)\), \(a\le b\), be the class-pair edge count and suppose \(E_{ab}^{(N)}(0)/N\to x_{ab}(0)\). Write \(C_N(t)=\sum_a E_{aa}^{(N)}(t)/K_N\) and \(d(x)=\sum_{a<b}x_{ab}\). Define
\[
 U_{ac}=\frac{\mu_cw_{ac}}{\sum_h\mu_hw_{ah}},\qquad u_a=U_{aa}=\frac{\mu_a}{\sum_h\mu_hw_{ah}}.
\]
All limits below concern fixed finite time horizons. The general fluid equation is asserted only before the first hitting of \(d=0\); the two-class scalar formula includes absorption.

## Proof
**1. Uniform sparse-target approximation.** Since \(K_N/N\to\kappa<1\) and \(w_{ab}\ge w_*>0\), the target normalizer at any retained vertex is at least \(w_*(N-1-K_N)\), uniformly over all graph states. Hence the conditional probability of selecting any particular vertex as a new target is bounded by \(B/N\), for a constant \(B\) independent of the state and large \(N\). In any fixed interval \([0,T]\), incoming edge arrivals to each specified vertex are dominated by a Poisson variable with mean \(BT\). A union bound yields a maximum arrival count of \(O_{\mathbb P}(\log N)\). Only target arrivals can raise a degree, so the maximum degree remains \(o_{\mathbb P}(N)\) uniformly on \([0,T]\). Consequently, conditional on a retained class-\(a\) vertex, the probability of a class-\(c\) target is \(U_{ac}+o_{\mathbb P}(1)\), uniformly in vertices and times on \([0,T]\).

**2. Exact edge-type fluid equation.** Let \(\mathbf e_{ab}\) denote a coordinate vector for unordered edge type \(\{a,b\}\). On any region with \(d(x)>0\), define
\[
 F(x)=\frac{1}{2d(x)}\sum_{a<b}x_{ab}\sum_c\left[U_{ac}(\mathbf e_{ac}-\mathbf e_{ab})+U_{bc}(\mathbf e_{bc}-\mathbf e_{ab})\right].
\]
Each jump of \(E^{(N)}/N\) is at most \(2/N\) in \(\ell^1\), and jumps occur at rate at most \(N\). Thus each coordinate martingale has predictable quadratic variation at most \(4T/N\). Combining the uniform target approximation with this martingale bound and Gronwall's inequality, up to any region \(d(x)\ge\eta>0\), yields convergence in probability, uniformly on compact time intervals, to the unique solution \(\dot x=F(x)\) with the stated initial condition. In particular,
\[
 \dot C(t)=\frac{1}{2\kappa d(x(t))}\sum_{a<b}x_{ab}(t)(u_a+u_b),\qquad d(x(t))>0.
\]
This derives the fluid dynamics from the finite stochastic process rather than assuming a representative-density graphon closure.

**3. Universal two-class scalar closure.** For \(q=2\), all discordant edges have type \(\{1,2\}\), so the displayed derivative is constant \(v=(u_1+u_2)/(2\kappa)>0\). At finite \(N\), conditional on a discordant-edge update, the probability of replacing it by a concordant edge equals \((u_1+u_2)/2+o_{\mathbb P}(1)\), uniformly on finite horizons. The number of discordant edges is nonincreasing, and each successful update decreases it by exactly one. On the high-probability uniform-target event the success probability is squeezed between \(h-\varepsilon_N\) and \(h+\varepsilon_N\), where \(h=(u_1+u_2)/2\) and \(\varepsilon_N\to0\). Coupling successive Bernoulli success marks with independent uniforms and using the Poisson-event law gives uniform-on-compact convergence, including the random absorption boundary, to the stopped linear path:
\[
 \sup_{0\le t\le T}\left|C_N(t)-\min\{1,C(0)+vt\}\right|\xrightarrow{\mathbb P}0
\]
for every \(T<\infty\). The same formula applies when the initial concordance is already one. Thus the closure is genuinely universal over the stated sparse initial graph sequences, not merely an initial-derivative identity.

**4. Three-class obstruction, with an exact finite-population check.** Set \(N=3n\), \(K_N=n\), class opinions \(0,2/5,4/5\), tolerance \(1/5\), and give each class \(n\) vertices. The affinities are \(w_{01}=w_{12}=3/5\), \(w_{02}=1/5\), and same-class affinities are one. For the first graph connect each vertex of class \(0\) to one vertex of class \(1\) in a perfect matching; for the second use the corresponding matching between classes \(0\) and \(2\). Both graphs have \(n\) discordant edges, no concordant edges and maximum degree one.

The limiting successful-rewire probabilities at retained class \(0,1,2\) vertices are respectively \(u_0=5/9\), \(u_1=5/11\), \(u_2=5/9\). Thus a random selected discordant edge in the first graph creates concordance with limiting probability \((u_0+u_1)/2=50/99\), while in the second it does so with probability \((u_0+u_2)/2=5/9\). As the event rate is \(3n\) and \(C_N\) increases by \(1/n\) on success, the two fluid slopes are \(50/33\) and \(5/3\). The finite-\(n\) probabilities (with self-loops excluded and the old neighbor still excluded during target sampling) are exactly
\[
 p_{01}(n)=\frac{5(n-1)}2\left(\frac1{9n-8}+\frac1{11n-8}\right),\qquad
 p_{02}(n)=\frac{5(n-1)}{9n-6}.
\]
Direct simplification gives \(p_{02}(n)>p_{01}(n)\) for all integers \(n\ge3\). The two limiting class-edge ODEs start from \(d=1/3>0\), so their distinct derivatives imply distinct concordance trajectories for every sufficiently small positive time. A common single-valued scalar ODE with the same initial concordance cannot have both derivatives. One class is trivially concordant and two classes always have the universal law above, so three classes are the smallest possible for this type of failure.

## Verification
The standalone `check.py` enumerates every eligible target and both possible retained endpoints for the two finite matching configurations at every integer \(3\le n\le34\), using exact rational arithmetic. It checks the two displayed finite probabilities, their strict ordering, the exact limiting slopes and their difference, plus nonuniform two-class affinity identities. It reports PASS. The code checks finite algebra and generator normalization; the infinite-population convergence follows from the martingale/coupling proof above, not from the enumeration.

Run with `python3 check.py` in a directory containing the supplied source file. Only the Python standard library is required.

## Relationship to prior work
Nagel, Winkelmann, Koltai, Djurdjevac Conrad and Lücke (2026) define the fixed-opinion homophilic threshold rewiring process and give a representative-density graphon closure (their equations (21)–(26) and Appendix D), describing it as an approximation and examining the very-sparse formal limit (D37). The present result neither claims their approximation universally exact nor disputes its reported empirical accuracy. It proves a **separate exact sparse stochastic limit** and a sharp, explicit distinction between universal two-class closure and three-class failure; the paper's step-graphon ansatz does not establish these assertions. Kan, Feng and Porter (2023) introduce a related model in which both opinions and edges evolve, mainly studied numerically. Chodrow and Mucha (2020) address moment closure for adaptive binary voter models, which have opinion updates absent here. Cárdenas-Sabando, Cosenza and González-Avella (2025) study stationary active-link mean fields under different rewiring rules, not a verified proof of this fixed-rule sparse closure dichotomy.

## Limitations
The theorem requires finitely many opinion classes, all interclass pairs discordant, positive affinities, \(K_N/N\to\kappa\in(0,1)\), fixed opinions and initially sublinear maximum degree. It does not classify mixed interclass concordance, dense graphs, coevolving opinions or finite-\(N\) exact lumpability. Its three-class obstruction is **existential**, not a claim that every three-class parameter choice fails closure. The original work's general graphon closure is approximate; the present counterexample shows only that no **universal exact scalar** model can represent every allowed sparse initial topology. Priority remains subject to checking other historical sources, including inaccessible full texts of some broadly related models.

## References
- S. Nagel, S. Winkelmann, P. Koltai, N. Djurdjevac Conrad and M. Lücke, *Collective variables for homophily-driven network rewiring dynamics*, arXiv:2606.25872v1 (publicly posted 2026-06-24), https://arxiv.org/abs/2606.25872.
- U. Kan, M. Feng and M. A. Porter, *An adaptive bounded-confidence model of opinion dynamics on networks*, Journal of Complex Networks 11 (2023), cnac055, https://doi.org/10.1093/comnet/cnac055; arXiv:2112.05856.
- P. S. Chodrow and P. J. Mucha, *Local Symmetry and Global Structure in Adaptive Voter Models*, SIAM Journal on Applied Mathematics 80 (2020), 620–638, https://doi.org/10.1137/18M1232346.
- R. Cárdenas-Sabando, M. G. Cosenza and J. C. González-Avella, *Structural transitions induced by adaptive rewiring in networks with fixed states*, arXiv:2511.15043 (2025), https://arxiv.org/abs/2511.15043.
