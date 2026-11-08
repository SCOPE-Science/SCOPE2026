# Facet inflation and two boundary collapses for a shortened four-cycle metric

## Finding

Let \(N\ge 5\), and distinguish four points in cyclic order \(a_0,a_1,a_2,a_3\) among \(N\) points. For \(\tfrac12\le t\le1\), assign distance \(t\) to the four consecutive cyclic pairs \(a_0a_1,a_1a_2,a_2a_3,a_3a_0\), and distance \(1\) to every other distinct pair (including both core diagonals and all pairs meeting an outside point). Let \(F_N(t)\) be the number of facets of the unit ball of the **real** Lipschitz-free space over this metric.

**Theorem.** With \(k=N-4\ge1\), the complete count is

\[
F_N(t)=\begin{cases}
26\cdot 2^k-22,&t=\tfrac12,\\
38\cdot 2^k-22,&\tfrac12<t<1,\\
16\cdot 2^k-2,&t=1.
\end{cases}
\]

Both endpoints have strictly fewer facets than every interior parameter, with respective losses \(12\cdot2^k\) and \(22\cdot2^k-20\). For \(N=5\), the successive counts are \(30,54,30\); for \(N=6\), they are \(82,130,62\). The interior family remains strictly nongeneric even though every triangle inequality is strict. These assertions include all endpoint equalities and make no claim outside the indicated interval.

## Assumptions and scope

All spaces are real and all points are distinct. The displayed function is a metric: for \(\tfrac12\le t\le1\), a core diagonal of length one is at most the sum \(2t\) along its two short sides, and all other triangle inequalities hold. At the lower endpoint exactly these diagonal triangle inequalities become equalities; at the upper endpoint the metric becomes equilateral.

Fix one of the \(k\) outside points as basepoint \(o\). The unit ball of the dual \(\operatorname{Lip}_0(M)\) is the \((N-1)\)-dimensional polytope
\[
P_t=\{f:M\to\mathbb R:f(o)=0,\ |f(x)-f(y)|\le d_t(x,y)\ \forall x,y\}.
\]
Its vertices correspond, by polar duality, to facets of the Lipschitz-free unit ball. Throughout the proof potentials may first be shifted by constants, then uniquely normalized by \(f(o)=0\). The outside points are denoted by \(b_1,\ldots,b_k\).

## Proof

**1. Extremal potentials are exactly those with connected tight graphs.** Join distinct points \(x,y\) in \(G_f\) when \(|f(x)-f(y)|=d_t(x,y)\). The normals of the active inequalities are signed incidence vectors of this graph, whose rank after quotienting constant functions is \(N-c(G_f)\), where \(c(G_f)\) counts connected components. Since \(P_t\) is full-dimensional, \(f\) is a vertex if and only if this rank is \(N-1\), equivalently \(G_f\) is connected. This is the standard tight-edge criterion; it is not claimed as new.

**2. The outside-point dichotomy is exhaustive.** All core pairwise distances are at most one, so their potentials have range at most one. All outside-to-core distances and outside-to-outside distances are exactly one.

If the outside potentials have range exactly one, translate their minimum to zero and their maximum to one. Every core potential is in \([0,1]\), since it must be within one of both extremes. An outside potential strictly between zero and one could not be tight with an outside endpoint or any core point, and hence would be isolated. Therefore all outside values belong to \(\{0,1\}\), with both occurring. The outside tight edges form a connected complete bipartite graph. The full tight graph is connected precisely when **every connected component of the core tight-edge graph** contains a core potential at \(0\) or \(1\), where that core component attaches to the outside graph.

If the outside potentials have range strictly less than one, no two outside points are connected by a tight edge. Each outside point must therefore attach to a core point via an edge of length one. Let the core minimum and maximum be \(m\) and \(M\), with \(M-m\le1\). Such an outside point must equal either \(m+1\) or \(M-1\); the distance between these two possible levels is \(2-(M-m)\ge1\). Since the outside range is strictly less than one, all outside points take the **same** value. Set it equal to zero. Some core point is then at \(1\) or at \(-1\), but both signs cannot occur because the core range is at most one. By sign reversal it suffices to count the configuration in which all core potentials lie in \([0,1]\) and at least one equals \(1\). The graph is connected exactly when each component of the core tight graph contains a core vertex at \(1\). The sign-reversed configurations contribute an equal disjoint count.

**3. A four-symbol core reduction.** In each case, core potentials belong to \([0,1]\) and every core tight component is joined to at least one endpoint \(0\) or \(1\). Tight core edges have length \(t\) on the cycle or length one along a diagonal. Starting from an endpoint, a tight path must stay in \([0,1]\). When \(\tfrac12<t<1\), the only values reachable by successive steps of size \(t\) or one without leaving \([0,1]\) are
\[
\{0,\ 1-t,\ t,\ 1\}.
\]
Indeed a short step from zero reaches \(t\), from one reaches \(1-t\), and their next short steps can only return to an endpoint because \(2t>1\); a diagonal step of length one exchanges the endpoints. At \(t=\tfrac12\), the two interior symbols merge, leaving \(\{0,\tfrac12,1\}\). The reduction is exhaustive for any real parameter in the corresponding open or boundary regime.

**4. Finite core-state count, with exact conditions.** Number the four core points \(0,1,2,3\) cyclically. A four-tuple of symbols from the indicated value set is *feasible* when neighboring cyclic entries differ by at most \(t\); diagonal entries always differ by at most one. Draw a core tight edge on every cyclic pair differing by exactly \(t\), and on every diagonal pair differing by exactly one. For the **two-level outside** case, require every connected core component to contain at least one symbol at \(0\) or \(1\); call the number of feasible tuples \(A_t\). For the **one-level outside** case, require every core component to contain a symbol at \(1\); call the number \(B_t\).

The complete enumeration below groups tuples according to multiplicities of symbols. The entry \(\mathbf v\) is the ordered list of numbers of appearances of the symbols, in the order indicated. The column counts give \(B_t\) and \(A_t\), respectively.

| Parameter | Symbols | \(\mathbf v\) | One-level count | Two-level count |
|---|---|---|---:|---:|
| \(\tfrac12<t<1\) | \(0,1-t,t,1\) | \((0,0,0,4)\) | 1 | 1 |
| | | \((0,1,0,3)\) | 4 | 4 |
| | | \((0,2,0,2)\) | 6 | 6 |
| | | \((1,0,2,1)\) | 4 | 4 |
| | | \((1,1,1,1)\) | 8 | 8 |
| | | \((1,2,0,1)\) | 4 | 4 |
| | | \((2,0,2,0)\) | 0 | 6 |
| | | \((3,0,1,0)\) | 0 | 4 |
| | | \((4,0,0,0)\) | 0 | 1 |
| **Totals** | | | **27** | **38** |
| \(t=\tfrac12\) | \(0,\tfrac12,1\) | \((0,0,4)\) | 1 | 1 |
| | | \((0,1,3)\) | 4 | 4 |
| | | \((0,2,2)\) | 6 | 6 |
| | | \((1,2,1)\) | 4 | 4 |
| | | \((2,2,0)\) | 0 | 6 |
| | | \((3,1,0)\) | 0 | 4 |
| | | \((4,0,0)\) | 0 | 1 |
| **Totals** | | | **15** | **26** |

These counts follow by applying the displayed neighboring-edge rule and the explicit connected-component rule to at most \(4^4=256\) symbol tuples. For example, the 8 admissible four-distinct-symbol tuples in the interior case have their zero and one on opposite core vertices, and each of the two interior symbols on the short-edge neighbor of its relevant anchor. The included `verify_cycle_facets.py` implements the complete rational enumeration with no floating-point comparisons; the table is also checkable directly from the rules.

**5. Assemble the count.** For \(k\ge1\), there are precisely \(2^k-2\) outside binary assignments using both zero and one, giving \(A_t(2^k-2)\) vertices in the two-level case. In the one-level case there are \(B_t\) core choices with core maximum one, and another \(B_t\) choices by sign reversal, giving \(2B_t\) vertices. These cases are disjoint and exhaust the tight-connected potentials. Therefore
\[
\#\operatorname{vert}(P_t)=A_t(2^k-2)+2B_t.
\]
Substitution gives \(38\cdot2^k-22\) in the open interval and \(26\cdot2^k-22\) at the lower endpoint. At \(t=1\), all pair distances are one: the vertices are exactly the nonconstant binary potentials, of which there are \(2^N-2=16\cdot2^k-2\). Polar duality now proves the facet formula.

## Verification

The standalone standard-library script `verify_cycle_facets.py` reproduces the exact rational core-state table at \(t=\tfrac12,\tfrac34,\tfrac78\). As a separate check, it enumerates **every labeled spanning tree** and all sign assignments to its tight-edge equations, solves them over rational numbers, tests every metric inequality, and deduplicates resulting dual vertices for \(N=5,6\) at those three parameters and at \(t=1\). Thus the independent small-case enumerations cover all possible vertices; no numerical optimizer or random sample is used. The actual execution completed with `ALL_SHORT_CYCLE_FACET_CHECKS_PASSED`. These finite checks test, but do not replace, the proof for every \(N\) and real \(t\) in the theorem's domain.

## Relationship to prior work

Vershik introduced the finite-metric polytope classification problem. Gordon and Petrov proved general tight-graph criteria and face-number formulas for generic metrics (arXiv:1608.06848, first public 2016-08-24). The present metrics are **not generic**: the core assignment \((0,t,0,t)\) makes all four short edges simultaneously tight, producing a tight cycle; an outside point at one attaches through a tight unit edge and makes the tight graph connected. Hence generic simplicial counts do not determine this result. The four-core metric also fails the tree four-point condition, because the two diagonal-pair distances sum to two, while both opposite-side pair sums equal \(2t<2\); general tree-metric face-vector formulas therefore do not apply.

A separate result on independently shortened pairs allows **disjoint** short edges, whereas the four short edges here overlap and form a cycle. Another result on interpolated complete-multipartite metrics concerns lengths **greater than one** within parts and its modified-edge graph is a union of disjoint cliques; the short-edge graph here is a cycle, so neither hypothesis holds. More broadly, exact low-cardinality classifications or generic-metric algorithms do not imply the closed all-dimensional three-regime formula without additional enumeration. The equilateral endpoint count is classical and excluded from the novelty claim. Full-text comparison was possible for Gordon–Petrov and the two cited structured-family results; completeness of bibliographic coverage is not asserted.

## Limitations

Only four consecutive core distances are shortened; all core diagonals, and all distances involving outside points, are one. The classification concerns \(N\ge5\) and \(\tfrac12\le t\le1\); it does not determine all higher-codimension faces, asymmetric four-cycle weights, or metrics below the triangle-inequality boundary. The formula is not a statement about generic metrics or ordinary unweighted graph shortest-path metrics. The symbolic-state computation is exhaustive only because of the proved core-value reduction, not by extrapolation from finite experiments. No independent external validation has been performed.

## References

1. A. M. Vershik, *Classification of finite metric spaces and combinatorics of convex polytopes*, arXiv:1504.03601, first public 2015-04-14. https://arxiv.org/abs/1504.03601
2. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848, first public 2016-08-24; Arnold Mathematical Journal 3 (2017), 205–218. https://arxiv.org/abs/1608.06848 ; https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/17-63/index.html
3. *Facet enumeration for equilateral metrics with independently shortened pairs*, public research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-facet-enumeration-for-equilateral-metrics-with-independently-sho--3bd6d7048744
4. *Sharp facet jumps for interpolated complete-multipartite Lipschitz-free balls*, public research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-facet-jumps-for-interpolated-complete-multipartite-lipschi--5c07b142df09
5. E. Delucchi and L. Hoessly, *Fundamental polytopes of metric trees via parallel connections of matroids*, arXiv:1612.05534, first public 2016-12-16 (tree-metric scope only). https://arxiv.org/abs/1612.05534
