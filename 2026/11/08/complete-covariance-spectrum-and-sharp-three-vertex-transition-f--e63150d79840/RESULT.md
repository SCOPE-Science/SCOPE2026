# Complete covariance spectrum and sharp three-vertex transition for bipartite Lipschitz polytopes

## Finding
Let \(p,q\ge2\) be integers, \(n=p+q\), and let \(K_{p,q}\) be the complete bipartite graph with the indicated part sizes. Form its symmetric edge polytope
\[
P_{p,q}=\operatorname{conv}\{\pm(e_i-e_j):ij\in E(K_{p,q})\}\subset H,
\qquad H=\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\}.
\]
Write \(L_{p,q}=P_{p,q}^{\circ}\) for the **Euclidean polar inside \(H\)**, and sample \(X\) uniformly according to intrinsic \((n-1)\)-dimensional volume on \(L_{p,q}\). The covariance operator \(\operatorname{Cov}(X)\), acting on \(H\), has exactly the following eigenvalues:
\[
\lambda_P=\frac{(p+1)(p+2)}{3n(n+1)}\quad(\text{multiplicity }p-1),
\]
\[
\lambda_Q=\frac{(q+1)(q+2)}{3n(n+1)}\quad(\text{multiplicity }q-1),
\]
\[
\lambda_B=\frac{pq+2}{3n(n+1)}\quad(\text{multiplicity }1).
\]
The respective eigenspaces are contrasts inside the first block, contrasts inside the second block, and the one-dimensional between-block contrast. All eigenvalues are positive; the covariance in ambient \(\mathbb R^n\) additionally has the zero eigenvector \(\mathbf1\).

Assume henceforth \(2\le p\le q\). The largest eigenvalue is \(\lambda_Q\), with the additional first-block multiplicity when \(p=q\). The **smallest-eigenvalue mode switches at exactly \(q=p+3\)**: it is the between-block contrast for \(q<p+3\); it is the first-block contrasts for \(q>p+3\); and the two modes tie exactly at \(q=p+3\). The intrinsic covariance condition number is therefore
\[
\boxed{\kappa(L_{p,q})=
\begin{cases}
\dfrac{(q+1)(q+2)}{pq+2},&p\le q\le p+3,\\[4pt]
\dfrac{(q+1)(q+2)}{(p+1)(p+2)},&q\ge p+3.
\end{cases}}
\]
The two formulas agree at their common boundary. The balanced family satisfies \(\kappa(L_{p,p})=(p+1)(p+2)/(p^2+2)\to1\); for each fixed \(p\), the condition number grows quadratically in \(q\).

## Assumptions and scope
All graph edges have unit length and all polar inequalities are \(|x_i-x_j|\le1\). The polar is taken within the zero-sum Euclidean subspace, not the ambient space or the unit-cube polar. The sampling measure is normalized intrinsic Lebesgue measure, **not** uniform over vertices or lattice points. The claim covers all integer pairs \(p,q\ge2\); swapping blocks exchanges the first two eigenvalue classes. The exact volume identity used for normalization is ancillary and is not asserted to be a new result.

## Proof
**1. Parametrization of uniform volume.** A point in \(L_{p,q}\) is precisely a potential vector satisfying \(\sum_i x_i=0\) and \(|x_i-x_j|\le1\) for every cross-block pair. Choose the gauge in which the final second-block coordinate is zero. Let \(u_1,\ldots,u_p\) and \(v_1,\ldots,v_{q-1},0\) denote the gauge-fixed coordinates. The gauge-to-zero-sum map subtracts the global mean; its Jacobian is constant, so uniform gauge-fixed volume pushes forward to uniform intrinsic volume.

Set \(m=\min_i u_i\), \(M=\max_i u_i\), \(z=(M-m)/2\), \(c=(M+m)/2\), and \(h=1-z\). Away from a null set, \(0<z<1\), \(-h<c<h\), two of the \(u_i\)'s are \(c-z\) and \(c+z\), the remaining \(p-2\) are independently uniform on their interval, and the \(q-1\) non-root \(v_j\)'s are independently uniform on \([c-h,c+h]\). Indeed all cross-block inequalities are equivalent to membership of each \(v_j\) (including zero) in that intersection interval. The minimum–maximum change of variables gives marginal density proportional to \(z^{p-2}(1-z)^q\). Consequently,
\[
z\sim\operatorname{Beta}(p-1,q+1),\qquad
c\mid z\sim\operatorname{Unif}[-h,h].
\]
The locations of the minimum and maximum are distinct and uniformly randomized. This also holds when \(p=2\) with no interior \(u_i\)'s. Thus
\[
\mathbb E z^2=\frac{p(p-1)}{n(n+1)},\qquad
\mathbb E h^2=\frac{(q+1)(q+2)}{n(n+1)}.
\]

**2. Orthogonal decomposition.** The symmetry under permutations within each block makes the covariance scalar on the two contrast spaces. Their dimensions are \(p-1\) and \(q-1\), while the complementary subspace within \(H\) is the one-dimensional between-block contrast. This decomposition exhausts \(n-1\) dimensions. The distribution is centrally symmetric, hence \(\mathbb E X=0\).

**3. Within-block eigenvalues.** For any two distinct first-block positions, the squared difference equals \(2\lambda_P\) in expectation. Conditional on \(z\), standardize the \(u_i\)'s to \(-1,+1\) and \(p-2\) independent uniforms on \([-1,1]\). The expected sum of squared pair differences is \((p+1)(p+2)/3\) in these units, hence
\[
\mathbb E (u_i-u_j)^2=\frac{2(p+1)(p+2)}{3p(p-1)}\mathbb E z^2,
\]
which yields the claimed \(\lambda_P\). For the second block, \(v_j=c+h S_j\) with \(S_j\) uniform on \([-1,1]\), and \(\mathbb E(v_j-0)^2=2\mathbb E h^2/3\). Symmetry of all second-block labels gives \(2\lambda_Q=2\mathbb E h^2/3\), yielding the claimed \(\lambda_Q\).

**4. Between-block eigenvalue.** Let \(\bar u\) and \(\bar v\) be the two block averages of gauge-fixed potentials. Using independent centered uniforms \(T_i,S_j\) on \([-1,1]\),
\[
\bar u-\bar v=\frac cq+\frac zp\sum_{i=1}^{p-2}T_i-\frac hq\sum_{j=1}^{q-1}S_j.
\]
Because \(\operatorname{Var}(c\mid z)=h^2/3\), the conditional variance of this contrast is \(h^2/(3q)+z^2(p-2)/(3p^2)\). The unit vector constant on the first and second blocks with opposite signs has squared projection \((pq/n)(\bar u-\bar v)^2\). Therefore
\[
\lambda_B=\frac{pq}{3n}\left(\frac{\mathbb E h^2}{q}+\frac{p-2}{p^2}\mathbb E z^2\right)=\frac{pq+2}{3n(n+1)}.
\]

**5. Extremal ordering.** When \(p\le q\), direct subtraction gives
\[
\lambda_Q-\lambda_B=\frac{q(q-p+3)}{3n(n+1)}>0,\qquad
\lambda_B-\lambda_P=\frac{p(q-p-3)}{3n(n+1)}.
\]
Also \(\lambda_Q\ge\lambda_P\). These three identities prove the exact minimum-mode transition, equality boundary, maximum mode, and condition number. No numerical or asymptotic argument is required.

**6. Volume normalization.** As a check rather than a separate new claim, integration in the same gauge gives coordinate volume
\[
\operatorname{Vol}_{\mathrm{root}}(L_{p,q})=2^{n-1}\frac{p!q!}{(n-1)!}.
\]
The map from \(n-1\) root coordinates to the zero-sum subspace has Gram determinant \(1/n\), hence intrinsic Euclidean volume is this quantity divided by \(\sqrt n\). The covariance derivation is independent of the overall constant Jacobian.

## Verification
A standalone script `artifacts/verify.py` enumerates vertices from half-space inequalities, triangulates their convex hull, and integrates first and second moments of the resulting origin-coned simplices by exact rational formulas. All determinant and covariance comparisons after vertex enumeration are exact; no floating-point covariance tolerances are used. The cases \((p,q)=(2,2),(2,3),(3,2),(2,4),(4,2),(3,3)\) give 76 distinct vertices, 360 simplices (including any zero-volume facets returned by the hull algorithm), and 174 checked ambient covariance entries. The checker also verifies zero first moment and the root-gauge volume identity. It requires Python 3, NumPy, SciPy, and SymPy. This finite verification supplements the all-parameter proof above.

## Relationship to prior work
Higashitani, Jochemko, and Michałek (arXiv:1807.07678, first public July 20, 2018) study the same symmetric edge polytopes, characterize facets, and determine the complete-bipartite \(h^*\)-polynomial. D'Alì, Delucchi, and Michałek (arXiv:1910.05193) connect these polytopes to metric Lipschitz/Kantorovich–Rubinstein polytopes, studying face structures, triangulations, volumes, and integral-point counts of duals. D'Alì, Juhnke-Kubitzke, and Koch (arXiv:2307.04933) treat polar and matroidal Ehrhart structure. None of the portions inspected derives the continuous-volume covariance spectrum or the sharp three-vertex eigenmode transition. The intrinsic polar-volume formula is already available and is not the originality claim. The conclusion of originality is conditional on the literature examined, not a certification of global historical priority.

## Limitations
The theorem concerns complete bipartite graphs with both parts of size at least two, unit cross-edge weights, and uniform volume in the intrinsic Euclidean polar. It does not classify arbitrary bipartite graphs, nonuniform edge metrics, vertex-uniform sampling, or higher moments. The finite checker covers only six small dimension profiles. An equivalent formula under the terminology of Lipschitz polytopes or transportation spaces might exist outside the sources located. No independent mathematical audit has been performed.

## References
- A. Higashitani, K. Jochemko, and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (2018), https://arxiv.org/abs/1807.07678.
- A. D'Alì, E. Delucchi, and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (2019), https://arxiv.org/abs/1910.05193.
- A. D'Alì, M. Juhnke-Kubitzke, and D. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933 (2023), https://arxiv.org/abs/2307.04933.
- J. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, https://arxiv.org/abs/1608.07905 (2016), related metric-polytope background.
