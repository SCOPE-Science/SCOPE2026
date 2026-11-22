# A unique blind tuning curve for a signed Lévy goodness-of-fit statistic under Gamma alternatives

## Finding

For every shape \(2<k\le5/2\), the signed Laplace-integral goodness-of-fit statistic \(R_{n,a}\) of Lukić–Milošević, with the published inverse-moment fitted Lévy scale, has **exactly one** positive weight \(a=a_k\) at which its population discrepancy vanishes under an independent \(\operatorname{Gamma}(k,\theta)\) alternative, for every scale \(\theta>0\). The population discrepancy is positive for \(0<a<a_k\) and negative for \(a>a_k\). A fixed alternative on this curve is not a Lévy distribution. Yet \(\sqrt nR_{n,a_k}\) converges to a centered nondegenerate Gaussian law, so rejecting for large \(\sqrt n|R_{n,a_k}|\) with any positive finite null-calibrated threshold is **not consistent**: its limiting rejection probability is strictly below one. This applies to the signed-integral test, not the companion supremum test.

For example, when \(k=9/4\), \(a_k=0.03754904932048\ldots\), independently of \(\theta\). The exact result is the unique integral root; the decimal is a numerical approximation.

## Assumptions and scope

Let \(X_1,\ldots,X_n\) be independent with \(X_i\sim\operatorname{Gamma}(k,\theta)\), using shape \(k\) and scale \(\theta\); assume \(2<k\le5/2\) and \(\theta>0\). Let \(\widehat\lambda_n=(n^{-1}\sum_iX_i^{-1})^{-1}\), \(Y_i=X_i/\widehat\lambda_n\), and for any \(a>0\) define exactly the published signed statistic

\[
R_{n,a}=\int_0^\infty t^{3/2}e^{-at}\left\{\frac1n\sum_{i=1}^ne^{-tY_i}-\frac1{n^2}\sum_{i,j=1}^ne^{-t(Y_i+Y_j)/4}\right\}\,dt.
\]

The alternative is non-Lévy because Gamma has an exponentially decaying upper tail while Lévy has a polynomial tail. The estimator converges almost surely to \(\lambda_*=(k-1)\theta\). Put \(h=k-1\) and

\[
F_k(a)=\int_0^\infty t^{3/2}e^{-at}\left\{(1+t/h)^{-k}-(1+t/(4h))^{-2k}\right\}\,dt.
\]

For fixed \(a>0\), the population limit is \(F_k(a)\), and the unique root \(a_k\) depends only on \(k\). All limits are for fixed \(k,\theta,a\), as \(n\to\infty\). No claim is made about shrinking or data-selected \(a\), or about the separately defined supremum \(J_{n,a}\).

## Proof

**Population limit.** Since \(\mathbb E X^{-1}=1/((k-1)\theta)\), the strong law gives \(\widehat\lambda_n\to\lambda_*\) almost surely. The Gamma Laplace transform and boundedness of \(t^{3/2}e^{-at}\) as an integrable envelope give \(R_{n,a}\to F_k(a)\) almost surely by the strong law for V-statistics and continuous scaling. In particular, the V-diagonal contributes only an asymptotically negligible term.

**One sign switch.** Write \(D_k(t)=(1+t/h)^{-k}-(1+t/(4h))^{-2k}\). For \(t>0\), strict monotonicity of positive powers gives

\[
\operatorname{sgn}D_k(t)=\operatorname{sgn}\{(1+t/(4h))^2-(1+t/h)\}=\operatorname{sgn}(t-8h).
\]

Set \(T=8h\) and \(H_k(a)=e^{aT}F_k(a)\). Differentiation under the integral for each \(a>0\) yields

\[
H_k'(a)=-\int_0^\infty (t-T)t^{3/2}D_k(t)e^{-a(t-T)}\,dt<0.
\]

The strict inequality holds because \((t-T)D_k(t)>0\) for every \(t\ne T\). As \(a\to\infty\), \(D_k(t)=-kt/(2h)+O(t^2)\) at zero, so \(F_k(a)\sim-[k/(2h)]\Gamma(7/2)a^{-7/2}<0\), implying \(H_k(a)\to-\infty\). As \(t\to\infty\), \(D_k(t)\sim h^k t^{-k}>0\), and therefore \(F_k(a)\to+\infty\) as \(a\downarrow0\) for \(k\le5/2\), by monotone convergence on the positive tail and boundedness of the negative contribution on \((0,T)\). Thus \(H_k\) passes strictly once from positive to negative. This proves existence, uniqueness, and the asserted sign orientation. At the root \(F_k'(a_k)=e^{-a_kT}H_k'(a_k)<0\), so the root is simple.

**Nondegenerate fixed-alternative limit.** For \(x,y>0\) and \(\lambda>0\), write

\[
K_a(x,y;\lambda)=\int_0^\infty t^{3/2}e^{-at}\bigl\{\tfrac12e^{-tx/\lambda}+\tfrac12e^{-ty/\lambda}-e^{-t(x+y)/(4\lambda)}\bigr\}\,dt.
\]

Then \(R_{n,a}=n^{-2}\sum_{i,j}K_a(X_i,X_j;\widehat\lambda_n)\). Define \(\mu_a(\lambda)=\mathbb EK_a(X_1,X_2;\lambda)\), with independent variables, and \(g_a(x)=2\{\mathbb E[K_a(x,X_2;\lambda_*)]-\mu_a(\lambda_*)\}\). The bounded kernel and its first two scale derivatives admit uniform integrable envelopes for \(\lambda\) in a compact neighborhood of \(\lambda_*\): derivatives reduce to bounded functions of \(tx/\lambda\) multiplied by \(t^{3/2}e^{-at}\). The ordinary nondegenerate V-statistic projection and a first-order expansion in the fitted scale therefore give

\[
\sqrt n\{R_{n,a}-\mu_a(\lambda_*)\}=\frac1{\sqrt n}\sum_{i=1}^n\left[g_a(X_i)+\mu_a'(\lambda_*)\left(\lambda_*-\frac{\lambda_*^2}{X_i}\right)\right]+o_{\mathbb P}(1).
\]

Here the inverse-moment estimator influence function follows from the delta method; its second moment is finite exactly when \(k>2\). To verify \(\mu_a'(\lambda_*)\ne0\) at \(a=a_k\), set \(s=\theta/\lambda\), \(s_*=1/h\), and \(B_k(b)=\int_0^\infty u^{3/2}e^{-bu}[(1+u)^{-k}-(1+u/4)^{-2k}]\,du\). Then \(\mu_a(\lambda)=s^{-5/2}B_k(a/s)\), and differentiation at \(\lambda_*\), using \(B_k(a_k/s_*)=0\), yields

\[
\mu_{a_k}'(\lambda_*)=\frac{a_k}{\lambda_*}F_k'(a_k)\ne0.
\]

The function \(g_a(x)\) is bounded in \(x>0\), whereas \(\lambda_*-\lambda_*^2/x\) is unbounded as \(x\downarrow0\). Thus their nonzero-coefficient combination cannot be constant under a fully supported Gamma law and has strictly positive finite variance \(\sigma_{k,a_k}^2\). Lindeberg–Lévy's central limit theorem gives

\[
\sqrt nR_{n,a_k}\ \Rightarrow\ N(0,\sigma_{k,a_k}^2),\qquad 0<\sigma_{k,a_k}^2<\infty.
\]

For a fixed positive finite null critical value \(c_{a_k,\alpha}\) on this \(\sqrt n|R|\) scale, the limiting rejection probability is \(2[1-\Phi(c_{a_k,\alpha}/\sigma_{k,a_k})]\in(0,1)\). Thus the signed test fails to have power approaching one at the specified non-null Gamma alternatives. For ordinary asymptotic-normal critical values one can take \(c_{a_k,\alpha}=z_{1-\alpha/2}\sigma_{0,a_k}\) whenever the null variance is positive.

## Verification

The bundled `verify.py` numerically integrates \(F_k\), checks the strict sign switch of the integrand at \(8(k-1)\), locates the unique root by bracketing, and evaluates the derivative. It was run successfully with 33 assertions for \(k=2.02,\ 2.25,\ 2.50\). For \(k=2.25\), it returned \(a_k=0.03754904932048\ldots\), with an integral residual below \(10^{-12}\). Numerical integration corroborates, but does not replace, the analytic existence/uniqueness and asymptotic-limit arguments.

## Relationship to prior work

Lukić and Milošević introduce both signed-integral \(R_{n,a}\) and supremum \(J_{n,a}\) tests, prove the null limits, and tabulate empirical power against Gamma and other alternatives; they also establish consistency for the **supremum** statistic under fixed alternatives. Their displayed simulations use selected weights \(a=0.2,0.5,1,2,5\), not the small exact blind weight here, and their reported Gamma example has shape 3, outside the claimed shape window. The new assertion is not a reparameterization of the original null central-limit theorem or an implication of their supremum consistency: it is a global fixed-alternative zero of a signed integrated transform together with its nondegenerate alternative CLT. The earlier scale-ratio Lévy tests of Kumari and Bhati are based on a distinct statistic and do not imply this tuning curve.

## Limitations

The blind curve is proved only for \(2<k\le5/2\), and the corresponding weights are below the principal numerical weights emphasized by the source. This is not evidence that the published recommended weights are inconsistent, nor that the supremum test is blind. The root's decimal is approximate; the complete exact specification is its unique-integral equation. All conclusions are same-source model-based mathematical calculations, without an independent audit or empirical performance benchmark for a practical sample size. Standard asymptotic normal testing relies on a valid positive null-calibration variance, as in the source.

## References

1. Ž. Lukić and B. Milošević, “Characterization-based approach for construction of goodness-of-fit test for Lévy distribution,” *Statistics* 57 (2023), 1087–1116. https://doi.org/10.1080/02331888.2023.2238236 . Public online version 24 July 2023; arXiv first version 1 August 2023: https://arxiv.org/abs/2308.00460 . See Eq. (4), Theorem 2, Section 5, and Appendix A.
2. A. Kumari and D. Bhati, “Goodness-of-fit test for the one-sided Lévy distribution,” *Journal of Applied Statistics* 51 (2024), 1961–1975. https://doi.org/10.1080/02664763.2023.2251098 .
