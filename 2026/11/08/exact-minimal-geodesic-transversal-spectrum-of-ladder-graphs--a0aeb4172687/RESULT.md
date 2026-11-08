# Exact minimal geodesic-transversal spectrum of ladder graphs

## Finding

For every integer \(h\ge2\), write \(L_h=P_h\square K_2\). Vertices have coordinates \((i,c)\), with \(0\le i\le h-1\) and \(c\in\{0,1\}\); consecutive rungs are joined in the same column, and each rung joins its two vertices. A **geodesic transversal** meets every inclusion-maximal shortest path. A transversal is **inclusion-minimal** if deleting any chosen vertex destroys the transversal property.

Let \(M_h(z)\) count inclusion-minimal transversals by cardinality. Then
\[
M_h(z)=\begin{cases}
3hz^2,&h=2,3,\\[2pt]
3hz^2+\dfrac{h(h-4)(h-5)}{3}z^3,&h\ge4.
\end{cases}
\]
All inclusion-minimal transversals are precisely the following disjoint families, with column labels \(c\in\{0,1\}\):

1. \(\{(0,c),(h-1,c)\}\), for either column.
2. \(\{(a,0),(b,1)\}\), for \(0\le a,b\le h-1\) and \(|a-b|\le1\).
3. \(\{(a,c),(b,1-c),(d,c)\}\), for \(0\le a<b<d\le h-1\), \(a+2\le b\le d-2\), and \((a,d)\ne(0,h-1)\).

The minimum transversal cardinality is \(2\); the maximum cardinality among inclusion-minimal transversals is \(2\) for \(2\le h\le5\), and \(3\) for \(h\ge6\). The corresponding simplicial complex of complements of transversals is pure exactly for \(2\le h\le5\).

## Assumptions and scope

All graphs are finite, simple, undirected, unweighted. Here \(P_h\) has \(h\) vertices. A shortest path is maximal if no strictly longer shortest path contains it as a consecutive subpath; this is not the same as being a longest simple path. The claim covers all integers \(h\ge2\), without divisibility or asymptotic assumptions. Families above are labeled: the two columns and individual rung positions are distinguished.

## Proof

**1. Maximal geodesics.** In the Cartesian product \(P_h\square K_2\), a shortest path changes column at most once and changes its rung coordinate monotonically. Any shortest path can be extended in the same rung direction to span the extreme rungs \(0\) and \(h-1\). If it never switches column, a column-switching edge may be appended at one extreme. These extensions preserve shortestness. Thus the maximal geodesics are exactly the \(2h\) paths from \((0,c)\) to \((h-1,1-c)\), each switching at a unique rung \(t\in\{0,\ldots,h-1\}\). They have \(h\) edges and are already diameter paths, so cannot be further extended.

**2. Exact transversal criterion.** For a selected set \(S\), let \(A=\{i:(i,0)\in S\}\) and \(B=\{i:(i,1)\in S\}\). If only one of these is nonempty, every switch position must be hit by the selected column from both travel orientations; this occurs exactly when its extreme indices \(0,h-1\) are both selected. If \(A,B\ne\varnothing\), define \(a=\min A\), \(c=\max A\), \(b=\min B\), \(d=\max B\). A path starting in column \(0\) and switching to column \(1\) at \(t\) avoids \(S\) exactly when \(t<a\) and \(t>d\), possible for an integer \(t\) precisely when \(a>d+1\). Reversing the columns gives an avoiding path exactly when \(b>c+1\). Thus
\[
S\text{ is a transversal}\quad\Longleftrightarrow\quad a\le d+1\ \text{ and }\ b\le c+1
\]
when both columns occur.

**3. Minimality classification.** The criterion uses only the minimum and maximum selected rung of each nonempty column. Therefore an inclusion-minimal transversal has at most two vertices per column, since any intermediate chosen vertex can be deleted. If both columns have two chosen vertices, write their extrema \(a<c\) and \(b<d\). Essentiality of the vertex at \(a\) forces \(c>d+1\); essentiality of the vertex at \(b\) forces \(d>c+1\). These inequalities contradict each other. Hence a minimal set has at most three vertices.

With exactly one selected column, the criterion makes the two boundary vertices necessary and sufficient (family 1). With one selected vertex in each column, the criterion becomes \(|a-b|\le1\), and deletion of either point leaves a singleton which is not a transversal (family 2). With two vertices \(a<d\) in column \(c\) and a singleton at \(b\) in the other column, essentiality of the two same-column vertices is equivalent to \(a+2\le b\le d-2\). These inequalities already imply feasibility. Deleting the singleton is a failure exactly unless the other column's two vertices are precisely the boundary pair; excluding \((a,d)=(0,h-1)\) gives family 3. Conversely every set in these three families satisfies the transversal criterion and fails after every single deletion. Since transversality is upward closed, single-deletion failure is equivalent to inclusion-minimality. This proves completeness.

**4. Enumeration.** Family 1 has \(2\) members. Family 2 has \(h+2(h-1)=3h-2\) members, so exactly \(3h\) minimal transversals have size \(2\). For a fixed doubled column, in family 3 choose \(b=2,\ldots,h-3\). The number of pairs \((a,d)\) is \((b-1)(h-b-2)\), minus exactly one pair \((0,h-1)\). Thus the number of triples per doubled column is
\[
\sum_{b=2}^{h-3}\big((b-1)(h-b-2)-1\big)
=\binom{h-2}{3}-(h-4)
=\frac{h(h-4)(h-5)}6
\]
for \(h\ge4\); for \(h=2,3\) no such triples exist. Multiplying by the two column choices yields the displayed cubic coefficient. It is positive exactly when \(h\ge6\). The claimed extrema and purity criterion follow because faces are complements of transversals and facets correspond to inclusion-minimal transversals. \(\square\)

## Verification

The standalone `ladder_transversal_verify.py` calculates shortest paths using independent breadth-first-search distances and verifies that the \(2h\) stated paths are precisely the maximal geodesics for \(2\le h\le8\). It then checks every one of the \(349520\) vertex subsets for \(2\le h\le9\) directly against the resulting paths, independently enumerates all inclusion-minimal sets, and compares their exact labeled membership and cardinality polynomial against all three families. A separate finite arithmetic check compares the summation with the cubic formula through \(h=99\). The executed result was `VERIFY_OK`, including \(70\) maximal paths checked in the independent shortest-path phase and \(242\) inclusion-minimal sets identified in the full subset phase. Finite calculations support, but do not prove, the unrestricted theorem; the proof above establishes all \(h\ge2\).

To reproduce, run `python ladder_transversal_verify.py` with Python 3 and no external libraries.

## Relationship to prior work

Manuel, Brešar and Klavžar introduced the geodesic-transversal problem and proved its basic complexity and tree/cactus results in their January 20, 2021 preprint [1]. Peterin and Semanišin independently formulated the equivalent *maximal shortest paths cover* number and investigated scalar bounds and values [2]. Their terminology and the equivalence between these definitions are acknowledged. The later geodesic-packing literature studies the minimum transversal number and packing relations [3]. No previously inspected result supplied the labeled inclusion-minimal transversal classification or its exact size-polynomial for all ladders. The minimum scalar value \(2\) is not asserted as a new invariant; the novel claim is the complete minimal-set spectrum, including the threshold for size-three minimal sets.

## Limitations

The result is specific to two-column ladders \(P_h\square K_2\), and does not classify arbitrary grids, cylindrical ladders, edge transversals, strong geodetic sets, or path vertex covers where every path of a fixed length is required to be hit. The originality comparison is provisional: exhaustive priority across all unindexed literature is not possible, and the full published text of [2] could not be re-opened during this comparison; its accessible searchable sections and abstract were evaluated. No independent mathematical audit is claimed.

## References

[1] P. Manuel, B. Brešar, S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042 (first public 2021-01-20), https://arxiv.org/abs/2101.08042 .

[2] I. Peterin, G. Semanišin, *On the Maximal Shortest Paths Cover Number*, Mathematics 9(14), 1592 (2021-07-07), https://doi.org/10.3390/math9141592 .

[3] P. Manuel, B. Brešar, S. Klavžar, *Geodesic packing in graphs*, arXiv:2210.15325 (first public 2022-10-27), https://arxiv.org/abs/2210.15325 .
