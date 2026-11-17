# Exact two-mode coordinate memory and monotone transport variance for quadratic beta maps

## Finding

For each integer \(m\ge1\), define the quadratic Parry base and its greedy map by
\[
\beta_m=\frac{m+\sqrt{m^2+4}}2,\qquad
T_\beta(x)=\beta x-\lfloor\beta x\rfloor\quad (0\le x<1).
\]
Let \(X_0\) have the unique absolutely continuous invariant probability law of \(T_\beta\), and let \(X_n=T_\beta^n(X_0)\) for all integer \(n\ge0\). For every such \(n\),
\[
C_n:=\operatorname{Cov}(X_0,X_n)
=A(\beta)\beta^{-n}+B(\beta)(-\beta^{-2})^n,
\]
where, writing \(b=\beta\),
\[
 A(b)=\frac{b^4-3b^3+6b^2-3b+1}{12b^2(b^2+1)},
 \qquad B(b)=\frac{(b-1)^2(b^2+b+1)}{4b(b^2+1)^2}.
\]
Both coefficients are positive; indeed \(C_n>0\) for all \(n\ge0\), including odd lags when the second mode is negative. The transfer operator has a further eigenvalue \(-\beta^{-3}\) on the relevant four-dimensional invariant space, but it has **zero projection onto these coordinate correlations**.

For the stationary coordinate sum \(S_N=\sum_{j=0}^{N-1}X_j\), every integer \(N\ge1\) satisfies
\[
\operatorname{Var}(S_N)=NC_0+2\sum_{k=1}^{N-1}(N-k)
\left[A(\beta)\beta^{-k}+B(\beta)(-\beta^{-2})^k\right].
\]
Consequently the normalized long-run variance exists and has the closed form
\[
V_m=\lim_{N\to\infty}\frac{\operatorname{Var}(S_N)}N
=\frac{(\beta+1)(\beta^8-\beta^6+8\beta^4-\beta^2+1)}{12\beta^2(\beta-1)(\beta^2+1)^3}.
\]
It is **strictly decreasing** as \(m=1,2,\ldots\) increases, and \(V_m\to1/12\) as \(m\to\infty\). In particular, increasing expansion strength reduces long-time coordinate-sum variance despite the presence of two decay modes.

## Assumptions and scope

The parameter \(m\) is a positive integer, so \(\beta>1\) solves \(\beta^2=m\beta+1\). This is the deterministic greedy beta map, not random mixing of maps. The stationary initialization is essential for the covariance and variance formulas; claims do not apply without adjustment to an arbitrary initial distribution. All equalities are with respect to the unique absolutely continuous invariant measure; endpoints of half-open branches do not affect these measures. No central limit theorem is claimed.

## Proof

**Invariant density and four-dimensional exact action.** Set \(b=\beta\), \(I=[0,b^{-1})\), and \(k=b^2/(b^2+1)\). By \(b=m+b^{-1}\), the map has \(m\) full affine inverse branches and one remaining branch on \(I\). Its Perron–Frobenius operator \(\mathcal P\) therefore preserves
\[
\mathcal V=\operatorname{span}\{1,\mathbf1_I,x,x\mathbf1_I\}.
\]
Relative to the displayed basis, a column of coefficients is multiplied by
\[
M=\begin{pmatrix}
 m/b&1/b&m(m-1)/(2b^2)&0\\
 1/b&0&m/b^2&0\\
 0&0&m/b^2&1/b^2\\
 0&0&1/b^2&0
\end{pmatrix}.
\]
This follows by evaluating the \(m\) complete preimages \((x+j)/b\) for \(0\le j<m\) and the final preimage \((x+m)/b\) on \(I\), including the \(1/b\) Jacobian. The vector \(h=(k,k/b,0,0)^\mathsf T\) is fixed by \(M\), and its density
\[
h_b(x)=k\bigl(1+b^{-1}\mathbf1_I(x)\bigr)
\]
integrates to one. Standard uniqueness of the absolutely continuous invariant measure of the greedy beta map identifies it as the stationary density. Multiplication by \(x\) gives the starting vector \(q=(0,0,k,k/b)^\mathsf T\), which represents \(x h_b\).

**Exact lag calculation.** Define row functionals for any \(f\in\mathcal V\) by
\[
L_0=(1,b^{-1},1/2,(2b^2)^{-1}),\qquad
L_1=(1/2,(2b^2)^{-1},1/3,(3b^3)^{-1}).
\]
These are respectively \(\int_0^1 f(x)\,dx\) and \(\int_0^1 xf(x)\,dx\). The stationary mean is
\[
\mu=L_0q=\frac{(b+1)(b^2-b+1)}{2b(b^2+1)}.
\]
Transfer duality gives, for every integer \(n\ge0\),
\[
C_n=L_1M^nq-\mu^2.
\]
The four eigenvalues of \(M\) are the distinct numbers \(1\), \(b^{-1}\), \(-b^{-2}\), \(-b^{-3}\); equivalently
\[
\det(tI-M)=(t-1)(t-b^{-1})(t+b^{-2})(t+b^{-3}).
\]
The constant mode cancels after centering, so \(C_n\) is a linear combination of the three nonunit eigenmode powers. Direct exact integration yields
\[
C_0=\frac{b^6+4b^4-6b^3+4b^2+1}{12b^2(b^2+1)^2},
\quad
C_1=\frac{b^6-3b^5+4b^4-3b^3+7b^2-2}{12b^3(b^2+1)^2}.
\]
The third computed moment \(C_2=L_1M^2q-\mu^2\) obeys the exact identity
\[
C_2=(b^{-1}-b^{-2})C_1+b^{-3}C_0.
\]
Since \(-b^{-3}\) differs from both \(b^{-1}\) and \(-b^{-2}\), this identity forces the coefficient of the third nonunit eigenmode to vanish. Solving the two equations at \(n=0,1\) yields exactly the stated \(A(b),B(b)\), proving the two-mode identity at **every** lag without extrapolating finite experiments.

**Positive correlations.** Both \(A(b),B(b)>0\) for \(b>1\): the numerator of \(A\), after substituting \(b=1+t\), is \(t^4+t^3+3t^2+4t+2>0\). The more stringent condition
\[
A(b)b-B(b)=\frac{b^6-3b^5+4b^4-3b^3+7b^2-2}{12b(b^2+1)^2}>0
\]
holds because its numerator becomes \(t^6+3t^5+4t^4+3t^3+7t^2+12t+4\) for \(t=b-1>0\). Thus the negative mode at odd \(n\ge1\) cannot dominate the positive mode, and all \(C_n>0\).

**Long-run variance and strict monotonicity.** Stationarity gives the finite-window sum above. Both decay bases have absolute value below one, hence summation gives
\[
V(b)=A(b)\frac{b+1}{b-1}+B(b)\frac{b^2-1}{b^2+1}.
\]
Simplifying gives the claimed rational function. Its derivative is exactly
\[
V'(b)=-\frac{Q(b)}{6b^3(b-1)^2(b^2+1)^4},
\]
with
\[
Q(b)=b^{11}-4b^{10}+22b^8+7b^7-29b^6+7b^5+15b^4-3b^2+b-1.
\]
A direct binomial expansion at \(b=1+t\) yields
\[
Q(1+t)=t^{11}+7t^{10}+15t^9+7t^8+33t^7+258t^6+666t^5+890t^4+712t^3+360t^2+112t+16.
\]
Every coefficient is strictly positive and \(t>0\), so \(V'(b)<0\) throughout \(b>1\). The sequence \(\beta_m\) increases strictly with \(m\), proving strict decrease of \(V_m\). Taking \(b\to\infty\) in the rational expression gives \(1/12\). This completes the proof.

## Verification

The standalone symbolic script `check.py` constructs the exact transfer matrix and integration functionals, checks invariance, normalizations, characteristic polynomial, low-lag identities, disappearance of the third mode, the closed Green–Kubo expression, and the derivative factorization. These checks use symbolic rational functions in \(b\), not a finite sample of parameter choices; the written transfer-operator derivation and polynomial positivity arguments establish the unrestricted integer-family theorem.

Run from the extracted directory with `python check.py` and SymPy installed. No additional data files are required.

## Relationship to prior work

Rényi (1957) and Parry (1960) establish the deterministic beta-map invariant-density framework; the stationary density here is not claimed as new. Suzuki (2023, arXiv:2303.17521) derives invariant densities and linear response for random beta transformations, with deterministic maps as components. Cornean and Sørensen (2025, arXiv:2502.17113) explicitly construct the very same four-dimensional piecewise-affine transfer-operator invariant space for quadratic Parry bases, derive its eigenvalues, and prove iteration asymptotics. Their invariant-space construction is prior work, **not** an independent new contribution here. The present claim consists of the coordinate-observable cancellation, exact all-lag covariance coefficients, and strictly monotone long-run variance across the integral quadratic family; these particular quantified formulas and parameter ordering were not found in the full texts inspected. They are algebraically derivable from the earlier transfer framework, a material limitation on originality and mathematical scope.

## Limitations

The theorem concerns coordinate sums in the one-parameter deterministic quadratic-base subfamily only. It establishes a long-run variance rate, not a functional central limit theorem or a large-deviation law. It does not assert an originality result beyond the literature inspected; algebraically equivalent formulas could be present in other published analyses. Direct transfer results and classic invariant densities are credited to their prior authors. Independent mathematical validation has not been performed.

## References

1. S. Suzuki, *Absolutely continuous invariant measures for random dynamical systems of beta-transformations*, arXiv:2303.17521 (first posted 2023-03-30), https://arxiv.org/abs/2303.17521 .
2. H. D. Cornean and K. S. Sørensen, *Sharp iteration asymptotics for transfer operators induced by greedy beta-expansions*, arXiv:2502.17113 (first posted 2025-02-24), https://arxiv.org/abs/2502.17113 .
3. W. Parry, *On the beta-expansions of real numbers*, Acta Math. Acad. Sci. Hung. 11 (1960), 401–416, https://doi.org/10.1007/BF02020954 .
4. A. Rényi, *Representations for real numbers and their ergodic properties*, Acta Math. Acad. Sci. Hung. 8 (1957), 477–493, https://doi.org/10.1007/BF02020331 .
