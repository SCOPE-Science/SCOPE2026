# Exact design loss and Gaussian fluctuations for stratified Brownian kernel quadrature

## Finding
Let \(B\) be standard Brownian motion on \([0,1]\), with \(B(0)=0\), and let \(I=\int_0^1 B(t)\,dt\). For an integer \(n\ge1\), choose independent \(U_1,\ldots,U_n\sim\mathrm{Unif}(0,1)\), independently of \(B\), and observe \(B(T_i)\) at \(T_i=(i-1+U_i)/n\). Write \(V_n=\operatorname{Var}(I\mid T_1,\ldots,T_n,B(T_1),\ldots,B(T_n))\). The following statements hold.

The conditional variance is an exact gap-cubic functional:
\[
12n^3 V_n=U_1^3+\sum_{i=2}^n(1+U_i-U_{i-1})^3+4(1-U_n)^3.
\]
Its expectation has the exact finite-budget formula
\[
\mathbb E V_n=\frac{6n-1}{48n^3}.
\]
Among *all* deterministic choices of \(n\) strictly ordered observation times in \((0,1]\), the minimum conditional variance is \(V_n^{\rm opt}=1/[3(2n+1)^2]\), uniquely attained by \(t_i=2i/(2n+1)\). The optimal times also lie inside the prescribed equal strata. Consequently
\[
\frac{\mathbb E V_n}{V_n^{\rm opt}}=\frac{(6n-1)(2n+1)^2}{16n^3}\longrightarrow\frac32.
\]
Finally, across randomized designs the normalized variance obeys the sharp fluctuation limit
\[
\sqrt n\left(n^2V_n-\frac18\right)\ \Longrightarrow\ N\!\left(0,\frac{11}{3456}\right).
\]
If the same independent infinite sequence \((U_i)_{i\ge1}\) is used to define all \(V_n\), then \(n^2V_n\to1/8\) almost surely.

## Assumptions and scope
All variance statements condition on both the exact observation times and exact Brownian values; the variance is independent of those values. The random design is exactly one independent uniform point in each equal-probability interval. There is no observation noise, no estimated covariance hyperparameter, and no adaptive point selection. The design-optimal comparison is for the same Gaussian prior, target integral, and number of exact point observations. The central limit statement concerns randomness in the observation *locations*, not Gaussian posterior integration error conditional on a fixed design.

## Proof
**Conditional-variance decomposition.** Put \(t_0=0\), \(t_i=T_i\) and \(h_i=t_i-t_{i-1}\) for \(1\le i\le n\), with \(h_{n+1}=1-t_n\). Conditional on the observations, the centered path on each fully observed interval \([t_{i-1},t_i]\) is an independent Brownian bridge of duration \(h_i\), with covariance \(\min(s,t)-st/h_i\) in local coordinates. Its integrated variance is \(h_i^3/12\), by double integration. The centered path on the final unobserved interval is an independent Brownian motion starting at zero, with integrated variance \(h_{n+1}^3/3\). Thus
\[
V_n=\frac1{12}\sum_{i=1}^nh_i^3+\frac13h_{n+1}^3.
\]
The stipulated \(T_i\) give \(nh_1=U_1\), \(nh_i=1+U_i-U_{i-1}\) for \(2\le i\le n\), and \(nh_{n+1}=1-U_n\), proving the first formula, also at \(n=1\).

**Exact mean and optimum.** Integrating uniforms gives \(\mathbb E[U^3]=1/4\) and \(\mathbb E[(1+U-V)^3]=3/2\) for independent uniforms \(U,V\). Hence \(12n^3\mathbb E V_n=1/4+(n-1)3/2+4(1/4)=(6n-1)/4\). For a deterministic grid, minimize \((\sum_{i=1}^n h_i^3+4h_{n+1}^3)/12\) subject to nonnegative gaps summing to one. Strict convexity and positive Lagrange multipliers give \(h_1=\cdots=h_n=2h_{n+1}\); the unique solution is \(h_{n+1}=1/(2n+1)\) and \(h_i=2/(2n+1)\). Its value is \(1/[3(2n+1)^2]\). Furthermore \((i-1)/n<2i/(2n+1)<i/n\) holds for all \(1\le i\le n\), so even an optimally designed one-per-cell rule attains this minimum. Dividing the exact formulas gives the claimed ratio.

**Fluctuations.** Set \(W_i=(1+U_i-U_{i-1})^3\) for \(i\ge2\). The sequence \((W_i)\) is bounded, stationary, and 1-dependent. Exact polynomial integrations with independent \(U,V,Z\sim\mathrm{Unif}(0,1)\) give
\[
\mathbb EW_i=\frac32,\quad \mathbb EW_i^2=\frac{127}{28},\quad \mathbb E(W_iW_{i+1})=\frac{449}{336}.
\]
Therefore \(\operatorname{Var}(W_i)=16/7\) and \(\operatorname{Cov}(W_i,W_{i+1})=-307/336\); all covariances at distance at least two vanish. The long-run variance is
\[
\sigma_W^2=\frac{16}{7}-2\frac{307}{336}=\frac{11}{24}>0.
\]
The bounded 1-dependent central limit theorem applies:
\(n^{-1/2}\sum_{i=2}^n(W_i-3/2)\Longrightarrow N(0,11/24)\). One direct justification partitions indices into blocks of length \(k_n=\lfloor n^{1/3}\rfloor\) separated by one deleted index. The retained block sums are independent; the deleted terms have variance \(O(n/k_n)\), while each centered block is bounded by \(O(k_n)=o(\sqrt n)\), yielding Lindeberg's theorem with the same limiting covariance. In the expression for \(12n^2V_n\), the endpoint terms are bounded and the centering error is \(O(1)\). Division by twelve gives variance \((11/24)/144=11/3456\). Finally, the strong law holds for the stationary 1-dependent variables by applying the independent strong law separately to their even and odd subsequences; bounded endpoints are negligible.

## Verification
The standalone \(VERIFY.py\) checks the five exact uniform-moment expressions, exact posterior-covariance identities for rational sample points, and optimal-grid formulas. Run from this directory with `python VERIFY.py`; `sympy` is required. Algebraic checks verify finite identities, not the infinite-dimensional bridge decomposition or limit theorem; these are proved above.

## Relationship to prior work
Briol et al. (2017) identify sensitivity of kernel quadrature to point-sampling design, but do not give this stratified Brownian posterior-variance law or its fluctuation coefficient. Foster, Lyons and Oberhauser (2019) study polynomial approximation of Brownian paths and bridge-integral structure, not one-per-cell sampling efficiency. Li et al. (2022) examine multilevel Gaussian-process quadrature, including the Brownian kernel and Latin-hypercube comparison in an experiment, but not these exact finite-budget, design-optimality and central-limit constants. The bridge-covariance formula and convex design optimization are standard ingredients, not independently asserted new results. The contribution assessed here is the linked exact random-grid calculation, \(3/2\) design-loss limit, and explicit \(11/3456\) fluctuation constant.

## Limitations
No minimax claim over unknown integrands is made. The deterministic optimum is specific to the Brownian covariance prior and noiseless integral estimation. Similar formulas may exist under stochastic-process experimental-design terminology not captured by the inspected sources; publication precedence remains subject to independent review. The central limit theorem assumes independent jitters and makes no robustness claim under correlated or adaptively sampled positions.

## References
- F.-X. Briol, C. J. Oates, J. Cockayne, W. Y. Chen, M. Girolami, *On the Sampling Problem for Kernel Quadrature*, arXiv:1706.03369, initial posting 2017-06-11, https://arxiv.org/abs/1706.03369.
- J. Foster, T. Lyons, H. Oberhauser, *An optimal polynomial approximation of Brownian motion*, arXiv:1904.06998, initial posting 2019-04-15, https://arxiv.org/abs/1904.06998.
- K. Li, D. Giles, T. Karvonen, S. Guillas, F.-X. Briol, *Multilevel Bayesian Quadrature*, arXiv:2210.08329, initial posting 2022-10-15, https://arxiv.org/abs/2210.08329.
