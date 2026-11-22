# Water-filling contact strata of complete multipartite Laplacian simplices

## Finding
Let \(r\ge3\) and let \(a_1,\ldots,a_r\) be arbitrary positive integers, with \(N=\sum_j a_j\). Let \(G=K_{a_1,\ldots,a_r}\) be the unweighted complete multipartite graph, \(L\) its ordinary graph Laplacian, and
\[
T_G=\operatorname{conv}\{Le_1,\ldots,Le_N\}\subset\mathbf 1^\perp\subset\mathbb R^N
\]
its canonical full-column Euclidean Laplacian simplex. Put
\[
b_j=(N-a_j)(N-a_j+1),\qquad (x)_+=\max\{x,0\}.
\]
There is a **unique** real number \(\tau\) satisfying the exact one-dimensional equation
\[
\boxed{\sum_{j=1}^r a_j(b_j-\tau)_+=2N^2.}\tag{1}
\]
Set \(t_j=(b_j-\tau)_+\) and \(S=\sum_j a_jt_j^2\). The **unique minimum enclosing Euclidean ball** of the entire simplex has center \(c\) and squared radius
\[
\boxed{c_v=\frac{t_j}{2N}-1\quad(v\in A_j),\qquad R^2=N+\tau+\frac{S}{4N^2}.}\tag{2}
\]
Every vertex of class \(A_j\) has the same squared-distance clearance from its optimal sphere, exactly
\[
\boxed{R^2-\|Le_v-c\|^2=(\tau-b_j)_+\quad(v\in A_j).}\tag{3}
\]
Consequently the sphere contacts **exactly** the vertices of classes with \(b_j\ge\tau\); the unique nonnegative center-barycentric certificate assigns total weight
\[
\boxed{\lambda_j=\frac{a_j(b_j-\tau)_+}{2N^2}}\tag{4}
\]
to class \(A_j\), equally distributed among its vertices. A class with \(b_j=\tau\) touches the sphere but receives zero certificate weight. This distinction is genuine at integer parameters.

Sorting part sizes in ascending order sorts the \(b_j\) in descending order. Therefore the positive-weight classes are always an initial segment of the smallest parts, with no omissions, and the contact classes add at most one further block of equal-size parts. The equations use only integer arithmetic and a rational threshold: all optimal center coordinates, squared radii, and clearances are rational.

For \(K_{3,3,6}\), the threshold is \(\tau=42\), the center is \(+1\) on the two three-vertex classes and \(-1\) on the six-vertex class, and \(R^2=78\). **All twelve vertices touch**, but the six vertices of the largest class have zero certificate weight. For \(K_{4,17,17}\), \(\tau=468\), \(R^2=867\), and precisely the four vertices in the smallest class touch; each of the other thirty-four has squared clearance \(6\). These examples witness a boundary-contact stratum and complete screening, respectively.

An exact finite algorithm is obtained by sorting \(b_1\ge\cdots\ge b_r\) and testing
\[
\tau_k=\frac{\sum_{j\le k}a_jb_j-2N^2}{\sum_{j\le k}a_j}
\]
for the unique active prefix satisfying \(b_k>\tau_k\ge b_{k+1}\), with \(b_{r+1}=-\infty\) and equal-size blocks treated together; equivalently solve (1) by its monotone piecewise-linear graph.

## Assumptions and scope
The theorem applies to \(r\ge3\) nonempty vertex parts. The polytope is formed from the **original full columns** in \(\mathbb R^N\), with the inherited Euclidean metric on the zero-sum hyperplane. Deleting a coordinate and passing to an arbitrary unimodular lattice representative does **not** generally preserve Euclidean radii. Every graph here is connected, so its \(N\) Laplacian columns are affinely independent and form an \((N-1)\)-simplex. An enclosing ball must contain the whole solid simplex, equivalently its \(N\) vertices. No edge weights or alternate metric are considered.

## Proof
**1. Existence and rationality of the threshold.** For fixed positive integers \(a_j\), the function \(F(t)=\sum_j a_j(b_j-t)_+\) is continuous, tends to infinity as \(t\to-\infty\), vanishes for \(t\ge\max_j b_j\), and is strictly decreasing throughout the range where it is positive. Thus \(F(\tau)=2N^2\) has exactly one solution. On its nonempty positive set \(I=\{j:b_j>\tau\}\), it gives
\[
\tau=\frac{\sum_{j\in I}a_jb_j-2N^2}{\sum_{j\in I}a_j},
\]
so \(\tau\), the coefficients (2)–(4), and \(R^2\) are rational.

**2. Geometry of each vertex orbit.** If \(v\in A_j\), its Laplacian column \(y_v=Le_v\) equals \(N-a_j\) at \(v\), equals \(-1\) outside \(A_j\), and vanishes at other vertices of \(A_j\). It has \(\|y_v\|^2=b_j\), and its class average is
\[
m_j=\frac N{a_j}\mathbf1_{A_j}-\mathbf1.
\]
The class weights \(\lambda_j=a_jt_j/(2N^2)\) are nonnegative and sum to one by (1). Distributing \(\lambda_j\) uniformly inside each class gives a probability vector on all \(N\) vertices whose weighted mean is
\[
\sum_j\lambda_jm_j
=\sum_j\frac{t_j}{2N}\mathbf1_{A_j}-\mathbf1=c.
\]
In particular \(\sum_v c_v=0\), and
\[
\|c\|^2=\sum_j a_j\left(\frac{t_j}{2N}-1\right)^2=\frac S{4N^2}-N.
\]

**3. Every squared vertex distance.** Since \(c\) is class-constant and has coordinate sum zero, \(\langle y_v,c\rangle=Nc_v=t_j/2-N\). Therefore
\[
\begin{aligned}
\|y_v-c\|^2
&=b_j-2\langle y_v,c\rangle+\|c\|^2\\
&=N+b_j-t_j+\frac S{4N^2}\\
&=N+\min\{b_j,\tau\}+\frac S{4N^2}.
\end{aligned}
\]
This is at most \(R^2\) in (2), with equality if and only if \(b_j\ge\tau\), and its difference from \(R^2\) is (3). Hence the asserted ball contains every vertex and therefore the whole simplex.

**4. Exact global optimality and uniqueness.** By (4), every vertex given positive probability in the constructed barycentric certificate lies on the proposed sphere, and their weighted mean is \(c\). For any competing center \(z\) in the ambient Euclidean space, the variance identity yields
\[
\sum_v w_v\|y_v-z\|^2
=\sum_v w_v\|y_v-c\|^2+\|z-c\|^2
=R^2+\|z-c\|^2,
\]
where \(w_v=\lambda_j/a_j\) for \(v\in A_j\). Some simplex vertex is therefore at squared distance at least \(R^2+\|z-c\|^2\), so \(c\) is the **unique** optimum among even unrestricted ambient centers. Because \(L\) has rank \(N-1\) and kernel \(\langle\mathbf1\rangle\), its columns are affinely independent, making the barycentric representation of \(c\) unique. Thus (4), including its zero-weight boundary contacts, is the unique probability certificate representing \(c\).

**5. Ordering, equality strata, and examples.** For \(1\le a\le N-1\), the function \(a\mapsto(N-a)(N-a+1)\) is strictly decreasing. Thus the active classes are the smallest-size classes, and equality can occur only at an entire equal-size group. Direct substitution into (1) yields \(\tau=42\), \(R^2=78\) for \((3,3,6)\), and \(\tau=468\), \(R^2=867\) for \((4,17,17)\); (3) gives all stated contact multiplicities and clearances. This proves every assertion.

## Verification
The included standalone `check_multipartite_ball.py` reconstructs original full Laplacian columns from the graph, computes (1)–(4) in exact rational arithmetic, and checks the exact center, contact, clearance, and weighted-distance optimality identities on a broad finite grid. It also solves the minimum enclosing sphere as an **unrestricted ambient-dimensional numerical convex program** for selected instances, without enforcing partwise symmetry. The exact checker passed 646 profiles, found five profiles with zero-weight contacts, and passed 23 independent unrestricted numerical optimizations. The proof above covers all positive integer part sizes and all \(r\ge3\); no finite experiment is substituted for a proof.

## Relationship to prior work
Braun and Meyer introduced graph Laplacian simplices and studied their lattice structure, spanning-tree volume, reflexivity, integer decomposition and Ehrhart properties. Balletti, Hibi, Meyer and Tsuchiya extended the framework to directed graphs. Neither inspected full-text treatment states the Euclidean multipartite minimum-sphere formula or its contact and zero-weight boundary strata. A previously published result determines minimum enclosing spheres for **two-part complete-bipartite** Laplacian simplices and expressly leaves graphs with at least three parts outside its scope; the present arbitrary-part formula introduces a multi-threshold active-set law and genuine integer weak-contact strata. A vertex-transitive Laplacian-simplex result covers the equal-class regular case, in which the center is zero and all vertices contact, but does not imply the unequal-class screening. A superficially similar threshold formula for **complete multipartite stable-set polytopes** concerns a different set of vertices, dimension, and Euclidean geometry; its proof does not yield (1)–(4) for Laplacian columns. General minimum-sphere duality explains the supporting convex combination but not the evaluated graph-specific thresholds or complete contact classification.

## Limitations
The invariant depends on the canonical Euclidean embedding and is not an arbitrary unimodular-affine invariant. The theorem does not address weighted graphs, sparse multipartite graphs, non-Euclidean norms, or the smallest enclosing ellipsoid. Its rational phase rule is exact but need not collapse to a single simple expression without determining the active part-size prefix. Historical priority under alternate terminology remains provisional, and independent mathematical validation has not been performed.

## References
1. B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085v1 (first public 2017-06-21), *Advances in Applied Mathematics* 114 (2020), 101976.
2. G. Balletti, T. Hibi, M. Meyer and A. Tsuchiya, *Laplacian Simplices Associated to Digraphs*, arXiv:1710.00252v1 (first public 2017-09-30), *Arkiv för Matematik* 56 (2018), 243–264.
3. *Sharp vertex-contact transition for complete-bipartite Laplacian simplices*, published research record `ac6d13296de7`, 2026-11-08.
4. *Vertex-transitive Laplacian simplices have spectral inradii and degree-controlled circumradii*, published research record `841b23980b76`, 2026-10-11.
5. *Large-part screening in minimum spheres of complete multipartite stable-set polytopes*, published research record `2a7050b5d350`, 2026-10-11.
