# A log-log finite-hyperexpansivity cutoff beyond the geometric-shift boundary

## Finding

Fix \(p>1\), \(q=p^{-1}\), and \(0<a<p^{-1}\). For \(\varepsilon>0\) sufficiently small, put \(b=pa+\varepsilon<\min(1,p^2a)\) and consider the unilateral weighted shift
\[
W_\varepsilon e_n=\left(\frac{p^n-a}{p^n-b}\right)^{1/2}e_{n+1}\quad(n\ge0).
\]
Let \(\gamma_0=1\) and \(\gamma_n=\prod_{j=0}^{n-1}(p^j-a)/(p^j-b)\). Write \(\Delta\gamma_n=\gamma_{n+1}-\gamma_n\). Define \(M(\varepsilon)\) to be the largest \(m\ge1\) such that \((-1)^{j+1}\Delta^j\gamma_n\ge0\) for every \(n\ge0\) and every \(1\le j\le m\). Equivalently, the shift is \(M(\varepsilon)\)-hyperexpansive but not \((M(\varepsilon)+1)\)-hyperexpansive.

**Exact finite-order threshold.** Let
\[
F_\varepsilon(z)=\prod_{j=0}^\infty\frac{1-bq^jz}{1-aq^jz}
=\sum_{k=0}^\infty c_kz^k,
\qquad
c_0=1,\qquad
c_k=\frac{a-bq^{k-1}}{1-q^k}c_{k-1}.
\]
Then \(c_1<0\), \(c_k>0\) for \(k\ge2\). With
\[
R_m(\varepsilon)=\sum_{k=2}^\infty\frac{c_k}{-c_1}
\left(\frac{1-q^k}{1-q}\right)^m,
\]
there is a finite, uniquely determined integer \(M(\varepsilon)\ge1\) characterized by
\[
\boxed{R_{M(\varepsilon)}(\varepsilon)\le1<R_{M(\varepsilon)+1}(\varepsilon).}
\]
All sums converge absolutely for each fixed \(m\).

**Sharp logarithmic boundary law.** As \(\varepsilon\downarrow0\) with \(p,a\) held fixed,
\[
\boxed{M(\varepsilon)=\frac{\log(1/\varepsilon)+\frac{\log(1/a)}{\log p}\log\log(1/\varepsilon)}{\log(1/(1-p^{-1}))}+O_{p,a}(1).}
\]
Thus the first failing hyperexpansivity order diverges logarithmically at the completely hyperexpansive boundary, but has an unavoidable positive log-log correction.

## Assumptions and scope

The conditions \(0<a<p^{-1}\) and \(0<\varepsilon<\min(1,p^2a)-pa\) ensure all weights are positive, bounded, and larger than one. The parameters correspond to the geometrically regular shift with \(N=-a\), \(D=-b\); the limiting ray \(b=pa\) belongs to its completely hyperexpansive sector. The result concerns all tail indices \(n\ge0\) and *all* difference orders through \(m\), not just a single inequality at \(n=0\).

The notation \(O_{p,a}(1)\) means a bound uniform in \(\varepsilon\) sufficiently small with \(p,a\) fixed. The theorem makes no uniform claim when \(p\) or \(a\) varies with \(\varepsilon\).

## Proof

**1. Charge expansion and signs.** The product defining \(F_\varepsilon\) is analytic on \(|z|<1/a\) because its factors converge locally uniformly and \(b<1\). Multiplying \(F_\varepsilon(qz)(1-bz)=F_\varepsilon(z)(1-az)\) gives the coefficient recurrence displayed above. Since \(b>pa>a\), its first coefficient is negative; since \(b<p^2a\), the factor \(a-bq^{k-1}\) is strictly positive for \(k\ge3\), whereas the factor at \(k=2\) is negative. Hence \(c_1<0\) and \(c_k>0\) for every \(k\ge2\). Because \(a<1\), the coefficients are absolutely summable.

The telescoping infinite products give, exactly,
\[
\gamma_n=\frac{F_\varepsilon(q^n)}{F_\varepsilon(1)}
=\frac1{F_\varepsilon(1)}\sum_{k\ge0}c_kq^{kn},\qquad F_\varepsilon(1)>0.
\]
In particular, this is a signed, summable atomic representation; no positivity of the charge is assumed. Termwise differences are justified by absolute convergence and yield, for \(m\ge1\),
\[
(-1)^{m+1}\Delta^m\gamma_n=
\frac{(-c_1)(1-q)^mq^n}{F_\varepsilon(1)}
\left[1-\sum_{k\ge2}\frac{c_k}{-c_1}
\left(\frac{1-q^k}{1-q}\right)^m q^{(k-1)n}\right].
\]
Every summand inside the brackets is nonnegative and decreases as \(n\) increases. Therefore the inequality at a fixed order \(m\) holds for all \(n\) if and only if it holds at \(n=0\), that is, exactly when \(R_m\le1\). Each ratio \((1-q^k)/(1-q)>1\) for \(k\ge2\), so \(R_m\) increases strictly in \(m\). First-order positivity follows independently from \(\gamma_{n+1}/\gamma_n=(p^n-a)/(p^n-b)>1\); hence \(R_1<1\). Since \(c_2>0\), the \(k=2\) summand shows \(R_m\to\infty\). The unique integer threshold follows.

**2. Uniform coefficient bounds.** The second coefficient satisfies
\[
\frac{c_2}{-c_1}=\frac{q\varepsilon}{1-q^2}.
\]
For \(k\ge2\), the exact ratio is
\[
\frac{c_k}{-c_1}=\frac{q\varepsilon}{1-q^2}
 a^{k-2}\prod_{j=3}^k\frac{1-(b/a)q^{j-1}}{1-q^j}.
\]
Choose \(\varepsilon_0>0\) so that \(pa+\varepsilon_0<\min(1,p^2a)\). The numerator factors are uniformly bounded away from zero at \(j=3\), and their deficits from one form a uniformly summable geometric tail. The denominator factors are likewise bounded away from zero with a convergent product. Consequently there are positive constants \(A,B\), depending only on \(p,a,\varepsilon_0\), such that
\[
A\varepsilon a^{k-2}\le\frac{c_k}{-c_1}\le B\varepsilon a^{k-2},
\qquad k\ge2,\quad0<\varepsilon\le\varepsilon_0.
\]

**3. The logarithmic saddle.** Put \(\beta=\log(1/a)/\log p>1\), \(L=-\log(1-q)>0\), and
\[
S_m=\sum_{k\ge2}a^{k-2}(1-q^k)^m.
\]
We claim that \(S_m\asymp_{p,a}m^{-\beta}\). For \(r=\lfloor\log_p m\rfloor\), the upper tail \(k\ge\max(2,r)\) is at most a constant times \(a^r\). For \(2\le k<r\), write \(k=r-j\). The inequality \((1-x)^m\le e^{-mx}\) and \(m q^{r-j}\ge p^j\) give
\[
\sum_{2\le k<r}a^{k-2}(1-q^k)^m
\le a^{r-2}\sum_{j\ge1}a^{-j}e^{-p^j}
\le C_{p,a}a^r.
\]
The series converges superexponentially. Conversely, at \(k=r+2\), one has \(mq^{r+2}<q\), so Bernoulli's inequality gives \((1-q^{r+2})^m\ge1-mq^{r+2}>1-q\). This single term contributes at least \((1-q)a^r\). As \(p^r\le m<p^{r+1}\), the quantities \(a^r\) and \(m^{-\beta}\) are comparable with fixed constants. This proves the claim for all \(m\ge1\).

Using the coefficient bounds and factoring \((1-q)^{-m}=e^{Lm}\), we obtain constants independent of small \(\varepsilon\) and all \(m\ge1\) such that
\[
\boxed{R_m(\varepsilon)\asymp_{p,a}\varepsilon e^{Lm}m^{-\beta}.}
\]

**4. Location of the first failure.** Define \(H=\log(1/\varepsilon)\). Since \(R_M\le1<R_{M+1}\), the preceding two-sided estimate implies
\[
LM-\beta\log M=H+O_{p,a}(1).
\]
Indeed, the inequality for \(M+1\) gives the reverse bound after replacing \(M+1\) by \(M\), changing the expression by at most \(L\) plus an \(O(1/M)\) correction. The solution has \(M\to\infty\) and \(M=H/L+O(\log H)\), whence \(\log M=\log H+O(1)\). Substitution gives \(LM=H+\beta\log H+O_{p,a}(1)\), precisely the claimed expansion.

## Verification

The standalone `check.py` checks the coefficient recurrence and explicit moment ratios with exact rational arithmetic, tests finite differences at multiple shifts and orders, and compares several exact integer thresholds against the stated two-term asymptotic. Run `python3 check.py` in an ordinary Python 3 environment; it requires no nonstandard packages. Those tests are *finite diagnostics*, not proofs of the infinite product, complete order classification, or asymptotic estimates, which are established analytically above.

## Relationship to prior work

Benhida, Curto and Exner's *Geometrically regular weighted shifts* (arXiv:2309.05888, originally submitted 12 September 2023), especially Theorem 2.10, proves complete hyperexpansivity inside the limiting sector, and develops the coefficient recurrence for signed moment charges. Their *Signed representing measures* (arXiv:2405.15000, submitted 23 May 2024) establishes further sign-pattern and charge information. Those qualitative descriptions are credited, and the mere failure of complete hyperexpansivity outside the boundary is **not** presented as new. The present assertion is the exact maximal finite difference order, uniformity over *every* tail index, and its two-term logarithmic/log-log blow-up along the near-boundary ray. The related paper on moment infinite divisibility and safe quotients (arXiv:2312.06390, originally submitted 11 December 2023) addresses different operator conditions.

## Limitations

The asymptotic has bounded, unspecified order-one fluctuations; no limiting constant for that remainder or joint \((p,a,\varepsilon)\)-scaling is claimed. The exact criterion involves an absolutely convergent infinite sum rather than a finite closed form. The weighted shifts are bounded but not asserted to be subnormal. Finite numerical diagnostics do not establish infinite-order conclusions. The comparison with accessible literature does not constitute a guarantee of historical priority or independent verification.

## References

1. C. Benhida, R. E. Curto, G. R. Exner, *Geometrically regular weighted shifts*, arXiv:2309.05888, first version 12 September 2023, https://arxiv.org/abs/2309.05888.
2. C. Benhida, R. E. Curto, G. R. Exner, *Signed representing measures (Berger-type charges) in subnormality and related properties of weighted shifts*, arXiv:2405.15000, first version 23 May 2024, https://arxiv.org/abs/2405.15000.
3. C. Benhida, R. E. Curto, G. R. Exner, *\(\mathcal{MID}\) and safe quotients for GRWS*, arXiv:2312.06390, first version 11 December 2023, https://arxiv.org/abs/2312.06390.
