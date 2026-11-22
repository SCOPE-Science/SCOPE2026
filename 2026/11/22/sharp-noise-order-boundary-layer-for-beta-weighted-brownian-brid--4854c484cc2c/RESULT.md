# Sharp noise-order boundary layer for Beta-weighted Brownian-bridge one-point quadrature

## Finding

For every positive integer \(n\), let \(B\) be a standard zero-endpoint Brownian bridge and define the normalized, endpoint-concentrating polynomial moment
\[
A_n=n\int_0^1s^{n-1}B_s\,ds.
\]
We determine the unique optimal time for **one point measurement** of this integral, the exact Bayes risk, and a sharp transition between noiseless and noisy high-order designs. If the observation has independent Gaussian variance \(\eta\ge0\), the unique optimal time is the interior solution of
\[
2\eta+t-2(n+1)\eta t^n-(2n+1)t^{n+1}+2nt^{n+2}=0.
\]
Writing \(t_n=t_n(\eta)\), \(c=1.256431208626169677\ldots\), the strictly positive solution of \(e^c=1+2c\), and \(\rho_n\) for the optimally explained fraction of the prior variance, the limiting regimes are
\[
\begin{aligned}
\eta=0:&\quad n(1-t_n)\to c,\quad\rho_n\to\frac{2(1-e^{-c})^2}{c}=0.814528755178\ldots;\\
\eta>0\text{ fixed}:&\quad n(1-t_n)=\log n+\log\frac{2\eta}{1+2\eta}+o(1),\quad\rho_n\sim\frac{2}{\eta n};\\
n\eta_n\to\alpha<\infty:&\quad n(1-t_n)\to u_\alpha,\quad\rho_n\to\frac{2(1-e^{-u_\alpha})^2}{u_\alpha+\alpha}.
\end{aligned}
\]
Here \(u_\alpha\ge c\) is the unique root of \(e^u=1+2u+2\alpha\) in \([c,\infty)\). Thus an arbitrarily small **fixed** measurement-noise variance moves the optimal location from a constant-over-order terminal layer to a logarithm-over-order terminal layer and causes asymptotic information collapse. For \(n>1\), increasing noise strictly moves the unique optimal point leftward; for \(n=1\) it is identically \(1/2\).

## Assumptions and scope

The field is a centered continuous Gaussian process on \([0,1]\) with covariance \(K(s,t)=\min(s,t)-st\). A single deterministic time \(t\in[0,1]\) is selected in advance, with observation \(Y_t=B_t+\sqrt\eta Z\), where \(Z\) is an independent standard normal random variable, and known noise variance \(\eta\ge0\). The functional \(A_n\) uses the probability density \(ns^{n-1}\) (a \(\operatorname{Beta}(n,1)\) law), with \(n\in\{1,2,\ldots\}\). Loss is unconditional mean-square error, minimized over every measurable estimator from this one observation. When \(\eta=0\), the deterministic endpoint observations contain zero information; the optimizer remains interior.

## Proof

**Exact posterior risk.** Direct integration against the bridge covariance gives
\[
C_n(t):=\operatorname{Cov}(A_n,B_t)=n\int_0^1s^{n-1}K(s,t)\,ds=\frac{t(1-t^n)}{n+1}.
\]
Applying the same identity once more yields
\[
V_n:=\operatorname{Var}(A_n)=n\int_0^1s^{n-1}C_n(s)\,ds=\frac{n^2}{(n+1)^2(2n+1)}.
\]
The Gaussian conditional-mean estimator is \(\widehat A_{n,t}=C_n(t)Y_t/[t(1-t)+\eta]\), and its exact Bayes risk is
\[
R_n(t,\eta)=V_n-\frac{t^2(1-t^n)^2}{(n+1)^2[t(1-t)+\eta]}.
\]
The endpoint values use the continuous value of the explained variance, zero at both endpoints, including when \(\eta=0\).

**Unique global location.** Differentiating the explained-variance term, canceling its strictly positive factors on \(0<t<1\), gives the sign of
\[
F_{n,\eta}(t)=2\eta+t-2(n+1)\eta t^n-(2n+1)t^{n+1}+2nt^{n+2}.
\]
For \(\eta>0\), the coefficient sequence of this polynomial, after zero coefficients are removed (and coincident monomials are combined when \(n=1\)), has at most two sign changes. Since \(F_{n,\eta}(0)>0\), \(F_{n,\eta}(1)=-2n\eta<0\), and \(F_{n,\eta}(t)\to+\infty\) as \(t\to\infty\), there is a root in \((0,1)\) and one in \((1,\infty)\). Descartes' rule of signs leaves no other positive root, counting multiplicities. Thus the sole interior root is simple, and is the unique global maximizer, since the information is positive inside and zero at the endpoints. If \(\eta=0\), factor \(F_{n,0}(t)=t f_n(t)\), where
\[
f_n(t)=1-(2n+1)t^n+2nt^{n+1}.
\]
Here \(f_n(0)=1\), \(f_n(1)=0\), and \(f_n'(1)=n>0\), so the function is negative immediately to the left of one and must have a root in \((0,1)\). Two coefficient sign changes and the already known root at one force precisely one such interior root. Its sign change proves global optimality. For \(n=1\), direct substitution gives \(t_1=1/2\) for every noise variance.

**Strict noise ordering.** For \(n>1\), write \(r_n=(n+1)^{-1/n}>1/2\). The derivative of \(F\) with respect to noise is \(2[1-(n+1)t^n]\); at \(t=r_n\) it vanishes, while \(F_{n,\eta}(r_n)=r_n n(2r_n-1)/(n+1)>0\). Consequently the optimizer obeys \(t_n(\eta)>r_n\) for finite \(\eta\), and \(\partial F/\partial\eta<0\) there. At its simple crossing \(\partial F/\partial t<0\), hence implicit differentiation gives \(dt_n/d\eta<0\). Dividing \(F\) by \(\eta\) and taking \(\eta\to\infty\) shows \(t_n(\eta)\downarrow r_n\).

**Exact order/noise balance.** Put \(u_n=n(1-t_n)\). At the unique optimizer the root equation is equivalent to
\[
t_n^{n}=\frac{t_n+2\eta_n}{t_n(1+2u_n)+2(n+1)\eta_n}.
\tag{1}
\]
For \(\eta_n=0\), the bound \(r_n<t_n<1\) gives \(0<u_n<n(1-r_n)\sim\log n\). To exclude \(u_n\to\infty\), use (1) and \((1-u_n/n)^n\le e^{-u_n}\): because its right-hand side is of order \((1+2u_n)^{-1}\) for \(u_n=O(\log n)\), an unbounded \(u_n\) would force \(e^{u_n}=O(1+2u_n)\), a contradiction. Every subsequential limit then solves \(e^u=1+2u\). The positive solution \(c\), rather than zero, follows directly by the zero-noise first-order equation and its unique nontrivial interior maximizer: equivalently, testing \(t=1-c/n\) yields a limiting explained fraction greater than zero, whereas \(u_n\to0\) would make it vanish. Thus \(u_n\to c\).

If \(n\eta_n\to\alpha\in[0,\infty)\), (1) similarly first forces \(u_n\) bounded and then gives \(e^u=1+2u+2\alpha\). Since larger noise moves the optimizer left, \(u_n\) is no smaller than its noiseless counterpart; the unique solution in \([c,\infty)\) is \(u_\alpha\). If instead \(\eta>0\) is fixed, the bound \(t_n>r_n\) yields \(u_n=O(\log n)\), and (1) implies \(t_n^n=(1+2\eta+o(1))/[2\eta n(1+o(1))]\). Taking logarithms yields
\[
u_n=\log n+\log\frac{2\eta}{1+2\eta}+o(1).
\]
Finally the fraction explained is exactly
\[
\rho_n(t,\eta)=\frac{2n+1}{n^2}\,\frac{t^2(1-t^n)^2}{t(1-t)+\eta},
\]
which, with the three location limits, gives all asserted high-order information laws.

## Verification

The included \(\texttt{verify.py}\) independently performs exact rational integration identities for the point covariance and the integrated variance, high-precision root/bisection comparisons against dense grids, and numerical checks of the three asymptotic regimes. All executable checks passed with the included \(\texttt{verification\_output.txt}\). The uniqueness and limiting claims rely on the analytic argument above, not on finite sampling. Run using Python 3.9 or newer with \(\texttt{mpmath}\) version 1.3 or newer: `python verify.py`.

## Relationship to prior work

The Brownian-bridge covariance and Gaussian conditional-mean projection are standard; this paper does **not** claim their discovery. Foster, Lyons and Oberhauser (2019 preprint) study polynomial integral coordinates and optimal polynomial approximations of Brownian motion, motivating precisely the family of high-order polynomial moment functionals. They do not solve the single noisy point-location design or its order/noise crossover. Cai, Lam and Scarlett (2022) develop average-case bounds for noisy Bayesian quadrature, without this exact point-optimality and singular Beta-weight limit. Santin (2022) studies Brownian-bridge kernel power-function interpolation with multiple points in a distinct worst-case approximation criterion. Karvonen, Kanagawa and Särkkä (2019) give general stability and positivity results for Bayesian quadrature, not the present high-order single-point location theorem. A search of related mathematical research records did not identify an implication covering this entire theorem; this is not a claim of exhaustive historical novelty or independent priority certification.

## Limitations

Only one predetermined point, a known standard Brownian bridge, a normalized \(\operatorname{Beta}(n,1)\) integration weight, squared-error Bayes risk, and independent constant-variance Gaussian observation noise are considered. The crossover is stated for \(n\eta_n\to\alpha<\infty\); the fixed-positive-noise regime is treated separately. The theorem does not address arbitrary weights, unknown parameters, correlated sensors, multiple/adaptive observation, non-Gaussian noise, or minimax function-class quadrature. Comparisons to earlier sampling-design literature may reveal equivalent specialized formulations; historical priority should be checked independently.

## References

1. J. Foster, T. Lyons and H. Oberhauser, *An Optimal Polynomial Approximation of Brownian Motion*, arXiv:1904.06998 (public version 15 April 2019), https://arxiv.org/abs/1904.06998 .
2. X. Cai, C. T. Lam and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615 (2022), https://arxiv.org/abs/2202.10615 .
3. G. Santin, *A Brownian Bridge and the Reproducing Kernel Hilbert Space*, arXiv:2210.15959 (2022), https://arxiv.org/abs/2210.15959 .
4. T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, Statistics and Computing (2019), https://doi.org/10.1007/s11222-019-09901-0 .
