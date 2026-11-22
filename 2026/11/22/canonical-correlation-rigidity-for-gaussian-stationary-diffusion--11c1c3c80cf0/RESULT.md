# Canonical-correlation rigidity for Gaussian stationary diffusions with two reciprocal feedback pairs

## Finding

Let \(C\) be any real \(2\times2\) matrix with largest singular value strictly below one, and let \(\rho_C\) be the centered four-dimensional Gaussian density with covariance
\[
\Sigma_C=\begin{pmatrix}I_2&C\\ C^{\mathsf T}&I_2\end{pmatrix}.
\]
Consider graph-local vector fields \(v(x,y)=(u(x),w(y))\), where \(x,y\in\mathbb R^2\), satisfying \(\operatorname{div}(\rho_C v)=0\). Each two-dimensional block permits a reciprocal feedback pair, but there are no drift edges between blocks.

Write \(s_1\ge s_2\ge0\) for the singular values of \(C\). Among the fields specified below, **the complete null-current space** has:

- infinite dimension when \(s_1=s_2=0\);
- dimension zero when \(s_1>s_2\), including the rank-one case \(s_2=0<s_1\);
- dimension one when \(s_1=s_2=s\in(0,1)\).

In the last case, choose orthogonal matrices \(U,V\) with \(U^{\mathsf T}CV=sI_2\), and put
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Every null-current field is, for exactly one real \(\omega\),
\[
v_\omega(x,y)=\bigl(\omega UJU^{\mathsf T}x,\ \omega VJV^{\mathsf T}y\bigr).
\]
Consequently, for the **fixed, known** diffusion covariance \(2\Sigma_C\), the stationary density \(\rho_C\) uniquely identifies a graph-local drift in this class whenever \(s_1>s_2\). If the two nonzero singular values coincide, a one-dimensional family of distinct stable Ornstein–Uhlenbeck drifts has the identical stationary law. At \(C=0\), there are even infinitely many non-linear alternatives.

## Assumptions and scope

The unknown drift field is \(C^2\), block-local as above, with its components and first derivatives in \(L^2(\rho_C)\). The same class is used for differences of candidate drifts. The stationarity equation is interpreted distributionally, which agrees with the classical equation here. No coordinate-wise independence is assumed between the two blocks; their cross-covariance is \(C\). All statements concern the given four-dimensional covariance family, not arbitrary covariances or graphs.

The stochastic differential equation underlying the identifiability consequence has constant noise matrix \(\sqrt 2\,\Sigma_C^{1/2}\). Thus the driving noises may be cross-correlated even though the drift has no cross-block dependence. In particular, the result does not assert that these correlated stationary laws are attainable with two autonomous drift blocks driven by independent noises.

## Proof

**1. Reduction to canonical correlations.** A singular-value decomposition yields \(C=U\operatorname{diag}(s_1,s_2)V^{\mathsf T}\). The orthogonal transformations \(x\mapsto U^{\mathsf T}x\), \(y\mapsto V^{\mathsf T}y\) preserve block locality, Gaussian \(L^2\) integrability and weighted divergence. Hence assume \(C=\operatorname{diag}(s_1,s_2)\) with nonnegative entries.

Set \(\alpha_i=(1-s_i^2)^{-1}\) and \(\beta_i=s_i(1-s_i^2)^{-1}\) for \(i=1,2\). Differentiating the Gaussian density gives
\[
\begin{split}
0={}&\operatorname{div}_x u+\operatorname{div}_y w
-\sum_{i=1}^2\alpha_i(x_iu_i(x)+y_iw_i(y))\\
&+\sum_{i=1}^2\beta_i(y_iu_i(x)+x_iw_i(y)). \tag{1}
\end{split}
\]
Integrating \(\operatorname{div}(\rho_C v)=0\) over \(y\), and separately over \(x\), shows
\[
\operatorname{div}_x(\phi_2u)=0,
\qquad\operatorname{div}_y(\phi_2w)=0, \tag{2}
\]
where \(\phi_2\) is the standard two-dimensional Gaussian density. For full justification, test against smooth compactly supported functions of the retained block and insert cutoffs in the discarded block. The cutoff-gradient terms vanish in the limit by Cauchy–Schwarz, since the vector fields are Gaussian-square-integrable and the density has Gaussian tails. Thus (2) holds distributionally and hence pointwise. It is equivalent to \(\operatorname{div}_x u=x\cdot u\) and \(\operatorname{div}_y w=y\cdot w\).

**2. Both canonical correlations positive.** Apply \(\partial_{x_j}\partial_{y_k}\) to (1), for any \(j,k\in\{1,2\}\). All pure-block terms disappear and leave
\[
\beta_k\partial_{x_j}u_k(x)+\beta_j\partial_{y_k}w_j(y)=0. \tag{3}
\]
If \(s_1s_2>0\), both factors are positive. The first term of (3) depends only on \(x\), the second only on \(y\), so each is constant. Varying \(j,k\) proves every first derivative of \(u,w\) is constant. Therefore \(u(x)=Ax+a\) and \(w(y)=By+b\). Equation (2), compared as a polynomial identity, makes \(a=b=0\) and \(A,B\) skew-symmetric. Thus \(u=\omega Jx\), \(w=\eta Jy\) for real \(\omega,\eta\).

Substituting these into (1), the pure-block quadratic terms are
\[
\omega(\alpha_1-\alpha_2)x_1x_2
+\eta(\alpha_1-\alpha_2)y_1y_2.
\]
If \(s_1\ne s_2\), then \(\alpha_1\ne\alpha_2\), and the coefficients force \(\omega=\eta=0\). If \(s_1=s_2=s>0\), the pure-block terms vanish and the remaining term is \(\beta(\omega-\eta)\,y\cdot Jx\), with \(\beta=s/(1-s^2)>0\). It vanishes precisely when \(\omega=\eta\). Undoing the orthogonal changes of coordinates yields the asserted one-dimensional family, and direct substitution establishes sufficiency.

**3. Rank-one cross-covariance.** Now let \(s_1>0=s_2\). Equation (3) with \((j,k)=(2,1)\) and \((1,2)\) implies \(\partial_{x_2}u_1=0\) and \(\partial_{y_2}w_1=0\). Hence \(u_1=f(x_1)\) and \(w_1=g(y_1)\). Integrate the first equation of (2), equivalently \(\partial_{x_1}u_1+\partial_{x_2}u_2=x_1u_1+x_2u_2\), against the standard Gaussian in \(x_2\). The \(x_2\)-weighted divergence integrates to zero by the same cutoff argument. Thus \(f'(x_1)=x_1f(x_1)\). Every solution is \(f(x_1)=c\exp(x_1^2/2)\), which is in Gaussian \(L^2\) only for \(c=0\). Similarly \(g=0\). Equation (2) now gives \(\partial_{x_2}u_2=x_2u_2\) and \(\partial_{y_2}w_2=y_2w_2\). Gaussian \(L^2\) again forces \(u_2=w_2=0\). This proves the rank-one rigidity, including the boundary where one singular value vanishes.

**4. Uncorrelated blocks.** If \(C=0\), choose any smooth compactly supported scalar function \(h\) of a nonnegative argument and let \(u(x)=h(|x|^2)Jx\), \(w(y)=0\). Then \(\operatorname{div}u=0\), \(x\cdot u=0\), so (2) and the full weighted divergence equation hold. Linearly independent choices of \(h\) exhibit infinite dimension.

**5. Actual stationary diffusions.** Let \(Z=(X,Y)\). The drift \(b_0(Z)=-Z\) and diffusion \(\sqrt2\,\Sigma_C^{1/2}\) define a stable Ornstein–Uhlenbeck process with unique invariant law \(N(0,\Sigma_C)\), since \((-I)\Sigma_C+\Sigma_C(-I)+2\Sigma_C=0\). For every null-current field \(v\), the drift \(b_0+v\) satisfies the same stationary Fokker–Planck equation. In the equal-positive-singular-value case, \(v_\omega\) is a blockwise skew-symmetric linear map and \(-I+v_\omega\) has eigenvalues with real part \(-1\), so all \(\omega\) give genuine stable Ornstein–Uhlenbeck diffusions with the same unique invariant Gaussian. At \(C=0\), the smooth compactly supported rotational fields in step 4 yield globally Lipschitz, radially dissipative drifts, and uniform ellipticity ensures existence and uniqueness of the same invariant Gaussian. The zero-null-space regimes give uniqueness of graph-local stationary drift by subtracting any two candidates with the same fixed diffusion coefficient.

## Verification

The standalone Python/SymPy checker in `verification/check.py` constructs the entire rational coefficient matrix of the weighted-divergence equation on block-local polynomial vector fields of total block degree at most one, two and three. It checks twelve exact nullities, including zero-dimensional spaces at unequal singular values, one-dimensional spaces at equal nonzero singular values, and the expanding nullities \(2,6,12\) in the independent-block case. It also symbolically substitutes a coordinated block rotation at equal and unequal canonical correlations. The checker uses exact rational arithmetic: no floating-point nullspace threshold is involved. These finite-degree computations are **diagnostics, not the proof** of the general nonlinear theorem; steps 1–4 establish the infinite-dimensional classification directly.

Reproduce with `python verification/check.py` using Python 3 and SymPy. The checker does not require external datasets.

## Relationship to prior work

Schwank and Drton (2026), Theorems 1.1 and 3.4, establish nonlinear graph-local drift identifiability under density convexity when the interaction graph **has no directed two-cycles**. Their discussion expressly identifies reciprocal pairs as potential obstacles; their theorem cannot be applied to the two reciprocal pairs here. The present result gives a sharp positive/no-null-current classification **with two-cycles**, using the cross-block Gaussian correlations and a full mixed-derivative argument.

Dettling, Homs, Améndola, Drton and Hansen (2023) establish global and generic identifiability criteria for **linear** drift matrices; their Appendix A, Example 42, shows that correlated driving noise can remove non-identifiability for a reciprocal two-node pair plus a third isolated node. This is important prior evidence for the mechanism, but does not provide the four-dimensional canonical-correlation phase diagram or exclude arbitrary nonlinear block-local null currents.

Garcez Vicente and Salehkaleybar (2026) study generic covariance identifiability for **linear** stochastic differential equations with reciprocal interactions and optional latent variables. Their rank methods do not prove this pointwise Gaussian nonlinear space classification. Published results on time-dependent observation or diffusion shifts ask different inverse questions.

## Limitations

The theorem is restricted to two size-two blocks with standard-Gaussian marginal covariances, arbitrary positive-definite joint Gaussian cross-covariance, graph-local \(C^2\) fields and the stated Gaussian \(L^2\) conditions. It does not determine the inverse problem for larger blocks, non-Gaussian equilibria, unknown diffusion matrices or systems with drift edges between the blocks. The claim is a mathematical classification and not an estimate from finite samples. Historical priority beyond the compared accessible sources is not independently certified.

## References

1. R. Schwank and M. Drton, *Fingerprints of feedback cycles in stationary diffusions*, arXiv:2611.11288v1 (first publicly available 2026-11-08). https://arxiv.org/html/2611.11288v1
2. P. Dettling, R. Homs, C. Améndola, M. Drton and N. R. Hansen, *Identifiability in Continuous Lyapunov Models*, arXiv:2209.03835 (first publicly available 2022-09-08); *SIAM Journal on Matrix Analysis and Applications* 44 (2023), 1799–1821. https://arxiv.org/pdf/2209.03835
3. A. L. Garcez Vicente and S. Salehkaleybar, *Identifiability from Stationary Covariance in Linear SDEs with Reciprocal Interactions and Latent Variables*, arXiv:2610.31310 (first publicly available 2026-10-22). https://arxiv.org/abs/2610.31310
