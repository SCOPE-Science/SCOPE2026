# Exact equilibrium census on balanced complete multipartite networks

## Finding

Let \(r\geq2\) and \(n\geq1\) be integers. On the complete \(r\)-partite graph \(K_{n,\ldots,n}\), every labeled vertex chooses one of two actions, \(0\) or \(1\), and receives one unit for each neighbor with the opposite action and zero for each neighbor with the same action. A pure Nash equilibrium allows equality of payoffs under a unilateral switch. Write \(x_i\in\{0,\ldots,n\}\) for the number of action-\(1\) vertices in part \(i\); call a part *mixed* when \(0<x_i<n\), and let \(t\) be the number of mixed parts and \(h\) the number of monochromatic action-\(1\) parts.

**Complete classification.** A profile is a pure Nash equilibrium if and only if exactly one of these disjoint cases holds:

1. \(t=0\) and \(r-1\leq2h\leq r+1\).
2. \(t=1\), \(r\) is odd, \(h=(r-1)/2\), and the single mixed part has an arbitrary action-\(1\) count in \(\{1,\ldots,n-1\}\).
3. \(2\leq t\leq r\), all mixed parts have the same action-\(1\) count
   \[
   c=\frac{n(r-1-2h)}{2(t-1)},
   \]
   which must be an integer in \(\{1,\ldots,n-1\}\). There are \(r-t-h\) monochromatic action-\(0\) parts.

The exact number \(E_{r,n}\) of labeled pure Nash profiles is
\[
\begin{aligned}
E_{r,n}={}&\sum_{\substack{0\le h\le r\\r-1\le 2h\le r+1}}\binom rh
+\mathbf1_{\{r\ \mathrm{odd}\}}\,r\binom{r-1}{(r-1)/2}(2^n-2)\\
&+\sum_{t=2}^{r}\binom rt\sum_{h=0}^{r-t}
\binom{r-t}{h}\mathbf1_{\{c\in\{1,\ldots,n-1\}\}}\binom nc^{t},
\qquad c=\frac{n(r-1-2h)}{2(t-1)}.
\end{aligned}
\]
The binomial term in the last sum is included only when \(c\) is an admissible integer. The number of summands is polynomial in \(r\), although the count may be exponentially large.

**Tripartite parity corollary.** For \(r=3\), all Nash profiles except one possible family attain maximum social welfare. In particular,
\[
E_{3,n}=6(2^n-1)+\mathbf1_{\{2\mid n\}}\binom n{n/2}^{3}.
\]
The first \(6(2^n-1)\) equilibria have cut size \(2n^2\), hence social welfare \(4n^2\), the optimum over *all* strategy profiles. If \(n\) is even, the remaining \(\binom n{n/2}^{3}\) equilibria split every part equally and have cut size \(3n^2/2\), social welfare \(3n^2\). Consequently the pure price of stability is \(1\) for all \(n\), and the pure price of anarchy is \(1\) when \(n\) is odd and \(4/3\) when \(n\) is even. Among even \(n\), the fraction of equilibrium profiles that attain optimum welfare is asymptotic to
\[
\frac{6(2^n-1)}{6(2^n-1)+\binom n{n/2}^{3}}
\sim\frac{6(\pi n/2)^{3/2}}{4^n}.
\]
For odd \(n\), that fraction is exactly \(1\).

## Assumptions and scope

All vertices and part indices are labeled. The parts are equal in size, all interpart edges are present and have unit weight, within-part edges are absent, both actions are always available, and utility is the *number* rather than the fraction of opposite-action neighbors. All vertices have degree \((r-1)n\), so dividing utility by degree would leave the equilibria unchanged. A unilateral deviation must *strictly* improve payoff to invalidate Nash equilibrium; indifference is allowed. The classification is for deterministic pure profiles, not mixed Nash strategies, logit stationary states, asynchronous best-response dynamics, heterogeneous payoffs, or unequal part sizes. The parity corollary concerns exactly three nonempty equal-sized parts.

## Proof

Fix the action counts \(x_1,\ldots,x_r\), let \(X=\sum_i x_i\), and write \(d=(r-1)n\). A vertex in part \(i\) sees \(X-x_i\) neighbors choosing \(1\) and \(d-(X-x_i)\) choosing \(0\). An action-\(1\) vertex is content precisely when \(2(X-x_i)\le d\); an action-\(0\) vertex is content precisely when \(2(X-x_i)\ge d\). Thus a mixed part forces \(X-x_i=d/2\).

If there are no mixed parts, \(X=hn\). A monochromatic action-\(0\) part is content if \(hn\ge d/2\), and a monochromatic action-\(1\) part is content if \((h-1)n\le d/2\). Both constraints combine to \(r-1\le 2h\le r+1\) whenever both colors occur. The all-zero and all-one profiles fail because \(r\ge2\), and the same displayed inequality already excludes them. This proves the first case.

If exactly one part is mixed with action-\(1\) count \(x\), then that part's neighbors contain precisely \(hn\) action-\(1\) vertices; hence \(hn=d/2\) forces odd \(r\) and \(h=(r-1)/2\). For each monochromatic action-\(1\) part the number of neighboring ones is \((h-1)n+x\le hn=d/2\). For each monochromatic action-\(0\) part it is \(hn+x\ge d/2\). Therefore every \(1\le x\le n-1\) works and there are no others in the second case.

Suppose \(t\ge2\) parts are mixed. The equality \(X-x_i=d/2\) holds for every mixed part, hence their occupancies must be a common integer \(c\). With \(h\) fully action-\(1\) parts, \(X=hn+tc\); the equality becomes \(hn+(t-1)c=d/2\), giving the displayed formula for \(c\). Conversely, any integer \(0<c<n\) satisfying this identity makes every mixed vertex indifferent. Moreover \(X=d/2+c\): a monochromatic action-\(1\) part has \(X-n=d/2+c-n\le d/2\) neighboring ones, and an action-\(0\) part has \(X=d/2+c\ge d/2\) neighboring ones. Thus all its vertices are content. This proves case three, including its converse and all endpoints.

The three cases have distinct values of \(t\), and within each case the chosen mixed parts, the chosen monochromatic one-parts, and the action-\(1\) subsets of each mixed part uniquely specify a labeled profile. The first term of \(E_{r,n}\) selects \(h\) fully one-parts. The second selects the unique mixed part, exactly half of the remaining \(r-1\) parts to be fully one, and any nonconstant binary pattern on its \(n\) labeled vertices. The last selects \(t\) mixed parts, then \(h\) fully one-parts, then chooses \(c\) one-vertices separately in each mixed part. This proves the exact sum without overcounting.

For \(r=3\), the no-mixed case comprises six profiles. The one-mixed case has two opposite monochromatic parts and contributes \(6(2^n-2)\) profiles. With two mixed parts, the formula for \(c\) is either \(0\) or \(n\), which is inadmissible. With three mixed parts it demands \(c=n/2\), giving the stated extra family exactly for even \(n\). In every no-mixed or one-mixed equilibrium two parts are monochromatic and opposite, while the third is arbitrary. There are exactly \(2n^2\) crossing edges: \(n^2\) between the opposite monochromatic parts and a total of \(n^2\) across the remaining two part-pairs. In the three-mixed family each of the three part-pairs contributes \(n^2/2\) crossing edges.

For any coloring with action-\(1\) counts \(x_1,x_2,x_3\), the cut has size
\[
F(x_1,x_2,x_3)=\sum_{1\le i<j\le3}\big[x_i(n-x_j)+(n-x_i)x_j\big].
\]
This is affine in each variable when the other two are fixed, so its maximum on the box \([0,n]^3\) is attained at a corner. A corner means each part is monochromatic. Among the eight corners, six have cut size \(2n^2\) and two have cut size zero. Thus the global optimum is \(2n^2\), and twice the cut is utilitarian welfare because each crossing edge contributes one payoff to both endpoints. The listed Nash profiles therefore have precisely the two welfare values asserted, and the price-of-anarchy and price-of-stability formulas follow.

Finally the central binomial asymptotic \(\binom n{n/2}\sim2^n\sqrt{2/(\pi n)}\) as even \(n\to\infty\) gives the equilibrium fraction asymptotic. The asymptotic is along even integers only.

## Verification

Run `python3 verify.py` in the same directory. This standard-library-only checker uses three cross-checks: it independently enumerates per-part occupancy vectors and their binomial multiplicities for small \(r,n\); it independently enumerates all labeled binary profiles for smaller instances and directly tests each player's actual incident-edge payoff on a unilateral flip; and it checks the tripartite formula against its closed form. It also verifies all tripartite equilibrium welfare multiplicities in those finite instances. It prints `VERIFY_OK macro_cases=34 labeled_cases=17 tripartite_formula_cases=11` on success. These finite checks are not a proof for arbitrary \(r,n\); the proof above handles every positive integer in scope.

## Relationship to prior work

Deligkas, Eiben, Gutin, Neary and Yeo (2023, arXiv:2311.03195) study binary-action anti-coordination polymatrix games and the difficulty of finding welfare-optimizing outcomes; the present equal-payoff game is a homogeneous specialization, but the paper's inspected definitions, theorems and appendices do not state this complete multipartite census or the tripartite parity-and-count conclusion. Lampis (2021, arXiv:2104.13097) identifies Nash profiles in this homogeneous game with locally maximal cuts and studies general algorithms and complexity for minimum stable cuts, not the closed counting formula on balanced complete multipartite graphs. Cao and Yang (2012, arXiv:1201.0410), building on Bramoullé (2007), examine anti-coordination and a maximum independent-cut problem in an asymmetric-payoff regime; that restriction does not determine the symmetric equal-payoff equilibrium census here. The familiar potential/Max-Cut equivalence and binomial asymptotic are prior facts, not novelty claims.

## Limitations

The census explicitly permits indifferent players; an arbitrarily small payoff asymmetry can change it. The complete multipartite formula is restricted to equal part sizes and identical unit edge payoffs. The tripartite welfare result does not assert an efficiency theorem for other numbers of parts. The classification is deterministic pure Nash stability, not dynamic selection or social prediction. No assertion is made that all equivalent results have been excluded from every unindexed work. A relevant earlier published study by Bramoullé (2007) was available through abstract and a subsequent full-text exposition, but its original full article was not inspected. There has been no independent external mathematical audit.

## References

1. Deligkas, A., Eiben, E., Gutin, G., Neary, P. R., and Yeo, A., *Some coordination problems are harder than others*, arXiv:2311.03195 (first submission 2023-11-06). https://arxiv.org/abs/2311.03195
2. Lampis, M., *Minimum Stable Cut and Treewidth*, arXiv:2104.13097 (first submission 2021-04-27). https://arxiv.org/abs/2104.13097
3. Cao, Z., and Yang, X., *A note on anti-coordination and social interactions*, arXiv:1201.0410 (first submission 2012-01-02). https://arxiv.org/abs/1201.0410
4. Bramoullé, Y., *Anti-coordination and social interactions*, Games and Economic Behavior 58(1), 30–49 (2007), DOI:10.1016/j.geb.2005.12.006. https://doi.org/10.1016/j.geb.2005.12.006
