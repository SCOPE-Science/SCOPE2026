# Sharp simultaneous extremes and latent localization for shared-gamma products

## Finding

Let \(m\ge 2\) be fixed. Suppose that \(A\sim\operatorname{Gamma}(a,1)\) and \(B_i\sim\operatorname{Gamma}(b_i,1)\), \(1\le i\le m\), are mutually independent with \(a,b_i>0\); the second gamma parameter denotes **scale one**. Define \(X_i=AB_i\). For fixed positive directional thresholds \(w_1,\ldots,w_m\), write

\[
W=\sum_{i=1}^m w_i,\qquad
\nu=a+m-\sum_{i=1}^m b_i,\qquad
\beta=\frac{a+\sum_{i=1}^m b_i-m}{2}-\frac14.
\]

For \(E_t=\{X_i>w_it\text{ for all }1\le i\le m\}\), the **exact leading joint-tail constant** is

\[
\Pr(E_t)\sim
\frac{\sqrt\pi\,W^{\nu/2-1/4}\prod_{i=1}^m w_i^{b_i-1}}
{\Gamma(a)\prod_{i=1}^m\Gamma(b_i)}
\,t^\beta\exp(-2\sqrt{Wt})\quad(t\to\infty).
\]

Moreover, let \(G_t\) have density on \((0,\infty)\) proportional to
\(x^{\nu-1}\exp(-x-Wt/x)\). The conditional common-factor law satisfies

\[
d_{\mathrm{TV}}\bigl(\mathcal L(A\mid E_t),\mathcal L(G_t)\bigr)
=O(t^{-1/4}),\qquad
\frac{A-\sqrt{Wt}}{(Wt)^{1/4}}\,\bigg|\,E_t
\ \Longrightarrow\ N(0,1/2).
\]

Thus an unusually high common gamma factor is concentrated at \(\sqrt{Wt}\), with fluctuations of order \(t^{1/4}\), rather than at order \(t\).

Let \(F_i\) be the continuous CDF of \(X_i\). The logarithmic multivariate upper-orthant dependence exponent satisfies

\[
\lim_{u\downarrow0}
\frac{\log\Pr\{F_i(X_i)>1-u\ \text{for every }i\}}{\log u}
=\sqrt m.
\]

In particular, the reciprocal log-tail exponent is \(1/\sqrt m\) regardless of the gamma shape parameters. This last exponent is an implication of more general random-scale tail theory in the bivariate case; it is included as a consequence, not asserted as independently novel.

## Assumptions and scope

All gamma variables use unit scale. The integer \(m\), all gamma shapes, and all direction weights \(w_i\) stay fixed while \(t\to\infty\). No uniformity is asserted as \(m\), shapes, or weights vary. Thresholds must be strictly positive; zero-direction faces reduce dimension and require a different statement. These are upper tails of **products**, not ratios or inverse-gamma frailty mixtures.

## Proof

**Step 1: conditional representation.** Write \(Q_b(z)=\Gamma(b,z)/\Gamma(b)\) for the survival function of \(\operatorname{Gamma}(b,1)\). Conditioning on \(A=x\), independence gives the exact integral

\[
\Pr(E_t)=\frac1{\Gamma(a)}\int_0^\infty
x^{a-1}e^{-x}\prod_{i=1}^m Q_{b_i}(w_it/x)\,dx.
\]

For each fixed \(b>0\), elementary integration by parts (or the incomplete-gamma expansion) gives \(Q_b(z)=z^{b-1}e^{-z}\Gamma(b)^{-1}(1+O(z^{-1}))\) as \(z\to\infty\). This holds for noninteger and subunit positive \(b\) as well.

**Step 2: uniform saddle region.** On \(t^{1/4}\le x\le t^{3/4}\), all \(w_it/x\ge w_it^{1/4}\), so the product of gamma survivals equals

\[
\frac{t^{\sum b_i-m}\prod_iw_i^{b_i-1}}
{\prod_i\Gamma(b_i)}
\,x^{m-\sum b_i}\exp(-Wt/x)\,[1+O(t^{-1/4})],
\]

uniformly there. Outside this interval, the contribution to the original integral is exponentially negligible relative to \(e^{-2\sqrt{Wt}}\) times any fixed power of \(t\). Indeed \(x>t^{3/4}\) is controlled by the gamma tail of \(A\), while \(x<t^{1/4}\) is controlled by the gamma tail of any one \(B_i\). The same holds for the comparison integral from Step 3. All constants can depend on the fixed parameters.

**Step 3: exact Bessel saddle integral.** It follows that

\[
\Pr(E_t)=\frac{t^{\sum b_i-m}\prod_iw_i^{b_i-1}}
{\Gamma(a)\prod_i\Gamma(b_i)}
\int_0^\infty x^{\nu-1}e^{-x-Wt/x}\,dx\,[1+O(t^{-1/4})].
\]

The classical modified-Bessel identity, valid for every real \(\nu\), is

\[
\int_0^\infty x^{\nu-1}e^{-x-Wt/x}\,dx
=2(Wt)^{\nu/2}K_\nu(2\sqrt{Wt}).
\]

Since \(K_\nu(z)\sim\sqrt{\pi/(2z)}e^{-z}\), multiplication of the exponents and prefactors gives precisely the displayed \(\beta\), power of \(W\), weight product, and \(\sqrt\pi\) constant. In particular, the comparison integral asymptotic is nonzero, so the negligible-tail and relative-error bounds are valid.

**Step 4: conditional localization.** The numerator density of \(A\) given \(E_t\) is \(x^{a-1}e^{-x}\prod_iQ_{b_i}(w_it/x)\), up to normalization. Step 2 shows that this density, after normalization, differs in total variation by \(O(t^{-1/4})\) from the generalized-inverse-Gaussian comparison density \(x^{\nu-1}e^{-x-Wt/x}\). To determine its limit, set \(s=\sqrt{Wt}\) and \(x=s+s^{1/2}z\). Uniformly for bounded \(z\),

\[
x+\frac{Wt}{x}=2s+z^2+O(s^{-1/2}|z|^3),
\]

and \(x^{\nu-1}/s^{\nu-1}\to1\). The rescaled densities therefore converge to \(\pi^{-1/2}e^{-z^2}\); outside a fixed rescaled window tightness follows from the strict convex saddle \(y+y^{-1}\) minimized uniquely at \(y=1\). Hence the centered and scaled conditional factor converges weakly to \(N(0,1/2)\).

**Step 5: copula exponent.** Taking \(m=1\) in the same integral calculation (only for this intermediate marginal calculation) gives \(\log\Pr(X_i>t)=-2\sqrt t+O(\log t)\). Consequently, if \(q_i(u)=F_i^{-1}(1-u)\), then \(q_i(u)\sim\tfrac14[\log(1/u)]^2\). For every fixed \(\epsilon\in(0,1)\), all \(q_i(u)\) eventually lie between \((1-\epsilon)L^2/4\) and \((1+\epsilon)L^2/4\), where \(L=\log(1/u)\). Sandwich the common-quantile joint survival between the equal-direction survival functions at those two thresholds, apply Step 3, and let \(\epsilon\downarrow0\). This yields \(\log\Pr(\text{joint quantile exceedance})\sim-\sqrt m L\), which is the stated log-tail exponent. This comparison proves a logarithmic exponent only; it does not claim a particular slowly varying multiplier in the quantile parametrization.

## Verification

`verify.py` evaluates the exact finite Bessel-\(K\) sum for integer \(b_i\), compares it with independent numerical integration of the conditional survival integral, and checks convergence of exact-tail ratios for both equal and unequal directional thresholds. It also checks the conditional generalized-inverse-Gaussian mean and variance in an exactly soluble subcase. Run `python verify.py` after installing the scientific dependency recorded in `requirements.txt`. The tests are finite diagnostics; Steps 1–5 establish the infinite-parameter conclusions.

For positive **integer** \(b_i\), the survival polynomial \(Q_{b_i}(z)=e^{-z}\sum_{r=0}^{b_i-1}z^r/r!\) supplies an independent exact finite formula for every \(t>0\):

\[
\Pr(E_t)=\frac2{\Gamma(a)}\sum_{0\le r_i<b_i}
\left(\prod_{i=1}^m\frac{(w_it)^{r_i}}{r_i!}\right)
(Wt)^{(a-\sum_i r_i)/2} K_{a-\sum_i r_i}(2\sqrt{Wt}).
\]

This finite identity serves as an additional check on the asymptotic normalization.

## Relationship to prior work

Baricz, Prabhu, Sahoo and Singh (2026, arXiv:2610.37725v1) analyze the univariate gamma–gamma product law, including the univariate sharp survival equivalent in their Section 3 and Bessel identities. Their result covers the \(m=1\) marginal calculations, which are not claimed as new. Their paper does not establish the anisotropic simultaneous exceedance constant or the conditional shared-factor localization for fixed \(m\ge2\).

Engelke, Opitz and Wadsworth (2019) develop extremal dependence for general common-random-scale vectors; their Proposition 8 and Example 10 already imply the **bivariate residual exponent** \(1/\sqrt2\) in the independent exponential-tailed factor case. Accordingly the residual exponent here is treated as a contextual corollary, not the central novelty. Their results characterize dependence rates, not the exact heterogeneous gamma-shape and direction-dependent high-orthant prefactor or its conditional latent-factor total-variation approximation.

Zhang, Matthaiou, Karagiannidis and Dai (2015/2016, arXiv:1505.06685, especially Section II-C) derive joint distributions for gamma–gamma vectors formed by independent coordinatewise gamma factors paired with correlated multivariate gamma components. Their covariance-matrix model does not directly include the rank-one *identical* common gamma factor with arbitrary separate \(b_i\) considered here; the exact joint CDF formulas are different, and no claimed asymptotic equivalence follows directly from those formulas. Arnold and Arvanitis (2021) consider copulas built from **ratios** of gamma sums, also a different construction.

The older literature remains a real priority risk for the precise simultaneous-tail constant; the comparisons here concern the statements and parameter assumptions, not merely titles.

## Limitations

No assertion of independent verification or exhaustive literature priority is made. The fixed-dimensional large-threshold regime does not establish a limit with growing dimension or weights approaching zero. The conditional weak limit does not supply a uniform finite-sample error for arbitrary parameters. Even though the exact prefactor and latent-factor approximation appear absent from the closely inspected sources, a different earlier common-factor product-tail theorem could subsume them; external historical review is needed. Source titles and abstracts alone are not used to certify absence.

## References

1. Á. Baricz, D. Prabhu K., S. Sahoo, S. Singh, *The NWU ageing property of the gamma-gamma distribution*, arXiv:2610.37725v1 (2026-10-27). https://arxiv.org/html/2610.37725v1
2. S. Engelke, T. Opitz, J. Wadsworth, *Extremal dependence of random scale constructions*, Extremes 22 (2019), 623–666; arXiv:1803.04221. https://doi.org/10.1007/s10687-019-00353-3
3. J. Zhang, M. Matthaiou, G. K. Karagiannidis, L. Dai, *On the Multivariate Gamma-Gamma Distribution with Arbitrary Correlation and Applications in Wireless Communications*, IEEE Transactions on Vehicular Technology 65 (2016), 3834–3840; arXiv:1505.06685. https://arxiv.org/abs/1505.06685
4. B. C. Arnold, M. Arvanitis, *On a general class of gamma based copulas*, Dependence Modeling 9 (2021), 374–384. https://doi.org/10.1515/demo-2021-0117
5. NIST Digital Library of Mathematical Functions, modified-Bessel integral representations and large-argument asymptotics, §§10.32, 10.40. https://dlmf.nist.gov/10
