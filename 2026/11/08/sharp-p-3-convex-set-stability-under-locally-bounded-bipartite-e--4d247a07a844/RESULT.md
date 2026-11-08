# Sharp \(P_3\)-convex-set stability under locally bounded bipartite edge deletion

## Finding

**Theorem (sharp local-deletion threshold).** Let \(d\ge1\) be an integer. Let \(A\) and \(B\) be disjoint vertex sets with \(|A|=m\ge2d+3\) and \(|B|=n\ge2d+3\). From the complete bipartite graph on \(A\cup B\), delete *any* cross-edge set \(F\) for which each vertex is incident with at most \(d\) deleted edges. Write the resulting graph as \(G\).

Then the \(P_3\)-convex vertex subsets of \(G\) are **precisely** the full vertex set and the subsets \(S\) satisfying
\[
|S\cap A|\le1,\qquad |S\cap B|\le1.
\]
Consequently the full cardinality polynomial is
\[
C_G(z)=\sum_{\substack{S\subseteq V(G)\\S\ \text{is }P_3\text{-convex}}}z^{|S|}
=(1+mz)(1+nz)+z^{m+n},
\]
and the number of \(P_3\)-convex sets is \((m+1)(n+1)+1\), independent of which cross edges were deleted. In particular, the \(P_3\)-convex hull of every pair of *distinct vertices on the same shore* is all of \(V(G)\); equivalently, every such pair eventually activates every vertex under the irreversible threshold-two neighbour rule.

The universal threshold is **sharp**: for every \(d\ge1\), there is a graph obtained by deleting at most \(d\) cross edges per vertex from \(K_{2d+2,2d+2}\) with an additional proper \(P_3\)-convex four-vertex set meeting each shore twice. Thus replacing \(2d+3\) by \(2d+2\) for both shores would make the assertion false.

## Assumptions and scope

The graph is finite, simple, and bipartite with the designated shores \(A\) and \(B\); there are no within-shore edges. A \(P_3\)-convex set is one containing the middle vertex of **every** length-two path whose endpoints it contains, whether or not the endpoints are adjacent. Equivalently, each vertex outside the set has at most one neighbour inside it. This is ordinary \(P_3\)-convexity (not a different path-convexity on non-bipartite graphs). The deleted-edge budget is a maximum-degree condition on the bipartite graph \(H=(A\cup B,F)\), not a bound on the total number of missing edges.

## Proof

Fix any \(P_3\)-convex set \(S\), put \(X=S\cap A\) and \(Y=S\cap B\), and set \(a=|X|\), \(b=|Y|\). The graph of missing edges \(H\) has maximum degree at most \(d\).

**Step 1: a proper convex set leaves vertices on both shores.** If \(X=A\) but \(Y\ne B\), then any vertex of \(B\setminus Y\) has at least \(m-d\ge d+3\ge2\) neighbours in \(S\), contradicting convexity. The same reasoning applies with the shores exchanged. Thus any proper convex set satisfies \(a<m\) and \(b<n\). In particular, both complements used below are nonempty.

**Step 2: missing-edge capacity.** Every vertex of \(B\setminus Y\) has at most one graph-neighbour in \(X\), so it must have at least \(a-1\) deleted edges into \(X\). Counting these missing edges from \(B\setminus Y\) and from \(X\) gives
\[
(n-b)(a-1)\le da.\tag{1}
\]
Symmetrically,
\[
(m-a)(b-1)\le db.\tag{2}
\]
Since \(B\setminus Y\) is nonempty, a vertex of that complement has at least \(a-d\) graph-neighbours in \(X\). Convexity therefore forces \(a\le d+1\). Likewise \(b\le d+1\).

**Step 3: excluding large partial selections.** Suppose \(a\ge2\) and \(b\le1\). From (1),
\[
n\le b+\frac{da}{a-1}\le1+2d<2d+3,
\]
contradicting the shore-size hypothesis. The case \(b\ge2\), \(a\le1\) is symmetric. If instead \(a,b\ge2\), exchange shores if necessary so that \(a\le b\). Since the function \(t/(t-1)\) decreases for real \(t>1\), equation (2) implies
\[
m\le a+\frac{db}{b-1}\le a+\frac{da}{a-1}\le2d+2.
\]
The last inequality follows from the identity
\[
\left(a+\frac{da}{a-1}\right)-(2d+2)
=\frac{(a-2)(a-1-d)}{a-1}\le0
\]
for \(2\le a\le d+1\). Again this contradicts \(m\ge2d+3\). Hence every proper convex set has \(a\le1\) and \(b\le1\).

Conversely, a set choosing at most one vertex from each shore is \(P_3\)-convex: any vertex outside it sees at most one selected vertex because graph edges go between shores. The full vertex set is convex vacuously. This proves the classification. Summing over the choices of zero or one vertex per shore proves the generating polynomial and its specialization at \(z=1\). Every \(P_3\)-convex superset of two vertices on the same shore must be the full set, giving the hull and threshold-two activation consequences.

**Step 4: optimality.** Fix \(d\ge1\), let both shores have size \(2d+2\), and label them \(A=\{a_0,a_1,\ldots,a_{2d+1}\}\) and \(B=\{b_0,b_1,\ldots,b_{2d+1}\}\). Delete edges from \(a_0\) to \(b_2,\ldots,b_{d+1}\) and from \(a_1\) to \(b_{d+2},\ldots,b_{2d+1}\). Also delete edges from \(b_0\) to \(a_2,\ldots,a_{d+1}\) and from \(b_1\) to \(a_{d+2},\ldots,a_{2d+1}\). No other edges are deleted. Each of \(a_0,a_1,b_0,b_1\) is incident with exactly \(d\) deleted edges and every other vertex with exactly one, so the maximum deleted degree is \(d\). The set \(\{a_0,a_1,b_0,b_1\}\) is proper, and every outside vertex has exactly one neighbour in it: outside vertices on each shore are missing exactly one of the two selected opposite-shore edges. This proves sharpness for every \(d\).

## Verification

The standard-library script `artifacts/verify.py` independently tests convexity by constructing the adjacency relation and checking every outside vertex's selected-neighbour count. Run from the package root with `python3 artifacts/verify.py`. It exhausts all 1,546 partial matchings deleted from \(K_{5,5}\), checking every labelled vertex subset for each graph. It additionally tests 40 deterministic samples with \((m,n,d)=(5,7,1)\), 28 with \((7,7,2)\), and 14 with \((8,9,2)\), and checks the sharpness construction for all \(1\le d\le24\). Successful output ends with `VERIFY_OK`. These are finite tests, distinct from the unrestricted proof in the preceding section.

## Relationship to prior work

Dourado, Grippo, Lin, and Protti (2026) define and study counting \(P_3\)-convex sets, give a linear-time method on trees and threshold graphs, establish counting hardness on split graphs, and develop general exact exponential-time methods. The present result concerns a different structural class: arbitrary high-density bipartite graphs formed by an adversarial *maximum-degree-bounded deletion*, for which it supplies a universal, sharp closed-set classification and complete polynomial. The cited paper does not supply this threshold or family classification in its inspected HTML text.

The earlier hull-versus-geodetic-number work of Centeno, Penso, Rautenbach, and Pereira de Sá concerns minimum generating sets for threshold-two closure, not the complete family of convex subsets after locally bounded deletions. Cappelle and collaborators (2022) address hull and interval numbers in diameter-two graphs; graphs with even one deleted edge from a sufficiently large complete bipartite graph typically have diameter three, and the stated invariants do not determine the present coefficientwise stability law. Those prior results are not claimed to be false or superseded.

## Limitations

The result applies only under the per-vertex deletion budget and two-shore size bounds; it does not characterize all convex subsets below the threshold or arbitrary sparse bipartite graphs. The sharpness construction proves failure when both shore sizes are decreased to \(2d+2\), not an optimal separate condition for every unbalanced pair. For \(d=0\), complete bipartite graphs also have this classification at smaller shore sizes, so the sharp-threshold assertion is deliberately restricted to \(d\ge1\). Finite tests are supporting evidence only. Literature priority is provisional because unindexed or inaccessible older work may contain a related formulation; there has been no independent mathematical audit.

## References

1. M. C. Dourado, L. N. Grippo, M. C. Lin, and F. Protti, *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706v1, first publicly submitted 2026-03-05. https://arxiv.org/abs/2603.04706
2. C. C. Centeno, L. D. Penso, D. Rautenbach, and V. G. Pereira de Sá, *Geodetic Number versus Hull Number in \(P_3\)-Convexity*, SIAM J. Discrete Math. 27 (2013), 717–731. https://doi.org/10.1137/110859014
3. M. R. Cappelle, E. M. M. Coelho, H. Coelho, B. R. Silva, U. S. Souza, and F. Protti, *\(P_3\)-convexity on graphs with diameter two: Computing hull and interval numbers*, Discrete Applied Math. 321 (2022), 368–378. https://doi.org/10.1016/j.dam.2022.07.013
