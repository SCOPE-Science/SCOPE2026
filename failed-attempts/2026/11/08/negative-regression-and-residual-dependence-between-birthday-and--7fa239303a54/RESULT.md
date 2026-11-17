# Negative regression and residual dependence between birthday and cover times

## Finding

Let \(X_1,X_2,\ldots\) be independent, uniformly sampled labels from \(\{1,\ldots,n\}\), where \(n\ge2\). Define the **birthday time** \(B_n\) as the draw index of the first repeated label and the **cover time** \(C_n\) as the first draw index by which all labels have appeared. Although the two times concern the same sample path and both are stopping times, they satisfy the following joint theorem.

**Conditional negative regression.** For every \(2\le t\le n\), the conditional distribution of \(C_n\) given \(B_n=t+1\) is stochastically strictly smaller than the conditional distribution given \(B_n=t\). Consequently, for all nondecreasing real functions \(f,g\) for which the covariance exists,
\[
\operatorname{Cov}(f(B_n),g(C_n))\le0.
\]
In particular \(\operatorname{Cov}(B_n,C_n)<0\) for every \(n\ge2\).

**Exact covariance.** With \((n)_{\underline j}=n(n-1)\cdots(n-j+1)\),
\[
\boxed{\operatorname{Cov}(B_n,C_n)=-\sum_{j=2}^n\frac{(n)_{\underline j}}{n^j}\sum_{k=1}^{j-1}\frac{k}{n-k}.}
\]
The first two values are \(-1/2\) and \(-8/9\), respectively.

**Two-scale limit.** Let \(R\) be Rayleigh with \(\Pr(R>x)=e^{-x^2/2}\) for \(x\ge0\), and let \(G\) be standard Gumbel with \(\Pr(G\le y)=e^{-e^{-y}}\). Then
\[
\left(\frac{B_n}{\sqrt n},\frac{C_n-n\log n}{n}\right)
\ \Longrightarrow\ (R,G),\qquad R\text{ and }G\text{ independent},
\]
but an unnormalized dependence remains:
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(B_n,C_n)}{\sqrt n}
=-\sqrt{\frac\pi8},\qquad
\lim_{n\to\infty}n\operatorname{Corr}(B_n,C_n)
=-\sqrt{\frac{3}{2\pi(4-\pi)}}.}
\]
The weak asymptotic independence and the nonzero residual covariance constant are compatible because the birthday and cover times fluctuate on different scales.

## Assumptions and scope

Each draw is independent and exactly uniform on \(n\) types, with sampling **with replacement**. A repetition is a second appearance of any previously seen label. Thus \(2\le B_n\le n+1\); if the first \(n\) draws are all distinct, then \(C_n=n\) and \(B_n=n+1\). This last event is included explicitly and is not approximated away in the finite formulas. All waiting times count the successful draw; a geometric random variable with success parameter \(p\) takes values \(1,2,\ldots\). Natural logarithms are used. The theorem does not concern nonuniform coupons, collection of multiple sets, or additional collisions.

## Proof

**Independent discovery stages.** Write \(G_{r,n}\), for \(r=1,\ldots,n\), for independent geometric variables with success probabilities \(r/n\). Upon having exactly \(n-r\) distinct labels, the waiting time for the next new label has this law. Independence follows from disjoint future draws and the memoryless sampling rule. Hence
\[
C_n\overset d=\sum_{r=1}^{n}G_{r,n},\quad
\mathbb EC_n=nH_n,\quad
\operatorname{Var}(C_n)=n^2H_n^{(2)}-nH_n,
\]
where \(H_n=\sum_{r=1}^n1/r\) and \(H_n^{(2)}=\sum_{r=1}^n1/r^2\). This can be realized jointly with \(B_n\) by taking the stage variables from the original drawing process.

**Conditional stochastic order, including the boundary.** For \(2\le t\le n\), exactly \(t-1\) distinct labels have been seen at the first repetition; the future is fresh independent sampling. Therefore
\[
(C_n\mid B_n=t)\overset d=t+\sum_{r=1}^{n-t+1}G_{r,n}.
\]
If \(B_n=n+1\), the first \(n\) draws are all distinct and \(C_n=n\) deterministically. For consecutive values \(t,t+1\) with \(2\le t<n\), couple these conditional laws using one common family of geometric variables. The first conditional cover time minus the second is exactly \(G_{n-t+1,n}-1\ge0\), positive with nonzero probability. In the final comparison \(t=n\), the difference is \(G_{1,n}\ge1\). Thus the conditional cover-time laws decrease strictly in first-order stochastic order. For increasing \(g\), the conditional expectation \(h(t)=\mathbb E[g(C_n)\mid B_n=t]\) is nonincreasing. For an independent copy \(B'_n\),
\[
2\operatorname{Cov}(f(B_n),h(B_n))
=\mathbb E[(f(B_n)-f(B'_n))(h(B_n)-h(B'_n))]\le0.
\]
The tower property transfers this to the stated covariance of \(f(B_n)\) and \(g(C_n)\); identity functions give strict negativity. This also implies negative quadrant dependence of the two stopping times.

**Exact covariance without conditioning on the full path.** Let \(I_j\) indicate that the first \(j\) draws were all distinct. On the joint discovery-stage construction,
\[
I_j=\prod_{r=n-j+1}^{n-1}{\bf1}_{\{G_{r,n}=1\}},\qquad
B_n=2+\sum_{j=2}^{n}I_j,\qquad
\mathbb EI_j=\frac{(n)_{\underline j}}{n^j}.
\]
If \(n-j+1\le r\le n-1\), then \(I_jG_{r,n}=I_j\), and therefore
\[
\operatorname{Cov}(I_j,G_{r,n})
=\mathbb EI_j\left(1-\frac nr\right).
\]
All other stage variables are independent of \(I_j\). Sum these covariances first over \(r\) and then over \(j\), setting \(k=n-r\), to obtain the exact displayed negative double sum. Every inner summand is positive, proving the sign independently of the stochastic-order argument.

**Rayleigh limit and covariance scale.** Put \(s_{n,j}=(n)_{\underline j}/n^j\) for \(0\le j\le n\). Since
\[
\Pr(B_n>j)=s_{n,j},\qquad
s_{n,j}=\prod_{k=0}^{j-1}\left(1-\frac{k}{n}\right)
\le \exp\left(-\frac{j(j-1)}{2n}\right),
\]
for every fixed \(x\ge0\), \(s_{n,\lfloor x\sqrt n\rfloor}\to e^{-x^2/2}\). The exponential tail bound gives convergence of the first two scaled moments, hence
\[
\frac{\operatorname{Var}(B_n)}n\longrightarrow
\operatorname{Var}(R)=\frac{4-\pi}{2}.
\]
For \(j/\sqrt n\to x\) the inner sum in the covariance equals
\[
\sum_{k=1}^{j-1}\frac{k}{n-k}\longrightarrow\frac{x^2}{2}.
\]
For \(j\le n/2\), this sum is at most \(j^2/n\), and the displayed exponential bound dominates the resulting Riemann sums. For \(j>n/2\), the sum is at most \(nH_n\) while \(s_{n,j}\le e^{-n/8+O(1)}\); the entire upper tail is \(o(\sqrt n)\). Therefore
\[
\frac{\operatorname{Cov}(B_n,C_n)}{\sqrt n}
\longrightarrow-\int_0^\infty\frac{x^2}{2}e^{-x^2/2}\,dx
=-\sqrt{\frac\pi8}.
\]
Since \(\operatorname{Var}(C_n)/n^2\to\pi^2/6\), division by the standard deviations gives the Pearson-correlation limit.

**Asymptotic independence despite residual covariance.** The standard full-coverage Gumbel limit can be derived directly from
\[
\Pr(C_n\le m)=\sum_{j=0}^n(-1)^j\binom nj(1-j/n)^m
\]
by taking \(m=\lfloor n\log n+ny\rfloor\) and using truncated inclusion-exclusion (Bonferroni bounds) to pass to the limit \(\exp(-e^{-y})\). To prove joint convergence, sample a birthday time \(B_n\) independently of a fresh family \(\{G_{r,n}\}\). Conditional on \(B_n=t\le n\), set \(\widetilde C_n=t+\sum_{r=1}^{n-t+1}G_{r,n}\), and for \(B_n=n+1\) set \(\widetilde C_n=n\). This has exactly the original joint distribution with \(B_n\). The complete-stage sum \(C_n^*=\sum_{r=1}^nG_{r,n}\), however, is independent of \(B_n\). On \(B_n=t\le n\),
\[
\widetilde C_n-C_n^*=t-\sum_{r=n-t+2}^nG_{r,n}.
\]
For any fixed \(K\), on \(B_n\le K\sqrt n\) its absolute value is bounded by \(K\sqrt n\) plus a sum of at most \(K\sqrt n\) geometric variables with means uniformly bounded for large \(n\). Dividing by \(n\) makes this vanish in probability. The complement is arbitrarily rare as \(K\to\infty\), by Rayleigh tightness; the exceptional all-distinct event has probability \(n!/n^n\to0\). Therefore \((\widetilde C_n-C_n^*)/n\to0\) in probability, proving the independent Rayleigh–Gumbel joint limit by Slutsky's theorem.

## Verification

The standalone standard-library script `verify.py` checks two algebraically distinct exact covariance evaluations for each \(2\le n\le119\), exhaustive enumeration of all \(n^{n+1}\) prefixes for \(2\le n\le6\) followed by the Markov expected-cover recursion for unfinished prefixes, exact conditional-mean monotonicity for \(2\le n\le100\), and numerical diagnostics of the derived asymptotic coefficient. It passed **5,430 finite assertions**. Its exhaustive prefix enumeration is finite and does not replace the all-size analytic argument. The script may be run with `python3 verify.py` and requires no third-party libraries.

## Relationship to prior work

Classical birthday and coupon collection laws, including geometric discovery-stage decompositions and Gumbel limits, are established background. Flajolet–Gardy–Thimonier provide a general framework for separate birthday and coupon collection waiting times; their inspected birthday and coupon sections give marginal formulas. Pósfai's coupon-collector thesis develops the independent geometric stages and marginal limit theory. Myers–Wilf focus on other coupon-collector variants, and Inoue–Aki study generalized birthday and collection waiting times. The present target is the **joint law** of the first *repetition* and the first *full collection*: its conditional negative regression, exact mixed covariance, independent joint weak limit, and sharp nonzero residual covariance scale. These are not conclusions of the marginal formulas alone. Broader combinatorial formula systems may give an implicit route to the identity; an inaccessible relevant full text remains a priority risk.

## Limitations

The order and constants rely on equal coupon probabilities. No nonuniform extension, optimal bound, or universal dependence claim is made. The 1987 technical report was inspected in its relevant sections, but an original exact day of public distribution was not established. A relevant 2008 paper was accessible in abstract but not in full text, so historical-priority assessment is qualified. The mathematical proof is self-contained; the finite verifier is corroboration only, and no independent validation is claimed.

## References

1. Anna Pósfai, *Approximation Theorems Related to the Coupon Collector's Problem*, arXiv:1006.3531v1, posted 17 June 2010. https://arxiv.org/abs/1006.3531
2. Philippe Flajolet, Danièle Gardy and Loÿs Thimonier, *Birthday Paradox, Coupon Collectors, Caching Algorithms and Self-Organizing Search*, INRIA Research Report RR-0720 (1987); later in *Discrete Applied Mathematics* 39 (1992), 207–229. https://inria.hal.science/inria-00075832
3. Amy N. Myers and Herbert S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229v1, 16 April 2003. https://arxiv.org/abs/math/0304229
4. Kiyoshi Inoue and Sigeo Aki, *Methods for Studying Generalized Birthday and Coupon Collection Problems*, *Communications in Statistics – Simulation and Computation* 37 (2008), 844–862. https://doi.org/10.1080/03610910801943669
5. Lars Holst, *On Birthday, Collectors', Occupancy and Other Classical Urn Problems*, *International Statistical Review* 54 (1986), 15–27. https://doi.org/10.2307/1403255
