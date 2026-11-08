# A sharp mesh–sampling phase law for Sibuya Grünwald differentiation of polynomial past tails

## Finding

For every real \(0<\alpha<1\) and \(0<\beta<\alpha\), consider the one-sided power-tail test function
\[
f_\beta(t)=(-t)_+^\beta=\begin{cases}(-t)^\beta,&t<0,\\0,&t\ge0.\end{cases}
\]
At the positive evaluation point \(t=1\), let independent \(K_1,\ldots,K_N\) have Sibuya probabilities \(p_k=(-1)^{k+1}\binom{\alpha}{k}\), \(k\ge1\), and use the unmodified stochastic Grünwald difference
\[
\widehat D_{N,h}=-\frac1{Nh^\alpha}\sum_{j=1}^N(hK_j-1)_+^\beta,\qquad h>0,\ N\in\mathbb N.
\]
Write \(c_\alpha=\alpha/\Gamma(1-\alpha)\), \(I_{\alpha,\beta}=c_\alpha B(\beta+1,\alpha-\beta)>0\), and \(b_{\alpha,\beta}=\tfrac12\alpha(\alpha-\beta)I_{\alpha,\beta}>0\). Then the absolutely convergent Marchaud integral and Grünwald mesh limit agree:
\[
D=-c_\alpha\int_1^\infty(r-1)^\beta r^{-1-\alpha}\,dr=-I_{\alpha,\beta}.
\]
The finite-mesh bias has the **nonzero sharp first-order coefficient**
\[
\mathbb E\widehat D_{N,h}-D=-b_{\alpha,\beta}h+o(h),\qquad h\downarrow0,
\]
uniformly in the sample count because the expectation is independent of \(N\).

There is an exact variance phase transition. For \(\alpha/2\le\beta<\alpha\), every \(h>0\) and every finite \(N\ge1\) produce **infinite mean-squared error**, despite a finite target and an absolutely convergent expected Grünwald series. For \(0<\beta<\alpha/2\), define \(v_{\alpha,\beta}=c_\alpha B(2\beta+1,\alpha-2\beta)>0\). Then
\[
\operatorname{Var}(\widehat D_{N,h})=\frac{v_{\alpha,\beta}}{Nh^\alpha}(1+o(1)),\qquad h\downarrow0,
\]
and consequently, for any choice of positive integer \(N=N(h)\),
\[
\mathbb E(\widehat D_{N,h}-D)^2
=b_{\alpha,\beta}^2h^2(1+o(1))+\frac{v_{\alpha,\beta}}{Nh^\alpha}(1+o(1)).
\]
In the fine-mesh large-budget regime, the positive mesh that uniquely minimizes this **leading two-term risk** satisfies
\[
h_N^*\sim\left(\frac{\alpha v_{\alpha,\beta}}{2b_{\alpha,\beta}^2N}\right)^{1/(\alpha+2)},
\]
and the resulting leading risk is
\[
\left(1+\frac2\alpha\right)b_{\alpha,\beta}^2
\left(\frac{\alpha v_{\alpha,\beta}}{2b_{\alpha,\beta}^2}\right)^{2/(\alpha+2)}
N^{-2/(\alpha+2)}.
\]
These last two formulas concern the fine-mesh leading-risk balance of **this unchanged estimator**; they are not global optimality statements over finite fixed meshes or other numerical algorithms.

## Assumptions and scope

All parameters are real. The Sibuya distribution is untruncated on the positive integers, with independent draws. The same step \(h\) is used for the expected Grünwald series and every Monte Carlo draw. Only the value at \(t=1\) is evaluated, and \(f_\beta(1)=0\). The function has polynomial growth toward the infinite past: it is not an \(L^1(\mathbb R)\) datum, so the theorem uses the absolutely convergent Marchaud integral at this point, not a general \(L^1\) Riemann–Liouville theorem. Each summand is a nonnegative power of \((hK-1)_+\); cancellation cannot restore its second moment in the infinite-variance range. The sampler evaluates one function value per sampled index, with no truncation, importance weighting, analytic tail correction, or control variate.

## Proof

**1. Sibuya tail and finite target.** The exact coefficients are
\[
p_k=\frac{\alpha\Gamma(k-\alpha)}{\Gamma(1-\alpha)\Gamma(k+1)}
=c_\alpha k^{-1-\alpha}\left(1+\frac{\alpha(\alpha+1)}{2k}+O(k^{-2})\right).
\]
The Gamma-quotient asymptotic follows, for example, from the first two terms of the Stirling expansion for fixed shifts. All terms are positive and \(\sum_{k\ge1}p_k=1\). Since \((hk-1)_+^\beta\asymp h^\beta k^\beta\) for large \(k\), the series defining \(\mathbb E\widehat D_{N,h}\) converges exactly when \(\beta<\alpha\). Substituting \(u=1-1/r\) yields
\[
\int_1^\infty(r-1)^s r^{-1-\alpha}\,dr
=B(s+1,\alpha-s),\qquad -1<s<\alpha.
\]
In particular, this establishes the finite Marchaud target and the explicit \(I_{\alpha,\beta}\).

**2. Exact first-order mesh bias.** Put \(\phi(r)=(r-1)_+^\beta r^{-1-\alpha}\) and \(\psi(r)=(r-1)_+^\beta r^{-2-\alpha}\) for positive \(r\). Inserting the Gamma-quotient expansion, using that the summand vanishes for \(kh\le1\), gives
\[
h^{-\alpha}\mathbb E(hK-1)_+^\beta
=c_\alpha\left[h\sum_{k\ge1}\phi(kh)
+\frac{\alpha(\alpha+1)}2h^2\sum_{k\ge1}\psi(kh)+O(h^2)\right].
\]
The remainder follows by summing the uniform \(O(k^{-2})\) term over \(k>1/h\), and is bounded by a constant times \(h^2\int_1^\infty(r-1)^\beta r^{-3-\alpha}dr\) plus a smaller boundary term. The function \(\phi\) is absolutely continuous on \([0,\infty)\), vanishes at both ends, and satisfies \(\phi'\in L^1\) because \(\beta>0\) and \(\beta<\alpha\). For any such function, the uniform-grid right Riemann sum equals its integral plus \(o(h)\): integrate its derivative against the bounded centered sawtooth and use its weak averaging to zero for \(L^1\) test functions. Also \(h\sum\psi(kh)\to\int\psi\). Thus
\[
h^{-\alpha}\mathbb E(hK-1)_+^\beta
=c_\alpha B(\beta+1,\alpha-\beta)
+\frac{\alpha(\alpha+1)}2c_\alpha B(\beta+1,\alpha+1-\beta)h+o(h).
\]
The beta recurrence gives \(B(\beta+1,\alpha+1-\beta)/B(\beta+1,\alpha-\beta)=(\alpha-\beta)/(\alpha+1)\). Multiplying by the minus sign in \(\widehat D\) proves the coefficient \(-b_{\alpha,\beta}\).

**3. Variance dichotomy.** For every fixed \(h>0\),
\[
\mathbb E[(hK-1)_+^{2\beta}]
=\sum_{k\ge1}p_k(hk-1)_+^{2\beta}
\asymp\sum_{k\gg1}k^{2\beta-\alpha-1}.
\]
The second moment is finite precisely when \(2\beta<\alpha\). At equality it diverges logarithmically, and above equality as a positive power of the cutoff. Because the summands are nonnegative, a finite average of independent copies also has infinite second moment when each individual copy does, while its finite mean exists for \(\beta<\alpha\). Hence MSE is infinite in the asserted parameter range. Conversely, when \(2\beta<\alpha\), applying the leading part of Step 2 with \(2\beta\) instead of \(\beta\) gives
\[
\mathbb E(hK-1)_+^{2\beta}=h^\alpha v_{\alpha,\beta}(1+o(1)).
\]
The first moment has order \(h^\alpha\), so its square has order \(h^{2\alpha}\) and is negligible. The independent-average identity \(\operatorname{Var}(N^{-1}\sum X_j)=\operatorname{Var}(X_1)/N\), followed by the factor \(h^{-2\alpha}\), proves the variance law and exact bias–variance decomposition.

**4. Fine-mesh budget.** For fixed \(0<\beta<\alpha/2\), write the leading error as \(b^2h^2+v/(Nh^\alpha)\). Its derivative is \(2b^2h-\alpha v/(Nh^{\alpha+1})\) and its second derivative is strictly positive. Hence it has the unique positive stationary minimizer quoted above. At that mesh the variance term equals \(2/\alpha\) times the squared-bias term, proving the sharp coefficient and exponent of the leading-risk envelope as \(N\to\infty\). The remainder terms are relative little-oh along any such sequence; this does not assert optimization over arbitrary non-vanishing meshes.

## Verification

Run `python verify.py` with the `mpmath` dependency listed in `requirements.txt`. The checked script exercises the exact Sibuya probability recurrence with rational arithmetic, the gamma-tail coefficient, the relevant beta-integral and beta-recurrence identities, numerical integral cross-checks, the first-order bias coefficient, the finite-variance constants and the leading-risk stationary equation. The captured output in `verification_output.txt` records a successful run. Each check concerns a finite identity or numerical approximation; the infinite-series convergence, divergence and mesh asymptotics are established in the analytic proof above.

For an illustrative finite-variance case \((\alpha,\beta)=(3/4,1/4)\), the constants are \(I\approx0.3616022711580193\), \(b\approx0.0678004258421286\), and \(v\approx0.7232045423160386\). At \((3/4,1/2)\), the target remains finite but the raw Monte Carlo estimator has infinite MSE for every \(h,N\).

## Relationship to prior work

Leonenko and Podlubny (2022) introduced Monte Carlo sampling of Grünwald fractional differences using the probabilities \(p_k\), and explicitly conditioned their Gaussian sampling argument on the variance being finite. Their paper also states the first-order **tail** asymptotic for \(p_k\), but not the two-term **mesh** bias, the sharp power-tail variance threshold with a finite Marchaud target, or the joint fine-mesh sampling law established here. The subsequent Leonenko–Podlubny Sibuya study (2026) gives simulation algorithms, signed and sieved laws, and integral extensions; its explicit Sibuya distribution/tail formulas are acknowledged, not claimed here. The new claim is confined to the simultaneous exact first-order bias and leading-variance/MSE classification on a natural, explicitly defined test family.

## Limitations

The chosen one-sided power tail is not in the classical \(L^1\)-based functional domain of the 2022 paper. Although the Marchaud expression here exists absolutely at the fixed point, no blanket derivative convergence theorem on all nonintegrable functions follows. The infinite-variance conclusion applies to the unmodified Sibuya-index estimator, not to truncated, importance-sampled, or variance-reduced alternatives. The optimal mesh balances two leading small-\(h\) terms within the given estimator; an exact integrand-specific finite coarse mesh might cancel bias, and is not ruled out. The analysis ignores random-index simulation cost and floating-point effects. No independent external audit has been performed.

## References

1. N. Leonenko and I. Podlubny, *Monte Carlo method for fractional-order differentiation*, Fractional Calculus and Applied Analysis **25** (2022), 346–361, first online 18 April 2022, DOI: 10.1007/s13540-022-00017-3, https://link.springer.com/article/10.1007/s13540-022-00017-3.
2. N. Leonenko and I. Podlubny, *Sibuya probability distribution and numerical evaluation of fractional-order operators*, Fractional Calculus and Applied Analysis (2026), DOI: 10.1007/s13540-026-00547-0, https://link.springer.com/article/10.1007/s13540-026-00547-0. The 2026 paper is comparative literature, not the temporally qualifying motivating source.
