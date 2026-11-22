# Exact odd-budget minimax numerical differentiation under independent oracle noise

## Finding

Let \(n\geq3\) be odd, \(a,b>0\), and let \(x_0\in\mathbb R\). Among **all deterministic, nonadaptive linear estimators** \(\widehat g=\sum_{j=1}^n w_jY_j(x_0+\delta_j)\) formed from \(n\) independent noisy function calls with freely chosen real sites and weights, the exact minimax mean-square risk for the Taylor-remainder class specified below is

\[
R_n=\left(\frac{3a^2b^2}{16}\right)^{1/3}\left(\frac{n}{n^2-1}\right)^{2/3}.
\]

Every minimax design, up to permutation and reflection about \(x_0\), uses exactly two sites \(x_0-h_n\) and \(x_0+h_n\), with \(p=(n-1)/2\) calls at one and \(q=(n+1)/2\) at the other, and the equally weighted sample mean at each site:

\[
\widehat g=\frac{\overline Y_+-\overline Y_-}{2h_n},\qquad
h_n=\left(\frac{18b}{a^2}\frac{n}{n^2-1}\right)^{1/6}.
\]

The only permissible alternatives are interchanging the counts between sides or permuting call labels. Relative to the continuous-allocation lower bound of Lam--Li--Zhang, the exact unavoidable odd-budget penalty is \((n^2/(n^2-1))^{2/3}\). At \(n=3\), this factor is approximately \(1.08168718\); using the third call optimally lowers risk by \(1-(3/4)^{2/3}\approx17.4518\%\) relative to using just two calls. For even \(n\ge2\), balanced equal-count central differences attain the known bound \(R_n=(3a^2b^2/16)^{1/3}n^{-2/3}\); this even case is prior work and is not claimed as new.

## Assumptions and scope

The target is \(g=f'(x_0)\) for an unknown real-valued function with a second derivative at \(x_0\) and the *global anchored Taylor remainder* condition

\[
\left|f(x_0+u)-f(x_0)-f'(x_0)u-\frac{f''(x_0)}2u^2\right|\le\frac a6|u|^3\quad(u\in\mathbb R).
\]

A call at any selected site returns \(Y_j(x)=f(x)+\varepsilon_j(x)\), where the \(n\) observed errors are mutually independent, centered, and each has variance at most \(b\), including for repeated calls to the same site. A variance exactly \(b\) is admissible. No Gaussian assumption is required. The minimax criterion first takes the worst-case mean-square error over all admissible functions and independent oracle laws, then minimizes over deterministic sites and fixed real weights. The function value, target slope, and second derivative at \(x_0\) are unrestricted. No random or adaptive design, nonlinear estimator, correlated noise, or variable query cost is covered. A single call, \(n=1\), has infinite linear minimax risk.

## Proof

Translate \(x_0\) to zero. Since the constant, linear, and quadratic polynomials are in the function class with arbitrary coefficients, finite worst-case risk forces the exactness constraints

\[
\sum_j w_j=0,\qquad \sum_j w_j\delta_j=1,\qquad \sum_j w_j\delta_j^2=0.\tag{1}
\]

For repeated identical sites, replacing their weights by their common average preserves the estimator's noiseless response and its three moments, leaves its worst-case bias unchanged, and weakly reduces its variance. Thus minimizers can be taken with uniform weights within each repeated-site group. In particular, all nonzero weights attached to a given site have the same sign. Setting

\[
S=\sum_j|w_j|,\qquad C=\sum_j|w_j|\,|\delta_j|^3,
\]

an adversary may choose an anchored remainder with its signs aligned with the nonzero site-weight sums. This is achieved by bounded smooth interpolation away from zero, with remainder magnitude \(a|\delta_j|^3/6\) at each distinct nonzero selected site. Therefore, with all oracle variances equal to \(b\), every design has worst-case risk at least

\[
\frac{a^2}{36}C^2+b\sum_jw_j^2.\tag{2}
\]

The slope identity in (1) and Holder's inequality give

\[
1=\left|\sum_j w_j\delta_j\right|\le \sum_j|w_j\delta_j|\le C^{1/3}S^{2/3},\qquad C\ge S^{-2}.\tag{3}
\]

The zero-sum identity in (1) makes the positive and negative weight totals each \(S/2\). Let \(p'\) and \(q'\) be their nonzero counts, so \(p',q'\ge1\) and \(p'+q'\le n\). Cauchy--Schwarz applied separately to the two sign classes gives the integer-sharp estimate

\[
\sum_j w_j^2\ge \frac{S^2}{4}\left(\frac1{p'}+\frac1{q'}\right)
\ge \frac{S^2}{4}\left(\frac1{\lfloor n/2\rfloor}+\frac1{\lceil n/2\rceil}\right)
=\frac{n}{n^2-1}S^2\quad\text{for odd }n.\tag{4}
\]

Combining (2)--(4), and putting \(k_n=n/(n^2-1)\),

\[
\mathrm{MSE}\ge \frac{a^2}{36S^4}+bk_nS^2
\ge\left(\frac{3a^2b^2}{16}\right)^{1/3}k_n^{2/3},\tag{5}
\]

where the second equality is the exact positive-scalar minimum at \(S^6=a^2/(18bk_n)\).

For attainability, choose \(p=\lfloor n/2\rfloor\) independent calls at \(x_0+h\) and \(q=\lceil n/2\rceil\) at \(x_0-h\), with each plus-site weight \(1/(2ph)\) and each minus-site weight \(-1/(2qh)\). All constraints (1) hold. The anchored remainder bounds the worst-case bias by \(ah^2/6\), and a cubic function realizes this bias. The largest noise variance gives variance \(bk_n/h^2\). Hence the exact worst-case risk is

\[
\frac{a^2h^4}{36}+\frac{bk_n}{h^2},
\]

uniquely minimized at \(h^6=18bk_n/a^2\), giving (5) with equality.

Finally, all equality conditions are necessary. Strictness in the scalar minimization fixes \(S\). Equality in (4) requires all \(n\) weights nonzero, sign-group counts differing by one, and equal weights within each group. Equality in (3) requires every nonzero \(|\delta_j|\) to be the same and every \(w_j\delta_j\) to have positive sign. Thus all positive weights are at \(+h\), all negative weights at \(-h\), and their fixed totals force exactly the displayed centered-difference estimator. This proves the complete optimizer classification.

## Verification

The included `verify.py` reconstructs the closed-form risk formula symbolically; checks all polynomial moment constraints; verifies the exact optimum against the analytic derivative; and compares many finite arbitrary feasible stencil designs with the asserted lower bound. For every tested odd \(n\in\{3,5,7,9,11,13,15\}\), the constructed optimal split attains equality within floating-point tolerance. Numerical comparisons are supplementary and are not substituted for (1)--(5), which prove the statement over the full claimed domains.

## Relationship to prior work

Lam, Li and Zhang (arXiv:2007.04443, first publicly available 8 July 2020), Theorem 1, establish a minimax lower bound for all sample budgets and exact equality for **even** budgets through balanced central finite differences. Their Section 2.1 proves the same original zero-sum and Holder steps but uses an unrestricted \(n\)-term Cauchy--Schwarz inequality, which cannot be saturated at odd \(n\). The additional sign-partition integer inequality (4), exact odd risk, and the characterization of **all** odd minimizers are not contained in their stated theorem. The result neither contests nor claims their even-budget theorem. Earlier derivative-free optimization work by Berahas, Cao, Choromanski and Scheinberg (arXiv:1905.01332) analyzes noisy gradient approximations more generally but was available for this comparison only as abstract-level context; it is not used as evidence of whole-paper noncoverage.

## Limitations

This is an exact result for linear, deterministic, nonadaptive differentiation schemes and the anchored third-order remainder class only. It does not give the minimax risk among all nonlinear or adaptive procedures. The proof develops a short, natural refinement of the exact-in-even-budgets argument; a previously unlocated equivalent treatment of integer allocation remains possible. The relative odd-budget penalty decays as \(1+2/(3n^2)+O(n^{-4})\), so its chief practical impact is at small query budgets.

## References

1. H. Lam, H. Li, X. Zhang, *Minimax Efficient Finite-Difference Stochastic Gradient Estimators Using Black-Box Function Evaluations*, arXiv:2007.04443 (initial submission 8 July 2020), https://arxiv.org/abs/2007.04443, Section 2.1, Theorem 1 and its proof.
2. A. S. Berahas, L. Cao, K. Choromanski, K. Scheinberg, *A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization*, arXiv:1905.01332 (initial submission 3 May 2019), https://arxiv.org/abs/1905.01332. Contextual abstract-level comparison only.
