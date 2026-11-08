# The sharp universal second-subspace backward-error factor for MINBERR

## Finding
For every integer \(n\ge1\), every nonzero real symmetric positive-semidefinite matrix \(A\in\mathbb R^{n\times n}\), and every nonzero \(b\in\mathbb R^n\), let \(\mathcal K_2(A,b)=\operatorname{span}\{b,Ab\}\). Define
\[
\beta_2(A,b)=\inf_{x\in\mathcal K_2(A,b)\setminus\{0\}}
\frac{\|Ax-b\|_2}{\|A\|_2\|x\|_2}.
\]
Then the exact universal worst-case value is
\[
\sup_{n,A\succeq0,\ A\ne0,\ b\ne0}\beta_2(A,b)
=\frac{\sqrt2-1}{2}.
\]
Equality is attained in dimension three with
\[
A_0=\operatorname{diag}(0,1/\sqrt2,1),\qquad
b_0=((\sqrt2-1)^{1/2},\ 2^{1/4},\ 1)^\top.
\]
The same constant is the supremum when the matrices are restricted to be positive definite, by taking \(A_\varepsilon=\operatorname{diag}(\varepsilon,1/\sqrt2,1)\) and \(\varepsilon\downarrow0\). The theorem is a sharp finite-step guarantee, not a claim about numerical floating-point stability.

## Assumptions and scope
The matrix and vector are finite-dimensional and real, and all calculations are in exact arithmetic. The matrix is positive semidefinite, nonzero; the right-hand side need not belong to its range. The one-sided normwise matrix-only backward error is \(\|Ax-b\|_2/(\|A\|_2\|x\|_2)\). The result concerns the best vector in the second Krylov subspace \(\mathcal K_2\), corresponding to the ideal MINBERR objective; it makes no assertion for an arbitrary computed iterate or a finite-precision implementation. An infimum is used to cover potentially nonattained edge cases. The displayed three-dimensional example attains the infimum at a finite vector.

## Proof
Put \(L=\|A\|_2>0\) and \(B=A/L\). All eigenvalues of \(B\) lie in \([0,1]\). Write
\[
E=\frac{\sqrt2-1}{2},\qquad p(t)=2(1+\sqrt2)-4t.
\]
The polynomial is strictly positive on \([0,1]\), with \(p(1)=2(\sqrt2-1)>0\). The function \(\phi(t)=t-1/p(t)\) is strictly concave because \(\phi''(t)=-32/p(t)^3<0\). It satisfies \(\phi(0)=\phi(1)=-E\), and its sole interior stationary point \(t=1/\sqrt2\) satisfies \(\phi(t)=E\). Consequently \(|t-1/p(t)|\le E\) for every \(t\in[0,1]\). Since \(p(B)\) is invertible and commutes with \(B\), the nonzero trial vector \(x=p(B)b/L\in\mathcal K_2(A,b)\) satisfies
\[
\frac{\|Ax-b\|_2}{L\|x\|_2}
=\frac{\|(Bp(B)-I)b\|_2}{\|p(B)b\|_2}
\le\|B-p(B)^{-1}\|_2\le E.
\]
This proves the universal upper bound, including for singular matrices.

For sharpness, set \(r=\sqrt2\), \(t=1/r\), and use the displayed \(A_0,b_0\). Its three component squared weights are \(w_0=r-1\), \(w_1=r\), \(w_2=1\) at eigenvalues \(0,t,1\). Every vector in \(\mathcal K_2(A_0,b_0)\) is \(x=(aI+cA_0)b_0\) for real coefficients \(a,c\). Define
\[
Q(a,c)=\|A_0(aI+cA_0)b_0-b_0\|_2^2
-E^2\|(aI+cA_0)b_0\|_2^2.
\]
Direct expansion yields the *exact* identity
\[
\begin{split}
Q(a,c)={}&(3-r)(a-a_*)^2+2r(a-a_*)(c+4)\\
&+\frac{3(2+r)}8(c+4)^2,\qquad a_*=2(1+r).
\end{split}
\]
The symmetric coefficient matrix of this quadratic form has leading principal minor \(3-r>0\) and determinant \((3r-4)/8>0\). Thus \(Q(a,c)\ge0\) for all real \(a,c\), with equality only at \((a,c)=(a_*,-4)\). As \(b_0,A_0b_0\) are linearly independent, nonzero coefficient pairs give nonzero vectors. Therefore every admissible nonzero \(x\) has backward error at least \(E\), and the affine polynomial \(p\) attains exactly \(E\). Equality proves the claimed maximum.

To obtain positive-definite examples arbitrarily close to the maximum, replace the zero eigenvalue by \(\varepsilon>0\) while retaining the same \(b_0\). For every fixed \(\delta\in(0,E)\), the quadratic in \((a,c)\) defined by
\[
Q_{\varepsilon,E-\delta}(a,c)=
\|A_\varepsilon(aI+cA_\varepsilon)b_0-b_0\|_2^2
-(E-\delta)^2\|(aI+cA_\varepsilon)b_0\|_2^2
\]
is strictly positive for every \((a,c)\) at \(\varepsilon=0\): it equals \(Q(a,c)+(E^2-(E-\delta)^2)\|(aI+cA_0)b_0\|_2^2\). Its quadratic coefficient matrix is positive definite, and its unconstrained minimum is positive because the norm term vanishes only at \((0,0)\), where \(Q(0,0)=\|b_0\|_2^2>0\). Both properties persist for all sufficiently small positive \(\varepsilon\) by continuity of a quadratic form's coefficients. Hence \(\beta_2(A_\varepsilon,b_0)\ge E-\delta\) eventually. The universal upper bound yields \(\lim_{\varepsilon\downarrow0}\beta_2(A_\varepsilon,b_0)=E\).

## Verification
Running `python verify.py` (with SymPy installed) checks the endpoint and interior-contact identities, the exact quadratic expansion and its positive-definiteness certificate, and equality at the explicit witness. The script additionally runs 3,000 seeded random PSD spectral tests as supplementary checks. The proof of the universal, all-dimensional bound is analytic; those finite tests are not used as proof.

## Relationship to prior work
Dereziński, Nakatsukasa and Rebrova introduce ideal MINBERR and prove the dimension- and condition-independent bound \(3/(k^2-1)\) for \(k\ge2\) (Theorem 9 of arXiv:2604.16075v1), which gives the noninformative value \(1\) at \(k=2\). Their proof already reduces MINBERR to reciprocal-polynomial approximation. Levin and Saff studied approximation of positive functions by polynomial reciprocals and proved two-sided rate estimates; exact low-degree scalar rational-approximation calculations may belong to earlier classical theory, including Binh Lam. The result here is the sharp *algorithmic* second-subspace bound and an explicit finite spectral-weight extremizer realizing it. Neither the general reciprocal-approximation framework alone nor an upper inequality establishes the matching weighted Krylov lower bound without the exhibited certificate.

## Limitations
This is a single sharp early-iteration case; it does not settle optimal constants or extremizers for later subspaces. The extremal semidefinite system is inconsistent, while the positive-definite case attains the same value only as a supremum via a limiting family. The result is for symmetric positive-semidefinite matrices, real arithmetic, spectral norm and the matrix-only normwise backward error. It does not treat nonsymmetric systems, MINBERR-NE, rounding error or implementational stability. An equivalent sharp scalar approximation calculation may have appeared in earlier approximation literature; that possibility is not ruled out by the available materials.

## References
1. M. Dereziński, Y. Nakatsukasa and E. Rebrova, *Towards Universal Convergence of Backward Error in Linear System Solvers*, arXiv:2604.16075v1, first posted 17 April 2026. https://arxiv.org/html/2604.16075v1
2. A. L. Levin and E. B. Saff, *Degree of Approximation of Real Functions by Reciprocals of Real and Complex Polynomials*, SIAM Journal on Mathematical Analysis 19 (1988), 233–245. https://www.math.vanderbilt.edu/saffeb/texts/80.pdf
3. Binh Lam, *A Note on Best Uniform Rational Approximation*, SIAM Journal on Numerical Analysis 13 (1976), 962–965. https://doi.org/10.1137/0713076
