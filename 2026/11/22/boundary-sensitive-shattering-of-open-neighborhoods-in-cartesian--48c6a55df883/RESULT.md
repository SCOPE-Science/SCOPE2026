# Boundary-sensitive shattering of open neighborhoods in Cartesian path boxes

## Finding

Fix an integer \(d\ge1\) and integers \(n_1,\ldots,n_d\ge2\). Let \(G=\square_{i=1}^d P_{n_i}\), where \(P_n\) is the path with \(n\) vertices. Its vertex set is \(V=\prod_{i=1}^d[n_i]\), and two vertices are adjacent precisely when one coordinate differs by one and all others agree. The concept family is **exactly** \(\mathcal N(G)=\{N_G(v):v\in V\}\), the open vertex neighborhoods. Write \(\Phi_{\mathbf n}(z)=\sum_{S\subseteq V:\,S\text{ shattered by }\mathcal N(G)}z^{|S|}\). Set \(N=\prod_i n_i\), and write \((a)_+=\max(a,0)\).

**Theorem.** For every permitted box,
\[
\Phi_{\mathbf n}(z)=1+Nz+C_2(\mathbf n)z^2+C_3(\mathbf n)z^3,
\]
with no other terms. The quadratic coefficient is
\[
C_2(\mathbf n)=\begin{cases}
(n_1-4)_+,&d=1,\\
(n_1-2)n_2+n_1(n_2-2)+2(n_1-1)(n_2-1)-4+2\mathbf1_{\{n_1=n_2=2\}},&d=2,\\
\displaystyle\sum_i(n_i-2)\prod_{j\ne i}n_j+2\sum_{i<j}(n_i-1)(n_j-1)\prod_{k\notin\{i,j\}}n_k,&d\ge3.
\end{cases}
\]
The cubic coefficient vanishes for \(d\le2\). In dimension three it is the boundary-sensitive expression
\[
C_3(n_1,n_2,n_3)=8\left[\prod_{i=1}^3(n_i-2)+\sum_{1\le i<j\le3}(n_i-2)(n_j-2)+\sum_{i=1}^3(n_i-3)_++\mathbf1_{\{\min_i n_i\ge3\}}\right].
\]
For every \(d\ge4\), it simplifies to
\[
C_3(\mathbf n)=8\sum_{\substack{I\subseteq[d]\\|I|=3}}\left(\prod_{i\in I}(n_i-1)\right)\left(\prod_{j\notin I}n_j\right).
\]

The formulas also classify all supports: every singleton is shattered. A pair is shattered in dimension at least three precisely when its graph distance is two. In a two-dimensional box, shattered pairs are exactly distance-two straight-axis pairs and distance-two diagonal pairs with neither point a corner of the whole rectangle. On one path, the pair endpoints must be separated by two edges and neither be an endpoint of the path. A triple can be shattered only when it consists of three distinct-axis neighbors of one center. In dimension at least four every such triple is shattered; in dimension three, it is shattered exactly when each of its vertices has a private singleton-trace witness among the other open neighborhoods, as characterized explicitly in the proof.

Consequently, \(\operatorname{VCdim}=3\) for \(d\ge4\). In dimension three the VC dimension is \(2\) precisely for the permutations of \((2,2,2)\) and \((2,2,3)\), and is \(3\) otherwise. In dimension two it is \(1\) at \((2,2)\) and \(2\) otherwise. In dimension one it is \(1\) for \(2\le n_1\le4\) and \(2\) for \(n_1\ge5\).

Examples: \(\Phi_{(2,2,3)}=1+12z+26z^2\), \(\Phi_{(2,2,4)}=1+16z+40z^2+8z^3\), \(\Phi_{(3,3,3)}=1+27z+99z^2+40z^3\), and \(\Phi_{(2,2,2,2)}=1+16z+48z^2+64z^3\). The last, all-binary case is already encompassed by a known full-Hamming-graph census; the new claim is the complete boundary-sensitive Cartesian-**path** family.

## Assumptions and scope

The number \(n_i\) counts vertices, not edges. Every factor is nontrivial (at least two vertices); a trivial factor may be deleted before applying the theorem. Supports are unordered sets of distinct graph vertices. A support \(S\) is shattered when \(\{N(v)\cap S:v\in V\}=2^S\); there is no additional empty, full, or closed-neighborhood concept. The parameters and the support may be arbitrary, subject to the displayed finite integer hypotheses. No probabilistic sampling, asymptotic assumption, or fixed dimension is needed.

## Proof

**1. Intersection geometry and the degree-three cap.** The box has Manhattan graph distance and is bipartite. Distinct open-neighborhood centers share a neighbor only when their graph distance is two. They share exactly one for a displacement of two along one axis and exactly two for unit displacements along two distinct axes. In particular, any two distinct centers have at most two common neighbors. If a support \(S\) with at least four vertices were shattered, one center \(c\) would contain \(S\) in its open neighborhood. For any three-element subset \(T\subset S\), a different center must have trace \(T\) on \(S\), but that center would share at least three neighbors with \(c\), impossible. Heredity excludes supports of higher order.

**2. Singletons and pairs.** Every point has a neighbor, so a neighbor-center realizes its positive singleton label; the point itself is a center whose *open* neighborhood excludes it, realizing the negative label. A pair \(\{u,v\}\) is shattered exactly when (i) it has a common neighbor, and (ii) each vertex possesses some neighbor not adjacent to the other: the first condition realizes both positives, the second realizes each singleton, and choosing \(u\) itself as center realizes both negatives because every pair with a common neighbor is at graph distance two. Therefore the pair must have a displacement either two on one axis or one on two axes. A straight pair has one common neighbor; a diagonal pair has two. In dimension at least three every vertex has degree at least three, so both types meet (ii). In dimension two straight pairs still meet (ii) since minimum degree is two, whereas diagonal pairs fail exactly when one endpoint is a degree-two corner. There are \(2(n_1-1)(n_2-1)\) diagonal pairs before removing the four corner incidences; in the \((2,2)\) box the two diagonals have both endpoints at corners and were each counted twice, explaining the \(+2\) correction. In dimension one both endpoints of a straight pair must have degree two, giving exactly \((n_1-4)_+\) pairs. Counting straight pairs by their unique varying axis, and diagonal pairs by their unique two varying axes, gives \(C_2\).

**3. Triples and private witnesses.** Let \(S\) be a shattered triple. Some center \(c\) has all three vertices in \(N(c)\). If two selected neighbors are the opposite directions along the same axis, their sole common neighbor is \(c\), which also contains the third selected vertex; thus the two-positive/one-negative trace fails. Accordingly the three neighbors must be selected on three distinct axes. Conversely, for this distinct-axis pattern, \(c\) realizes all positives, the two-axis intermediate center realizes any selected pair, and a selected vertex itself realizes the empty trace since the three selected vertices lie in one bipartition class. Only the three singleton traces remain.

Fix a selected neighbor \(u_i\) in axis \(i\). Every center realizing the trace \(\{u_i\}\) must be a neighbor of \(u_i\) other than \(c\). Its displacement from \(c\) is either two steps in the selected direction along axis \(i\), or a one-step displacement toward \(u_i\) along axis \(i\) and a second step along some *different* axis \(j\). In the second case it also sees a selected neighbor in axis \(j\) exactly when that second step uses that neighbor's chosen direction. Therefore \(u_i\) has a singleton witness precisely if its chosen direction admits a second step, or if \(c\) has an unselected neighbor direction belonging to a different axis. This is a necessary-and-sufficient local criterion for every triple.

If \(d\ge4\), an axis outside the three selected ones always provides such a spare neighbor for all three singleton traces. Each triple then has a unique all-positive center by Step 1. Choosing that center and three axes, and one direction on each, gives the displayed \(C_3\) after summing the per-axis neighbor counts \(\sum_{x=1}^{n_i}\deg_{P_{n_i}}(x)=2(n_i-1)\).

For \(d=3\), classify the all-positive center according to its number \(h\) of interior coordinates (an interior coordinate has two neighboring directions, an endpoint one). The three selected axes use one direction each. For \(h=3\), all eight direction triples are shattered at each center, contributing \(8\prod_i(n_i-2)\). For \(h=2\), each center has two spare directions on different axes, so all four direction triples work, contributing \(8\sum_{i<j}(n_i-2)(n_j-2)\). For \(h=1\), the only spare direction belongs to the sole interior axis. Its selected neighbor needs to extend straight one more step to be isolated; the number of such directed two-step extensions starting at interior positions of a path of length \(n_i\) is \(2(n_i-3)_+\). The other two coordinates each have two endpoint choices, giving \(8\sum_i(n_i-3)_+\). For \(h=0\), all three selected directions must extend a further step; the eight corners succeed exactly when all three side lengths are at least three. These four disjoint cases establish \(C_3\).

**4. VC thresholds.** All coefficients are nonnegative counts. In three dimensions the displayed cubic coefficient is positive exactly when at least two side lengths are at least three, or some side length is at least four. The only complementary sorted triples are \((2,2,2)\) and \((2,2,3)\). The other dimension claims follow directly from \(C_2\) and \(C_3\), finishing the proof.

## Verification

The standalone Python program `verify_pathbox_neighborhoods.py` constructs graph adjacency directly from coordinate moves, and enumerates the trace sets \(N(c)\cap S\) for **every** support through size four on 21 specified boxes, including \((3,3,4)\), \((2,2,2,3)\), and \((2,2,2,2,2)\). It compares independent direct counts to the theorem's formulas and exits with an error on any disagreement. The displayed output from a successful local execution is `ALL_PATHBOX_NEIGHBORHOOD_CHECKS_PASS`. The finite computation checks examples and boundary cases only; the infinite family is established by the four proof steps above.

## Relationship to prior work

Adler, Benediktsson and Macpherson, first publicly available 2020-07-31, establish the degree-three upper bound for open neighborhoods of full Hamming graphs, and its inheritance by induced subgraphs. Cartesian products of paths embed in hypercubes via unary threshold coordinates, so their upper bound also applies here. That bound, and the all-binary special case, are **not** claimed as new. Their Section 4 does not give the complete support coefficients for finite rectangular path products. A subsequent full-Hamming open-neighborhood coefficient census treats products of complete graphs and explicitly leaves induced subgraphs outside its claim; it recovers the special case with every \(n_i=2\). A separate rectangular path-grid result concerns **geodesically convex subsets**, which form a much larger concept class than the individual open neighborhoods studied here. A graph VC algorithm in SEA 2024 uses **closed** neighborhoods and does not provide the displayed all-parameter path-box coefficients.

## Limitations

The theorem does not cover arbitrary induced subgraphs, toroidal grid quotients, closed neighborhoods, or larger-radius balls. Its proofs do not imply historical priority beyond the sources compared. Equivalent formulations in unpublished or unindexed literature could exist; the exact support-polynomial comparison is independent of known scalar VC bounds. No external independent mathematical validation is asserted.

## References

1. I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, version 1 posted 2020-07-31; *Discrete Applied Mathematics* 312 (2022), 29–44, DOI:10.1016/j.dam.2021.09.017; especially Section 4.
2. *Coefficientwise VC-shattering census of open neighborhoods in Hamming graphs*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-coefficientwise-vc-shattering-census-of-open-neighborhoods-in-ha--c2c444ddd1a2; exact full-Hamming open-neighborhood polynomial and explicit exclusion of induced subgraphs.
3. *Exact VC-shattering polynomial of rectangular path grids*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-vc-shattering-polynomial-of-rectangular-path-grids--dd0fe3219184; geodesically convex-set concepts, not open-neighborhood concepts.
4. D. Coudert, M. Csikós, G. Ducoffe and L. Viennot, *Practical Computation of Graph VC-Dimension*, SEA 2024, DOI:10.4230/LIPIcs.SEA.2024.8; closed-neighborhood algorithmic context.
