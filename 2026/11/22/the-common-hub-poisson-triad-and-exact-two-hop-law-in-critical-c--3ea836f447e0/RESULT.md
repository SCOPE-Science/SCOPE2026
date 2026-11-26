# The common-hub Poisson triad and exact two-hop law in critical capped-Pareto graphs

## Finding

For the critical capped-Pareto random graph described below, the degrees of **two fixed tagged vertices and their number of common neighbors** converge jointly, conditional on their positive finite weights, to a three-component Poisson construction. This yields an exact conditional probability that two typical vertices lie at graph distance two, rather than just a bound on their distance.

For weights \(w,v\ge1\), define
\[
\mu_w=\frac{\lambda w^\alpha}{1-\alpha},\quad
\mu_v=\frac{\lambda v^\alpha}{1-\alpha},\quad
\gamma_{w,v}=\frac{\lambda}{1-\alpha}\left[m^\alpha-\frac{\alpha}{2-\alpha}mM^{\alpha-1}\right],
\]
where \(m=\min(w,v)\) and \(M=\max(w,v)\). Let \(U,V,C\) be independent Poisson variables of respective means \(\mu_w-\gamma_{w,v}\), \(\mu_v-\gamma_{w,v}\), and \(\gamma_{w,v}\). Then, for the two tagged degrees \(D_n(1),D_n(2)\) and their codegree \(C_n=|N_n(1)\cap N_n(2)|\),
\[
(D_n(1),D_n(2),C_n)\ \Longrightarrow\ (U+C,V+C,C)
\]
under the regular conditional law given \(W_1=w,W_2=v\). In particular,
\[
\lim_{n\to\infty}\Pr\bigl(\mathrm{dist}_{G_n}(1,2)=2\mid W_1=w,W_2=v\bigr)
=1-\exp(-\gamma_{w,v}).
\]
At equal tagged weights \(w=v\), the fraction of each limiting expected degree contributed by common neighbors is the **weight-independent** ratio
\[
\frac{\gamma_{w,w}}{\mu_w}=\frac{2(1-\alpha)}{2-\alpha}.
\]
The limiting degrees have strictly positive conditional dependence: their joint zero probability divided by the product of the two marginal zero probabilities equals \(\exp(\gamma_{w,v})>1\). Nevertheless, for independent unconditioned Pareto tagged weights and the limiting degree pair \((D_1,D_2)\), the simultaneous high-degree tail obeys
\[
\lim_{x\to\infty}x^2\Pr(D_1>x,D_2>x)
=\left(\frac{\lambda}{1-\alpha}\right)^2.
\]
The tail statement uses only the conditional Poisson marginals of the limiting law and independence of the tagged weights; it does not require conditional independence of the degrees. The graph-size limit is taken before the degree-threshold limit.

## Assumptions and scope

Choose any \(0<\alpha<1\), \(\lambda>0\), and positive deterministic \(\varepsilon_n\) such that \(n\varepsilon_n^\alpha\to\lambda\). Let \(W_1,\ldots,W_n\) be independent Pareto random variables with
\(\Pr(W_i>x)=x^{-\alpha}\) for \(x\ge1\). Given all the weights, place distinct undirected edges independently with probabilities
\[
p_{ij}=\min(\varepsilon_n W_iW_j,1),\qquad i\ne j.
\]
Self-edges are absent. The joint limit is for any fixed two distinct labels, or for two uniformly sampled distinct labels by exchangeability. Conditioning on exact values of continuous weights means using the regular conditional distribution defined by the above construction. All fixed-weight assertions require \(w,v\in[1,\infty)\) independent of \(n\); there is no uniform claim for tagged weights growing with \(n\).

Graph distance is the ordinary undirected distance, infinity when vertices are disconnected. Codegree counts common distinct neighbors, excluding the tagged endpoints. The unconditioned high-degree tail refers only to the limiting vector, not a simultaneous \(n,x\) limit.

## Proof

**1. Exact finite-neighbor mark representation.** Fix \(W_1=w,W_2=v\). For each external vertex \(j\ge3\), classify its two incident edges as marks \(00,10,01,11\). Averaging over its Pareto weight and its two independent edge coins, different external vertices produce independent identically distributed marks. Write \(g_a(z)=\min(az,1)\) and
\[
A_a(\varepsilon)=\mathbb E[g_a(\varepsilon W)],\qquad
B_{w,v}(\varepsilon)=\mathbb E[g_w(\varepsilon W)g_v(\varepsilon W)].
\]
The exact mark probabilities are \(B_{w,v}\), \(A_w-B_{w,v}\), \(A_v-B_{w,v}\), and \(1-A_w-A_v+B_{w,v}\), respectively. Their counts over \(n-2\) vertices are multinomial. The direct edge between vertices \(1\) and \(2\), independent of these marks, has probability \(\min(\varepsilon_nwv,1)\to0\).

**2. Evaluated intensities.** For small enough \(\varepsilon\) that \(\varepsilon\max(w,v)<1\), direct integration of the Pareto density gives
\[
A_a(\varepsilon)=\frac{a^\alpha\varepsilon^\alpha-\alpha a\varepsilon}{1-\alpha}.
\]
For \(m=\min(w,v)\), \(M=\max(w,v)\), and \(\varepsilon M<1\), substituting \(z=\varepsilon W\), splitting the integral at \(1/M\) and \(1/m\), and integrating yields the **exact** formula
\[
B_{w,v}(\varepsilon)
=\frac{\varepsilon^\alpha}{1-\alpha}
\left[m^\alpha-\frac{\alpha mM^{\alpha-1}}{2-\alpha}\right]
-\frac{\alpha}{2-\alpha}wv\varepsilon^2.
\]
The three contributing intervals are \((\varepsilon,1/M)\), \((1/M,1/m)\), and \((1/m,\infty)\). The omission of the interval \((0,\varepsilon)\) contributes exactly the last \(\varepsilon^2\) term. Consequently
\(nA_w\to\mu_w\), \(nA_v\to\mu_v\), and \(nB_{w,v}\to\gamma_{w,v}\).
The intensities are nonnegative because the three mark categories are probabilities; alternatively the integral below gives \(0<\gamma_{w,v}\le\min(\mu_w,\mu_v)\).

**3. Joint Poisson limit.** The probability generating function of the three nonzero mark counts, at arguments \(s,t,u\in[0,1]\), is
\[
\bigl[1+(A_w-B_{w,v})(s-1)+(A_v-B_{w,v})(t-1)+B_{w,v}(u-1)\bigr]^{n-2}.
\]
Its limit is the product of Poisson generating functions of intensities \(\mu_w-\gamma_{w,v}\), \(\mu_v-\gamma_{w,v}\), \(\gamma_{w,v}\). Convergence of their joint distribution follows; adding the direct-edge indicator to both degrees changes the vector with probability tending to zero. The \(11\) count is exactly \(C_n\). The limiting bivariate degree generating function is
\[
\exp\{\mu_w(s-1)+\mu_v(t-1)+\gamma_{w,v}(s-1)(t-1)\}.
\]
For equal weights, evaluating the coefficient gives \(\gamma_{w,w}=2\lambda w^\alpha/(2-\alpha)\), hence the constant common-neighbor fraction.

**4. Distance and dependence.** Distance two between the tagged vertices occurs if and only if a common external neighbor exists and their direct edge is absent. In the limit the direct edge vanishes, while the codegree becomes \(\operatorname{Pois}(\gamma_{w,v})\). Thus the two-hop probability tends to \(1-e^{-\gamma_{w,v}}\). Without conditioning on the weights, bounded convergence gives the exactly specified integral
\[
\lim_{n\to\infty}\Pr(\mathrm{dist}(1,2)=2)
=\mathbb E_{W_1,W_2}[1-e^{-\gamma_{W_1,W_2}}].
\]
The two limiting marginal zero probabilities are \(e^{-\mu_w}\) and \(e^{-\mu_v}\); their joint zero probability is \(e^{-\mu_w-\mu_v+\gamma_{w,v}}\), showing strict conditional positive dependence.

**5. Joint high-degree tail.** Under unconditioned tags, each \(\mu_i=\lambda W_i^\alpha/(1-\alpha)\) has an exact Pareto tail \(\Pr(\mu_i>y)=c/y\) for \(y\ge c\), where \(c=\lambda/(1-\alpha)\). The two means are independent. Conditional on both weights, each marginal limiting degree is Poisson of its own mean, regardless of their dependence. For any \(\delta\in(0,1)\), standard elementary exponential-moment bounds for a Poisson variable imply that the probability of exceeding \(x\) when its mean is at most \((1-\delta)x\), or falling below \(x\) when its mean is at least \((1+\delta)x\), is at most \(e^{-c_\delta x}\) for some \(c_\delta>0\). Hence
\[
\frac{c^2}{(1+\delta)^2}
\le\liminf_{x\to\infty}x^2\Pr(D_1>x,D_2>x)
\le\limsup_{x\to\infty}x^2\Pr(D_1>x,D_2>x)
\le\frac{c^2}{(1-\delta)^2}.
\]
Letting \(\delta\downarrow0\) proves the stated tail constant. This does not assert finite covariance of the unconditioned degree pair: the marginal limiting mean is infinite.

## Verification

Run `python3 check.py`. The standalone standard-library checker verifies the exact three-region Pareto integration independently from the closed overlap formula for rational test parameters, all multinomial mark probabilities, the finite joint-zero expression, intensity limits, strict shared-neighbor positivity, symmetry, and the example \(\alpha=1/2\), \(\lambda=1\), \((w,v)=(1,4)\), whose exact intensities are \((2,4,5/3)\). The checker reports 225 passed assertions. The analytic proofs above, not finite numerical examples or a test count, establish the all-parameter claims.

## Relationship to prior work

Andreis, Avena, Hazra and Matteini [1] establish single-tag degree limits (Theorem 1), an extreme-weight point process (Theorem 3), extreme-degree results (Theorem 6), and distance at most three with high probability for two typical vertices in the largest component (Proposition 1.4). Their Remark 2.5 identifies common hubs as a source of isolation dependence. For the same model, [4] uses the extreme-weight point process and Poisson marking for a single root to study clustering. The independent Poisson decomposition of the neighbor counts here is a two-tag extension of that marking mechanism; general Poisson marking and the common-hub mechanism are not new. The extra calculation evaluates the shared-neighbor intensity for the capped kernel, gives the finite-neighbor overlap probability including its lower-cutoff correction, and thus specifies the probability of distance exactly two rather than a high-probability distance bound.

Avena, Garlaschelli, Hazra and Lalli [2] use the **soft exponential** kernel. They give an explicit limiting bivariate degree generating function in (4.19), building on the conditional calculation (4.18), and conjecture joint tail factorization in (2.8). The capped-kernel result above proves the corresponding tail factorization in the critical capped model, with its own marginal tail constant. It is not an assertion about the soft model. The two kernels give different shared-neighbor intensities.

## Limitations

The comparisons above concern the stated results and their relevant proofs; they do not certify historical priority. No claim is made for the soft exponential kernel, the boundary cases \(\alpha=0,1\), growing tagged weights, joint shortest paths of length three, or simultaneous graph-size and tail thresholds.

## References

1. L. Andreis, L. Avena, R. S. Hazra, E. Matteini, *Inhomogeneous random graphs: how heavy tails reshape connectivity* (public preprint 2026-10-21), https://arxiv.org/abs/2610.29564.
2. L. Avena, D. Garlaschelli, R. S. Hazra, M. Lalli, *Inhomogeneous random graphs with infinite-mean fitness variables* (public preprint 2022-12-16), https://arxiv.org/abs/2212.08462; Journal of Applied Probability, DOI 10.1017/jpr.2025.10037.
3. K. Lin, G. Reinert, *Joint vertex degrees in the inhomogeneous random graph model* (2016), https://arxiv.org/abs/0912.4812.
4. [*An exact full-clustering atom for hard-saturated infinite-mean random graphs*](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-an-exact-full-clustering-atom-for-hard-saturated-infinite-mean-r--0f1726f44dd0/RESULT.md) (2026), Proof §§1, 3–4.
