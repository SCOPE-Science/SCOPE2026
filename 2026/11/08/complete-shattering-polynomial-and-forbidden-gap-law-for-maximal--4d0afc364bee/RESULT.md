# Complete shattering polynomial and forbidden-gap law for maximal independent sets of cycles

## Finding
For an integer \(n\ge3\), let \(C_n\) be the simple cycle with labeled vertices \(\mathbb Z/n\mathbb Z\). Let \(\mathcal M_n\) be the family of all inclusion-maximal independent vertex subsets of \(C_n\). For a vertex support \(S\), call \(S\) *shattered* when every subset of \(S\) equals \(I\cap S\) for some \(I\in\mathcal M_n\). Define \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}=\sum_{k\ge0}s_{n,k}z^k\).

**Forbidden-gap characterization.** Let \(S\ne\varnothing\) have \(k\) vertices in cyclic order and let \(g_1,\ldots,g_k\) be the positive clockwise distances between consecutive vertices (with \(\sum_i g_i=n\)). Then \(S\) is shattered if and only if both conditions hold:

1. Each \(g_i\ge2\).
2. Between every two consecutive occurrences of a gap \(2\), read cyclically, at least one gap is \(\ge4\). In particular, when there is no gap \(\ge4\), at most one gap \(2\) is allowed.

Equivalently, apart from forbidden adjacent queried vertices, the minimal local forbidden gap runs are \(2,3,\ldots,3,2\), interpreted cyclically. The empty support is shattered.

**Entire coefficient formula.** Set \(s_{n,0}=1\). For \(k\ge1\), use the convention that an indicator contributes zero unless its subscript equality holds, and restrict the inner sum to \(E=n-3k-p+q\ge0\):

\[
\boxed{\displaystyle
s_{n,k}=3\,\mathbf 1_{\{n=3k\}}
+n\,\mathbf 1_{\{n=3k-1\}}
+\sum_{p=1}^{k}\ \sum_{\substack{0\le q\le\min(p,k-p)\\n-3k-p+q\ge0}}
\frac{n}{p}\binom pq\binom{k-1}{k-p-q}
\binom{n-3k+q-1}{p-1}.}
\]

Every term is an integer after summation, and the expression is zero for \(k>\lfloor(n+1)/3\rfloor\). In particular,

\[
\boxed{\operatorname{VCdim}(\mathcal M_n)=\left\lfloor\frac{n+1}{3}\right\rfloor.}
\]

For \(k\ge2\), at the tight circumference \(n=3k-1\) the **exact** top coefficient is
\[
\boxed{s_{3k-1,k}=3k-1.}
\]
The top supports are precisely the \(3k-1\) distinct rotations of the cyclic gap sequence with one \(2\) and \(k-1\) copies of \(3\). Example: \(\Phi_{10}(z)=1+10z+35z^2+40z^3\).

## Assumptions and scope
All graphs are labeled, finite, simple cycles of length \(n\ge3\). Independence means no pair of adjacent selected vertices, and maximality is by inclusion rather than cardinality. Queries are membership at individual vertices; they are neither edge queries nor graph-neighborhood queries. A zero label means the queried vertex is excluded from the chosen maximal independent set. Cyclic gaps are measured in edges in a fixed orientation. The formula counts labeled supports, not isomorphism classes under rotations or reflections. No claim about Littlestone dimension is made.

## Proof
**1. Maximal independent sets as local constraints.** A subset \(I\) is maximal independent exactly when its cyclic membership word has no consecutive \(1\)'s and no three consecutive \(0\)'s. Indeed, the first condition is independence and the second means each omitted vertex has a selected neighbor. For every fixed partial assignment on \(S\), existence of an extending maximal independent set is equivalent to the existence of an independent *witness set* \(W\) that contains each positive queried vertex and, for each negative queried vertex \(v\), contains at least one of its two neighbors but not \(v\). Any independent \(W\) can be enlarged greedily to a maximal independent set \(I\); the excluded queried vertices cannot enter \(I\) because they are already dominated by \(W\).

**2. Necessity of the forbidden gaps.** If \(S\) has a gap \(1\), the all-positive labeling contradicts independence. Suppose two cyclically consecutive gaps \(2\), as occurrences among gaps of length \(2\), have only gaps \(3\) between them. Label the queried vertices at the endpoints of this entire run positive and all queried vertices strictly inside it negative. Begin with the first positive vertex. Its next vertex is necessarily unselected; at the following negative queried vertex two steps away, the only neighbor available to dominate it is the next vertex, so that vertex is forced positive. Each intervening gap \(3\) propagates this forced selection to the vertex immediately after the next negative query. At the final gap \(2\), the forced selected vertex is adjacent to the prescribed positive endpoint, a contradiction. If the two gaps \(2\) exhaust the whole cyclic list, use one endpoint positive and the others negative; the propagation returns to a neighbor of the starting positive vertex and gives the same contradiction. Thus neither forbidden configuration can be shattered.

**3. Sufficiency using local neighbor choices.** Assume the gap conditions hold, and prescribe arbitrary positive/negative labels on \(S\). Put every positive queried vertex into \(W\). For each negative queried vertex choose either its clockwise neighbor (orientation \(R\)) or its counterclockwise neighbor (orientation \(L\)) and put it in \(W\). Gaps \(\ge4\) yield no conflict between any chosen witnesses on their two sides. At gap \(3\), the sole potentially conflicting choice is \(R\) at the preceding negative query followed by \(L\) at the following negative query; a uniform orientation across a run of gaps \(3\) avoids it. At gap \(2\), a positive followed by a negative requires \(R\) for that negative, while a negative followed by a positive requires \(L\) for that negative. Two negatives at gap \(2\) create no conflict for either uniform orientation (the two witnesses may coincide). Two positives at gap \(2\) are nonadjacent.

If a gap \(\ge4\) is present, divide the cyclic list into blocks separated by these long gaps. By hypothesis, each block has at most one gap \(2\). Within each block choose one uniform orientation for all negative vertices: use \(R\) if its gap \(2\) has positive-then-negative labels, \(L\) if it has negative-then-positive labels, and either orientation otherwise. If there are no long gaps, there is at most one short gap, and the same single uniform orientation works around the circle. Chosen witnesses from nonconsecutive queried vertices cannot be adjacent, because those vertices are separated by at least two gaps, each at least \(2\). Therefore \(W\) is independent, every negative query is dominated, and step 1 extends \(W\) to a maximal independent set satisfying the arbitrary labeling. Hence \(S\) is shattered.

**4. Counting cyclic gap words.** Fix \(k\ge1\) and let \(p\) be the number of gaps at least \(4\), \(q\) the number of gaps \(2\), and \(r=k-p-q\) the number of gaps \(3\). If \(p=0\), admissibility allows either all gaps \(3\), giving exactly \(3\) supports when \(n=3k\), or exactly one gap \(2\), giving exactly \(n\) supports when \(n=3k-1\).

For \(p\ge1\), each interval of gap positions between two consecutive long gaps contains any number of \(3\)'s and at most one \(2\). The two-variable generating series for one interval is
\[
F(u,v)=\frac{1}{1-u}+\frac{v}{(1-u)^2}.
\]
Consequently the number of type sequences rooted at one specified long gap is
\[
[u^r v^q]F(u,v)^p=\binom pq\binom{k-1}{r},
\]
where \(q\le p\). Writing each long gap as \(4+e_j\), the excesses are nonnegative and sum to \(E=n-3k-p+q\), giving \(\binom{E+p-1}{p-1}\) choices. For each unrooted index sequence, there are \(k\) possible indexed gap positions and \(p\) distinguished long-gap positions. Thus the number of ordered gap sequences is \(k/p\) times the rooted number. Each labeled support of size \(k\) is represented exactly \(k\) times by a starting selected vertex, whereas that vertex has \(n\) possible labels. Multiplying by \(n/k\) gives the announced coefficient formula.

**5. Dimension and tight-length faces.** If \(p\ge1\), admissibility gives \(q\le p\), so \(n\ge3k+p-q\ge3k\). If \(p=0\), admissibility allows at most one gap \(2\), so \(n\ge3k-1\). Hence \(k\le\lfloor(n+1)/3\rfloor\). Conversely, with \(k=\lfloor(n+1)/3\rfloor\), choose \(k-1\) gaps of size \(3\) and one gap of size \(n-3(k-1)\), which is at least \(2\). This is an admissible support of size \(k\). When \(n=3k-1\), the inequalities force \(p=0,q=1\), and there are precisely \(n\) corresponding labeled supports.

## Verification
The standalone program `verify_cycle_mis.py` enumerates every maximal independent set on cycles of lengths \(3\) through \(18\), checks every one of the \(524280\) supports by direct trace cardinality against the forbidden-gap rule, and compares all coefficients with the binomial sum. It also tests the finite-parameter boundary identities through length \(90\). Running `python verify_cycle_mis.py` produces `MAXIMAL_CYCLE_SHATTERING_PASS`. All finite checks are corroboration; the unrestricted theorem is proved in steps 1–5.

## Relationship to prior work
Guingona, Kolesnikov, Nierwinski and Soucy (first circulated September 10, 2021) develop VC and Littlestone dimensions of zero-set families, not maximal independent sets of cycles. Bisdorff and Marichal (first circulated January 23, 2007) establish the cyclic no-\(11\), no-\(000\) description and enumerate maximal independent sets up to dihedral action; their explicit orbit counts are not shattering counts. Goh, Koh, Sagan and Vatter study extremal totals of maximal independent sets in graphs with bounded cycle number; those results do not imply the incidence-trace classification here. Exact results for maximal independent sets of paths do not automatically transfer to cycles: joining the endpoints changes maximality and allowable traces. The present forbidden-gap law and all-coefficient shattering enumeration concern a different invariant from the Perrin sequence of concept counts.

## Limitations
Novelty assessment is based on accessible primary literature and semantic database comparisons, and not on a proof of historical priority. Equivalent results might exist under the terminology of independent dominating-set traces or cyclic binary constraint systems. The theorem makes no statement about other graphs, minimal-cardinality independent dominating sets, adaptive learning, or unlabeled-support orbits. The listed formula assumes a simple cycle of length at least three.

## References
- V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (first public 2021-09-10), https://arxiv.org/abs/2109.04805.
- R. Bisdorff and J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, arXiv:math/0701647 (first public 2007-01-23); Journal of Integer Sequences 11 (2008), Article 08.5.7, https://arxiv.org/html/math/0701647v2.
- C. Y. Goh, K. M. Koh, B. E. Sagan and V. R. Vatter, *Maximal independent sets in graphs with at most r cycles*, Journal of Graph Theory 53 (2006), 270–282, https://doi.org/10.1002/jgt.20185.
