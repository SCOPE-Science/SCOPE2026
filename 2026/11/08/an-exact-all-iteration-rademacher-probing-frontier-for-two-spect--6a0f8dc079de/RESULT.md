# An exact all-iteration Rademacher probing frontier for two-spectrum Landweber covariance

## Finding

For linear Landweber iteration with a positive-definite normal matrix having exactly two spectral values, reusing the same Rademacher probes at all iterations yields an **exact, pathwise, all-iteration relative covariance-diagonal error**. The worst relative error is either at the first step or at the infinite-step limit, and the choice is determined solely by whether the coordinate leverage of the high-eigenvalue spectral projector is below or above one half. In a flat rank-one spectral spike, the entire infinite-horizon error has an exact binomial tail law. These statements hold without a union bound over iterations.

Let \(\kappa=\lambda_+/\lambda_->1\), \(p=P_{jj}\in(0,1)\), and
\[
C_{\kappa}(p)=(\kappa-1)\max\left\{\frac1{1+p(\kappa-1)},\frac1{\kappa-p(\kappa-1)}\right\}.
\]
For every realized set of probes, and all positive integral iteration indices, the exact identity is
\[
\boxed{\sup_{k\ge1}\frac{|\widehat\gamma_{k,j}-\gamma_{k,j}|}{\gamma_{k,j}}
=C_{\kappa}(p)\,|\widehat p_j-p|.}
\]
Here \(\widehat p_j\) is the usual Rademacher diagonal estimator of the projector \(P\) using precisely the same probes. If \(\widehat p_j\ne p\), the supremum is reached at \(k=1\) for \(p\le1/2\), whereas for \(p>1/2\) it is approached only as \(k\to\infty\). The threshold \(p=1/2\) is independent of the spectral condition number and the allowed Landweber step size.

For \(N\) independent probes and every \(\varepsilon>0\),
\[
\mathbb P\left(\sup_{k\ge1}\frac{|\widehat\gamma_{k,j}-\gamma_{k,j}|}{\gamma_{k,j}}>\varepsilon\right)
\le 2\exp\left(-\frac{N\varepsilon^2}{2p(1-p)C_\kappa(p)^2}\right).
\]
In the flat rank-one case \(P=\boldsymbol1\boldsymbol1^\mathsf T/d\), \(d\ge3\), this probability is **exactly**
\[
2^{-M}\sum_{h=0}^{M}\binom Mh
\boldsymbol1\left\{|2h-M|>\frac{N\varepsilon(d-1+\kappa)}{\kappa-1}\right\},\qquad M=N(d-1).
\]
No distributional approximation is used in this formula.

## Assumptions and scope

Work over a real finite-dimensional Euclidean space of dimension \(d\ge2\). Let \(A\in\mathbb R^{m\times d}\) have full column rank, and let its normal matrix have precisely two eigenvalues:
\[
B=A^\mathsf T A=\lambda_- I+(\lambda_+-\lambda_-)P,
\qquad 0<\lambda_-<\lambda_+,
\]
where \(P=P^\mathsf T=P^2\) is a nonzero, nonidentity orthogonal projector. Let \(\sigma>0\) be the standard deviation of independent white Gaussian observational noise and take \(0<\omega\le1/\lambda_+\). The propagated covariance after \(k\ge1\) Landweber steps from a deterministic initialization is
\[
\Gamma_k=\sigma^2\left[I-(I-\omega B)^k\right]^2B^{-1}.
\]
For one fixed coordinate \(j\) assume \(p=P_{jj}\in(0,1)\). Take \(N\ge1\) independent vectors \(w^1,\ldots,w^N\), each with independent uniformly random \(\{-1,1\}\) coordinates, and **reuse these exact vectors for every \(k\)**. Set
\[
\gamma_{k,j}=(\Gamma_k)_{jj},\quad
\widehat\gamma_{k,j}=\frac1N\sum_{\ell=1}^N w_j^\ell(\Gamma_kw^\ell)_j,
\quad\widehat p_j=\frac1N\sum_{\ell=1}^Nw_j^\ell(Pw^\ell)_j.
\]
Every \(\gamma_{k,j}\) is strictly positive. Statements concern this exact covariance, not an additional low-rank truncation, approximate matrix multiplication, or a confidence interval's full coverage when its stopping time depends on observation noise. A separate flat-spike specialization assumes \(d\ge3\) and \(P=\boldsymbol1\boldsymbol1^\mathsf T/d\).

## Proof

**1. Exact two-spectral reduction.** Set
\[
q_{\pm,k}=\frac{[1-(1-\omega\lambda_\pm)^k]^2}{\lambda_\pm},\quad
 t_k=\frac{q_{+,k}}{q_{-,k}}.
\]
The spectral calculus gives
\[
\Gamma_k=\sigma^2[q_{-,k}I+(q_{+,k}-q_{-,k})P].
\]
Since every probe has squared entries equal to one, its diagonal estimator has the identical decomposition with \(P_{jj}\) replaced by \(\widehat p_j\). Dividing by \(\gamma_{k,j}=\sigma^2[q_{-,k}+(q_{+,k}-q_{-,k})p]\) yields the **exact signed identity**
\[
\frac{\widehat\gamma_{k,j}-\gamma_{k,j}}{\gamma_{k,j}}
=(\widehat p_j-p)\frac{t_k-1}{1+p(t_k-1)}.
\tag{1}
\]
This holds for arbitrary realized probes, without averaging or concentration.

**2. Strict ordering of the Landweber spectral ratios.** Write \(a=1-\omega\lambda_+\), \(b=1-\omega\lambda_-\), so \(0\le a<b<1\). The ratio
\[
\frac{1-a^k}{1-b^k}=\frac{1-a}{1-b}
\frac{\sum_{r=0}^{k-1}b^r(a/b)^r}{\sum_{r=0}^{k-1}b^r}
\]
is a weighted average of the strictly decreasing sequence \((a/b)^r\), with strictly positive weights \(b^r\), multiplied by a fixed positive constant. Appending the next, smaller term strictly decreases the average. Therefore \(t_k\) strictly decreases with \(k\). Direct calculation gives
\[
 t_1=\kappa,\qquad \lim_{k\to\infty}t_k=1/\kappa.
\tag{2}
\]

**3. Endpoint maximization and the half-leverage frontier.** The scalar function \(g_p(t)=|t-1|/[1+p(t-1)]\) decreases on \((0,1)\) and increases on \((1,\infty)\), for any \(0<p<1\). Consequently its largest value along the decreasing sequence in (2) is the larger of its two spectral-endpoint values:
\[
 g_p(\kappa)=\frac{\kappa-1}{1+p(\kappa-1)},\qquad
 g_p(1/\kappa)=\frac{\kappa-1}{\kappa-p(\kappa-1)}.
\]
The first is at least the second exactly when \(p\le1/2\). Combining with (1) proves the asserted exact all-time identity and attainment statements. When \(p>1/2\), strict monotonicity in (2) ensures the larger endpoint is only a limit, provided \(\widehat p_j\ne p\). If \(\widehat p_j=p\), every error is zero.

**4. Time-uniform probability bound.** For each probe, the centered projector diagonal observation equals
\[
 w_j^\ell(Pw^\ell)_j-p=\sum_{i\ne j}P_{ji}w_j^\ell w_i^\ell.
\]
The \(d-1\) signs in this sum are independent Rademacher variables: the change of signs from \((w_j,w_i:i\ne j)\) to \((w_j,w_jw_i:i\ne j)\) is a bijection of the Boolean cube. Thus the \(N\) probe sums are independent and centered, with sub-Gaussian variance proxy \(\sum_{i\ne j}P_{ji}^2=p-p^2=p(1-p)\), the last equality following from \(P^2=P\). The standard exponential-moment bound for sums of Rademacher variables gives
\[
\mathbb P(|\widehat p_j-p|>u)\le 2\exp[-Nu^2/(2p(1-p))].
\]
The deterministic equality in the Finding transfers this inequality to a **single event covering every iteration**, including any finite probe-dependent chosen iteration index, without an iteration-count union bound.

**5. Exact flat-spike law.** If \(P=\boldsymbol1\boldsymbol1^\mathsf T/d\), then \(p=1/d\) and
\[
\widehat p_j-p=\frac1{Nd}\sum_{\ell=1}^N\sum_{i\ne j}w_j^\ell w_i^\ell.
\]
The \(M=N(d-1)\) signs in the double sum are independent, so their sum equals \(2H-M\) in distribution for \(H\sim\operatorname{Bin}(M,1/2)\). Because \(p<1/2\), the first-step endpoint wins, giving
\[
\sup_{k\ge1}\frac{|\widehat\gamma_{k,j}-\gamma_{k,j}|}{\gamma_{k,j}}
=\frac{\kappa-1}{N(d-1+\kappa)}|2H-M|.
\]
Taking the exact binomial mass of the strict exceedance event proves the stated formula. Summing those masses is a finite, exhaustive calculation; no asymptotic or simulation argument is needed.

## Verification

Run `python verify.py` with NumPy installed. It checks the exact signed error identity by direct dense-matrix multiplication for two-eigenvalue random orthoprojectors, several iterations and step sizes; compares the all-time endpoint formula with both spectral endpoints; exhaustively enumerates short Rademacher sign arrays to check the binomial multiplicities; and tests the half-leverage endpoint comparison. The observed output is:

```
VERIFY_OK; 1200 dense-operator comparisons; 6 exact exhaustive binomial cases; 20 endpoint checks
```

These tests are diagnostics. The statements for arbitrary dimension, number of probes, and all iterations follow from the five proof steps above.

## Relationship to prior work

Abhishek and Holman (2026, arXiv:2610.00882v1, Sections 3.3 and 3.5 and Appendix 5.1) give the Landweber propagated covariance and the Rademacher diagonal estimator with a fixed-iteration guarantee, and motivate a data-independent or probe-dependent stopping index. The present result **does not claim** those covariance or unbiased-estimation formulas as new. It identifies an exact uniform-in-iteration error factor and its universal half-leverage endpoint switch for the two-eigenvalue subclass; neither classification is stated there.

Hallman, Ipsen, and Saibaba (2023, DOI:10.1137/22M1476277, Sections 3 and 5) give general fixed-matrix diagonal-estimation concentration bounds including the source paper's fixed-index guarantee. These bounds apply separately to every covariance matrix in the family, but do not assert which time is worst or the exact common-probe infinite-horizon law. Matti, He, Kressner, and Lam (2025 preprint, arXiv:2502.18626, Section 2) study *parameter-dependent trace estimators* with shared Gaussian randomization and an integrated error criterion, not coordinatewise Rademacher errors at the supremum norm or this spectral-leverage threshold. Their work is relevant as a broader shared-randomness method, not a statement implying the exact result.

## Limitations

The two-spectral-value, positive-definite normal-matrix condition and nonnegative Landweber propagation factors are essential to the proof. The conclusion has not been established for three or more eigenvalues, for step sizes above \(1/\lambda_+\), or for independently resampled probes across iterations. The binomial equality additionally requires a flat rank-one projector. The probability bound is an upper bound, not claimed optimal for a general projector. It controls random numerical covariance-diagonal estimation, not automatic frequentist coverage after arbitrary data-dependent stopping. These results have not undergone independent mathematical review; historical priority remains subject to further literature comparison.

## References

1. A. Abhishek and S. Holman, *Uncertainty Quantification for Landweber Iteration with Randomized Normal-Operator Approximation*, arXiv:2610.00882v1 (first public posting 2026-10-01). https://arxiv.org/html/2610.00882v1
2. E. Hallman, I. C. F. Ipsen, and A. K. Saibaba, *Monte Carlo Methods for Estimating the Diagonal of a Real Symmetric Matrix*, SIAM J. Matrix Anal. Appl. 44 (2023), 240–269. https://doi.org/10.1137/22M1476277
3. F. Matti, H. He, D. Kressner, and H. Y. Lam, *Stochastic Trace Estimation for Parameter-Dependent Matrices Applied to Spectral Density Approximation*, arXiv:2502.18626; SIAM J. Sci. Comput. 48 (2026), A2287–A2313. https://arxiv.org/abs/2502.18626
