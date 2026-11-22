# A sharp compound-Poisson boundary for Bernoulli–Poisson–Lindley counts

## Finding
For the two-parameter Bernoulli–Poisson–Lindley distribution of Bakouch, Chesneau, Maya, Irshad, Aswathy and Qarmalah, a sharp criterion for additive infinite divisibility on the nonnegative integers is
\[
\boxed{X_{\alpha,\theta}\text{ is infinitely divisible}\quad\Longleftrightarrow\quad 0<\alpha\le\frac{1}{\theta+2}.}
\]
On this closed-in-\(\alpha\) parameter region, the exact compound-Poisson jump intensities are
\[
\lambda_k=\frac{2q^k-r^k+(-1)^{k+1}b^k}{k}>0,\qquad k=1,2,\ldots,
\]
with \(q=(1+\theta)^{-1}\), \(r=(2+\theta)^{-1}\), \(b=\alpha/(1-\alpha)\).
Above the boundary, infinitely many even-index intensities are negative. Let \(K(\alpha,\theta)\) be the *first even index* with negative formal log-PGF coefficient. For each fixed \(\theta>0\), as \(\alpha\downarrow(\theta+2)^{-1}\) from above,
\[
\boxed{K(\alpha,\theta)\log\!\left(\frac{b}{q}\right)\longrightarrow\log 2.}
\]
Thus no fixed finite number of coefficients detects failure arbitrarily close to the boundary. These statements form one phase-classification theorem with its sharp near-boundary obstruction law.

## Assumptions and scope
Fix \(\theta>0\), \(0<\alpha<1\), and let \(X=B+Y\) for independent \(B\sim\operatorname{Bernoulli}(\alpha)\) and Poisson–Lindley \(Y\) with probability mass function
\[
\Pr(Y=j)=\frac{\theta^2(j+\theta+2)}{(1+\theta)^{j+3}},\qquad j\in\mathbb N_0.
\]
For this published law the probability generating function is
\[
G(s)=\frac{(1-\alpha+\alpha s)\theta^2(\theta+2-s)}{(1+\theta)(1+\theta-s)^2}.
\]
The theorem concerns ordinary additive infinite divisibility under convolution of probability measures on \(\mathbb N_0\), not binomial-thinning self-decomposability. The convention includes all positive integer jump sizes. The boundary \(\alpha=(\theta+2)^{-1}\) is included, but the defining family excludes \(\alpha=0,1\).

## Proof
**Logarithmic coefficients.** Put \(q=(1+\theta)^{-1}\), \(r=(2+\theta)^{-1}\), \(b=\alpha/(1-\alpha)\). Then \(0<r<q<1\), \(b>0\), and exact factorization gives
\[
G(s)=p_0\frac{(1+bs)(1-rs)}{(1-qs)^2},\qquad
p_0=\frac{(1-\alpha)\theta^2(\theta+2)}{(1+\theta)^3}>0.
\]
Taking the Taylor logarithm at zero (as a formal power series, valid regardless of whether \(b<1\)) yields
\[
\log G(s)=\log p_0+\sum_{k\ge1}\lambda_k s^k,\qquad
\lambda_k=\frac{2q^k-r^k+(-1)^{k+1}b^k}{k}.
\]

**Compound-Poisson criterion.** Any law on \(\mathbb N_0\) with positive zero atom and infinitely divisible PGF has nonnegative logarithmic coefficients: for each positive integer \(n\) write its PGF as \(F_n(s)^n\) and note that \(n[s^k]F_n(s)\to\lambda_k\) as \(n\to\infty\). Each coefficient on the left is nonnegative. Conversely, if all \(\lambda_k\ge0\) and their sum is finite, then \(G(s)=\exp(\sum_{k\ge1}\lambda_k(s^k-1))\), the compound-Poisson PGF with jump intensity \(\lambda_k\). Here \(G(1)=1\) and the factorization gives the normalization whenever \(b\le q<1\). Thus this criterion is both necessary and sufficient in the range in question.

**Exact boundary.** For odd \(k\), the numerator of \(\lambda_k\) is \(2q^k-r^k+b^k>0\). If \(b\le q\), then for every even \(k\),
\[
2q^k-r^k-b^k\ge q^k-r^k>0.
\]
Since \(\lambda_k=O(q^k/k)\), the series converges, giving the explicit compound-Poisson law. If \(b>q\), for even \(k\) sufficiently large,
\[
2q^k-r^k-b^k<2q^k-b^k<0,
\]
contradicting the necessary criterion. The inequality \(b\le q\) rearranges to \(\alpha\le 1/(\theta+2)\), proving the iff claim.

**First forbidden coefficient.** Set \(t=\log(b/q)>0\) and \(\rho=r/q\in(0,1)\). For even indices \(k\), negativity is exactly
\[
e^{kt}+\rho^k>2.
\]
Given \(\varepsilon\in(0,\log2)\), for every \(k\ge(\log2+\varepsilon)/t\) the first summand already exceeds two, hence the first forbidden *even* index is eventually no larger than that scale, up to a bounded rounding error. Conversely, for even \(k\le(\log2-\varepsilon)/t\), the first summand is at most \(2e^{-\varepsilon}\). Choose a fixed sufficiently large integer \(J\) such that \(\rho^J<2(1-e^{-\varepsilon})\); for \(k\ge J\) the sum is strictly below two. For the finitely many even \(k<J\), the sum tends to \(1+\rho^k<2\) as \(t\downarrow0\), so it is likewise below two for all sufficiently small \(t\). Therefore \((\log2-\varepsilon)/t<K\le(\log2+\varepsilon)/t+2\) eventually. Multiply by \(t\), send \(t\downarrow0\), then \(\varepsilon\downarrow0\) to obtain the stated limit.

**A shape diagnostic distinct from infinite divisibility.** At \(\theta=1\), \(\alpha=1/2\), the first even logarithmic coefficient is \(\lambda_2=-11/36\), yet \(\mathbb E X=2\) and \(\operatorname{Var}(X)=7/2\). Overdispersion therefore does not ensure a compound-Poisson representation for this model.

## Verification
`check_bpl.py` requires only Python 3 and performs exact rational checks of the published mass function against the formal-log coefficients over a parameter grid, including the sharp equality case; it also verifies the overdispersed negative-intensity witness and numerical examples of the growing first forbidden index. The checker reports **1384 passing finite/formula assertions**. The infinite-support inequality and asymptotic argument are proved above, not inferred from the finite checks. Reproduction: `python3 check_bpl.py`.

## Relationship to prior work
Bakouch et al. (2023) define the exact Bernoulli–Poisson–Lindley PMF and PGF, as well as ordinary moments, modes, dispersion and hazard behavior. The published article does not give this compound-Poisson/ordinary-infinite-divisibility phase diagram. The classical criterion that a discrete infinitely divisible law with a positive zero atom must be compound Poisson is prior theory and is not claimed new. Letac, Malouche and Maurer (2002) analyze convolution powers of a Bernoulli and a negative-binomial law with normalized generating factors \((1+z/c)^x(1-z)^{-y}\). That problem has a two-factor algebraic form, whereas the current PGF has the additional distinct numerator factor \(1-rs\); their family does not directly contain this one. Alrumayh (2024) treats Bernoulli plus Poisson-moment-exponential counts, a different baseline distribution. The current theorem is specific to the exact Poisson–Lindley convolution, and no broad characterization for all Bernoulli-perturbed mixed Poisson laws is asserted.

## Limitations
The theorem concerns one published parametric family, not general mixtures or all Bernoulli convolutions. The first-obstruction asymptotic fixes \(\theta\); no uniform-in-\(\theta\) claim is made. Decimal illustrations are non-certifying. Historical priority may depend on related convolution-power papers beyond those compared; a full independent literature audit is not claimed. No independent mathematical validation has been performed.

## References
1. H. S. Bakouch, C. Chesneau, R. Maya, M. R. Irshad, S. Aswathy and N. Qarmalah, *A Flexible Dispersed Count Model Based on Bernoulli Poisson–Lindley Convolution and Its Regression Model*, Axioms **12** (2023), 813; first published 24 August 2023, https://doi.org/10.3390/axioms12090813.
2. G. Letac, D. Malouche and S. Maurer, *The Real Powers of the Convolution of a Negative Binomial Distribution and a Bernoulli Distribution*, Proc. Amer. Math. Soc. **130** (2002), 2107–2114; https://doi.org/10.1090/S0002-9939-02-05352-2.
3. A. Alrumayh, *Bernoulli Poisson Moment Exponential Distribution: Mathematical Properties, Regression Model, and Applications*, International Journal of Mathematics and Mathematical Sciences (2024), article 5687958; https://doi.org/10.1155/2024/5687958.
4. *Mixed Poisson Distributions* (survey; §3.6, classical discrete infinite divisibility and compound-Poisson characterization), https://www.academia.edu/14101979/Mixed_Poisson_Distributions.
