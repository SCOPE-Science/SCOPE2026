# Sharp rank-conditioned contraction frontier for nuclear-scaled polar descent

## Finding

Let \(d,n\ge 1\), let \(1\le r\le\min\{d,n\}\), and let \(H\in\mathbb R^{d\times d}\) be symmetric positive definite with eigenvalues \(0<\lambda_1\le\cdots\le\lambda_d\), counted with multiplicity. For each index \(i\), let \(T_{r,i}\) be \(\lambda_i\) plus the \(r-1\) largest eigenvalues among the indexed multiset \(\{\lambda_j:j\ne i\}\). Let \(T_r\) be the sum of the \(r\) largest eigenvalues. Consider

\[
f(X)=\tfrac12\operatorname{tr}((X-X_*)^{\mathsf T}H(X-X_*)),\quad G=H(X-X_*),\quad X^+=X-\alpha\|G\|_*\operatorname{polar}(G),
\]

where \(\operatorname{polar}(G)=UV^{\mathsf T}\) for any thin singular-value decomposition \(G=U\Sigma V^{\mathsf T}\), and \(\operatorname{polar}(0)=0\). For every \(0<\alpha<2/T_r\), the **exact supremum**, over all \(X\) with \(\operatorname{rank}G=r\), of the objective ratio is

\[
\boxed{\quad q_r(\alpha)=\sup_{\operatorname{rank}G=r}\frac{f(X^+)}{f(X)}
=\max_{1\le i\le d}\left\{1-2\alpha\lambda_i+\alpha^2\lambda_iT_{r,i}\right\}.\quad}
\]

For \(r=1\), the supremum is attained and is exactly the usual sharp gradient-descent factor. For every \(r\ge2\), it is **not attained** by any rank-exactly-\(r\) gradient, but is approached by gradients with one fixed nonzero singular value and \(r-1\) positive singular values tending to zero. At any common admissible step, \(q_{r+1}(\alpha)>q_r(\alpha)\); thus an arbitrarily weak extra singular direction increases the sharp worst-case one-step contraction factor. The function \(q_r\) is strictly convex and has a unique minimizing step in \((0,2/T_r)\), computable from the maximum of \(d\) explicit scalar quadratics.

The strict universal one-step descent range for gradients of rank exactly \(r\) is also sharp: at \(\alpha=2/T_r\) there are rank-\(r\) gradients whose objective is unchanged, and for \(\alpha>2/T_r\) there are rank-\(r\) gradients whose objective increases. If the initial gradient has rank at most \(r\) and \(0<\alpha<2/T_r\), then \(f(X_k)\le q_r(\alpha)^k f(X_0)\): the update preserves the gradient right-factor space, so rank cannot increase. This last bound need not be sharp as a multi-step asymptotic rate.

## Assumptions and scope

All matrices are real and all operations are in exact arithmetic. The curvature acts by left multiplication by the fixed matrix \(H\); no simultaneous right-curvature, noise, momentum, approximate polar factors, or weight decay are assumed. The nuclear norm is the sum of the positive singular values. Repeated eigenvalues are treated as distinct indexed eigenvalue positions when computing \(T_{r,i}\). The step \(\alpha\) is fixed and positive. At \(G=0\), the iteration is stationary. A nonzero rank-\(r\) gradient exists because \(r\le\min\{d,n\}\).

## Proof

**Step 1: exact objective identity.** Write \(G=U\operatorname{diag}(s_1,\ldots,s_r)V^{\mathsf T}\) with all \(s_j>0\), and write \(u_j\) for the columns of \(U\). Set \(S=\sum_j s_j\), \(t=\sum_j u_j^{\mathsf T}Hu_j\), and \(D=\sum_j s_j^2u_j^{\mathsf T}H^{-1}u_j\). Then \(2f(X)=D\), and direct expansion of the quadratic after the update gives

\[
\frac{f(X^+)}{f(X)}=1-\alpha(2-\alpha t)\frac{S^2}{D}.
\]

The Ky Fan maximum principle gives \(t\le T_r\), so the factor \(2-\alpha t\) is positive in the stated step range.

**Step 2: marked-frame spectral assignment lemma.** For any orthonormal \(r\)-frame \((u_1,\ldots,u_r)\), define

\[
J_r=\min_i\lambda_i(2-\alpha T_{r,i}).
\]

For each marked column \(u_k\), one has

\[
\alpha\sum_{j=1}^r u_j^{\mathsf T}Hu_j+J_r u_k^{\mathsf T}H^{-1}u_k\le2.
\]

To prove this, diagonalize \(H\), relabel the marked column first, and complete the frame to an orthogonal \(d\times d\) matrix. Its matrix of entrywise squared coordinates is doubly stochastic. The displayed left-hand side is a linear function of that doubly stochastic matrix. By the Birkhoff–von Neumann theorem it is at most the maximum over permutation matrices. In a permutation, the marked direction is an eigenvector indexed by \(i\); the other \(r-1\) selected indices are distinct from \(i\). Their curvature sum is at most \(T_{r,i}\), and hence the objective is at most \(\alpha T_{r,i}+J_r/\lambda_i\le2\). This proves the lemma, including repeated-eigenvalue cases.

**Step 3: exact supremum and nonattainment.** Let \(d_{\max}=\max_j u_j^{\mathsf T}H^{-1}u_j\) and mark a maximizing column. Since

\[
D\le d_{\max}\sum_j s_j^2\le d_{\max}S^2,
\]

Step 1 and the lemma give

\[
\frac{f(X^+)}{f(X)}\le1-\frac{\alpha(2-\alpha t)}{d_{\max}}\le1-\alpha J_r=q_r(\alpha).
\]

Choose an index \(i\) attaining the minimum in \(J_r\), and form an eigenframe using index \(i\) and the \(r-1\) largest other eigenvalues. Set its singular values to \((1,\varepsilon,\ldots,\varepsilon)\) with \(\varepsilon>0\). In the exact identity, the quotient of squared singular sums tends to \(\lambda_i\) as \(\varepsilon\downarrow0\), while \(t=T_{r,i}\). Thus the ratios tend to \(q_r\), establishing sharpness. For \(r>1\), the strict inequality \(\sum_j s_j^2<S^2\) holds for all positive singular values, making the supremum unattained. For \(r=1\), the eigenvector construction attains it exactly.

**Step 4: rank and tuning.** Adding another selected eigenvalue strictly increases every \(T_{r,i}\), so at any step admissible for both ranks every displayed branch of \(q_{r+1}\) strictly exceeds the corresponding branch of \(q_r\). In particular \(q_{r+1}>q_r\). Each branch is a strictly convex quadratic with second derivative \(2\lambda_iT_{r,i}>0\); their maximum is strictly convex because they share a positive uniform strong-convexity constant. Its right derivative at zero equals \(-2\lambda_1<0\). At \(\alpha=2/T_r\), a branch indexed by an eigenvalue in the top-\(r\) set has value \(1\). Thus the unique minimum is interior. The strict-descent threshold and its boundary follow from the exact identity by taking an eigenframe spanning the top \(r\) eigenvectors, for which \(t=T_r\), and any positive singular values. For completeness, \(X^+-X_*=\big(H^{-1}U\Sigma-\alpha S U\big)V^{\mathsf T}\), so \(\operatorname{rank}G^+\le\operatorname{rank}G\). This rank-monotonicity property is also in Shulgin et al., Proposition 9, and is not claimed as new. The all-iterates claim follows from the same bound for each rank at most \(r\) and the monotonicity just established.

## Verification

The standalone program `verify.py` uses exact rational arithmetic to test the marked-frame permutation inequality on exhaustively enumerated permutation vertices for multiple spectra, including repeated eigenvalues. It tests the rank-\(r\) singular-value collapse witness, rank monotonicity, the sharp stability boundary, and an explicit three-eigenvalue example. Separately, randomized SPD rotations and rectangular singular-vector frames reconstruct both the actual quadratic objective ratio and its analytic formula. Executing `python verify.py` produces `PASS: 56010 exact assignment/witness and numeric reconstruction checks`. The finite checks are corroboration, not a proof of the universal statement; the proof above supplies the needed all-dimension arguments.

As an explicit comparison, for \(H=\operatorname{diag}(1,10,11)\), \(r=2\), and \(\alpha=2/25\), the new sharp factor is \(573/625=0.9168\); replacing the marked eigenvalue sum by the global top-two trace gives only \(609/625=0.9744\). The rank-conditioned optimum for this spectrum is \(\alpha=1/12\), with factor \(11/12\).

## Relationship to prior work

Jawanpuria, Garai and Mishra (arXiv:2610.27747v1, October 20, 2026) establish the exact quadratic one-step loss identity, constant-step convergence under a top-eigenvalue trace condition, and sharpness of the convergence threshold by invariant eigenspaces. Their Appendix C does not compute the exact all-spectrum rank-conditioned worst-case *one-step objective ratio* or identify its nonattained thin-spectrum extremizers. The present result takes the published identity as a starting point and solves the remaining marked-direction orthogonal-frame extremal problem with a Birkhoff assignment argument; the proof does not claim the identity or the trace threshold as new.

Lau, Long and Su (arXiv:2505.21799v4, original public version May 27, 2025) introduce the nuclear-scaled PolarGrad update and general smooth/Polyak–Łojasiewicz convergence estimates. Their update and rank-based sufficient rates are prior; no exact anisotropic Hessian eigenvalue envelope of the form above was located in the inspected convergence and supplementary sections. Shulgin, Laing, Orvieto and Richtárik (arXiv:2610.30280, October 21, 2026) give the exact full-row-rank, exact-line-search progress coefficient and its sharp almost-rank-one limit (Theorem 3 and Appendix E.2), the rank-deficient projector bound (Appendix E.6, Corollary 2), and rank nonincrease (Proposition 9). In particular, the full-rank case \(r=d\) of the present envelope agrees with their previously known sharp bound; the rank-one case is ordinary gradient descent. Neither boundary is claimed new. Their rank-deficient bound separates smallest curvature from active-subspace trace, but does not provide the coupled eigenvalue assignment or sharp intermediate-rank \(1<r<d\) frontier here. The Birkhoff–von Neumann and Ky Fan inequalities are classical and are used, not claimed as new. A broader earlier variational inequality could imply this special frontier, so priority remains subject to further bibliographic verification.

## Limitations

This is a worst-case one-step objective theorem, not a statement that a single trajectory achieves its worst-case ratio repeatedly. For ranks above one the sharp ratio is only a supremum approached by ill-conditioned gradients; a nonzero lower bound on the smallest singular value can improve it. The result does not prove convergence for all steps above the strict one-step descent boundary, nor quantify stochastic, approximate-polar, or practical training performance. It assumes a fixed SPD left-curvature quadratic and exact arithmetic. An independent mathematical audit has not been performed.

## References

- P. Jawanpuria, B. Garai, and B. Mishra, *Constant Step Sizes for Muon-Type Spectral Optimizers on Strongly Convex Quadratics*, arXiv:2610.27747v1 (first public October 20, 2026), https://arxiv.org/html/2610.27747v1 . See Theorem 3, Appendix C, equation (8), Proposition 8, and Remark 2.
- E. Shulgin, S. Laing, A. Orvieto, and P. Richtárik, *A Quadratic Lens on Muon’s Polar Update: Benefits, Pitfalls, and the Role of Newton–Schulz*, arXiv:2610.30280 (first public October 21, 2026), https://arxiv.org/abs/2610.30280 . See Theorem 3, Appendix E.2 and E.6, and Proposition 9.
- T. T.-K. Lau, Q. Long, and W. Su, *PolarGrad: A Class of Matrix-Gradient Optimizers from a Unifying Preconditioning Perspective*, arXiv:2505.21799v4 (first public May 27, 2025), https://arxiv.org/html/2505.21799v4 . See Sections 3.3, 3.5 and the supplementary PolarGrad sections.
- G. Birkhoff, *Tres observaciones sobre el álgebra lineal*, Univ. Nac. Tucumán Revista A **5** (1946), 147–151 (doubly stochastic matrix vertices); J. von Neumann's earlier matching formulation.
- K. Fan, *On a theorem of Weyl concerning eigenvalues of linear transformations I*, Proc. Natl. Acad. Sci. USA **35** (1949), 652–655 (trace extremal principle).
