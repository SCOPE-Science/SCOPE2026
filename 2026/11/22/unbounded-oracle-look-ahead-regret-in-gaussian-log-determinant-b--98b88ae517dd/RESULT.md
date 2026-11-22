# Unbounded oracle-look-ahead regret in Gaussian log-determinant budget allocation

## Finding

An idealized rule for choosing between one Gaussian trace probe and multiple probes can have **unbounded mean-square-error regret**, even when supplied with exact spectral approximation errors. This is not a failure of the finite-sample Gaussian moment formula: it is a failure of extrapolating a rank-comparison test to a larger budget.

Fix any rational \(\beta=p/q\) with integers \(0<p<q\) in lowest terms, and any integer \(m\ge2\). For each positive integer \(j\), take

\[
\ell=mq^2j,\qquad N=\ell^2,\qquad r_1=\beta\ell,\qquad r_0=\beta^2\ell,\qquad \delta=r_1-r_0,
\]

and any \(0<a\le1/4\). Define \(b=a\sqrt{m/2}/\ell\) and the positive-definite two-plateau matrix

\[
A=\operatorname{diag}(aI_{r_1},bI_N)\in\mathbb R^{(r_1+N)\times(r_1+N)}.
\]

Let \(A_r\) be any best rank-\(r\) spectral truncation of \(A\), and put \(P_r=I+A_r\) and \(M_r=P_r^{-1/2}(I+A)P_r^{-1/2}\). Define two exact, nonnegative residual diagnostics

\[
F(r)=\|A-A_r\|_F^2,\qquad L(r)=\|\log M_r\|_F^2.
\]

The short-rank look-ahead factor from Cortinovis and Toni is \(\gamma=m/(\delta+m)\). For every member of the family, **both exact inequalities hold strictly**:

\[
\boxed{\gamma F(r_0)>F(r_1),\qquad \gamma L(r_0)>L(r_1).}
\]

Consequently, either ideal oracle version of that look-ahead rule chooses the **one-probe** option. Yet under the same modeled total budget of \(\ell+m\) matrix-vector products, the feasible alternative using rank \(r_1\) and \(K=1+(1-\beta)\ell/m\) independent Gaussian probes is strictly better. Its exact mean-square-error improvement factor is

\[
\boxed{\frac{\mathbb E(\widehat T_{1}-T)^2}{\mathbb E(\widehat T_{K}-T)^2}
=\left(1+\frac{(1-\beta)\ell}{m}\right)\left(1-\frac{1-\beta}{\ell}\right)
\longrightarrow\infty.}
\]

This can happen with \(\|A\|_2=a\) arbitrarily small and \(\kappa_2(I+A)<1+a\), arbitrarily close to one. Two Lanczos steps suffice to calculate **each** Gaussian quadratic form exactly in exact arithmetic.

For the recommended \(\beta=3/4\), take \(m=2\) and \(\ell=32j\), so \(b=a/(32j)\) and \(K=4j+1\). The exact ratio becomes

\[
\boxed{(4j+1)\left(1-\frac1{128j}\right),}
\]

which grows linearly; it is \(635/128\) at \(j=1\).

## Assumptions and scope

The comparison is entirely within the **ideal best-rank spectral-preconditioner model**: obtaining the leading \(r\) eigenpairs is assigned a modeled cost of \(r\) matrix-vector products, each independent real standard-Gaussian probe costs \(m\) products, the preconditioner determinant is computed exactly, and the logarithmic Gaussian quadratic form is evaluated by exact-arithmetic Lanczos. The target is \(T=\log\det(I+A)\). Both competing strategies have the same modeled cost \(\ell+m\). Eigenvalue multiplicities are permitted, and any spectral truncation within the lower plateau has the same relevant residual norm.

The deterministic oracle look-ahead tests compare \(r_0=\beta^2\ell\) and \(r_1=\beta\ell\). They are distinguished from the **implemented** randomized Nyström leave-one-out diagnostic: this theorem does not assert its behavior or failure probability.

## Proof

**Integer budgets and spectrum.** Because \(\beta=p/q\) and \(\ell=mq^2j\), both look-ahead ranks are integers. Also \(K=1+(1-\beta)\ell/m\) is an integer, the full rank satisfies \(r_1<\ell<r_1+N\), and \(0<b<a\) as \(\ell\ge m\ge2\). All eigenvalues are strictly positive.

**The Frobenius oracle chooses one probe.** By \(Nb^2=(m/2)a^2\), the exact squared residuals at the two look-ahead ranks are

\[
F(r_0)=\delta a^2+\frac m2a^2,\qquad F(r_1)=\frac m2a^2.
\]

Hence

\[
\gamma F(r_0)-F(r_1)=\frac{m\delta}{2(\delta+m)}a^2>0.
\]

No approximation or sampling is involved in this decision.

**Even the exact logarithmic oracle chooses one probe.** Write \(h=\log(1+a)\), \(t=\log(1+b)\). The spectral preconditioner acts as the identity on the captured leading eigenspaces, so

\[
L(r_0)=\delta h^2+Nt^2,\qquad L(r_1)=Nt^2.
\]

For \(0<a\le1/4\), the elementary inequalities \(\log(1+a)\ge a/(1+a)\ge4a/5\) and \(\log(1+b)\le b\) imply

\[
mh^2\ge\frac{16m}{25}a^2>\frac m2a^2=Nb^2\ge Nt^2.
\]

Consequently,

\[
\gamma L(r_0)-L(r_1)=\frac\delta{\delta+m}(mh^2-Nt^2)>0.
\]

Thus neither perfect knowledge of the two Frobenius errors nor perfect knowledge of the two logarithmic errors repairs the short-to-full-rank extrapolation.

**Actual full-budget risks.** After rank \(r_1\) preconditioning, exactly \(N\) eigenvalues of \(M_{r_1}\) equal \(1+b\); after rank \(\ell\) preconditioning, exactly \(N-(\ell-r_1)\) do. All other eigenvalues equal one. Therefore each residual logarithm is a scalar multiple of an orthogonal projector and, for an independent standard-Gaussian vector \(w\),

\[
\operatorname{Var}(w^T\log(M_r)w)=2\|\log(M_r)\|_F^2.
\]

The deterministic preconditioner contribution is exact and the Gaussian sample mean is unbiased. The respective mean-square errors are thus exactly

\[
R_1=2\bigl(N-\ell+r_1\bigr)t^2,\qquad R_K=\frac{2N}{K}t^2.
\]

Their ratio is

\[
\frac{R_1}{R_K}=K\left(1-\frac{\ell-r_1}{N}\right)
=\left(1+\frac{(1-\beta)\ell}{m}\right)\left(1-\frac{1-\beta}{\ell}\right).
\]

Since \(\beta\) and \(m\) are fixed, the first factor diverges linearly with \(\ell\), and the second tends to one. The preconditioned matrices have spectra contained in \(\{1,1+b\}\): their minimal polynomials have degree at most two, so the Lanczos space is invariant after at most two steps, proving exactness of the stipulated quadrature. Finally \(\kappa_2(I+A)=(1+a)/(1+b)<1+a\), and \(a\) may be chosen arbitrarily close to zero without changing the displayed ratio. This proves every assertion.

## Verification

The standalone Python-standard-library file `verify.py` checks exact rational budget integrality, Frobenius predictor inequalities, exact regret identities, and numerical evaluations of the logarithmic predictor for rational \(\beta\), multiple positive integer probe costs, and multiple spectral scales. Its expected output is

```text
VERIFY_OK general_inequality_checks=26460 recommended_checks=1400
```

The numerical inequalities are supplementary finite tests; the universal result and divergence follow from the inequalities and Gaussian-moment identity in the proof.

## Relationship to prior work

Cortinovis and Toni, first public preprint January 9, 2026, establish the ideal Gaussian residual variance in their Section 2 and introduce the two-rank look-ahead and Frobenius heuristic in Section 4.3. Their Remark 4.1 notes a tendency toward one-probe selection from replacing the logarithmic error by a Frobenius proxy, and their experiments include some incorrect decisions at small values of \(\beta\). These facts are credited, not claimed as new. The present statement provides a **universal unbounded loss family for every fixed rational** \(\beta\) **and every fixed** \(m\ge2\), including the recommended \(\beta=3/4\), and proves that the same loss occurs even when the original logarithmic short-rank criterion is evaluated exactly.

A previously published exact-allocation classification establishes that under ideal spectral deflation a one-probe option is truly optimal if and only if it beats the **two-probe option at the full budget**. That result does not justify extrapolating from the two reduced look-ahead ranks or bound its regret. The present counterexample contrasts the short-rank predictor with full-budget MSE, rather than re-deriving that global optimizer classification. Earlier adaptive trace-allocation studies and leave-one-out diagnostics address different random-oracle guarantees; their results do not supply the exact short-look-ahead regret law stated here.

## Limitations

This is a lower bound on the quality of a **deterministic idealized diagnostic**, not a proven failure mode for the implemented randomized Nyström selection algorithm or its leave-one-out error estimator. It assumes real Gaussian probes, complete knowledge of best rank-\(r\) eigenspaces at modeled cost \(r\), the fixed two-choice allocation, and exact arithmetic. It makes no claim about Rademacher probes, non-Gaussian sketch distributions, finite-precision Lanczos, or true runtime optimality. The family grows in dimension with the budget; fixed-dimensional uniform bounds are not excluded. The linear regret factor is exact for this family but is not asserted as a worst-case upper bound over all spectra.

## References

1. A. Cortinovis and D. Toni, *Preconditioned log-determinant approximation: one Gaussian probe vector is almost always enough*, arXiv:2601.05778, first posted January 9, 2026. https://arxiv.org/abs/2601.05778
2. A. Cortinovis and D. Toni, *Detecting When One Probe Vector is Enough for Preconditioned Log-Determinant Approximation*, Numerical Linear Algebra with Applications 33 (2026), e70106, July 2, 2026. https://doi.org/10.1002/nla.70106
3. D. Persson, A. Cortinovis, and D. Kressner, *Improved variants of the Hutch++ algorithm for trace estimation*, arXiv:2109.10659. https://arxiv.org/abs/2109.10659
4. E. N. Epperly and J. A. Tropp, *Efficient Error and Variance Estimation for Randomized Matrix Computations*, SIAM Journal on Scientific Computing 46 (2024), A508–A528; preprint arXiv:2207.06342. https://arxiv.org/abs/2207.06342
5. *Single-crossing optimality of Gaussian probe allocation after ideal spectral deflation*, publicly available mathematical record, October 13, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-single-crossing-optimality-of-gaussian-probe-allocation-after-id--63138f0a4092
