# A sharp endpoint-to-interior loading transition for spectral conditioning of a four-site diffusion path

## Finding

For the unweighted four-vertex path with Laplacian \(L\), let \(\mu>0\) and \(B>0\). Among **all** independently chosen nonnegative vertex loadings \(d_i\) satisfying \(d_1+d_2+d_3+d_4=B\), minimize the ordinary spectral condition number of
\[
A(d)=\mu I_4+L+\operatorname{diag}(d_1,d_2,d_3,d_4),\qquad
L=\begin{pmatrix}1&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&1\end{pmatrix}.
\]

The unique global minimizer is reflection-symmetric, \(d^*=(x,y,y,x)\). Put \(q=B/4\), \(m=\mu+1+q\), \(a(t)=\sqrt{1+t^2}\), \(b(t)=\sqrt{1+(1-t)^2}\), and define
\[
F_{\mu,q}(t)=\frac{t}{a(t)[m-a(t)]}
-\frac{1-t}{b(t)[m+1+b(t)]}.
\]
There is a unique \(q_c(\mu)\in(0,1/2)\) characterized by \(F_{\mu,q_c}(q_c)=0\), and \(B_c(\mu)=4q_c(\mu)\). Precisely:

- For \(0<B\le B_c(\mu)\), the unique optimum is \(d^*=(B/2,0,0,B/2)\).
- For \(B>B_c(\mu)\), the unique optimum is \(d^*=(q+t_*,q-t_*,q-t_*,q+t_*)\), where \(t_*\in(0,\min\{q,1/2\})\) is the unique solution of \(F_{\mu,q}(t_*)=0\).

The exact optimal condition number in both regimes is
\[
\kappa_*=\frac{m+1+b(t_*)}{m-a(t_*)},
\]
where \(t_*=q\) in the first regime. For fixed \(\mu\), the optimum contrast \(x-y=2t_*\) increases strictly with \(B\) once the interior sites activate, and tends to \(1\) as \(B\to\infty\). The threshold obeys \(B_c(\mu)\to2\) as \(\mu\to\infty\) and \(B_c(\mu)\sim4\mu/(1+2\sqrt2)\) as \(\mu\downarrow0\).

## Assumptions and scope

All edges have unit positive conductance, all four vertex masses are one, and \(\mu>0\), \(B>0\) are real. Every \(d_i\) is independently feasible subject only to nonnegativity and the budget. This is **additive diagonal loading**, not multiplicative Jacobi preconditioning. The condition number is \(\kappa_2(A)=\lambda_{\max}(A)/\lambda_{\min}(A)\). The matrix is symmetric positive definite because \(\mu>0\), and this theorem claims exactly the global minimizer and its condition number, not optimality for every larger path or different cost weighting.

## Proof

**1. Reduction to reflection symmetry, with strict uniqueness.** Let \(R\) reverse the four coordinates, and let \(\bar A=(A+RAR)/2\). The nonnegative diagonal budget is preserved. By the max/min eigenvalue variational principles,
\[
\lambda_{\max}(\bar A)\le\lambda_{\max}(A),\qquad
\lambda_{\min}(\bar A)\ge\lambda_{\min}(A).
\]
Thus symmetrization never increases condition number. Equality is impossible for a nonsymmetric loading: the minimum-eigenvalue eigenvector \(v\) of \(\bar A\) is strictly positive and unique up to scale because \(\bar A\) is an irreducible Stieltjes matrix. Its positivity follows, for example, by Perron--Frobenius applied to the strictly positive inverse \(\bar A^{-1}\). The positive vector is invariant under reflection. Hence \(v^TAv=v^T\bar A v=\lambda_{\min}(\bar A)\) for unit \(v\). If \(\lambda_{\min}(A)=\lambda_{\min}(\bar A)\), equality in Rayleigh--Ritz would make \(v\) an eigenvector of \(A\). But \((A-\bar A)v\ne0\) whenever any reflection-paired loads differ, since each entry of \(v\) is positive. Contradiction. Therefore \(\lambda_{\min}(A)<\lambda_{\min}(\bar A)\) and \(\kappa_2(A)>\kappa_2(\bar A)\) whenever \(d\) is not reflection-symmetric.

**2. Four eigenvalues from two parity blocks.** Write \(d=(q+t,q-t,q-t,q+t)\) with \(-q\le t\le q\). The reflection-even and reflection-odd subspaces block-diagonalize \(A\) into
\[
S(t)=\begin{pmatrix}m+t&-1\\-1&m-t\end{pmatrix},\qquad
T(t)=\begin{pmatrix}m+t&-1\\-1&m+2-t\end{pmatrix}.
\]
Their eigenvalues are respectively \(m\pm a(t)\) and \(m+1\pm b(t)\). Because \(T-S=\operatorname{diag}(0,2)\) is positive semidefinite, the smallest eigenvalue belongs to \(S\) and the largest to \(T\):
\[
\lambda_{\min}(A)=m-a(t)>0,\quad
\lambda_{\max}(A)=m+1+b(t),\quad
K_{\mu,q}(t)=\frac{m+1+b(t)}{m-a(t)}.
\]
Positivity of the denominator follows from \(m\ge\mu+1+q>\sqrt{1+q^2}\ge a(t)\).

**3. Unique fixed-budget optimizer.** Direct differentiation gives \(d\log K_{\mu,q}(t)/dt=F_{\mu,q}(t)\). It is negative for \(t\le0\), positive for \(t\ge1\), and positive at \(t=1/2\), since there \(a=b\) and \(m-a<m+1+b\). On \(0<t<1/2\), the first summand of \(F\) is strictly increasing: \(t/a(t)\) increases and \(m-a(t)\) decreases. The second positive quantity being subtracted is strictly decreasing: writing \(s=1-t\) and \(M=m+1\), the derivative of \(s/[\sqrt{1+s^2}(M+\sqrt{1+s^2})]\) with respect to \(s\) has the sign of \(M+\sqrt{1+s^2}(1-s^2)>0\) for \(0<s<1\). Hence \(F\) crosses zero exactly once in \((0,1/2)\), starting with \(F(0)<0\). Constraining \(t\in[-q,q]\), the optimizer is \(t=q\) if \(F(q)\le0\); otherwise it is the unique root \(t_*\in(0,\min\{q,1/2\})\). Strict decrease then strict increase of \(K\) proves uniqueness.

**4. Exactly one budget activation threshold.** At the boundary \(t=q\), put \(\alpha=\sqrt{1+q^2}\), \(\beta=\sqrt{1+(1-q)^2}\) and split \(F(q)=f(q)-g(q)\), where
\[
f(q)=\frac{q}{\alpha(\mu+1+q-\alpha)},\quad
g(q)=\frac{1-q}{\beta(\mu+2+q+\beta)}.
\]
For \(0<q<1/2\), \(f(q)\) is strictly increasing. Indeed, with \(h(q)=1+q-\alpha\),
\[
f(q)=\frac{1+q+\alpha}{2\alpha}\,\frac{h(q)}{h(q)+\mu},
\]
and both positive factors strictly increase because the derivative of the first is \((1-q)/[2(1+q^2)^{3/2}]>0\), while \(h'(q)=1-q/\alpha>0\). Meanwhile \(g(q)\) strictly decreases: its numerator-to-\(\beta\) factor increases with \(s=1-q\), while its other denominator \(\mu+2+q+\beta\) increases with \(q\) on this range. Also \(f(0)=0<g(0)\); at \(q=1/2\), \(\alpha=\beta\), and the positive first fraction exceeds the second since \(\mu+1+q-\alpha<\mu+2+q+\beta\). Thus exactly one \(q_c\in(0,1/2)\) satisfies equality. For \(q\ge1/2\) the feasible set contains \(t=1/2\), so an interior optimum always exists.

**5. Monotonic contrast and limiting cases.** For \(q>q_c\), at fixed \(t\in(0,1/2)\) the ratio of the first and second derivative terms is strictly decreasing in \(m=\mu+1+q\), since its logarithmic derivative with respect to \(m\) is
\[
\frac1{m+1+b(t)}-\frac1{m-a(t)}<0.
\]
As the ratio is strictly increasing in \(t\), its root \(t_*\) increases strictly with budget. After dividing the equality by the common large scale \(m\), its limit is \(t/a(t)=(1-t)/b(t)\), whose unique solution is \(t=1/2\). Hence \(x-y=2t_*\uparrow1\). For fixed \(q\in(0,1/2)\), as \(\mu\to\infty\) the critical equality reduces to \(q/\alpha=(1-q)/\beta\), implying \(q_c\to1/2\), or \(B_c\to2\). As \(\mu\downarrow0\), the critical equation forces \(q_c\to0\); here \(f(q)=q/(\mu+q+O(q^2))\) and \(g(q)\to1/[\sqrt2(2+\sqrt2)]\), yielding \(q_c\sim\mu/(1+2\sqrt2)\) and the claimed small-\(\mu\) asymptotic.

## Verification

Run the standalone `CHECKER.py` with Python and installed SymPy, NumPy and SciPy dependencies. It checks six exact symbolic identities, 6,000 independently sampled nonnegative diagonal allocations against the analytical optimizer, 60 fixed-budget scalar optimization comparisons, seven numerical root-bracket checks for the activation threshold, and two reference checks. The numerical tests are corroboration, not the general uniqueness proof. For \(\mu=1\), the threshold is \(B_c\approx0.669854112318303\). At \(B=1\), the unique optimum is approximately \((0.42542745718,0.07457254282,0.07457254282,0.42542745718)\) and \(\kappa_*\approx3.68187390675\).

## Relationship to prior work

Lu and Pong (2011) treat general spectral condition-number minimization over convex feasible sets and provide convex optimization machinery. That general framework contains the present feasible-set family, but the inspected full text supplies neither the explicit four-path even/odd eigenvalue reduction nor the endpoint-to-interior budget cutoff and uniqueness classification. Torres and Roy (2015) optimize one dominant eigenvalue under trace-preserving diagonal perturbations, a different objective from a ratio of both extreme eigenvalues. The literature on maximum pinned-consensus decay optimizes the smallest eigenvalue alone. Generic algorithms or lower-dimensional star allocations do not give the four-path critical equation or its globally strict symmetry certificate without additional analysis.

## Limitations

The result is exact for the four-vertex unit-weight path, uniform baseline \(\mu I\), equal loading prices and additive nonnegative diagonal controls. No claim is made for arbitrary path lengths, heterogeneous costs or masses, or multiplicative diagonal scaling. The critical budget is characterized implicitly by a unique scalar root rather than elementary radicals. Numerical checker output does not substitute for the analytic proof. The source comparison is not an exhaustive priority determination; a plausible older diagonal-perturbation paper was available only at abstract level.

## References

1. Z. Lu and T. K. Pong, *Minimizing Condition Number via Convex Programming*, SIAM J. Matrix Anal. Appl. **32** (2011), 1193–1211. DOI: https://doi.org/10.1137/100795097 . Online 2011-11-01; full author-provided text https://www.researchgate.net/publication/220656493_Minimizing_Condition_Number_via_Convex_Programming .
2. M. Maréchal and J. Ye, *Optimizing Condition Numbers*, SIAM J. Optimization (2009). DOI: https://doi.org/10.1137/080740544 .
3. J. A. Torres and S. Roy, *Dominant Eigenvalue Minimization with Trace Preserving Diagonal Perturbation: Subset Design Problem*, IEEE CDC (2015), 4208–4213. DOI: https://doi.org/10.1109/CDC.2015.7402875 .
4. P. van den Driessche, *Dominant Eigenvalues under Trace-Preserving Diagonal Perturbations*, Linear Algebra Appl. (1994). DOI: https://doi.org/10.1016/0024-3795(94)90415-4 .
