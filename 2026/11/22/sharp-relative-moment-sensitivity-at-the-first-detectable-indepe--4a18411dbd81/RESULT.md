# Sharp relative moment sensitivity at the first detectable independence order

## Finding
Let \(n\ge4\) be an even integer and \(\xi=(\xi_1,\ldots,\xi_n)\) a fair, \((n-1)\)-wise independent vector of signs. Put \(\theta=\mathbb E\prod_{j=1}^n\xi_j\in[-1,1]\). For every nonzero real \(a=(a_1,\ldots,a_n)\), define
\[
F_\theta(a)=\mathbb E\left|\sum_{j=1}^n a_j\xi_j\right|^n,
\qquad F_0(a)=2^{-n}\sum_{\varepsilon\in\{-1,1\}^n}\left|\sum_{j=1}^n a_j\varepsilon_j\right|^n.
\]
The exact **uniform relative-error constant** is
\[
\boxed{\quad \sup_{a\ne0}\left|\frac{F_\theta(a)}{F_0(a)}-1\right|
=|\theta|\lambda_n,\qquad
\lambda_n=\frac{n!}{M_n}=\frac{1}{[z^n](\cosh z)^n},\quad
M_n=2^{-n}\sum_{j=0}^n\binom nj(n-2j)^n.\quad}
\]
Equivalently, for all such coefficients,
\[
1-|\theta|\lambda_n\le\frac{F_\theta(a)}{F_0(a)}\le1+|\theta|\lambda_n.
\]
For \(\theta\ne0\), both endpoints are attained, and each endpoint is attained **only** by coefficients with identical nonzero absolute values, with the sign of their product chosen appropriately. In particular, \(\lambda_4=3/5\), \(\lambda_6=15/47\), and \(\lambda_8=315/1957\). If \(\theta=0\), the ratio is identically one for all nonzero coefficients.

The first detectable relative error decays exponentially with an exact prefactor. Let \(r>0\) be the unique solution of \(r\tanh r=1\). Then, as even \(n\to\infty\),
\[
\boxed{\quad\lambda_n\sim\frac{r\sqrt{2\pi n}}2
\left(\frac{r}{\cosh r}\right)^n.\quad}
\]
The exponential base \(r/\cosh r\) is strictly between zero and one (approximately \(0.66274342\)).

## Assumptions and scope
The sign vector has uniform independent marginals on every proper coordinate subset; it need not be jointly independent. Coefficients are real, and the moment order equals the even number of sign coordinates. The independent law is \(\theta=0\), while \(\theta=\pm1\) is the uniform distribution on one parity half of the cube. The denominator \(F_0(a)\) is strictly positive when \(a\ne0\). The norm ratio itself, if desired, equals the \(n\)-th root of the displayed moment ratio; the theorem concerns the **moment** ratio.

The lower moments of order strictly below \(n\) are exactly those of independent fair signs. Consequently \(n\) is the first polynomial moment degree capable of detecting the hidden dependence parameter; the theorem measures the worst multiplicative sensitivity precisely at that first degree.

## Proof
**1. Identify the sole hidden interaction.** Fourier--Walsh inversion applied to the cube shows that the law is necessarily
\[
\mathbb P(\xi=\varepsilon)=2^{-n}\left(1+\theta\prod_{j=1}^n\varepsilon_j\right)
\qquad(\varepsilon\in\{-1,1\}^n).
\]
The proper-coordinate Walsh coefficients vanish by the marginal hypothesis, and \(|\theta|\le1\) follows from nonnegativity. Conversely every such parameter produces the required law. Expanding the even \(n\)-th power shows that its unique contribution involving all \(n\) sign coordinates uses each coordinate once, with multinomial coefficient \(n!\). Therefore the exact identity is
\[
F_\theta(a)=F_0(a)+\theta n!\prod_{j=1}^n a_j.\tag{1}
\]
At every smaller polynomial moment order no complete-coordinate character appears, proving the lower-moment assertion.

**2. An opposite-direction geometric-moment extremal principle.** We prove
\[
\boxed{\ F_0(a)\ge M_n\prod_{j=1}^n|a_j|\ },\tag{2}
\]
with equality for nonzero \(a\) exactly when all \(|a_j|\) are equal and positive. If some coordinate is zero, the right side is zero while \(F_0(a)>0\), so inequality (2) is strict. Otherwise set \(u_j=\log|a_j|\). In the multinomial expansion, only even multiplicities survive the independent-sign expectation, and hence
\[
F_0(a)=n!\!\sum_{k_1+\cdots+k_n=n/2}\prod_{j=1}^n\frac{e^{2k_ju_j}}{(2k_j)!}=:G(u).
\]
This is a symmetric, strictly convex function on \(\mathbb R^n\). Convexity holds because every summand is a positive multiple of an exponential of a linear function; strictness follows from the \(n\) pure terms \(e^{nu_j}\), whose Hessians add a positive diagonal matrix at every point. Averaging \(u\) over all coordinate permutations gives \(\overline u\mathbf 1\), where \(\overline u=n^{-1}\sum u_j\). Jensen's inequality and symmetry now give
\[
G(u)\ge G(\overline u\mathbf1)=M_n e^{n\overline u}=M_n\prod_j|a_j|.
\]
Strict convexity forces equality only when \(u\) is constant. This proves (2), with its full equality case.

**3. Exact relative error and extremizers.** Divide (1) by \(F_0(a)\), take absolute values, and apply (2):
\[
\left|\frac{F_\theta(a)}{F_0(a)}-1\right|
=|\theta|\frac{n!\prod_j|a_j|}{F_0(a)}\le|\theta|\frac{n!}{M_n}.
\]
When \(a_j\) have equal nonzero absolute value, equality holds. Their product can have either sign independently of the law, which realizes both endpoints for \(\theta\ne0\). Strictness in Step 2 classifies all extremizers. For \(\theta=0\), both bounds coincide at one.

**4. Sharp large-order scale.** Let \(r\) denote the unique positive root of \(r\tanh r=1\); uniqueness follows because \(t\mapsto t\tanh t\) increases continuously from zero to infinity. Introduce the even-valued integer random variable
\[
\mathbb P(X=2k)=\frac{r^{2k}}{(2k)!\cosh r}\qquad(k\ge0).
\]
Then \(\mathbb EX=r\tanh r=1\) and
\[
\operatorname{Var}X=r\tanh r+r^2\operatorname{sech}^2r=r^2,
\]
where the final equality uses \(r\tanh r=1\). Its support has exact lattice span \(2\), positive variance, and exponential tails. For independent copies \(X_1,\ldots,X_n\), the standard lattice local central limit theorem at the mean (with even \(n\)) gives
\[
\mathbb P\left(\sum_{j=1}^nX_j=n\right)
\sim\frac{2}{r\sqrt{2\pi n}}.
\]
The generating function satisfies
\[
[z^n](\cosh z)^n=\left(\frac{\cosh r}{r}\right)^n
\mathbb P\left(\sum_{j=1}^nX_j=n\right).
\]
Taking reciprocals completes the exact asymptotic, including the factor of two arising from lattice span two. Finally, \(\cosh r>r\), since \(\cosh t-t>0\) for \(t\ge0\), proving strict exponential decay.

## Verification
The accompanying `checker.py` uses only the Python standard library, enumerates all \(2^n\) sign configurations for \(n\in\{4,6,8\}\), and uses exact rational arithmetic for a range of coefficient vectors and dependence parameters. It independently checks (1), (2), the extremizer condition, and both sides of the sharp relative inequality, and reports `PARITY_NTH_RELATIVE_EXACT_OK 293`. These finite tests corroborate the algebra; the all-order statement and the asymptotic are proved analytically in Steps 1--4.

## Relationship to prior work
The published *Sharp endpoint Khintchine constants for next-to-independent Rademacher vectors* (2026) provides the same Walsh law classification and the unnormalized endpoint bound against Euclidean coefficient length. In particular, it proves an **upper** bound for \(F_0(a)\) at fixed Euclidean coefficient energy. The present exact multiplicative **relative** error is a distinct extremal functional: it requires the **lower** bound (2) at fixed coefficient geometric mean, not implied by that Euclidean upper bound, followed by a sharp large-order coefficient asymptotic. This note does not claim the law classification or the independent-moment upper bound as new.

Pass and Spektor (2017) study \(k\)-wise independent Khintchine inequalities with constants normalized against \(\ell_2\), not the relative \(n\)-th moment discrepancy between two sign laws. Gao and Qian (2026) analyze independent-sign high-moment geometry and finite-dimensional norm ratios, not the parity-induced error at the first detectable dependence degree. Dai and Kosov (2026) study empirical approximation of \(L^p\) norms for \(1<p<2\), a separate exponent range. The exact \(\lambda_n\) and its exponential saddlepoint prefactor were not identified in the inspected sources or targeted record searches; absence from a search cannot establish global priority.

## Limitations
The exact formula is restricted to even moment order equal to the number of coordinates, real coefficients, and fully fair \((n-1)\)-wise independent sign laws; it does not address lower-order independence, non-even moments, nonfair marginals, or vector-valued coefficients. The flat extremizers and asymptotic do not give a new sharp \(L^n/L^2\) Khintchine constant. The Gao--Qian primary manuscript's full text was not accessible during comparison, so the corresponding bibliographic assessment rests on its public abstract and topical description.

## References
1. P. Gao and J. Qian, *Fourth-Moment Geometry of Rademacher Sums*, arXiv:2608.17802 (first posted 18 August 2026), https://arxiv.org/abs/2608.17802 .
2. B. Pass and S. Spektor, *On Khintchine type inequalities for k-wise independent Rademacher random variables*, arXiv:1708.08775 (2017), https://arxiv.org/abs/1708.08775 .
3. B. Pass and S. Spektor, *On Khinchine type inequalities for pairwise independent Rademacher random variables*, arXiv:1412.7859 (2014), https://arxiv.org/abs/1412.7859 .
4. A. Dai and E. Kosov, *Empirical approximation of \(L^p\) norms for \(p\in(1,2)\)*, arXiv:2611.05930 (2026), https://arxiv.org/abs/2611.05930 .
5. *Sharp endpoint Khintchine constants for next-to-independent Rademacher vectors* (2026), prior published mathematical note on the variance-normalized moment constant; its result is distinguished in the preceding section.
