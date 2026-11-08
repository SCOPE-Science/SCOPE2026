# Logarithmic sign transition for completion-time covariance with terminal coupon multiplicities

## Finding
For a uniform coupon collector on \(n\ge2\) types, let \(T_n\) be the number of draws needed to see every type, and \(C_{n,r}\) the number of types that occur **exactly** \(r\ge1\) times among the first \(T_n\) draws. Write \(H_n=\sum_{j=1}^{n}j^{-1}\). Define \(Y_n=\sum_{k=2}^{n}Z_k\) for independent exponential random variables \(Z_k\) of rate \(k\), and \(\mu_{n,r}=\mathbb E[Y_n^r]\).

For every \(n\ge2\) and integer \(r\ge1\),
\[
\operatorname{Cov}(T_n,C_{n,r})=\frac{n}{r!}\bigl(\mu_{n,r+1}-H_n\mu_{n,r}\bigr).
\]
The ratios \(R_{n,r}=\mu_{n,r+1}/\mu_{n,r}\) increase strictly in \(r\), start below \(H_n\), and eventually exceed it. Consequently the covariance sequence is negative at low multiplicities and positive at high multiplicities, with a **single transition** and at most one zero at the transition. For example, for \(n=2\), the covariance at \(r=2\) equals zero. Define \(r_+(n)=\min\{r\ge1:\operatorname{Cov}(T_n,C_{n,r})>0\}\). Then
\[
\lim_{n\to\infty}\frac{r_+(n)}{\log n}=1.
\]
More precisely, for integer sequences \(r_n/\log n\to\alpha\in(0,2)\),
\[
\frac{\mu_{n,r_n+1}}{\mu_{n,r_n}}-H_n\longrightarrow -\psi(2-\alpha)-\gamma,
\]
where \(\psi\) denotes the logarithmic derivative of the gamma function, and \(\gamma\) Euler's constant. The right side is negative for \(\alpha<1\) and positive for \(\alpha>1\).

## Assumptions and scope
The draws are independent and each of the \(n\) types has probability \(1/n\); counting stops on the **first** complete collection. An exactly \(r\)-fold occurrence means \(r\) visits in the stopped sample, including the terminal draw. The exponential variable \(Y_n\) is auxiliary and is not the collection time; its rates are \(2,3,\ldots,n\), not probability parameters. The theorem concerns covariance, not an assertion of independence, stochastic order, or a central-limit theorem.

## Proof
**1. Poissonization with correct time scale.** Equip each type with its own independent rate-one Poisson process. Their superposition is a rate-\(n\) Poisson process with iid uniform labels. Let \(\tau\) be the first instant at which every process has at least one arrival. Conditional on the label sequence, its inter-event times are independent exponentials of mean \(1/n\), so \(\mathbb E[\tau\mid\text{labels}]=T_n/n\) and, for any terminal label statistic \(C\), \(\operatorname{Cov}(T_n,C)=n\operatorname{Cov}(\tau,C)\). Also \(\mathbb E\tau=H_n\).

**2. Mark one type.** Let \(A_i\) be its first arrival time and \(M_i=\max_{j\ne i}A_j\). If \(A_i>M_i\), type \(i\) is the last first arrival and contributes exactly one occurrence at \(\tau=A_i\). Each of the \(n\) types is last with probability \(1/n\), and conditional on being last, \(\tau\) has its unconditional maximum-of-\(n\)-exponentials distribution and mean \(H_n\). This gives aggregate contributions \(\mathbf1_{\{r=1\}}\) and \(H_n\mathbf1_{\{r=1\}}\) to the expectations of \(C_{n,r}\) and \(\tau C_{n,r}\).

On \(A_i<M_i\), the terminal time is \(M_i\), independent of the Poisson process of type \(i\). The probability that type \(i\) has exactly \(r\ge1\) arrivals before \(M_i=t\) is \(e^{-t}t^r/r!\); this event already guarantees \(A_i<t\). Therefore
\[
\begin{aligned}
\mathbb E C_{n,r}&=\mathbf1_{\{r=1\}}+\frac{n}{r!}\mathbb E[e^{-M_i}M_i^r],\\
\mathbb E[\tau C_{n,r}]&=H_n\mathbf1_{\{r=1\}}+\frac{n}{r!}\mathbb E[e^{-M_i}M_i^{r+1}].
\end{aligned}
\]
The density of \(M_i\) is \((n-1)e^{-t}(1-e^{-t})^{n-2}\), \(t>0\). Thus the exponentially tilted density \(n e^{-t}\,d\Pr(M_i\le t)\) is \(n(n-1)e^{-2t}(1-e^{-t})^{n-2}\,dt\), a probability density. This is exactly the law of \(Y_n\), since \(e^{-Y_n}\) has the \(\operatorname{Beta}(2,n-1)\) law: both have transform
\[
\mathbb E[e^{-sY_n}]=\prod_{k=2}^n\frac{k}{k+s}
=\frac{\Gamma(n+1)\Gamma(s+2)}{\Gamma(n+1+s)},\quad s>-2.
\]
Consequently \(\mathbb E C_{n,r}=\mathbf1_{\{r=1\}}+\mu_{n,r}/r!\) and \(\mathbb E[\tau C_{n,r}]=H_n\mathbf1_{\{r=1\}}+\mu_{n,r+1}/r!\). Subtracting \(H_n\mathbb E C_{n,r}\), then multiplying by \(n\), proves the exact covariance identity.

**3. Exactly one sign transition.** The distribution of \(Y_n\) is nondegenerate, positive, and unbounded. Strict Cauchy–Schwarz gives \(\mu_{n,r+1}^2<\mu_{n,r}\mu_{n,r+2}\), hence strict increase of \(R_{n,r}\). The first ratio is
\[
R_{n,1}=H_n-1+\frac{\sum_{k=2}^n k^{-2}}{\sum_{k=2}^n k^{-1}}<H_n.
\]
Unbounded support forces \(R_{n,r}\to\infty\): otherwise moment growth would be bounded geometrically, contradicting \(\Pr(Y_n>b)>0\) for arbitrarily large \(b\). The covariance sign equals the sign of \(R_{n,r}-H_n\), proving the finite-size classification.

**4. Position of the transition.** Put \(L_n=\log n\) and \(W_n=Y_n-L_n\). For every fixed \(t<2\),
\[
\mathbb E[e^{tW_n}]=n^{-t}\frac{\Gamma(n+1)\Gamma(2-t)}{\Gamma(n+1-t)}\longrightarrow\Gamma(2-t),
\]
with uniformly bounded exponential moments on compact subintervals of \(( -\infty,2)\). Thus \(W_n\) converges in distribution to \(W=-\log G\), where \(G\) is gamma distributed with shape two and unit rate. For \(r_n/L_n\to\alpha\in(0,2)\), the weight \((Y_n/L_n)^{r_n}=(1+W_n/L_n)^{r_n}\) converges to \(e^{\alpha W}\). Its product with \(W_n\) is uniformly integrable: above zero use \(\log(1+x)\le x\) and an exponential moment at a parameter strictly between \(\alpha\) and two; below zero the weight is at most one and negative exponential moments bound \(|W_n|\). Hence
\[
\frac{\mu_{n,r_n+1}}{\mu_{n,r_n}}-L_n
=\frac{\mathbb E[W_n(Y_n/L_n)^{r_n}]}{\mathbb E[(Y_n/L_n)^{r_n}]}
\longrightarrow \frac{\mathbb E[We^{\alpha W}]}{\mathbb E[e^{\alpha W}]}
=-\psi(2-\alpha).
\]
Finally \(H_n-\log n\to\gamma\). Since \(\psi\) is strictly increasing and \(\psi(1)=-\gamma\), the limiting sign crosses zero only at \(\alpha=1\). Compare \(r=\lfloor(1-\varepsilon)\log n\rfloor\) and \(r=\lceil(1+\varepsilon)\log n\rceil\) for any fixed \(0<\varepsilon<1\); finite-size monotonicity sandwiches \(r_+(n)\) between them for large \(n\). This proves the claimed limit.

## Verification
The accompanying standalone \(\texttt{verify_coupon.py}\) uses exact rational arithmetic to compare the moment formula with an independent, finite-state stopped-occupancy recursion. It checks all \(2\le n\le8\), \(1\le r\le6\), including the mixed moment, and verifies strict moment-ratio growth for \(2\le n\le32\), \(1\le r\le12\). It reports 457 exact assertions passed. These finite checks are corroboration, not an infinite proof; the proof above is analytic.

## Relationship to prior work
Myers and Wilf (2003), section 4, give the full joint law of completion time and the number of singleton coupons; in particular, the specialization \(r=1\) is **already covered in principle** and is not claimed as a novel standalone result. Doumas and Papanicolaou (2014) treat cumulative sibling deficits, corresponding to sums of terminal multiplicity counts, and analyze their expectations. Ilienko (2020) proves infinite-dimensional, coordinatewise (fixed-sibling-index) limit laws for sibling deficits and separately for completion times; these do not yield a mixed growing-index covariance. Long (2026) develops exact Poissonized identities and fixed-sibling-index limit laws, including mixed moments among sibling deficits, but not the covariance against the discrete completion time across multiplicities growing on the logarithmic scale. The new assessed claim is the complete sign profile and its logarithmic threshold, not the classical mean completion time or the known singleton distribution.

## Limitations
Only the equal-probability model and stopping at first coverage are treated. The theorem does not classify correlations (which require variance normalization), nonuniform coupon weights, higher mixed cumulants, or the exact constant-order offset of \(r_+(n)\) around \(\log n\). General multivariate terminal occupancy generating functions in older literature could imply portions of the exact moment identity; priority over all historical sources is not independently certified.

## References
- A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229 (first posted 2003-04-16), especially section 4, https://arxiv.org/html/math/0304229v1.
- A. V. Doumas and V. G. Papanicolaou, *The Siblings of the Coupon Collector*, arXiv:1412.4346 (first posted 2014-12-14), https://arxiv.org/abs/1412.4346.
- A. Ilienko, *Limit theorems in the extended coupon collector's problem*, arXiv:2002.00650 (2020), https://arxiv.org/abs/2002.00650.
- C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, arXiv:2606.29635 (2026), https://arxiv.org/abs/2606.29635.
