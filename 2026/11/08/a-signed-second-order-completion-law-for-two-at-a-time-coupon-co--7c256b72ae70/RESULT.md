# A signed second-order completion law for two-at-a-time coupon collection

## Finding
For each integer \(n\ge2\), repeatedly draw uniformly and independently one unordered pair of distinct coupon types from \(\{1,\ldots,n\}\). Let \(Z_{n,m}\) be the number of types never drawn in the first \(m\) draws. Define \(c_n=2m/n-\log n\) and \(\lambda_n=e^{-c_n}\). For every fixed compact real interval \(I\), uniformly over integers \(m\ge0\) such that \(c_n\in I\),
\[
\Pr(Z_{n,m}=0)=e^{-\lambda_n}\left[1-\frac{\lambda_n^2+(\lambda_n^2-2\lambda_n)(\log n+c_n)}{2n}\right]+O_I\!\left(\frac{(\log n)^2}{n^2}\right).
\]
For every fixed \(c\ne-\log 2\) and \(m_n=\lfloor (n/2)(\log n+c)\rfloor\), the first correction to \(e^{-\lambda_n}\) is asymptotic to \(-e^{-e^{-c}}e^{-c}(e^{-c}-2)(\log n)/(2n)\). Its sign changes at the unique point \(c=-\log2\). At that point, with the same integer rounding,
\[
\Pr(Z_{n,m_n}=0)-e^{-\lambda_n}=-\frac{2e^{-2}}{n}+O\!\left(\frac{(\log n)^2}{n^2}\right).
\]
The comparison uses the precisely defined parameter \(\lambda_n\), not the finite-sample missing-type mean.

## Assumptions and scope
The draws are independent across time, contain exactly two *distinct* coupon types, and every unordered pair has probability \(1/\binom n2\). Integer \(m\) is nonnegative. The asymptotics are for \(n\to\infty\) with \(c_n\) in an arbitrary fixed bounded interval. The uniform big-O constant may depend on the interval. No extension to larger group sizes or unequal sampling weights is asserted.

## Proof
Let \(E_i\) denote the event that type \(i\) is absent. A specified set of \(k\) types is missed in one drawing with probability
\[
q_{n,k}=\frac{(n-k)(n-k-1)}{n(n-1)}
\]
for \(0\le k\le n-2\), and with probability zero for larger \(k\) (when \(m>0\)). Inclusion-exclusion therefore gives the *exact* finite formula
\[
\Pr(Z_{n,m}=0)=\sum_{k=0}^n(-1)^k\binom nk q_{n,k}^{m}.
\]
Write \(L_n=\log n+c_n=2m/n\). For every fixed \(k\), Taylor expansion, uniformly for bounded \(c_n\), gives
\[
\log q_{n,k}=-\frac{2k}{n}-\frac{k(k+1)}{n^2}+O\!\left(\frac{(k+1)^3}{n^3}\right),\qquad
\binom nk=\frac{n^k}{k!}\left[1-\frac{k(k-1)}{2n}+O\!\left(\frac{(k+1)^4}{n^2}\right)\right].
\]
Combining with \(m=nL_n/2\) yields
\[
\binom nk q_{n,k}^m=\frac{\lambda_n^k}{k!}\left[1-\frac{k(k-1)+k(k+1)L_n}{2n}\right]+O_I\!\left(\frac{\lambda_n^k}{k!}\frac{(k+1)^8L_n^2}{n^2}\right).
\]
This expansion can be summed: truncate at \(K_n=\lceil 6\log n\rceil\). For \(k\le K_n\), Taylor remainders obey the displayed weighted polynomial bound for all sufficiently large \(n\). For \(k>K_n\), use \(q_{n,k}\le(1-k/n)^2\le e^{-2k/n}\) to get
\[
0\le \binom nk q_{n,k}^{m}\le \frac{n^k}{k!}e^{-2mk/n}=\frac{\lambda_n^k}{k!}.
\]
The omitted factorial tails, also after multiplying by any fixed polynomial in \(k\), are smaller than \(n^{-A}\) for any fixed \(A\), uniformly over bounded \(c_n\). The sum of the errors for the remaining terms is \(O_I(L_n^2/n^2)\), as \(\sum_{k\ge0}C^k(k+1)^8/k!<\infty\) for fixed \(C\). Thus no interchange of an unbounded asymptotic series is assumed without domination.

Finally, the alternating exponential sums are
\[
\sum_{k\ge0}\frac{(-1)^k\lambda^k}{k!}=e^{-\lambda},\quad
\sum_{k\ge0}\frac{(-1)^k\lambda^k k(k-1)}{k!}=\lambda^2e^{-\lambda},\quad
\sum_{k\ge0}\frac{(-1)^k\lambda^k k(k+1)}{k!}=(\lambda^2-2\lambda)e^{-\lambda}.
\]
Substitution proves the uniform expansion. For fixed \(c\), \(\lambda_n=e^{-c}+O(1/n)\) under flooring, so the coefficient of \(\log n/n\) is \(-e^{-\lambda}\lambda(\lambda-2)/2\), and its only positive zero is \(\lambda=2\). At the exceptional centering \(c=-\log2\), \(\lambda_n=2+O(1/n)\), so its logarithmic term is absorbed into the error and the remaining term is \(-2e^{-2}/n\). This proves the sign statements and the exceptional correction.

## Verification
`verify.py` is a standalone Python-standard-library checker. It verifies the exact inclusion-exclusion formula against an independently implemented finite-state recursion in the number of missing coupons for \(2\le n\le9\) and \(0\le m\le18\), and compares high-precision probabilities with the asymptotic expansion over three centerings and four sizes. The checked run reported `VERIFY_OK 171 checks`. These computations corroborate the proof and do not establish its infinite quantifiers.

## Relationship to prior work
Schilling and Henze (2021) establish Poisson limits in coupon collection with group drawings. Betken and Thäle (arXiv 2022; published 2023) develop a general quantitative Poisson approximation with order \((\log n)/n\), noting earlier bounds from Barbour, Holst, and Janson. The present statement evaluates an explicit *signed* correction for the probability of complete collection under fixed pair drawings, including a unique cancellation point; the general approximation bounds alone do not determine that correction. The inclusion-exclusion method is classical, and no priority claim is made for that method or the leading limit law.

## Limitations
This is a second-order asymptotic for a single completion probability, not a better total-variation bound for the missing-count distribution. The special cancellation is relative to the canonical parameter \(\lambda_n=e^{-c_n}\); replacing it by the exact finite-sample mean changes the displayed correction. Historical priority of the evaluated coefficient is not independently certified. The source paper by Schilling and Henze was inspected in its accessible abstract only.

## References
1. J. Schilling and N. Henze, *Two Poisson limit theorems for the coupon collector's problem with group drawings*, Journal of Applied Probability, first published online 22 November 2021, https://www.cambridge.org/core/journals/journal-of-applied-probability/article/two-poisson-limit-theorems-for-the-coupon-collectors-problem-with-group-drawings/14AC31D4C06D477DD4A613B846AE3CAE.
2. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, arXiv:2202.07485 (first submitted 15 February 2022); Journal of Applied Probability 60 (2023), 1352–1366, https://doi.org/10.1017/jpr.2023.6.
3. A. D. Barbour, L. Holst, and S. Janson, *Poisson Approximation*, 1992, cited for general approximation bounds by Betken and Thäle.
