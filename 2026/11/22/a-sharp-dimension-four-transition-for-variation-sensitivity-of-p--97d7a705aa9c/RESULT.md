# A sharp dimension-four transition for variation sensitivity of path-TV-ball projection

## Finding
For each integer \(n\ge2\) and each radius \(\tau>0\), let \(P_{n,\tau}\) be Euclidean nearest-point projection in real \(\mathbb R^n\) onto the closed convex total-variation ball
\[
\mathcal B_{n,\tau}=\left\{z\in\mathbb R^n:\ V_n(z)=\sum_{i=1}^{n-1}|z_{i+1}-z_i|\le\tau\right\}.
\]
Its exact two-input Lipschitz modulus in the *same* variation seminorm is
\[
\boxed{\sup_{V_n(x-y)>0}\frac{V_n(P_{n,\tau}x-P_{n,\tau}y)}{V_n(x-y)}
=\begin{cases}1,&n=2,3,\\2,&n\ge4.\end{cases}}
\]
Every constant is attained by two distinct real input vectors, for every positive radius. Projection decreases the variation of each individual input, but for four or more sites it may *double the variation of a perturbation*. The sharp coefficient is independent of both resolution and radius.

## Assumptions and scope
Vectors are real; all observation masses are one; the edges form the open path with unit variation weights. The ball is unbounded in the constant-vector direction but is closed and convex, so its Euclidean projection is uniquely defined. Since the ball is invariant under adding constants, \(P_{n,\tau}(x+c\mathbf1)=P_{n,\tau}x+c\mathbf1\). Thus its induced map modulo constants is well-defined and the displayed seminorm ratio is meaningful. The radius is strictly positive; at radius zero the projection is the constant-sequence mean map and its variation modulus is zero.

## Proof
**1. Exact difference-coordinate problem.** Let \(m=n-1\), \(D:\mathbb R^n\to\mathbb R^m\) be the forward difference matrix, \((Dx)_j=x_{j+1}-x_j\), and \(G=DD^T\). Then \(G\) is the Dirichlet tridiagonal matrix with diagonal \(2\) and adjacent entries \(-1\); it is invertible. Write \(H=G^{-1}\), with entries indexed by \(1\le j,k\le m\),
\[
H_{jk}=\frac{\min(j,k)[m+1-\max(j,k)]}{m+1}.
\]
For any input \(x\), the projection retains its mean. Among pairs of vectors with the same mean, the squared Euclidean distance of a pair having difference coordinates \(y=Dx\) and \(z\) is \((z-y)^T H(z-y)\). Consequently the output difference vector \(z=D(P_{n,\tau}x)\) is precisely the unique minimizer of
\[
\frac12(z-y)^T H(z-y)\quad\text{subject to }\sum_{j=1}^m|z_j|\le\tau.
\]
The desired variation modulus is therefore the global \(\ell_1\)-Lipschitz modulus of this metric projection.

**2. Affine pieces, with every face realizable.** The objective is strictly convex and the constraint is a polytope, so its projection is continuous and piecewise affine. On the open face region whose nonzero output coordinates form a nonempty set \(J=\{j_1<\cdots<j_r\}\) with signs \(s=(s_1,\dots,s_r)\in\{-1,1\}^r\), the active constraint reads \(s^Tz_J=\tau\), while \(z_{J^c}=0\). Put \(B=(H_{JJ})^{-1}\), \(U=B H_{J,*}\), and \(v=Bs\). Differentiating the Lagrange-multiplier formula yields the edge-coordinate Jacobian
\[
T_{J,s}=E_J\left(U-\frac{v(s^TU)}{s^Tv}\right),
\]
where \(E_J\) inserts coordinates at \(J\) and zeros elsewhere. In the interior of the variation ball the Jacobian is the identity. All these Jacobians arise on full-dimensional input cells: choose any \(z\) in the relative interior of the specified face and put \(y=z+\lambda G a\), where \(\lambda>0\), \(a_J=s\), and \(a_{J^c}=0\). Its KKT certificate has strict off-support subgradient inequalities and nonzero on-support coordinates. Hence sufficiently small changes of \(y\) remain on that face.

**3. An exact positive-interpolation lemma.** The matrix \(B\) is a tridiagonal Dirichlet path Laplacian on the selected nodes. Put \(j_0=0\), \(j_{r+1}=m+1\), and \(c_a=1/(j_{a+1}-j_a)\) for \(0\le a\le r\). Then
\[
B_{aa}=c_{a-1}+c_a,\qquad B_{a,a+1}=B_{a+1,a}=-c_a,
\]
with all other entries zero (the displayed indices of \(B\) run from \(1\) to \(r\)). This follows either from the explicit Green kernel in Step 1 or from Schur complementation of a one-dimensional Dirichlet Laplacian. For each canonical input edge vector \(e_k\), the column \(Ue_k\) is a nonnegative, at-most-two-point linear interpolation vector: it is \(e_a\) when \(k=j_a\); between \(j_a\) and \(j_{a+1}\) its two nonzero coordinates are \((j_{a+1}-k)/(j_{a+1}-j_a)\) and \((k-j_a)/(j_{a+1}-j_a)\); to the left of \(j_1\) it has only entry \(k/j_1\); to the right of \(j_r\) it has only entry \((m+1-k)/(m+1-j_r)\). Indeed these weights reproduce every value \(H_{j,k}\) for \(j\in J\) by linearity of the Green kernel between selected nodes. In particular,
\[
Ue_k\ge0,\qquad\|Ue_k\|_1\le1\qquad(1\le k\le m).
\]

**4. A sign-alignment lemma and the universal factor two.** Since \(s_a\in\{-1,1\}\), the displayed tridiagonal formula implies
\[
s_a(Bs)_a=c_{a-1}(1-s_{a-1}s_a)+c_a(1-s_{a+1}s_a)\ge0,
\]
where for this expression only, \(s_0=s_{r+1}=0\). Thus each coordinate of \(v=Bs\) has the sign of the corresponding \(s_a\), or is zero, and
\[
\|v\|_1=s^Tv>0.
\]
Every Jacobian column therefore obeys
\[
\begin{aligned}
\|T_{J,s}e_k\|_1
&\le\|Ue_k\|_1+\frac{\|v\|_1}{s^Tv}|s^TUe_k|\\
&\le2\|Ue_k\|_1\le2.
\end{aligned}
\]
This proves the upper bound two for all dimensions. Since there are finitely many affine pieces, applying this inequality along a generic segment and then using continuity for exceptional segments establishes the *global*, not merely local, estimate.

**5. The small dimensions.** If \(m=1\), the induced difference map is scalar clipping, of Lipschitz norm one. If \(m=2\), singleton active supports have zero Jacobian; for full support the two possible sign patterns, modulo simultaneous sign reversal, give exactly
\[
\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]
both of induced \(\ell_1\)-operator norm one. The interior identity also has norm one. Thus \(n=2,3\) have sharp constant one.

**6. Attainment from four sites onward.** If \(m\ge3\), use the full active set \(J=\{1,\ldots,m\}\) and all-positive signs. Then \(U=I\), \(v=G\mathbf1=e_1+e_m\), \(s^Tv=2\), and
\[
T_{J,s}=I-\tfrac12(e_1+e_m)\mathbf1^T.
\]
For every interior index \(2\le k\le m-1\), \(\|T_{J,s}e_k\|_1=2\). This norm is realized by actual data pairs. For radius \(\tau=m\) take input difference vector \(y=(2,1,\ldots,1,2)\) and \(y'=y+\varepsilon e_k\), with \(0<\varepsilon<1\). Their projected difference vectors are \(z=\mathbf1\) and \(z'=\mathbf1+\varepsilon[e_k-(e_1+e_m)/2]\). Both have positive coordinates, sum \(m\), and satisfy their KKT equations with strictly positive multipliers; therefore they are the unique projections. Their input \(\ell_1\) distance is \(\varepsilon\) and output distance is \(2\varepsilon\). Lifting these edge differences back to real input vectors proves attainment for \(n\ge4\). Scaling the entire pair by \(\tau/m\) gives a witness for every \(\tau>0\). Interior points show the sharp norm one in the small dimensions. This concludes the proof.

## Verification
The standalone, standard-library-only `tv_ball_exact_check.py` evaluates all \(3^{n-1}-1\) signed active-support patterns through \(n=8\), checking Green matrix inversions, barycentric columns, signed Laplacian identities, exact rational Jacobian column norms, and the claimed sharp values. It independently checks explicit primal KKT attaining pairs for every \(4\le n\le100\). Execute `python3 tv_ball_exact_check.py` alongside this document. Exact finite verification supplements, but does not replace, the all-dimensional proof above.

## Relationship to prior work
Fadili and Peyré [1] study Euclidean projection onto total-variation balls and algorithms to compute it, including dual optimization and convergence rates. Their publicly accessible abstract covers the same constrained projection object; the complete original text could not be inspected, so any further historical coincidence is an explicit priority risk rather than an asserted negative. Fadili et al. [2] analyze regularized recovery with decomposable priors (including total variation), deriving conditional uniqueness and noise-stability results in Euclidean reconstruction norms. The openly accessible full HTML text of their main theorems addresses a penalized inverse problem, rather than the uniform, two-input sharp variation-seminorm modulus of the fixed-radius Euclidean projection considered here.

Published exact stability results for metric projection onto weighted cross-polytopes in \(\ell_p\) spaces [3] concern *diagonal coordinate* \(\ell_p\) metrics. They do not directly cover this Green-matrix quadratic metric, which is nondiagonal for all dimensions above two. Published sharp variation sensitivity of Euclidean simplex projection [4] concerns a different constraint polytope and either cyclic or open-path first differences; it does not imply the bound for a variation ball. Here the essential new mathematical content is the positive Green-kernel interpolation and active-sign alignment on the path, which together force the all-dimensional factor two and identify the first expansive dimension.

## Limitations
Only real, equally weighted finite open paths, positive radii, and Euclidean data fidelity are covered. Neither weighted vertex masses and edge penalties nor cycles, branching graphs, or infinite paths are addressed. The complete full text of the closest archival paper [1] was not available for comparison, so priority is not conclusively established. The analytic proof does not depend on numerical enumeration or the availability of that source.

## References
1. J. Fadili and G. Peyré, *Total Variation Projection With First Order Schemes*, IEEE Transactions on Image Processing 20 (2011), 657–669; public online article date 2010-09-27 per PubMed 20876024. DOI: https://doi.org/10.1109/TIP.2010.2072512. An earlier conference/preprint version is recorded from 2009 with no independently verified day-level public date here.
2. M. J. Fadili, G. Peyré, S. Vaiter, C. Deledalle, and J. Salmon, *Stable Recovery with Analysis Decomposable Priors*, first posted 2013-04-16, https://arxiv.org/abs/1304.4407.
3. *Exact Lipschitz Stability and Contractivity Threshold for Weighted Cross-Polytope Projections*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-lipschitz-stability-and-contractivity-threshold-for-weight--c92b6dad1bd0.
4. *Sharp Cyclic-Variation Amplification of Euclidean Simplex Projection*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-cyclic-variation-amplification-of-euclidean-simplex-projec--95284892279a.
