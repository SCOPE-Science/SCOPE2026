# Cubic flatness of the mean-square score discrepancy in three-party Frege dynamics

## Finding
For the three-party Frege election rule, the long-run **mean-square discrepancy** between accumulated scores and ideal proportional shares has a sharp universal floor, and an exact nonconstant cubic law on the first stability polygon. If the vote shares are \(p,q,r=1-p-q\) and \(1,p,q\) are rationally independent, write \(z(n)=(z_1(n),z_2(n),z_3(n))\), \(\sum_i z_i(n)=0\), for the score discrepancies in the normalization of Conze–Janson–Öberg. The limit \(E(p,q)=\lim_{N\to\infty}N^{-1}\sum_{n=1}^N\|z(n)\|_2^2\) exists by the known invariant-polygon equidistribution theorem and satisfies
\[
 E(p,q)\ge\frac5{18}.
\]
In the open first Farey stability triangle \(S\) with vertices \((1/3,1/3),(1/2,0),(1/6,1/6)\), on the chamber \(0<q<p<1-p-q\), it has the exact formula
\[
 \boxed{E(p,q)=\frac5{18}+\frac{(p-q)^2(3-4p-5q)}9.}
\]
The correction is strictly positive in the interior, vanishes quadratically when approaching the equal-small-share edge \(p=q\) away from its endpoints, and is of cubic order on approaching the equal-share vertex. Consequently the universal lower bound is a sharp **infimum** over rationally independent admissible vote shares. No orbital equidistribution assertion is made at rationally dependent boundary shares.

## Assumptions and scope
The dynamics, score normalization and invariant polygon are those of Conze–Janson–Öberg [1]. Its zero-sum three-score coordinates \(z\) are related to the planar polygon coordinates \((x,y)\) by
\[
 z=(x+1/3-p,\;y+1/3-q,\;-x-y+1/3-r).
\]
We use area \(dx\,dy=dz_1\,dz_2\), not Euclidean surface area on the tilted score plane. The source's theorems establish that for rationally independent \(1,p,q\) the orbit empirical law converges to unit area on the invariant polygon and that its projection modulo the root lattice \(A_2=\{\ell\in\mathbb Z^3:\sum_i\ell_i=0\}\) is a fundamental-domain section, up to null boundaries. This finding concerns quadratic score energy, **not** the source's previously known area, the polygon itself or its ergodicity theorem. In the first cell the polygon has eleven listed vertices, with collinear coincidences allowed only on the boundary, as supplied in [1, Section 11.3].

## Proof
**(1) Universal energy floor.** Let \(H=\{z\in\mathbb R^3:\sum z_i=0\}\). Every area-one measurable fundamental section \(D\subset H\) of the root lattice has mean square energy at least the Voronoi-cell energy: write the integral over any fixed quotient fundamental domain and choose the minimal-norm representative in each lattice coset. The Voronoi cell is
\[
 V=\{z\in H:\max_i z_i-\min_i z_i\le1\}.
\]
Indeed, if the spread exceeds one, subtracting the root \(e_{i_{\max}}-e_{i_{\min}}\) strictly decreases squared norm. Conversely for \(z\in V\), a nonzero lattice vector \(\ell\) with positive and negative total mass \(m\) satisfies \(2z\cdot\ell\ge-2m\) and \(\|\ell\|_2^2\ge2m\), so \(\|z+\ell\|_2^2\ge\|z\|_2^2\). Its six vertices in score coordinates \((z_1,z_2)\) are permutations of \((2/3,-1/3,-1/3)\); direct polygon integration gives area one and \(\int_V\|z\|_2^2\,dz_1dz_2=5/18\). The fundamental-section property in [1] then proves the bound. The lattice nearest-point argument is classical background [2].

**(2) Exact first-cell energy.** Put \(r=1-p-q\), \(X=(p-1,q)\), \(Y=(p,q-1)\), \(Z=(p,q)\), and
\[
 A=((p+2q)/3,(p+2q)/3),\quad B=(2(p-q-1)/3,-(p-q-1)/3),\quad C=((p-q+1)/3,-2(p-q+1)/3).
\]
The polygon \(D\) in [1, Eq. (11.49)] has clockwise vertices
\[
 C+X,\ X,\ A+X,\ X+Z,\ B+Z,\ Z,\ C+Z,\ Y+Z,\ A+Y,\ Y,\ B+Y.
\]
For adjacent listed vertices \(a,b\), the signed origin-fan wedge has area \(-\det(a,b)/2\). Its score-space vertices are \(v_0=(1/3-p,1/3-q)\), \(v_1=a+v_0\), \(v_2=b+v_0\). Set \(Q(u,v)=2(u^2+uv+v^2)\), the squared norm of the zero-sum score vector. Its exact triangular mean is
\[
 \frac{Q(v_0)+Q(v_1)+Q(v_2)+\sum_{0\le j<k\le2}v_j^{\mathsf T}\begin{pmatrix}2&1\\1&2\end{pmatrix}v_k}{6}.
\]
Summing the eleven oriented wedge integrals and simplifying gives
\[
 \operatorname{area}(D)=1,\qquad \int_DQ(x+1/3-p,y+1/3-q)\,dx\,dy
 =\frac5{18}+\frac{(p-q)^2(3-4p-5q)}9.
\]
The fan formula remains valid even if the origin is outside the polygon, because wedges are signed. The exact symbolic expansion and rational checks are reproduced by the accompanying standalone Python script. By [1]'s equidistribution, the area moment equals \(E(p,q)\) for rationally independent votes.

**(3) Sharpness and cubic cancellation.** The open cell obeys \(3-4p-5q>0\), so its correction is positive whenever \(p>q\). Along the segment \(p=q=t\), \(1/6<t<1/3\), the invariant polygon's *area measure* becomes the translated Voronoi hexagon (including collinear extra vertices) and its energy is \(5/18\). Choose rationally independent \((p,q)\) in the open cell tending to \((t,t)\): their energies tend to \(5/18\). At the equal-share corner \(p=1/3+\varepsilon u,q=1/3+\varepsilon v\), the correction is exactly \(\varepsilon^3(u-v)^2(-4u-5v)/9\) while remaining in the stability cell, giving cubic onset rather than a generic quadratic change.

## Verification
The accompanying `check_frege_moment.py` implements the source's exact 11-vertex polygon, symbolic oriented-area formula, quadratic triangle moment, the polynomial factorization, and rational boundary and interior substitutions. Execute `python check_frege_moment.py` with Python 3 and SymPy installed. Every asserted identity is symbolic or exact rational. The paper's equidistribution theorem and root-lattice Voronoi argument are mathematical premises, not conclusions proved by finite tests. The proof does not claim a uniform-in-parameter rate for convergence of finite election averages.

## Relationship to prior work
[1] proves the invariant polygon's structure, its area-one torus section and convergence of orbit empirical distributions. Those are used without claiming them as new. [2] develops nearest-point and quantization theory for root lattices, which explains the universal comparison bound. The contribution here is the *explicit natural dynamical observable* \(E\) and its factorized three-share cubic correction, along with the sharp floor and its flat limiting family. The displayed cubic polynomial has not been located in the inspected source or compared records; this is not a proof of absolute historical priority.

## Limitations
The closed formula is specific to the first stability cell, not a whole-Farey-fan classification. The sharp floor applies to all rationally independent shares because of an existing fundamental-domain theorem; nonergodic boundary orbits need not share the normalized-area expectation. Different Frege score normalizations change the numerical constant. A general historical second-moment theorem for the exact same polygon, if found, could supersede the claimed contribution. No independent external mathematical audit has been performed.

## References
[1] J.-P. Conze, S. Janson, A. Öberg, *Frege's election method: discrepancy, invariant polygons and Farey geometry*, arXiv:2611.13996v1 (first public 2026-11-10), https://arxiv.org/html/2611.13996v1, especially Theorems 7.5 and 7.7 and Section 11.3.

[2] R. McKilliam, A. Subramanian, E. Viterbo, I. Clarkson, *On the error performance of the A_n lattices*, arXiv:1111.6334, https://arxiv.org/abs/1111.6334 (root-lattice quantization background).
