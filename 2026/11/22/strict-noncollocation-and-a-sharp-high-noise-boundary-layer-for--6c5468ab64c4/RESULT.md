# Strict noncollocation and a sharp high-noise boundary layer for two Brownian path sensors

## Finding

Let \(B_t\), \(0\le t\le1\), be standard Brownian motion with \(B_0=0\). Observe \(Y_1=B_x+\xi_1\) and \(Y_2=B_y+\xi_2\), with independent centered Gaussian noise of the same variance \(\eta>0\), and choose \(0\le x\le y\le1\) to minimize the integrated posterior variance
\[
R_\eta(x,y)=\int_0^1\operatorname{Var}(B_t\mid Y_1,Y_2)\,dt.
\]
For **every** finite \(\eta>0\), every global minimizer satisfies \(0<x<y<1\): repeated measurements are strictly suboptimal, and neither the initial nor terminal time is optimal. There exists a finite \(\eta_0\) such that for all \(\eta>\eta_0\) the minimizer is unique, and
\[
x_\eta=1-\frac1{2\eta}+O(\eta^{-2}),\qquad
 y_\eta=1-\frac1{6\eta}+O(\eta^{-2}),\qquad
 y_\eta-x_\eta=\frac1{3\eta}+O(\eta^{-2}).
\]
Its integrated posterior variance is
\[
\min_{0\le x\le y\le1}R_\eta(x,y)
=\frac12-\frac2{3\eta}+\frac4{3\eta^2}-\frac{53}{18\eta^3}+O(\eta^{-4}).
\]
If the two independent measurements must instead be taken at the **same** optimized location, the minimum risk exceeds the unrestricted minimum by
\[
\min_{0\le t\le1}R_\eta(t,t)-\min_{0\le x\le y\le1}R_\eta(x,y)
=\frac1{18\eta^3}+O(\eta^{-4}).
\]
The last coefficient is positive and sharp; optimization over the collocated position is essential in this comparison.

## Assumptions and scope

The covariance is exactly \(\operatorname{Cov}(B_s,B_t)=\min(s,t)\) on \([0,1]\); noise observations are independent of the process and of each other and have **variance** \(\eta\), not standard deviation \(\eta\). Both measurements have the same noise variance and may coincide. The loss integrates posterior pointwise *path* variance with unit Lebesgue weight; it is **not** the posterior variance of the path integral and not a determinant criterion. The all-noise result concerns strict interior and distinctness of **all** optimizers, while uniqueness and asymptotic formulas are claimed only for sufficiently large noise. No explicit universal value for \(\eta_0\) is asserted.

## Proof

**1. Exact objective.** Write \(\varepsilon=1/\eta\) and
\[
A(t)=t^2-\tfrac23t^3,\quad
C(x,y)=xy-\tfrac12xy^2-\tfrac16x^3\quad(x\le y).
\]
Integrating products of covariance sections gives \(\int_0^1\min(t,x)^2dt=A(x)\) and \(\int_0^1\min(t,x)\min(t,y)dt=C(x,y)\). The observation covariance matrix is \(\begin{psmallmatrix}x+\eta&x\\x&y+\eta\end{psmallmatrix}\). Conditional Gaussian covariance, matrix inversion, and \(\int_0^1\operatorname{Var}(B_t)dt=1/2\) yield \(R_\eta=1/2-F_\varepsilon\), where
\[
F_\varepsilon(x,y)
=\frac{\varepsilon[A(x)+A(y)]+\varepsilon^2B(x,y)}{1+\varepsilon(x+y)+\varepsilon^2x(y-x)},
\qquad B(x,y)=\frac{x(x-y)(x^2-xy+2y^2-3y)}3.
\]
The denominator is strictly positive throughout the closed design triangle. Consequently a global optimum exists for each \(\eta>0\).

**2. No initial sensor.** If \(x=0\), the first observation is independent pure noise. For any \(y>0\), adding an observation at \(0<x'<y\) gives a *strictly* positive integrated conditional-variance reduction relative to keeping only the observation at \(y\). Indeed the conditional covariance of \(B_{x'}\) with \(Y_{x'}\) given \(Y_y\) equals \(x'(y+\eta-x')/(y+\eta)>0\), and remains nonzero on an interval of prediction times. For \(y=0\), both observations are pure noise and a positive-time observation strictly improves the risk. Thus every optimum has \(x>0\).

**3. No collocation.** On the ordered side of the diagonal, exact differentiation gives
\[
(\partial_y-\partial_x)F_\varepsilon(t,t)
=\frac{2\varepsilon^2t^2(3-2t)}{3(1+2\varepsilon t)^2}>0\qquad(0<t<1).
\]
Perturbing a collocated pair to \((t-\delta,t+\delta)\) therefore improves the objective. At \((1,1)\), \(\partial_xF_\varepsilon=-\varepsilon^2/(1+2\varepsilon)^2<0\), so moving the first measurement left improves it as well. The pair \((0,0)\) is handled by step 2. Hence every optimizer has \(x<y\).

**4. No terminal sensor.** At \(y=1\), let \(D=1+\varepsilon(1+x)+\varepsilon^2x(1-x)\). Exact differentiation shows
\[
\left.\partial_yF_\varepsilon(x,y)\right|_{y=1}
=-\frac{\varepsilon^2\{1+\varepsilon x(1-x)^2(x+2)+\varepsilon^2x^2(1-x)^3\}}{3D^2}<0.
\]
For \(x<1\), moving the second observation slightly to the left while keeping it to the right of \(x\) improves the objective. Together with step 3 this proves \(0<x<y<1\) at every global minimum.

**5. Localization and uniqueness at high noise.** Uniformly on the compact design triangle,
\[
F_\varepsilon(x,y)=\varepsilon[A(x)+A(y)]+O(\varepsilon^2).
\]
Since \(A'(t)=2t(1-t)>0\) for \(0<t<1\), the unique maximizer of its leading term is \((1,1)\). Compactness shows that all exact global maximizers approach \((1,1)\) as \(\varepsilon\downarrow0\). On the fixed convex triangle \(3/4\le x\le y\le1\), the Hessian, computed from the smooth ordered formula, is uniformly
\[
\nabla^2 F_\varepsilon
=\varepsilon\operatorname{diag}(2-4x,2-4y)+O(\varepsilon^2),
\]
with strictly negative-definite leading term. Therefore \(F_\varepsilon\) is strictly concave there for all sufficiently small \(\varepsilon\). All global maxima lie there, so there is exactly one, and steps 2–4 place it in the open triangle.

**6. Sharp location layer.** The uniform first-derivative expansion is
\[
\partial_xF_\varepsilon=\varepsilon A'(x)+\varepsilon^2H_x(x,y,\varepsilon),\qquad
\partial_yF_\varepsilon=\varepsilon A'(y)+\varepsilon^2H_y(x,y,\varepsilon),
\]
where \(H_x,H_y\) are smooth near \((1,1,0)\) and \(H_x(1,1,0)=-1\), \(H_y(1,1,0)=-1/3\). Stationarity and \(A'(t)=2t(1-t)\) first give \(1-x=O(\varepsilon)\), \(1-y=O(\varepsilon)\), then the two sharp coefficients \(1/2\) and \(1/6\) with \(O(\varepsilon^2)\) remainder by smoothness.

**7. Risk and optimized collocation gap.** Substitution \(x=1-u\varepsilon\), \(y=1-v\varepsilon\) into the exact formula yields, uniformly for bounded \(u,v\),
\[
F_\varepsilon=\frac23\varepsilon-\frac43\varepsilon^2
+\varepsilon^3\left(\frac83-u^2+u-v^2+\frac v3\right)+O(\varepsilon^4).
\]
At the unique high-noise optimizer, \(u=1/2+O(\varepsilon)\), \(v=1/6+O(\varepsilon)\); the cubic coefficient is \(53/18\). For collocated samples at \(t\), independent noises combine into effective variance \(\eta/2\), giving \(F_\varepsilon(t,t)=2\varepsilon A(t)/(1+2\varepsilon t)\). Its global optimizer localizes at \(t=1\) as above and is unique for small \(\varepsilon\); with \(t=1-w\varepsilon\), the cubic coefficient is \(8/3-2w^2+4w/3\), uniquely maximized at \(w=1/3\), where its value is \(26/9\). Subtracting \(26/9\) from \(53/18\) proves the sharp difference \(1/18\). All remainders come from rational functions analytic on a compact neighborhood with positive denominators.

## Verification

Run `python check_brownian_design.py` with Python, SymPy, NumPy, and SciPy. The checker symbolically verifies the exact matrix-derived rational objective, the interior-point directional identities, the high-noise Taylor coefficients, and the collocated comparison. It then numerically optimizes the exact objective at five noise levels. The symbolic identities are exact; the finite numerical tests are not a proof of global optimization. The proof above supplies the global and all-parameter claims independently of those tests.

## Relationship to prior work

Ji and Müller (2016, arXiv:1604.05375), particularly their observation-noise model and integrated recovery criterion in Section 2, provide the general posterior-variance optimization framework, but no Brownian-motion two-site strong-noise layer or strict noncollocation theorem was identified in the inspected work. Mukherjee's paper *A Note on Sampling Designs for Random Processes with No Quadratic Mean Derivative* explicitly uses exact process observations and treats large sample-count asymptotics; it also describes the closely related 2003 product-covariance paper as having an interpolating BLUE. Those conclusions do not cover the strictly noisy fixed-two-site boundary layer. Müller-Gronbach's earlier path-design work addresses exact process sampling and many-point asymptotics in the accessible descriptions. A separate Brownian-*bridge* two-observation optimum involves covariance \(\min(s,t)-st\) and does not imply this free-end Brownian-motion boundary layer.

## Limitations

Uniqueness is proved only for sufficiently large \(\eta\); the paper neither asserts uniqueness for every positive noise level nor supplies an explicit transition threshold. The conclusions do not cover correlated or unequal sensor noises, alternative weighted path losses, integrated-value estimation, or other stochastic processes. Bibliographic originality is qualified: the full text of Mukherjee's 2003 article and its associated dissertation was not accessible during the comparison, so an unindexed or unavailable equivalent result cannot be excluded. No independent mathematical audit has been performed.

## References

1. Hao Ji and Hans-Georg Müller, *Optimal Designs for Longitudinal and Functional Data*, arXiv:1604.05375, first public arXiv posting 18 April 2016, https://arxiv.org/abs/1604.05375.
2. Bhramar Mukherjee, *A Note on Sampling Designs for Random Processes with No Quadratic Mean Derivative*, openly accessible author manuscript, https://websites.umich.edu/~bhramar/research/synote1.pdf.
3. Bhramar Mukherjee, *Exactly optimal sampling designs for processes with a product covariance structure*, Canadian Journal of Statistics 31 (2003), 69–87, https://doi.org/10.2307/3315904 (full text not accessed).
4. Thomas Müller-Gronbach, *Optimal designs for approximating the path of a stochastic process*, Journal of Statistical Planning and Inference 49 (1996), 371–385, https://doi.org/10.1016/0378-3758(95)00017-8 (bibliographic and abstract descriptions consulted).
5. Bhramar Mukherjee, *Optimal designs for estimating the path of a stochastic process*, Purdue dissertation catalog, https://docs.lib.purdue.edu/dissertations/AAI3043760/ (abstract only).
