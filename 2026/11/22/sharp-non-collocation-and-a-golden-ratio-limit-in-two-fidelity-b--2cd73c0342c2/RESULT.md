# Sharp non-collocation and a golden-ratio limit in two-fidelity Brownian-bridge quadrature

## Finding

For independent standard Brownian bridges \(U,V\) and an arbitrary discrepancy-to-baseline variance ratio \(d>0\), let \(H_d=U+\sqrt d V\), \(L=U\). Estimate \(J_d=\int_0^1 H_d(t)\,dt\) by the conditional mean from a single exact high-fidelity observation \(H_d(x)\) and a single exact low-fidelity observation \(L(y)\), placed deterministically at \(x,y\in[0,1]\). Write \(\mathcal R_d(x,y)=\operatorname{Var}(\mathbb E[J_d\mid H_d(x),L(y)])\), the explained variance to be maximized. The conditional-mean mean-square error equals \((1+d)/12-\mathcal R_d(x,y)\).

**Non-collocation for every \(d>0\).** The maximum explained variance among colocated pairs is \((1+d)/16\), whereas
\[
\mathcal R_d(1/2,1/4)-\max_{0\le t\le1}\mathcal R_d(t,t)
=\frac{d+1}{64(3d+2)}>0.
\]
Consequently every globally optimal fidelity-labeled pair is separated, for every finite \(d>0\).

**Sharp large-discrepancy configuration.** There is a finite constant \(d_0>0\) (not explicitly bounded) such that for each \(d>d_0\) there are exactly two global maximizers, exchanged by reflection \((x,y)\mapsto(1-x,1-y)\). On the branch with \(y_d<x_d\),
\[
 y_d=\frac{3-\sqrt5}4+O(d^{-1}),\qquad
 x_d=\frac12+\frac{7-3\sqrt5}{4d}+O(d^{-2}).
\]
The optimal explained variance satisfies
\[
\max_{x,y}\mathcal R_d(x,y)
=\frac{d+1}{16}+\frac{5\sqrt5-11}{32}+O(d^{-1}).
\]
In particular the limiting additional gain over the best colocated design is strictly positive: \((5\sqrt5-11)/32=0.005635621484\ldots\).

## Assumptions and scope

A standard Brownian bridge is the centered continuous Gaussian process with covariance \(K(s,t)=\min(s,t)-st\) on \([0,1]\). The two bridges are independent; the independent discrepancy is scaled by \(\sqrt d\), with \(d\in(0,\infty)\). Each observation is exact and fidelity-labeled; observation locations are deterministic and can coincide or be endpoints. Covariance parameters are known, and the predictor is the conditional mean (the minimum-mean-square estimator under the specified joint Gaussian law). The calculation is a one-high/one-low, non-nested, fixed-budget design problem. A high-fidelity evaluation does **not** automatically return a low-fidelity evaluation at the same site; doing so would be a different cost constraint.

## Proof

**1. Exact risk.** Put \(a=x(1-x)\), \(b=y(1-y)\), and \(k=\min(x,y)-xy\). The variance of \(J_d\) is \((1+d)/12\), and its covariance with the observation vector \((H_d(x),L(y))\) is \(c=((1+d)a/2,b/2)\). The covariance of the observations is
\[
\Sigma=\begin{pmatrix}(1+d)a&k\\k&b\end{pmatrix}.
\]
For interior \(x,y\), the matrix is positive definite because \(d>0\) and \(k^2\le ab\). Gaussian conditioning and one Schur-complement step give
\[
\mathcal R_d(x,y)=c^\mathsf T\Sigma^{-1}c
=\frac{(1+d)a}4+
\frac{(b-k)^2}{4\left(b-k^2/((1+d)a)\right)}.\tag{1}
\]
At endpoints, the zero-variance channel conveys no information and the formula is interpreted by its unique continuous extension. This extension also covers coincident sites.

**2. Finite-ratio strict separation.** For \(x=y=t\), \(a=b=k=t(1-t)\), hence the second term in (1) vanishes; its maximum is \((1+d)/16\) at \(t=1/2\). Direct substitution of \(x=1/2,y=1/4\) into (1) gives
\[
\mathcal R_d(1/2,1/4)
=\frac{3(d+1)(4d+3)}{64(3d+2)}
=\frac{d+1}{16}+\frac{d+1}{64(3d+2)}.
\]
Thus no global maximizer lies on the diagonal for any \(d>0\), without assuming a priori where a maximizer is located.

**3. Uniform large-discrepancy expansion.** Define the continuous function
\[
g(x,y)=\begin{cases}(b-k)^2/b,&0<y<1,\\0,&y\in\{0,1}.\end{cases}
\]
Because \(0\le k\le b\) and \(k^2\le ab\), it obeys \(0\le g\le b\le1/4\). Let \(q=k^2/(ab)\in[0,1]\) for interior sites. Then (1) becomes
\[
\mathcal R_d(x,y)=\frac{da}4+\frac a4+
\frac g{4(1-q/(1+d))}.
\]
Since \(1\le[1-q/(1+d)]^{-1}\le1+1/d\), the error in the following expansion is globally uniform on the closed design square:
\[
\mathcal R_d(x,y)=\frac{d x(1-x)}4+F(x,y)+E_d(x,y),
\quad F(x,y)=\frac{x(1-x)+g(x,y)}4,
\quad 0\le E_d\le\frac1{16d}.\tag{2}
\]

**4. Golden-ratio limit and global localization.** The maximum of \(x(1-x)\) is attained uniquely at \(x=1/2\). Comparing a global maximizer with the candidate \((1/2,y_0)\) in (2), using boundedness of \(F\), first shows \(x_d\to1/2\). On this line,
\[
g(1/2,y)=\frac{y(1/2-y)^2}{1-y}\quad(0\le y\le1/2),
\qquad g(1/2,1-y)=g(1/2,y).
\]
For \(0<y<1/2\),
\[
\frac{d}{dy}g(1/2,y)
=-\frac{(2y-1)(4y^2-6y+1)}{4(y-1)^2}.
\]
It has the unique maximum on \([0,1/2]\) at \(y_0=(3-\sqrt5)/4\), with \(g(1/2,y_0)=(5\sqrt5-11)/8>0\). The two and only two maxima of \(F(1/2,\cdot)\) are \(y_0\) and \(1-y_0\). If \((x_d,y_d)\) is any global maximizer and \(y_d\to\bar y\) along a subsequence, optimality compared with \((1/2,y_0)\), together with \(x(1-x)\le1/4\) in (2), implies \(F(1/2,\bar y)\ge F(1/2,y_0)\). Hence every such \(\bar y\) is one of the two stated points. This proves localization of **all** global maximizers, not just a selected local branch.

**5. Exactly two optimizers for sufficiently large \(d\).** Around \((1/2,y_0)\) choose a small convex rectangle strictly inside \(0<y<x<1\), and around \((1/2,1-y_0)\) choose its midpoint reflection. In either rectangle, formula (1) has a smooth expansion with all derivatives through second order. At its central limiting point, \(\partial_{yy}g=-10+4\sqrt5<0\); therefore \(\partial_{yy}\mathcal R_d<0\) uniformly throughout sufficiently small rectangles for all sufficiently large \(d\). Also \(\partial_{xx}\mathcal R_d=-d/2+O(1)\) and \(\partial_{xy}\mathcal R_d=O(1)\) uniformly there. The Hessian is consequently negative definite on both rectangles for all sufficiently large \(d\), so each admits at most one maximizer. Step 4 forces every global maximizer into these rectangles; compactness ensures existence, and reflection gives a counterpart. There are therefore exactly two, exchanged by reflection. This proves existence of a finite \(d_0\), without claiming a numeric threshold.

**6. Refined location and value.** For the branch with \(y_d<x_d\), stationarity and the derivative expansions of (2) give \(x_d=1/2+O(d^{-1})\) and \(y_d=y_0+O(d^{-1})\). In that region \(g(x,y)=y(x-y)^2/(1-y)\), so \(\partial_xg(1/2,y_0)=2y_0(1/2-y_0)/(1-y_0)\). The \(x\)-stationarity equation yields
\[
d(x_d-1/2)\longrightarrow\frac12\partial_xg(1/2,y_0)
=\frac{y_0(1/2-y_0)}{1-y_0}
=\frac{7-3\sqrt5}4.
\]
Smoothness and the nondegenerate Hessian equations improve this to \(x_d=1/2+(7-3\sqrt5)/(4d)+O(d^{-2})\). Substitution in (2) gives the optimal-value expansion, with \(g(1/2,y_0)/4=(5\sqrt5-11)/32\). The other branch is its reflection.

## Verification

The standalone \(verify.py\), run using \(python verify.py\) with no third-party dependencies, checks the exact Schur-complement identity against an independently coded two-by-two covariance inversion on rational grids, checks the finite-ratio separation margin exactly, evaluates the golden limiting constant, and checks asymptotic candidate improvements for increasing \(d\). The verifier reported 1,745 assertions passing. These computational checks are supplementary; the global conclusions follow from the analytic proof above. The decoded script bundled with this finding is the one to run.

## Relationship to prior work

Li, Giles, Karvonen, Guillas and Briol's *Multilevel Bayesian Quadrature* develops levelwise Gaussian-process models, including a correlated-level extension in Appendix B.3, posterior-variance formulas, and sample-count allocations using paired differences at each level; it does not establish a globally optimized, non-nested one-high/one-low Brownian-bridge location pair. Yang, Barajas-Solano, Tartakovsky and Tartakovsky develop additive-discrepancy CoKriging and greedy pointwise uncertainty reduction, but not this exact integral-design phase and asymptotic location law. Yang, Zhu and Li develop physics-informed bifidelity CoKriging and greedy sampling, again with a different objective. Standard Gaussian conditioning itself is prior-known and is not claimed as a new theorem. The strict all-ratio separation and two-global-optima golden limit require further optimization beyond the general covariance identities. Equivalent historical co-kriging design special cases remain a publication-priority risk.

## Limitations

No explicit minimal threshold \(d_0\) for the two-optima theorem is provided. No assertion is made about uniqueness at smaller \(d\), noisy channels, unequal kernel scales, different fidelity-evaluation costs, learned covariance hyperparameters, adaptive locations, or more than one observation from either fidelity. Numerical grids do not prove uniqueness and finite search cannot establish originality. The claim is a self-reviewed mathematical result, not an independently audited theorem.

## References

1. X. Yang, D. Barajas-Solano, G. Tartakovsky and A. Tartakovsky, *Physics-Informed CoKriging: A Gaussian-Process-Regression-Based Multifidelity Method for Data-Model Convergence*, arXiv:1811.09757 (first submitted 2018-11-24). https://arxiv.org/abs/1811.09757
2. X. Yang, X. Zhu and J. Li, *When Bifidelity Meets CoKriging: An Efficient Physics-Informed Multifidelity Method*, arXiv:1812.02919 (first submitted 2018-12-07). https://arxiv.org/abs/1812.02919
3. K. Li, D. Giles, T. Karvonen, S. Guillas and F.-X. Briol, *Multilevel Bayesian Quadrature*, arXiv:2210.08329 (first submitted 2022-10-15). https://arxiv.org/abs/2210.08329
4. X. Cai, C. T. Lam and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615 (first submitted 2022-02-22). https://arxiv.org/abs/2202.10615
