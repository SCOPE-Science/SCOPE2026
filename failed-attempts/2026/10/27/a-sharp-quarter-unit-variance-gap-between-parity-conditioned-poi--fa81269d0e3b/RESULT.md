# A sharp quarter-unit variance gap between parity-conditioned Poisson trinomial scores

## Finding
Let \(X_1,\ldots,X_n\) be independent random variables supported on \(\{0,1/2,1\}\), with arbitrary nonnegative masses, and suppose both events \(S=\sum_iX_i\in\mathbb Z\) and \(S\in\mathbb Z+1/2\) have positive probabilities. Let \(E\) and \(O\) denote the respective conditional distributions. Then
\[
-\frac14\le\operatorname{Var}(E)-\operatorname{Var}(O)\le\frac14.
\]
Both constants are attained, even with two or fewer summands. The estimate is independent of the number of summands and of their individual probabilities.

## Assumptions and scope
Here \(n\ge1\) is finite. For each \(i\), write \(\Pr(X_i=0)=L_i\), \(\Pr(X_i=1/2)=T_i\), and \(\Pr(X_i=1)=W_i\), with \(L_i+T_i+W_i=1\). No identical-distribution or positivity condition is imposed other than positive probabilities for the two conditioning events. A conditional variance refers to the ordinary variance of the conditional score, not to the variance of an independent coupling.

## Proof
First assume all \(L_i,T_i,W_i\) are positive. The generating polynomial for \(2S\) is
\[
G(w)=\prod_{i=1}^n(L_i+T_iw+W_iw^2)=P(w^2)+wQ(w^2).
\]
Every quadratic factor has both zeros strictly in the open left half-plane: its zero sum is \(-T_i/W_i<0\) and product \(L_i/W_i>0\). Thus \(G\) is Hurwitz stable. The strict Hermite--Biehler theorem for a stable real polynomial of even degree shows that \(P\) has \(n\) negative real zeros and \(Q\) has \(n-1\) negative real zeros which strictly alternate with the zeros of \(P\). The even and odd score generating functions are respectively \(P(z)/P(1)\) and \(z^{1/2}Q(z)/Q(1)\), so the conditional laws are Poisson-binomial sums, with the odd law shifted by \(1/2\).

Write the zeros of \(P\) as \(-\beta_1,\ldots,-\beta_n\) and those of \(Q\) as \(-\gamma_1,\ldots,-\gamma_{n-1}\), with the ordering chosen so that the Bernoulli success parameters
\[
t_i=(1+\beta_i)^{-1},\qquad u_j=(1+\gamma_j)^{-1}
\]
satisfy \(1>t_1>u_1>t_2>\cdots>u_{n-1}>t_n>0\). This follows because the transformation \(b\mapsto(1+b)^{-1}\) strictly reverses the order of positive root magnitudes. Factoring \(P/P(1)\) and \(Q/Q(1)\) gives
\[
\operatorname{Var}(E)=\sum_{i=1}^n t_i(1-t_i),\qquad
\operatorname{Var}(O)=\sum_{j=1}^{n-1}u_j(1-u_j).
\]
The extra half-unit shift in \(O\) does not change its variance.

Define for \(0\le x\le1\) the alternating-count function
\[
B(x)=\sum_{i=1}^n\mathbf1_{\{x\le t_i\}}-\sum_{j=1}^{n-1}\mathbf1_{\{x\le u_j\}}.
\]
The displayed interlacing forces \(B(x)\in\{0,1\}\) at all non-root points. Since \(t(1-t)=\int_0^t(1-2x)\,dx\), the difference of conditional variances is exactly
\[
\Delta=\int_0^1(1-2x)B(x)\,dx.
\]
The integrand weight is nonnegative on \([0,1/2]\) and nonpositive on \([1/2,1]\). Therefore
\[
-\int_{1/2}^1(2x-1)\,dx\ \le\ \Delta\ \le\ \int_0^{1/2}(1-2x)\,dx,
\]
and both endpoint integrals equal \(1/4\). This proves the inequality for strictly positive masses.

For general nonnegative masses, replace each probability triple by its convex mixture with \((1/3,1/3,1/3)\), with mixture weight \(\varepsilon>0\). Each perturbed array is strictly positive. Its conditional means and second moments are ratios of polynomials in the masses whose denominators are the respective parity probabilities. Because those original denominators are positive, all ratios, and hence both conditional variances, converge as \(\varepsilon\downarrow0\). This proves the general inequality.

Both signs are attained: for a single \(X_1\) with \(\Pr(X_1=0,1/2,1)=(1/4,1/2,1/4)\), the integer conditional law is a fair two-point law on \(\{0,1\}\) and the half-integer conditional law is constant \(1/2\), giving \(\Delta=+1/4\). For two independent variables, take \(X_1\equiv1/2\) and let \(X_2\) have those same probabilities. Then the integer conditional law is the constant \(1\), while the half-integer conditional law is fair on \(\{1/2,3/2\}\), giving \(\Delta=-1/4\).

## Verification
The included `verify.py` performs exact-rational distribution convolution and conditional moment computations directly in the original score space, without using the root-interlacing representation. It enumerates all denominator-four probability triples for \(n\le4\), checks 1,200 additional deterministic sampled configurations with up to nine variables, and verifies both sharp endpoint examples. The saved output reports 53,886 exact finite-law checks. Finite enumeration is corroboration only; the proof for all \(n\) is the analytic Hermite--Biehler/integral argument above.

## Relationship to prior work
Broadie and Petkova (2026) establish the conditional Poisson-binomial representations and bounds on means and modes for these half-integral score sums; their generating-polynomial proof supplies the Hurwitz-stability setting. The alternating placement of the Bernoulli parameters, rather than merely separate real-rootedness, yields this sharp **variance** comparison. Hermite--Biehler root interlacing itself is classical, not a new lemma. The distinct variance assertion is not a logical consequence of an abstract coupling with fixed displacement \(1/2\): fair two-point laws on \(\{0,N\}\) and \(\{1/2,N-1/2\}\) admit such a coupling, but their variance difference equals \((2N-1)/4\), which is unbounded as \(N\to\infty\). The stronger alternating-root structure is essential to the dimension-free bound.

## Limitations
The result requires independent summands on the stated three-value support and nonzero masses for both parity classes. It neither covers arbitrary dependent scores nor bounds the absolute unconditional variance. The proof employs a standard classical stability theorem, and an unlocated earlier application of its root interlacing to these conditional variances remains a priority risk. No independent mathematical audit has been carried out.

## References
1. M. Broadie and I. Petkova, *On the structure of the Poisson trinomial distribution*, arXiv:2603.09019v1, first public 2026-03-09, https://arxiv.org/html/2603.09019v1.
2. R. Ellard and H. Šmigoc, *An extension of the Hermite--Biehler theorem with application to polynomials with one positive root*, arXiv:1701.07912, 2017, https://arxiv.org/abs/1701.07912.
