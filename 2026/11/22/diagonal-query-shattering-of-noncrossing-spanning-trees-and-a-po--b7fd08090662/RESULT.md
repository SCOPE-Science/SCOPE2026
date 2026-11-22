# Diagonal-query shattering of noncrossing spanning trees and a polygon-dissection enumerator

## Finding

Let \(n\ge3\), let \(V_n=\{0,\ldots,n-1\}\) be points in strictly convex cyclic order, and let \(\mathcal T_n\) be all crossing-free straight-line spanning trees on them. Query only the genuine diagonals \(\mathcal D_n\), excluding the \(n\) polygon sides: the Boolean response to diagonal \(d\) is whether \(d\in T\).

**Exact support classification.** For every \(S\subseteq\mathcal D_n\), all \(2^{|S|}\) Boolean query patterns occur among \(\mathcal T_n\) if and only if \(S\) is itself a crossing-free graph without cycles (a noncrossing diagonal forest). In particular,

\[
\operatorname{VCdim}(\mathcal T_n\vert_{\mathcal D_n})=n-3.
\]

Write \(\Phi_n(z)=\sum_{S\subseteq\mathcal D_n:\ S\text{ shattered}}z^{|S|}\). The entire family of polynomials is determined by two algebraic formal power series. Define \(F(x,z)=\sum_{n\ge3}\Phi_n(z)x^{n-1}\), and let \(G(x,z)\in x^2\mathbb Z[z][[x]]\) be the unique series satisfying

\[
G=\frac{(x+zG)^2}{1-x-zG}-\frac{(zG)^2}{1-zG}.
\]

Then

\[
\boxed{F=\frac{(x+zG)^2}{1-x-zG}.}
\]

Furthermore, the top-degree coefficient has a closed form:

\[
\boxed{[z^{n-3}]\Phi_n(z)=n2^{n-5}\quad(n\ge4),}
\]

with \(\Phi_3(z)=1\). Thus the maximum shattered supports are exactly the diagonals of polygon triangulations whose dual graph is a path. For example,

\[
\begin{aligned}
\Phi_5(z)&=1+5z+5z^2,\\
\Phi_6(z)&=1+9z+21z^2+12z^3,\\
\Phi_7(z)&=1+14z+56z^2+77z^3+28z^4.
\end{aligned}
\]

## Assumptions and scope

All polygon vertices are labeled, and segments are straight. Chords are noncrossing when their relative interiors do not intersect; meeting at polygon vertices is allowed. A forest may have isolated vertices and the empty diagonal set is allowed. Concept trees may use *all* polygon sides, even though the query universe consists solely of true diagonals. This last distinction is essential: the theorem does not claim the same classification for an all-edge query universe or a tree class forbidden to use boundary edges.

For the generating functions, \(x\) counts non-root polygon sides, so a polygon with \(n\) vertices contributes degree \(n-1\) in \(x\); \(z\) marks the number of selected diagonals. All identities are formal power series, not analytic convergence assertions.

## Proof

**1. Complete shattering criterion.** If \(S\) is shattered, the labeling that answers yes on every query must be realized by a noncrossing spanning tree. Every subset of a noncrossing tree is acyclic and noncrossing, so \(S\) must be a noncrossing forest.

Conversely, suppose \(S\) is such a forest and prescribe any labeling of its queries. Let \(A\subseteq S\) be the yes-labeled diagonals. Consider the graph \(H\) formed by all \(n\) polygon boundary sides together with \(A\). The boundary cycle makes \(H\) connected, while \(H\) is geometrically noncrossing because the diagonals \(A\) are mutually noncrossing and cannot cross polygon sides. Since \(A\) is a forest, the standard forest-extension property for a connected graph provides a spanning tree \(T\subseteq H\) containing every edge of \(A\). No diagonal of \(S\setminus A\) belongs to \(H\), hence none belongs to \(T\). Thus \(T\in\mathcal T_n\) realizes precisely the assigned pattern. This works for every \(A\), including the empty set.

**2. Noncrossing forests and polygon regions.** A noncrossing diagonal set partitions the convex polygon into polygonal faces. It is acyclic if and only if **every resulting face has at least one original polygon boundary side**. If a face has only selected diagonals on its boundary, these diagonals form a cycle. Conversely, if selected diagonals contain a cycle, the region enclosed by that cycle contains no original polygon boundary side; at least one of its constituent faces therefore has only diagonals on its boundary. Strict convexity ensures that original boundary sides lie outside the interior of any such cycle. The two conditions are equivalent.

**3. An exact recursive dissection.** Root a dissection at a distinguished original polygon side. Its root face has an ordered sequence of \(\ell\ge2\) additional sides. Each additional side is either an original polygon boundary side, contributing \(x\), or an interior selected diagonal, contributing \(zG\) for its recursively attached child region. The root face itself already touches an original boundary side, so no extra constraint is needed. Therefore

\[
F=\sum_{\ell\ge2}(x+zG)^\ell=\frac{(x+zG)^2}{1-x-zG}.
\]

In a child region rooted at a selected diagonal, the face adjacent to its root must contain at least one *other* original polygon boundary side; otherwise it is a face bounded entirely by selected diagonals, forbidden by Step 2. The same ordered-list decomposition applies, except that lists composed entirely of descendant diagonals are excluded. Thus

\[
G=\sum_{\ell\ge2}\left((x+zG)^\ell-(zG)^\ell\right),
\]

which is exactly the stated second equation. Each decomposition is reversible: the ordered list fixes the root face and each recursive child fixes its interior, so no configurations are omitted or multiply counted. Since the recursion adds at least two original-side counts before starting any child, the solution with \(G\in x^2\mathbb Z[z][[x]]\) is uniquely determined recursively coefficient by coefficient. This proves the complete polynomial enumeration.

**4. Dimension and exact maximum faces.** Every noncrossing diagonal set has size at most \(n-3\), with equality exactly for triangulations. Triangulations exist, and the support criterion in Step 1 shows their diagonal sets are shattered if and only if they are forests. Fan triangulations provide such examples for all \(n\ge3\), yielding the claimed VC dimension.

A triangulation's weak dual has one node per triangle and one edge per shared diagonal; it is a tree. Each triangle node has degree equal to its number of interior-diagonal sides. The selected diagonals form a forest precisely when there is no triangle bounded entirely by diagonals, equivalently the dual has no node of degree three. A finite tree with maximum degree at most two is a path. Hence maximum shattered supports are exactly the dual-path triangulations.

Let \(Z_n\) count dual-path triangulations of the labeled convex \(n\)-gon, so \(Z_4=2\). For \(n\ge5\), every dual-path triangulation has exactly two ears. Deleting a marked ear gives a dual-path triangulation on \(n-1\) vertices; conversely an ear can be inserted only along one of the four boundary sides incident with the two terminal triangles of an \((n-1)\)-gon dual-path triangulation. Double-counting marked ears, with cyclic symmetry of the root side in the smaller polygon, gives

\[
2Z_n=\frac{4n}{n-1}Z_{n-1}.
\]

Iterating from \(Z_4=2\) gives \(Z_n=n2^{n-5}\) for all \(n\ge4\). All these triangulations yield distinct diagonal supports. This establishes the top coefficient.

## Verification

The attached pure-Python `verify.py` independently enumerates every noncrossing diagonal forest by a recursion using exact crossing and union-find tests. It also computes the coefficients from the formal two-series equations, and checks equality for every \(3\le n\le12\). The last four computed polynomials have coefficient rows:

- \(n=9\): \((1,27,225,795,1251,792,144)\).
- \(n=10\): \((1,35,385,1875,4430,4965,2320,320)\).
- \(n=11\): \((1,44,616,3927,12804,21725,18183,6512,704)\).
- \(n=12\): \((1,54,936,7532,32109,75522,96482,62472,17664,1536)\).

Separately, for every \(n=3,4,5,6\), the checker enumerates all noncrossing spanning trees among all edge subsets, and checks the actual binary trace on **every** possible diagonal-query support. In total, 549 support instances are directly checked, and all agree with the forest criterion. All enumerations are finite checks of the algebraic proof, not replacements for its all-order argument. Run `python3 verify.py` without dependencies beyond Python 3.

## Relationship to prior work

Flajolet and Noy's classical noncrossing-forest counting theorem enumerates unrestricted forests, including polygon boundary edges, by number of vertices and components; its equations do not directly supply the diagonal-only edge enumerator here. Hurtado and Noy studied triangulations by their number of ears; the numerical count of two-ear triangulations, \(n2^{n-5}\), is classical and is not claimed as new in isolation. The new use of that count here is identifying these triangulations as the maximum shattered diagonal-query supports. Work of Aichholzer and collaborators studies flip reconfiguration of noncrossing spanning trees, including convex configurations, but not Boolean diagonal-query shattering. Keller and collaborators study blocking sets for noncrossing spanning trees; a blocker obstructs every tree but does not determine which designated edge families have all binary traces. A publicly available study of half-turn-fixed noncrossing-forest complexes uses all polygon chords (including sides) and describes fixed-point homotopy types for finitely many even polygon orders; a heptagon noncrossing-tree Fourier study counts vanishing parity characters on all edges. Neither cited result gives the support criterion or the all-size algebraic diagonal-only shattering profile established here.

The present theorem changes the observable edge universe: all boundary sides are available to construct witnesses but are not queries. It is not a rephrasing of an unrestricted forest enumerator, and no assertion of bibliographic uniqueness is made.

## Limitations

No formula is asserted for the shattering polynomial with polygon sides included as queries, nor for nonconvex point sets, or for trees forbidden to use sides. The result is a formal generating-function classification rather than a closed hypergeometric expression for each coefficient. Comparison with accessible literature and indexed findings does not rule out all unindexed or terminologically different prior formulations. No independent external mathematical validation was performed.

## References

1. P. Flajolet and M. Noy, *Analytic Combinatorics of Non-crossing Configurations*, Discrete Mathematics 204 (1999), 203–229, https://igor-kortchemski.perso.math.cnrs.fr/lecon/Analytic%20combinatorics%20of%20non-crossing%20configurations.pdf .
2. O. Aichholzer et al., *Reconfiguration of Non-crossing Spanning Trees*, first publicly posted 2022-06-08, arXiv:2206.03879, https://arxiv.org/abs/2206.03879 .
3. C. Keller, M. Perles, E. Rivera-Campo and J. Urrutia-Galicia, *Blockers for non-crossing spanning trees in complete geometric graphs*, arXiv:1201.4782, https://arxiv.org/abs/1201.4782 .
4. *Half-turn-fixed noncrossing forest complexes through twelve vertices*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-half-turn-fixed-noncrossing-forest-complexes-through-twelve-vert--720207ff1c37 .
5. *Exact Fourier nullity and endpoint stability for seven-vertex noncrossing trees*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-fourier-nullity-and-endpoint-stability-for-seven-vertex-no--e72f53947dae .
6. F. Hurtado and M. Noy, *Ears of triangulations and Catalan numbers*, Discrete Mathematics 149 (1996), 319–324, https://core.ac.uk/download/pdf/82091698.pdf .
