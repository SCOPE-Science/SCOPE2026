# A sharp factor-two infinite-divisibility threshold for binned two-stage exponential lifetimes

## Finding

Let \(E_a\) and \(E_b\) be independent exponential waiting times with respective rates \(0<a\le b\), let \(T=E_a+E_b\), and record the completed integer-time bins \(X=\lfloor T\rfloor\). Then the law of \(X\), viewed either as a nonnegative integer distribution or as a distribution on the real line, is infinitely divisible **if and only if**
\[
 b\ge 2a.
\]
The criterion is sharp at every absolute rate scale. In the affirmative regime the distribution has an explicit compound-Poisson representation, including the boundary \(b=2a\); outside it, infinitely many even-index logarithmic generating-function coefficients are strictly negative.

In particular, the discrete Bilal distribution with parameter \(0<p<1\), defined by
\[
 \Pr(X=n)=3(1-p^2)p^{2n}-2(1-p^3)p^{3n},\qquad n=0,1,\ldots,
\]
is **never infinitely divisible**, despite having a log-concave probability-mass function. Its Poisson-mixed continuous Bilal counterpart **always** is infinitely divisible: if \(Y\mid T\sim\operatorname{Poisson}(T)\), then \(Y\) is the sum of two independent geometric counts. The latter geometric-sum representation is classical, not asserted as a new fact.

For discrete Bilal counts let \(N(p)\) be the first even index with a negative coefficient of the logarithmic probability-generating function. Define \(c_*>0\) as the unique root of \(e^{c/3}=1+e^{-c}\). Then
\[
 \lim_{p\uparrow1}(1-p)N(p)=c_*=0.9668538479130901801\ldots.
\]
Thus detecting non-divisibility may require checking an arbitrarily distant coefficient even though non-divisibility holds for every parameter.

## Assumptions and scope

All rates are strictly positive and \(a\le b\); reversing the labels does not change the law. The floor is taken with bins of width one. Both summands are independent and exponentially distributed, with survival \(\Pr(E_a>t)=e^{-at}\) for \(t\ge0\). The compound-Poisson characterization is the usual one for nonnegative integer laws with a positive atom at zero: infinite divisibility is equivalent to nonnegative, summable coefficients \(\lambda_n\) in \(\log(G(z)/G(0))=\sum_{n\ge1}\lambda_n z^n\). Such a distribution is a compound-Poisson sum of integer jumps with intensity \(\sum\lambda_n\). These assumptions exclude zero rates, dependent waiting times and arbitrary rounded rather than floored observations.

## Proof

**1. Binned hypoexponential generating function.** Assume first \(0<a<b\) and abbreviate
\[
 u=e^{-a},\quad v=e^{-b},\quad A=\frac{b(1-u)}{b-a},\quad B=\frac{a(1-v)}{b-a}.
\]
The hypoexponential survival function is \(\Pr(T\ge t)=(b e^{-at}-a e^{-bt})/(b-a)\). Subtract its values at consecutive integers to obtain, for every integer \(n\ge0\),
\[
 p_n:=\Pr(X=n)=Au^n-Bv^n,\qquad p_0=A-B>0.
\]
Consequently
\[
 G(z)=\sum_{n\ge0}p_nz^n=\frac{A}{1-uz}-\frac{B}{1-vz}
      =p_0\frac{1+rz}{(1-uz)(1-vz)},
 \quad r=\frac{Bu-Av}{A-B}.
\]
Here \(0<v<u<1\). Furthermore \(r>0\), since \(Bu-Av\) has the sign of \(a(e^b-1)-b(e^a-1)\), and \((e^t-1)/t\) is strictly increasing for \(t>0\).

**2. All-order infinite-divisibility criterion.** Expanding the logarithm at the origin gives for every \(n\ge1\)
\[
 \lambda_n:=[z^n]\log\frac{G(z)}{G(0)}
 =\frac{u^n+v^n+(-1)^{n-1}r^n}{n}.
\]
All odd coefficients are positive. If \(r\le u\), all even coefficients are also positive because \(u^n-r^n+v^n>0\). The series is absolutely summable at \(z=1\), and \(G(z)=\exp(\sum_{n\ge1}\lambda_n(z^n-1))\) gives the required compound-Poisson intensities \(\lambda_n\). Conversely, if \(r>u\), then for every sufficiently large even \(n\),
\[
 \left(\frac ru\right)^n>1+\left(\frac vu\right)^n,
\]
so \(\lambda_n<0\); the necessary compound-Poisson coefficient condition fails. Therefore \(X\) is infinitely divisible precisely when \(r\le u\).

**3. Exact factor-two threshold.** Put \(q=e^{-a}\in(0,1)\) and \(t=b/a>1\). By positive-denominator algebra, \(r\le u\) is equivalent to
\[
 F_q(t):=t(1-q)(1+q^{t-1})-2(1-q^t)\ge0.
\]
The exact identities \(F_q(1)=F_q(2)=0\) hold, and direct differentiation yields
\[
 F_q''(t)=q^{t-1}(\log q)
 \left[2(1-q)+(t(1-q)+2q)\log q\right].
\]
The logarithmic-mean inequality \(-\log q>2(1-q)/(1+q)\) holds for every \(0<q<1\) (set \(q=e^{-x}\) and use \(\tanh(x/2)<x/2\)). Since \(t\ge1\), the square bracket is strictly negative and \(\log q<0\), hence \(F_q''(t)>0\). Strict convexity with zeros at \(t=1,2\) makes \(F_q(t)<0\) for \(1<t<2\) and \(F_q(t)>0\) for \(t>2\). At \(t=2\) equality holds. Thus for unequal rates \(r\le u\) exactly when \(b\ge2a\), as claimed.

**4. Equal rates.** For \(b=a\), \(T\) is Erlang of shape two. With \(u=e^{-a}\) and \(D=1-u-au>0\),
\[
 \Pr(X=n)=u^n\{D+a(1-u)n\},\qquad
 G(z)=D\frac{1+rz}{(1-uz)^2},\quad
 r=\frac{u(a+u-1)}{D}.
\]
Both \(r\) and \(D\) are positive because \(e^a>1+a\) and \(a>1-e^{-a}\). Moreover \(r>u\) exactly when \(a(1+u)>2(1-u)\), again equivalent to \(a>2\tanh(a/2)\), which is strict. The same even-coefficient obstruction applies with \(v=u\). This covers the diagonal \(a=b\) and completes the criterion.

**5. Discrete Bilal and delayed obstruction.** The Bilal survival function equals \(3e^{-2t/\beta}-2e^{-3t/\beta}\), exactly the survival of the two-stage exponential sum with \(a=2/\beta\), \(b=3/\beta\); its floored count has \(p=e^{-1/\beta}\). Since \(b/a=3/2<2\), the result above proves non-divisibility for every \(0<p<1\). Direct substitution also yields \(u=p^2\), \(v=p^3\) and
\[
 r=p^2\frac{2+p}{1+2p},\qquad
 n\lambda_n=p^{2n}+p^{3n}+(-1)^{n-1}r^n.
\]
Hence an even index \(n\) is obstructing exactly when \(R(p)^n>1+p^n\), where \(R(p)=(2+p)/(1+2p)>1\). The function \(x\mapsto x\log R(p)-\log(1+p^x)\) is strictly increasing from \(-\log2\) to \(+\infty\), so it has one positive zero \(x_p\). Then \(N(p)=2(\lfloor x_p/2\rfloor+1)\) and \(0<N(p)-x_p\le2\). As \(p\uparrow1\), \(\log R(p)/(1-p)\to1/3\) and \(\log p/(1-p)\to-1\). Rescale the defining equation by \(c_p=(1-p)x_p\): it becomes
\[
 \exp\left(c_p\frac{\log R(p)}{1-p}\right)
 =1+\exp\left(c_p\frac{\log p}{1-p}\right).
\]
The two sides are respectively increasing and decreasing in \(c_p\), with a unique positive crossing. Pointwise convergence and monotonic bracketing imply \(c_p\to c_*\), the unique root of \(e^{c/3}=1+e^{-c}\). Since \(0<N(p)-x_p\le2\), the claimed limit for \(N(p)\) follows.

**6. Poisson observation of the same lifetime.** For \(Y\mid T\sim\operatorname{Poisson}(T)\), independent conditional sampling gives
\[
 H(z)=\mathbb E z^Y=\frac{a}{a+1-z}\frac{b}{b+1-z}
 =\prod_{\rho\in\{a,b\}}\frac{1-s_\rho}{1-s_\rho z},
 \qquad s_\rho=\frac1{1+\rho}.
\]
Therefore \(Y\) is the sum of two independent zero-based geometric counts, and has compound-Poisson intensities \(\{s_a^n+s_b^n\}/n>0\) for every \(n\ge1\), without a rate-ratio restriction. For the Bilal rates this is the Poisson–Bilal mixing model of Eliwa et al. This geometric-convolution property follows from standard classical theory; the new comparison is its contrast with the sharp binned-law boundary.

## Verification

The accompanying standalone `checks.py` performs symbolic generating-function identities, exact-rational sign and mass tests for a range of Bilal parameters, high-precision rate-ratio scans on both sides of the threshold, numerical examination of the delayed-index scaling and the elementary logarithmic-mean inequality. A replay produced 3,122 successful assertions. The infinite-support conclusions, unique scaling limit and exact threshold do **not** rely on finite enumeration or numerics: their justifications are the analytic arguments in Sections 2–6.

## Relationship to prior work

Altun, El-Morshedy and Eliwa introduced the discrete Bilal model and supplied its mass and generating functions, shape analysis and autoregressive application [1]. Freitas and colleagues examined censored discrete Bilal inference in an openly posted 2021 preprint [2]. Eliwa and coauthors introduced the Poisson–Bilal mixed-Poisson count model and studied its statistical properties [3]. Hürlimann's established theory covers log-generating-function coefficient tests and sums of independent geometric variables [4]. Krishnakumari and George subsequently considered a discretized two-parameter hypoexponential family and an integer-valued autoregressive process [5], overlapping the **object** but with no full text available for a conclusive comparison of the **specific criterion**. The claims here concern the exact universal \(2:1\) infinite-divisibility boundary for the floored two-rate sum, its specialized discrete Bilal obstruction law and the binned-versus-Poisson-observed contrast; the existing generating functions, classical convolution criterion, and geometric-sum representation are not claimed as novel discoveries.

## Limitations

A full-text priority comparison against [5] was not possible: the publisher-repository PDF was inaccessible and alternative institutional retrieval was unavailable. Its abstract names distributional and structural properties but does not explicitly assert the present infinite-divisibility threshold, so an unrecognized prior theorem remains possible; this is a historical-priority uncertainty, not a proof gap. The 2020 month-level release date attached to the original discrete Bilal work was not verified to an exact calendar day; the cited arXiv preprint [2], publicly dated 2 November 2021, supplies an independently verifiable exact-date antecedent. This result does not classify alternative discretizations, correlated stages, or renewal-process first-passage counts. Independent mathematical review has not been performed.

## References

[1] E. Altun, M. El-Morshedy, M. S. Eliwa, "A Study on Discrete Bilal Distribution with Properties and Applications on Integer-Valued Autoregressive Process," *REVSTAT–Statistical Journal* 20(4), 501–528 (2022). https://doi.org/10.57805/revstat.v20i4.384 ; full text: https://revstat.ine.pt/index.php/REVSTAT/article/download/384/577

[2] B. C. Lopes de Freitas, J. A. Achcar, M. V. Oliveira Peres, E. Z. Martinez, "Discrete Bilal distribution with right-censored data," arXiv:2111.01943, publicly posted 2021-11-02. https://arxiv.org/abs/2111.01943

[3] M. S. Eliwa, M. Ahsan-ul-Haq, A. Almohaimeed, A. Al-Bossly et al., "Discrete Extension of Poisson Distribution for Overdispersed Count Data: Theory and Applications," *Journal of Mathematics* 2023, article 2779120, first published 2023-02-13. https://doi.org/10.1155/2023/2779120

[4] W. Hürlimann, "The Concepts of Pseudo Compound Poisson and Partition Representations in Discrete Probability," *Journal of Probability and Statistics* 2015, article 189596. https://doi.org/10.1155/2015/189596

[5] K. Krishnakumari, D. George, "On Discrete Hypoexponential Distribution and Integer-valued Autoregressive Process," *Applications and Applied Mathematics* 20(1), article 6 (listed 2024). https://digitalcommons.pvamu.edu/aam/vol20/iss1/6/
