# Exact past–future dependence of independent-sample record maxima

## Finding
Let \(X_1,X_2,\ldots\) be independent, identically distributed real observations with a continuous, nondegenerate distribution function. Let \(M_j=\max_{1\le i\le j}X_i\). For integers \(1\le n<m\) let \(\mathcal F_n=\sigma(M_1,\ldots,M_n)\) and \(\mathcal G_m=\sigma(M_m,M_{m+1},\ldots)\). Set \(r=n/m\).

Write \(\beta(\mathcal A,\mathcal B)\) for the total-variation distance between the joint law of generators of two countably generated sigma fields and the product of their marginal laws; equivalently, the absolute-regularity coefficient with normalization \(\sup_E|P(E)-Q(E)|\). Write \(\phi(\mathcal A,\mathcal B)=\sup_{A\in\mathcal A,P(A)>0,B\in\mathcal B}|P(B\mid A)-P(B)|\).

The exact past–future coefficient is
\[
\boxed{\displaystyle \beta(\mathcal F_n,\mathcal G_m)=r+\frac{r(1-r)}{1+r}(1-r)^{1/r}.}
\]
For every such pair, \(\phi(\mathcal F_n,\mathcal G_m)=1\). Moreover, the relative entropy of the joint past–future distribution with respect to its independent product is infinite. These three assertions hold for **every continuous parent distribution**, with no density or moment assumption.

Consequently, if \(r\to0\) along integer pairs, then
\[
\beta(\mathcal F_n,\mathcal G_m)\sim (1+e^{-1})\frac nm.
\]
In particular, for each fixed \(n\) the absolute-regularity coefficient vanishes as \(m\to\infty\), while for any fixed lag \(k\ge1\), \(\sup_{n\ge1}\beta(\mathcal F_n,\mathcal G_{n+k})=1\). Thus vanishing average dependence requires separation large relative to the age of the record process; in contrast, the uniform conditional-probability coefficient never decreases.

## Assumptions and scope
The index set is \(\{1,2,\ldots\}\). The observations are i.i.d. and their common cumulative distribution function is continuous, but it may fail to have a density or be strictly increasing on the whole real line. The joint and product measures are on the standard Borel product path spaces with the natural generators \((M_1,\ldots,M_n)\) and \((M_m,M_{m+1},\ldots)\). Total variation uses \(\mathrm{TV}(P,Q)=\sup_E|P(E)-Q(E)|\), not twice this number. Relative entropy is \(D(P\Vert Q)\), allowing \(+\infty\). Statements concern a nonstationary record-maximum process, not the stationary chains obtained by iterating a fixed Marshall–Olkin copula.

## Proof
**1. Distribution-free bivariate copula.** Let \(F\) be the continuous parent CDF. Probability-integral transformation gives i.i.d. uniforms \(F(X_i)\). As far as all maximum statistics are concerned, monotone quantile inversion is almost surely lossless. Put \(U=F(M_n)^n\) and \(V=F(M_m)^m\); each is uniform on \([0,1]\). The direct joint distribution is
\[
 P(M_n\le x,M_m\le y)=
 \begin{cases}F(x)^nF(y)^{m-n},&x\le y,\\F(y)^m,&x>y.\end{cases}
\]
In the uniform coordinates this gives
\[
 C_r(u,v)=\min\{u v^{1-r},\,v\},\quad 0\le u,v\le1.
\]
The curve \(u=v^r\) represents the event that no new record is established between the two times. By exchangeability of the location of the largest observation among the first \(m\), this curve carries probability \(r=n/m\). On the open region \(0<u<v^r<1\), the absolutely continuous part has density \(c_r(u,v)=(1-r)v^{-r}\); on \(u>v^r\) it has zero density. Thus the only remaining probability is the stated singular mass.

**2. Exact total variation.** Under the independent uniform benchmark \(Q\), the joint density is one and the singular curve is null. The overlap formula for two probability laws, including a possible singular part, is
\[
 1-\mathrm{TV}(P,Q)=\int_0^1\!\int_0^1\min(c_r(u,v),1)\,du\,dv.
\]
Integrating horizontally gives the one-dimensional integrand \(\min\{v^r,1-r\}\). With \(a=(1-r)^{1/r}\), split at \(a\) and integrate exactly:
\[
 \int_0^1\min\{v^r,1-r\}\,dv
 =\frac{a^{1+r}}{1+r}+(1-r)(1-a)
 =1-r-\frac{r(1-r)}{1+r}a.
\]
Subtracting from one proves the formula for \(\mathrm{TV}(\mathcal L(M_n,M_m),\mathcal L(M_n)\otimes\mathcal L(M_m))\). The optimal measurable event in uniform coordinates is the union of the singular curve and \(\{u<v^r,\ v<a\}\), up to negligible boundaries. Its probability difference against independence achieves the formula, so this is an exact value, not merely an upper bound.

**3. Full sigma fields do not increase total variation.** Conditional on \(M_n\), the future observations after \(n\) are independent of the entire preceding maximum history; in particular the conditional law of \(M_m\) depends on that history only through \(M_n\). Conditional on \(M_m\), the maximum process after \(m\) is independent of all preceding observations. Hence the joint law of the full past vector and infinite future vector is obtained from the law of \((M_n,M_m)\) by attaching two conditional Markov kernels: one generating the earlier maximum history given \(M_n\), and one generating the later maximum process given \(M_m\). The product of the marginal past and future laws is obtained from the independent product of the endpoint marginals using **the same two kernels**. Applying a common Markov kernel cannot increase total variation, proving an upper bound by the endpoint total variation. Conversely, projection of full histories to \((M_n,M_m)\) cannot increase total variation, giving the reverse bound. This proves the claimed equality for \(\beta(\mathcal F_n,\mathcal G_m)\).

**4. Uniform mixing and information obstruction.** Choose thresholds \(t\) with \(0<F(t)<1\) and put \(A_t=\{M_n>t\}\) and \(B_t=\{M_m>t\}\). Then \(A_t\subseteq B_t\), so \(P(B_t\mid A_t)=1\), whereas \(P(B_t)=1-F(t)^m\to0\) as \(F(t)\uparrow1\). Therefore \(\phi=1\). Independently, \(P(M_n=M_m)=r>0\), while two independently sampled continuous maximum variables have equality probability zero. The endpoint joint law is therefore not absolutely continuous with respect to its product law, which forces its Kullback–Leibler divergence to be infinite. The same remains true for the full path laws under projection.

**5. Scaling and boundaries.** As \(r\downarrow0\), \((1-r)^{1/r}\to e^{-1}\), yielding the sharp relative-lag constant \(1+e^{-1}\). As \(r\uparrow1\), the formula tends to one. For fixed \(k\), \(n/(n+k)\uparrow1\) as \(n\to\infty\), which gives the asserted supremum. For \(n<m\) the exact value lies strictly between \(r\) and one.

## Verification
A standalone standard-library checker in `checker.py` independently verifies the exact optimization identity at reciprocal ratios using rational arithmetic, the exact singular mass by exhaustive rank-permutation counting for sample sizes up to eight, numerical quadrature of the overlap integral, and seeded independent-law versus joint-law experiments for representative ratios. It also checks the claimed bounds and small-ratio behavior. Execute `python checker.py` from the directory containing this file. Finite checks are diagnostic and do not replace the sigma-field or asymptotic proofs above.

## Relationship to prior work
Košir, Lazić, and Omladič provide stochastic representations and structural classifications of Marshall–Olkin and related copulas, including the minimum-of-two expression used here in a boundary parameter regime. Their work does not calculate past–future absolute regularity for an evolving record process. Longla establishes mixing criteria for **stationary** chains generated by copulas; his Marshall–Olkin example assumes both mixing parameters strictly below their excluded boundary. In the family \(\min\{u v^{1-r},v\}\), one parameter is at that boundary, and the process also has changing margins. Consequently neither his stationary mixing theorem nor its rate assertion applies.

The subsequently posted work of Baz and Pellerey gives two-time dependence descriptions of discrete maximum processes. Its copula for i.i.d. maxima covers the bivariate copula intermediate step above; that step is not claimed as new. The contribution assessed here is the exact total-variation optimum, the reduction to **complete past and infinite future sigma fields**, and the resulting sharp separation between absolute regularity, uniform mixing, and information divergence. This identification depends on explicit further analysis and is subject to the historical-priority limitations below.

## Limitations
The parent distribution must be continuous; atoms introduce ties and destroy the stated universal singular-mass/coplanar decomposition. The normalized process is nonstationary, so no stationary sequence mixing theorem is asserted. The value of \(\beta\) uses one standard normalization; an alternative coefficient convention can differ by a factor of two. The conclusions do not imply a central limit theorem or a time-series estimator. Historical literature may contain equivalent total-variation computations under other names; novelty is a best-knowledge assessment rather than an independent priority certification.

## References
1. T. Košir, P. Lazić, M. Omladič, *Marshall–Olkin copulas revisited*, arXiv:2512.12265v1, first publicly posted 2025-12-13. https://arxiv.org/abs/2512.12265
2. M. Longla, *On mixtures of copulas and mixing coefficients*, arXiv:1310.8241, first publicly posted 2013-10-30. https://arxiv.org/abs/1310.8241
3. B. K. Beare, *Copulas and temporal dependence*, Econometrica 78 (2010), 395–410. https://www.jstor.org/stable/25621357
4. J. Baz and F. Pellerey, *Dependence properties between marginals of discrete-time maximum processes*, arXiv:2611.22599, first publicly posted 2026-11-17. https://arxiv.org/abs/2611.22599
