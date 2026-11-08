# Sharp heavy tails and a four-node mean-square threshold for unconstrained affine-exact random quadrature

## Finding

Let \(m\ge2\) and let \(X_1,\ldots,X_m\) be independent samples on \([0,1]\) with a bounded continuous probability density \(\rho\). Choose, without nonnegativity or conditioning restrictions, the unique minimum-Euclidean-norm vector of weights \(w=(w_1,\ldots,w_m)\) satisfying the exact moment equations
\[
\sum_{i=1}^m w_i=1,\qquad \sum_{i=1}^m w_i X_i=\tfrac12.
\]
Write \(W=\|w\|_2\), and let \(V_d=\pi^{d/2}/\Gamma(d/2+1)\) denote the Euclidean unit-ball volume. Then
\[
\lim_{t\to\infty}t^{m-1}\Pr\{W>t\}=C_m(\rho)
=\sqrt m\,V_{m-1}\int_0^1|u-\tfrac12|^{m-1}\rho(u)^m\,du>0.
\]
In particular, the exact positive-moment threshold is
\[
\mathbb E W^p<\infty\quad\Longleftrightarrow\quad 0<p<m-1.
\]
For uniformly sampled nodes, \(C_m(1)=V_{m-1}/(\sqrt m\,2^{m-1})\). If node evaluations are corrupted by independent centered errors with common variance \(\sigma^2\in(0,\infty)\), independent of the nodes, the conditional integration-error variance for the zero integrand is exactly \(\sigma^2W^2\). Consequently its unconditional mean-square error is infinite at \(m=2,3\) and finite at every \(m\ge4\).

## Assumptions and scope

All claims are for integers \(m\ge2\), iid abscissae in \([0,1]\) with density \(\rho\ge0\), continuous and bounded, integrating to one. With probability one the abscissae are not all equal, so the two affine moment equations are independent and the minimum-norm solution exists uniquely. The target integral is \(\int_0^1 f(u)\,du\), rather than integration against \(\rho\). The sampled nodes may follow a nonuniform density while the exactness moments remain the Lebesgue moments \(1\) and \(1/2\). No positivity constraint, rejection of poorly conditioned samples, or deterministic regularization is imposed. Noise is independent of positions and independent across evaluations, centered with finite common positive variance.

## Proof

**1. Minimum-norm weights.** Define \(\bar X=m^{-1}\sum_iX_i\), \(v_i=X_i-\bar X\), and \(S=\sum_i v_i^2>0\). The row space of the moment matrix is exactly \(\operatorname{span}\{(1,\ldots,1),v\}\), an orthogonal direct sum. The vector satisfying both moments within that row space is
\[
w_i=\frac1m+\frac{(\frac12-\bar X)v_i}{S},\qquad
W^2=\frac1m+\frac{(\frac12-\bar X)^2}{S}.
\]
Every other feasible vector differs by a vector orthogonal to that row space and therefore has strictly greater Euclidean norm unless identical. This proves uniqueness and the norm formula.

**2. Exact small-ball representation.** Let \(H=\{v\in\mathbb R^m:\sum_i v_i=0\}\) with its ordinary \((m-1)\)-dimensional Euclidean volume. The orthogonal decomposition \(x=z\mathbf1+v\), where \(z=m^{-1}\sum_i x_i\), has Jacobian \(\sqrt m\,dz\,dv\). For \(t>m^{-1/2}\), set \(a_t=\sqrt{t^2-1/m}\). The identity above gives
\[
W>t\quad\Longleftrightarrow\quad \|v\|_2<\frac{|z-\frac12|}{a_t}.
\]
Changing variables \(y=a_tv\) inside \(H\) gives the *exact* identity
\[
\begin{aligned}
a_t^{m-1}\Pr(W>t)
={}&\sqrt m\int_0^1\int_{\substack{y\in H\\\|y\|<|z-1/2|}}
\mathbf1_{\{z\mathbf1+y/a_t\in(0,1)^m\}}\\
&\qquad\prod_{i=1}^m\rho(z+y_i/a_t)\,dy\,dz.
\end{aligned}
\]
Outside the density support, the integrand is interpreted as zero. Every inner ball has radius at most \(1/2\), and its integrand is bounded by \(\|\rho\|_\infty^m\). For every interior \(z\in(0,1)\) and almost every \(y\) in this ball, the indicator eventually equals one and the density product tends to \(\rho(z)^m\). Dominated convergence therefore yields
\[
\lim_{t\to\infty}a_t^{m-1}\Pr(W>t)
=\sqrt m\,V_{m-1}\int_0^1|z-\tfrac12|^{m-1}\rho(z)^m\,dz.
\]
As \(a_t/t\to1\), this is also the asserted limit with \(t^{m-1}\). The constant is strictly positive because a continuous density with unit integral is positive on an interval containing points other than \(1/2\).

**3. Sharp moments and the noisy estimator.** The tail integral \(\mathbb E W^p=p\int_0^\infty t^{p-1}\Pr(W>t)\,dt\) and a strictly positive, finite tail constant imply exactly the cutoff \(p<m-1\), with logarithmic divergence at \(p=m-1\). When \(\rho\equiv1\), direct integration gives
\[
\int_0^1|z-\tfrac12|^{m-1}\,dz=\frac{1}{m2^{m-1}},
\quad C_m(1)=\frac{V_{m-1}}{\sqrt m\,2^{m-1}}.
\]
Finally, given the nodes, \(\sum_iw_i\eta_i\) is centered with variance \(\sigma^2\sum_iw_i^2=\sigma^2W^2\). Tonelli's theorem therefore gives unconditional mean-square error \(\sigma^2\mathbb EW^2\), infinite exactly when \(m\le3\) and finite for \(m\ge4\).

## Verification

The included standalone \(\texttt{check.py}\) reproduces exact-rational minimum-norm and moment identities for node sets of sizes \(2\) through \(8\), compares weights independently with numerical least squares, verifies independent noise variance identities, and performs limited Monte Carlo tail-scale checks for uniform nodes of sizes \(2,3,4\). The included \(\texttt{check_output.txt}\) contains the actual run output; **9,859 assertions passed**. The tail limit, all-density assertion and sharp moment cutoffs follow from the proof, not from finite simulation.

## Relationship to prior work

Van den Bos et al. (2018) construct exact positive-weight nested rules by nullspace selection. Migliorati and Nobile (2018) provide *conditioned* randomized least-squares cubature, using a tailored sampling measure and high-probability stability. Glaubitz (2020), particularly its section on minimizing the \(\ell^2\) norm of weights for **prescribed scattered nodes**, already establishes the deterministic minimum-norm mechanism and its numerical motivation; the formula for weights by itself is **not claimed as new**. Later work on well-conditioned randomized least-squares/positive rules further addresses *different protected schemes*. The assessed additional result is the **exact random-node Pareto tail coefficient for all bounded continuous densities and every \(m\ge2\)**, its necessary-and-sufficient moment cutoff, and the four-node unconditional noisy mean-square threshold for *unconstrained* affine moment fitting. No examined paper supplied this same tail-and-threshold theorem. The scope deliberately does not imply a failure of conditioned or positive rules.

## Limitations

The argument is univariate, affine-exact, and independent-node, with bounded continuous sampling density; no assertion is made for noncontinuous densities, multivariate high-degree moment fitting, rejection schemes, positive-weight enforcement, or arbitrary correlated noise. The mean-square divergence concerns independent *measurement noise*; it does not assert divergence of smooth deterministic integrand error. Similar inverse-small-ball phenomena may appear elsewhere, and specialist publication precedence is an acknowledged unresolved risk. The calculation and scientific assessment have not received independent audit.

## References

1. L. M. M. van den Bos, B. Sanderse, W. A. A. M. Bierbooms, G. J. W. van Bussel, *Generating nested quadrature rules with positive weights based on arbitrary sample sets*, arXiv:1809.09842, first posted 2018-09-26. https://arxiv.org/abs/1809.09842
2. G. Migliorati and F. Nobile, *Stable high-order randomized cubature formulae in arbitrary dimension*, arXiv:1812.07761, first posted 2018-12-19. https://arxiv.org/abs/1812.07761
3. J. Glaubitz, *Stable High Order Quadrature Rules for Scattered Data and General Weight Functions*, arXiv:2007.09082, first posted 2020-07-17. https://arxiv.org/abs/2007.09082
4. F. Bělík, A. Narayan and J. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506. https://arxiv.org/abs/2609.09506
5. S. Neumayer, M. Schäfer and T. Ullrich, *Random nodes with positive weights: Richter-Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699. https://arxiv.org/abs/2610.32699
