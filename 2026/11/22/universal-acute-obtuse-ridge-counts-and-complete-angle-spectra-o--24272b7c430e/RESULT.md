# Universal acute–obtuse ridge counts and complete angle spectra of multipartite edge polytopes

## Finding
Let \(G=K_{a_1,\ldots,a_k}\) be a complete multipartite graph with \(k\ge3\) and each \(a_i\ge3\), and put \(n=\sum_i a_i\). Its ordinary graph-edge polytope in the inherited Euclidean coordinate metric is
\[
P_G=\operatorname{conv}\{e_u+e_v:u,v\text{ belong to distinct parts}\}\subseteq\{x\in\mathbb R^n:\sum_vx_v=2\}.
\]
All codimension-two faces (ridges) have the following **complete intrinsic interior dihedral-angle multiset**:

* Coordinate–coordinate ridges: \(\binom n2\) copies of \(\theta_0=\arccos(1/(n-1))\).
* Coordinate–part-cap ridges with the coordinate inside part \(i\): \(a_i\) copies of \(\theta_i^-=\arccos\sqrt{(n-a_i)/(a_i(n-1))}\).
* Coordinate–part-cap ridges with the coordinate outside part \(i\): \(n-a_i\) copies of \(\theta_i^+=\pi-\arccos\sqrt{a_i/((n-a_i)(n-1))}\).

Consequently, precisely \(\binom n2+n\) ridges are acute and \(n(k-1)\) are obtuse. No right-angled ridges exist. The total ridge count is \(\binom n2+nk\), and its facet-adjacency graph is the complete split graph \(K_n\vee\overline K_k\), independent of all class sizes. If there are \(d\) distinct part sizes, there are exactly \(1+2d\) distinct angle values. Thus the unsigned acute/obtuse census is rigid while the exact angles vary strictly with part size. These are interior angles of adjacent supporting facets, not solid angles of vertex normal cones.

## Assumptions and scope
The graph is finite, simple and undirected. Every part has at least three vertices and there are at least three parts. All distances, facet normals and angles use the standard Euclidean inner product restricted to the \((n-1)\)-dimensional affine hull \(H=\{x:\sum_vx_v=2\}\). A ridge is a face of dimension \(n-3\), and two facets are adjacent precisely when their intersection is a ridge. The interior dihedral angle between facets with nonzero projected outward normals \(u,v\) is \(\pi-\arccos(\langle u,v\rangle/(\|u\|\|v\|))\). The stated angle multiset counts each distinct ridge once. No extension to parts of size one or two is asserted.

## Proof
**1. Complete irredundant facet system.** Let \(A_i\) denote the parts of \(G\). The polytope has the exact description
\[
 P_G=\{x\in\mathbb R^n:x_v\ge0\ (v\in V),\quad \sum_{v\in A_i}x_v\le1\ (1\le i\le k),\quad \sum_vx_v=2\}.
\]
Indeed, its edge vertices satisfy these inequalities. Conversely, for a feasible point define its class masses \(t_i=\sum_{v\in A_i}x_v\). They belong to \([0,1]\), sum to two, and hence lie in the rank-two hypersimplex \(\Delta_{2,k}\), the convex hull of the incidence vectors of pairs of parts. Fixing any convex decomposition of the class masses into pair indicators and independently distributing each chosen class's unit mass among its coordinates according to the normalized within-class entries \(x_v/t_i\) (with arbitrary choices when \(t_i=0\)) expresses the original point as a convex combination of allowed edge indicators. This proves equality. There are \(n\) coordinate facets \(F_v=\{x_v=0\}\) and \(k\) part-cap facets \(U_i=\{\sum_{v\in A_i}x_v=1\}\). Each is genuine: after removing one coordinate, at least three nonempty classes remain and the remaining multipartite edge polytope has dimension \(n-2\); and \(U_i=\Delta_{a_i-1}\times\Delta_{n-a_i-1}\) has dimension \(n-2\). A point with all defining inequalities strict exists, e.g. \(x_v=2/n\), since \(2a_i<n\) is not guaranteed: choose positive class masses strictly below one and summing to two (possible for \(k\ge3\)), then distribute them positively within each part. The corresponding affine dimension is \(n-1\).

**2. Exactly which facet pairs share a ridge.** For distinct vertices \(u,v\), the intersection \(F_u\cap F_v\) is the edge polytope of the graph after deleting the two vertices, which still has at least three nonempty parts, so its affine dimension is \(n-3\). Thus every pair of coordinate facets defines a ridge. The cap face \(U_i\) is a product of two simplices. The intersection \(U_i\cap F_v\), whether \(v\in A_i\) or \(v\notin A_i\), deletes one coordinate of the corresponding simplex; since both factors have at least three vertices, it is a facet of that product and has dimension \(n-3\). Finally, for distinct \(i,j\), the intersection \(U_i\cap U_j\) contains only mass in the two parts \(i,j\), and equals \(\Delta_{a_i-1}\times\Delta_{a_j-1}\) with dimension \(a_i+a_j-2\le n-5\), using the third part's size at least three. Hence two cap facets never define a ridge. There are therefore \(\binom n2\) coordinate pairs and \(nk\) coordinate-cap pairs, establishing both the ridge count and the complete split facet-adjacency graph.

**3. Euclidean normals and all angles.** Write \({\bf1}\) for the all-one vector. Within the affine direction space \(\{x:\sum_vx_v=0\}\), projected outward normals are
\[
 c_v= -e_v+\frac1n{\bf1},\qquad d_i={\bf1}_{A_i}-\frac{a_i}{n}{\bf1}.
\]
Their squared lengths are \(\|c_v\|^2=(n-1)/n\) and \(\|d_i\|^2=a_i(n-a_i)/n\). For \(u\ne v\), \(\langle c_u,c_v\rangle=-1/n\). Moreover,
\[
\langle c_v,d_i\rangle=\begin{cases}-(n-a_i)/n,&v\in A_i,\\a_i/n,&v\notin A_i.\end{cases}
\]
Substitution into the definition of the interior dihedral angle gives precisely \(\theta_0,\theta_i^-,\theta_i^+\) as displayed. Each cap has \(a_i\) inside-coordinate ridges and \(n-a_i\) outside-coordinate ridges. Every coordinate-coordinate or inside-coordinate angle is strictly acute; each outside-coordinate angle strictly obtuse, yielding the universal counts. No normals are orthogonal.

**4. All distinct values.** For \(3\le a\le n-6\), \(\sqrt{(n-a)/(a(n-1))}\) decreases strictly with \(a\), so \(\theta^-(a)\) increases strictly; likewise \(\sqrt{a/((n-a)(n-1))}\) increases and \(\theta^+(a)\) increases strictly. The \(\theta^-\) family is acute, \(\theta^+\) is obtuse. The equation \(\theta^-(a)=\theta_0\) would force \(a=n-1\), impossible under the stated hypotheses. Hence the spectrum has exactly \(1+2d\) distinct values when there are \(d\) distinct sizes.

## Verification
The standalone exact rational checker `ridge_checker.py` constructs the complete edge vertex sets and all supporting facet pairs for six part profiles \((3,3,3)\), \((3,3,4)\), \((3,4,5)\), \((4,4,4)\), \((3,3,3,3)\) and \((3,3,4,4)\). It computes affine dimensions of every double-facet intersection using exact Gaussian elimination, independently checks which intersections are ridges, and compares squared normalized outward-normal inner products and signs against the analytic formulas. It successfully reports `MULTIPARTITE_EDGE_RIDGE_PASS profiles=6 ridge_pairs=603 nonridge_pairs=24`. These finite tests corroborate, but cannot prove, the universal theorem; all-parameter correctness follows from the exact face description and Gram identities above.

## Relationship to prior work
Higashitani and Matsushita (arXiv:2102.02349v1) define precisely these edge polytopes and study the corresponding toric rings, levelness, and Gorenstein conditions; their full text does not give Euclidean dihedral-angle distributions. Tran and Ziegler (arXiv:1307.6708v2) treat face structure and extremal face counts for general graph-edge polytopes, not this metric ridge classification. Ferroni and Schröter's *Face enumeration for split matroid polytopes* develops a broad face-number formula for rank-two matroid base polytopes, which include the same complete multipartite edge polytopes; the numeric ridge count alone is accordingly not claimed as new. Related work on normal-cone angles of rank-two matroid base polytopes calculates **vertex exposure solid angles**, and work on multipartite **stable-set** polytopes concerns a distinct polytope with different inequalities and angular statistics. Neither implies this face-by-face Euclidean dihedral-angle multiset or the universal acute/obtuse split.

## Limitations
The theorem does not classify Euclidean ridge areas, higher-codimension angles, or small-part boundary cases. Its facet graph and raw ridge count are elementary consequences of the known rank-two matroid face structure; its asserted mathematical contribution is the sharp Euclidean angular classification, rigidity of acute/obtuse counts and strict angular dependence on part sizes. Priority remains provisional because unindexed equivalent angle computations may exist. Independent mathematical validation has not been performed.

## References
- Akihiro Higashitani and Koji Matsushita, *Levelness versus almost Gorensteinness of edge rings of complete multipartite graphs*, arXiv:2102.02349v1, first public 2021-02-04, https://arxiv.org/html/2102.02349v1.
- Tuan Tran and Günter M. Ziegler, *Extremal edge polytopes*, arXiv:1307.6708v2, https://arxiv.org/html/1307.6708v2.
- Luis Ferroni and Benjamin Schröter, *Face enumeration for split matroid polytopes*, Combinatorics, Probability and Computing (2025), Section 2.6, https://doi.org/10.1017/S0963548325000021.
