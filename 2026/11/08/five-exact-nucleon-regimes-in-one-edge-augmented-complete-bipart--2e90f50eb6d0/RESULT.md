# Five exact nucleon regimes in one-edge-augmented complete bipartite matching games

## Finding
For every pair of integers \(a\ge2\), \(b\ge1\), take a complete bipartite graph \(K_{a,b}\) with sides \(A\) and \(B\), and add the single edge \(uv\) joining two marked vertices \(u,v\in A\). Give each graph edge unit weight and define a transferable-utility matching game by \(v(S)=\nu(G[S])\). Its multiplicative nucleon is a singleton. The unique efficient payoff \(x\) is

\[
\begin{array}{c|ccc}
\text{regime}&x_u=x_v&x_{A\setminus\{u,v\}}&x_B\\\hline
 a<b&1&1&0\\
 a=b&2/3&2/3&1/3\\
 a=b+1&b/(2b+1)&b/(2b+1)&b/(2b+1)\\
 a=b+2&1/2&1/4&3/4\\
 a\ge b+3&1/2&0&1
\end{array}
\]

The matching-game core is empty exactly when \(a=b+1\). In that case the optimal minimum proper-coalition payoff/value ratio is \(2b/(2b+1)\); in all other cases it is \(1\).

## Assumptions and scope
The graph is finite, simple, unweighted, and has exactly the described edges. Here \(a\ge2\), \(b\ge1\), the endpoints \(u,v\) are distinct, \(x(S)=\sum_{i\in S}x_i\), and the imputation domain is \(x_i\ge0\) and \(x(V)=v(V)\). For each nonempty proper coalition \(S\subsetneq V\) with \(v(S)>0\), form the ratio \(x(S)/v(S)\). Sort every such ratio in nondecreasing order, retaining multiplicities, and maximize the resulting vector lexicographically. This is the multiplicative *nucleon*, not the additive nucleolus; no assumption of a nonempty core is made.

Write \(A^\circ=A\setminus\{u,v\}\), with \(|A^\circ|=a-2\). For a coalition with \(s=|S\cap\{u,v\}|\), \(t=|S\cap A^\circ|\), \(j=|S\cap B|\), and \(i=s+t\), the exact coalition value is
\[
v(S)=\min(i,j)+\mathbf1_{\{s=2,\ i\ge j+2\}}.
\]
Indeed any maximum matching either uses only crossing edges, or uses \(uv\) and crossing edges on the remaining vertices. The grand value is \(W=\min(a,b)+\mathbf1_{\{a\ge b+2\}}\).

## Proof
**Core reduction.** For a matching game with nonnegative payoffs, the inequalities \(x_p+x_q\ge1\) for every graph edge \(pq\), together with \(\sum x_i=W\), are equivalent to the core inequalities for all coalitions. The forward implication sums vertex-disjoint edge inequalities over any matching; the reverse implication takes two-vertex coalitions.

Let \(z=\min_{j\in B}x_j\). Every \(A\)-vertex has payoff at least \(1-z\), and \(x_u+x_v\ge1\). These constraints yield the following exhaustive core descriptions.

**Regime \(a<b\).** If \(z\le1\), efficiency and the cross-edge bounds give
\[
a=W\ge a(1-z)+bz=a+(b-a)z,
\]
so \(z=0\), all \(A\)-payoffs are one and all \(B\)-payoffs vanish. The case \(z>1\) is impossible by efficiency. The core is a singleton and hence is the nucleon.

**Regime \(a=b\).** Equality in the preceding bound forces every vertex in \(A\) to receive \(t\) and every vertex in \(B\) to receive \(1-t\), with \(1/2\le t\le1\); the added-edge inequality supplies the lower endpoint. Thus the core is a line segment. The coalition consisting of all \(A\) and \(a-2\) vertices of \(B\) has value \(a-1\) and ratio \(1+(2t-1)/(a-1)\). The coalition consisting of all \(B\) and \(a-1\) vertices of \(A\) has value \(a-1\) and ratio \(1+(1-t)/(a-1)\). Consequently the least nonconstant ratio cannot exceed
\[
1+\frac{\min(2t-1,1-t)}{a-1}\le1+\frac1{3(a-1)},
\]
with equality only at \(t=2/3\). At this candidate every payoff and hence every coalition surplus is an integer multiple of \(1/3\). Every proper coalition has value at most \(a-1\), so every strictly positive surplus has ratio at least \(1+1/[3(a-1)]\). All zero-surplus coalitions are fixed throughout the core, because their nonnegative affine surpluses vanish at this relative-interior point. Thus the next stage after the permanently tight core coalitions attains its sharp upper bound uniquely at \(t=2/3\), proving the stated nucleon.

**Regime \(a=b+1\).** The grand value is \(W=b\). Assign positive fractional edge weights: \(1/2\) to \(uv\), \(1/(2b)\) to each of the \(2b\) marked-to-\(B\) edges, and \(1/b\) to each of the \(b(b-1)\) ordinary-to-\(B\) edges. Every vertex has total incident weight exactly one; the weights sum to \((2b+1)/2\). Every edge coalition is proper, so if all proper-coalition ratios are at least \(\alpha\), then every edge pair receives at least \(\alpha\). Multiplying these inequalities by the fractional edge weights gives \(b=\sum_i x_i\ge\alpha(2b+1)/2\), hence \(\alpha\le2b/(2b+1)\). The uniform imputation \(x_i=b/(2b+1)\) attains this bound: any coalition matching of size \(k\) covers \(2k\) distinct vertices, yielding \(x(S)\ge2kb/(2b+1)\). At equality all positively weighted edge inequalities must be tight. The complete crossing edges imply all \(A\)-payoffs coincide and all \(B\)-payoffs coincide; the marked edge then forces both sides to equal \(b/(2b+1)\). Thus the first stage is uniquely optimized, and the core is empty because its optimal ratio is below one.

**Regime \(a=b+2\).** Now \(W=b+1\). For \(z<1/2\), the crossing-edge bounds imply \(\sum x_i\ge(b+2)(1-z)+bz>b+1\); for \(z>1\), the \(b\) vertices of \(B\) and the marked-edge constraint give \(\sum x_i\ge bz+1>b+1\). Thus \(1/2\le z\le1\). In this interval the \(b\) ordinary vertices have payoff at least \(1-z\), the marked pair totals at least one, and the \(B\)-vertices total at least \(bz\). These lower bounds sum to \(b+1\), forcing equality throughout. The core is therefore parametrized by
\[
x_B=1-y,\qquad x_{A^\circ}=y,\qquad x_u=e,\qquad x_v=1-e,
\quad 0\le y\le1/2,\quad y\le e\le1-y.
\]
Three proper coalitions (all \(A\) and \(b-1\) of \(B\); all \(B\) and \(b-1\) ordinary \(A\) plus respectively \(u\) or \(v\)) each have matching value \(b\) and ratios
\[
1+\frac{y}{b},\qquad1+\frac{e-y}{b},\qquad1+\frac{1-e-y}{b}.
\]
Their minimum is at most \(1+1/(4b)\), with equality only when \(y=1/4\), \(e=1/2\). At this relative-interior point all payoffs are multiples of \(1/4\); any proper coalition has matching value at most \(b\) (a matching of size \(b+1\) requires all vertices). Accordingly every strictly positive coalition surplus has ratio at least \(1+1/(4b)\). Any tight coalition is fixed throughout the core by the same interior affine-slack argument. The stated allocation uniquely optimizes the first nonfixed lexicographic stage.

**Regime \(a\ge b+3\).** With \(W=b+1\), \(z<1/2\) would force \(\sum x_i\ge a(1-z)+bz>b+1\), and \(z>1\) again violates the marked-edge constraint. For \(z\in[1/2,1]\), summing the \(b\) lower bounds for \(B\), the \(a-2\) crossing bounds for ordinary \(A\), and the marked-pair bound gives
\[
b+1=W\ge bz+(a-2)(1-z)+1=b+1+(a-b-2)(1-z).
\]
Since \(a-b-2>0\), equality forces \(z=1\); then all \(B\) receive one, ordinary \(A\) receive zero, and \(x_u=e\), \(x_v=1-e\) with \(0\le e\le1\). A proper coalition whose payoff depends on \(e\) has exactly one marked endpoint, say \(u\), and its value is at most its number of \(B\)-vertices, at most \(b\). Its ratio is therefore at least \(1+e/b\); the analogous bound for \(v\) is \(1+(1-e)/b\). Both bounds are attained by a coalition containing all \(b\) vertices of \(B\), that chosen marked endpoint, and \(b-1\) ordinary \(A\)-vertices. All other coalitions have payoff constant on the core. Hence the first nonfixed lexicographic ratio is maximized uniquely by \(e=1/2\), giving the final regime.

In each nonempty-core regime some proper edge coalition receives exactly its worth, so the first minimum ratio is one; uniqueness after the first nonfixed stage, or immediately, establishes uniqueness of the full lexicographic maximizer. This completes the proof.

## Verification
An independent exact-rational script `verify.py` evaluates the proposed payoffs, grand efficiency, and every positive-valued proper-coalition ratio in 50 parameter pairs with \(2\le a\le8\), \(1\le b\le8\), and \(a+b\le13\). It checks 74,142 ratios in exact arithmetic. On all checked graphs with at most 10 vertices it reconstructs every coalition's matching number by a separate recursive matching algorithm, independently of the stated closed formula. It also verifies the first ratio and the first nonfixed ratio predicted by the proof. These finite checks corroborate, but do not replace, the all-parameter argument above. Run `python3 verify.py` with Python 3.9 or later; no third-party packages are required.

## Relationship to prior work
Faigle, Fekete, Hochstättler and Kern introduced the multiplicative nucleon and a general polynomial-time algorithm for matching games. Aziz and Csáji (arXiv:2610.29731v1, 21 October 2026) give a combinatorial polynomial-time algorithm for ordinary matching games and state the precise lexicographic definition used here. Their generic algorithms apply to every graph in this family, but the inspected 2026 full text does not state this five-regime explicit formula or its sharp core boundary. The present calculation gives an all-parameter closed form in a structurally natural first non-bipartite perturbation of a complete two-sided market; it is not a new general matching-game algorithm and does not claim algorithmic complexity improvements.

## Limitations
The theorem assumes precisely one extra intra-\(A\) edge, complete unit-weight crossing edges, and one vertex per cooperative player. No weighted, sparse, or multiple-extra-edge extension is proved. Generic existing nucleon algorithms imply computability for each fixed instance; discovery of an equivalent previously published closed form would supersede the claimed explicit classification. The 1995 preprint abstract was accessible, but its full text was not inspected; publication priority against all unindexed treatments is therefore not certified.

## References
1. H. Aziz and G. Csáji, *Computing the Nucleon of Matching Games*, arXiv:2610.29731v1, first posted 2026-10-21, https://arxiv.org/html/2610.29731v1 .
2. U. Faigle, S. P. Fekete, W. Hochstättler and W. Kern, *The Nucleon of Cooperative Games and an Algorithm for Matching Games*, ECCC TR95-007, 1995; *Mathematical Programming* **83** (1998), 195–211, https://eccc.weizmann.ac.il/eccc-reports/1995/TR95-007/index.html .
