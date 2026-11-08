# A square-root crossover in the probability of fair orientations of multistars

## Finding
Consider a multistar with a central agent and \(k\ge2\) leaf agents. There are \(r_i\ge1\) distinct parallel goods between the center and leaf \(i\); each good is worth one to its two endpoint agents and zero to everyone else. Each good is independently assigned with probability \(1/2\) to either endpoint. We require **EFX including zero-valued goods**: for all agents \(u,v\) and all goods \(g\) assigned to \(v\), agent \(u\)'s value for her own bundle is at least her value for \(v\)'s bundle after removing \(g\).

Write \(X_i\sim\operatorname{Bin}(r_i,1/2)\) for the independent numbers of goods assigned to the leaves and \(Y_i=r_i-X_i\). Then the random orientation is EFX **if and only if**
\[
\sum_{j=1}^kY_j+1\ge\max_i X_i,\qquad
X_i\ge Y_i-\mathbf1\!\left\{\sum_{j\ne i}Y_j=0\right\}\quad(1\le i\le k).
\]
Consequently, for any positive integer multiplicities, its exact probability equals
\[
2^{-\sum_i r_i}\sum_{0\le x_i\le r_i}
 \left(\prod_i\binom{r_i}{x_i}\right)
 \mathbf1\!\left\{\sum_i(r_i-x_i)+1\ge\max_i x_i\right\}
 \prod_i\mathbf1\!\left\{x_i\ge r_i-x_i-\mathbf1\{\sum_{j\ne i}(r_j-x_j)=0\}\right\}.
\]

There is a sharp supply crossover when one spoke dominates. Fix \(k\ge2\). Let \(r_1=m\to\infty\), let all \(r_i=r_i(m)\to\infty\) for \(i\ge2\), and put \(R_m=\sum_{i=2}^k r_i=o(m)\). Denote the probability of EFX by \(p_m\), and let \(\Phi\) be the standard Gaussian distribution function. If \(R_m/\sqrt m\to\gamma\in[0,\infty)\), then
\[
\boxed{\lim_{m\to\infty}p_m=2^{-(k-1)}\bigl(\Phi(\gamma/2)-1/2\bigr).}
\]
If \(R_m/\sqrt m\to\infty\), still with \(R_m=o(m)\), then \(p_m\to2^{-k}\). In the strictly subcritical case \(R_m=o(\sqrt m)\), the vanishing probability has the **sharp equivalent**
\[
\boxed{p_m\sim\frac{2^{-(k-1)}R_m}{2\sqrt{2\pi m}}.}
\]
Thus the aggregate multiplicity on the subsidiary spokes needs to reach the square-root scale of the dominant multiplicity before a uniformly random non-wasteful assignment has a nonzero limiting chance of EFX.

## Assumptions and scope
All multiplicities are positive integers. Items are labeled, each orientation is uniformly selected from the \(2^{\sum_i r_i}\) endpoint assignments, and only these non-wasteful orientations are counted. Every incident good has unit additive value; nonincident goods have value zero. The strong, zero-inclusive EFX convention matters: removing a nonincident good from the center's bundle cannot relieve a leaf's envy. The asymptotic limit keeps the number \(k\) of leaves fixed; it allows different subsidiary multiplicities but requires each to diverge. Nothing is claimed for arbitrary valuations, correlated assignments, non-star graphs, or growing \(k\).

## Proof
**Exact orientation criterion.** Leaf \(i\)'s own value is \(X_i\); the center holds \(Y_i\) goods on spoke \(i\). If the center also holds any good on another spoke, removal of that zero-valued-to-\(i\) good leaves leaf \(i\)'s value for the center's bundle at \(Y_i\). Otherwise, if the center holds any goods, every deletion reduces that value to \(Y_i-1\). Thus the leaf's EFX constraint is exactly
\(X_i\ge Y_i-\mathbf1\{\sum_{j\ne i}Y_j=0\}\).
The center has own value \(S=\sum_iY_i\). Leaf \(i\)'s bundle contains only goods valued at one by the center. Deleting any one of them leaves value \(X_i-1\), whenever the bundle is nonempty. Hence all the center's EFX constraints are equivalent to \(S+1\ge\max_i X_i\). Other pairs of leaves assign zero value to each other's bundles and are automatically EFX. These conditions are necessary and sufficient; summing the independent binomial point masses proves the finite formula.

**Exact dominant-spoke reduction.** Put \(m=r_1\) and \(R=\sum_{i=2}^k r_i\), and suppose \(m>3R+2\). Write \(Y=\sum_{i=2}^k(r_i-X_i)\) and \(B=\bigcap_{i=2}^k\{X_i\ge\lceil r_i/2\rceil\}\). The center's constraint against leaf one gives \(2X_1\le m+Y+1\le m+R+1\), so \(Y_1=m-X_1\ge(m-R-1)/2>R\). Consequently every subsidiary leaf sees a zero-valued-to-it good in the center's bundle, and its EFX condition is precisely the corresponding event in \(B\). The center's other EFX conditions hold because \(Y_1>R\ge X_i\) for \(i\ge2\). If \(Y>0\), leaf one requires \(X_1\ge\lceil m/2\rceil\); if \(Y=0\), it instead requires \(2X_1\ge m-1\). Therefore, with \(Z_m\sim\operatorname{Bin}(m,1/2)\) independent of the subsidiary counts, define
\[
H_m(y)=\Pr\!\left(\left\lceil\frac m2\right\rceil\le Z_m\le\left\lfloor\frac{m+y+1}{2}\right\rfloor\right).
\]
The following **finite exact identity** holds for every \(m>3R+2\):
\[
\boxed{p_m=\mathbb E[\mathbf1_B H_m(Y)]+\mathbf1_{\{m\text{ odd}\}}2^{-R}\Pr(Z_m=(m-1)/2).}
\]
The last term is the single extra configuration \(Y=0\), \(X_1=(m-1)/2\), which is admissible only for odd \(m\). Notice that this correction is not dropped in the finite assertion.

**Gaussian and supercritical windows.** Since the subsidiary counts are independent symmetric binomials and all their multiplicities diverge, \(\Pr(B)\to2^{-(k-1)}\). Moreover \(\mathbb EY=R/2\) and \(\operatorname{Var}(Y)=R/4\). As \(R\to\infty\), Chebyshev's inequality gives \(Y/R\to1/2\) in probability, also conditionally on \(B\), because the latter's probability stays bounded away from zero. The central binomial normal approximation, with standardized variable \((2Z_m-m)/\sqrt m\), gives \(H_m(Y)\to\Phi(\gamma/2)-1/2\) in probability whenever \(R/\sqrt m\to\gamma<\infty\); for \(R/\sqrt m\to\infty\), it gives \(H_m(Y)\to1/2\). The exceptional correction is bounded by \(O(2^{-R}m^{-1/2})\) and vanishes. Bounded convergence establishes both limiting formulas.

**Sharp subcritical equivalent.** If \(R=o(\sqrt m)\), the central binomial local limit estimate is uniform for \(|z-m/2|\le R+2\):
\[
\Pr(Z_m=z)=\sqrt{\frac2{\pi m}}\,(1+o(1)).
\]
On \(B\), the number of admissible integers in \(H_m(Y)\) equals \(Y/2+O(1)\). Thus \(H_m(Y)=\bigl(Y+O(1)+o(R)\bigr)/\sqrt{2\pi m}\), uniformly for \(0\le Y\le R\). Also \(\mathbb E[\mathbf1_B Y]\sim (R/2)\Pr(B)\), using \(Y/R\to1/2\) and boundedness. The \(O(1)\) lattice term is negligible since \(R\to\infty\), and the exceptional correction is negligible. This yields \(p_m\sim2^{-(k-1)}R/(2\sqrt{2\pi m})\), as claimed.

## Verification
Run `python3 verification/check_multistar.py` with a standard Python 3 installation. It enumerates all individually oriented labeled edges for 85 small multistars and compares the literal EFX inequalities (including deletions of nonincident goods) against the reduced count criterion. It also checks the exact dominant-spoke binomial-slice expression against exhaustive finite counts for qualifying small parameters, using integer arithmetic. The finite tests are consistency checks, not an infinite proof; the latter is supplied above by deterministic reduction, binomial central limit and local limit estimates.

## Relationship to prior work
Afshinmehr, Ashuri, Mahmoudkhan, Mehlhorn and Shahrezaei (2026) prove general **existence** of EFX allocations for multigraph valuations under cancelable utilities. Afshinmehr, Danaei, Kazemi, Mehlhorn and Rathi (2026), especially their Sections 2--4 and Proposition 4.3, analyze EFX **orientations** on bipartite multigraphs and establish existence on multistars, but their statements address existence/computation rather than the probability of a uniformly random orientation satisfying zero-inclusive EFX. Neoh and Teh (2025) study the number of EFX allocations for general domains with goods close to the number of agents; the present independent-binomial, multi-edge multistar square-root crossover is a different natural counting regime. A random-orientation EFX success probability is not implied by an existential orientation theorem or by general counting hardness.

## Limitations
This is a single-model exact and asymptotic result, not a guarantee for arbitrary valuation functions or allocation procedures. Other models may employ the weaker convention that ignores deletions of zero-valued goods, for which these formulas should not be reused. The asymptotic result assumes \(k\) fixed and each subsidiary multiplicity diverging; cases with bounded subsidiary multiplicity have different lattice constants. Relevant unindexed or inaccessible literature may contain equivalent probability calculations. Independent validation has not been carried out.

## References
1. M. Afshinmehr, A. Ashuri, P. Mahmoudkhan, K. Mehlhorn and A. M. Shahrezaei, *EFX Allocations Exist on Multi-Graphs*, arXiv:2606.18665v1, first posted 2026-06-17. https://arxiv.org/abs/2606.18665
2. M. Afshinmehr, A. Danaei, M. Kazemi, K. Mehlhorn and N. Rathi, *EFX Allocations and Orientations on Bipartite Multi-Graphs: A Complete Picture*, Autonomous Agents and Multi-Agent Systems 40, article 32 (2026), DOI:10.1007/s10458-026-09754-8. https://link.springer.com/article/10.1007/s10458-026-09754-8
3. T. Y. Neoh and N. Teh, *Understanding EFX Allocations: Counting and Variants*, AAAI 2025, DOI:10.1609/aaai.v39i13.33536. https://ojs.aaai.org/index.php/AAAI/article/view/33536
