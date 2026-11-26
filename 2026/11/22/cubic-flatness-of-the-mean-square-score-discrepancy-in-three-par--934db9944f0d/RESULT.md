# Cubic flatness of the mean-square score discrepancy in three-party Frege dynamics

## Finding

Let \(p,q,r=1-p-q\) be the positive vote shares for the three-party Frege election rule, and suppose \(1,p,q\) are rationally independent. Write \(z(n)\) for the zero-sum score discrepancy in the normalization of Conze–Janson–Öberg [1]. The limiting average
\[
E(p,q)=\lim_{N\to\infty}N^{-1}\sum_{n=1}^N\|z(n)\|_2^2
\]
exists and is at least \(5/18\). In the open first Farey stability triangle \(S_{1/2}\) with vertices \((1/3,1/3),(1/2,0),(1/6,1/6)\), in the ordering \(0<q<p<r\), it is exactly
\[
\boxed{E(p,q)=\frac5{18}+\frac{(p-q)^2(3-4p-5q)}9.}
\]
The excess is positive in the interior and vanishes quadratically when approaching an interior point of the edge \(p=q\). At the equal-share vertex it is exactly homogeneous of degree three in the two share displacements: it has cubic order along each fixed inward ray in the open cell, and can vanish faster on paths that become tangent to the flat edge. The floor \(5/18\) is the sharp infimum over rationally independent vote shares. No equidistribution for boundary orbits is asserted.

## Assumptions and scope

The zero-sum score plane and the planar coordinates of [1, Eq. (11.5)] are related by
\[
z=(x+1/3-p,\ y+1/3-q,\ -x-y+1/3-r).
\]
The area measure is \(dx\,dy=dz_1\,dz_2\), not Euclidean surface area (which is \(\sqrt3\) times as large). By [1, Theorems 7.5 and 7.7], the orbit distributes according to Lebesgue measure on the compact area-one invariant set, which is a fundamental section of the score plane modulo \(A_2=\{\ell\in\mathbb Z^3:\sum_i\ell_i=0\}\) up to null sets. The three-party region considered below is the eleven-vertex cell of [1, §11.3].

## Proof

**Universal floor.** In each lattice coset a representative of minimum Euclidean norm belongs to the Voronoi cell
\[
V=\{z:\sum_i z_i=0,\ \max_i z_i-\min_i z_i\le 1\}.
\]
Indeed, spread greater than one lets us subtract \(e_{i_{\max}}-e_{i_{\min}}\) and reduce the squared norm. If the spread is at most one, let \(m\) be the sum of the positive entries of a nonzero \(\ell\in A_2\), also the sum of the absolute values of its negative entries. Then \(2z\cdot\ell\ge-2m\) and \(\|\ell\|_2^2\ge2m\), yielding \(\|z+\ell\|_2^2\ge\|z\|_2^2\). The six vertices in the three-score plane are the permutations of \((2/3,-1/3,-1/3)\) **and their negatives**. On each of the six triangles from the origin to two adjacent vertices, the vertices other than the origin have squared norms \(2/3\) and mutual dot product \(1/3\). The triangle mean of the squared norm is therefore \((2/3+2/3+1/3)/6=5/18\). The cell has area one in the quotient normalization, since projection onto \((z_1,z_2)\) sends \(A_2\) to \(\mathbb Z^2\). On any measurable fundamental section, cosetwise minimization bounds the average below by the Voronoi average. This proves the lower bound for \(E\); the lattice minimization and second moment are classical [2].

**First-cell moment.** Put \(X=(p-1,q)\), \(Y=(p,q-1)\), \(Z=(p,q)\), and
\[
A=((p+2q)/3,(p+2q)/3),\quad B=(2(p-q-1)/3,-(p-q-1)/3),\quad C=((p-q+1)/3,-2(p-q+1)/3).
\]
By [1, Eq. (11.49), Theorem 11.6 and Corollary 11.7], the clockwise vertices of the polygon \(D\) are
\[
C+X,\ X,\ A+X,\ X+Z,\ B+Z,\ Z,\ C+Z,\ Y+Z,\ A+Y,\ Y,\ B+Y.
\]
Let \(G=\begin{pmatrix}2&1\\1&2\end{pmatrix}\), \(Q(u)=u^{\mathsf T}Gu\), and \(h=(1/3-p,1/3-q)\). The oriented origin wedge for a clockwise edge \(a,b\) has signed area \(-\det(a,b)/2\); its score-space vertices in the first two coordinates are \(v_0=h,v_1=a+h,v_2=b+h\). Integrating the barycentric coordinates gives mean
\[
\frac{\sum_{j=0}^2Q(v_j)+\sum_{0\le j<k\le2}v_j^{\mathsf T}Gv_k}{6}.
\]
The signed wedge sum (valid even for an origin outside the polygon) simplifies to
\[
\operatorname{area}(D)=1,\qquad
\int_D Q((x,y)+h)\,dx\,dy=\frac5{18}+\frac{(p-q)^2(3-4p-5q)}9.
\]
Here \(Q(u_1,u_2)=u_1^2+u_2^2+(u_1+u_2)^2\) is the three-score energy. The orbit stays in a bounded region, so equidistribution transfers this continuous moment to the orbit limit.

**Sharpness and order of vanishing.** The affine factor \(3-4p-5q\) has values \(0,1,3/2\) at the three vertices in the stated order. On \(p=q=t\) with \(1/6<t<1/3\), its limit is \(3-9t>0\), giving quadratic vanishing in \(p-q\). At \(p=1/3+\varepsilon u,q=1/3+\varepsilon v\) the excess is exactly \(\varepsilon^3(u-v)^2(-4u-5v)/9\). The cubic formula along any fixed ray entering the open cell thus has a positive cubic coefficient. Rationally independent shares are dense in the open cell, since the dependent ones lie on a countable union of affine lines. Approaching an interior point of the flat edge shows sharpness without evaluating any dependent-share time average.

## Verification

The supplied `check_frege_moment.py`, run with Python 3 and SymPy, symbolically evaluates the signed areas and the eleven quadratic wedge moments, checks the factorization, and checks rational specializations. The code verifies the finite algebra, not equidistribution or orbit behavior at any boundary. The universal floor uses the lattice section property and the analytic Voronoi comparison.

## Relationship to prior work and limitations

The invariant sets and their rationally independent orbit equidistribution, the polygon vertices, and the limiting hexagon on the equal-small-share edge are from [1]. The value of the normalized Voronoi second moment and its minimization over fundamental sections are classical [2]; the lower-bound comparison uses those existing ingredients. What the first-cell computation adds is the explicit factorized energy and its cubic degeneration at equal shares, not a new polygon or lattice theorem. The exact law is specific to the first cell, not an expression for other Farey cells or a uniform time-convergence rate. No absolute historical priority is asserted.

## References

1. J.-P. Conze, S. Janson and A. Öberg, *Frege's election method: discrepancy, invariant polygons and Farey geometry*, arXiv:2611.13996v1, https://arxiv.org/html/2611.13996v1, Theorems 7.5 and 7.7 and §11.3.
2. R. McKilliam, A. Subramanian, E. Viterbo and I. Clarkson, *On the error performance of the A_n lattices*, arXiv:1111.6334, https://arxiv.org/abs/1111.6334.
