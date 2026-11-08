# Strict balancing and polynomial decay of realized EF1 for shared Bernoulli lottery goods

## Finding

**Theorem.** Fix integers \(n\ge 2\), \(m\ge1\), and a parameter \(0<p<1\). Before any values are revealed, divide \(m\) indivisible goods among \(n\) labeled agents. Each good independently realizes a common value in \(\{0,1\}\), equal to one with probability \(p\); all agents value a given good *identically after realization*. Utilities are additive. For a fixed deterministic allocation \(A\), let \(\mathcal P(A)\) be the probability that \(A\) satisfies envy-freeness up to one good (EF1) after realization.

Then \(\mathcal P(A)\) is maximized **if and only if** its bundle cardinalities differ by at most one. In particular, the ex-ante EF1 allocations and the maximizers of ex-post EF1 probability are exactly the same allocations. More quantitatively, if a bundle of size \(b\) transfers one good to a bundle of size \(a\) with \(b\ge a+2\), then its EF1 probability increases by at least
\[
(b-a-1)p^2(1-p)^{m-2}>0.
\]

Write \(m=nq+r\), \(q=\lfloor m/n\rfloor\), \(0\le r<n\), and put
\[
\beta_s(t)=\begin{cases}\binom{s}{t}p^t(1-p)^{s-t},&0\le t\le s,\\0,&\text{otherwise}.\end{cases}
\]
The optimal probability has the finite expression
\[
\mathcal P^*_{n,m}(p)=\sum_{t\ge0}\left[
\bigl(\beta_q(t)+\beta_q(t+1)\bigr)^{n-r}
\bigl(\beta_{q+1}(t)+\beta_{q+1}(t+1)\bigr)^r
-\beta_q(t+1)^{n-r}\beta_{q+1}(t+1)^r
\right].
\]
For every *fixed* \(n\ge2\) and \(p\in(0,1)\), as \(q\to\infty\) (with any \(0\le r<n\)),
\[
\mathcal P^*_{n,nq+r}(p)\sim
\frac{2^n-1}{\sqrt n}\bigl(2\pi q p(1-p)\bigr)^{-(n-1)/2}.
\]
Thus even the best allocation chosen without knowing the realizations has a polynomially vanishing realized-EF1 probability as the number of goods grows with the number of agents fixed. If \(m\le n\), the optimal probability is instead exactly one.

## Assumptions and scope

For each good \(g\), let \(Z_g\) be a Bernoulli random variable of parameter \(p\). The variables \(Z_g\) are mutually independent across goods, but a given \(Z_g\) is the *same realized value for every agent*, not an independently sampled agent-specific value. For every agent \(i\) and set \(S\) of goods, the realized utility is \(u_i(S)=\sum_{g\in S}Z_g\). All \(m\) goods must be allocated, and the allocation must be fixed before any \(Z_g\) is revealed. No monetary transfers are allowed.

EF1 means: for all agents \(i,j\), either \(u_i(A_i)\ge u_i(A_j)\), or there exists a good \(g\in A_j\) such that \(u_i(A_i)\ge u_i(A_j\setminus\{g\})\). Because realized values are zero or one and common to all agents, if \(X_i=\sum_{g\in A_i}Z_g\), this condition is equivalent to \(\max_i X_i-\min_i X_i\le1\). Under fixed bundle sizes \(k_i=|A_i|\), these \(X_i\) are independent \(\operatorname{Bin}(k_i,p)\) random variables. Under expected values, EF1 is likewise equivalent to \(\max_i k_i-\min_i k_i\le1\), because every good has the common positive expected value \(p\).

The theorem does not allow adaptive reallocation after realization; it does not cover heterogeneous success parameters, cross-good correlation, independently drawn values across agents for the same good, or values outside \(\{0,1\}\). The asymptotic keeps \(n\) and \(p\) fixed.

## Proof

**1. Strict pair smoothing.** For an integer vector \(k=(k_1,\ldots,k_n)\), write \(F(k)=\Pr(\max_i X_i-\min_i X_i\le1)\), where the \(X_i\) are independent binomial variables with parameters \((k_i,p)\). Consider two coordinates with sizes \(a,b\), where \(b\ge a+2\), and leave all other coordinates fixed. Let \(U\sim\operatorname{Bin}(a,p)\), \(V\sim\operatorname{Bin}(b-1,p)\), and \(Z\sim\operatorname{Bernoulli}(p)\), mutually independent and independent of all other counts \(C\). For fixed \(c\), define \(K(x,y,c)\) to be the indicator that the range of the list \((x,y,c)\) is at most one. The difference between the probability after smoothing and before smoothing is
\[
p\,\mathbb E\bigl[K(U+1,V,C)-K(U,V+1,C)\bigr].
\]
Indeed, the two arrangements agree when \(Z=0\); when \(Z=1\), the extra success belongs to the initially smaller or larger bundle, respectively.

Fix \(c\) and let \(f_c(u,v)=K(u+1,v,c)-K(u,v+1,c)\). It is antisymmetric in \((u,v)\). If \(u<v\), then adding one to the smaller coordinate cannot increase the maximum and cannot decrease the minimum, whereas adding one to the larger coordinate cannot decrease the maximum and cannot increase the minimum. Thus \(f_c(u,v)\ge0\) for \(u<v\).

Let \(A_j=\Pr(U=j)\) and \(B_j=\Pr(V=j)\). Since \(b-1>a\), the ratio \(B_j/A_j\) is nondecreasing wherever \(A_j>0\): for \(0\le j<a\), its consecutive ratio is \((b-1-j)/(a-j)>1\). For \(j>a\), \(A_j=0\), so the same monotone-likelihood-ratio comparison extends across the supports. Consequently, \(A_uB_v-A_vB_u\ge0\) whenever \(u<v\). Pairing terms \((u,v)\) and \((v,u)\) in the expectation gives
\[
\mathbb E[f_C(U,V)\mid C=c]
=\sum_{u<v}f_c(u,v)(A_uB_v-A_vB_u)\ge0.
\]
It is strictly positive. Namely, when all other bundle counts are zero, \(f_c(0,1)=1\), and
\[
A_0B_1-A_1B_0=(b-a-1)p(1-p)^{a+b-2}>0.
\]
The probability that all other counts vanish is \((1-p)^{m-a-b}\). Retaining just this nonnegative summand and multiplying by the preceding factor \(p\) yields the claimed strict lower bound \((b-a-1)p^2(1-p)^{m-2}\). This also covers the case \(n=2\), with no other counts.

**2. Global optimum and equality.** Any vector of nonnegative integer bundle sizes summing to \(m\) that is not balanced has two coordinates differing by at least two. A one-unit transfer as above strictly increases \(F\) and decreases the sum of squared bundle sizes. Repeating must reach the unique (up to permutation) vector consisting of \(n-r\) copies of \(q\) and \(r\) copies of \(q+1\). Strictness in every unbalanced step proves both optimality and the full equality classification. Since expected item values are all \(p>0\), that balanced cardinality condition is exactly ex-ante EF1.

**3. Exact probability.** For arbitrary independent integer-valued bundle counts with probability masses \(\gamma_i(t)\), the event that their range is at most one is the union, over \(t\ge0\), of events that every count belongs to \(\{t,t+1\}\). Adjacent events overlap exactly when every count equals their common endpoint \(t+1\); no three such events share an outcome. Inclusion–exclusion therefore gives
\[
\Pr(\text{range}\le1)=\sum_{t\ge0}\left[\prod_i(\gamma_i(t)+\gamma_i(t+1))-\prod_i\gamma_i(t+1)\right].
\]
Insert the \(n-r\) binomial masses with size \(q\) and \(r\) with size \(q+1\) to obtain the displayed formula. If \(m\le n\), each balanced bundle has zero or one good and hence each realized count belongs to \(\{0,1\}\), giving probability one.

**4. Sharp asymptotic.** Put \(\sigma^2=p(1-p)>0\). The local central limit theorem for binomial variables, uniformly for \(t-qp=O(\sqrt q)\), implies that the masses \(\beta_q(t)\) and \(\beta_{q+1}(t)\), as well as their neighboring masses at \(t+1\), have the same leading Gaussian approximation
\[
(2\pi q\sigma^2)^{-1/2}\exp\left(-\frac{(t-qp)^2}{2q\sigma^2}\right).
\]
Binomial concentration makes the complementary tails negligible at order \(q^{-(n-1)/2}\); one can first restrict to a growing central window and then use the uniform local limit there. Substitution into the finite formula leaves the coefficient \(2^n-1\) multiplying the sum of \(n\)-th powers of this Gaussian mass. The corresponding Gaussian Riemann sum is
\[
(2\pi q\sigma^2)^{-n/2}\sqrt{\frac{2\pi q\sigma^2}{n}}
=\frac{(2\pi q\sigma^2)^{-(n-1)/2}}{\sqrt n}.
\]
This proves the asymptotic, uniformly over the finitely many possible residues \(r\).

## Verification

The standalone dependency-free Python script `verify.py` computes exact integer probability numerators, with the common denominator determined by rational \(p\), in three different ways: direct enumeration over realized bundle counts, interval-overlap summation, and complete binary-outcome enumeration. It checks all labeled bundle-size compositions in its finite stated ranges, global optimality and strictness, and the quantitative one-step lower bound. The executed script reports 7,920 formula/count comparisons and optimality tests, 1,458 independent binary-outcome comparisons, and 30,240 one-step inequalities. In particular, for three agents and six goods at \(p=1/2\), balanced bundle sizes \((2,2,2)\) give probability \(23/32\), while \((1,2,3)\) give \(9/16\).

These finite checks do not certify the infinite theorem on their own. The independent arguments in Proof 1–4 establish the universal assertions.

## Relationship to prior work

Igarashi and Oh, *Fair Division of Lotteries* (arXiv:2610.34906v1, first submitted October 26, 2026), study ex-post **envy-freeness**, not EF1, when goods have uncertain values; their Proposition 7.2 handles common realized valuations, while the conclusion explicitly identifies EF1 as a future direction. Their exact-EF balance result neither states nor implies the strict pair-smoothing law for the broader range-at-most-one event, the complete EF1 probability formula, or the EF1 decay constant. The present theorem addresses that specifically motivated gap on the natural iid-binary common-value domain.

Chen and Long, *Randomized Online Fair Division: High-Probability and Expected Realized Fairness* (arXiv:2609.23577v1, September 20, 2026), study random **online allocations** with fixed valuations and adversarial arrivals, a different source of randomness and objective. Halpern, Psomas and Zhang, *Truthful Fair Division under Stochastic Valuations* (arXiv:2602.12359v1, February 12, 2026), focus on strategic mechanisms, welfare, and high-probability exact fairness rather than optimizing the EF1 probability of a fixed allocation under a common realized value per item. Aloisio et al., *Approximately Fair Allocation of Indivisible Items with Random Valuations* (AAMAS 2024), optimize expected maximum envy, rather than this realized-EF1 event. The pairwise likelihood-ratio argument uses standard binomial structure; no claim is made that the underlying stochastic-order tool is new.

## Limitations

Publication priority is provisional: an unindexed probabilistic majorization or stochastic scheduling result could imply this particular finite-event inequality. The inspection was not a universal search of all probability literature. No extension to independent agent-specific realizations, unequal item distributions, arbitrary nonnegative lotteries, or risk-aware allocation policies is proved. The limiting relation requires a fixed positive success probability and fixed population, and no uniform-in-population or rare-event asymptotic is asserted. Independent verification has not been performed.

## References

1. A. Igarashi and Y. Oh, *Fair Division of Lotteries*, arXiv:2610.34906v1 (2026-10-26), https://arxiv.org/abs/2610.34906.
2. T. Chen and J. Long, *Randomized Online Fair Division: High-Probability and Expected Realized Fairness*, arXiv:2609.23577v1 (2026-09-20), https://arxiv.org/abs/2609.23577.
3. D. Halpern, A. Psomas and S. Zhang, *Truthful Fair Division under Stochastic Valuations*, arXiv:2602.12359v1 (2026-02-12), https://arxiv.org/abs/2602.12359.
4. A. Aloisio, V. Bilò, A. M. Caruso, M. Flammini and C. Vinci, *Approximately Fair Allocation of Indivisible Items with Random Valuations*, AAMAS (2024), https://iris.gssi.it/handle/20.500.12571/30247.
