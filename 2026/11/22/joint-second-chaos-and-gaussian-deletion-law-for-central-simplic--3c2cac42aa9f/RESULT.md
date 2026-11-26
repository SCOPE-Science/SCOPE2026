# Joint second-chaos and Gaussian deletion law for central simplicial depth

## Finding

Let \(X_1,\ldots,X_n\) be independent points uniform by arclength on the unit circle, with \(n\ge4\). Let \(D_n\) be the fraction of unordered triples whose Euclidean triangle contains the origin; let \(D_{n,-1}\) be the analogous fraction after deleting \(X_1\). With
\[
Z_n=n(D_n-1/4),\qquad J_n=n^{3/2}(D_n-D_{n,-1}),
\]
the pair \((Z_n,J_n)\) converges jointly in distribution to \((Z,J)\), where
\[
Z=3\sum_{m\ge1\atop m\ \mathrm{odd}}\lambda_m(\xi_m^2+\eta_m^2-2),\qquad
J=6\sqrt2\sum_{m\ge1\atop m\ \mathrm{odd}}\lambda_m\xi_m,
\qquad \lambda_m=-\frac1{\pi^2m^2},
\]
and all \(\xi_m,\eta_m\) are independent standard normal variables. The sums converge in \(L^2\), and \(J\) alone is normal with variance \(3/4\); nevertheless the two limits are not independent:
\[
\operatorname{Var}(Z)=3/8,\quad \operatorname{Var}(J)=3/4,\quad
\operatorname{Cov}(Z,J)=0,\quad \operatorname{Cov}(Z,J^2)=-9/20.
\]
For \(t\ge0\), \(u\in\mathbb R\), and \(q=\sqrt{6t}/2\), their joint Laplace–Fourier transform is
\[
\mathbb E\,e^{tZ+iuJ}=
\frac{e^{3t/4}}{\cosh q}\,
\exp\left\{-\frac{9u^2}{8q^2}\left(1-\frac{\tanh q}{q}\right)\right\},
\]
with continuous interpretation at \(q=0\).

For comparison with the limit, the known exact depth variance and its single-deletion consequence, valid at every \(n\ge4\), are
\[
\operatorname{Var}(D_n)=\frac{3}{8(n-1)(n-2)},\qquad
\mathbb E(D_n-D_{n,-1})^2=\frac{3}{4(n-1)(n-2)(n-3)}.
\]
For the usual delete-one jackknife variance statistic
\[
\widehat V_{\mathrm J}=\frac{n-1}{n}\sum_{i=1}^{n}(D_{n,-i}-D_n)^2,
\]
the exact expectation-to-true-variance ratio is \(\mathbb E\widehat V_{\mathrm J}/\operatorname{Var}(D_n)=2(n-1)/(n-3)\), tending to \(2\). This is an explicit manifestation of the familiar jackknife distortion for degenerate statistics, rather than a proposed universal correction.

## Assumptions and scope

The angles are independent and exactly uniform on the full circle. More generally, the same assertions hold for independent planar observations whose angular directions about the origin are uniform and whose radial coordinates are almost surely positive, because only directions enter triangle containment. Boundary coincidences have probability zero. The deletion is a specified observation, equivalent by exchangeability to uniformly choosing one of the sampled observations. The theorem is about a fixed number of deletions (one); it does not assert uniform conditional convergence over every data set, arbitrary nonuniform angular laws, or validity of a plug-in confidence interval.

## Proof

**1. A rotation-degenerate triangle kernel.** Write \(H(x,y,z)\) for the indicator that the triangle formed by three directions contains the origin. The classical hemisphere-counting argument gives \(\theta=\mathbb EH=1/4\). Because the angular law is invariant under rotations, \(\mathbb E[H(x,X_2,X_3)]=\theta\) for each \(x\). For two directions separated by the minor angle \(\delta\in[0,\pi]\), the third direction must lie on the opposite arc of angular length \(\delta\), hence
\[
h_2(x,y)=\mathbb E[H(x,y,X_3)]-\theta=\frac\delta{2\pi}-\frac14.
\]
Thus the first Hoeffding projection vanishes. This is a triangular-wave kernel, with the exact Fourier decomposition
\[
h_2(x,y)=\sum_{m\ \mathrm{odd}}\lambda_m\bigl[u_{mc}(x)u_{mc}(y)+u_{ms}(x)u_{ms}(y)\bigr],
\]
where \(u_{mc}(x)=\sqrt2\cos(mx)\), \(u_{ms}(x)=\sqrt2\sin(mx)\) and \(\lambda_m=-1/(\pi^2m^2)\). These functions are orthonormal for uniform angle measure. Parseval gives \(\mathbb Eh_2(X_1,X_2)^2=2\sum_{m\ \mathrm{odd}}\lambda_m^2=1/48\).

**2. Exact finite variance and deletion second moment.** The canonical Hoeffding decomposition of this order-three \(U\)-statistic is
\[
D_n-\theta=3U_{n,2}(h_2)+U_{n,3}(h_3).
\]
Since \(\operatorname{Var}(H)=3/16\), orthogonality gives \(\operatorname{Var}(h_3)=3/16-3/48=1/8\). The canonical variance formula then yields
\[
\operatorname{Var}(D_n)=\frac{9(1/48)}{\binom n2}+\frac{1/8}{\binom n3}=\frac3{8(n-1)(n-2)}.
\]
Every triple appears in exactly \(n-3\) of the leave-one-out samples, so \(D_n=n^{-1}\sum_iD_{n,-i}\). Consequently \(\operatorname{Cov}(D_n,D_{n,-1})=\operatorname{Var}(D_n)\), and the deletion second moment is \(\operatorname{Var}(D_{n-1})-\operatorname{Var}(D_n)\). The two stated finite identities and jackknife expectation follow by substitution.

**3. Joint limit.** Apply the finite-rank central limit theorem to the empirical Fourier coefficients of \(X_2,\ldots,X_n\). The canonical remainder \(nU_{n,3}(h_3)\) tends to zero in \(L^2\). Writing the quadratic projection with its diagonal removed gives
\[
n(D_{n,-1}-\theta)\Longrightarrow3\sum_{m\ \mathrm{odd}}\lambda_m(\xi_m^2+\eta_m^2-2).
\]
Define \(D_n^{\mathrm{incl}}\) as the fraction of triangles involving \(X_1\) among all choices of two other observations. The exact identity
\[
D_n=\frac{n-3}{n}D_{n,-1}+\frac3nD_n^{\mathrm{incl}}
\]
shows that \(J_n=3\sqrt n(D_n^{\mathrm{incl}}-D_{n,-1})\). Conditional on \(X_1=x\), the first projection of the order-two kernel \(H(x,\cdot,\cdot)\) is \(h_2(x,\cdot)\); its canonical order-two remainder vanishes after multiplication by \(\sqrt n\). Since \(\sqrt n(D_{n,-1}-\theta)\to0\), it follows that
\[
J_n=\frac6{\sqrt n}\sum_{j=2}^{n}h_2(X_1,X_j)+o_{\mathbb P}(1).
\]
In a joint finite-frequency Gaussian limit, the cosine–sine pairs can be rotated through the (independent) random angle \(mX_1\). Their joint standard-Gaussian law is unchanged by this rotation, so the linear limit becomes \(6\sqrt2\sum_{m\ \mathrm{odd}}\lambda_m\xi_m\), using the *same* \(\xi_m,\eta_m\) as in the quadratic limit. The Fourier tails vanish in \(L^2\), because \(\sum_m\lambda_m^2<\infty\); this upgrades finite-frequency convergence to the full joint claim. Standard bounded-kernel degeneracy moment bounds, or direct enumeration of index overlaps in these expansions, give uniform fixed higher moments, justifying the mixed-moment limit involving \(J_n^2\).

**4. Transform and nonindependence.** The finite truncations of \(Z\) are bounded above by \(-6\sum_{m\ \mathrm{odd}}\lambda_m=3/4\). Thus their Laplace–Fourier transforms converge to the transform of the \(L^2\) limit for \(t\ge0\). Integrating one Gaussian pair at a time gives
\[
\mathbb E\,e^{tZ+iuJ}=
 e^{3t/4}\prod_{m\ \mathrm{odd}}\left(1+\frac{6t}{\pi^2m^2}\right)^{-1}
\exp\left\{-36u^2\sum_{m\ \mathrm{odd}}\frac{\lambda_m^2}{1-6t\lambda_m}\right\}.
\]
The odd-integer Euler product gives \(\prod_{m\ \mathrm{odd}}(1+6t/(\pi^2m^2))=\cosh q\), while differentiating its logarithm gives
\[
\sum_{m\ \mathrm{odd}}\frac{\lambda_m^2}{1-6t\lambda_m}
=\frac1{32q^2}\left(1-\frac{\tanh q}{q}\right).
\]
Finally \(\sum_{m\ \mathrm{odd}}m^{-4}=\pi^4/96\) and \(\sum_{m\ \mathrm{odd}}m^{-6}=\pi^6/960\). Wick's Gaussian moment identities imply
\(\operatorname{Cov}(Z,J^2)=432\sum_m\lambda_m^3=-9/20\) whereas \(\operatorname{Cov}(Z,J)=0\), proving nonindependence.

## Verification

Run `python checker.py` using Python 3 and the standard library. The checker verifies the Fourier kernel against its triangular-wave definition, the exact finite variance and jackknife algebra, the odd-eigenvalue transform, the exact limit constants and seeded finite-sample geometric simulations. Its finite experiments are reproducibility checks, not an infinite proof. The analytic kernel projections and Gaussian limit arguments above supply the infinite statements.

## Relationship to prior work

Liu introduced simplicial depth as a multivariate statistical depth measure. Dyckerhoff, Ley and Paindaveine developed a different bivariate depth-based runs statistic for symmetry testing. Afshani, Sheehy and Stein studied computation and sample-instability scenarios for simplicial depth, motivating sensitivity under deletion. Reference [7] gives the exact central variance for the unnormalized triangle count; dividing by \(\binom n3^2\) gives the variance in this note. The deletion second moment and jackknife expectation are direct consequences of that variance by deletion averaging, not new variance principles.

The marginal central second-chaos law and its odd Fourier spectrum are also covered, including by the \(c=0\) case of the moving-query result [8]. In that result the critical displacement shifts only the first cosine coordinate. By contrast, the deletion studied here couples the central depth to a linear response involving every odd frequency. Generic degenerate \(U\)-statistic theory accounts for the types of limits, but not this explicit shared-coordinate coupling, its joint transform or the mixed moment \(\operatorname{Cov}(Z,J^2)=-9/20\). These are the contribution. A same-date deletion result for chord crossings [9] concerns a different kernel and is not a depth theorem. The full texts of Dümbgen and of Killeen and Hettmansperger were not available for checking closer overlap.

## Limitations

This is a one-observation, exactly angular-uniform theorem; it does not cover arbitrary asymmetric distributions. The Gaussian deletion marginal does *not* make the deletion statistic independent of the global depth. The exact expected jackknife inflation does not imply that the realized jackknife estimator converges to twice a nonrandom variance for every sample. Historical priority is provisional given the full-text limitations above and the possibility of older general jackknife results.

## References

- R. Y. Liu, “On a notion of simplicial depth,” *Proceedings of the National Academy of Sciences* 85 (1988), 1732–1734. https://doi.org/10.1073/pnas.85.6.1732
- R. Dyckerhoff, C. Ley, and D. Paindaveine, “Depth-based Runs Tests for Bivariate Central Symmetry,” first posted 2014-01-10. https://arxiv.org/abs/1401.2377
- P. Afshani, D. R. Sheehy, and Y. Stein, “Approximating the Simplicial Depth,” first posted 2015-12-15. https://arxiv.org/abs/1512.04856
- L. Dümbgen, “Limit theorems for the simplicial depth,” *Statistics & Probability Letters* 14 (1992), 119–128. https://doi.org/10.1016/0167-7152(92)90075-G
- T. J. Killeen and T. P. Hettmansperger, “A bivariate test for location based on simplicial depth,” published online 2020-03-02. https://doi.org/10.1080/03610926.2019.1710205
- S. Nagy, M. Wendler, and C. Jentsch, “Resampling simplicial depth.” https://arxiv.org/abs/2608.11131
- [7] “Sharp covariance and angular cutoff for central simplicial depth.” https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-sharp-covariance-and-angular-cutoff-for-central-simplicial-depth--c891d8b1a570/RESULT.md
- [8] “A noncentral-to-Gaussian transition for simplicial depth near the center.” https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-noncentral-to-gaussian-transition-for-simplicial-depth-near-th--c1bb34e0d615/RESULT.md
- [9] “Conditional Gaussian deletion noise for crossings of random circular chords.” https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-conditional-gaussian-deletion-noise-for-crossings-of-random-circ--d7315075b295/RESULT.md
