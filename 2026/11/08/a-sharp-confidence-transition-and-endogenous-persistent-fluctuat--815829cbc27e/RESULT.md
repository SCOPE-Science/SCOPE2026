# A sharp confidence transition and endogenous persistent fluctuations in neighborhood Deffuant–Weisbuch stars

## Finding

**Theorem (sharp three-agent threshold and frozen binary stars).** Consider the pure neighborhood Deffuant–Weisbuch (NDW) opinion model on a fixed finite unweighted undirected graph. Each discrete time step selects one edge uniformly and independently; endpoints simultaneously make their directed confidence decisions using pre-interaction opinions. Each receptive endpoint moves a fraction \(\rho\in(0,1/2]\) toward the selected neighbor. A directed confidence distance compares the endpoint's opinion with the *mean opinion of its selected neighbor's neighbors*, and receptiveness requires that distance be strictly less than \(\varepsilon>0\).

**(a) Three-vertex path.** Put opinions \(x_L(0)=0\), \(x_R(0)=1\), and \(x_C(0)=z\in[0,1]\) on the leaves and center of the path \(L-C-R\). For \(0<\varepsilon\le1/2\), both leaves stay fixed for all times, and the center has the exact recursion
\[
H_{t+1}=(1-\rho)H_t+\rho B_t,\qquad
\Pr(B_t=0)=\Pr(B_t=1)=\tfrac12,
\]
with independent inputs. Its distributions converge to the unique stationary law of \(\rho\sum_{j=0}^{\infty}(1-\rho)^jB_j\), whereas almost surely
\[
\liminf_{t\to\infty}H_t=0,\qquad \limsup_{t\to\infty}H_t=1.
\]
In particular, when \(\rho=1/2\), the limiting law is uniform on \([0,1]\), even though almost-sure convergence fails.

For \(\varepsilon>1/2\), every edge interaction is a two-sided compromise and all three opinions converge almost surely to their preserved mean \((1+z)/3\). If \(V_t\) is their sum of squared deviations from that mean, then
\[
\mathbb E[V_{t+1}\mid X_t]\le(1-\rho(1-\rho))V_t.
\]
Thus the confidence boundary is sharp, including equality in the nonconvergent regime.

**(b) Binary stars.** Let the graph be \(K_{1,m}\), where \(m\ge2\), the center starts from any \(z\in[0,1]\), and exactly \(k\in\{1,\ldots,m-1\}\) leaves start at opinion \(1\) and the other leaves at \(0\). Write \(p=k/m\). If \(0<\varepsilon\le\min\{p,1-p\}\), every leaf remains fixed forever, and the center evolves as
\[
H_{t+1}=(1-\rho)H_t+\rho B_t,\qquad B_t\overset{\mathrm{iid}}\sim\operatorname{Bernoulli}(p).
\]
Its unique stationary law \(\mu_{\rho,p}\) has
\[
\mathbb E_{\mu}[H]=p,\qquad
\operatorname{Var}_{\mu}(H)=\frac{\rho p(1-p)}{2-\rho},
\]
and the finite-time quantities are
\[
\mathbb E[H_t]=p+(1-\rho)^t(z-p),\qquad
\operatorname{Var}(H_t)=\frac{\rho p(1-p)}{2-\rho}\bigl[1-(1-\rho)^{2t}\bigr].
\]
There is distributional convergence to \(\mu_{\rho,p}\) at Wasserstein-1 distance at most \((1-\rho)^t\), but no almost-sure convergence: the pathwise liminf and limsup are \(0\) and \(1\). At \(\rho=1/2\), \(\mu_{\rho,p}\) is the binary digit measure with iid \(\operatorname{Bernoulli}(p)\) digits. It is Lebesgue-uniform if and only if \(p=1/2\); for \(p\ne1/2\) it is singular with Hausdorff dimension
\[
\dim_{\mathrm H}(\mu_{1/2,p})=\frac{-p\log p-(1-p)\log(1-p)}{\log2}.
\]
Here dimension of a probability measure means the infimum of the Hausdorff dimensions of its full-measure Borel sets.

Among connected graphs, two vertices cannot exhibit these persistent fluctuations in the pure NDW model; the path on three vertices is the minimal witness.

## Assumptions and scope

The graph is static (no rewiring), all node and edge weights are one, and only one edge is sampled per time step. For a vertex \(i\) and selected neighbor \(j\), its directed confidence distance is
\[
d_{\mathrm{NBC}}(i,j)=\left|x_i-\frac{1}{\deg(j)}\sum_{v\sim j}x_v\right|.
\]
The selected endpoints use the same old-state opinions to compute both directed confidence indicators; an endpoint that is not receptive does not move. The mixing parameter is exactly \(\sigma=0\) in Eq. (3) of Krishnagopal and Porter, arXiv:2402.05368v2. The one-edge rule is an allowed sampling choice in that model, corresponding to \(f=1\). These claims do not concern the adaptive rewiring model, arbitrary intermediate \(\sigma\), or general graphs beyond the stated cases.

## Proof

**Directed thresholds and invariant stars.** Each leaf \(j\) of a star has unique neighbor the center \(C\), so the center sees the average of the neighbors of \(j\), which is exactly its own opinion: \(d_{\mathrm{NBC}}(C,j)=0\). Thus the center always updates. A leaf at opinion \(b\in\{0,1\}\) sees the average of the center's neighbor opinions, namely \(p\), whence \(d_{\mathrm{NBC}}(j,C)=|b-p|\in\{p,1-p\}\). Under \(\varepsilon\le\min\{p,1-p\}\), the strict confidence condition fails for every leaf. Induction freezes every leaf and leaves each random edge selection an independent Bernoulli input for the center. The P3 low-confidence regime is the special case \(m=2,p=1/2\).

**Stationarity, moments, and sample paths.** Put \(q=1-\rho\in[1/2,1)\). Iterating gives
\[
H_t=q^tz+\rho\sum_{j=0}^{t-1}q^{t-1-j}B_j.
\]
The input sum has the same distribution as the first \(t\) terms of \(\rho\sum_{j\ge0}q^jB_j\), whose infinite series converges absolutely. The update map contracts pairs of trajectories driven by the same inputs by \(q\), proving uniqueness of its invariant law and Wasserstein-1 convergence with bound \(q^t\) (couple two initial values in \([0,1]\)). Taking expectations and variances of the independent inputs proves the stated formulas.

For every integer \(M\), infinitely many pairwise-disjoint length-\(M\) input blocks are all zero, and infinitely many are all one, almost surely, by independence and the second Borel–Cantelli lemma. On a zero block the end opinion is at most \(q^M\) because all opinions remain in \([0,1]\); on a one block it is at least \(1-q^M\). Intersect over \(M\in\mathbb N\) to obtain the pathwise liminf and limsup, hence nonconvergence.

**Exact law at half compromise.** With \(\rho=q=1/2\), the stationary series is \(\sum_{j\ge0}2^{-j-1}B_j\). Every dyadic cylinder interval determined by \(a\) digits equal to one and \(b\) digits equal to zero has mass \(p^a(1-p)^b\), up to a null set of dyadic-boundary ambiguities. For \(p=1/2\), its mass equals its length, so the distribution is Lebesgue-uniform. For \(p\ne1/2\), its typical digit frequency is \(p\), whereas Lebesgue-almost every number has digit frequency \(1/2\); the measures are mutually singular. By the strong law, the local exponent of a typical depth-\(n\) dyadic cylinder is \(h(p)/\log2\). Standard cylinder covering and the mass-distribution argument give the same upper and lower Hausdorff dimension of the full-measure typical-digit set, proving the exact dimension stated. This last dimension step is a classical Bernoulli-product fact, not presented as an independent new theorem.

**High-confidence P3 consensus.** Suppose \(\varepsilon>1/2\). Initially the center lies between the two leaf opinions. At every edge selection both endpoints update: the center sees distance zero, while each selected leaf sees half the current leaf-to-leaf distance, bounded by \(1/2\) as long as the order is maintained. A simultaneous convex compromise at weight \(\rho\le1/2\) preserves the order \(x_L\le x_C\le x_R\); no opinion leaves the current opinion interval, so its width cannot increase. Thus the two-sided update condition holds inductively forever. The mean \(\bar x=(1+z)/3\) is conserved. A two-sided update on an edge with difference \(d\) reduces \(V=\sum(x_i-\bar x)^2\) by exactly \(2\rho(1-\rho)d^2\). Uniform selection of the two edges yields
\[
\mathbb E[V_{t+1}\mid X_t]=V_t-\rho(1-\rho)\left[(x_L-x_C)^2+(x_C-x_R)^2\right].
\]
The edge-square sum exceeds or equals \(V_t\), since their difference is \((x_L+x_R-2x_C)^2/3\). Hence \(\mathbb EV_t\le[1-\rho(1-\rho)]^tV_0\). Markov's inequality and summability give \(V_t\to0\) almost surely, hence consensus at the conserved mean. At equality \(\varepsilon=1/2\), the leaf distances are exactly the threshold, so the low-confidence proof applies instead.

**Minimality.** On the connected two-node graph, every neighbor's only neighbor is the updating vertex itself, so both directed neighborhood-confidence distances are zero. Every update reduces the opinion difference by \(1-2\rho\in[0,1)\), yielding deterministic consensus for any positive threshold. Thus P3 is minimal.

## Verification

Execute `python verify.py` using Python's standard library. The checker reconstructs each asymmetric directed step directly from the defining rule, checks exact-rational frozen-star invariance, the high-confidence conditional variance identity and contraction, finite dyadic distributions and moments, and biased Bernoulli moment recurrences. It reports 7,057 successful exact checks. The infinite statements follow from the mathematical proof; no bounded enumeration is used as an infinity certificate.

## Relationship to prior work

Krishnagopal and Porter, arXiv:2402.05368 (first public v1 on 2024-02-08; consulted revised v2, Section III.1), introduce NDW directed confidence based on the neighbor's mean and investigate many regimes by simulations. The present theorem resolves a specific exact three-agent threshold and a binary-star family analytically; it is not a claim about the paper's rewiring outcomes. Acemoglu, Como, Fagnani and Ozdaglar, arXiv:1009.2653 (2010), already establish persistent fluctuations from *exogenously stubborn* agents and describe stationary laws in that setting. The affine perpetuity after leaf freezing, and its Bernoulli digit structure, are consequently not asserted to be new in isolation; the NDW mechanism here makes the leaves **endogenously** unreceptive under an exact sharp confidence bound, while selecting consensus on the opposite side. Chu and Porter, arXiv:2409.15148, study randomized interaction times in different bounded-confidence dynamics and do not supply this fixed-graph pure-neighborhood threshold. This literature comparison does not amount to a comprehensive priority guarantee.

## Limitations

All topology and sample-path claims concern fixed stars with the stated binary leaf configurations; the high-confidence consensus classification is proved for P3, not for larger stars or arbitrary graphs. The dimension formula uses classical iid Bernoulli coding. At low confidence the law approaches stationarity but the center does not converge on almost every realized sample path. Numerical checks supplement, but do not replace, exact proofs. Possible unindexed or inaccessible equivalent source results remain a scientific-priority risk. No independent external audit has occurred.

## References

1. S. Krishnagopal and M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Neighborhood Effects*, arXiv:2402.05368v1 (2024-02-08) and v2 (2025-05-22), https://arxiv.org/html/2402.05368v2 . Especially corrected Eq. (3), Section III.1.
2. D. Acemoglu, G. Como, F. Fagnani and A. Ozdaglar, *Opinion fluctuations and disagreement in social networks*, arXiv:1009.2653 (2010), https://arxiv.org/abs/1009.2653 .
3. Y. Chu and M. A. Porter, *Bounded-confidence opinion models with random-time interactions*, arXiv:2409.15148 (2024), https://arxiv.org/html/2409.15148v1 .
