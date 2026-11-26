# Independent mathematical audit

## correctness

PASS

For fixed m, the CDF power gives r_k=p_k A_{m,k}, with 0<r_k<=m p_k. At small intensity the masses at zero and one are 1-m lambda+O(lambda^2) and m lambda+O(lambda^2). On all k>=2, monotonicity of -x log x for small x and r_k<=m lambda^k/k! bound the entire entropy remainder by O_m(lambda^2 log(1/lambda)); subtracting the parent expansion yields both coefficients and strict positivity near zero. At high intensity the standardized counts converge to independent normals, so the standardized maximum converges and its second moment converges by a uniform fourth-moment bound. The displayed central Stirling remainder is O(lambda^(-1/2)) in expectation. On the outside event, its probability under the parent or maximum is O_m(exp(-c lambda)); for lambda>=1 one can bound the absolute log mass globally by lambda+k log(lambda)+k^2, so Cauchy–Schwarz and raw Poisson moment bounds make that contribution vanish. For U_lambda=F_M, its CDF at u equals F_j^m for the last j with F_j<=u (or zero); the gap to u is at most the largest Poisson atom, which tends to zero. Thus U_lambda converges to Beta(m,1) and the bound P(-log U_lambda>t)<=exp(-mt) gives the needed uniform logarithmic integrability. Combining gives the stated Gaussian differential entropy difference, not merely weak convergence. Gaussian Poincare is strict because the maximum is not affine, so the variance is less than one and the Gaussian maximum-entropy inequality gives a strictly negative limiting constant. For m=2 the max/min symmetry gives second moment one and c_2=1/2-log 2. Locally uniform factorial entropy tails give continuity and the intermediate value conclusion. No uniqueness, rate uniform in m, or monotonicity is established. The numerical checker was inspected, not executed.

## originality

PASS

The supported new comparison is the fixed-sample Poisson maximum versus its own parent Shannon entropy across the intensity axis, with the two asymptotic formulas and strict opposite signs. Neither the order-statistic mass identity nor the parent or Gaussian entropy tools receive novelty credit.

## value

PASS

Retaining the maximum of replicated counts is a standard summary. The fixed-sample reversal says when this summary can have higher or lower marginal uncertainty than one original count, which prior mean and variance results do not answer. The endpoint coefficients quantify a structural comparison for every m, not a single numerical crossover or a claim that taking the maximum creates information about the full sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
