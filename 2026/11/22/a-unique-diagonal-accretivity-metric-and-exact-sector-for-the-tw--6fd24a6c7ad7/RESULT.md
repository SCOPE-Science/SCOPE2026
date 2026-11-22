# A unique diagonal accretivity metric and exact sector for the two-stage Radau pressure surrogate

## Finding

The two-stage Radau IIA inverse pressure-Schur surrogate has a sharp weighted field-of-values description even when the two spatial pressure operators do not commute. Fix any integer \(m\ge1\), any real symmetric positive-definite matrices \(P,Q\in\mathbb R^{m\times m}\), and \(\alpha,\beta>0\). Let
\[
A=\begin{pmatrix}5/12&-1/12\\3/4&1/4\end{pmatrix},\qquad B=A^{-1},\qquad C=A^{-2},\qquad L=\alpha B\otimes P+\beta C\otimes Q.
\]
For \(W=\operatorname{diag}(9,1)\otimes I_m\), the exact identity
\[
\frac{WL+L^{\mathsf T}W}{2}=
\operatorname{diag}\left(\frac{27}{2}\alpha P,\,\frac52\alpha P+4\beta Q\right)
\]
holds. Thus \(L\) is strictly accretive in the \(W\)-inner product and
\[
\operatorname{Re}\frac{x^*WLx}{x^*Wx}\ge\frac32\alpha\lambda_{\min}(P)
\quad(x\in\mathbb C^{2m}\setminus\{0\}).
\]
The constant is attained. Among all positive diagonal *stage* weights \(\operatorname{diag}(d_1,d_2)\otimes I_m\), the ratio \(d_1:d_2=9:1\) is the only one whose symmetric weighted part is positive semidefinite for **every** such \(P,Q,\alpha,\beta\).

Define the weighted numerical range \(\mathcal F_W(L)=\{x^*WLx/(x^*Wx):x\in\mathbb C^{2m}\setminus\{0\}\}\) and the largest generalized spatial eigenvalue
\[
\mu_+=\lambda_{\max}(P^{-1/2}QP^{-1/2}),\qquad r=\frac{\alpha}{\beta\mu_+}.
\]
The **smallest** symmetric closed sector about the positive real axis containing \(\mathcal F_W(L)\) has half-angle \(\theta\), exactly specified by
\[
\boxed{\tan\theta=\sqrt{\frac{3(r+4)^2}{r(5r+8)}}.}
\]
Its two boundary rays are attained by weighted Rayleigh quotients. In contrast, \((L+L^{\mathsf T})/2\) is indefinite for every admissible \(P,Q,\alpha,\beta\), including dimension one. The result distinguishes unconditional invertibility and strict weighted accretivity from the failure of unweighted accretivity and from deterioration of the sharp sector when the squared-inverse contribution dominates.

## Assumptions and scope

The stage tableau is the standard two-stage order-three Radau IIA tableau in the displayed order. All matrices are finite dimensional and real; the field of values is formed in the complexified vector space. No simultaneous diagonalizability or commutativity of \(P\) and \(Q\) is assumed. Strict spatial positive definiteness is needed: in incompressible-flow discretizations the constant-pressure nullspace must first be eliminated or a pressure gauge fixed. The coefficients \(\alpha,\beta\) are strictly positive. The statement is for the **exact algebraic inverse-Schur approximation**, not the full saddle-point Jacobian or inexact spatial solves.

## Proof

**1. Stage identities and coercivity.** Exact inversion and multiplication give
\[
B=\begin{pmatrix}3/2&1/2\\-9/2&5/2\end{pmatrix},\qquad
C=\begin{pmatrix}0&2\\-18&4\end{pmatrix}.
\]
For \(D=\operatorname{diag}(9,1)\), direct products give
\[
\frac{DB+B^{\mathsf T}D}{2}=\operatorname{diag}(27/2,5/2),\qquad
\frac{DC+C^{\mathsf T}D}{2}=\operatorname{diag}(0,4).
\]
Tensoring with the symmetric spatial factors proves the displayed weighted identity. Since \(\lambda_{\min}(P)>0\), each block dominates \((3/2)\alpha\lambda_{\min}(P)\) times its corresponding diagonal stage-weight block: \(27/2\ge(3/2)9\) and \(5/2\ge3/2\). Choosing a first-stage vector \((y,0)\), where \(Py=\lambda_{\min}(P)y\), gives equality in the weighted Rayleigh bound. Strict accretivity implies nonsingularity. Cauchy–Schwarz yields \(\|L^{-1}\|_W\le2/(3\alpha\lambda_{\min}(P))\), where \(\|\cdot\|_W\) is the induced norm.

**2. Uniqueness of diagonal stage weighting.** Suppose \(D'=\operatorname{diag}(d_1,d_2)\), with \(d_1,d_2>0\), makes \(((D'\otimes I)L+L^{\mathsf T}(D'\otimes I))/2\) positive semidefinite for all admissible data. Set \(m=1\) and \(P=Q=[1]\), fix \(\beta=1\), and let \(\alpha\downarrow0\). The limiting symmetric matrix must remain positive semidefinite, but it is
\[
\frac{D'C+C^{\mathsf T}D'}2=\begin{pmatrix}0&d_1-9d_2\\d_1-9d_2&4d_2\end{pmatrix}.
\]
Its determinant is \(-(d_1-9d_2)^2\), so \(d_1=9d_2\) is necessary. Step 1 proves sufficiency.

**3. Exact numerical-range angle.** With \(S=W^{1/2}=\operatorname{diag}(3,1)\otimes I_m\), the similar matrix \(N=SLS^{-1}\) has Hermitian and skew-Hermitian parts
\[
H=\frac{N+N^{\mathsf T}}2=\begin{pmatrix}H_1&0\\0&H_2\end{pmatrix},
\quad K=\frac{N-N^{\mathsf T}}2=\begin{pmatrix}0&T\\-T&0\end{pmatrix},
\]
where \(H_1=\frac32\alpha P\), \(H_2=\frac52\alpha P+4\beta Q\), and \(T=\frac32(\alpha P+4\beta Q)\). For every complex vector \(y\ne0\), \(\operatorname{Re}(y^*Ny)=y^*Hy>0\) and \(\operatorname{Im}(y^*Ny)=y^*(-iK)y\). The maximal absolute imaginary-to-real quotient equals the norm
\[
\kappa=\left\|H^{-1/2}(-iK)H^{-1/2}\right\|_2
=\left\|H_1^{-1/2}TH_2^{-1/2}\right\|_2.
\]
Here \(H^{-1/2}(-iK)H^{-1/2}\) is Hermitian and has eigenvalues equal to the signed singular values of \(H_1^{-1/2}TH_2^{-1/2}\), proving that both extremes are attained.

To compute the norm without supposing \(PQ=QP\), let \(U\) be an orthogonal eigenbasis of \(P^{-1/2}QP^{-1/2}\) with eigenvalues \(\mu_1,\ldots,\mu_m>0\). The invertible spatial congruence \(P^{-1/2}U\) simultaneously transforms \(P\) to \(I_m\) and \(Q\) to \(\operatorname{diag}(\mu_j)\). All generalized Hermitian Rayleigh quotients \(y^*(-iK)y/(y^*Hy)\) are invariant under an invertible congruence, so their extrema reduce to scalar two-stage blocks. For the \(j\)-th block, writing \(r_j=\alpha/(\beta\mu_j)\), the optimal ratio is
\[
\kappa_j=\frac{\frac32(\alpha+4\beta\mu_j)}{\sqrt{\frac32\alpha\left(\frac52\alpha+4\beta\mu_j\right)}}
=\sqrt{\frac{3(r_j+4)^2}{r_j(5r_j+8)}}.
\]
The derivative of its square is
\[
\frac{d}{dr}\frac{3(r+4)^2}{r(5r+8)}
=-\frac{96(r+1)(r+4)}{r^2(5r+8)^2}<0.
\]
Thus the largest \(\mu_j\) gives the largest \(\kappa_j\), establishing the exact sharp sector formula and attainment at a generalized eigenvector with eigenvalue \(\mu_+\). The value \(\tan\theta\) tends to \(\sqrt{3/5}\) when \(r\to\infty\) and diverges like \(\sqrt{6/r}\) as \(r\downarrow0\).

**4. Euclidean indefiniteness.** For any real nonzero spatial vector \(v\), the compression of the Euclidean symmetric part to \(\{(a_1v,a_2v):a_1,a_2\in\mathbb R\}\) is
\[
\begin{pmatrix}\frac32u&-2u-8w\\-2u-8w&\frac52u+4w\end{pmatrix},
\qquad u=\alpha v^{\mathsf T}Pv>0,\quad w=\beta v^{\mathsf T}Qv>0.
\]
Its determinant is \(-(u^2+104uw+256w^2)/4<0\). Therefore the full real symmetric part has a positive and a negative direction, whatever the spatial dimension. This proves the final assertion.

## Verification

The accompanying standalone `checker.py` directly reconstructs \(A^{-1}\) and \(A^{-2}\), checks exact rational stage identities, symbolic determinant and derivative factorizations, then checks 120 deterministic finite spatial matrix configurations with positive-definite (generally noncommuting) \(P,Q\). It compares the sector formula with the largest generalized Hermitian eigenvalue of the complexified matrix and checks the indefinite Euclidean symmetric part. Run `python checker.py` with `sympy` and `numpy` installed. The finite cases are diagnostic and are not used as a proof of the unrestricted-dimensional statements.

## Relationship to prior work

Ali and Kirby (2026), Equation (25), explicitly introduce the two-term inverse-Schur pressure surrogate involving \(A^{-1}\) and \(A^{-2}\); its construction is prior work, not a claimed contribution here. Leveque, He and Olshanskii (2025), Equations (21)–(22), give the earlier augmented-Lagrangian Runge–Kutta Schur approximation that motivates the same structure. Axelsson, Dravins and Neytcheva (2024), Sections 4–5, analyze field-of-values properties of a different, single-\(A^{-1}\) Radau tensor operator and its preconditioned variants. The present claim is the explicit unique diagonal accretivity metric and exact sharp sector for the *two-term \(A^{-1}\)/\(A^{-2}\) surrogate with arbitrary noncommuting spatial SPD factors*. These inspected works do not present this particular quantified statement. This is a best-knowledge comparison, not a proof of priority over all literature.

## Limitations

The result does not show that any full pressure Schur complement is spectrally equivalent to its approximation, does not prove an FGMRES iteration count for an inexact nonlinear preconditioner, and does not address singular pressure matrices before gauge fixing. A rapidly growing exact sector angle as \(\beta\mu_+/\alpha\to\infty\) prevents a coefficient-independent narrow sector conclusion. The analysis concerns exact arithmetic. Earlier general theorems on weighted accretivity of tensor sums may subsume portions of the argument; that priority risk is unresolved by the available searches. Independent validation has not been performed.

## References

1. A. Ali and R. C. Kirby, *Scalable Fully Implicit Runge–Kutta Solvers for Time-Dependent Rayleigh–Bénard Convection*, arXiv:2611.03361 (first public November 2, 2026), §§3, 5.2, Eq. (25). https://arxiv.org/html/2611.03361v1
2. L. Leveque, Y. He and M. Olshanskii, *An Augmented Lagrangian Preconditioner for Navier–Stokes Equations with Runge–Kutta in Time*, arXiv:2506.04451 (2025), §4, Eqs. (21)–(22). https://arxiv.org/html/2506.04451v1
3. O. Axelsson, I. Dravins and M. Neytcheva, *Stage-parallel preconditioners for implicit Runge–Kutta methods of arbitrarily high order, linear problems*, Numerical Linear Algebra with Applications 31 (2024), e2532, §§4–5. https://doi.org/10.1002/nla.2532
