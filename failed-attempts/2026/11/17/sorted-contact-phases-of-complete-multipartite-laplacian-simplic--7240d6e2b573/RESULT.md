# Sorted contact phases of complete multipartite Laplacian simplices

## Finding
Let \(r\ge3\), let \(a_1,\ldots,a_r\) be positive integers, and set \(n=\sum_{i=1}^r a_i\). Let \(G=K_{a_1,\ldots,a_r}\) be the complete multipartite graph, \(L=D-A\) its ordinary graph Laplacian, and
\[
P_G=\operatorname{conv}\{Le_v:v\in V(G)\}\subset\mathbf1^\perp\subset\mathbb R^n
\]
its canonical full-column Laplacian simplex with the inherited Euclidean metric. Define
\[
b_i=(n-a_i)(n-a_i+1),\qquad T_i=b_i+2n.
\]
There is a **unique real number** \(m\) satisfying the scalar equation
\[
\boxed{\sum_{i=1}^r a_i(T_i-m)_+=2n^2},\qquad(z)_+=\max\{0,z\}.
\]
Put
\[
t_i=\frac{(T_i-m)_+}{2n}-1,\qquad
c=\sum_i t_i\mathbf1_{A_i},\qquad
\boxed{R^2=m+\sum_i a_i t_i^2},
\]
where \(A_i\) is the \(i\)-th vertex class. Then \(c\) is the **unique center of a smallest enclosing Euclidean ball** of \(P_G\), and \(R\) is its radius. A Laplacian-column vertex in class \(A_i\) lies on the sphere **if and only if** \(T_i\ge m\). If \(T_i<m\), its exact squared-distance clearance is \(m-T_i\). The unique barycentric probability certificate has per-vertex weight
\[
\boxed{w_v=\frac{(T_i-m)_+}{2n^2}\quad(v\in A_i)}.
\]
In particular, at \(T_i=m\), all vertices of that class touch the sphere but have **zero** weight in the unique optimality certificate.

The formula is explicitly evaluable with rational arithmetic after sorting the class sizes \(a_1\le\cdots\le a_r\), so \(T_1\ge\cdots\ge T_r\). Exactly one \(k\in\{1,\ldots,r\}\) obeys \(T_k>m_k\ge T_{k+1}\), where \(T_{r+1}=-\infty\) and
\[
\boxed{m_k=\frac{\sum_{i=1}^k a_i T_i-2n^2}{\sum_{i=1}^k a_i}}.
\]
Then \(m=m_k\), and precisely the first \(k\) classes carry positive optimality weight. All vertices contact exactly when \(\overline b\le \min_i T_i\), where \(\overline b=\sum_i a_i b_i/n\); all certificates are strictly positive exactly when the inequality is strict.

The contact classification has a genuine multipartite phase hierarchy even at fixed order \(n=38\): profiles \((12,13,13)\), \((2,8,28)\), and \((4,17,17)\) yield respectively \(38\), \(10\), and \(4\) contacting vertices. At the exact critical profile \((3,3,6)\), all \(12\) vertices contact, but only the first two three-vertex classes receive positive certificate weights.

## Assumptions and scope
The graph is simple, unweighted, undirected and complete multipartite, with **at least three** nonempty parts. The simplex is realized using **all \(n\) Laplacian columns in \(\mathbf1^\perp\)**, rather than a coordinate-deletion lattice model, because the latter is generally not Euclidean-isometric. An enclosing ball contains every point of the convex simplex, equivalently every vertex. Its minimal radius must not be confused with the possibly larger radius of a sphere through every vertex. The earlier two-part case is prior work and is excluded from the new claim.

## Proof
**1. Uniqueness and symmetry.** Since \(G\) is connected, \(L\) has rank \(n-1\), and its \(n\) columns form an \((n-1)\)-simplex in \(\mathbf1^\perp\). For any finite vertex set, \(y\mapsto\max_v\|Le_v-y\|^2\) is strictly convex: subtract \(\|y\|^2\) to obtain a maximum of affine functions. Thus the minimizing center is unique. Orthogonal projection puts it in \(\mathbf1^\perp\), and within-class permutation symmetries force its coordinates to be constant on each class. We will independently construct its exact center and certify uniqueness below.

**2. Existence of the threshold.** The function \(F(s)=\sum_i a_i(T_i-s)_+\) is continuous, strictly decreasing whenever positive, diverges as \(s\to-\infty\), and vanishes for \(s\ge\max_iT_i\). Hence \(F(m)=2n^2>0\) has exactly one real solution. By its definition,
\[
\sum_i a_i t_i=\frac{F(m)}{2n}-n=0.
\]
Consequently \(c\in\mathbf1^\perp\). Its associated nonnegative weights \(w_v=(1+t_i)/n\) for \(v\in A_i\) satisfy \(\sum_vw_v=1\).

**3. The exact distance identity.** For \(v\in A_i\), the graph degree is \(d_i=n-a_i\). The \(v\)-th Laplacian column has squared norm \(d_i^2+d_i=b_i\). Because \(c\) is class-constant with coordinate sum zero,
\[
\langle Le_v,c\rangle=d_it_i-\sum_{u\notin A_i}c_u=nt_i.
\]
It follows that
\[
\|Le_v-c\|^2=\|c\|^2+b_i-2nt_i
=\begin{cases}\|c\|^2+m,&T_i\ge m,\\
\|c\|^2+T_i,&T_i<m.
\end{cases}
\]
The equality case \(T_i=m\) is included in the first branch. Thus the proposed ball contains every vertex, and the formula for \(R^2\), the contacts, and the exact clearances follow.

**4. Global minimality and the unique certificate.** Let \(w\in\mathbb R^n\) have the displayed per-vertex weights. It is a probability vector, constant on the classes. For \(v\in A_i\), using the complete multipartite Laplacian,
\[
(Lw)_v=(n-a_i)w_v-\sum_{u\notin A_i}w_u=nw_v-1=t_i.
\]
Thus \(c=Lw=\sum_vw_vLe_v\) is a convex combination of vertices, and every vertex receiving positive weight satisfies \(\|Le_v-c\|^2=R^2\). For any competing center \(y\), the variance identity yields
\[
\sum_vw_v\|Le_v-y\|^2
=\sum_vw_v\|Le_v-c\|^2+\|y-c\|^2
=R^2+\|y-c\|^2.
\]
Therefore \(\max_v\|Le_v-y\|^2\ge R^2+\|y-c\|^2\), proving the optimal ball and unique center. As the Laplacian columns are affinely independent, the representation of \(c\) by weights summing to one is unique; hence the certificate weights are uniquely specified, including zero weights for touching critical classes.

**5. Explicit sorted computation and all-contact criterion.** Because \(a_i\mapsto(n-a_i)(n-a_i+1)+2n\) is decreasing, positive terms in \(F(m)\) correspond to the smallest \(k\) class sizes. On that active prefix, \(\sum_{i=1}^k a_i(T_i-m)=2n^2\) gives the stated rational \(m_k\); the inequalities \(T_k>m_k\ge T_{k+1}\) are necessary and sufficient. If all classes touch, the untruncated sum at \(m=\overline b\) equals \(2n^2\), so this is possible precisely when \(\overline b\le\min_i T_i\). Strict inequality makes every certificate weight positive. The exhibited triples follow by direct rational substitution; in particular \((3,3,6)\) has \(m=66\), center values \((1,1,-1)\), and \(R^2=78\), while its third class has zero weight despite touching.

## Verification
Run `python check_multipartite_laplacian.py` using Python 3 and its standard library. It constructs the complete multipartite Laplacian matrices in full coordinates and verifies with exact fractions: the scalar threshold, zero-sum center, barycentric convexity certificate, every vertex-to-center squared distance, all contact and clearance conditions, and strict optimality witness. It passed 272 completely enumerated small class-size profiles, 50 seeded additional profiles, and four explicit phase examples; it encountered the intended critical-contact equality. Separately, unrestricted ambient-center SLSQP numerical optimizations on the five profiles \((2,3,5)\), \((3,3,6)\), \((4,17,17)\), \((2,8,28)\), and \((12,13,13)\) converged to the analytic radii and centers within numerical tolerances. These finite checks do **not** replace the proof for arbitrary part sizes.

## Relationship to prior work
Braun and Meyer introduced Laplacian simplices and investigated their lattice/Ehrhart properties, including trees, cycles and complete graphs [1]. Meyer and Pllaha studied coding-theoretic properties [2]; their relevant sections do not state Euclidean minimum enclosing balls. The published complete-bipartite Laplacian-simplex result [3] exactly treats **two parts**, with a one-dimensional optimization and one screening transition. It is credited and not claimed anew here. Its two-class formulas do not determine the sorted active prefixes, rational multi-class contact strata, and critical zero-weight contacts when \(r\ge3\). Another published threshold result [4] concerns **stable-set indicator polytopes**, which have different vertex sets and Euclidean distances; a resemblance between scalar threshold methods does not give an implication between their metric claims. Targeted literature searches did not identify a full multipartite Laplacian enclosing-sphere classification.

## Limitations
No claim is made for noncomplete graphs, weighted graph Laplacians, arbitrary affine or unimodular embeddings, or minimum-volume ellipsoids. A finite checker cannot establish the theorem for unbounded class sizes. The research comparison is a best-knowledge historical assessment, not a guarantee that no alternative earlier formulation exists. Independent mathematical verification remains outstanding.

## References
1. B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085v1 (first public 2017-06-21), Sections 3 and 6.
2. M. Meyer and T. Pllaha, *Laplacian Simplices II: A Coding Theoretic Approach*, arXiv:1809.02960v1 (2018-09-09), Sections 1 and 3.
3. *Sharp vertex-contact transition for complete-bipartite Laplacian simplices*, published research record, identifier `ac6d13296de7`, [public full result](https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-vertex-contact-transition-for-complete-bipartite-laplacian--ac6d13296de7/RESULT.md).
4. *Large-part screening in minimum spheres of complete multipartite stable-set polytopes*, published research record, identifier `2a7050b5d350`, [public full result](https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-large-part-screening-in-minimum-spheres-of-complete-multipartite--2a7050b5d350/RESULT.md).
