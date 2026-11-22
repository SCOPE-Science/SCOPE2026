# Marked rare-routing obstructions and the diameter transition in unbalanced random bipartite tournaments

## Finding

For integers \(m,n\geq 2\), orient every edge of the complete bipartite graph \(K_{m,n}\) independently and fairly. The left and right vertex sets are \(L=[m]\) and \(R=[n]\). Put \(S_i=\{r\in R:i\to r\}\) for each \(i\in L\), and let \(d(i,j)\) denote directed distance, with value \(+\infty\) when no directed path exists. An *obstruction* is an ordered pair \((i,j)\) of distinct left vertices with \(d(i,j)>2\), equivalently \(S_i\subseteq S_j\).

Let \(n\to\infty\) and let positive integers \(m=m_n\) satisfy
\[
m_n(m_n-1)(3/4)^n\longrightarrow\lambda\in(0,\infty).
\]
For each obstruction \((i,j)\), attach the location and standardized left outdegrees
\[
\left(\frac{i}{m_n},\frac{j}{m_n},
\frac{|S_i|-n/3}{\sqrt{2n/9}},
\frac{|S_j|-2n/3}{\sqrt{2n/9}}\right).
\]
The point measure of all these marked obstructions converges in distribution to a Poisson point process on \([0,1]^2\times\mathbb R^2\) with intensity
\[
\lambda\,du\,dv\,\mathcal N_2\!\left(0,
\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}\right)(dz_1,dz_2).
\]
Thus the obstruction count converges to \(\operatorname{Pois}(\lambda)\); conditional on any fixed positive number of limit points, their locations are independent uniform ordered pairs, and their degree marks are independent centered bivariate normals of correlation \(1/2\). With probability tending to one, all obstruction pairs have pairwise disjoint vertex sets.

Let \(\Delta_{m,n}=\max_{x\ne y}d(x,y)\) be directed diameter, permitting \(+\infty\). In the same regime,
\[
\Pr(\Delta_{m,n}=3)\to e^{-\lambda},\qquad
\Pr(\Delta_{m,n}=4)\to1-e^{-\lambda}.
\]
More precisely, with \(X_{m,n}\) the number of left ordered obstructions,
\[
\Pr\bigl(\Delta_{m,n}\ne3+\mathbf1_{\{X_{m,n}>0\}}\bigr)
\le 2m2^{-n}+n(n-1)(3/4)^m+2mn(3/4)^{m-1}.
\]
This bound holds for every \(m,n\ge2\). In the specified regime the right side tends to zero. Consequently failure of diameter three is caused by a finite Poisson population of highly atypical left-vertex pairs: their outward degrees concentrate near one-third and two-thirds of the smaller part, rather than the typical one-half.

## Assumptions and scope

All \(mn\) orientations are mutually independent fair coin flips. Loops and edges within either part are absent. The limit assumes \(\lambda\) fixed strictly between zero and infinity; it makes no claim about biased orientations or other growth regimes. The point process is considered with its ordinary weak/vague topology on the compact location square times the noncompact mark plane. The first two coordinates are *ordered* endpoints; there is no quotient by pair reversal. Equality of two subsets is allowed in the obstruction definition but asymptotically negligible.

## Proof

**1. Exact obstruction identity and local dependencies.** For distinct \(i,j\in L\), a directed two-step path \(i\to r\to j\) exists exactly when \(r\in S_i\setminus S_j\). Hence \(d(i,j)>2\) iff \(S_i\subseteq S_j\). Each coordinate of \((\mathbf1_{r\in S_i},\mathbf1_{r\in S_j})\) is uniform on its four binary possibilities; the inclusion event excludes only \((1,0)\). Therefore its probability is \(a_n=(3/4)^n\).

Events indexed by two ordered pairs of left vertices are independent when their endpoint sets are disjoint. For two distinct pairs sharing a left source or a left target, the probability of their joint occurrence is \((5/8)^n\). For pairs forming a directed inclusion chain it is \((1/2)^n\), as it is for the two opposite ordered pairs of the same endpoints. Thus all distinct overlapping pairs have joint probability at most \((5/8)^n\), except that a reversed pair has probability \((1/2)^n\), which is also below this bound.

**2. Mark law for one obstruction.** Conditional on \(S_i\subseteq S_j\), independent coordinates take values \((0,0),(0,1),(1,1)\), each with conditional probability \(1/3\). The two single-coordinate indicators have respective means \(1/3,2/3\), common variance \(2/9\), and covariance \(1/9\). The multivariate Lindeberg–Lévy central limit theorem yields the stated bivariate normal distribution for standardized degrees, with correlation \(1/2\). This conditional distribution is identical for all distinct ordered pairs \((i,j)\).

**3. Marked Poisson convergence.** Fix finitely many disjoint continuity sets in the location–mark space. For each ordered pair and each cell, use the indicator that the pair is obstructed and its location/degree mark belongs to that cell. These are dissociated Bernoulli events: each depends only on the independent orientations incident to its two left vertices. A dependency graph joins two such indicators if their underlying ordered pairs share at least one left vertex. The standard multivariate Stein–Chen local-dependence bound for the vector of counts has error bounded by a constant (depending only on the number of cells) times
\[
m^3a_n^2+m^3(5/8)^n+m^2(1/2)^n.
\]
Same-pair indicators assigned to different disjoint cells are mutually exclusive; they add only to the first term. The bound tends to zero because \(m^2a_n\to\lambda\), \((5/8)/(3/4)^{3/2}=5/(3\sqrt3)<1\), and \((1/2)/(3/4)=2/3<1\). The limiting mean in each cell is given by a Riemann sum over distinct ordered indices combined with the conditional bivariate central limit theorem. It equals the indicated Poisson intensity of that cell. The limiting normal mark law is tight, and the total point count has bounded expectation; hence convergence of all finite collections of continuity-set counts yields convergence of the marked point measure. The expected number of overlapping obstruction pairs obeys the same vanishing dependency bound, establishing asymptotic pairwise disjointness. Notice that no unjustified convergence of all ordinary moments is used; the unmarked count can have divergent high moments despite its Poisson distributional limit.

**4. A deterministic diameter reduction with explicit error.** Let \(E_{m,n}\) be the event on which (a) every left vertex has both an outgoing and an incoming neighbor in the right part; (b) every two distinct right vertices are linked by a directed path of length two in each ordered direction; (c) every ordered pair of opposite-part vertices has a directed path of length at most three. For (a), the union bound gives probability of failure at most \(2m2^{-n}\). For each ordered pair of right vertices, failure of a two-step path has probability \((3/4)^m\), giving a bound \(n(n-1)(3/4)^m\) for (b).

Condition on all orientations incident to a fixed left vertex \(i\). If its outgoing neighborhood is nonempty and the arc from a left vertex \(i\) to a right vertex \(j\) is absent, choose \(r\in S_i\); necessarily \(r\ne j\). For each other left vertex \(k\), the two independent arcs \(r\to k\) and \(k\to j\) form a three-step path with probability \(1/4\), independently across \(k\). The chance that no such route exists is at most \((3/4)^{m-1}\). If instead \(j\to i\) is absent, choose \(r\notin S_i\) and use independent routes \(j\to k\to r\to i\) to obtain the same bound. A union bound over the \(2mn\) ordered cross-part pairs establishes
\[
\Pr(E_{m,n}^c)\le2m2^{-n}+n(n-1)(3/4)^m+2mn(3/4)^{m-1}.
\]

On \(E_{m,n}\), all right-to-right distances are two, all cross-part distances are at most three, and every left vertex has an outgoing right neighbor. If no left obstruction exists, all left-to-left distances are two, so the diameter is at most three. At least one cross-part pair requires three steps because each left vertex has both types of incident arcs; hence the diameter is exactly three. If some left obstruction \((i,j)\) exists, its left-to-left distance is at least four by bipartite parity. Choose an outgoing neighbor \(r\) of \(i\); since \(r\to j\) is reachable in at most three steps, \(i\to j\) is reachable in at most four. The same argument works for every left ordered pair, proving diameter exactly four. The error bound follows.

Finally \(m^2(3/4)^n\to\lambda\) implies \(m=\Theta((4/3)^{n/2})\), so each term in the error bound vanishes. Combining with the Poisson obstruction-count limit proves both diameter probabilities.

## Verification

The standalone file `check.py` uses exhaustive independent orientation enumeration for several small bicliques, directed breadth-first distances, and exact fraction computations for all one-, two-, and three-row coordinate configurations. Running `python3 check.py` passed **79,561 assertions**. It verifies the deterministic obstruction identity, the implication from the good routing event to diameter three or four, the rates \((3/4)^n,(5/8)^n,(1/2)^n\), and the bivariate single-coordinate covariance. It does not establish the limiting Poisson process or replace the analytical probability bounds.

## Relationship to prior work

Dudley Stark, *Convergence in distribution for subset counts between random sets* (2004), DOI 10.37236/1812, proves a Poisson approximation for the **unmarked number** of comparable pairs of Bernoulli random subsets, in a general retention model. That count limit is used and credited here as prior knowledge; the count marginal is **not** the originality claim. Stark also records the three allowed single-coordinate configurations conditional on inclusion. The new assessed object is the **full marked point process of exceptional source/target degrees and ordered vertex positions**, together with the **directed diameter-three/four distribution and quantitative routing reduction** in unbalanced randomly oriented complete bipartite graphs. The marker independence and network routing assertions require separate arguments supplied above.

Moon and Moser (1962) and Bollobás, Frank and Karoński (1983) study directed four-cycle counts in bipartite tournaments; their publicly accessible summaries do not state the marked-diameter result. Choi, Eoh, Kim and Lee (2016) analyze the undirected \((1,2)\)-step **competition graph** derived from a bipartite tournament and prove bounds for that derived graph's diameter, not the directed diameter of the underlying tournament. Its accessible full arXiv article contains neither an independently random orientation law nor the present degree-marked Poisson threshold. Classical Poisson-approximation theorems supply proof methodology, not a standalone evaluation of these network marks and diameter. Searches for the exact degree-marked obstruction profile, directed diameter transition, the Boolean-subset alias, and prior result collections found no decisive stronger statement. This is a best-knowledge priority comparison, not a proof of uniqueness.

## Limitations

This theorem treats only fair independent orientations and the exponential-imbalance critical window. The full primary texts of some early bipartite-tournament studies were not accessible for line-by-line comparison, so historical priority is qualified. Stark's unmarked Poisson theorem covers part of the mathematics: the claimed contribution should not be described as discovery of the unmarked comparability threshold. The multivariate Stein–Chen inequality is a standard external theorem invoked with explicitly verified local-dependence estimates; the finite checker does not independently certify that theorem.

## References

1. D. Stark, *Convergence in distribution for subset counts between random sets*, Electronic Journal of Combinatorics **11** (2004), R59; first publicly published 2004-09-09. https://doi.org/10.37236/1812
2. J. W. Moon and L. Moser, *On the distribution of 4-cycles in random bipartite tournaments*, Canadian Mathematical Bulletin **5** (1962), 5–12. https://doi.org/10.4153/CMB-1962-002-0
3. B. Bollobás, O. Frank and M. Karoński, *On 4-cycles in random bipartite tournaments*, Journal of Graph Theory **7** (1983), 183–194. https://doi.org/10.1002/jgt.3190070207
4. A. D. Barbour, L. Holst and S. Janson, *Poisson Approximation*, Oxford University Press (1992), especially multivariate and local-dependence Poisson approximation.
5. J. S. Bagga and L. W. Beineke, *A survey of bipartite tournaments* (2025), https://doi.org/10.22049/cco.2025.30326.2415 (historical bibliographic context only).
6. J. Choi, S. Eoh, S.-R. Kim and S. J. Lee, *On \((1,2)\)-step competition graphs of bipartite tournaments*, arXiv:1611.01901 (2016-11-07), https://arxiv.org/abs/1611.01901 (distinct derived-graph diameter).
