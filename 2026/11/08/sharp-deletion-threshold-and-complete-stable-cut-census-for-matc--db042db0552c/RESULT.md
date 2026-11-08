# Sharp deletion threshold and complete stable-cut census for matching-deleted bicliques

## Finding
Consider a complete bipartite interaction network on two named sets of \(n\) vertices, and delete exactly \(t\) edges from a matching, where \(n\ge2\) and \(1\le t\le n\). In the homogeneous two-action anti-coordination game, each vertex gains one payoff unit from every neighbor taking the opposite action. A pure Nash equilibrium permits indifference.

**Theorem.** Write \(G_{n,t}=K_{n,n}\setminus\{a_i b_i:1\le i\le t\}\) and let \(E_{n,t}\) count all labeled pure Nash action profiles. With \(\binom uv=0\) when \(v\notin\{0,\ldots,u\}\),
\[
E_{n,t}=\begin{cases}
2+\displaystyle\sum_{k=0}^{t}\binom tk\binom{n-t}{n/2-k}^{\!2},&n\text{ even},\\[7pt]
2+2\binom{t}{(n+1)/2}
+2\mathbf1_{\{t=n-1\}}\binom{n-1}{(n-1)/2}
+2\mathbf1_{\{t=n\}}n\binom{n-1}{(n-1)/2},&n\text{ odd}.
\end{cases}
\]
The two profiles assigning opposite uniform actions to the bipartition classes are always socially optimal, with cut size \(n^2-t\). Every other equilibrium has one of the following cut sizes:

- For even \(n\), the cut size is exactly \(n^2/2\).
- For odd \(n\), the cut size is \((n^2-1)/2\), except that when \(t=n-1\), an additional \(2\binom{n-1}{(n-1)/2}\) equilibria have cut size \((n^2+1)/2\).

Consequently **odd population sizes exhibit a sharp contact-deletion threshold**: for odd \(n\), all Nash equilibria maximize welfare when \(t<(n+1)/2\), and inefficient equilibria first appear when \(t=(n+1)/2\). The (pure) price of anarchy, defined as the optimal social welfare divided by the minimum equilibrium welfare, is
\[
\operatorname{PoA}(G_{n,t})=
\begin{cases}
\dfrac{2(n^2-t)}{n^2},& n\text{ even},\\[7pt]
1,&n\text{ odd and }t<(n+1)/2,\\[4pt]
\dfrac{2(n^2-t)}{n^2-1},&n\text{ odd and }t\ge(n+1)/2.
\end{cases}
\]
The price of stability is always \(1\). The endpoint \(t=n\) is the classical crown graph; its equilibrium count is \(2+\binom n{n/2}\) for even \(n\), and \(2+2\binom n{(n-1)/2}+2n\binom{n-1}{(n-1)/2}\) for odd \(n\). The values for \(t=0\) given by the same formulas are a comparison baseline, not claimed as a new result.

## Assumptions and scope
Let \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). The only missing edges relative to \(K_{n,n}\) are the disjoint cross-edges \(a_ib_i\) for \(i\le t\). All remaining edges have equal positive weight; each vertex has one of the two actions \(-1,+1\). Players maximize the number of incident edges crossing the action cut, and switching at equal payoff does not invalidate Nash equilibrium. Both sides are labeled and the actions are distinguished. This is an ordinary static game, with no random updating, strategic edge changes, asymmetric incentives, or mixed strategies. Social welfare equals twice the cut size.

## Proof
**1. Exact equilibrium inequalities.** Denote the actions on the two vertex classes by \(\sigma_i,\tau_i\in\{-1,+1\}\), and their sums by \(X=\sum_i\sigma_i\) and \(Y=\sum_i\tau_i\). For a vertex on the \(A\) side, switching changes the number of disagreeing neighbors by the signed sum of its neighbors times its present action. Therefore absence of a profitable switch is equivalent to
\[
\sigma_i\bigl(Y-\mathbf1_{\{i\le t\}}\tau_i\bigr)\le0,
\qquad
\tau_i\bigl(X-\mathbf1_{\{i\le t\}}\sigma_i\bigr)\le0
\quad(1\le i\le n).
\]
These inequalities retain ties, rather than imposing a deterministic best-response tie rule.

**2. Reduction to small magnetizations.** If \(Y\ge2\), then \(Y-\mathbf1_{\{i\le t\}}\tau_i\ge1\) for every \(i\); thus all \(\sigma_i=-1\). Since \(n\ge2\), the second inequality then forces all \(\tau_i=+1\). The cases \(Y\le-2\) and \(\lvert X\rvert\ge2\) are symmetric. Hence every equilibrium outside the two opposite-uniform profiles satisfies \(\lvert X\rvert,\lvert Y\rvert\le1\).

**3. Even case.** For even \(n\), both sums are even integers, so \(X=Y=0\). For every deleted pair \(i\le t\), the inequalities reduce to \(\sigma_i\tau_i\ge0\), forcing \(\sigma_i=\tau_i\). The unmatched pairs are unconstrained locally. If \(k\) of the \(t\) deleted pairs have action \(+1\), then each side must select \(n/2-k\) of its \(n-t\) unmatched vertices for \(+1\). This gives \(\binom tk\binom{n-t}{n/2-k}^2\) profiles, and every such profile satisfies all inequalities. Adding the two opposite-uniform equilibria proves the even formula.

**4. Odd case.** Set \(n=2m+1\), so \(X,Y\in\{-1,+1\}\) outside the two uniform profiles. If \(X=Y=1\), a deleted pair with \(\tau_i=-1\) forces \(\sigma_i=-1\), while a deleted pair with \(\sigma_i=-1\) forces \(\tau_i=-1\). Hence deleted pairs agree, and every undeleted pair has both actions \(-1\). There must be exactly \(m+1\) positive deleted pairs, giving \(\binom t{m+1}\) profiles. If \(X=Y=-1\), the action-reversed argument gives the same count.

If \(X=1\) and \(Y=-1\), every undeleted pair has \((\sigma_i,\tau_i)=(+1,-1)\), and each deleted pair satisfies \(\sigma_i\ge\tau_i\). Every such unequal pair contributes \(2\) to \(X-Y=2\). Thus, writing \(u=n-t\) for the number of undeleted pairs and \(d\) for the number of unequal deleted pairs, \(u+d=1\). It follows that this sign case is impossible when \(t\le n-2\); when \(t=n-1\), all deleted pairs agree, with exactly \(m\) positive pairs, giving \(\binom{n-1}m\) profiles; when \(t=n\), there is exactly one unequal deleted pair, with \(+1\) on its \(A\) endpoint, and among the remaining \(n-1\) equal pairs exactly \(m\) are positive, giving \(n\binom{n-1}m\) profiles. Reversing actions and sides gives equal counts for \(X=-1,Y=1\). This exhausts all four sign cases and proves the odd formula, necessity and sufficiency.

**5. Welfare and threshold.** On \(K_{n,n}\), the number of crossing edges is \((n^2-XY)/2\). Deleting the \(t\) disjoint edges subtracts the number of unequal deleted pairs. In the even mixed class there are zero unequal deleted pairs and \(XY=0\), so every mixed equilibrium has cut \(n^2/2\). For odd equal-sign classes, \(XY=1\) with no unequal deleted pairs, giving \((n^2-1)/2\). The exceptional \(t=n-1\) cross-sign classes have \(XY=-1\) and no unequal deleted pairs, giving \((n^2+1)/2\). The \(t=n\) cross-sign classes have \(XY=-1\) and exactly one unequal deleted pair, giving \((n^2-1)/2\). Every edge of the bipartite graph can be cut simultaneously, so the global maximum is \(n^2-t\). The claimed worst-equilibrium cut values, the odd threshold, and both welfare ratios follow. For the boundary \(n=t=2\), all four equilibria are optimal; the formulas still give price of anarchy \(1\).

## Verification
Run `python3 verify.py` from the directory containing this document and `verify.py`. The checker independently enumerates all binary action profiles for \(2\le n\le8\) and every \(0\le t\le n\), computes individual unilateral incentives from the graph's adjacency, tests the separate predicted classification, and checks the exact labeled-count and cut-size histogram formulas. It passes \(42\) network instances and \(757296\) tested profiles, including the comparison case \(t=0\) and the special boundary \(n=t=2\). Finite enumeration is a regression test, not a proof for arbitrary \(n\); the five steps above provide that proof.

Illustrations: \(G_{5,2}\) has only the two efficient equilibria; \(G_{5,3}\) has four equilibria, two inefficient, with minimum cut \(12\); \(G_{5,4}\) has \(22\) equilibria, including \(8\) with cut \(12\) and \(12\) with cut \(13\); the crown graph \(G_{5,5}\) has \(82\) equilibria, of which \(80\) have cut \(12\). These follow from the exact formula and are checked by `verify.py`.

## Relationship to prior work
Qiu et al. study equilibrium existence and convergence of networked anti-coordination games, including a distinction between self-essential and self-nonessential update schemes; the present theorem is a static weak-inequality Nash census for a homogeneous game on a precisely specified matching-deleted bipartite network. Deligkas et al. study the computational difficulty of welfare objectives in general binary-action polymatrix games; this theorem instead gives an explicit complete equilibrium set and exact worst-equilibrium welfare for a structured graph family. Lampis studies the complexity of minimum stable cut, and the well-known stable-cut/Nash equivalence and generic one-half lower bound; those general results do not provide the matching-deletion counting formula or the odd-population threshold. Vanelli et al. count equilibria in all-to-all networks, but their interaction graph has no missing paired ties.

The \(t=0\) complete-bipartite count is a known comparison baseline; the contribution begins at positive matching deletion. Published results about crown graphs' domination or coloring invariants concern different problems and do not imply the equilibrium census. The result does not assert that a database search proves priority; an unindexed equivalent classification remains possible.

## Limitations
This is a homogeneous undirected, unweighted, two-action static model with ties accepted. With deterministic tie-breaking that eliminates indifferent action profiles, the counts generally differ. The result does not classify arbitrary edge deletions, weighted edges, asymmetric payoff matrices, arbitrary multipartite networks, stochastic dynamics, or mixed-strategy equilibria. The structural proof is complete under its hypotheses, but mathematical-priority uncertainty remains because not all relevant literature can be guaranteed indexed. There has been no independent external audit.

## References
1. Z. Qiu, C. Chen, M. V. Marathe, S. S. Ravi, D. J. Rosenkrantz, R. E. Stearns, and A. Vullikanti. *Networked Anti-Coordination Games Meet Graphical Dynamical Systems: Equilibria and Convergence*. arXiv:2301.02889, first released 2023-01-07. https://arxiv.org/abs/2301.02889
2. A. Deligkas, E. Eiben, G. Gutin, P. R. Neary, and A. Yeo. *Some coordination problems are harder than others*. arXiv:2311.03195, 2023. https://arxiv.org/abs/2311.03195
3. M. Lampis. *Minimum Stable Cut and Treewidth*. arXiv:2104.13097, first released 2021-04-27. https://arxiv.org/abs/2104.13097
4. M. Vanelli, L. Arditti, G. Como, and F. Fagnani. *On games with coordinating and anti-coordinating agents*. arXiv:1912.02000, 2019. https://arxiv.org/abs/1912.02000
5. E. W. Weisstein. *Crown Graph*. MathWorld. https://mathworld.wolfram.com/CrownGraph.html
