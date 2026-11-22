# A square-root validation/backtracking frontier for sampled Armijo acceptance at a least-squares optimum

## Finding
Consider a one-dimensional least-squares problem with two equally weighted observations at targets \(-1\) and \(+1\), evaluated at its exact full-data minimizer. A correction constructed from one randomly drawn observation and tested on an independent validation batch of \(s\) observations by finite dyadic Armijo backtracking has an **exact binomial false-acceptance probability**. Its sharp phase parameter is the product of the smallest trial displacement and \(\sqrt{s}\). Deepening backtracking at the same rate as increasing validation size can leave a strictly positive probability of accepting a full-objective ascent step, even though every candidate is tested on an independent batch.

Let \(c\in(0,1)\) be the Armijo constant and let \(J\ge0\) be the maximal number of halvings. Put \(a_J=2^{-J}\), \(t_J=a_J/[2(1-c)]\). Then the probability \(p_{s,J}\) of accepting a nonzero step is
\[
p_{s,J}=2^{-s}\sum_{k=\lceil s(1+t_J)/2\rceil}^{s}\binom{s}{k},
\]
interpreting an empty sum as zero. **Every accepted step strictly increases the full objective.** At the motivating implementation settings \(c=10^{-4}\), \(J=5\), and a 64-row validation batch, the exact probability is \(8307059966383480541/18446744073709551616\) (approximately \(0.4503266231\)). For any sequence \(J=J(s)\), the three sharp regimes are
\[
\begin{aligned}
\sqrt{s}\,2^{-J(s)}\longrightarrow \infty&\quad\Longrightarrow\quad p_{s,J(s)}\longrightarrow0,\\
\sqrt{s}\,2^{-J(s)}\longrightarrow a\in[0,\infty)&\quad\Longrightarrow\quad p_{s,J(s)}\longrightarrow 1-\Phi\!\left(\frac{a}{2(1-c)}\right).
\end{aligned}
\]
Here \(\Phi\) is the standard normal cumulative distribution function. In particular, when \(2^{-J}=o(s^{-1/2})\), the false-acceptance probability tends to \(1/2\). Thus \(J\) has a sharp transition on the scale \(\frac12\log_2 s\); at \(s=4^m\), \(J=m+j\), the limit is \(1-\Phi(2^{-j}/[2(1-c)])\).

Let \(x_+\) be the first accepted candidate, or zero if every candidate fails, and let \(\phi\) denote the half-sum-normalized full objective below. If \(\sqrt{s}\,2^{-J}\to0\), the expected damage has a nonvanishing, sharp-order scale:
\[
\frac{(1-c)^2}{4}\le \liminf_{s\to\infty}s\,\mathbb E[\phi(x_+)-\phi(0)]
\le\limsup_{s\to\infty}s\,\mathbb E[\phi(x_+)-\phi(0)]\le(1-c)^2.
\]
The two outer constants are universal dyadic-envelope bounds, **not** claimed to be equal or optimal asymptotic constants.

In validation-budget form, if \(J\to\infty\) and \(s/4^J\to\kappa\in(0,\infty)\), then
\[
p_{s,J}\longrightarrow1-\Phi\!\left(\frac{\sqrt{\kappa}}{2(1-c)}\right).
\]
For a prescribed limiting false-acceptance level \(\eta\in(0,1/2)\), the sharp critical sample-to-depth ratio is \(\kappa_\eta=4(1-c)^2[\Phi^{-1}(1-\eta)]^2\): ratios below this value yield a limiting failure probability greater than \(\eta\), and ratios above yield a smaller limit. This is a finite-grid, one-step **validation-budget law**; it is not a general error-control rule.

## Assumptions and scope
The two rows of the matrix are both \(1\), and the observations are \(-1,+1\). Define
\[
\phi(x)=\frac14\big((x-1)^2+(x+1)^2\big)=\frac12(x^2+1).
\]
The full-data objective is the sum \(F=2\phi\), so scaling does not affect an Armijo decision. Start at \(x_0=0\), which uniquely minimizes both \(F\) and \(\phi\). The unconstrained correction space is all of \(\mathbb R\). The correction sample consists of a single row, drawn uniformly from the two rows. Its zero-start least-squares step or sampled gradient followed by exact sampled one-dimensional scaling proposes the displacement \(b\in\{-1,1\}\), where \(b\) is the selected observed target. The initial step length is therefore one in displacement coordinates.

Independently sample \(s\ge1\) validation rows **with replacement** from the same uniform row law. Fix \(c\in(0,1)\). For \(j=0,\ldots,J\), test the candidate \(b2^{-j}\) in that order; accept the first one satisfying both a strict negative sampled directional derivative and the ordinary sampled Armijo inequality. All candidates use the same validation batch; if all fail, return \(0\). The random correction sign and validation sample are independent. These are one-sweep, exact-arithmetic assumptions. No assertion is made about general multidimensional iterations or the confidence-margin-certified test.

## Proof
Let \(B_1,\ldots,B_s\) be independent fair signs, write \(\overline B=s^{-1}\sum_{i=1}^sB_i\), and orient them by the independent correction sign \(b\), so \(Y=b\overline B\). Conditional on either correction sign, \(Y\) has the law \((2K-s)/s\), where \(K\sim\operatorname{Bin}(s,1/2)\). Up to a harmless positive factor, the sampled validation objective is \(\widehat\phi(x)=s^{-1}\sum_i(x-B_i)^2/2\), with \(\widehat\phi'(0)=-\overline B\).

For a candidate displacement \(z=b\alpha\), \(\alpha>0\), direct expansion gives
\[
\widehat\phi(z)-\widehat\phi(0)=\frac{\alpha^2}{2}-\alpha Y,
\qquad\widehat\phi'(0)z=-\alpha Y.
\]
The two sampled Armijo checks are equivalent to
\[
Y\ge\frac{\alpha}{2(1-c)}>0.
\]
As the candidate magnitudes form the decreasing dyadic grid \(1,1/2,\ldots,2^{-J}\), at least one is accepted precisely when \(Y\ge t_J\). Counting the fair sign outcomes produces the asserted exact binomial tail; an empty tail is zero. Since every accepted \(z\ne0\) satisfies \(\phi(z)-\phi(0)=z^2/2>0\), all acceptance is false acceptance relative to full-objective descent.

For a sequence \(s\to\infty\), the central limit theorem gives \(\sqrt{s}Y\Rightarrow N(0,1)\). If \(\sqrt{s}a_J\to a<\infty\), continuity of the normal distribution gives the stated normal-tail limit, including \(a=0\). If \(\sqrt{s}a_J\to\infty\), Hoeffding's inequality gives
\[
p_{s,J}\le\exp\left(-\frac{s\,2^{-2J}}{8(1-c)^2}\right)\longrightarrow0.
\]
The subsequence \(s=4^m\), \(J=m+j\) realizes each fixed dyadic critical parameter.

For the expected-increase assertion, on \(Y\ge t_J\) put \(q=2(1-c)Y\). The accepted displacement magnitude \(\alpha\) is the largest member of the dyadic grid not exceeding \(q\). Since \(q<2\) and \(\alpha\) is positive, \(q/2<\alpha\le q\), including the possible largest-grid saturation at \(1\). Therefore
\[
\frac{(1-c)^2}{2}Y^2\mathbf1_{Y\ge t_J}
\le \phi(x_+)-\phi(0)
\le2(1-c)^2Y^2\mathbf1_{Y\ge t_J}.
\]
By symmetry and \(\mathbb E[Y^2]=1/s\), we have \(s\mathbb E[Y^2\mathbf1_{Y>0}]=1/2\). Moreover
\(0\le s\mathbb E[Y^2\mathbf1_{0<Y<t_J}]\le st_J^2\to0\) whenever \(\sqrt{s}a_J\to0\). Expectations in the displayed inequality yield the stated bounds. No finite experiment is used to prove the infinite-parameter limits.

## Verification
Run `python checker.py` (Python standard library only). It independently constructs both correction signs and every possible validation sign string, applies the full sampled objective and negative-derivative plus Armijo comparisons using exact fractions, and compares the observed acceptance fraction to the binomial formula for multiple \(s\), \(J\), and \(c\). It also makes finite Gaussian-critical-window spot checks. The exact-arithmetic replay returned `PASS: 168 full-algorithm exact-rational cases, 12192 correction/validation outcomes; Gaussian-window spot checks passed`. Numerical limit checks are illustrative; the central limit theorem and Hoeffding bound carry the asymptotic proof.

## Relationship to prior work
Di, *Stochastic Multilevel Sampling for Inverse Problems via Coarse-Space Identifiability* (arXiv:2611.12667, version 1, November 9, 2026) defines an independent-batch projected Armijo test in Algorithm 3.1 and Equation (4.22), and proves a **different**, margin-corrected sufficient-decrease guarantee in Proposition 4.8. The present model uses the uncorrected experimental test specialized to a single scalar correction space; it does not contradict Proposition 4.8. Its new question is the exact probability of erroneous acceptance at a full-data stationary point as the validation size and backtracking depth vary jointly. Paquette and Scheinberg's *A Stochastic Line Search Method with Convergence Rate Analysis* (arXiv:1807.07994, 2018) already recognizes that noisy Armijo decisions can permit uphill steps and analyzes adaptive-oracle accuracy and iteration complexity. That general failure mechanism is not claimed as new here: the assessed fact is the exact binomial law and the sharp square-root coupling with backtracking depth for this independently validated finite-grid rule.

## Limitations
The model has exactly two contradictory scalar observations, a single correction-row draw, one unconstrained correction stage, and fair with-replacement validation. It gives one-step false acceptance, not global convergence or a guarantee of large objective damage. In the deep-backtracking regime the expected objective increase decays at order \(1/s\), despite the false-acceptance probability tending to \(1/2\). The main source's experiments keep \(J=5\), whereas the phase transition concerns growing \(J\) jointly with validation size. The confidence-margin-certified version of the test is outside the claim. Older stochastic line-search results may contain implicit consequences; no independent audit or exhaustive priority certification is claimed.

## References
1. Z. W. Di, *Stochastic Multilevel Sampling for Inverse Problems via Coarse-Space Identifiability*, arXiv:2611.12667v1, November 9, 2026. https://arxiv.org/abs/2611.12667
2. C. Paquette and K. Scheinberg, *A Stochastic Line Search Method with Convergence Rate Analysis*, arXiv:1807.07994v1, July 20, 2018. https://arxiv.org/abs/1807.07994
3. B. Jin, K. Scheinberg, M. Xie, *High Probability Complexity Bounds for Adaptive Step Search Based on Stochastic Oracles*, SIAM J. Optim. 34 (2024), 2411–2439. https://doi.org/10.1137/22M1512764
