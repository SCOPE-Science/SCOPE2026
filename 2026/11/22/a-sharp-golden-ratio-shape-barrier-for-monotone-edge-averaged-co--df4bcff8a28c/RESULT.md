# A sharp golden-ratio shape barrier for monotone edge-averaged convection–diffusion on parallelogram meshes

## Finding

For the incidence-based edge-averaged method (IBEAM) with complete-graph diagonal edge weights and bilinear/Wachspress nodal coordinates on affine parallelograms, **the exact geometric admissibility region** for a nonsingular \(M\)-matrix on a uniform three-by-three Dirichlet tiling is
\[
\frac12\leq\frac{\|u\|_2^2}{\|v\|_2^2}\leq2,
\qquad
|u\cdot v|\leq\frac{\|u\|_2^2+\|v\|_2^2}{3},
\]
where \(u,v\in\mathbb R^2\) are the nonparallel parallelogram side vectors. The criterion holds for **arbitrary positive edgewise diffusion factors and arbitrary real edgewise Péclet numbers** on every cell; in particular it is independent of the magnitude or direction of any constant convection field. Equality is permitted.

Every admissible element satisfies the **sharp Jacobian shape bound**
\[
\kappa_2([u\ v])\leq\frac{3+\sqrt5}{2},
\]
attained, for instance, by \(u=(\sqrt2,0)^\top\), \(v=(1/\sqrt2,1/\sqrt2)^\top\). The shape bound alone is not sufficient for admissibility: an orthogonal element of aspect ratio \(2\) violates the geometric criterion despite having Jacobian condition number \(2\). For rectangles the exact admissible aspect-ratio interval is \([1/\sqrt2,\sqrt2]\). For equal-length sides the exact allowed absolute cosine of the included angle is at most \(2/3\).

The classification is specifically of the **nonsingular \(M\)-matrix property** for the stated discretization and mesh. Outside this region the assembled stiffness is not a \(Z\)-matrix; this does **not**, by itself, prove that its inverse has a negative entry or that every computed solution oscillates.

## Assumptions and scope

Fix linearly independent \(u,v\in\mathbb R^2\), set \(J=[u\ v]\), and take the parallelogram \(K=\{su+tv:0\leq s,t\leq1\}\). On the reference square use the four nodal functions
\[
\widehat\lambda_1=(1-s)(1-t),\quad
\widehat\lambda_2=s(1-t),\quad
\widehat\lambda_3=(1-s)t,\quad
\widehat\lambda_4=st.
\]
Their affine pullbacks are also the Wachspress coordinates of \(K\). On all six unordered pairs of its vertices (including both complementary diagonals), assign the source-defined weights
\[
\omega_{ij}=-\int_K\nabla\lambda_i\cdot\nabla\lambda_j\,dx,
\qquad i<j.
\]

For an oriented pair \(e=(i,j)\) take an arbitrary real signed Péclet number \(p_{K,e}\) and an arbitrary positive edge diffusion factor \(\alpha_{K,e}>0\). For the constant-coefficient convection–diffusion model these specialize to \(p_{K,e}=\beta\cdot(x_j-x_i)/\alpha\) and \(\alpha_{K,e}=\alpha>0\). Define the Bernoulli function \(\mathcal B(p)=p/(e^p-1)\), with continuous value \(\mathcal B(0)=1\). The local IBEAM matrix is the sum, over all six pairs, of embedded two-by-two blocks
\[
\alpha_{K,e}\omega_{ij}
\begin{bmatrix}
\mathcal B(p_e)&-\mathcal B(-p_e)\\
-\mathcal B(p_e)&\mathcal B(-p_e)
\end{bmatrix}.
\]
The theorem allows the edge factors and Péclet labels to vary independently over cells; no global potential condition is needed for the algebraic claim. Tile the domain by translates of \(K\) in a three-by-three array and impose Dirichlet conditions at all outer-grid vertices; the four interior nodal unknowns define the reduced assembled matrix. The same statements hold for a larger rectangular array of such cells with at least three cells per direction, provided all boundary nodes are Dirichlet. Edgewise variation is allowed at the discrete matrix level, without claiming consistency for arbitrary prescribed edge data. The result does not concern other stabilizations, quadrature changes or nonaffine quadrilaterals.

## Proof

**Exact edge weights.** By the affine transformation rule for gradients and area, put
\[
H=|\det J|J^{-1}J^{-\mathsf T}
 =\frac1{|\det J|}
\begin{bmatrix}
\|v\|_2^2&-u\cdot v\\
-u\cdot v&\|u\|_2^2
\end{bmatrix}
 =\begin{bmatrix}a&c\\c&b\end{bmatrix}.
\]
Integrating the polynomial reference gradients gives all six weights exactly:
\[
\begin{aligned}
\omega_{12}=\omega_{34}&=\frac a3-\frac b6,\\
\omega_{13}=\omega_{24}&=\frac b3-\frac a6,\\
\omega_{14}&=\frac{a+b}{6}+\frac c2,\\
\omega_{23}&=\frac{a+b}{6}-\frac c2.
\end{aligned}
\]
Thus nonnegativity of every edge weight is equivalent to
\[
\frac12\le a/b\le2,\qquad |c|\le(a+b)/3,
\]
which is precisely the asserted pair of geometric inequalities after substitution of the entries of \(H\).

**Necessity on the full tiling.** The Bernoulli function is strictly positive on the real line. Each off-diagonal element of the local edge block is exactly a negative, strictly positive Bernoulli factor times \(\omega_{ij}\). If one weight is negative, the central cell of a three-by-three tiling has the corresponding vertex pair entirely interior. For the two complementary diagonals it is the unique cell containing that pair. For the four side edges every contributing cell has the same (negative) geometric weight. Consequently the corresponding assembled interior off-diagonal entry is strictly positive. The interior matrix is not a \(Z\)-matrix, hence cannot be a nonsingular \(M\)-matrix.

**Sufficiency, including equality.** If all six weights are nonnegative, each local edge block is a \(Z\)-matrix with zero column sums. Hence the full assembled matrix has nonpositive off-diagonals and zero column sums before boundary elimination. The subgraph of edges with strictly positive weights is connected within every cell: at most one of the two diagonal weights can vanish, and at most one of the two side-edge orientation families can vanish (indeed both side families cannot vanish simultaneously). In the endpoint combinations the remaining two parallel sides and one positive diagonal connect all four corners; in all other cases connectivity is immediate. The global positive-weight graph therefore connects each interior unknown to the boundary. Dirichlet elimination gives a weakly column-diagonally dominant \(Z\)-matrix whose interior graph components reach a strictly dominant boundary-adjacent column. Standard irreducible-diagonal-dominance arguments on these components establish a nonsingular \(M\)-matrix. This also proves the assertion at equality, where the source's strictly-positive-weight hypothesis alone is not sufficient.

**Sharp conditioning barrier.** Because \(H\) is positive definite and has eigenvalues reciprocal to those of \(J^{\mathsf T}J\) up to a common positive scalar,
\(\kappa_2(H)=\kappa_2(J)^2\). Put
\[
T=a+b,\qquad z=\frac{a-b}{T},\qquad q=\frac{2c}{T}.
\]
The geometric inequalities give \(|z|\le1/3\) and \(|q|\le2/3\). With \(\delta=\sqrt{z^2+q^2}\), the eigenvalues of \(H\) are \(T(1\pm\delta)/2\); hence
\[
\kappa_2(J)^2=\frac{1+\delta}{1-\delta}
\le\frac{1+\sqrt5/3}{1-\sqrt5/3}
=\left(\frac{3+\sqrt5}{2}\right)^2.
\]
Equality requires \(|a-b|/T=1/3\) and \(2|c|/T=2/3\), and is attained by the displayed vectors \(u,v\), whose Gram matrix is \(\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\). This completes the sharpness proof.

## Verification

The standalone `check.py` independently constructs the full four-by-four reference stiffness matrix by symbolic double integration, checks its row sums and the six explicit coefficients, and verifies an exact boundary-shape witness. With deterministic random seed it also tests 300 nonsingular parallelograms under varying convection and eight exact metric instances in three-by-three Dirichlet tilings. The script reported **2,233 checks passed**, including independently varied positive diffusion factors and real Péclet labels for all six element edges. Its finite checks are supplementary; the all-shape, all-drift statements follow from the exact proof above. Execute from this file's directory with `python check.py` (NumPy and SymPy required).

## Relationship to prior work

Adler, Hu, Lee and O'Keefe (2026) introduced the complete-graph IBEAM weight identity and proved nonsingular \(M\)-matrix behavior under **strictly positive** local weights and connectivity. That result supplies the operator under examination here; the present claim is the explicit **necessary-and-sufficient geometric classification** on affine parallelogram tilings, its zero-weight endpoint cases, and the sharp Jacobian-distortion extremum. The motivating paper's full text does not state this parallelogram shape characterization.

Cao, Chen and Lee (2024/2025) developed edge-averaged **virtual** elements and a monotone variant on Voronoi polygons with suitable Delaunay duals. Xu and Zikatanov (1999) developed classical edge-averaged finite elements on simplices. Li and Zhang (2023/2025) studied a **modified-quadrature** monotone \(Q_1\) scheme and its geometric admissibility conditions; they also discuss classical \(Q_1\) aspect-ratio obstructions. None of these identified results establishes the combined all-convection IBEAM complete-graph criterion together with the sharp golden-ratio condition-number barrier. General finite-element stiffness facts and their standard positive-edge implications are not claimed as new.

## Limitations

The theorem addresses a uniform affine parallelogram geometry with arbitrary positive edge factors and real edge Péclet labels. It does not give consistency or error estimates for arbitrary edge data, nor a classification for general quadrilateral meshes, higher-order bases or higher-dimensional polytopes. Its exactness concerns the nonsingular \(M\)-matrix property, not all possible forms of inverse positivity. A condition-number bound alone cannot characterize admissibility. The result supplies neither a convergence rate nor a discretization-error estimate. Equivalent explicit shape inequalities could occur in less easily indexed classical \(Q_1\) literature, even when not stated for IBEAM; this remains a publication-priority risk.

## References

1. J. H. Adler, X. Hu, S. Lee and E. O'Keefe, *An Incidence-Based Edge-Averaged Method for Convection-Diffusion Problems on Polytopal Meshes*, arXiv:2611.01175v1 (31 October 2026), https://arxiv.org/html/2611.01175v1.
2. S. Cao, L. Chen and S. Lee, *Edge-averaged virtual element methods for convection-diffusion and convection-dominated problems*, arXiv:2402.13347 (20 February 2024); *Journal of Scientific Computing* 104 (2025), https://arxiv.org/abs/2402.13347.
3. H. Li and X. Zhang, *A monotone Q1 finite element method for anisotropic elliptic equations*, arXiv:2310.16274 (2023); *Beijing Journal of Pure and Applied Mathematics* 2 (2025), 183–217, https://arxiv.org/abs/2310.16274.
4. J. Xu and L. T. Zikatanov, *A monotone finite element scheme for convection-diffusion equations*, *Mathematics of Computation* 68 (1999), 1429–1446, https://doi.org/10.1090/S0025-5718-99-01148-5.
