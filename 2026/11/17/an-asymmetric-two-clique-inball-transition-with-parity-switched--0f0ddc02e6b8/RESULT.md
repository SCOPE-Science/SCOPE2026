# An asymmetric two-clique inball transition with parity-switched optimal-center dimensions

## Finding

Let \(2\le a\le b\) be integers. Glue the complete graphs \(K_{a+1}\) and \(K_{b+1}\) at exactly one common vertex (the hub), with all edges of length \(1\), and give the resulting vertex set its shortest-path metric. Write \(N=a+b+1\) and let \(P_{a,b}\) be the real Lipschitz-free unit ball in the intrinsic Euclidean zero-sum coordinates, equivalently the symmetric edge polytope of this graph.

Define
\[
 Q_{a,b}(t)=a+t-\frac{(t-a)^2}{N}\quad(1\le t\le b),\qquad
 \alpha_{a,b}=\frac{3a+b+1}{2},
\]
and let \(J_{a,b}\subset\{1,\ldots,b\}\) be the one or two integers nearest to \(\alpha_{a,b}\) in that interval. Then the **global**, unrestricted-center Euclidean inradius \(\rho_{a,b}\), the number \(T_{a,b}\) of facets tangent to the largest *origin-centered* ball, and the affine dimension of the full set \(\mathcal C_{a,b}\) of centers of all largest balls are
\[
\boxed{\rho_{a,b}^{-2}=\max_{1\le t\le b} Q_{a,b}(t),\qquad
 T_{a,b}=2\sum_{t\in J_{a,b}}\binom bt,}
\]
\[
\boxed{
\dim\operatorname{aff}\mathcal C_{a,b}=
\begin{cases}
 a+b-1,&J_{a,b}=\{b\},\\
 a,&|J_{a,b}|=1,\ J_{a,b}\ne\{b\},\\
 a-1,&|J_{a,b}|=2.
\end{cases}}
\]
The origin is an optimal center and belongs to the relative interior of \(\mathcal C_{a,b}\).

This becomes an exact sharp transition in the blade-size imbalance:

* If \(a\le b\le3a+1\), then \(J_{a,b}=\{b\}\),
  \[\rho_{a,b}^{-2}=a+b-\frac{(b-a)^2}{a+b+1},\quad T_{a,b}=2,\quad\dim\operatorname{aff}\mathcal C_{a,b}=a+b-1.\]
* At \(b=3a+2\), both \(b-1\) and \(b\) maximize, so
  \[\rho_{a,b}^{-2}=a+b-\frac{(b-a)^2}{a+b+1},\quad T_{a,b}=2(b+1),\quad\dim\operatorname{aff}\mathcal C_{a,b}=a-1.\]
* For \(b\ge3a+3\), the larger blade is no longer fully occupied by a maximizing potential. If \(N\) is even, then \(J_{a,b}=\{\alpha_{a,b}\}\) and
  \[\rho_{a,b}^{-2}=2a+\frac N4,\quad T_{a,b}=2\binom b{\alpha_{a,b}},\quad\dim\operatorname{aff}\mathcal C_{a,b}=a.\]
  If \(N\) is odd, then \(J_{a,b}=\{\lfloor\alpha_{a,b}\rfloor,\lceil\alpha_{a,b}\rceil\}\) and
  \[\rho_{a,b}^{-2}=2a+\frac N4-\frac1{4N},\quad T_{a,b}=2\left(\binom b{\lfloor\alpha_{a,b}\rfloor}+\binom b{\lceil\alpha_{a,b}\rceil}\right),\quad\dim\operatorname{aff}\mathcal C_{a,b}=a-1.\]
At the threshold, the incenter-locus affine dimension collapses from \(a+b-1\) to \(a-1\); above it the locus alternates between dimensions \(a\) and \(a-1\) according to parity. All parameters are integer, and these statements include every boundary.

## Assumptions and scope

All vertices and edges are labeled. Let the hub be \(o\), and let \(A\) and \(B\) denote the other \(a\) and \(b\) vertices of their respective cliques. Thus edges occur inside \(\{o\}\cup A\) and inside \(\{o\}\cup B\), but not between \(A\) and \(B\). The distance between distinct vertices from different blades is \(2\), and all other nonzero distances are \(1\).

The ambient norm for Euclidean balls is inherited from \(\mathbb R^N\) on \(H=\{z\in\mathbb R^N:\sum_{v}z_v=0\}\); it is **not** the different norm obtained by deleting the hub coordinate. With \(e_v\) the usual standard basis vectors,
\[
P_{a,b}=\operatorname{conv}\{\pm(e_v-e_w):vw\in E(G_{a,b})\}\subset H.
\]
This equals the real Lipschitz-free unit ball for the unit-edge shortest-path metric because for two nonadjacent vertices the distance-two molecule is the average of the two signed edge molecules on a shortest path. A facet means a codimension-one face of \(P_{a,b}\), and all centers of largest Euclidean balls are permitted in the global inradius. The theorem does not assert an optimal ball is unique.

## Proof

**1. Complete classification of polar vertices.** The polar in \(H\) is
\[
P_{a,b}^{\circ}=\{u\in H:|u_v-u_w|\le1\ \text{whenever}\ vw\in E(G_{a,b})\}.
\]
Represent a potential modulo additive constants by fixing its hub value to \(0\); recover the vector in \(H\) by subtracting its mean from all \(N\) entries. A feasible potential is extreme precisely when its graph of edges on which the difference has absolute value \(1\) is connected. Indeed, the active edge-incidence equalities have rank \(N-1\) on \(H\) exactly for a connected tight-edge graph; if disconnected, one can change one connected component of the potential slightly while retaining all inactive strict inequalities. This proves both directions without assuming integrality.

For any extreme potential, following a spanning tree of tight edges from the hub shows that its entries are integers. Since each nonhub vertex is directly adjacent to the hub, each leaf value lies in \(\{-1,0,1\}\). Within a clique blade, \(+1\) and \(-1\) cannot coexist because their difference would be \(2\). A blade with only zero entries would contain no tight path to the hub and would contradict connectedness. Conversely, a blade with a nonempty collection of \(+1\)'s and the rest zero, or a nonempty collection of \(-1\)'s and the rest zero, is connected by tight edges to the hub, including every zero leaf through some nonzero leaf. Therefore **every polar vertex and no other feasible potential** is obtained by independently choosing in each blade a sign and a nonempty subset on which that sign is attained, with zeros on the other leaves.

**2. Strict screening of all but one integer parameter.** Let \(k\in\{1,\ldots,a\}\) and \(t\in\{1,\ldots,b\}\) denote the numbers of nonzero entries in the two blades. Opposite blade signs strictly improve the squared Euclidean norm over equal signs: the count of nonzero entries is unchanged while the absolute total potential changes from \(k+t\) to \(|k-t|\). A centered polar vertex with opposite signs therefore has squared norm
\[
\Phi(k,t)=k+t-\frac{(k-t)^2}{N}.
\]
If \(k<a\) and \(t<b\), the legal simultaneous increment \((k,t)\mapsto(k+1,t+1)\) increases \(\Phi\) by exactly \(2\), so cannot occur at the maximum. If \(k<a\) and \(t=b\), the legal increment \(k\mapsto k+1\) increases \(\Phi\) by
\[
1+\frac{2(b-k)-1}{N}>0.
\]
Consequently **every farthest polar vertex uses all \(a\) vertices of the smaller blade**. The remaining squared norm is the one-variable quadratic
\[
\Phi(a,t)=Q_{a,b}(t)
=2a+\frac N4-\frac{\left(t-\alpha_{a,b}\right)^2}{N}.
\]
Its maximum over the integers \(1\le t\le b\) is achieved precisely at the nearest allowed integer(s) to \(\alpha_{a,b}\), proving the first displayed formula and completely identifying the polar farthest vertices.

These vertices correspond to all opposite-sign patterns with all \(a\) smaller-blade leaves nonzero and exactly \(t\in J_{a,b}\) larger-blade leaves nonzero, with either overall sign. Thus their number, and hence the number of facets tangent to the central ball, is \(2\sum_{t\in J_{a,b}}\binom bt\), proving the second formula.

**3. Global Euclidean inradius.** Write \(R=\max_{u\in P_{a,b}^{\circ}}\|u\|_2\), attained at an extreme polar vertex by convexity of Euclidean norm. The polar inequalities are \(u\cdot z\le1\). Therefore the largest **origin-centered** Euclidean ball in \(P_{a,b}\) has radius \(R^{-1}\). Since \(P_{a,b}=-P_{a,b}\), reflection carries a ball centered at \(c\) to one of the same radius centered at \(-c\); convexity then implies the midpoint, origin-centered ball has the same radius and lies in \(P_{a,b}\). Hence no shifted ball has greater radius, and \(\rho_{a,b}=R^{-1}\) is global.

**4. Affine dimension of all optimal centers.** Let \(\mathcal V\) denote the finite polar-vertex set, and \(\mathcal V_*\) the just-classified subset with norm \(R\). The full optimal-center set is exactly
\[
\mathcal C_{a,b}=\{c\in H:u\cdot c+R^{-1}\|u\|_2\le1\quad(\forall u\in\mathcal V)\}.
\]
Both \(u\) and \(-u\) occur in \(\mathcal V_*\), so \(\mathcal C_{a,b}\) is contained in \(L=\mathcal V_*^{\perp}\cap H\). Conversely every noncontact vertex satisfies \(R^{-1}\|u\|_2<1\); because only finitely many such inequalities occur, a sufficiently small relative ball about \(0\) inside \(L\) satisfies all of them. Thus \(\operatorname{aff}\mathcal C_{a,b}=L\), and \(\dim\operatorname{aff}\mathcal C_{a,b}=a+b-\operatorname{rank}\mathcal V_*\).

For ranks, use the injective linear map from hub-zero leaf vectors \(\mathbb R^{a+b}\) into \(H\) obtained by including hub coordinate \(0\) and subtracting the mean. We may therefore compute ranks before centering. If \(J=\{b\}\), the contact vectors consist of just a vector with all \(a\) small-blade entries \(+1\), all \(b\) large-blade entries \(-1\), and its negative: rank \(1\). If \(J=\{t\}\) with \(1\le t<b\), the differences of incidence vectors of all \(t\)-element subsets of \(B\) span the \((b-1)\)-dimensional zero-sum subspace of \(\mathbb R^{B}\), and one contact vector with constant nonzero entries on \(A\) is independent of it. The rank is \(b\). If \(J=\{t,t+1\}\), where \(1\le t<b\), subtracting contact vectors for nested \(t\)- and \((t+1)\)-element subsets gives each individual basis vector in \(\mathbb R^B\); adding one contact vector with nonzero \(A\)-entries yields rank \(b+1\). Subtraction from \(a+b=\dim H\) gives all three center dimensions in the theorem. No genericity assumption was used.

**5. Exact parameter boundary and parity.** The quadratic vertex is \(\alpha_{a,b}=(3a+b+1)/2\). The top endpoint \(b\) is the sole nearest integer exactly while \(\alpha_{a,b}\ge b\), equivalent to \(b\le3a+1\). At \(b=3a+2\), \(\alpha=b-1/2\), so the endpoints \(b-1\) and \(b\) tie. For \(b\ge3a+3\) the optimum is interior, with a unique integer maximizer for even \(N\) and two adjacent maximizers for odd \(N\). Completing the square yields \(2a+N/4\) when \(N\) is even and \(2a+N/4-1/(4N)\) when odd. These are precisely the announced piecewise formulas, including the threshold.

## Verification

The standalone `verify.py` (standard Python 3 only) independently enumerates all signed nonempty blade patterns and computes uncentered squared-norm numerators \(N\|u\|_2^2\) using integers, not floating point. It checks 17 parameter instances and \(2{,}176{,}596\) polar candidates against the theorem, including both sides of the threshold. For smaller instances it independently enumerates the entire tight-edge inequality system over ternary assignments and confirms the polar extreme-vertex description. Rational Gaussian elimination checks contact-normal ranks for eligible sizes. An additional 1,485 integer parameter profiles check the exact quadratic maximizer and its strict/tie boundary.

The reproduced terminal output is:

```text
EXACT_POLAR_PRODUCT_MAX_CONTACT_PASS cases=17 checked_vertices=2176596
INDEPENDENT_TIGHT_EDGE_GRAPH_AND_CENTER_RANK_PASS
INTEGER_QUADRATIC_THRESHOLD_EXACT_PASS profiles=1485
TWO_CLIQUE_INBALL_AND_INCENTER_ALL_CHECKS_PASS
```

Finite checks do not establish the infinite theorem; the proof above gives all-parameter coverage. As illustrations, when \((a,b)=(2,7)\), \(\rho^{-2}=13/2\), there are two contacts and the center-locus dimension is \(8\); at \((2,8)\) the corresponding quantities are \(74/11\), \(18\), and \(1\); at \((2,9)\) they are \(7\), \(18\), and \(2\).

## Relationship to prior work

The known equal-blade windmill result, *Euclidean inballs of clique-windmill symmetric edge polytopes* (2026), proves formulas for \(m\) **equal-size** cliques sharing one hub, and its stated scope excludes unequal blades. Its special case of two equal blades agrees with this theorem when \(a=b\), but it does not determine the asymmetric screening threshold, the new partial-blade contacting facets, or the parity-switching dimensions; those changes cannot be inferred from an all-full-blade formula. This precise equal-blade overlap is acknowledged, not claimed as new.

Chen, Davis and Korchevskaia classify facet subgraphs of symmetric edge polytopes. Mori, Mori and Ohsugi count facets for join graphs and present the integer-valued facet-label criterion. Their facet counts do not distinguish which facets lie closest to the origin in the intrinsic zero-sum metric, nor rank their touching normals. The 1-sum total-facet formula yields \((2^{a+1}-2)(2^{b+1}-2)\) facets here, **not** the contact count or Euclidean inradius. General results on Lipschitz-free extreme points and graph spread motivate the duality and the maximum-variance formulation but do not directly evaluate the full asymmetric two-clique family. Since maximum squared norm divided by \(N\) is the graph spread (maximum variance of a 1-Lipschitz function), an alternative formulation under that name is the principal remaining priority risk.

## Limitations

The theorem requires exactly **two** clique blades, with integer sizes \(2\le a\le b\), a single shared hub, unit graph-edge lengths, and the canonical Euclidean zero-sum coordinates. It does not claim formulas for three or more unequal blades, clique blades connected by bridges, weighted edges, or different Euclidean coordinate metrics. It determines the affine hull dimension, not the complete inequality description or volume of the optimal-center set. No infinite theorem follows from the finite checker alone. Potential prior statements in differently indexed maximum-Lipschitz-variance literature remain a qualified originality risk. No independent mathematical audit has been performed.

## References

1. Ramón J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, first publicly available 1 February 2021, arXiv:2102.01219, https://arxiv.org/abs/2102.01219. Functional-analytic setting and 46B20 motivation; not a claim of a prior Euclidean-radius formula.
2. Tianran Chen, Robert Davis and Evgeniia Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, first publicly available 26 July 2021, arXiv:2107.12315, https://arxiv.org/abs/2107.12315.
3. Aki Mori, Kenta Mori and Hidefumi Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, first publicly available 18 December 2023, arXiv:2312.11287, https://arxiv.org/abs/2312.11287.
4. *Euclidean inballs of clique-windmill symmetric edge polytopes*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-euclidean-inballs-of-clique-windmill-symmetric-edge-polytopes--3dbe8167618b.
5. Louigi Addario-Berry, Svante Janson and Colin McDiarmid, *On the spread of random graphs*, arXiv:0902.1156, https://arxiv.org/abs/0902.1156. Related general terminology only.
