# A sharp \(1-\sqrt{2/3}\) complex-pair bound for minimally sketched symmetric Ritz matrices

## Finding

Let \(A\in\mathbb R^{3\times3}\) be **any real symmetric matrix**, and let \(U\in\mathbb R^{3\times2}\) have orthonormal columns. Draw \(S\in\mathbb R^{2\times3}\) with independent standard real Gaussian entries. Almost surely \(SU\) is invertible. Form the two-dimensional sketched Rayleigh–Ritz matrix
\[
M=(SU)^{-1}SAU.
\]
Then
\[
\boxed{\Pr\{M\text{ has a nonreal conjugate eigenpair}\}\le 1-\sqrt{2/3}.}
\]
This bound is **sharp even among symmetric positive-definite** \(A\). To characterize equality, diagonalize the ordinary Ritz compression \(U^\mathsf TAU\), writing its ordered eigenvalues as \(\alpha\le\beta\), and let \(v\) be either unit normal to the Ritz plane. With \(u_1,u_2\) its eigenvector basis, put \(t_i=v^\mathsf TAu_i\). Equality holds if and only if
\[
\alpha<\beta,\qquad |t_1|=|t_2|=\beta-\alpha.
\]
For example, equality is achieved by
\[
U=[e_1,e_2],\qquad
A=\begin{pmatrix}1&0&2\\0&3&2\\2&2&10\end{pmatrix}\succ0.
\]
The sharp probability is \(1-\sqrt{2/3}=0.1835034190722739\ldots\), or approximately \(18.35\%\). The result is for one exact-arithmetic extraction with **two sketch rows and a two-dimensional search space in ambient dimension three**; it is not a dimension-free or multi-iteration bound.

A finite-dimensional exact probability formula is also available. In the notation below, if the ordinary Ritz eigenvalues are distinct and both residual couplings are nonzero, diagonalize the explicit matrix \(K\) from the proof as \(\lambda_1\ge\lambda_2>0>\lambda_3\), and set \(u=-\lambda_3/\lambda_1\), \(v=-\lambda_3/\lambda_2\). Then \(u+v=1\) and
\[
\Pr\{M\text{ has a nonreal pair}\}
=1-\frac1{2\pi}\int_0^{2\pi}
\sqrt{\frac{C(\theta)}{1+C(\theta)}}\,d\theta,
\qquad C(\theta)=\frac{\cos^2\theta}{u}+\frac{\sin^2\theta}{v}.
\]
If the Ritz eigenvalues coincide or either residual coupling vanishes, this probability is zero.

## Assumptions and scope

All matrices and random variables are real. Arithmetic is exact; \(A\) need only be symmetric, not positive definite. Gaussian entries of any common nonzero variance give the same law because common scaling cancels from \((SU)^{-1}SAU\). The plane \(U\) and \(A\) are fixed independently of \(S\); the rank-full event for \(SU\) has probability one. The claim concerns whether the projected **two-by-two** matrix has strictly nonreal eigenvalues. The probability of a repeated real eigenvalue at the discriminant boundary is zero except in deterministic real-spectrum degeneracies.

The usual whitened sRR matrix is similar to \(M\): if \(SU=QR\) is a full-rank QR factorization, the whitened basis \(UR^{-1}\) produces \(RMR^{-1}\). Thus whitening does not change the event studied here.

## Proof

**1. Symmetric normal form.** By orthogonal invariance of Gaussian sketches and a change of orthonormal search basis, assume \(U=[e_1,e_2]\) and
\[
A=\begin{pmatrix}
\alpha&0&t_1\\0&\beta&t_2\\t_1&t_2&\gamma
\end{pmatrix},\qquad d=(\beta-\alpha)/2\ge0.
\]
Write the first two columns of \(S\) as \(F\in\mathbb R^{2\times2}\), and its third column as \(g\in\mathbb R^2\). Then \(F\) and \(g\) are independent Gaussian arrays and
\[
M=\begin{pmatrix}\alpha&0\\0&\beta\end{pmatrix}
+q(t_1,t_2),\qquad q=F^{-1}g.
\]
In particular, \(\gamma\) plays no role. A direct trace-and-determinant calculation gives the discriminant
\[
D=\bigl(\operatorname{tr}M\bigr)^2-4\det M
=4d^2-4d(t_1q_1-t_2q_2)+(t_1q_1+t_2q_2)^2.
\]
A real two-by-two matrix has a nonreal conjugate pair exactly when \(D<0\). When \(d=0\) or \(t_1t_2=0\), the discriminant is a square, so the probability is zero.

**2. A joint Cauchy identity.** For nondegenerate \(F\), the change of variables \(g=Fq\) has Jacobian \(|\det F|\). Integrating the joint Gaussian density over \(F\), and substituting \(Y=F(I+qq^\mathsf T)^{1/2}\), yields a density proportional to
\[
\det(I+qq^\mathsf T)^{-3/2}=(1+\|q\|^2)^{-3/2}.
\]
Normalization in \(\mathbb R^2\) gives exactly \((2\pi)^{-1}(1+\|q\|^2)^{-3/2}\). This is also the density of \((G_1/G_0,G_2/G_0)\), where \(G_0,G_1,G_2\) are independent standard normals. Therefore the event \(D<0\) has the same probability as negativity of the quadratic form
\[
Q=(t_1G_1+t_2G_2)^2-4dG_0(t_1G_1-t_2G_2)+4d^2G_0^2
=G^\mathsf TKG,
\]
where \(G=(G_1,G_2,G_0)^\mathsf T\) and
\[
K=\begin{pmatrix}
t_1^2&t_1t_2&-2dt_1\\
t_1t_2&t_2^2&2dt_2\\
-2dt_1&2dt_2&4d^2
\end{pmatrix}.
\]

**3. The rigid cone identity.** The three principal minors of order two of \(K\) vanish identically. Consequently, its second elementary spectral symmetric function is zero:
\[
\lambda_1\lambda_2+\lambda_1\lambda_3+\lambda_2\lambda_3=0.
\]
Furthermore \(\det K=-16d^2t_1^2t_2^2<0\) when \(dt_1t_2\ne0\), and \(\operatorname{tr}K=t_1^2+t_2^2+4d^2>0\); hence \(K\) has two positive eigenvalues \(\lambda_1,\lambda_2\) and one negative eigenvalue \(\lambda_3\). Defining \(u=-\lambda_3/\lambda_1>0\) and \(v=-\lambda_3/\lambda_2>0\), the vanishing spectral symmetric function gives the **exact identity** \(u+v=1\). Orthogonal invariance of the standard Gaussian vector now transforms \(Q<0\) into
\[
\frac{Z_1^2}{u}+\frac{Z_2^2}{v}<Z_3^2,
\]
where \(Z_1,Z_2,Z_3\) are independent standard normals.

**4. Sharp Gaussian ellipse comparison.** Fix \(Z_3=z\ne0\). The permitted \((Z_1,Z_2)\)-region is a centered ellipse with area \(\pi z^2\sqrt{uv}\), at most \(\pi z^2/2\) because \(u+v=1\). For the radially strictly decreasing standard bivariate Gaussian density, a centered disk maximizes mass among all measurable sets of a prescribed area: exchange a point outside the disk for a point inside to increase the mass. Hence the ellipse's Gaussian mass is bounded by that of the centered disk of radius \(|z|/\sqrt2\); equality for nonzero \(z\) occurs precisely when \(u=v=1/2\). Integrating over \(Z_3\),
\[
\Pr(Q<0)\le \Pr(Z_1^2+Z_2^2<Z_3^2/2)
=\mathbb E[1-e^{-Z_3^2/4}]
=1-\sqrt{2/3}.
\]
The integral identity in the Finding follows by conditioning instead on the polar angle of \((Z_1,Z_2)\): for fixed \(C>0\), rotational invariance in \(\mathbb R^3\) gives \(\Pr(Z_3^2>C(Z_1^2+Z_2^2))=1-\sqrt{C/(1+C)}\).

**5. Equality classification.** The strict Gaussian rearrangement step makes equality equivalent to \(\lambda_1=\lambda_2>0\). Put \(T=\operatorname{tr}K=t_1^2+t_2^2+4d^2\). With two equal positive eigenvalues and zero second spectral symmetric function, the eigenvalues must be \(2T/3,2T/3,-T/3\). Comparing their product with \(\det K\) gives
\[
T^3=108d^2t_1^2t_2^2.
\]
The arithmetic–geometric mean inequality gives
\[
(t_1^2+t_2^2+4d^2)^3\ge 27(t_1^2t_2^2\cdot4d^2)
=108d^2t_1^2t_2^2,
\]
with equality if and only if \(t_1^2=t_2^2=4d^2\). Conversely, these equalities yield \(K\)-eigenvalues \(8d^2,8d^2,-4d^2\), and thus attain the bound. For the explicit example, the Schur complement of the upper \(\operatorname{diag}(1,3)\) block is \(10-4-4/3=14/3>0\); therefore it is SPD. This completes the proof for all admissible inputs, including degenerate boundary cases.

## Verification

Run `python3 verify.py` from this directory. The verifier uses only the Python standard library and checks 14,400 exact-rational algebraic identities and inequalities, 20 numerical angular-integral cases, and 180,000 seeded Gaussian sketches drawn from the actual two-by-three sketch model. One recorded execution returned `VERIFY_OK`, with observed sharp-example frequency \(0.1844722\) versus the exact \(0.1835034\), inside the declared seven-standard-error tolerance. These finite checks are independent sanity checks of the formulas; the proof above establishes the universal constant and equality conditions.

## Relationship to prior work

Liu and Liu (2026) use whitening and a real Schur formulation to handle nonreal eigenpairs produced by symmetric sketched Rayleigh–Ritz extraction. Nakatsukasa and Tropp (2024, section 6.8) identify the same basic nonreal-eigenvalue failure mechanism. Neither of the inspected relevant sections gives a sharp probability **uniform over all three-dimensional symmetric inputs and all two-planes**, together with equality cases. This theorem analyzes only the minimally sized real Gaussian extraction, and does not supersede their broader algorithms. Classical real non-Hermitian random-matrix ensembles and rank-one non-Hermitian perturbations study different distributions and do not directly imply this sharp sRR constant. Priority relative to less-accessible specialized small-dimensional literature remains open.

## Limitations

The 18.35% bound applies only when the ambient dimension is exactly three, the search dimension and Gaussian sketch row count are both two, and the search plane is independent of the sketch. It does not bound nonreal-pair probability for larger ambient dimensions, sketches with more rows, adaptive data-dependent planes, non-Gaussian sketches, or full iterative eigensolvers. The equality condition is phrased in an eigenbasis of the ordinary two-dimensional Ritz compression, not in terms of the full spectral eigenvalue gaps of \(A\). All assertions concern exact arithmetic, not finite-precision complex rounding effects.

## References

- J. Liu and Y. Liu, *Real-Arithmetic Sketched Eigensolvers for Symmetric Matrices*, arXiv:2610.22261v1, first submitted 2026-10-15. https://arxiv.org/abs/2610.22261
- Y. Nakatsukasa and J. A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM Journal on Matrix Analysis and Applications 45 (2024), 1183–1214, especially section 6.8. https://doi.org/10.1137/23M1565413
- R. Kozhan, *Rank One Non-Hermitian Perturbations of Hermitian \(\beta\)-Ensembles of Random Matrices*, Journal of Statistical Physics 168 (2017), 92–108. https://doi.org/10.1007/s10955-017-1792-0
