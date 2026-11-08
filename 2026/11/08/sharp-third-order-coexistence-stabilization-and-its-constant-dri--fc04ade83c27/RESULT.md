# Sharp third-order coexistence stabilization and its constant-drift obstruction

## Finding
For \(n\geq 1\), fix \(r\in\mathbb R^n\), \(S\in\mathbb R^{n\times n}\), and a target abundance \(p\in(0,\infty)^n\). In the three-body Lotka--Volterra family
\[
\dot x_i=x_i\left(r_i+\sum_{j=1}^n S_{ij}x_j+\sum_{j,k=1}^n B_{ijk}x_jx_k\right),\quad B_{ijk}=B_{ikj}\in\mathbb R,
\]
the positive state \(p\) can be made an equilibrium with Hurwitz Jacobian by choosing \(B\) **if and only if** the vector
\[
w_i=-2r_i-\sum_{j=1}^n S_{ij}p_j
\]
is nonconstant, or is the constant vector \(c\mathbf1\) with \(c<0\). If \(w\) is nonconstant, every eigenvalue of the Jacobian can simultaneously be set to \(-1\) using just quadratic per-capita interactions (three-body terms). If \(w=c\mathbf1\) with \(c\geq0\), every equilibrium-realizing three-body tensor has \(c\) as a Jacobian eigenvalue. For \(n\ge2\), the obstruction to generic three-body stabilization is therefore confined to a codimension-\(n-1\) constant-drift locus. The assertion is about **linear local asymptotic stability at a prescribed target**, not global stability.

## Assumptions and scope
All coefficients of the three-body tensor are freely chosen real numbers, including mixed signs and repeated partner indices. The growth vector \(r\), the pairwise matrix \(S\), and the positive target \(p\) are fixed rather than optimized. The state space is the positive orthant and the system is a smooth autonomous ordinary differential equation. Here “Hurwitz” means every Jacobian eigenvalue has strictly negative real part. The one-species case is included; a nonconstant vector exists only when \(n\ge2\). The statement makes no claim about demographic stochasticity, finite-sample outcomes, globally bounded dynamics, or sign-constrained ecological tensors.

## Proof
**Step 1 (reduce to unit abundance).** Set \(y_i=x_i/p_i\) and \(A_{ij}=S_{ij}p_j\). In the \(y\)-coordinates, the per-capita growth functions are \(G_i(y)=r_i+\sum_j A_{ij}y_j+Q_i(y)\), where \(Q_i\) is homogeneous quadratic. The desired state is \(\mathbf1\). The Jacobians in \(x\) and \(y\) coordinates are similar via the positive diagonal matrix \(\operatorname{diag}(p)\).

**Step 2 (the forced row-sum identity).** At an equilibrium \(\mathbf1\), homogeneity and the equilibrium equations give
\[
Q_i(\mathbf1)=q_i:=-r_i-\sum_j A_{ij},\qquad
\sum_j\partial_jQ_i(\mathbf1)=2q_i.
\]
Because \(G_i(\mathbf1)=0\), the full Jacobian \(H\) in \(y\)-coordinates has entries \(H_{ij}=A_{ij}+\partial_jQ_i(\mathbf1)\). Consequently
\[
H\mathbf1=w,\qquad w_i=-2r_i-\sum_j A_{ij}.
\]
This identity holds for every admissible tensor; it is not merely a necessary condition for the construction below.

**Step 3 (every compatible Jacobian is realizable).** Conversely, suppose a real matrix \(H\) obeys \(H\mathbf1=w\), and set \(g_i=(H_{ij}-A_{ij})_{j=1}^n\). Then \(g_i\cdot\mathbf1=2q_i\). With \(L(y)=\sum_jy_j\), define
\[
Q_i(y)=\frac{L(y)}n\,(g_i\cdot y)-\frac{q_i}{n^2}L(y)^2.
\]
Direct differentiation yields \(Q_i(\mathbf1)=q_i\) and \(\nabla Q_i(\mathbf1)=g_i\). Thus \(\mathbf1\) is an equilibrium with exactly the requested Jacobian \(H\). This polynomial corresponds to the explicitly symmetric tensor
\[
T_{ijk}=\frac{g_{ij}+g_{ik}}{2n}-\frac{q_i}{n^2},\qquad B_{ijk}=\frac{T_{ijk}}{p_jp_k}.
\]
Hence no additional nonlinear-jet obstruction exists under the stated unrestricted-tensor convention.

**Step 4 (the nonconstant case).** Suppose \(w\) is nonconstant; write \(\bar w=n^{-1}\sum_iw_i\), \(u=w-\bar w\mathbf1\), \(v=w+\mathbf1\), and
\[
f=\frac{\mathbf1}{n}-(1+\bar w)\frac{u}{u^{\mathsf T}u}.
\]
Then \(f^{\mathsf T}\mathbf1=1\) and \(f^{\mathsf T}v=0\). Set \(H=-I+vf^{\mathsf T}\). It follows that \(H\mathbf1=w\), while \((vf^{\mathsf T})^2=0\). Therefore all eigenvalues of \(H\) are exactly \(-1\), counting algebraic multiplicity. Step 3 realizes \(H\) by a symmetric three-body tensor.

**Step 5 (constant case and necessity).** If \(w=c\mathbf1\), every compatible Jacobian has eigenpair \((\mathbf1,c)\); hence it cannot be Hurwitz when \(c\geq0\). If \(c<0\), take \(H=cI\), which is Hurwitz and satisfies the row-sum constraint; Step 3 realizes it. The argument also covers \(n=1\). Rescaling as in Step 1 proves the full claim for any positive target \(p\). \(\square\)

**Illustrative two-species boundary.** For \(p=(1,1)\), \(S=0\) and \(r=(-1,-1)\), one has \(w=(2,2)\) and cannot obtain a Hurwitz equilibrium using three-body terms alone. Replacing the second growth rate by \(-2\) makes \(w=(2,4)\): the construction yields
\[
H=\begin{pmatrix}13/2&-9/2\\25/2&-17/2\end{pmatrix},\qquad (H+I)^2=0.
\]
Both Jacobian eigenvalues are \(-1\), despite both intrinsic growth rates being negative.

## Verification
The standalone exact-rational checker \(\texttt{verify.py}\) constructs \(H\), the quadratic tensor, the target equilibrium and its full Jacobian for 960 reproducible rational input triples with \(1\leq n\leq6\). It checks all equilibrium and derivative identities exactly, verifies nilpotence in nonconstant cases, tests negative-constant and obstructed constant branches, and separately includes six explicit nonnegative-constant obstruction examples. Its result is: 640 nonconstant constructions, 152 negative-constant constructions, 168 obstructed cases; all assertions passed. These finite checks supplement and do not replace the arbitrary-dimensional proof. Run \(\texttt{python verify.py}\) with Python 3; no external dependencies are required.

## Relationship to prior work
Çelik, Isoldi, Portakal and Zucal's 2026 *Stable Coexistence in Ecologies and Games* proves universal prescribed-target stabilization with **both quadratic and cubic per-capita terms** (its Theorem 4.2), and its Example 4.1 shows a specific three-body rescue. The present theorem asks the strictly narrower intervention-order question: for fixed data and a fixed target, *when are quadratic per-capita terms alone enough?* The answer is a complete if-and-only-if classification, including an obstruction not ruled out by the sufficient four-body construction. Gibbs et al. (2024) analyze feasibility-constrained higher-order ecological interactions and stability effects under sampled/sign-constrained tensors, but do not establish this exact unrestricted polynomial-jet completion criterion. Duran-Sala et al. (2025) study a different competitive network/replicator model rather than unrestricted higher-order Lotka--Volterra coefficient selection. The row-sum calculation uses familiar Euler homogeneity and Hurwitz stability; the claim of distinct value is their sharp combination for a prescribed ecological target, not invention of these ingredients.

## Limitations
Coefficients are unrestricted real numbers and may be very large near the nonnegative constant-drift locus; the theorem does not establish biological implementability, positivity of higher-order terms, global attraction, or boundedness of solutions outside a local basin. A repeated partner index is allowed, so the finding is not automatically transferable to models imposing three *distinct* species per interaction. For the exceptional \(c=0\) locus, the result rules out Hurwitz stability but does not exclude nonhyperbolic nonlinear asymptotic stability. Originality is a best-knowledge literature comparison rather than a uniqueness certificate; unindexed equivalents remain possible.

## References
1. T. Ö. Çelik, V. A. Isoldi, I. Portakal, G. Zucal, *Stable Coexistence in Ecologies and Games*, arXiv:2609.09286v1, publicly posted 2026-09-08. https://arxiv.org/abs/2609.09286
2. T. L. Gibbs, G. Gellner, S. A. Levin, K. S. McCann, A. Hastings, J. M. Levine, *When can higher-order interactions produce stable coexistence?*, Ecology Letters 27 (2024), e14458. https://doi.org/10.1111/ele.14458
3. M. Duran-Sala, S. Meloni, V. Calleja-Solanas, *On the stability of competitive ecological communities with pairwise and higher-order interactions*, arXiv:2501.09172v1, publicly posted 2025-01-15. https://arxiv.org/abs/2501.09172
