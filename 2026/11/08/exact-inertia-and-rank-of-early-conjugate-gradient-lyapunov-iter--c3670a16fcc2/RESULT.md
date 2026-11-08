# Exact inertia and rank of early conjugate-gradient Lyapunov iterates

## Finding

Let \(A\in\mathbb R^{n\times n}\) be symmetric positive definite and let \(0\ne b\in\mathbb R^n\). For the exact-arithmetic, unpreconditioned, Frobenius-inner-product matrix conjugate-gradient method initialized at \(X_0=0\) on
\[
\mathcal L_A(X)=AX+XA=bb^\mathsf T,
\]
let \(r\) be the number of distinct eigenvalues of \(A\) on which \(b\) has a nonzero spectral projection. For **every** integer \(1\le k\le r\), the \(k\)-th approximate solution has the *exact* inertia
\[
\boxed{\operatorname{In}(X_k)=\left(\left\lceil\frac{k}{2}\right\rceil,\left\lfloor\frac{k}{2}\right\rfloor,n-k\right),}
\]
where the entries count strictly positive, strictly negative, and zero eigenvalues. In particular, \(\operatorname{rank}(X_k)=k\), and for \(r\ge2\), **every** \(X_k\) with \(2\le k\le r\) is indefinite, although the unique exact solution is positive semidefinite with inertia \((r,0,n-r)\). Neither eigenvalue spacing nor conditioning changes this inertia law.

## Assumptions and scope

All matrices and arithmetic are real and exact. The algorithm is ordinary CG on the self-adjoint positive-definite operator \(\mathcal L_A\), acting on real matrices with \(\langle U,V\rangle_F=\operatorname{tr}(U^\mathsf T V)\), initialized with \(X_0=0\), residual \(R_0=bb^\mathsf T\), and search direction \(P_0=R_0\). At iteration \(k\ge1\), with \(\rho_{k-1}=\langle R_{k-1},R_{k-1}\rangle_F\), use
\[
\alpha_k=\frac{\rho_{k-1}}{\langle P_{k-1},\mathcal L_A(P_{k-1})\rangle_F},\quad
X_k=X_{k-1}+\alpha_kP_{k-1},\quad
R_k=R_{k-1}-\alpha_k\mathcal L_A(P_{k-1}),
\]
followed, if \(R_k\ne0\), by \(\beta_k=\|R_k\|_F^2/\rho_{k-1}\) and \(P_k=R_k+\beta_kP_{k-1}\). There is no truncation, reorthogonalization, projection to the positive cone, or preconditioning. Repeated eigenvalues of \(A\) are allowed, and \(b\) may be orthogonal to some eigenspaces. The theorem describes the first \(r\) approximate solutions only; it makes no inertia claim at later, nonterminal iterations.

## Proof

**1. Active eigenspaces and nonbreakdown.** Let \(0<\lambda_1<\cdots<\lambda_r\) be the distinct active eigenvalues. Write \(b_i=E_{\lambda_i}b\ne0\) for their mutually orthogonal spectral components and set \(B=[b_1\ \cdots\ b_r]\), which has full column rank. The matrix \(bb^\mathsf T\) has a nonzero spectral component for every unordered pair \((i,j)\) under \(\mathcal L_A\), at spectral value \(\lambda_i+\lambda_j\). In particular, the strictly ordered chain
\[
2\lambda_1<\lambda_1+\lambda_2<\cdots<\lambda_1+\lambda_r
<\lambda_2+\lambda_r<\cdots<2\lambda_r
\]
has \(2r-1\) distinct active operator eigenvalues (for \(r=1\), one). Consequently, the Krylov dimension is at least \(r\) and exact CG cannot terminate before its \(r\)-th step. All required denominators are positive.

**2. The CG solution polynomial has a fixed alternating leading sign.** Standard CG recurrences imply \(X_k=q_{k-1}(\mathcal L_A)(bb^\mathsf T)\) for a real polynomial \(q_{k-1}\) of degree at most \(k-1\). The degree is *exactly* \(k-1\), with leading coefficient
\[
\gamma_{k-1}=(-1)^{k-1}\prod_{j=1}^{k}\alpha_j
\]
This follows by induction: \(R_0=P_0=bb^\mathsf T\), each \(R_k=R_{k-1}-\alpha_k\mathcal L_A(P_{k-1})\) acquires a nonzero degree-\(k\) leading term, and adding the lower-degree \(\beta_kP_{k-1}\) does not cancel it. Since every \(\alpha_j>0\), the sign of \(\gamma_{k-1}\) is \((-1)^{k-1}\).

**3. Exact inertia of every polynomial sum kernel.** For any real polynomial \(q(s)=\sum_{m=0}^{d}c_ms^m\) of exact degree \(d\), and any distinct real numbers \(\lambda_1,\ldots,\lambda_r\) with \(r\ge d+1\), let \(K_{ij}=q(\lambda_i+\lambda_j)\). The \(r\times(d+1)\) Vandermonde matrix \(V_{ia}=\lambda_i^a\), \(0\le a\le d\), has full column rank, and
\[
K=VCV^\mathsf T,\qquad
C_{ab}=\begin{cases}\binom{a+b}{a}c_{a+b},&a+b\le d,\\0,&a+b>d.\end{cases}
\]
The symmetric matrix \(C\) is anti-triangular and has
\[
\det C=(-1)^{d(d+1)/2}c_d^{d+1}\prod_{a=0}^{d}\binom da\ne0.
\]
Continuously scale \(c_0,\ldots,c_{d-1}\) to zero while keeping \(c_d\) fixed. The same determinant formula remains nonzero throughout, so inertia is unchanged. At the endpoint, \(C\) is anti-diagonal with \(C_{a,d-a}=\binom da c_d\): each off-central paired block contributes one positive and one negative eigenvalue, while for even \(d\), the central eigenvalue has the sign of \(c_d\). Sylvester congruence and full column rank of \(V\) transfer the inertia of \(C\) to \(K\), adding \(r-d-1\) zeros.

**4. Transfer to the matrix CG iterates.** Spectral calculus gives
\[
X_k=B K^{(k)}B^\mathsf T,\qquad K^{(k)}_{ij}=q_{k-1}(\lambda_i+\lambda_j).
\]
Since \(B\) has full column rank, it preserves the nonzero inertia of \(K^{(k)}\) and adds \(n-r\) zero eigenvalues. Set \(d=k-1\). If \(k\) is even, \(d\) is odd and the nonzero eigenvalues split equally into positive and negative. If \(k\) is odd, \(d\) is even and \(c_d=\gamma_d>0\), so there is one additional positive eigenvalue. This proves the displayed inertia and exact rank for all \(1\le k\le r\).

**5. Contrast with the true solution.** The unique solution is
\[
X_\star=\int_0^\infty e^{-tA}bb^\mathsf T e^{-tA}\,dt.
\]
Its quadratic form is the integral of \((\sum_{i=1}^r e^{-\lambda_it}u^\mathsf Tb_i)^2\), which vanishes precisely when \(u\) is orthogonal to all \(b_i\), by linear independence of distinct real exponentials. Thus \(X_\star\) has inertia \((r,0,n-r)\). For \(r\ge2\), this establishes unavoidable early nonpositivity of the standard CG approximations despite a positive semidefinite exact solution.

## Verification

Run `python verify_inertia.py` using Python 3 and SymPy. It constructs the actual unpreconditioned CG iterates in exact rational arithmetic for positive diagonal matrices with distinct rational eigenvalues and nonzero rational right-hand-side coordinates, then checks exact matrix inertia with characteristic-polynomial real-root isolation. Independent antitriangular determinant and polynomial-kernel tests are included. The checks passed for 68 specified instances/assertion groups; all dimensions are finite and the infinitely quantified conclusion rests on the proof above, not on these checks. The script was executed after extraction from the final package.

## Relationship to prior work

Lungová and Plešinger, *On bounds for rank growth of iterands in conjugate gradients for Lyapunov equation* (arXiv:2609.39308v1, September 30, 2026), study this same exact matrix CG scheme, prove \(\operatorname{rank}(X_k)\le\dim\mathcal K_k(A,b)\) and give the active-eigenvalue rank cap, but do not establish the matching lower rank or a positive/negative inertia count. Their work motivates the exact early-iteration question. Kressner, Lund, Massei and Palitta (2020/2021) analyze **different** projected/restarted Krylov methods and discuss positive semidefinite approximations and occasional indefinite corrections; this does not imply universal negative-eigenvalue counts for unpreconditioned matrix CG. Sun and Liu (2020) propose cone-constrained splitting methods instead of this unconstrained CG recurrence. Classical CG polynomial and Vandermonde facts are used explicitly and are not claimed as new. Historical text-access limits and any unindexed earlier equivalent statement remain originality risks.

## Limitations

The inertia result is exact-arithmetic and first-\(r\)-iterate only. It need not hold with finite-precision rank truncation, constrained positive semidefinite projection, preconditioning, other CG-type methods, nonsymmetric \(A\), indefinite \(A\), or higher-rank right-hand sides. It does not bound the magnitudes of negative eigenvalues or the error of a subsequent positive-semidefinite projection. It does not claim that all later CG iterates are indefinite: final exact CG convergence yields a positive semidefinite solution.

## References

1. J. Lungová and M. Plešinger, *On bounds for rank growth of iterands in conjugate gradients for Lyapunov equation*, arXiv:2609.39308v1, 2026-09-30. https://arxiv.org/html/2609.39308
2. D. Kressner, K. Lund, S. Massei and D. Palitta, *Compress-and-restart block Krylov subspace methods for Sylvester matrix equations*, Numerical Linear Algebra with Applications 28 (2021), e2339; online 2020-10-13. https://doi.org/10.1002/nla.2339
3. M. Sun and J. Liu, *Iterative Algorithms for Symmetric Positive Semidefinite Solutions of the Lyapunov Matrix Equations*, Mathematical Problems in Engineering (2020), article 6968402. https://doi.org/10.1155/2020/6968402
4. M. Hochbruck and G. Starke, *Preconditioned Krylov subspace methods for Lyapunov matrix equations*, SIAM Journal on Matrix Analysis and Applications 16 (1995), 156–171. https://doi.org/10.1137/S0895479892239238
