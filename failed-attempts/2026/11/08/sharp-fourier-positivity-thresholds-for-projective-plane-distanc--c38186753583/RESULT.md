# Sharp Fourier-positivity thresholds for projective-plane distance hypergroups

## Finding
For **every existing finite projective plane** \(\Pi\) of order \(q\ge2\), including non-Desarguesian planes, let \(G_\Pi\) be its bipartite point–line incidence graph and let \(\delta\) be its shortest-path distance. Set \(v=q^2+q+1\), and let \(D_\alpha=(\delta(x,y)^\alpha)_{x,y\in V(G_\Pi)}\) for \(\alpha>0\) (zero diagonal). The radial kernel \(D_\alpha\) lies in the four-dimensional commutative distance algebra of \(G_\Pi\).

**Complete spherical-Fourier spectrum.** Its four eigenvalues, with multiplicities in parentheses, are
\[
\begin{aligned}
\lambda_0&=q(q+1)2^\alpha+(q+1)+q^2 3^\alpha &&(1),\\
\lambda_s&=q(q+1)2^\alpha-(q+1)-q^2 3^\alpha &&(1),\\
\lambda_+&=-2^\alpha+\sqrt q\,(3^\alpha-1) &&(v-1),\\
\lambda_-&=-2^\alpha-\sqrt q\,(3^\alpha-1) &&(v-1).
\end{aligned}
\]
The \(\lambda_0\)-eigenspace consists of constants; the other three lie in their orthogonal complement. The nontrivial Fourier multipliers of \(-D_\alpha\) are all nonnegative **if and only if** \(0<\alpha\le\beta_q\), where \(\beta_q\in(0,1)\) is the unique solution of
\[
3^{\beta_q}-1=\frac{2^{\beta_q}}{\sqrt q}.
\]
Equivalently, the incidence-graph metric \(\delta\) has generalized roundness exactly \(\beta_q\): its powered distance kernel has conditional negative type precisely for these positive exponents, and has *strict* negative type exactly for \(0<\alpha<\beta_q\).

**Sharp Hilbert embedding dimensions.** The least Euclidean dimension in which the finite metric \(\delta^{\alpha/2}\) embeds isometrically is \(2v-1\) for \(0<\alpha<\beta_q\) and \(v\) at \(\alpha=\beta_q\); for \(\alpha>\beta_q\), no such embedding in any real Hilbert space exists. At the endpoint the zero-sum Fourier nullspace has dimension \(v-1\). The thresholds strictly decrease with \(q\) and satisfy
\[
\beta_q=\frac{1}{(\log 3)\sqrt q}+O(q^{-1})
\qquad(q\longrightarrow\infty\text{ through orders of existing planes}).
\]

## Assumptions and scope
A finite projective plane of order \(q\) is a finite incidence structure with \(v=q^2+q+1\) points and \(v\) lines, \(q+1\) lines through each point and \(q+1\) points on each line, with exactly one line through two distinct points and exactly one point on two distinct lines. The order \(q\) is a positive integer for which a plane exists; the result does not assert existence for every integer. We assume \(q\ge2\). Graph distance is \(1\) between incident point–line pairs, \(3\) between nonincident point–line pairs, \(2\) between distinct vertices of the same kind, and \(0\) on the diagonal. Real nonnegative powers are interpreted entrywise, including \(0^\alpha=0\) for \(\alpha>0\).

For the distance hypergroup, let \(A_j\) indicate ordered pairs at graph distance \(j\) for \(j=0,1,2,3\). Their span is the commutative real distance/adjacency algebra; the sphere-normalized matrices \(P_j=A_j/k_j\) for \(j=1,2,3\), with valencies \(k_1=q+1\), \(k_2=q(q+1)\), and \(k_3=q^2\), are its stochastic radial convolution operators. In the unnormalized convention \(D_\alpha=A_1+2^\alpha A_2+3^\alpha A_3\), the four scalars above are its spherical Fourier multipliers. The claim applies to every finite projective plane independently of whether its automorphism group is transitive.

## Proof
**(1) Incidence identities.** Index the points and lines arbitrarily and write \(B\) for the \(v\times v\) incidence matrix. The axioms give
\[
B\mathbf1=(q+1)\mathbf1,\quad B^T\mathbf1=(q+1)\mathbf1,\quad BB^T=B^TB=qI+J,
\]
where \(J\) is the all-ones matrix. The graph-distance matrix powered by \(\alpha>0\) is the real symmetric block matrix
\[
D_\alpha=\begin{pmatrix}
2^\alpha(J-I)&3^\alpha J+(1-3^\alpha)B\\
3^\alpha J+(1-3^\alpha)B^T&2^\alpha(J-I)
\end{pmatrix}.
\]
The four distance matrices form a commutative distance algebra because the incidence identities force closure of their products; equivalently this bipartite graph is distance regular. This also justifies the distance-hypergroup Fourier terminology and chosen normalization.

**(2) Complete diagonalization.** On the two-dimensional span of \((\mathbf1,0)\) and \((0,\mathbf1)\), the diagonal blocks act by \(q(q+1)2^\alpha\), while the off-diagonal blocks act by \((q+1)+q^2 3^\alpha\). Symmetric and antisymmetric combinations give \(\lambda_0\) and \(\lambda_s\). On \(\mathbf1^\perp\), \(BB^T=qI\); hence \(B\) has singular value \(\sqrt q\) with multiplicity \(v-1\) there. The remaining block diagonal terms act as \(-2^\alpha I\), and the off-diagonal terms are \((1-3^\alpha)B\) and its transpose, producing precisely \(\lambda_+\) and \(\lambda_-\) with multiplicity \(v-1\) each. These multiplicities sum to \(2v\).

**(3) Three signs and the unique threshold.** For all \(\alpha>0\), \(\lambda_-<0\). Also \(\lambda_s(0)=-1\), where the expression is evaluated continuously at zero. Its derivative is
\[
q(q+1)(\log2)2^\alpha-q^2(\log3)3^\alpha<0,
\]
since \((q+1)\log2<q\log3\) for every integer \(q\ge2\), and \(3^\alpha\ge2^\alpha\). Thus \(\lambda_s<0\) for all \(\alpha>0\).
Now \(\lambda_+\le0\) is equivalent to
\[
\bigl(3/2\bigr)^\alpha-\bigl(1/2\bigr)^\alpha\le q^{-1/2}.
\]
The left-hand side has derivative \(\log(3/2)(3/2)^\alpha+\log 2(1/2)^\alpha>0\), starts at zero and equals one at \(\alpha=1\). Hence it crosses \(q^{-1/2}\in(0,1)\) at exactly one \(\beta_q\in(0,1)\). The zero-sum restriction of \(D_\alpha\) is nonpositive exactly through this threshold; it is negative definite below and has nullity exactly \(v-1\) at equality.

**(4) Hilbert realization and sharp dimensions.** The finite Schoenberg criterion says \(\delta^\alpha\) is conditionally negative semidefinite if and only if the centered Gram matrix \(-\tfrac12 HD_\alpha H\), with \(H=I-J/(2v)\), is positive semidefinite. Its rank equals the smallest dimension of a Euclidean isometric realization of the distances \(\delta^{\alpha/2}\). Below threshold, it has rank \(2v-1\); at threshold, the \(v-1\) vanishing Fourier multipliers leave rank \(v\). Above threshold the positive \(\lambda_+\) prohibits any such realization. Generalized roundness agrees with supremal negative type, giving the asserted sharp value.

**(5) Large order.** Let \(h(t)=(3/2)^t-(1/2)^t\). Since \(h(0)=0\), \(h'(0)=\log3\), and \(h\) is smooth and strictly increasing, its inverse has expansion \(h^{-1}(s)=s/\log3+O(s^2)\) at \(s=0\). Substitution \(s=q^{-1/2}\) yields the asymptotic. Since \(h\) increases, \(\beta_q\) decreases strictly in every existing order \(q\).

## Verification
The included standalone `check.py` constructs the Desarguesian planes \(\mathrm{PG}(2,p)\) for primes \(p\in\{2,3,5,7\}\), with no reference to a precomputed graph spectrum. It constructs all points and lines as normalized nonzero vectors over \(\mathbb F_p\), verifies \(BB^T=pI+J\), independently computes shortest paths by breadth-first search, and checks all predicted eigenvalues and centered-matrix inertia on both sides of the threshold. Each test uses dense real symmetric eigenvalue diagonalization with tolerance \(10^{-9}\), and the endpoints are also checked. The reported critical exponents are approximately \(0.694280092777194\), \(0.560762760129698\), \(0.429000500245483\), and \(0.359970813996583\) for those four orders. The script emits `ALL_PROJECTIVE_PLANE_NEGATIVE_TYPE_CHECKS_OK` upon success.

The exact all-plane result and asymptotic are algebraic deductions above: finite numerical tests do not establish results for all finite planes, nor validate exotic non-Desarguesian planes separately. The finite calculation is corroboration, not a substitute for the incidence-axiom argument.

## Relationship to prior work
Murugan's *Generalized roundness of vertex transitive graphs* (arXiv:1112.5657, initially public 2011-12-23), especially Theorem 3.1, gives a general determinant criterion for generalized roundness of distance matrices with constant row multisets. It applies conceptually here, but its inspected statements do not evaluate the critical exponent, four multipliers, or endpoint embedding ranks for arbitrary projective-plane incidence hypergroups. Aalipour et al., *On the distance spectra of graphs* (arXiv:1509.01196, initially public 2015-09-03) develop ordinary distance-spectrum theory, including block-matrix spectral methods. Its inspected results concern unpowered distances and other graph families; the exponent-dependent Fourier threshold and Hilbert rank collapse are not directly supplied. The projective-plane incidence graphs and their significance appear, for example, in De Winter–Lazebnik–Verstraëte (2008), whose subject is extremal cycle geometry, not powered metric Fourier positivity.

The contribution claimed here is the explicit all-order distance-hypergroup multiplier calculation *as a function of real exponent* and the complete negative-type and endpoint Hilbert-dimension classification, including non-Desarguesian planes. The spectral step uses classical incidence identities and standard Schoenberg theory; the result should not be construed as a new general negative-type theorem. Prior authors' general theorems make this specialization natural, so a previously tabulated case or an unlocated stronger association-scheme theorem remains a genuine originality risk.

## Limitations
No finite plane existence theorem is asserted for orders where existence is unsettled or impossible. Only real exponents \(\alpha>0\) and the ordinary shortest-path distance are classified. The proof relies on well-known finite-dimensional spectral and Schoenberg equivalences. Historical priority beyond the bounded inspected literature is unverified; independent mathematical audit has not been performed.

## References
- S. De Winter, F. Lazebnik, J. Verstraëte, *An Extremal Characterization of Projective Planes*, Electronic Journal of Combinatorics **15** (2008), R143, https://doi.org/10.37236/867 (public 2008-11-30).
- M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657, https://arxiv.org/abs/1112.5657 (first public 2011-12-23), especially Theorem 3.1.
- G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196, https://arxiv.org/abs/1509.01196 (first public 2015-09-03).
