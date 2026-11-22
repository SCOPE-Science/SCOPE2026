# Exact graph balls and contact-edge boundaries in the 21-neighbor convex tiling

## Finding
Let \(\mathcal T\) be a monohedral tiling of the Euclidean plane by congruent compact convex tiles with disjoint interiors. Assume that each tile has exactly 21 neighbors, counting any nonempty boundary contact, including an isolated point. Let \(G\) be the simple *contact graph*: vertices are tiles, and distinct tiles are adjacent precisely when they intersect. Let \(B_r(v)\) be the set of tiles at graph distance at most integer \(r\ge0\) from a given tile \(v\). Write \(\partial_E B_r\) for the set of graph edges with exactly one endpoint in \(B_r\).

By the equality-rigidity theorem of Yang and Wang [1], the tiling is, up to similarity, the central subdivision of the standard equilateral-triangle tiling. In this unique equality case the contact graph has the exact structure
\[
 G\cong L(T)[K_2],
\]
where \(T\) is the six-regular triangular-lattice graph and \(L\) denotes the graph line graph; the bracket is the lexicographic graph product. In particular the graph is vertex-transitive and 21-regular. Its complete ball-size and outgoing contact-edge profiles are
\[
 |B_0(v)|=1,\qquad |\partial_E B_0(v)|=21,
\]
\[
 \boxed{|B_r(v)|=18r^2+6r-2,\qquad |\partial_E B_r(v)|=192r-8\quad (r\ge1).}
\]
The first distance sphere has 21 tiles; for every integer \(r\ge2\), the distance-\(r\) sphere has exactly \(36r-12\) tiles. The ball growth series is
\[
 \sum_{r\ge0}|B_r(v)|z^r=\frac{1+19z+19z^2-3z^3}{(1-z)^3}.
\]

## Assumptions and scope
The geometric uniqueness input is the recent, published-as-preprint theorem [1], with submission date November 10, 2026. The present statement concerns the specific equality tiling, not other monohedral tilings, and uses *all* point contacts as edges, not just side-sharing contacts. All radii are integers. Edges in \(\partial_E B_r\) are counted individually, even when multiple distinct pairs of tiles meet at one planar point. The combinatorial formulas do not depend on the common tile's scale or the chosen center tile.

## Proof
**1. A tile is an edge-face incidence.** Let the vertices of \(T\) be \(\mathbb Z^2\), with elementary undirected edge directions \((1,0)\), \((0,1)\), \((1,-1)\) in affine triangular coordinates. The central subdivision replaces every equilateral face \(F\) by three smaller triangles \(\operatorname{conv}(u,v,c_F)\), one for each side \(e=\{u,v\}\subset F\), where \(c_F\) is the center of \(F\). Every lattice edge lies in exactly two equilateral faces, hence gives exactly two small tiles.

Two small triangles touch if and only if their base lattice edges share at least one lattice vertex. Indeed a small triangle has only its two base endpoints and its face center as vertices. Intersections across distinct large faces can occur only on their common base edge or at a large-face vertex; within one large face, each pair of bases shares a vertex. A shared face center also implies that the two bases belong to the same face and so share a vertex. Conversely, at each lattice vertex all small tiles on incident base edges contain that vertex. Thus replacing each edge-vertex of the line graph \(L(T)\) by two adjacent twins gives exactly \(G=L(T)[K_2]\). Since a triangular-lattice edge is adjacent to ten other lattice edges, every small tile has \(2\cdot10+1=21\) neighbors, agreeing with [1].

**2. Balls reduce to incident-edge sets.** Fix the initial base edge \(e_0=\{(0,0),(1,0)\}\) and one of its two small triangles. For distinct lattice edges \(e,f\),
\[
 d_{L(T)}(e,f)=1+\min_{u\in e,\,w\in f}d_T(u,w),
\]
which follows by converting any chain of incident edges into an endpoint path and conversely. The twins of \(e_0\) have distance one; for \(r\ge1\) the blow-up ball is exactly the two twins of every lattice edge in the radius-\(r\) ball of \(L(T)\). Put \(k=r-1\), and define
\[
 S_k=B_k^T((0,0))\cup B_k^T((1,0)).
\]
The corresponding lattice edges are precisely all edges with at least one endpoint in \(S_k\). The triangular-lattice metric is
\[
 d_T((x,y),(0,0))=\max\{|x|,|y|,|x+y|\},
\]
so direct substitution gives the exact coordinate description
\[
 S_k=\{(x,y)\in\mathbb Z^2:-k\le x\le k+1,\ -k\le y\le k,\ -k\le x+y\le k+1\}.
\]

**3. Counting base edges.** For \(k\ge1\), the convex lattice hexagon above has successive vertices \((k+1,0)\), \((k+1,-k)\), \((0,-k)\), \((-k,0)\), \((-k,k)\), \((1,k)\). Its coordinate area is \(3k^2+2k\) and its lattice boundary count is \(6k+2\), by the determinant and gcd formulas applied to these six edges. Pick's theorem yields
\[
 |S_k|=3k^2+5k+2.
\]
The same count holds at \(k=0\), when \(S_0\) consists of the two adjacent vertices. For every \(k\ge0\), the outside vertices adjacent to \(S_k\) are exactly \(S_{k+1}\setminus S_k\), which has \(6k+8\) vertices by the count just established. In that ring, precisely the six points \( (-k-1,0), (-k-1,k+1), (0,-k-1), (1,k+1), (k+2,-k-1), (k+2,0) \) have one neighbor in \(S_k\); each of the remaining \(6k+2\) points has two neighbors in \(S_k\). This follows by checking the six allowed unit steps \(\pm(1,0),\pm(0,1),\pm(1,-1)\) against the displayed inequalities, and includes the degenerate case \(k=0\). None of these outside vertices has more than two interior neighbors. Therefore the number of triangular-lattice edges leaving \(S_k\) is
\[
 b_k=2(6k+2)+6=12k+10.
\]
By the degree-six identity, the number \(I_k\) of lattice edges with at least one endpoint in \(S_k\) is
\[
 I_k=\tfrac12(6|S_k|+b_k)=9k^2+21k+11.
\]
Each such edge indexes two small tiles. Hence for \(r=k+1\ge1\),
\[
 |B_r(v)|=2I_{r-1}=18r^2+6r-2.
\]

**4. Exact edge cuts.** Consider the line graph \(L(T)\). For each vertex \(w\notin S_k\) adjacent to \(S_k\), write \(a_w\) for its number of incident lattice edges with the other endpoint in \(S_k\). The six edges incident to \(w\) induce a clique in \(L(T)\), with exactly \(a_w(6-a_w)\) edges crossing the ball boundary. There are no other crossings, and no line-graph edge is double-counted because two distinct lattice edges meet at at most one vertex. The exterior-neighbor counts above give
\[
 |\partial_E B^{L(T)}_r(e_0)|=6(1\cdot5)+(6k+2)(2\cdot4)=48k+46.
\]
Each crossing edge of \(L(T)\) lifts to four crossing edges between its two two-vertex fibers in \(G\). Since the whole fiber of every base edge is inside or outside the ball for \(r\ge1\), there is no extra crossing from a fiber-internal edge. Thus
\[
 |\partial_E B_r(v)|=4(48(r-1)+46)=192r-8.
\]
At \(r=0\), the 21-regularity gives boundary size 21. Subtraction of successive ball counts gives the sphere profile. The stated generating function follows by summing the quadratic formula with its special radius-zero value. \(\square\)

## Verification
The included standard-library file `verify_contact_growth.py` checks actual rational-coordinate intersection/nonintersection of 150 small triangles across 11,175 pairs; 61 exact combinatorial incident-edge enumerations for \(0\le k\le60\); and independent contact-graph breadth-first searches through radius eight, including outgoing-edge cut checks through radius seven. All checks passed on the included source. They are finite corroboration only. The proof for all integer radii uses the coordinate hexagon, Pick's theorem and exterior-neighbor counts.

Run using `python3 verify_contact_growth.py`; no external dependencies or downloaded data are needed.

## Relationship to prior work
Yang and Wang [1] proved the sharp neighbor bound 21 and the uniqueness of its central-triangular-subdivision equality case. The uniqueness, local degree and geometry of the construction are **prior results**, not claimed as new here. The graph factorization and complete ball/cut formulas are the present additional statements, and are not stated in the introduction, equality-case proof, or inspected appendices of [1]. Friedman and van der Zwaag [2] reproduced earlier 21-neighbor examples and studied other uniform neighbor counts but do not supply these shortest-path or graph-cut profiles. The formulas should not be confused with the edge-adjacency (shared-side only) graph explicitly used in [1] to propagate equality: this theorem uses all contacts, including points.

## Limitations
The result is restricted to the equality tiling characterized in [1]. It does not classify metric growth in other monohedral tilings, nor claim a sharp graph isoperimetric inequality for arbitrary vertex sets: \(\partial_E B_r\) is the boundary **of balls**, not a minimizer assertion. The predecessor constructions from Fejes Tóth (1975) were identifiable through [1,2] but that original full text was not materially inspected. Exact priority versus unindexed or unpublished contact-graph computations remains unverified, and no independent mathematical audit was performed.

## References
[1] Yahui Yang and Erxiao Wang, *Convex monohedral tilings: a sharp neighbor bound and rigidity in the equality case*, arXiv:2611.13664v1, first public November 10, 2026. https://arxiv.org/html/2611.13664v1

[2] Erich Friedman and Berend Jan van der Zwaag, *Constant Neighbor Dihedral Tilings with 15, 32, and 43 Neighbors*, https://erich-friedman.github.io/papers/dihedral/dihedral.html (text and Figures 1–4 inspected).

[3] L. Fejes Tóth, *Tesselation of the plane with convex polygons having a constant number of neighbors*, Amer. Math. Monthly **82** (1975), 273–276 (historical source identified through [1,2]; not full-text inspected).
