# Sharp three-coalition transition in bipartite-enemy Nash welfare games

## Finding

For every integer \(q\ge 2\), construct a symmetric aversion-to-enemies additively separable hedonic game on \(n=2q+4\) agents. There are two disjoint two-agent core sets \(C_A,C_B\) and two disjoint \(q\)-agent peripheral sets \(P_A,P_B\). The pairs of enemies are precisely the pairs with one endpoint in \(C_A\) and the other in \(C_B\cup P_B\), together with pairs with one endpoint in \(C_B\) and the other in \(P_A\). All other distinct agent pairs are mutual friends. Friendship has value \(+1\), enmity has value \(-n\), and an agent's utility is the sum of valuations of other members of her coalition.

The enemy graph is connected and bipartite, with equal sides \(C_A\cup P_A\) and \(C_B\cup P_B\). Nash welfare is defined on individually rational partitions (every utility nonnegative) as the geometric mean of all agents’ utilities; a zero utility gives welfare zero. Its optimal \(n\)-th power is exactly
\[
\max_{\pi}\operatorname{NW}(\pi)^n=
\max\big\{(q+1)^{2q+4},\ (2q-1)^{2q}\big\}.
\]
The maximizing partition is unique up to coalition ordering and is:

- For \(2\le q\le8\): the two coalitions \(C_A\cup P_A\) and \(C_B\cup P_B\).
- For \(q\ge9\): the three coalitions \(C_A\), \(C_B\), and \(P_A\cup P_B\).

In particular, a **connected bipartite enemy graph does not force a two-coalition Nash-welfare maximizer**. The first three-coalition optimum in this explicitly defined family occurs at \(q=9\), or \(n=22\) agents; no global minimality claim is made.

## Assumptions and scope

The model is symmetric and complete as a signed valuation system: every pair receives exactly one of \(+1\) and \(-n\). Every agent belongs to exactly one nonempty coalition; there is no imposed bound on the number of coalitions. Each singleton has utility zero. The positive-optimum analysis considers partitions in which all utilities are positive, since the exhibited two-coalition allocation always has positive welfare.

The enemy graph may also be written as \(K_{q+2,q+2}\) with all \(q^2\) peripheral-to-peripheral edges deleted. The result depends on the specific two-core-per-side construction, not merely on enemy-graph bipartiteness.

## Proof

**1. Friendship cliques and a three-coalition normal form.** Any coalition containing an enemy pair has at least one agent of utility no greater than \((n-2)-n=-2\), so such a partition is not individually rational. Hence every admissible optimal coalition must be an enemy-free clique, and a clique of size \(s\ge2\) contributes precisely \((s-1)^s\) to the product.

Every member of \(C_A\) is friendly only to members of \(C_A\cup P_A\), and every member of \(C_B\) is friendly only to \(C_B\cup P_B\). If the two members of either core were in separate coalitions, those two coalitions could be merged, strictly increasing the Nash product, as all pairs across them are friends. Likewise all peripheral members left outside the core-containing coalitions are mutually friendly, and merging their separate coalitions strictly improves the product. Thus an optimum has two core-containing coalitions and at most one residual peripheral coalition.

Write \(a\) and \(b\) for the numbers of peripheral members in the two core-containing coalitions, where \(0\le a,b\le q\), and put \(r=2q-a-b\) for the residual size. The product for \(r\ge2\) is
\[
P_q(a,b)=(a+1)^{a+2}(b+1)^{b+2}(r-1)^r.
\]
If \(r=1\), the singleton gives product zero. If \(r=0\), necessarily \(a=b=q\), giving the unique two-coalition partition and product \(P_2=(q+1)^{2q+4}\).

**2. Convexity reduces all three-coalition possibilities to three numbers.** For \(s\ge2\), set \(f(s)=s\log(s-1)\). Then
\[
f''(s)=\frac{s-2}{(s-1)^2}\ge0.
\]
Consequently \(\log P_q(a,b)=f(a+2)+f(b+2)+f(2q-a-b)\) is convex on the real polygon \(0\le a,b\le q\), \(a+b\le2q-2\). This polygon has vertices \((0,0)\), \((q,0)\), \((0,q)\), \((q,q-2)\), and \((q-2,q)\), with repetitions permitted at \(q=2\). Thus its maximum over integer points is attained at a vertex. The corresponding distinct products are
\[
P_3=(2q-1)^{2q},\qquad
P_M=(q+1)^{q+2}(q-1)^q,\qquad
P_2=(q+1)^{2q+4}.
\]
The third vertex product \(P_M\) obeys \(P_M<P_2\) for all \(q\ge2\). Therefore the unrestricted optimum is exactly \(\max\{P_2,P_3\}\). In each regime its strictly preferred vertex identifies the stated unique partition.

**3. The unique crossover.** Treating \(q\) as a real \(x>2\), define
\[
D(x)=2x\log(2x-1)-(2x+4)\log(x+1).
\]
Its derivative is
\[
\tfrac12D'(x)=\log\frac{2x-1}{x+1}-\frac{x-2}{(2x-1)(x+1)}.
\]
For \(x>2\), use \(\log(1+t)\ge t/(1+t)\) with \(t=(x-2)/(x+1)>0\) to obtain \(D'(x)>0\). The exact integer comparisons \(15^{16}<9^{20}\) and \(17^{18}>10^{22}\) give \(D(8)<0<D(9)\), and monotonicity gives the claimed threshold for all integer \(q\ge2\). At \(q=2\), the same product inequality is immediate.

## Verification

Run `python verify.py` with Python 3 (standard library only). It checks the exact product classification for every integer \(2\le q\le80\), including both sides of the crossover, and separately enumerates all \(4{,}140\) unlabeled set partitions of the eight-agent instance and all \(115{,}975\) partitions of the ten-agent instance. Each brute-force computation reconstructs enemy pairs and coalition products directly, without assuming the three-coalition normal form. The output is `PASS`.

The finite checks are consistency tests, not the proof for unbounded \(q\). The three numbered analytic steps above establish that infinite statement.

## Relationship to prior work

Pagano and Schlenga (2026) define Nash welfare in additively separable hedonic games and show that aversion-to-enemies individually rational coalitions are friendship cliques (Lemma 1). Their Theorem 6.1 provides polynomial-time optimization **when at most two coalitions are permitted**, while Theorem 6.2 establishes hardness for three or more permitted coalitions in general. The exact unrestricted two-versus-three transition in the connected bipartite enemy-graph family defined here is not among their stated or proved classifications. The present result does not contradict either theorem: it compares the unrestricted global optimum with the two-coalition-restricted optimum on a special solvable family.

Earlier exact welfare classifications for complete multipartite friendship graphs concern a different compatibility structure: within-class enemies and cross-class friends, rather than the missing peripheral cross edges and two opposite hostile cores studied here. Their results do not determine these products or the crossover. Search results for equivalence and broader coverage were not conclusive proofs of global priority.

## Limitations

The \(22\)-agent crossover is sharp only **within this parametrized family**, not among all connected bipartite enemy graphs. This result gives Nash-welfare optimal partitions and their values, not coalition stability under all deviations, incentive compatibility, or polynomial-time solvability of arbitrary bipartite enemy-graph instances. The classification does not extend automatically to asymmetric agents, different enemy penalties, weighted friendship links, or different welfare objectives. The finding has received only self-review and no independent scientific audit.

## References

- Marta Pagano and Alexander Schlenga, *Nash Welfare in Additively Separable Hedonic Games*, arXiv:2605.19030v1, publicly posted 18 May 2026. https://arxiv.org/html/2605.19030v1, especially Sections 2, 3, 6.1 and appendix proofs of Section 6.
- Foivos Fioravantes, Harmender Gahlawat, Nikolaos Melissinos, and Šimon Schierreich, *Individual Rationality in Constrained Hedonic Games: Additively Separable and Fractional Preferences*, arXiv:2603.21826 (23 March 2026), https://arxiv.org/abs/2603.21826. Studies IR restrictions rather than unrestricted Nash welfare.
