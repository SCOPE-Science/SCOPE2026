# Sharp joint precision and time design for Wiener-integral quadrature

## Finding
Let \(B\) be standard Brownian motion on \([0,1]\), with \(B(0)=0\), and let \(J=\int_0^1B(t)\,dt\). Fix an integer \(n\ge1\) and a total sensor precision \(P>0\). Choose in advance \(n\) times \(t_i\in[0,1]\) and precisions \(p_i>0\) summing to \(P\), and observe \(Y_i=B(t_i)+\varepsilon_i\), where the independent noises are \(\varepsilon_i\sim N(0,p_i^{-1})\) and are independent of \(B\). The loss is the unconditional mean-square error of the exact conditional-mean estimator \(\mathbb E[J\mid Y_1,\dots,Y_n]\).

Set \(A_P=1+P^{-1}\) and
\[
 d_{n,P}=\frac{1}{nA_P+\sqrt{n^2A_P^2-n^2+1/4}}.
\]
Among all such designs, including repeated sites and endpoint sites, the **unique** optimum up to simultaneous relabeling has
\[
 \boxed{\quad t_i=1-\bigl(n+\tfrac12-i\bigr)d_{n,P},\qquad
 p_i=\frac Pn,\qquad i=1,\ldots,n.\quad}
\]
All these sites are distinct and strictly interior, and the posterior-mean estimator is \(\widehat J=d_{n,P}\sum_{i=1}^nY_i\). Its exact minimum risk is
\[
 \boxed{\quad R_{n,P}=\frac{n d_{n,P}^3}{12}+\frac{(1-nd_{n,P})^3}{3}+\frac{n^2d_{n,P}^2}{P}.\quad}
\]
At every finite positive budget, the optimal risk decreases strictly with \(n\). As \(P\to\infty\), the nodes approach the known noiseless optimum \(t_i=2i/(2n+1)\), and \(R_{n,P}\to1/[3(2n+1)^2]\); the noiseless rule is **not** a new claim.

There is a nontrivial fixed-budget infinite-sensor limit. Define
\[
 c_P=A_P-\sqrt{A_P^2-1}\in(0,1),\qquad (1-c_P)^2=\frac{2c_P}{P}.
\]
As \(n\to\infty\), \(nd_{n,P}\to c_P\) and
\[
 \boxed{\quad R_{n,P}\longrightarrow R_{\infty,P}=\frac{(1-c_P)^3}{3}+\frac{c_P^2}{P}=\frac{(1-c_P)^2(2+c_P)}6.\quad}
\]
The optimal node array fills only the terminal interval \([1-c_P,1]\), asymptotically uniformly, while the equally distributed sensor precisions converge as a design measure to uniform precision density \(P/c_P\) on that interval. Thus, for every finite \(P\), even arbitrarily many point sensors optimally leave a nonempty initial time interval unobserved.

## Assumptions and scope
The Brownian covariance is known and exactly \(K(s,t)=\min(s,t)\). The observations are scalar, nonadaptive, and conditionally independent given the path, with freely selectable **Gaussian** measurement precisions and a linear cost \(\sum_i p_i=P\). The estimator is the exact Gaussian conditional mean, which minimizes risk among all measurable estimators of the observations, not merely linear estimators. The theorem does not allow arbitrary path-linear functionals as individual measurements. A zero-precision sensor, interpreted as unused, is permitted for comparison and cannot be part of an optimal design. No Bayesian hyperparameter fitting is included.

## Proof
**1. Gaussian error and optimal precision reduction.** By stochastic Fubini, \(J=\int_0^1(1-u)\,dB(u)\) and \(B(t_i)=\int_0^1\mathbf1_{\{u\le t_i\}}\,dB(u)\). For any deterministic coefficients \(a_i\), Itô isometry and independent noise give exactly
\[
 \mathbb E\left[\left(J-\sum_i a_iY_i\right)^2\right]
 =\int_0^1\left(1-u-\sum_{i:u\le t_i}a_i\right)^2du+\sum_i\frac{a_i^2}{p_i}.
\]
The conditional estimator is linear because the observations and target are jointly Gaussian. For fixed coefficients, Cauchy–Schwarz gives
\[
 \sum_i\frac{a_i^2}{p_i}\ge\frac{(\sum_i|a_i|)^2}{P},
\]
with equality, for all nonzero coefficients, precisely when \(p_i=P|a_i|/\sum_j|a_j|\). This reduction is valid before or after optimizing the linear estimator, since both are joint infima.

**2. Global monotone-step reduction.** Substitute \(x=1-u\) and write \(h(x)=\sum_{i:1-t_i\le x}a_i\). This is a step function with at most \(n\) jumps, counting a possible jump at \(x=0\), whose total variation from the left baseline zero is at most \(\sum_i|a_i|\). Hence the joint optimization reduces exactly to minimizing
\[
 \int_0^1(x-h(x))^2dx+\frac{\operatorname{TV}_0(h)^2}{P}
 \tag{1}
\]
over such step functions, with \(\operatorname{TV}_0\) including a jump at zero if present. Every candidate step function is realized by sensors and coefficients, and the Cauchy–Schwarz precision assignment attains its penalty.

Clipping the step values to \([0,1]\) weakly decreases the squared-error term pointwise and cannot increase variation. The nondecreasing rearrangement of the resulting finitely many step levels preserves their distribution, so it preserves \(\int h^2\) and \(\int h\), while the strict rearrangement inequality for the strictly increasing target \(x\) maximizes \(\int xh\) uniquely at nondecreasing \(h\), up to null sets. Rearrangement does not increase the number of jumps or \(\operatorname{TV}_0\), which for a nonnegative nondecreasing function is its largest level. Thus every global minimizer must be nonnegative and nondecreasing. If its first positive level occupies the left endpoint, moving its first jump from zero to the midpoint between zero and that level strictly improves the squared error without changing the variation. Therefore the optimal step has a positive-length initial zero segment, followed by increasing positive levels \(0<q_1<\cdots<q_k<1\). The strict upper bound follows because clipping rules out values above one, while lowering a top level equal to one reduces both its positive noise penalty and its squared error.

All available \(n\) levels are used. Indeed, for any optimum with \(k<n\), the first positive jump from zero to \(q_1\) is optimally located at \(b_1=q_1/2>0\). Inserting a small level strictly between zero and \(q_1\) on a nonempty subinterval of \((0,b_1)\) reduces its squared-error integral. The top level, and therefore the variation penalty, are unchanged. This contradicts optimality with fewer than \(n\) jumps. Repeated, zero-weight or zero-precision sensors cannot tie.

**3. Stationarity and uniqueness.** Number the optimal positive levels in increasing \(x\)-order as \(q_1,\dots,q_n\), and put \(q_0=0\). Let \(b_j\) be the jump from \(q_{j-1}\) to \(q_j\). For fixed levels, the squared-error term uniquely chooses
\[
 b_j=\frac{q_{j-1}+q_j}{2},\qquad j=1,\dots,n.
\]
The variation penalty equals \(q_n^2/P\). Differentiating with respect to each intermediate positive level, for \(1\le j<n\), gives the centroid condition \(q_j=(b_j+b_{j+1})/2\). Combining these equations forces \(q_j=j d\) for one \(d>0\). The top-level stationarity is
\[
 \int_{b_n}^1(q_n-x)\,dx+\frac{q_n}{P}=0,
\]
which becomes
\[
 (1-nd)^2-\frac{d^2}{4}=\frac{2nd}{P}. \tag{2}
\]
Its left-minus-right side is strictly decreasing on \(0<d<1/n\), is positive at zero and negative at \(1/n\). Thus there is exactly one admissible solution. Solving the quadratic gives \(d=d_{n,P}\) as displayed. Since the feasible design space admits a minimizer after allowing zero precisions and coincident sensors, and all those degeneracies were excluded above, every minimizer must equal this unique interior stationary design.

Returning to observation time, the jumps are at \(b_j=(j-1/2)d\); their inverse-time positions are precisely the displayed \(t_i\). Every jump has size \(d\), so equality in the precision Cauchy–Schwarz bound forces \(p_i=P/n\) and coefficients \(a_i=d\). This proves both the unique design and the posterior estimator.

**4. Risk and limiting laws.** The lower zero segment, all interior cells and the upper terminal cell contribute
\[
 \int_0^1(x-h(x))^2dx=\frac{nd^3}{12}+\frac{(1-nd)^3}{3}.
\]
Adding the noise penalty \(n^2d^2/P\) proves the exact risk. A design using \(n\) jumps is strictly better than one using at most \(n-1\) by the splitting argument, hence \(R_{n+1,P}<R_{n,P}\). When \(P\to\infty\), equation (2) and \(0<d<1/n\) imply \(d\to2/(2n+1)\). When \(n\to\infty\) at fixed \(P\), the explicit formula yields \(nd\to c_P\); the remaining stated limits follow by substitution and the endpoint formulas for \(t_i\). The relation \((1-c_P)^2=2c_P/P\) reduces the limit risk to its second displayed expression.

## Verification
The standalone `verify.py` reproduces the exact scalar optimality identity, the covariance normal equations for every equally weighted optimal design, the rational \((n,P)=(2,1)\) example, the noiseless formula and supplementary numeric covariance/risk comparisons. From this directory, install `requirements.txt` and execute `python verify.py`. One exact example is \(n=2,P=1\): optimal times \((4/5,14/15)\), precisions \((1/2,1/2)\), both estimator weights \(2/15\), and Bayes risk \(137/675\). Direct covariance integration gives \(\operatorname{Var}(J)=1/3\), \(\operatorname{Cov}(J,B(t))=t-t^2/2\), and \(\operatorname{Cov}(B(s),B(t))=\min(s,t)\). These independently verify the proposed estimator and risk for any finite array.

## Relationship to prior work
The Brownian noiseless optimal grid \(t_i=2i/(2n+1)\) and its variance \(1/[3(2n+1)^2]\) were already established in *Exact design loss and Gaussian fluctuations for stratified Brownian kernel quadrature* (2026). They are used here only as a limiting consistency check. Karvonen, Kanagawa and Särkkä (2018) discuss Brownian-kernel quadrature weights and general positivity theory, not the exact joint noisy node/precision optimization. Cai, Lam and Scarlett (2022) prove broad noisy-kernel integration error rates under a different sampling/noise-cost framework, not the present finite-\(n\), exact-Bayes, fixed-total-precision design. Pathiraja, Schillings and Wacker (2026) develop general sensor-budget filtering optimization, with a two-dimensional Brownian example targeting filtering covariance rather than this integral. A related Brownian-bridge precision allocation theorem assumes covariance \(\min(s,t)-st\) and estimates the bridge integral: its symmetric, centrally supported designs do not yield the one-sided, terminal-window Wiener design by substitution.

## Limitations
This is an exact statement for one specifically normalized Gaussian prior and one scalar path integral, under independent Gaussian noise and a continuous precision budget. It is not a worst-case assertion over deterministic integrands, not an adaptive-sensing theorem, and not an optimum over arbitrary linear path observations or nonlinear measurements. The strict fixed-budget initial exclusion interval is a limit of finite optimal designs; its interpretation as a general sensor-design law beyond this model is unproved. Publication priority remains subject to verification against older quadrature and Gaussian experimental-design literature that may use equivalent formulations.

## References
- T. Karvonen, M. Kanagawa, and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, first posted 20 December 2018, arXiv:1812.08509. https://arxiv.org/html/1812.08509v2
- X. Cai, C. T. Lam, and J. Scarlett, *Order-Optimal Error Bounds for Noisy Kernel-Based Bayesian Quadrature* (later titled *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*), first posted 22 February 2022, arXiv:2202.10615. https://arxiv.org/abs/2202.10615
- S. Pathiraja, C. Schillings, and P. Wacker, *An optimal experimental design approach to sensor placement in continuous stochastic filtering*, 2026, https://doi.org/10.1007/s11222-026-10855-3
- *Exact design loss and Gaussian fluctuations for stratified Brownian kernel quadrature* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-design-loss-and-gaussian-fluctuations-for-stratified-brown--f119d713d36c
