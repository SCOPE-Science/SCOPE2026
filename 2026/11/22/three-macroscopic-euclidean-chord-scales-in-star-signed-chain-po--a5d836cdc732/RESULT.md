# Three macroscopic Euclidean chord scales in star signed-chain polytopes

## Finding
For every integer \(m\ge2\), define the full-dimensional centrally symmetric polytope
\[
K_m=\{(z,x_1,\ldots,x_m)\in\mathbb R^{m+1}: |z|\le1,\ |x_i|\le1,\ |z+x_i|\le1\ (1\le i\le m)\}.
\]
This is the signed-chain polytope of the height-two star poset, after choosing the signs of its chains. The Euclidean metric is the **standard coordinate metric** on the displayed variables, not the intrinsic zero-sum metric of graph potentials.

Let \(D_m(q)=\sum_{\{v,w\}\subset\operatorname{Vert}(K_m),\,v\ne w}q^{\|v-w\|_2^2}\), where each unordered pair occurs once. Then its entire squared-chord histogram is
\[
\boxed{D_m(q)=\frac{(2+2q^4)^m+2(2+2q)^m+(4q+2q^4)(1+2q+q^4)^m-3\cdot2^m}{2}.}\tag{1}
\]
All coefficients are nonnegative integers. The vertex count is \(3\cdot2^m\).

For a uniformly chosen unordered pair of distinct vertices, let \(Q_m\) denote its squared distance. The three-scale weak limit is
\[
\boxed{\frac{Q_m}{m}\ \Longrightarrow\ \frac29\delta_{1/2}+\frac23\delta_{3/2}+\frac19\delta_2.}\tag{2}
\]
These three populations have separate Gaussian refinements. Classify vertices into three equal-size types by \(z=1,0,-1\), and choose independent uniform vertices \(V,W\). Conditional on both vertices having the *same nonzero* hub coordinate,
\[
\frac{\|V-W\|^2-m/2}{\sqrt m}\Longrightarrow N(0,1/4).
\]
Conditional on both hub coordinates being zero,
\[
\frac{\|V-W\|^2-2m}{\sqrt m}\Longrightarrow N(0,4).
\]
Conditional on their hub coordinates being different,
\[
\frac{\|V-W\|^2-3m/2}{\sqrt m}\Longrightarrow N(0,9/4).\tag{3}
\]
The same limits hold for an unordered *distinct* pair under the corresponding type conditioning. As further exact information, the greatest squared distance is \(4(m+1)\), attained by one unordered pair; the second-greatest is \(4m+1\), attained by exactly \(2m+2\) unordered pairs. The diameter assertion alone already follows from a broader earlier difference-body theorem and is not asserted to be novel independently.

## Assumptions and scope
The metric is the ordinary Euclidean norm in the \(m+1\) anchored coordinates, with both root coordinate and leaf coordinates having unit weight. A polynomial \(q^k\) records **squared** Euclidean distance \(k\), including \(k=0\) only in the auxiliary ordered-pair polynomial used in the proof. A uniformly chosen unordered pair of distinct vertices means the uniform law on all \(\binom{3\cdot2^m}{2}\) possibilities. The Gaussian laws condition on vertex types; the marginal law without such conditioning is not a single Gaussian. Formula (1) and the Gaussian laws are asserted for all integers \(m\ge2\), with limits as \(m\to\infty\).

## Proof
**1. Exact vertex partition.** Split the hub coordinate into three boundary layers. When \(0\le z\le1\), each leaf lies in \([-1,1-z]\); when \(-1\le z\le0\), it lies in \([-1-z,1]\). Both endpoints of every such interval depend affinely on \(z\). Every point with hub coordinate strictly between successive values in \(\{-1,0,1\}\) is a convex combination of feasible points in its two boundary layers. Hence every vertex lies in one of these three layers. Within each boundary layer, every leaf coordinate must be at an endpoint, otherwise the point admits a nontrivial feasible segment.

Conversely, each endpoint choice in the \(z=1\) and \(z=-1\) layers is a vertex: fixing the active hub facet and one independent endpoint facet per leaf forces a unique point. At \(z=0\), each leaf endpoint \(x_i\in\{-1,1\}\) simultaneously saturates its coordinate bound and the corresponding signed inequality on \(z+x_i\), so the active normals span dimension \(m+1\). Thus the *complete* vertex set is the disjoint union
\[
\begin{aligned}
A_+&=\{(1,x):x\in\{-1,0\}^m\},\\
A_-&=\{(-1,x):x\in\{0,1\}^m\},\\
C&=\{(0,x):x\in\{-1,1\}^m\}.
\end{aligned}\tag{4}
\]
Each class contains exactly \(2^m\) vertices, agreeing with an existing complete face enumeration for the book-graph Lipschitz polytope.

**2. Factorization of all pair distances.** Set \(U_m(q)=\sum_{(v,w)\in\operatorname{Vert}(K_m)^2}q^{\|v-w\|^2}\), counting ordered pairs including identical ones. Independent leaf coordinates allow a product of one-coordinate enumerators. Two vertices in \(C\) give one-coordinate factor \(2+2q^4\). Two vertices in one of \(A_+,A_-\) give \(2+2q\). Any pair from two different classes gives \(1+2q+q^4\). The hub-coordinate squared difference is \(1\) for \(C\)--\(A_\pm\) and \(4\) for \(A_+\)--\(A_-\). Counting both orientations, we therefore obtain the polynomial identity
\[
U_m(q)=(2+2q^4)^m+2(2+2q)^m+(4q+2q^4)(1+2q+q^4)^m.\tag{5}
\]
There are precisely \(3\cdot2^m\) diagonal ordered pairs, each contributing constant term one. Every unordered distinct pair contributes twice. Hence \(D_m=(U_m-3\cdot2^m)/2\), proving (1) as an equality of polynomials. In particular \(U_m(1)=(3\cdot2^m)^2\), verifying the total multiplicity.

**3. Macroscopic and Gaussian limits.** For two independent uniform vertices, the nine equally likely ordered pairs of hub types split into two same-nonzero types, one both-zero type, and six distinct-type pairs. Conditional on either same-nonzero type, each of the \(m\) independent squared leaf distances is \(0\) or \(1\), each with probability \(1/2\), yielding mean \(1/2\) and variance \(1/4\) per coordinate. Conditional on both-zero, each leaf squared difference is \(0\) or \(4\), equally likely, yielding mean \(2\) and variance \(4\). For different types the per-coordinate squared difference is \(0,1,4\) with probabilities \(1/4,1/2,1/4\), yielding mean \(3/2\) and variance \(9/4\). The respective fixed squared hub gaps are \(0,0\), and either \(1\) or \(4\). The law of large numbers and ordinary bounded-variable central limit theorem give (2) and (3). Distinctness conditions remove just \(3\cdot2^m\) of the \(9\cdot4^m\) ordered choices, a proportion \(1/(3\cdot2^m)\); therefore conditioning on unequal vertices does not change the limits.

**4. Extreme chord shells.** Formula (4) or the maximal exponent of (5) gives squared diameter \(4m+4\), appearing in \(U_m\) with coefficient two. The next occupied exponent is \(4m+1\). Its ordered coefficient is \(4m\) from \(A_+\)--\(A_-\) pairs (one leaf squared gap lowered from four to one), plus four from the \(C\)--\(A_\pm\) pairs (all leaf gaps four). Halving gives precisely \(2m+2\) unordered pairs. No intermediate exponent occurs, establishing the additional shell count.

## Verification
Run `python3 verify_book_chords.py` in the same directory as this document. The standard-library checker directly enumerates the three explicit vertex sets and all ordered vertex pairs for \(1\le m\le8\) and compares every distance-polynomial coefficient against an independently expanded version of (5), totaling \(786{,}420\) ordered pairs. It also checks coefficient totals and extreme-shell counts using integer polynomial arithmetic for \(1\le m\le100\). The exact enumeration and high-dimensional polynomial checks confirm examples; the vertex argument, product factorization and probabilistic limit theorem prove the infinite-dimensional assertions.

## Relationship to prior work
Beck and Hlavacek define signed poset order and chain polytopes and the relevant signed-chain inequalities; the present work selects a natural height-two star subfamily. The same body, after a leaf sign reversal, is the **anchored** Lipschitz unit ball of a book graph (two adjacent hubs joined to \(m\) common leaves). The published complete norming-face theorem for that body already gives its face polynomial and in particular the vertex count \(3\cdot2^m\), so the face classification and vertex count are *background*, not asserted to be independently new. A separate book-graph study gives continuous-volume covariance and an inertia transition; it concerns the uniform **interior** distribution rather than the discrete Euclidean pair-distance measure. Another published result determines the volume of the same two-level signed-chain body, and a broader earlier result gives its Euclidean circumradius and diameter as a chain-polytope difference body. These statements do not supply the coefficientwise two-vertex chord polynomial (1) or the three-component distance limit (2)--(3).

The new contribution claimed here is **only** the complete evaluated squared-chord histogram, its three distinct macroscopic scales, and their Gaussian refinements, with an exact second shell. A general face-vector theorem alone has no metric data; conversely the diameter and continuous covariance do not determine the chord histogram. Searches and the inspected literature did not locate an equivalent exact two-vertex generating polynomial, but they cannot establish historical priority conclusively.

## Limitations
No claim concerns the invariant zero-sum metric on all graph potentials, arbitrary weighted book graphs, or other signed posets. The Gaussian description is a conditional limit for *uniform vertices*, not a central limit theorem for uniformly distributed interior points. The anchored-coordinate metric is essential: replacing it by the zero-sum graph metric changes the chord values. Neither the original signed-poset construction, known face counts, known volume, nor known diameter is presented as a new result. A previously unindexed two-point enumerator, potentially written in Lipschitz-free or optimal-transport language, could cover the stated polynomial. Independent audit has not been performed.

## References
1. Matthias Beck and Max Hlavacek, *Signed Poset Polytopes*, arXiv:2311.04409v1, submitted 2023-11-08. https://arxiv.org/abs/2311.04409
2. *Cubical norming faces and a complete face polynomial for book-graph Lipschitz-free spaces*, public result record, 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-cubical-norming-faces-and-a-complete-face-polynomial-for-book-gr--eea1883022b3
3. *Book-graph Lipschitz polytopes have a sharp three-page inertia crossing*, public result record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-book-graph-lipschitz-polytopes-have-a-sharp-three-page-inertia-c--7b1ca41fe5a4
4. *Exact volume and strict imbalance law for two-level signed-chain polytopes*, public result record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-volume-and-strict-imbalance-law-for-two-level-signed-chain--84c1d3d87a65
5. *A second-Greene-width outer-sphere law for classical signed-chain polytopes*, earlier unpublished mathematical statement; used solely to exclude the already-known diameter claim from novelty.
