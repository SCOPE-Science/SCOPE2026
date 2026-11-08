# Unique scalar Schur tuning for modal double-saddle-point Richardson iteration

## Finding

Let \(d\geq2\), let \(b_1,\ldots,b_d>0\), let \(c>0\), and write \(B=\max_i b_i\) and \(\beta=\min_i b_i\). For the symmetric double-saddle-point matrix and one-parameter block triangular preconditioner defined below, the exact asymptotic convergence factor of unit-step preconditioned Richardson iteration is uniquely minimized by

\[
 r_* = \frac{2B^2}{B^2+\beta^2+\sqrt{(B^2+\beta^2)^2+4c^2B^2}},
 \qquad q_* = \frac{B^2}{r_*^2}.
\]

Specifically, for every \(q>0\), the error iteration matrix \(T(q)\) satisfies \(\rho(T(q))\geq r_*\), with equality **if and only if** \(q=q_*\). Thus this is an exact scalar-Schur minimax law, valid in every modal dimension. At the optimizer the smallest-coupling mode has real eigenvalues \(r_*\) and \(r_*\beta^2/B^2\), while the largest-coupling mode has a conjugate pair of modulus \(r_*\) (coalescing to a double real eigenvalue when \(\beta=B\)). Intermediate modes cannot worsen the optimum. As \(0<r_*<1\), the optimal iteration converges from every initial error.

For example, with two modes \((b_1,b_2)=(1,3)\) and \(c=4\), the unique optimum is \(q_*=36\) and \(\rho(T(q_*))=1/2\). The natural largest-mode Schur scale \(q=B^2+c^2=25\) instead gives \(\rho(T(25))=3/5\).

## Assumptions and scope

Fix an integer \(d\geq2\), positive real numbers \(b_i\), and \(c>0\). Let \(D=\operatorname{diag}(b_1,\ldots,b_d)\) and \(I=I_d\). Define the \(3d\)-dimensional symmetric indefinite system and an invertible upper block triangular preconditioner

\[
 K=\begin{pmatrix}I&0&D\\0&I&cI\\D&cI&0\end{pmatrix},\qquad
 P(q)=\begin{pmatrix}I&0&0\\0&I&cI\\0&0&-qI\end{pmatrix},\quad q>0.
\]

The matrix \(K\) is nonsingular: its Schur complement on the final block is \(-(D^2+c^2I)\), negative definite. Consider **only** the exact, unit-step stationary iteration

\[
 x_{k+1}=x_k+P(q)^{-1}(f-Kx_k),\qquad
 T(q)=I_{3d}-P(q)^{-1}K.
\]

For fixed finite \(d\), \(\rho(T(q))\) is the exact asymptotic convergence factor in the sense of the matrix-power root limit \(\lim_{k\to\infty}\|T(q)^k\|^{1/k}=\rho(T(q))\). This concerns the scalar \(Q=qI\) approximation class, not arbitrary positive-definite Schur blocks, nonstationary iterations, or restarted Krylov methods.

## Proof

**Modal reduction.** Simultaneously permuting coordinates to group the three variables corresponding to each \(b_i\), the iteration is a direct sum of the matrices

\[
 T_i(q)=\begin{pmatrix}
 0&0&-b_i\\
 -cb_i/q&-c^2/q&-c\\
 b_i/q&c/q&1
 \end{pmatrix}.
\]

Direct determinant expansion gives

\[
 \det(zI_3-T_i(q))
 =z\left[z^2-\left(1-\frac{c^2}{q}\right)z+\frac{b_i^2}{q}\right].
\]

The zero root is harmless. Put \(a(q)=1-c^2/q\) and \(p_i(q)=b_i^2/q>0\). The two remaining roots of \(z^2-a(q)z+p_i(q)\) govern the asymptotic factor.

**Necessary lower bound.** Let \(r=\rho(T(q))\). Since the two nonzero roots belonging to the largest coupling \(B\) lie in the closed radius-\(r\) disk and their product is \(B^2/q\),

\[
 q\geq \frac{B^2}{r^2}.
\]

For the smallest coupling \(\beta\), the real polynomial evaluated at \(r\) is nonnegative: if the roots are real, both are at most \(r\), while if they are nonreal conjugates their factors at \(r\) multiply to a squared modulus. Hence

\[
 r^2-a(q)r+\frac{\beta^2}{q}\geq0,
 \qquad q r(1-r)\leq c^2r+\beta^2.
\]

For \(r\geq1\) there is nothing to show because the asserted minimum lies strictly below one. For \(0<r<1\), combining these inequalities yields

\[
 c^2r^2+(B^2+\beta^2)r-B^2\geq0.
\]

The left side is strictly increasing for nonnegative \(r\), negative at zero and positive at one. Its unique positive zero is exactly the displayed \(r_*\), so \(r\geq r_*\) for every \(q>0\).

**Attainment for every mode.** Set \(q_*=B^2/r_*^2\), and define \(\delta=\beta/B\in(0,1]\). The equality defining \(r_*\) implies

\[
 a(q_*)=r_*(1+\delta^2),\qquad
 \delta^2r_*^2\leq p_i(q_*)\leq r_*^2.
\]

For each mode consider \(h_i(z)=z^2-r_*(1+\delta^2)z+p_i(q_*)\). Its roots have positive sum and positive product. If they are nonreal, each has modulus \(\sqrt{p_i(q_*)}\leq r_*\). If they are real, they are positive and

\[
 h_i(r_*)=p_i(q_*)-\delta^2r_*^2\geq0.
\]

They cannot both exceed \(r_*\), since their product is at most \(r_*^2\), nor can they straddle \(r_*\), since the displayed evaluation is nonnegative. Consequently both lie in \((0,r_*]\). Thus \(\rho(T(q_*))\leq r_*\). At a smallest-coupling mode the roots factor exactly as \((z-r_*)(z-\delta^2r_*)\), establishing equality. At a largest-coupling mode the product is \(r_*^2\), and the sum is \(r_*(1+\delta^2)\), giving a conjugate pair of radius \(r_*\) when \(\delta<1\), or a double root \(r_*\) when \(\delta=1\).

**Uniqueness.** If some \(q>0\) attains \(r_*\), the largest-coupling product inequality forces \(q\geq B^2/r_*^2=q_*\). The smallest-coupling polynomial evaluation forces

\[
 q\leq\frac{c^2r_*+\beta^2}{r_*(1-r_*)}=q_*.
\]

Therefore \(q=q_*\), proving uniqueness and the theorem.

**Exact example.** For \((\beta,B,c)=(1,3,4)\), the defining equation is \(16r^2+10r-9=0\), whose positive root is \(r_*=1/2\). Thus \(q_*=36\). The small mode has quadratic eigenvalues \(1/2,1/18\), and the large mode has \((5\pm2i\sqrt{14})/18\), each of modulus \(1/2\). With \(q=25\), the large mode has a conjugate pair of modulus \(3/5\), while the small mode has modulus \(1/5\).

## Verification

The analytic determinant factorization and lower/upper bound argument constitute the proof for all positive real parameters and all finite modal dimensions. The accompanying `check.py` builds the actual full matrix, checks the exact rational example, and tests the modal formula against direct dense eigenvalue calculations and numerical parameter perturbations in 250 seeded cases (9456 passing assertions on the documented run). Repeated-root cases are checked with looser floating-point tolerances because numerical square roots at a double root are ill-conditioned. These finite checks are not substituted for the proof.

Reproduce with `python check.py` using Python 3 and NumPy.

## Relationship to prior work

Liang and Huang (arXiv:2609.01031, version 1 released 2026-09-01), Section 2, develop a block triangular inexact preconditioner for the same general symmetric double-saddle-point structure and derive real/nonreal spectral bounds via a parameterized cubic; Section 3 analyzes randomized construction of the Schur approximation. The present result retains its upper triangular block pattern but specializes to identity leading blocks and simultaneously diagonal modal couplings, changes the evaluation criterion to the exact convergence radius of unit-step Richardson, and **optimizes** a single scalar Schur block over all positive scales. The cubic collapses to a zero mode and a quadratic per coupling; the new extremal result balances the smallest and largest modes and proves uniqueness.

Bergamaschi, Ferronato, and Martínez (arXiv:2505.06043, first submitted 2025-05-09), Sections 2.1–2.2, bound real and complex eigenvalues for a different triangular Schur preconditioner arising from poroelasticity; their complex-eigenvalue circle is not a sharp scalar-block minimax prescription for the above iteration. Pearson and Potschka (2023, arXiv:2106.12433) analyze a symmetric positive-definite factorized preconditioner and its ideal eigenvalue clustering, not the present nonsymmetric scalar upper triangular preconditioner. Classical Richardson/Uzawa spectral-radius tuning is background motivation, but the exact two-extreme-mode quadratic balancing formula here is not obtained by directly applying the SPD real-spectrum Richardson formula.

## Limitations

The proof requires an exactly commuting modal family, positive \(b_i\) and common positive coupling \(c\). It optimizes the **asymptotic spectral radius** of the unit-step stationary iteration with \(Q=qI\), not the norm of a single step, nonnormal transient amplification, error in finite precision, GMRES iteration counts, or computational costs for a PDE problem. When \(\beta=B\), the critical repeated eigenvalue can be defective, producing polynomial prefactors despite the sharp asymptotic root factor. Wider noncommuting systems and variable \(Q\) are not classified. Historical equivalence with unindexed scalar saddle-point parameter analyses cannot be categorically excluded without independent review.

## References

1. S. Liang and N. Huang, *Randomized inexact block triangular preconditioners for double saddle-point systems in PDE-constrained optimization*, arXiv:2609.01031v1 (2026-09-01), https://arxiv.org/html/2609.01031.
2. L. Bergamaschi, M. Ferronato, and Á. Martínez, *Triangular preconditioners for double saddle point linear systems arising in the mixed form of poroelasticity equations*, arXiv:2505.06043 (first released 2025-05-09), https://arxiv.org/html/2505.06043.
3. J. W. Pearson and A. Potschka, *On symmetric positive definite preconditioners for multiple saddle-point systems*, IMA Journal of Numerical Analysis 44 (2024), 1731–1750, first available 2023-08-05 as journal article; preprint arXiv:2106.12433, https://arxiv.org/abs/2106.12433.
4. Y. Notay, *A New Analysis of Block Preconditioners for Saddle Point Problems*, SIAM Journal on Matrix Analysis and Applications 35 (2014), 143–173, DOI 10.1137/130911962, https://doi.org/10.1137/130911962 (2013 lecture notes inspected: https://diamhomes.ewi.tudelft.nl/~kvuik/notay_2013.pdf; the full journal article was not assessed).
