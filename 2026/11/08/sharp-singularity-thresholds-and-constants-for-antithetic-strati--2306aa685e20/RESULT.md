# Sharp singularity thresholds and constants for antithetic stratified quadrature

## Finding

For every real \(\beta>-1\), consider the power integrand \(f_\beta(t)=t^\beta\) on \((0,1]\), with integral \(I_\beta=1/(\beta+1)\). The antithetic stratified trapezoid with \(n\ge1\) equal panels and independent \(U_k\sim\mathrm{Uniform}(0,1)\) is
\[
R_{n,\beta}=\frac1{2n}\sum_{k=0}^{n-1}\left[\left(\frac{k+U_k}{n}\right)^\beta+\left(\frac{k+1-U_k}{n}\right)^\beta\right].
\]
It is unbiased for every \(\beta>-1\). Its exact variance is infinite for \(-1<\beta\le-1/2\); it is zero for \(\beta=0\) or \(\beta=1\). For the remaining \(\beta>-1/2\), let
\[
X_{k,\beta}(u)=\tfrac12[(k+u)^\beta+(k+1-u)^\beta],\qquad
m_{k,\beta}=\frac{(k+1)^{\beta+1}-k^{\beta+1}}{\beta+1},
\]
\[
v_{k,\beta}=\int_0^1[X_{k,\beta}(u)-m_{k,\beta}]^2\,du.
\]
Then \(\operatorname{Var}(R_{n,\beta})=n^{-2\beta-2}\sum_{k=0}^{n-1}v_{k,\beta}\), and its exact large-panel phase diagram is
\[
\operatorname{Var}(R_{n,\beta})\sim
\begin{cases}
C_\beta\,n^{-2\beta-2},&-\tfrac12<\beta<\tfrac32,\ \beta\notin\{0,1\},\\
\dfrac{\log n}{1280\,n^5},&\beta=\tfrac32,\\
\dfrac{\beta^2(\beta-1)^2}{720(2\beta-3)}\,n^{-5},&\beta>\tfrac32,
\end{cases}
\]
where \(C_\beta=\sum_{k=0}^\infty v_{k,\beta}\) is a well-defined, finite, strictly positive constant. The symbol \(\sim\) means the ratio tends to one as the integer \(n\to\infty\).

For comparison, use the same \(2n\) function evaluations but two *independent* uniform samples per panel, with their pair average denoted \(J_{n,\beta}\). Define
\[
t_{k,\beta}=\int_0^1(k+u)^{2\beta}\,du-m_{k,\beta}^2,\qquad
D_\beta=\sum_{k=0}^\infty t_{k,\beta}.
\]
For \(\beta>-1/2\), \(\operatorname{Var}(J_{n,\beta})=\tfrac12 n^{-2\beta-2}\sum_{k<n}t_{k,\beta}\); it vanishes at \(\beta=0\), while for all other \(\beta>-1/2\) it obeys
\[
\operatorname{Var}(J_{n,\beta})\sim
\begin{cases}
\tfrac12D_\beta\,n^{-2\beta-2},&-\tfrac12<\beta<\tfrac12,\ \beta\ne0,\\
\dfrac{\log n}{96\,n^3},&\beta=\tfrac12,\\
\dfrac{\beta^2}{24(2\beta-1)}\,n^{-3},&\beta>\tfrac12.
\end{cases}
\]
Thus antithetic pairing shifts the endpoint singularity threshold for smooth-rate saturation from \(\beta=1/2\) to \(\beta=3/2\). For every finite \(n\), its variance is minimal among all equal-weight, two-uniform-marginal estimators with *independent panels*: anti-coupling \((U,1-U)\) is the unique panelwise variance-minimizing coupling when \(\beta\ne0\) and \(\beta>-1/2\) (up to null sets). This restriction to independent panels matters; globally dependent cross-panel designs are not included.

For the standard smooth normalization, if \(f\in C^2([0,1])\), then the same antithetic rule satisfies
\[
\lim_{n\to\infty}n^5\operatorname{Var}(R_n(f))=\frac1{720}\int_0^1[f''(x)]^2\,dx.
\]
The exact polynomial benchmarks are \(\operatorname{Var}(R_{n,2})=1/(180n^5)\) and \(\operatorname{Var}(R_{n,3})=(4n^2-1)/(240n^7)\).

## Assumptions and scope

- The grid is \([k/n,(k+1)/n]\), \(k=0,\ldots,n-1\); panel random variables are independent and uniform, and there is one complementary pair per panel.
- The estimator uses two point evaluations per panel, hence \(2n\) evaluations total. The comparator uses two *independent* points per panel with the same sampling budget.
- \(\beta>-1\) is needed for integrability. For \(\beta<0\), the function value at \(t=0\) can be assigned arbitrarily because it is sampled with probability zero. Finite mean squared error additionally requires \(\beta>-1/2\).
- In the coupling-optimality assertion, each of the two sampling marginals is uniform *within its prescribed panel*, the two evaluations have equal fixed weights, and the panel pairs remain mutually independent. It is not a universal optimality claim over all numerical integration algorithms.
- The asymptotic results concern stochastic variance (which equals mean-square quadrature error here by unbiasedness), not almost-sure pathwise rates.

## Proof

**1. Unbiasedness, exact variance and the integrability boundary.** Each of \(U_k\) and \(1-U_k\) is uniform on \([0,1]\). Consequently the expectation of each panel contribution is its exact panel integral, giving \(\mathbb E R_{n,\beta}=I_\beta\). Extracting the powers of \(n\) and using independence across panels gives the displayed exact variance identity. The independent-pair identity follows by adding two independent one-point variances and dividing by four.

For \(-1<\beta\le-1/2\), the first panel contains a positive term proportional to \(U_0^\beta\), and the square of the whole nonnegative estimator dominates a positive multiple of \(U_0^{2\beta}\). The latter has infinite expectation. Yet its mean is finite. Thus the variance is infinite, regardless of any choice of the within-panel coupling with uniform marginals. When \(\beta>-1/2\), both sampled function values have finite second moments, so all finite-panel variances are finite. If \(\beta=0\), the function is constant; if \(\beta=1\), every complementary pair has the deterministic average \((k+1/2)/n\), yielding zero variance.

**2. A uniform local expansion and the sharp constant.** Fix real \(\beta\) and put \(c=k+1/2\) and \(T=U-1/2\), where \(\mathbb ET^2=1/12\), \(\mathbb ET^4=1/80\), and hence \(\operatorname{Var}(T^2)=1/180\). For integer \(k\ge1\), symmetric Taylor expansion uniformly for \(|T|\le1/2\) gives
\[
\tfrac12[(c+T)^\beta+(c-T)^\beta]
=c^\beta+\frac{\beta(\beta-1)}2c^{\beta-2}T^2+O_\beta(c^{\beta-4}).
\]
After subtraction of its expectation, the random part is
\[
\frac{\beta(\beta-1)}2c^{\beta-2}(T^2-1/12)+O_\beta(c^{\beta-4}),
\]
with a uniform remainder. Squaring, integrating, and controlling the cross term by Cauchy–Schwarz proves
\[
v_{k,\beta}=\frac{\beta^2(\beta-1)^2}{720}(k+1/2)^{2\beta-4}
+O_\beta((k+1/2)^{2\beta-6}). \tag{1}
\]
When \(\beta\in\{0,1\}\), the variance is exactly zero instead. For any other \(\beta\), \(u\mapsto X_{k,\beta}(u)\) is not constant: its derivative is \(\frac\beta2[(k+u)^{\beta-1}-(k+1-u)^{\beta-1}]\). Thus every \(v_{k,\beta}>0\).

For \(-1/2<\beta<3/2\), the exponent \(2\beta-4<-1\), and (1), with finite \(v_{0,\beta}\), proves absolute summability and the first asymptotic. At \(\beta=3/2\), the leading coefficient is \(1/1280\) and the sum of \((k+1/2)^{-1}\) through \(n-1\) is \(\log n+O(1)\); the remainder series is summable. For \(\beta>3/2\), the power-sum estimate \(\sum_{k<n}(k+1/2)^{2\beta-4}\sim n^{2\beta-3}/(2\beta-3)\) proves the remaining branch. The remainder in (1) is always lower order after summing (also at its own borderline). These are *infinite* asymptotic proofs, not extrapolations from finite experiments.

**3. The independent-pair comparator.** With the same centered \(T\), one-sided Taylor expansion yields
\[
t_{k,\beta}=\frac{\beta^2}{12}(k+1/2)^{2\beta-2}
+O_\beta((k+1/2)^{2\beta-4}),\qquad \beta\ne0.
\]
The same three power-sum cases, now at exponent \(2\beta-2=-1\) when \(\beta=1/2\), give the stated comparator laws. The factor \(1/2\) comes from averaging *two independent* samples per panel; it is essential to the equal-budget normalization.

**4. Sharp coupling choice.** Holding the two marginal uniform laws fixed holds each marginal second moment fixed. The only variable contribution to the variance of their equal-weight average is the cross moment. The strict rearrangement inequality for a strictly monotone real function states that \(\mathbb E[f(U)f(V)]\) is minimized by opposite-quantile coupling \(V=1-U\); for continuous strictly monotone laws it is unique up to null sets. Since \(u\mapsto(k+u)^\beta\) is strictly monotone whenever \(\beta\ne0\), this applies on every panel with finite second moments. Panel independence lets the panelwise minima add. No assertion is made about joint couplings across distinct panels.

**5. Smooth-function calibration.** Let \(c_k=(k+1/2)/n\) and \(T_k=U_k-1/2\). Uniform continuity of \(f''\) gives uniformly in \(k\) and \(T_k\)
\[
\tfrac12[f(c_k+T_k/n)+f(c_k-T_k/n)]
=f(c_k)+\frac{f''(c_k)}{2n^2}T_k^2+o(n^{-2}).
\]
Its variance is \(f''(c_k)^2/(720n^4)+o(n^{-4})\) uniformly. Multiplying by panel weights \(n^{-2}\), summing independently, and taking a midpoint Riemann sum gives the claimed \(1/720\) curvature-energy limit. The sharp power-family coefficient for \(\beta>3/2\) agrees with \(\int_0^1[f_\beta''(x)]^2dx/720\) whenever that integral is finite.

**6. Exact checks for integer powers.** For \(\beta=2\), the centered pair's random part is exactly \(T^2-1/12\); every unscaled panel has variance \(1/180\), yielding \(1/(180n^5)\). For \(\beta=3\), the centered pair's random part is \(3(k+1/2)(T^2-1/12)\), so its variance is \((k+1/2)^2/20\). Using \(\sum_{k=0}^{n-1}(k+1/2)^2=n(4n^2-1)/12\) gives \((4n^2-1)/(240n^7)\).

## Verification

The standalone \(\texttt{verify.py}\) (Python standard library only) checks exact polynomial moments and the closed forms for \(\beta=0,1,2,3\) over multiple cells and panel counts, including the equal-budget independent-pair linear benchmark. Deterministic midpoint numerical integrations of *centered* complementary pairs check the large-cell coefficient in (1) at the representative exponents \(5/4,3/2,7/4,2,3\). The executable printed \(552\) passed assertions when run from the actual package path; see \(\texttt{verification_output.txt}\). These tests are not substitutes for steps 1–5.

## Relationship to prior work

Wu, *A randomised trapezoidal quadrature*, arXiv:2011.15086 (first public 2020-11-30; later peer-reviewed in the *International Journal of Computer Mathematics*), introduced exactly the complementary-pair rule and proved Sobolev-class error bounds. Its numerical Example 1 specifically uses \(t^\gamma\) with \(\gamma\in\{5/4,3/2,7/4\}\). Its published Table 1 reports fitted root-mean-square orders approximately \(2.24,2.44,2.50\), respectively. Those data, the scheme, and general rate improvements are **prior art**. The present mathematical statement establishes exact finite-panel variance identities, a positive limiting series, the previously unquantified critical logarithm with coefficient \(1/1280\), the full sharp exponent ranges (including unbounded powers), and the exact equal-budget coupling comparison. It analytically explains, but does not claim discovery of, the source's numerical trend.

Owen, *Local antithetic sampling with scrambled nets* (2008), discusses classical antithetic sampling and smooth-function rate improvements, including the rate \(n^{-5/2}\) for one-dimensional locally antithetic stratification. That general rate is not new here. Kunsch, *Linear Monte Carlo quadrature with optimal confidence intervals* (2023), proves function-class confidence results for stratified control variates; it does not state this exact pointwise power-family variance law. The strict rearrangement principle used for coupling optimality is classical and not itself claimed as an original discovery.

The published positive-weight generalized Romberg quadrature result (2026-09-21) addresses deterministic extrapolation coefficients on nested grids, not random complementary-pair sampling. Its coefficient and noise-amplification assertions do not entail the power-law variance phase diagram established here. This is a statement-level comparison, not a claim of exhaustive priority verification.

## Limitations

The analysis is one-dimensional and requires independent panels. It does not optimize the number or lengths of panels, arbitrary sampling weights, cross-panel dependence, or alternative randomized algorithms. Constants in the summable regime are rigorously defined convergent series, not simplified elementary closed forms. The infinite-variance regime uses ordinary mean-square error; other tail-risk criteria could behave differently. The theorem does not claim novelty for complementary antithetic sampling itself, its generic \(n^{-5/2}\) smooth rate, or the source's empirical fitted exponents. Publication priority beyond the specifically inspected primary texts and searched published records remains subject to independent expert verification.

## References

1. Y. Wu, *A randomised trapezoidal quadrature*, arXiv:2011.15086 (submitted 2020-11-30), https://arxiv.org/pdf/2011.15086 ; peer-reviewed version *International Journal of Computer Mathematics* 99 (2022), 680–692, https://doi.org/10.1080/00207160.2021.1929194 .
2. A. B. Owen, *Local antithetic sampling with scrambled nets*, *Annals of Statistics* 36 (2008), 2319–2343, https://arxiv.org/pdf/0811.0528 ; https://doi.org/10.1214/07-AOS548 .
3. R. J. Kunsch, *Linear Monte Carlo quadrature with optimal confidence intervals*, arXiv:2309.09059 (submitted 2023-09-16), https://arxiv.org/pdf/2309.09059 .
4. *Positive-weight generalized Romberg quadrature for every integer refinement factor*, public mathematical result (2026-09-21), https://github.com/published-finding corpus/2026/tree/main/2026/9/21/SCOPE-generalized-romberg-positive-weights-integer-refinement--b7c2819b6648 .
