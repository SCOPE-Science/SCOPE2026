# Sharp vertex-contact transition for complete-bipartite Laplacian simplices

## Finding
For integers \(2\le p\le q\), put \(N=p+q\), let \(L\) be the ordinary graph Laplacian of \(K_{p,q}\), and consider the intrinsic Euclidean simplex
\[
Q_{p,q}=\operatorname{conv}\{Le_1,\ldots,Le_N\}\subset\mathbf1^\perp\subset\mathbb R^N.
\]
Define
\[
a_0=\frac{q(q-p)(N+1)}{2N^2},\qquad a_* =\min\{a_0,q/p\},\qquad c_*=(a_*\mathbf1_p,-pa_*\mathbf1_q/q).
\]
Then \(c_*\) is the **unique** center of a minimum enclosing Euclidean ball, whose squared radius is
\[
\boxed{R^2(Q_{p,q})=\begin{cases}
\displaystyle\frac{pq(N+2)}N+\frac{pq(q-p)^2(N+1)^2}{4N^3},&p(q-p)(N+1)\le2N^2,\\[4pt]
\displaystyle\frac{q^2(p-1)}p,&p(q-p)(N+1)>2N^2.
\end{cases}}
\]
In the first regime **all \(N\) vertices** touch the unique minimum sphere. In the second regime **exactly the \(p\) vertices indexed by the smaller color class** touch; each of the other \(q\) vertices has strict squared-distance clearance
\[
\boxed{R^2-\|Le_j-c_*\|^2=\frac{p(q-p)(N+1)-2N^2}{p}\quad(j\text{ in the larger class}).}
\]
At equality all vertices touch. This is an exact, finite-parameter phase transition, not merely an asymptotic approximation.

In particular, \(K_{3,13}\) has all sixteen vertices on the optimal sphere, whereas \(K_{3,14}\) has only three of seventeen vertices in contact, and each of the other fourteen has squared clearance \(16/3\).

## Assumptions and scope
The graph is unweighted, simple, and complete bipartite; \(2\le p\le q\). The coordinates are the **full Laplacian columns** in \(\mathbb R^N\), with the Euclidean metric restricted to the zero-sum hyperplane. The commonly used deletion-of-one-coordinate lattice representation of a Laplacian simplex is not, in general, Euclidean-isometric and is **not** used here. A minimum enclosing ball refers to a ball containing the entire simplex, equivalently its vertices; the equidistant vertex circumsphere need not be the smallest enclosing sphere.

## Proof
**1. Full dimension and uniqueness.** The connected graph Laplacian has kernel \(\operatorname{span}\{\mathbf1\}\), so its \(N\) columns affinely span \(\mathbf1^\perp\) and are the vertices of an \((N-1)\)-simplex. The squared enclosing-radius objective \(\max_i\|Le_i-c\|^2\) is strictly convex in \(c\), since subtracting \(\|c\|^2\) leaves a maximum of affine functions; hence the minimum center is unique.

**2. Symmetry reduction.** Permutations within either color class preserve the vertex set and the Euclidean metric. Averaging an optimal center over these permutations, then using its uniqueness, forces it to be constant on each color class. Because the vertices lie in \(\mathbf1^\perp\), orthogonal projection puts the optimum in that hyperplane. Thus the center is
\[
c(a)=(a\mathbf1_p,-pa\mathbf1_q/q)
\]
for a unique real scalar \(a\).

**3. The two exact distance functions.** For a vertex \(Le_i\) with \(i\) in the \(p\)-class, its squared norm is \(q(q+1)\), whereas in the \(q\)-class it is \(p(p+1)\). Moreover \(\|c(a)\|^2=pNa^2/q\), and \(\langle c(a),Le_i\rangle=Na\) in the first class and \(-Npa/q\) in the second. Hence the only two squared vertex distances are
\[
D_A(a)=q(q+1)+\frac{pN}{q}a^2-2Na,\qquad
D_B(a)=p(p+1)+\frac{pN}{q}a^2+\frac{2Np}{q}a.
\]
Their difference is
\[
D_A(a)-D_B(a)=(q-p)(N+1)-\frac{2N^2}{q}a.
\]
They cross at \(a=a_0\ge0\). The first parabola has its unique minimum at \(a=q/p\), and the second at \(a=-1\). For \(a\le a_0\), the larger distance is \(D_A(a)\), and for \(a\ge a_0\) it is \(D_B(a)\). Since \(D_B\) is strictly increasing for \(a\ge a_0\), the global minimizer of \(\max\{D_A(a),D_B(a)\}\) is exactly \(a_*=\min\{a_0,q/p\}\).

**4. Radius and contacts.** In the all-contact case \(a_*=a_0\), both classes have equal distance. Since the average vertex is \(0\), averaging the squared distances gives
\[
R^2=\frac{p q(q+1)+q p(p+1)}N+\|c(a_0)\|^2
=\frac{pq(N+2)}N+\frac{pq(q-p)^2(N+1)^2}{4N^3}.
\]
In the screened case \(a_*=q/p\), the minimizing first-class distance is \(D_A(q/p)=q^2(p-1)/p\); the displayed difference of squared distances gives exactly the clearance claimed. When the inequality is an equality, both classes contact. This proves the theorem for every admissible pair.

**5. Independent optimality certificate.** In the all-contact regime, the optimal center is the convex combination of vertices with per-vertex weights
\[
\lambda_A=\frac{1+a_0}{N},\qquad\lambda_B=\frac{1-pa_0/q}{N}.
\]
These are nonnegative precisely under the stated threshold, and their weighted vertex mean is \(c(a_0)\). In the screened regime, \(c_*=p^{-1}\sum_{i\in A}Le_i\), the average of the \(p\) contacting vertices. For any ball center \(y\), a convex combination of squared distances to the contact vertices is \(R^2+\|y-c_*\|^2\), so no smaller enclosing ball exists. This independently certifies optimality and uniqueness without relying on a numerical solver.

## Verification
The accompanying `check_circumball.py` reconstructs the original Laplacian matrices and vertex clouds, checks exact contact and clearance formulas, verifies nonnegative barycentric optimality certificates, and compares the predicted radius with unrestricted numerical minimum-sphere optimizations in ambient coordinates for all tested cases of manageable dimension. It passed 138 pairs \((p,q)\) with \(2\le p\le7\), \(p\le q<\min\{30,p+23\}\), including 77 strict screening examples. The analytic proof above, not finite computation, proves the all-parameter theorem. Requires Python, NumPy, and SciPy.

## Relationship to prior work
Braun and Meyer introduced Laplacian simplices and investigated reflexivity, normalized lattice volume, and Ehrhart properties; Meyer and Pllaha investigated associated linear codes. Neither inspected paper gives the minimum enclosing Euclidean sphere or the two-class contact threshold. A published result on **vertex-transitive** Laplacian simplices gives a common circumsphere of radius \(\sqrt{k(k+1)}\); it supplies the balanced case \(p=q\) but does not imply a phase transition for unequal part sizes. A separate result on **tree** Laplacian simplices studies inradii and does not cover the present nontrivial bicliques (the boundary stars have \(p=1\)). General convex-hull minimum-sphere principles give the certificate mechanism but not the evaluated threshold or the class-specific classification. The new assertion concerns the **minimum sphere**; an all-vertex equidistant sphere exists even in the strict screening regime and is then not minimum.

## Limitations
The classification is for the full-column Euclidean embedding only. It is not invariant under arbitrary unimodular coordinate changes or edge reweighting, and it does not cover general noncomplete bipartite graphs or full multipartite graphs. Historical priority under alternative graph-simplex terminology remains provisional, and no independent proof audit has been performed.

## References
1. B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085, first public version 2017-06-21; *Advances in Applied Mathematics* 114 (2020), 101976.
2. M. Meyer and T. Pllaha, *Laplacian Simplices II: A Coding Theoretic Approach*, arXiv:1809.02960, first public version 2018-09-09.
3. M. Manjunath and B. Sturmfels, *The Laplacian lattice of a graph under a simplicial distance function*, *European Journal of Combinatorics* 34 (2013), 1051–1070. This concerns a non-Euclidean metric and a lattice, not the Euclidean enclosing ball here.
4. *Vertex-transitive Laplacian simplices have spectral inradii and degree-controlled circumradii*, published research record, identifier `841b23980b76` (2026).
5. *Tree Laplacian simplices exhibit sharp, lattice-invisible Euclidean inradius exponents*, published research record, identifier `e122ee1ddbbf` (2026).
