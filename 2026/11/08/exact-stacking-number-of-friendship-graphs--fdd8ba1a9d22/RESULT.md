# Exact stacking number of friendship graphs

## Finding
For every integer \(r\ge1\), the friendship graph \(F_r=K_1\vee(rK_2)\), consisting of \(r\) edge-disjoint triangles sharing one central vertex, has stacking number
\[
\operatorname{stack}(F_r)=4r.
\]
A pebbling move along an undirected edge removes two pebbles from its source and places one at its destination. A configuration is stackable when a finite sequence of such moves leaves a nonzero number of pebbles supported on exactly one vertex. The stacking number is the least integer \(t\ge2\) such that every configuration of total mass \(t\) is stackable. Both the upper and lower bounds are unconditional.

## Assumptions and scope
All graphs are finite, simple, and undirected; pebble counts are nonnegative integers. Label the center \(h\) and the vertices of blade \(i\) as \(a_i,b_i\). Each \(h,a_i,b_i\) induces a triangle; different blades intersect only at \(h\). The statement concerns the unweighted standard two-for-one pebbling rule, named vertices, and arbitrary initial configurations, not only almost-stacked configurations. It applies for every \(r\ge1\), including \(F_1=K_3\).

## Proof
**Upper bound.** For an outer blade carrying \(a+b=s\) pebbles, define the guaranteed hub credit
\[
\gamma(0)=0,\quad \gamma(1)=\gamma(2)=-1,\qquad
\gamma(s)=\left\lfloor\frac{s-2}{2}\right\rfloor\quad(s\ge3).
\]
A blade of mass at least four can be emptied into the hub, even when the hub starts empty, producing at least \(\gamma(s)\) hub pebbles. For mass four, the unordered outer distributions \((4,0),(3,1),(2,2)\) produce respectively at least two, one, and two hub pebbles. For mass five, the distributions \((5,0),(4,1),(3,2)\) produce respectively at least one, one, and two hub pebbles. These assertions follow by explicit two-for-one moves along the triangle; for example \((h,a,b)=(0,3,1)\) follows \(a\to b\), \(b\to a\), \(a\to h\). For \(s\ge6\), move two pebbles from any outer vertex with at least two to the hub; the remainder has mass \(s-2\ge4\), and \(1+\gamma(s-2)=\gamma(s)\) completes the induction.

A blade of mass three can always be emptied without reducing a positive hub reserve: the type \((2,1)\) pays one hub pebble, while \((3,0)\) needs one hub pebble in reserve and preserves the hub count. A blade of mass two is either \((2,0)\), paying one pebble, or \((1,1)\), which is emptied from any hub reserve \(H\ge2\) and leaves \(H-1\). A blade of mass one likewise consumes one hub pebble and requires \(H\ge2\). The empty blade is irrelevant.

Let the initial hub count be \(H\), and the outer blade masses be \(s_1,\ldots,s_r\), with \(H+\sum_i s_i=4r\). In every case,
\[
H+\sum_{i=1}^r\gamma(s_i)\ge1.
\]
Indeed \(s\le 2\gamma(s)+4\) for every nonnegative integer \(s\), strictly for \(s\ne2\). When \(H=0\), not all \(s_i\) equal two; summing the strict inequality shows \(\sum\gamma(s_i)\ge1\). When \(H=1\), the ordinary inequality gives \(\sum\gamma(s_i)\ge0\). For \(H\ge2\), it gives \(H+\sum\gamma(s_i)\ge H/2\ge1\). Empty every mass-at-least-four blade first. If \(H\le1\), at least one such blade exists for \(r\ge2\), since otherwise \(\sum_i s_i\le3r<4r-H\). The remaining blade types can now be emptied in decreasing order of their hub contribution, processing zero-cost blades before the negative-cost ones. If a negative-cost blade remains, the final-credit inequality ensures at least two hub pebbles immediately before it is processed. Thus all outer pebbles can be swept into the hub and at least one remains. For \(r=1\) the claim is \(\operatorname{stack}(K_3)=4\), also immediate from the complete-graph theorem or direct inspection.

**Lower bound and blade-resource lemma.** Call a blade initially of type \((1,1)\) a *frozen blade*. It has no legal internal or outward move until the hub sends a pebble into it, costing two hub pebbles. From a hub reserve \(H\ge2\), three moves (hub to one leaf, that leaf to its mate, mate to hub) empty the frozen blade, leaving \(H-1\). This is an optimal resource schedule: any way of emptying it needs at least one hub injection, and no extra injection/internal cycle improves the net hub return. The latter follows by counting the inward moves \(p\), outward moves \(q\), and internal moves \(u\): from initial outer mass two and final outer mass zero, \(2+p-2q-u=0\); since \(p,u\ge1\), the hub change \(q-2p=(2-3p-u)/2\le-1\). In a collection of frozen blades, actions on different blades use only the shared hub. Completing a started blade immediately with the three-move procedure releases its optimal return before another blade starts; postponing its return or making additional injections cannot improve any future reserve. Hence, to empty \(k\) such blades with no other source of hub pebbles, the hub must start with at least \(k+1\), and this is attained by processing them consecutively. To finish with a stack supported on one formerly frozen blade while all others are cleared requires a further unit of hub resource: the chosen pair needs a hub injection and a final internal concentration instead of returning a pebble to the hub.

For \(r\ge2\), set \(k=r-1\). Place \(2k+3=2r+1\) pebbles on \(a_1\), none on \(h,b_1\), and one pebble on each vertex of the other \(k\) blades. This has mass \(4r-1\). It cannot be stacked. To end at the hub, the marked odd pile must be emptied, and its maximum net hub supply is \(k\): at most \(k+1\) direct outward moves leave one pebble, whose removal consumes one hub pebble. This is insufficient to clear \(k\) frozen blades. To end on a formerly frozen blade, the marked blade must again be emptied, and the other frozen blades plus the final concentration consume at least \(k+1\) hub pebbles, also more than the supply. To end in the marked blade, clearing the \(k\) frozen blades requires \(k+1\) hub pebbles. The marked pile can provide at most \(k+1\), achieved only by moving \(k+1\) times directly from \(a_1\) to the hub, leaving exactly one pebble on \(a_1\). The optimal processing of the \(k\) frozen blades then leaves exactly one pebble on the hub and one at \(a_1\). Neither vertex has two pebbles, so no move remains. A nonoptimal choice only reduces the available supply. This excludes every possible terminal vertex.

The lower bound must also exclude smaller totals, because the definition uses the least qualifying total. For every \(2\le t\le2r+1\), an all-singleton configuration on \(t\) vertices is unstackable. For \(2r+2\le t\le4r-1\), use the same \(r-1\) frozen blades but reduce the marked pile to \(t-2r+2\le2r+1\) pebbles. Removing pebbles cannot improve the marked blade's maximum resource supply; the preceding resource argument remains valid. Thus no smaller \(t\) qualifies, and the stacking number is exactly \(4r\). For \(r=1\), the three-singleton configuration on \(K_3\) shows that sizes two and three fail.

The scheduling statement in the frozen-blade lemma is essential: the proof does not assume that arbitrary sequences were originally arranged blade by blade. It uses the exchange fact that immediately completing a started frozen blade maximizes hub availability, so interleavings are dominated by a consecutive schedule. Each other blade is disjoint from it except for the hub.

## Verification
The self-contained Python program `artifacts/verify.py` provides independently implemented exact reachability recurrences for every configuration on \(F_1,F_2,F_3\), checks the local triangle reduction over a range of masses, checks the arithmetic credit inequality over finite parameter ranges, and tests the explicit unstackable family for \(2\le r\le7\). The proof for all \(r\) is the preceding blade-resource and accounting argument, not an extrapolation from the finite runs. Execute with `python3 artifacts/verify.py` from the package root using Python 3.9 or later.

## Relationship to prior work
Csernák and Soukup introduced the stacking number and proved exact values for complete and complete multipartite graphs and paths, as well as general bounds [1]. Their complete-multipartite theorem does not apply: a friendship graph is a clique bouquet, not complete multipartite when \(r\ge2\). Their later Almost Stacked Hypothesis paper addresses cycles, trees, and clearing conditions, without computing this parameter for friendship graphs [2]. Fairfax-Ball's exact tree theorem is also inapplicable because \(F_r\) contains triangles [3]. The present theorem is an unconditional exact result for a natural non-tree cactus family. The shared-small-graph computational reports mentioned in [1] may contain isolated small cases; these would not establish the unrestricted formula.

## Limitations
The theorem concerns unweighted two-for-one moves on the clique bouquet of triangles. It does not establish a stacking formula for arbitrary cacti, generalized windmills with larger cliques, the clearing number, or all block graphs. The initial-source comparison does not exclude equivalent formulas in unindexed material. Independent mathematical validation has not been performed.

## References
[1] T. Csernák and L. Soukup, *Stacking and clearing in graph pebbling*, arXiv:2604.22341, first public 2026-04-24; https://arxiv.org/abs/2604.22341 .

[2] T. Csernák and L. Soukup, *The Almost Stacked Hypothesis: A Conjectural Analogue of Sjöstrand's Cover Pebbling Theorem*, arXiv:2610.09650, first public 2026-10-07; https://arxiv.org/abs/2610.09650 .

[3] J. Fairfax-Ball, *The stacking number of a tree*, arXiv:2609.31811, first public 2026-09-25; https://arxiv.org/abs/2609.31811 .
