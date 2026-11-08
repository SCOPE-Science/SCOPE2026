# A sharp finite-ensemble risk singularity for positive Bernoulli Gram control variates

## Finding

For every fixed integer \(\nu\ge2\), there is a family of three-row, one-column leverage-score Bernoulli Gram sketches with all physical and control parameters in \([1,3]\), and with control-parameter error tending to zero, for which the same-ensemble empirical-covariance control-variate estimator has mean-square error diverging as the inverse of the squared control-parameter error. In contrast, a fixed, known coefficient gives a mean-square error tending to zero. The former produces a *negative* corrected scalar Gram estimate with an exact positive limiting probability, although the uncorrected Gram average is positive on every event responsible for this negative output.

More precisely, for \(0<\varepsilon<1/4\) set \(\delta=\sqrt\varepsilon\), \(U=3^{-1/2}(1,1,1)^{\mathsf T}\), \(T=\operatorname{diag}(2,2+\varepsilon,1)\), and \(P=\operatorname{diag}(2,2+\varepsilon+\delta,1)\). For \(\nu\) independent replicate sketches as defined below, write \(\widetilde Y_{\nu,\varepsilon}\) for the same-ensemble fitted control-variate scalar and \(Y_\varepsilon=U^{\mathsf T}PU=(5+\varepsilon+\delta)/3\). Then

\[
\lim_{\varepsilon\downarrow0}\varepsilon\,\mathbb E\bigl[(\widetilde Y_{\nu,\varepsilon}-Y_\varepsilon)^2\bigr]
=C_\nu:=\frac{A_\nu+16B_\nu}{9}>0,
\]
\[
\lim_{\varepsilon\downarrow0}\mathbb P(\widetilde Y_{\nu,\varepsilon}<0)
=A_\nu+B_\nu>0,
\]
where
\[
A_\nu=\left(\frac8{27}\right)^\nu-2\left(\frac4{27}\right)^\nu,
\qquad
B_\nu=\left(\frac4{27}\right)^\nu-2\left(\frac2{27}\right)^\nu.
\]
For \(\nu=2\), these constants are \(C_2=160/6561\) and \(A_2+B_2=40/729\). In the same construction the fixed-coefficient estimator with coefficient one is strictly positive and has exact mean-square error \(2\varepsilon/(9\nu)\).

## Assumptions and scope

The object is a scalar projected Gram matrix in the parameter-oblivious leverage-score Bernoulli setting. The orthonormal column \(U\in\mathbb R^{3\times1}\) has leverage scores \(\ell_i=1/3\). Choose expected per-replicate sampling budget \(c=1\), so the three Bernoulli inclusion probabilities are \(\eta_i=c\ell_i=1/3\). Independently for every replicate \(j=1,\ldots,\nu\) and row \(i=1,2,3\), draw \(\gamma_{ji}\sim\operatorname{Bernoulli}(1/3)\), and form the diagonal sketch \(S_j=\operatorname{diag}(\gamma_{j1}/\sqrt{\eta_1},\gamma_{j2}/\sqrt{\eta_2},\gamma_{j3}/\sqrt{\eta_3})\). (Since each indicator is binary, its square yields the correct inverse-probability weight.) The scalar sketches are
\[
T_j=U^{\mathsf T}T^{1/2}S_j^{\mathsf T}S_jT^{1/2}U
=2\gamma_{j1}+(2+\varepsilon)\gamma_{j2}+\gamma_{j3},
\]
\[
Y_j=U^{\mathsf T}P^{1/2}S_j^{\mathsf T}S_jP^{1/2}U
=T_j+\delta\gamma_{j2}.
\]
Thus \(\mathbb E T_j=\tau_\varepsilon=(5+\varepsilon)/3\) and \(\mathbb EY_j=Y_\varepsilon=\tau_\varepsilon+\delta/3\). Let \(\overline T\) and \(\overline Y\) be replicate averages, and define the standard same-ensemble ordinary-least-squares slope
\[
\widehat b=\frac{\sum_{j=1}^\nu (T_j-\overline T)(Y_j-\overline Y)}{\sum_{j=1}^\nu(T_j-\overline T)^2}
\]
when the denominator is positive; set \(\widehat b=0\) when it is zero. The corrected *forward* estimator is
\[
\widetilde Y_{\nu,\varepsilon}=\overline Y-\widehat b(\overline T-\tau_\varepsilon).
\]
The choice at ties is explicitly part of the definition. The result concerns this *pre-damping* scalar estimator, not a separately regularized inverse estimate, and requires fixed finite \(\nu\) as \(\varepsilon\downarrow0\). Both \(P\) and \(T\) are positive definite with all diagonals in \([1,3]\); moreover \(\|P-T\|_2=\delta\to0\).

## Proof

Let a row-selection pattern be \(g=(g_1,g_2,g_3)\in\{0,1\}^3\), of probability \((1/3)^{g_1+g_2+g_3}(2/3)^{3-g_1-g_2-g_3}\). Its control-sketch value is \(t_\varepsilon(g)=k(g)+\varepsilon g_2\), where the *integer base level* is \(k(g)=2g_1+2g_2+g_3\). Its physical sketch is \(y_\varepsilon(g)=k(g)+(\varepsilon+\delta)g_2\).

The eight patterns partition into base levels \(0,1,2,3,4,5\). Levels \(0,1,4,5\) contain one pattern each. Level \(2\) consists of \((1,0,0)\) and \((0,1,0)\), each of probability \(4/27\). Level \(3\) consists of \((1,0,1)\) and \((0,1,1)\), each of probability \(2/27\).

Define the *mixed level-two event* \(E_2\) on which all \(\nu\) patterns lie in the level-two pair and both patterns occur. Similarly define \(E_3\). Independence gives exactly
\[
\mathbb P(E_2)=\left(\frac8{27}\right)^\nu-2\left(\frac4{27}\right)^\nu=A_\nu,
\quad
\mathbb P(E_3)=\left(\frac4{27}\right)^\nu-2\left(\frac2{27}\right)^\nu=B_\nu.
\]
These probabilities are strictly positive for every \(\nu\ge2\).

On either \(E_k\) with \(k\in\{2,3\}\), the observed \(T_j\) take the two distinct values \(k\) and \(k+\varepsilon\), and the observed \(Y_j\) take the corresponding values \(k\) and \(k+\varepsilon+\delta\). Hence the sample slope is *exactly* \(\widehat b=(\varepsilon+\delta)/\varepsilon\), irrespective of their nonzero counts. Substitution into the correction yields
\[
\widetilde Y_{\nu,\varepsilon}
=\tau_\varepsilon-\frac{\delta}{\varepsilon}(k-\tau_\varepsilon),
\qquad
\widetilde Y_{\nu,\varepsilon}-Y_\varepsilon
=-\frac{\delta}{\varepsilon}\left(k-\frac53\right).
\]
(The second identity follows by cancelling the two terms in \(\delta/3\).) Therefore the squared errors on \(E_2,E_3\) are respectively \(1/(9\varepsilon)\) and \(16/(9\varepsilon)\), and the corrected Gram is negative on both events once \(\varepsilon\) is sufficiently small. Every \(T_j\) on these events is at least \(2\), so the uncorrected Gram average is strictly positive there.

It remains to show these are the *only* contributions to the leading risk and limiting negativity probability. There are finitely many ordered ensembles for fixed \(\nu\). If the observed integer levels \(k(g)\) are not all identical, the sample variance of \(T_j\) converges to a strictly positive integer-level sample variance. Because \(Y_j-T_j=\delta g_{j2}\), the fitted slope converges to one, and \(\widetilde Y_{\nu,\varepsilon}\to5/3\). These outcomes give bounded squared errors and are eventually positive. If all integer levels coincide and the \(g_{j2}\) values vary, the only possible classes are exactly \(E_2\) and \(E_3\). Otherwise all patterns are identical; then \(T_j\) is constant, the tie convention gives \(\widehat b=0\), and the corrected estimator is the nonnegative single-sketch value \(Y_j\) with bounded error. Since the ensemble space is finite, multiplying the expected squared error by \(\varepsilon\) and passing to the limit leaves only the two mixed-level contributions, proving the displayed \(C_\nu\). The same trichotomy proves the exact limiting negativity probability \(A_\nu+B_\nu\).

Finally, the fixed control coefficient \(b=1\) instead gives
\[
\widetilde Y^{(1)}=\overline Y-(\overline T-\tau_\varepsilon)=\tau_\varepsilon+\delta\,\frac1\nu\sum_{j=1}^\nu\gamma_{j2}>0,
\]
so by independence and \(\operatorname{Var}(\gamma_{j2})=2/9\),
\[
\mathbb E[(\widetilde Y^{(1)}-Y_\varepsilon)^2]=\frac{2\delta^2}{9\nu}=\frac{2\varepsilon}{9\nu}.
\]
This proves the claimed separation without invoking a numerical or asymptotic regression approximation. In fact, the population-optimal fixed coefficient is \(1+\delta(2+\varepsilon)/(5+(2+\varepsilon)^2)\), whose error is smaller still.

## Verification

The accompanying standard-library `checker.py` enumerates *all* eight Bernoulli row patterns and all multinomial replicate histograms for \(\nu\in\{2,3,4\}\). It computes finite-parameter mean-square error and negative-sketch probability with exact rational arithmetic at \(\varepsilon=1/m^2\), \(m\in\{10,30,100\}\), checks the negative probability against the derived rational value, and checks convergence of scaled risk to the predicted constant. It reports `CHECKS_OK`. The analytic partition and cancellation argument, not this finite test, establishes every integer \(\nu\ge2\) and the limiting assertions.

## Relationship to prior work

Polydorides, Wu, Noori, Vandierendonck and Woods (2026) introduce parameter-oblivious leverage-score Bernoulli Gram sketches and a same-ensemble control-variate correction (their equations (23)–(25) and (51)–(54)); they note that empirical control weights may be noisy and that corrected Gram sketches need not remain positive definite. The present result specializes the natural sample-covariance/sample-variance implementation to the smallest nontrivial row family and quantifies an *exact fixed-ensemble singular limit* despite bounded, strictly positive physical coefficients and an arbitrarily accurate control matrix. It does not claim novelty for ordinary regression estimation, the control-variate principle, or the general possibility of losing positive definiteness.

Portier and Segers (2018, Sections 2–3) analyze same-sample ordinary-least-squares control variates and establish large-sample asymptotics under nondegeneracy conditions. Those statements take sample size to infinity and do not provide the fixed-\(\nu\), nearly-tied Bernoulli-sketch risk coefficient or negativity probability above. Glynn and Szechtman (2002) treat control-variate coefficient estimation and limit theory more generally; the present narrowly identified numerical-sketch specialization should not be interpreted as a new general regression theorem.

## Limitations

The failure concerns an *uncapped*, sample-covariance/sample-variance estimate of the control weight computed from the same ensemble; different coefficient estimators, deterministic coefficients, clipping, or subsequent positive-definiteness damping are not covered. The Bernoulli parameter \(c=1\) is the minimal expected sample budget and some individual uncorrected sketches may be zero, although the problematic mixed-level events all have a strictly positive uncorrected average. The singular limit holds for every *fixed* finite ensemble size, not necessarily for ensemble sizes growing with \(\varepsilon^{-1}\). The result is a scalar Gram-estimation statement, not a complete FEM solution-error or inverse-estimation theorem. Novelty remains subject to further historical literature review and independent mathematical audit.

## References

1. N. Polydorides, Y. Wu, H. Noori, H. Vandierendonck and R. Woods, *Low-Variance Randomised Numerical Linear Algebra for Finite Element Simulation*, arXiv:2606.08817v1, publicly posted 7 June 2026. https://arxiv.org/html/2606.08817
2. F. Portier and J. Segers, *Monte Carlo integration with a growing number of control variates*, arXiv:1801.01797, 2018. https://arxiv.org/abs/1801.01797
3. P. W. Glynn and R. Szechtman, *Some New Perspectives on the Method of Control Variates*, in *Monte Carlo and Quasi-Monte Carlo Methods 2000*, Springer, 2002, pp. 27–49. https://web.stanford.edu/~glynn/papers/2002/GSzechtman02.html
