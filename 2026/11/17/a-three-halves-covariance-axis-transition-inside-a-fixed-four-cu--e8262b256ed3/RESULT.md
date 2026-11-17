# A three-halves covariance-axis transition inside a fixed four-cube section type

## Finding

For each real parameter \(t\geq1\), consider the three-dimensional Euclidean polytope
\[
K_t=[-1,1]^4\cap\{x\in\mathbb R^4:x_1+x_2+t x_3+t x_4=0\}.
\]
Let \(X_t\) be uniformly distributed with respect to intrinsic three-dimensional Lebesgue volume on \(K_t\), and let \(C_t=\operatorname{Cov}(X_t)\), acting on its three-dimensional linear span with the metric inherited from \(\mathbb R^4\).

The three orthogonal, one-dimensional covariance eigenspaces are
\[
E_A=\operatorname{span}(1,-1,0,0),\qquad
E_B=\operatorname{span}(0,0,1,-1),\qquad
E_C=\operatorname{span}(-t,-t,1,1).
\]
Their eigenvalues, respectively, are
\[
\lambda_A(t)=\frac{5t-1}{5(3t-1)},\quad
\lambda_B(t)=\frac{10t^3-10t^2+5t-1}{5t^2(3t-1)},\quad
\lambda_C(t)=\frac{(t^2+1)(5t-3)}{5t^2(3t-1)}.
\]
At \(t=1\), all three equal \(2/5\). For every \(t>1\), the largest eigenvalue is strictly \(\lambda_B(t)\). The least eigenvalue is \(\lambda_A(t)\) when \(1<t<3/2\), is doubly degenerate with \(\lambda_A(3/2)=\lambda_C(3/2)=13/35\) at \(t=3/2\), and is \(\lambda_C(t)\) when \(t>3/2\). In particular, the least-variance eigendirection switches **at exactly \(t=3/2\)**, while the combinatorial type remains unchanged for all \(t>1\).

The intrinsic covariance condition number is therefore
\[
\kappa(C_t)=\begin{cases}
\dfrac{10t^3-10t^2+5t-1}{t^2(5t-1)},&1\leq t\leq3/2,\\[4pt]
\dfrac{10t^3-10t^2+5t-1}{(t^2+1)(5t-3)},&t\geq3/2.
\end{cases}
\]
The two formulas agree at the transition, giving \(\kappa(C_{3/2})=142/117\); furthermore, \(\kappa(C_1)=1\) and \(\lim_{t\to\infty}\kappa(C_t)=2\).

For comparison, the intrinsic volume of the same section is
\[
\operatorname{vol}_3(K_t)=\frac{8\sqrt{2(t^2+1)}(3t-1)}{3t^2}.
\]
Along this path of normal vectors, volume decreases strictly on \(1<t<2\) and increases strictly on \(t>2\). The known volume-critical direction \((1,1,2,2)\) and the covariance-axis crossing \((1,1,3/2,3/2)\) are thus different. Novelty is asserted only for the exact covariance spectrum, eigendirection change, and condition-number law, **not** for the previously studied volume-critical direction.

## Assumptions and scope

The cube has fixed side length \(2\), its center is the origin, and no rescaling of the ambient Euclidean metric is performed. The parameter range is every **real** \(t\geq1\), not merely rational or sampled values. The probability measure is intrinsic volume normalized to total mass one; it is not the uniform distribution on vertices, nor the uniform distribution in the ambient four-dimensional cube. The covariance has one additional zero eigenvalue when regarded as a four-by-four ambient matrix, in the direction \((1,1,t,t)\); the condition number concerns only the three positive eigenvalues in the section's span.

For \(t=1\), the section is an octahedron with six vertices and eight triangular facets. For every \(t>1\), it has eight vertices and eight facets: four quadrilateral facets and four triangular facets, independent of \(t\). Thus the transition at \(3/2\) is not induced by a face-lattice change.

## Proof

**1. Orthogonal parameters and volume normalization.** Introduce real coordinates \(a,b,B\) by
\[
x=(a-tB,-a-tB,B+b,B-b).
\]
The coordinate tangent vectors are \((1,-1,0,0)\), \((0,0,1,-1)\), and \((-t,-t,1,1)\), which are mutually orthogonal with squared Euclidean norms \(2,2,2(t^2+1)\). Therefore the intrinsic Euclidean volume element is precisely
\[
2\sqrt{2(t^2+1)}\,da\,db\,dB.
\]
The cube bounds are exactly
\[
|B|\leq1/t,\qquad |a|\leq1-t|B|,\qquad |b|\leq1-|B|.
\]
Writing \(u=t|B|\in[0,1]\), the normalized distribution of \(u\) has density proportional to \((1-u)(1-u/t)\), whose integral is
\[
I_0=\int_0^1(1-u)(1-u/t)\,du=\frac{3t-1}{6t}.
\]
Integrating the rectangle fibers, including both signs of \(B\), yields
\[
\operatorname{vol}_3(K_t)=\frac{16\sqrt{2(t^2+1)}}{t}I_0
=\frac{8\sqrt{2(t^2+1)}(3t-1)}{3t^2}.
\]

**2. Exact covariance moments.** The map \(x\mapsto-x\) preserves volume, so \(\mathbb E X_t=0\). Conditional on \(B\), the coordinates \(a\) and \(b\) are independent and uniform on the symmetric intervals above. Consequently their mixed second moments vanish, and their cross-moments with \(B\) vanish as well. Thus the three orthogonal tangent coordinate vectors are covariance eigenvectors.

The required elementary integrals are
\[
\begin{aligned}
I_A&=\int_0^1(1-u)^3(1-u/t)\,du=\frac{5t-1}{20t},\\
I_B&=\int_0^1(1-u)(1-u/t)^3\,du=\frac{10t^3-10t^2+5t-1}{20t^3},\\
I_2&=\int_0^1u^2(1-u)(1-u/t)\,du=\frac{5t-3}{60t}.
\end{aligned}
\]
Because a symmetric uniform interval of radius \(r\) has second moment \(r^2/3\), we obtain
\[
\begin{aligned}
\lambda_A&=2\mathbb E[a^2]=\frac{2I_A}{3I_0},\\
\lambda_B&=2\mathbb E[b^2]=\frac{2I_B}{3I_0},\\
\lambda_C&=2(t^2+1)\mathbb E[B^2]=\frac{2(t^2+1)I_2}{t^2I_0}.
\end{aligned}
\]
Substituting the three integrals gives exactly the displayed spectral formulas for **all** real \(t\geq1\).

**3. Exhaustive eigenvalue ordering.** Subtracting the explicit rational formulas gives
\[
\begin{aligned}
\lambda_B-\lambda_A&=\frac{(t-1)(5t^2-4t+1)}{5t^2(3t-1)},\\
\lambda_B-\lambda_C&=\frac{(t-1)(5t^2-2t-2)}{5t^2(3t-1)},\\
\lambda_C-\lambda_A&=\frac{(t-1)(3-2t)}{5t^2(3t-1)}.
\end{aligned}
\]
Both quadratic factors in the first two differences are positive for \(t\geq1\): the first is \(5(t-2/5)^2+1/5\), and the second is increasing for \(t\geq1\) and equals \(1\) at \(t=1\). Their common denominator is positive. This proves strict maximality of \(\lambda_B\) at \(t>1\), and the sign of the last difference proves the unique least-eigenvalue crossing at \(t=3/2\). Taking the appropriate positive-eigenvalue ratio proves the condition-number formula and its endpoint values.

**4. No combinatorial change at the crossing.** On any coordinate hyperplane \(x_1=\pm1\) or \(x_2=\pm1\), the remaining last-block coordinates form a square cut by a nondegenerate strip between two parallel lines, producing a quadrilateral for \(t>1\). On any coordinate hyperplane \(x_3=\pm1\) or \(x_4=\pm1\), the first two coordinates lie in a square cut through one diagonal, producing a triangle when \(t\geq1\); no inequality disappears for \(t>1\). All eight coordinate facets are nonredundant, giving four quadrilaterals and four triangles for every \(t>1\). Euler's formula then gives eight vertices. At \(t=1\) the quadrilaterals degenerate into triangles, yielding the six-vertex octahedron. Hence the crossing at \(3/2\) occurs strictly within one fixed face-lattice chamber.

**5. Comparison with the volume-critical parameter.** Direct differentiation of the volume identity yields
\[
\frac{d}{dt}\operatorname{vol}_3(K_t)=
\frac{8\sqrt2(t-1)(t-2)}{3t^3\sqrt{t^2+1}}.
\]
Its sign gives the stated restricted-path minimum at \(t=2\). That parameter is already documented in prior cube-section literature, and is used here only to distinguish the newly identified covariance transition from a familiar volume event.

## Verification

The independent file `artifacts/verify.py` reconstructs all vertices as exact rational intersections between the section plane and cube edges. For 15 rational parameter profiles spanning the octahedral endpoint, both sides of the covariance transition, the crossing itself, the volume-critical parameter, and the large-parameter regime, it triangulates the section boundary and integrates quadratic forms tetrahedron by tetrahedron using exact rational arithmetic. Hull triangulation uses floating-point arithmetic **only for combinatorial incidence**; all subsequent vertex arithmetic, determinants, and second moments are rational. It checks the exact three eigenvalues and section-volume normalization at each profile, and independently checks the integral reductions, spectral factorizations, and volume derivative symbolically with SymPy.

Run with `python artifacts/verify.py` in an environment with NumPy, SciPy, and SymPy. The observed output from the supplied standalone file is `FOUR_CUBE_PAIR_SECTION_CHECKS_PASSED profiles=15 vertices=118 tetrahedra=176`. This finite verification corroborates but is not a substitute for the continuous-parameter proof above.

## Relationship to prior work

The direct point of departure is G. Ambrus, *Critical central sections of the cube* (first publicly available 2021-07-30, arXiv:2107.14778), whose Theorem 3 isolates the volume-critical direction \((1,1,2,2)\) in dimension four. Our family contains that direction, but the new statistic is the **uniform-volume covariance tensor**, whose smallest eigenvector changes already at \(t=3/2\).

Ambrus and Gárgyán, *Non-diagonal critical central sections of the cube* (arXiv:2307.03792, first public 2023-07-07), analyze the central section **volume functional** and its normal-direction Hessian. That Hessian is not the covariance of the uniform-volume distribution inside a fixed section. Their explicit results do not give the above covariance spectrum.

Brandenburg, De Loera, and Meroni, *The Best Ways to Slice a Polytope* (arXiv:2304.14239, first public 2023-04-27), establish broad piecewise-rational **algorithms** for polynomial moments of polytope sections. These algorithms can in principle compute any of the moments considered here, so our claim is not a new general moment-integration method. The contribution is the fully evaluated spectral family and its exact, constant-face-type transition. Jevtić and Živaljević, *Bier spheres of extremal volume and generalized permutohedra* (arXiv:2108.00618, first public 2021-08-02), identify the equal-weight central section with a median hypersimplex by affine equivalence, which describes the \(t=1\) boundary but not the varying covariance.

## Limitations

The result is a complete classification only for the indicated one-parameter family of four-dimensional cube sections. It does not classify arbitrary normal vectors or arbitrary dimensions. The novelty assessment is a comparison with inspected literature and searches, **not** an assertion that historical priority has been independently established; an unlocated equivalent calculation remains possible. The volume stationarity of \((1,1,2,2)\), algorithms for general polynomial moments, and the median-hypersimplex identification are established prior facts rather than new contributions. Numerical hull triangulation is used only for reproducibility tests, not for the infinite proof. Independent mathematical audit has not been performed.

## References

1. G. Ambrus, *Critical central sections of the cube*, arXiv:2107.14778 (first posted 2021-07-30), https://arxiv.org/abs/2107.14778.
2. G. Ambrus and B. Gárgyán, *Non-diagonal critical central sections of the cube*, arXiv:2307.03792 (first posted 2023-07-07), https://arxiv.org/abs/2307.03792.
3. M.-C. Brandenburg, J. A. De Loera, and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239 (first posted 2023-04-27), https://arxiv.org/abs/2304.14239.
4. F. D. Jevtić and R. T. Živaljević, *Bier spheres of extremal volume and generalized permutohedra*, arXiv:2108.00618 (first posted 2021-08-02), https://arxiv.org/abs/2108.00618.
