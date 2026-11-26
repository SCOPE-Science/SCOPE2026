# Exact shattering polynomial for maximal independent sets of cycles

## Finding
For an integer \(n\ge3\), let \(C_n\) be the simple cycle with labeled vertices \(\mathbb Z/n\mathbb Z\). Let \(\mathcal M_n\) be the family of all inclusion-maximal independent vertex subsets of \(C_n\). For a vertex support \(S\), call \(S\) *shattered* when every subset of \(S\) equals \(I\cap S\) for some \(I\in\mathcal M_n\). Define \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}=\sum_{k\ge0}s_{n,k}z^k\).

**Structural criterion used in the count.** Let \(S\ne\varnothing\) have \(k\) vertices in cyclic order and let \(g_1,\ldots,g_k\) be the positive clockwise distances between consecutive vertices (with \(\sum_i g_i=n\); for a singleton the gap is \(n\)). Then \(S\) is shattered if and only if both conditions hold:

1. Each \(g_i\ge2\).
2. If there are at least two occurrences of a gap \(2\), then between every two consecutive distinct occurrences, read cyclically, there is at least one gap \(\ge4\). In particular, when there is no gap \(\ge4\), at most one gap \(2\) is allowed.

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

The expression counts labeled supports and vanishes for \(k>\lfloor(n+1)/3\rfloor\). As known from [1,2],

\[
\boxed{\operatorname{VCdim}(\mathcal M_n)=\left\lfloor\frac{n+1}{3}\right\rfloor.}
\]

For \(k\ge2\), the known obstruction and extremal construction of [1,2] already imply that at the tight circumference \(n=3k-1\) the top coefficient is
\[
\boxed{s_{3k-1,k}=3k-1.}
\]
The top supports are precisely the \(3k-1\) distinct rotations of the cyclic gap sequence with one \(2\) and \(k-1\) copies of \(3\). Example: \(\Phi_{10}(z)=1+10z+35z^2+40z^3\).

## Assumptions and scope
All graphs are labeled, finite, simple cycles of length \(n\ge3\). Independence means no pair of adjacent selected vertices, and maximality is by inclusion rather than cardinality. Queries are membership at individual vertices; they are neither edge queries nor graph-neighborhood queries. A zero label means the queried vertex is excluded from the chosen maximal independent set. Cyclic gaps are measured in edges in a fixed orientation. The formula counts labeled supports, not isomorphism classes under rotations or reflections. No claim about Littlestone dimension is made.

## Proof
**1. Maximal independent sets as local constraints.** A subset \(I\) is maximal independent exactly when its cyclic membership word has no consecutive \(1\)'s and no three consecutive \(0\)'s. Indeed, the first condition is independence and the second means each omitted vertex has a selected neighbor. For every fixed partial assignment on \(S\), existence of an extending maximal independent set is equivalent to the existence of an independent *witness set* \(W\) that contains each positive queried vertex and, for each negative queried vertex \(v\), contains at least one of its two neighbors but not \(v\). Any independent \(W\) can be enlarged greedily to a maximal independent set \(I\); the excluded queried vertices cannot enter \(I\) because they are already dominated by \(W\).

**2. Necessity of the forbidden gaps (the obstruction from [1,2]).** If \(S\) has a gap \(1\), the all-positive labeling contradicts independence. Suppose two distinct cyclically consecutive occurrences of gaps \(2\) have only gaps \(3\) between them. Label the queried vertices at the endpoints of this entire run positive and all queried vertices strictly inside it negative. Begin with the first positive vertex. Its next vertex is necessarily unselected; at the following negative queried vertex two steps away, the only neighbor available to dominate it is the next vertex, so that vertex is forced positive. Each intervening gap \(3\) propagates this forced selection to the vertex immediately after the next negative query. At the final gap \(2\), the forced selected vertex is adjacent to the prescribed positive endpoint, a contradiction. If the run exhausts the whole cyclic list, its endpoints are the same vertex, labeled positive, and every other query is labeled negative. The same argument works because the final forced selected vertex is a neighbor of the starting vertex.

**3. Sufficiency using local neighbor choices.** Assume the gap conditions hold, and prescribe arbitrary positive/negative labels on \(S\). Put every positive queried vertex into \(W\). For each negative queried vertex choose either its clockwise neighbor (orientation \(R\)) or its counterclockwise neighbor (orientation \(L\)) and put it in \(W\). Gaps \(\ge4\) yield no conflict between any chosen witnesses on their two sides. At gap \(3\), the sole potentially conflicting choice is \(R\) at the preceding negative query followed by \(L\) at the following negative query; a uniform orientation across a run of gaps \(3\) avoids it. At gap \(2\), a positive followed by a negative requires \(R\) for that negative, while a negative followed by a positive requires \(L\) for that negative. Two negatives at gap \(2\) create no conflict for either uniform orientation (the two witnesses may coincide). Two positives at gap \(2\) are nonadjacent.

If a gap \(\ge4\) is present, divide the cyclic list into blocks separated by these long gaps. By hypothesis, each block has at most one gap \(2\). Within each block choose one uniform orientation for all negative vertices: use \(R\) if its gap \(2\) has positive-then-negative labels, \(L\) if it has negative-then-positive labels, and either orientation otherwise. If there are no long gaps, there is at most one short gap, and the same single uniform orientation works around the circle. For any two distinct queried vertices, their witnesses move each endpoint by at most one in cyclic distance. An arc containing at least two successive gaps has length at least four, so on that side the witnesses cannot become adjacent. For arcs consisting of a single gap, the local checks apply; when there are just two queried vertices, both arcs are checked. For a singleton there is only one witness and no possible pairwise conflict. No witness of a negative vertex is another queried vertex, since queries were nonadjacent. Therefore \(W\) is independent, every negative query is dominated, and step 1 extends \(W\) to a maximal independent set satisfying the arbitrary labeling. Hence \(S\) is shattered.

**4. Counting cyclic gap words.** Fix \(k\ge1\) and let \(p\) be the number of gaps at least \(4\), \(q\) the number of gaps \(2\), and \(r=k-p-q\) the number of gaps \(3\). If \(p=0\), admissibility allows either all gaps \(3\), giving exactly \(3\) supports when \(n=3k\), or exactly one gap \(2\), giving exactly \(n\) supports when \(n=3k-1\).

For \(p\ge1\), each interval of gap positions between two consecutive long gaps contains any number of \(3\)'s and at most one \(2\) (for \(p=1\) it is the single interval after that long gap, wrapping back to it). The two-variable generating series for one interval is
\[
F(u,v)=\frac{1}{1-u}+\frac{v}{(1-u)^2}.
\]
Consequently the number of type sequences rooted at one specified long gap is
\[
[u^r v^q]F(u,v)^p=\binom pq\binom{k-1}{r},
\]
where \(q\le p\). Writing each long gap as \(4+e_j\), the excesses are nonnegative and sum to \(E=n-3k-p+q\), giving \(\binom{E+p-1}{p-1}\) choices. Count pairs of an indexed gap sequence and a marked index occupied by a long gap: each indexed sequence has \(p\) marks, and choosing the mark's position among \(k\) indices followed by the sequence starting there is a bijection with the rooted count times \(k\), with no assumption of aperiodicity. Each labeled support of size \(k\) is represented exactly \(k\) times by a starting selected vertex, whereas that vertex has \(n\) possible labels. Multiplying by \(n/k\) gives the announced coefficient formula.

**5. Dimension and tight-length faces.** If \(p\ge1\), admissibility gives \(q\le p\), so \(n\ge3k+p-q\ge3k\). If \(p=0\), admissibility allows at most one gap \(2\), so \(n\ge3k-1\). Hence \(k\le\lfloor(n+1)/3\rfloor\). Conversely, with \(k=\lfloor(n+1)/3\rfloor\), choose \(k-1\) gaps of size \(3\) and one gap of size \(n-3(k-1)\), which is at least \(2\). This is an admissible support of size \(k\). When \(n=3k-1\), the inequalities force \(p=0,q=1\), and there are precisely \(n\) corresponding labeled supports.

## Verification
The standalone program `verify_cycle_mis.py` enumerates every maximal independent set on cycles of lengths \(3\) through \(18\), checks every one of the \(524280\) supports by direct trace cardinality against the forbidden-gap rule, and compares all coefficients with the binomial sum. It also tests the finite-parameter boundary identities through length \(90\). Running `python verify_cycle_mis.py` produces `MAXIMAL_CYCLE_SHATTERING_PASS`. All finite checks are corroboration; the unrestricted theorem is proved in steps 1–5.

## Relationship to prior work
[1] and [2] prove the same all-order Boolean trace (VC) dimension for this precise cycle family. Both use the obstruction in Step 2, and [1] uses a uniform helper-neighbor construction for supports with at most one short gap. At \(n=3k-1\) their obstruction forces the one-short-gap type and the extremal construction realizes it, so the tight coefficient follows without the all-degree formula. The counting contribution here is the exact coefficient for every size, using separate helper orientations across gaps of length at least four to handle arbitrary admissible supports, followed by the marked-gap count. Upper bounds and optimal-width examples from [1,2] alone do not enumerate supports with multiple short gaps separated by long ones. Bisdorff and Marichal [3] give the cyclic no-\(11\), no-\(000\) description and enumerate the maximal independent sets themselves, not shattered supports. Exact results for paths do not automatically extend across the closing edge.

## Limitations
Novelty assessment is based on accessible primary literature and semantic database comparisons, and not on a proof of historical priority. Equivalent results might exist under the terminology of independent dominating-set traces or cyclic binary constraint systems. The theorem makes no statement about other graphs, minimal-cardinality independent dominating sets, adaptive learning, or unlabeled-support orbits. The listed formula assumes a simple cycle of length at least three.

## References
1. *Minimal one-pass implications and exact Boolean trace rank for cycle maximal-independent-set contexts*, recorded October 26, 2026, [full statement and proof](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-minimal-one-pass-implications-and-exact-boolean-trace-rank-for-c--5aa3700acbcd/RESULT.md), “Boolean trace upper bound” and “Boolean trace lower bound”.
2. *Maximal independent sets of cycles: exact VC dimension and the first adaptive gap*, recorded November 2, 2026, [full statement and proof](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-maximal-independent-sets-of-cycles-exact-vc-dimension-and-the-fi--11ee458f4c85/RESULT.md), Steps 1–2.
3. R. Bisdorff and J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, arXiv:math/0701647, Journal of Integer Sequences 11 (2008), Article 08.5.7, https://arxiv.org/html/math/0701647v2.
