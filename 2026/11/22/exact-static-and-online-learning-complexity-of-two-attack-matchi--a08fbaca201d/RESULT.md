# Exact static and online learning complexity of two-attack matching frameworks

## Finding

Fix a labeled set \(V\) of \(n\) arguments. Consider every symmetric, irreflexive attack relation whose underlying undirected graph is a matching of size at most two. For each such framework \(M\), its stable-extension membership classifier is \(h_M(S)=1\) exactly when \(S\subseteq V\) is a Dung stable extension. Let \(P_n(z)=\sum_{j\ge0} s_j(n)z^j\), where \(s_j(n)\) is the number of \(j\)-element sets of distinct subset queries shattered by \(\{h_M\}\).

For every \(n\ge5\), with \(N=\binom n2\), the complete polynomial is

\[
P_n(z)=1+(1+n+N)z+\left(N+\binom N2\right)z^2+12\binom n4 z^3.
\]

Moreover, both its VC dimension and its Littlestone dimension equal \(3\). The cutoff is sharp: for \(n=1,2,3,4\), the respective complete coefficient lists are \((1)\), \((1,3)\), \((1,4,3)\), and \((1,11,18)\), and their VC and Littlestone dimensions are respectively \(0,1,2,2\). No query support of size four can be shattered at any \(n\).

For \(n\ge5\), every shattered triple consists of three queries omitting the pairs of vertices represented by the three edges of a simple four-vertex path. Every pair of distinct two-omission queries is shattered; every pair of distinct one-omission queries is also shattered. Queries of differing omission sizes cannot jointly be shattered.

## Assumptions and scope

An attack is a directed edge, and every selected undirected matching edge corresponds to two opposite attacks. There are no self-attacks, no attacks among unmatched vertices, and at most two undirected edges in total; the empty matching is permitted. The set of observations is the entire Boolean domain \(2^V\), with queries at distinct subsets. A stable extension is conflict-free and attacks every vertex outside it. The VC dimension refers to the class of classifiers **as the attack relation varies**, not to the class of stable extensions of a single fixed graph. Littlestone dimension is the maximum depth of a complete binary adaptive mistake tree whose internal queries are subsets of \(V\), with every root-to-leaf label sequence realized by a classifier.

## Proof

**Step 1: exact positive-query geometry.** Let a matching \(M\) have \(t\in\{0,1,2\}\) edges and let \(B=V\setminus S\). The set \(S\) is stable if and only if it contains every unmatched vertex and exactly one endpoint of each matched edge. Necessity follows because an unmatched vertex cannot be attacked if excluded and an entire edge cannot be included without conflict. For sufficiency, each excluded endpoint is attacked by its paired included endpoint. Thus \(|B|=t\), and \(B\) is a transversal choosing one endpoint of every edge of \(M\). In particular, the positive queries for a zero-edge hypothesis consist solely of \(B=\varnothing\); a one-edge hypothesis is positive at its two singleton endpoints; and a two-edge hypothesis is positive exactly at the four 2-sets forming a chordless four-cycle in the complete graph on its four endpoints.

**Step 2: shattered singletons and pairs.** Any shattered support must admit a jointly positive labeling, so its omitted sets all have the same size \(t\). The unique zero-omission query is shattered when \(n\ge2\). Every singleton-omission query is shattered when \(n\ge2\); any two distinct singleton omissions are shattered when \(n\ge3\): the joining matching edge gives both positive, an edge from either vertex to a third vertex gives exactly one positive, and the empty matching gives neither. There are \(n\) singleton-omission queries. The \(N=\binom n2\) two-omission queries are individually shattered when \(n\ge4\). For \(n\ge5\), every pair of distinct two-omission queries is shattered. If the omitted pairs share a vertex, choose their jointly positive four-cycle and replace an endpoint by a spare vertex to realize each singleton-positive labeling. If the omitted pairs are disjoint, two crossing edges give the both-positive labeling, and replacing one of the four vertices by a fifth produces each singleton-positive labeling. The empty matching gives neither. For \(n=4\), exactly the disjoint pairs of two-omission queries cannot be shattered: the four positive query pairs of a perfect matching come in complementary pairs, so such queries always receive the same label. There are three forbidden pairs at \(n=4\). For \(n\le3\), no two-edge matching exists. Consequently the first two coefficients equal the stated formulas at every order.

**Step 3: shattered triples and the degree bound.** At least three jointly positive two-omission queries must be chosen among the four edges of the same four-cycle; thus their edge set is a simple path on four vertices \(a,b,c,d\). For \(n\ge5\), choose an additional vertex \(e\). For the three queries omitting \(ab,bc,cd\), the following two-edge matchings (written as their disjoint edges) realize the complete Boolean trace:

| Trace | Matching edges |
|---|---|
| 111 | \(ac,bd\) |
| 110 | \(ac,be\) |
| 101 | \(ad,bc\) |
| 011 | \(bd,ce\) |
| 100 | \(ae,bd\) |
| 010 | \(ab,ce\) |
| 001 | \(ac,de\) |
| 000 | empty matching |

This proves sufficiency. For \(n=4\), a matching positive on all three edges of the path is determined uniquely; no alternative four-vertex matching makes exactly two of these queries positive, so the triple is not shattered. Each four-element vertex set has exactly \(4!/2=12\) undirected Hamiltonian paths, whence \(s_3(n)=12\binom n4\) for \(n\ge5\) and zero otherwise. If four queries were shattered, the all-positive hypothesis would necessarily be a two-edge matching with its four transversal pairs (the four-cycle). But any three of these four pairs uniquely determine that matching, forcing the fourth positive whenever the other three are positive. Thus no four-query support is shattered; larger shattered supports are impossible by downward closure. Summing Steps 1–3 gives the complete polynomial.

**Step 4: adaptive dimension.** A shattered triple supplies a complete depth-three mistake tree by asking its three fixed queries, so the Littlestone dimension is at least three for \(n\ge5\). For the upper bound, suppose a complete depth-four tree existed and take its root query \(B\). Its positive branch would have to support a depth-three tree. If \(|B|=0\), there is exactly one positive hypothesis. If \(|B|=1\), the positive hypotheses are the one-edge matchings containing that omitted vertex; after any further positive query the matching is uniquely determined, so the root-positive class has Littlestone dimension at most one. If \(|B|=2\), write \(B=\{a,b\}\). Any second query split within the root-positive class must also omit two vertices. If it is disjoint from \(B\), the joint-positive fiber has at most two matchings, hence Littlestone dimension at most one. If it shares one vertex, say \(\{a,c\}\), the joint-positive fiber consists exactly of \(\{\{b,c\},\{a,x\}\}\) for \(x\notin\{a,b,c\}\). On this fiber, every query is either always true, always false, or true for only a single choice of \(x\). No query splits this fiber into two nontrivial classes each admitting a further split; thus its Littlestone dimension is at most one. If the second query equals \(B\) or has a different omission size, it cannot split the root-positive class. Therefore the root-positive class in all cases has Littlestone dimension at most two, contradicting the required depth three. The all-order upper bound is three. At \(n\le4\), an online depth-three tree is also excluded: if \(n=4\), the positive fiber of any two-omission query has exactly two matchings, and one-omission queries have at most three positive hypotheses with singleton-positive fibers. For \(n=3\), one-omission positive fibers have two matchings; smaller orders are immediate. The shattered pairs and singletons in Step 2 give the matching lower bounds.

## Verification

The standalone `verify.py` enumerates all matchings on \(n=1,\ldots,8\) labeled vertices with at most two edges. It calculates stable-extension membership directly using conflict-freeness and domination rather than the transversal lemma, enumerates every potential support of up to four active queries, and independently computes adaptive mistake-tree depth by memoized Boolean hypothesis-set recursion. The tests confirm, order by order, the coefficient profiles \((1)\), \((1,3)\), \((1,4,3)\), \((1,11,18)\), \((1,16,55,60)\), \((1,22,120,180)\), \((1,29,231,420)\), and \((1,37,406,840)\). The last line is `VERIFY_OK 8`. Only the proof establishes the result for unbounded \(n\); finite tests alone do not.

## Relationship to prior work

Dung's foundational 1995 semantics defines stable extensions. Niskanen, Wallner and Järvisalo (2019) study synthesis of argumentation frameworks from examples and stable-semantic consistency methods. Malmqvist (published online October 21, 2026) studies learning attack relations from extension examples, proving general quadratic VC bounds and sparsity-sensitive bounds for stable semantics. The result here restricts to **symmetric matchings of size at most two** and derives a complete exact VC-shattering polynomial together with the adaptive Littlestone dimension; these are not claimed to follow from the stated general bounds. The 2026 article's publicly available abstract was examined, but its full paper was not accessible for an exhaustive comparison. It remains possible that the new formula is implicit in uninspected parts of that paper or another earlier publication.

## Limitations

The result concerns only one fixed finite universe and two or fewer mutually attacking disjoint pairs; it does not generalize by itself to arbitrary sparse digraphs, asymmetric attacks, or three-edge matchings. The polynomial counts labeled query supports, not argumentation frameworks up to isomorphism. Numerical checks stop at eight arguments. Historical originality has been assessed against accessible literature and relevant mathematical-record search results, not independently certified.

## References

1. P. M. Dung, *On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games*, Artificial Intelligence **77** (1995), 321–357, https://doi.org/10.1016/0004-3702(94)00041-X.
2. A. Niskanen, J. P. Wallner, M. Järvisalo, *Synthesizing Argumentation Frameworks from Examples*, Journal of Artificial Intelligence Research **66** (2019), https://doi.org/10.1613/jair.1.11758.
3. L. Malmqvist, *Learning attack relations in abstract argumentation from extension examples*, Journal of Logic and Computation **36** (2026), first online October 21, 2026, https://doi.org/10.1093/logcom/exag049.
