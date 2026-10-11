# A sharp oracle tuning envelope for Gaussian-mixture sequential \(t\)-martingales
## Finding
For the Gaussian location model with unknown variance, Wang and Ramdas write the Gaussian-mixture scale-invariant test martingale at time \(n\) as a function of the classical statistic \(T_{n-1}\) and a precision parameter \(c>0\). Fix \(n\ge2\), put \(t=T_{n-1}^2\), and consider the entire published family \(\{G_n^{(c)}:c>0}\). Its exact pointwise envelope is
\[
\sup_{c>0}G_n^{(c)}=
\begin{cases}
1,&0\le t\le1,\\
\left(\dfrac{(1+(t-1)/n)^n}{t}\right)^{1/2},&t>1.
\end{cases}
\]
When \(t>1\), the maximizing precision is unique:
\[
c_*^2=\frac{n}{t-1}.
\]
When \(t\le1\), every finite \(c\) gives a value below one and the supremum one is approached as \(c\to\infty\).

Consequently, for every \(\alpha\in(0,1)\), there is a unique \(b_{n,\alpha}>1\) satisfying
\[
\left(1+\frac{b_{n,\alpha}^2-1}{n}\right)^n
=\frac{b_{n,\alpha}^2}{\alpha^2}.
\]
No predetermined member of this Gaussian-mixture martingale family can cross the level \(1/\alpha\) at time \(n\) unless \(|T_{n-1}|\ge b_{n,\alpha}\). At equality, the oracle precision is \(c_*^2=n/(b_{n,\alpha}^2-1)\). The barriers decrease with \(n\) and converge to
\[
b_{\infty,\alpha}=\sqrt{-W_{-1}(-\alpha^2/e)}.
\]
At \(\alpha=0.05\), \(b_{10,0.05}=3.8526382363\ldots\) and \(b_{\infty,0.05}=3.0351224130\ldots\). Under the Gaussian null, the limiting fixed-time probability that even the oracle envelope reaches 20 is
\[
2\Phi(-b_{\infty,0.05})=0.0024043808\ldots.
\]
This quantifies a fixed-time evidence barrier for the whole precision-tuned family, not merely for one arbitrary tuning choice.

## Assumptions and scope
The observations are iid Gaussian with the point-null mean used in the published scale-invariant construction, unknown positive variance, and \(n\ge2\). The statistic \(T_{n-1}\) is the usual Student statistic with \(n-1\) degrees of freedom under the null. The family \(G_n^{(c)}\) is exactly the Gaussian-prior scale-invariant martingale of Lindon et al. (in the one-dimensional no-covariate specialization) and Wang--Ramdas, with \(c>0\) the prior precision parameter.

The maximization over \(c\) is pointwise and retrospective. It is used only to characterize the largest evidence that any *fixed* member of the family could have produced on the observed statistic. The maximized envelope itself is not claimed to be an e-value or e-process, and the result does not license data-dependent selection of \(c\) without a separate validity argument.

## Proof
Equation (41) of Wang--Ramdas gives
\[
G_n^{(c)}=
\sqrt{\frac{c^2}{n+c^2}}
\left(
1+\frac{n}{(n+c^2)(n-1)/T_{n-1}^2+c^2}
\right)^{n/2}.
\]
Put \(x=c^2\), \(t=T_{n-1}^2\), and \(a=n-1+t\). Direct algebra yields
\[
\left(G_n^{(c)}\right)^2
=\frac{x(n+x)^{n-1}a^n}{\left(n(n-1)+ax\right)^n}.
\]
Its logarithmic derivative is
\[
\frac{d}{dx}\log\left(G_n^{(c)}\right)^2
=-\frac{n(n-1)\left(x(t-1)-n\right)}
{x(n+x)\left(n(n-1)+ax\right)}.
\]
All denominator factors are positive. If \(t>1\), the derivative is positive for \(0<x<n/(t-1)\), zero only at \(x=n/(t-1)\), and negative afterwards. Thus the maximizer is unique. Substitution gives
\[
\left(G_n^{(c_*)}\right)^2
=\frac1t\left(1+\frac{t-1}{n}\right)^n.
\]
If \(t\le1\), then \(x(t-1)-n<0\), so the martingale value is strictly increasing in \(x\), with limit one as \(x\to\infty\).

For \(t>1\), the squared envelope has logarithmic derivative
\[
\frac{d}{dt}\log\left(\sup_{c>0}G_n^{(c)}\right)^2
=\frac{(n-1)(t-1)}{t(n+t-1)}>0.
\]
It starts at one and diverges, which proves existence and uniqueness of \(b_{n,\alpha}\). For fixed \(t>1\), the function \(n\log(1+(t-1)/n)\) increases to \(t-1\); therefore the envelope increases with \(n\), so its crossing barrier decreases. The limiting envelope is
\[
\frac{\exp((t-1)/2)}{\sqrt t}.
\]
Writing \(y=b_{\infty,\alpha}^2\), the level equation becomes \(y e^{-y}=\alpha^2/e\). Since \(y>1\), the relevant inverse is the \(-1\) Lambert branch, giving the stated formula.

## Verification
The accompanying `verify.py` recomputes the algebraic formula numerically, checks the derivative sign change around \(c_*^2=n/(t-1)\), verifies monotonicity of the finite-\(n\) barriers, solves the \(5\%\) barriers by bisection, and checks the limiting Gaussian null tail using only the Python standard library. It prints `VERIFY_OK` when all checks pass.

The source formula was checked against equation (41) and Theorem 4.9 of Wang--Ramdas. Their discussion explicitly states that the tuning precision changes nonasymptotic power and that, for fixed \(n\) and fixed \(T_{n-1}^2\), the martingale vanishes when \(c\) is too small or too large; the exact optimizer and tuning-independent barrier above are not stated there.

## Relationship to prior work
Lindon, Ham, Tingley, and Bojinov derive the same one-dimensional martingale as a special case of their sequential \(F\)-test construction and study tuning through prior effect size, expected log-growth, minimum detectable effects, and confidence-set width. Wang and Ramdas explicitly identify that equivalence, express the martingale in terms of the classical \(t\)-statistic, and analyze asymptotic growth and confidence-sequence tuning. These works establish the family being optimized here.

The present statement is different from those tuning criteria: it takes the realized fixed-time \(t\)-statistic as given and solves the exact pointwise optimization over every positive Gaussian-prior precision. This produces a closed-form oracle envelope and a tuning-independent necessary threshold for any member of the family to cross an e-value level. Searches for the optimizer \(c_*^2=n/(T^2-1)\), its equivalent envelope, and the Lambert-\(W\) limiting barrier did not locate an equivalent result in the checked sources. This absence is evidence of noncoverage, not a proof that no equivalent formulation exists elsewhere.

## Limitations
The envelope is not itself asserted to be a valid e-value after data-dependent tuning. It is an upper diagnostic for the published family of valid fixed-precision martingales. The theorem is for the one-dimensional Gaussian mean problem and does not optimize the semi-one-sided mixture, the universal-inference e-process, or multivariate regression mixtures. The originality comparison has residual risk from older Bayes-factor and empirical-Bayes literature where the same pointwise precision optimization could appear under different notation.

## References
1. M. Lindon, D. W. Ham, M. Tingley, and I. Bojinov, *Anytime-Valid Linear Models and Regression Adjusted Causal Inference in Randomized Experiments*, arXiv:2210.08589, first public 2022-10-16.
2. H. Wang and A. Ramdas, *Anytime-valid t-tests and confidence sequences for Gaussian means with unknown variance*, arXiv:2310.03722, first public 2023-10-05; Sequential Analysis 44 (2025), DOI 10.1080/07474946.2024.2428245.
