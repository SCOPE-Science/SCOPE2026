# A Chernoff location law for the busiest cut in a random chord diagram

## Finding

For each integer \(n\ge2\), choose a perfect matching uniformly from all pairings of the ordered endpoints \(1,\ldots,2n\). Let \(H_{n,k}\), for \(0\le k\le2n\), be the number of matching edges with exactly one endpoint in \(\{1,\ldots,k\}\). Define \(K_n\) to be the *smallest* index at which \(H_{n,k}\) attains its maximum, and set \(H_n^*=H_{n,K_n}\). Let \(B\) be standard two-sided Brownian motion with \(B(0)=0\) and independent standard-Brownian restrictions on positive and negative time.

**Joint cut-location and excess-height theorem.** As \(n\to\infty\),
\[
\left(\frac{K_n-n}{n^{2/3}},\frac{H_n^*-H_{n,n}}{n^{1/3}}\right)
\ \Longrightarrow\
\left(\mathop{\rm argmax}_{t\in\mathbb R}\{B(t)-t^2/2\},
\ \sup_{t\in\mathbb R}\{B(t)-t^2/2\}\right).
\]
The argmax on the right is almost surely unique. If \(Z\) denotes the conventional Chernoff random variable \(\arg\max_s\{B(s)-s^2\}\), the first coordinate equals \(2^{2/3}Z\) in distribution. The second coordinate is nondegenerate and strictly positive almost surely. The theorem describes the index of the busiest cut in *the given endpoint order*, not the graph-theoretic cutwidth optimized over vertex orders.

## Assumptions and scope

The sampling law is uniform over the \((2n-1)!!\) perfect matchings on a **fixed labeled linear order**. No independence assumption is imposed between different cut counts. The endpoint index \(k\) is integer-valued; the leftmost maximizer convention removes finite-sample ties. The centering for the height is the *random central cut count* \(H_{n,n}\), not its deterministic mean. Convergence is joint weak convergence in \(\mathbb R^2\); the theorem does not claim finite-sample Chernoff laws or rates of convergence.

## Proof

**1. Exact exposure dynamics and deterministic peak.** Drop the first subscript temporarily and put \(M=2n\). Scan the sites from left to right, revealing only which already scanned endpoints are mutually paired and which remain unpaired, without revealing identities of future partners. Conditional on the exposed information at time \(k\), exactly \(H_k\) of the \(M-k\) sites still unseen are partners of the open endpoints. Uniform matching symmetry therefore yields
\[
\Pr(H_{k+1}=H_k-1\mid\mathcal F_k)=\frac{H_k}{M-k},\qquad
\Pr(H_{k+1}=H_k+1\mid\mathcal F_k)=1-\frac{H_k}{M-k}.
\]
In particular, with \(m_k=\mathbb E H_k\),
\[
m_k=\frac{k(M-k)}{M-1},\qquad
m_{n+h}-m_n=-\frac{h^2}{M-1}.
\]
The first identity follows by summing crossing-edge indicators, since each prescribed edge belongs to a uniform matching with probability \(1/(M-1)\). The second is exact, for every integer \(-n\le h\le n\). This parabolic profile supplies the deterministic restoring force.

**2. Centered martingale innovations and a local variance bound.** Let \(Y_k=H_k-m_k\), and define
\[
\xi_{k+1}=H_{k+1}-\mathbb E(H_{k+1}\mid\mathcal F_k).
\]
Then \(\mathbb E(\xi_{k+1}\mid\mathcal F_k)=0\), \(|\xi_{k+1}|\le2\), and
\[
Y_{k+1}=\left(1-\frac2{M-k}\right)Y_k+\xi_{k+1},\qquad
\mathbb E(\xi_{k+1}^2\mid\mathcal F_k)=4p_k(1-p_k),
\quad p_k=\frac{H_k}{M-k}.
\]
Direct counting of one and two prescribed matching edges gives
\[
\operatorname{Var}(H_k)=
\frac{2k(k-1)(M-k)(M-k-1)}{(M-3)(M-1)^2}
\quad (M\ge4).
\]
Consequently \(Y_n=O_{\Pr}(\sqrt n)\), and in fact \(\sup_{|h|\le Tn^{2/3}}|Y_{n+h}|=O_{\Pr}(\sqrt n)\) for every fixed \(T\). To verify the latter, for positive increments use the product
\[
q_r=\prod_{j=n}^{n+r-1}\left(1-\frac2{M-j}\right)
=\frac{(n-r)(n-r-1)}{n(n-1)}
\]
for \(0\le r\le n/2\), and observe that \(Y_{n+r}/q_r\) is a martingale with bounded increments and \(q_r\) bounded away from zero in that range for all sufficiently large \(n\). Doob's inequality bounds its squared maximum by \(C(n+r)\). Reversal symmetry of the uniform matching gives the corresponding negative-time bound. In particular, uniformly for \(|h|\le Tn^{2/3}\),
\[
\frac1{n^{1/3}}\left|
(Y_{n+h}-Y_n)-\sum_{j=n}^{n+h-1}\xi_{j+1}
\right|\xrightarrow{\Pr}0
\]
when \(h\ge0\); for \(h<0\), interpret the sum by the signed reverse-sum convention. Indeed, the discrepancy is a sum of \(2Y_j/(M-j)\), whose absolute value is bounded by \(C Tn^{-1/3}\sup_{|h|\le Tn^{2/3}}|Y_{n+h}|=O_{\Pr}(n^{1/6})\), hence negligible after division by \(n^{1/3}\).

**3. The local two-sided Brownian limit.** Uniformly on every window \(|k-n|\le Tn^{2/3}\), the previous maximal estimate and the formula for \(m_k\) imply \(H_k/n\to1/2\) in probability and \((M-k)/n\to1\). Thus
\[
\max_{|k-n|\le Tn^{2/3}}
\left|\mathbb E(\xi_{k+1}^2\mid\mathcal F_k)-1\right|
\xrightarrow{\Pr}0.
\]
The martingale difference array has jumps bounded by two, so its Lindeberg condition is automatic on the \(n^{1/3}\) scale. The predictable quadratic variation over \(\lfloor t n^{2/3}\rfloor\) consecutive steps, after division by \(n^{2/3}\), tends to elapsed time \(t\). The martingale functional central limit theorem, applied over the entire interval \([n-Tn^{2/3},n+Tn^{2/3}]\) and anchored by subtracting its value at index \(n\), consequently gives a standard two-sided Brownian motion; increments on opposite sides of the origin are independent in the Gaussian limit.

Together with step 2 and the exact parabola of step 1, this proves, for every fixed \(T>0\), the polygonally interpolated process convergence in \(C([-T,T])\):
\[
\left(\frac{H_{n,n+\lfloor t n^{2/3}\rfloor}-H_{n,n}}{n^{1/3}}\right)_{-T\le t\le T}
\ \Longrightarrow\
(B(t)-t^2/2)_{-T\le t\le T}.
\]
Flooring and endpoint interpolation errors are at most two matching-edge units after centering and therefore vanish under normalization.

**4. Global localization of every maximizer.** Local process convergence alone is not enough to justify taking an unrestricted argmax. We establish the needed tightness. Let \(R\le n/2\). The martingale product in step 2, together with \(\mathbb E Y_n^2=O(n)\) and Doob's inequality, gives the quantitative bound
\[
\mathbb E\max_{0\le r\le R}|Y_{n+r}-Y_n|^2
\le C\left(R+\frac{R^2}{n}\right).
\]
The same bound holds for \(Y_{n-r}-Y_n\) by reversal of endpoint order. For any dyadic annulus \(R\le |h|\le2R\) contained in \(|h|\le n/2\), the exact mean loss is at least \(R^2/(2n-1)\). Thus Chebyshev's inequality gives
\[
\Pr\left(\max_{R\le|h|\le2R} H_{n,n+h}\ge H_{n,n}\right)
\le C\left(\frac{n^2}{R^3}+\frac n{R^2}\right).
\]
Summing geometric annuli with \(R\ge Tn^{2/3}\) shows that the probability of a maximizer in \(Tn^{2/3}\le|h|\le n/2\) is at most \(C T^{-3}+o(1)\).

For the remaining cuts \(|h|>n/2\), the deterministic gap \(m_n-m_{n+h}\) is at least order \(n\). Expose the random pairing sequentially, choosing one partner at each step. Switching two possible partners affects at most two matching edges and changes any one \(H_k\) by at most two. The associated Doob martingale has \(n\) increments bounded in absolute value by a universal constant. Azuma–Hoeffding and a union bound over the \(2n+1\) cuts therefore give \(\max_k|Y_k|=o_{\Pr}(n)\). This rules out \(|h|>n/2\), with probability tending to one. Combining the regions,
\[
\lim_{T\to\infty}\limsup_{n\to\infty}
\Pr(|K_n-n|>Tn^{2/3})=0.
\]

**5. Argmax and supremum mapping.** Almost surely \(B(t)-t^2/2\to-\infty\) as \(|t|\to\infty\), and it has a unique global maximizer (the classical Chernoff property). On any compact interval containing that maximizer, the supremum functional is continuous and the leftmost-argmax functional is continuous at such a unique-maximizer path. Apply the joint continuous mapping theorem to step 3, then remove the compact cutoff using step 4. This proves the joint assertion. Finally, Brownian scaling with \(t=2^{2/3}s\) identifies the location as \(2^{2/3}Z\). Since two-sided Brownian motion almost surely makes positive excursions in every right neighborhood of zero, the limiting excess height is almost surely strictly positive.

## Verification

The standalone standard-library Python program `verify.py` enumerates all \((2n-1)!!\) matchings for \(n=2,3,4,5,6\), up to 10,395 matchings on twelve endpoints. It reconstructs each cut-count path and checks the exact means, variances, one-step conditional transition law, and parity of the path. The program passed 195 exact-rational assertions. Run `python verify.py` with Python 3 and no additional packages. The martingale limit and localization arguments, rather than enumeration or simulation, establish the infinite-size theorem.

## Relationship to prior work

Acan, *On a uniformly random chord diagram and its intersection graph* (arXiv:1501.01489v1, publicly posted 7 January 2015), studies chord intersections, single-chord degrees, graph cores and chord-by-chord growth. The paper establishes the uniform chord-diagram framework but does not analyze where the ordered endpoint-scan cut profile attains its maximum.

*Exact crossing-cut Green kernel and Gaussian bridge for uniform pairings* (published published-finding corpus research record of 18 October 2026) proves the exact mean/covariance, the Markov exposure recursion, and a global \(\sqrt n\)-scale Gaussian bridge for the centered cut profile. Those are **prior ingredients, not new results here**. A global functional central limit theorem alone does not determine the finer \(n^{2/3}\) maximum location and \(n^{1/3}\) excess height: these require a local martingale invariance principle plus a global localization estimate.

Groeneboom, Lalley and Temme, *Chernoff's distribution and differential equations of parabolic and Airy type* (arXiv:1305.6053, first posted 26 May 2013), establish the law and almost-sure uniqueness of the Brownian-minus-parabola maximizer. The classical maximum-of-a-drifting-walk and cube-root asymptotic frameworks of Daniels–Skyrme and Kim–Pollard provide a broad methodological precedent, not a model-specific analysis of uniform matching cuts. The claim here is the matching-specific scaling and joint limit with its exact normalizations, not the existence of the classical Chernoff distribution itself.

## Limitations

The statement is limited to uniform perfect matchings in the specified order. It is not about the minimum cutwidth over all endpoint permutations. It gives weak convergence but no explicit finite-size rate or moment convergence for the maximum excess. The generic literature on maxima of stochastic processes with concave mean paths is extensive; an earlier equivalent specialized matching-cut application cannot be ruled out solely by the searches described in the accompanying review. All provided code tests are finite, while the argument for the limiting law is analytic.

## References

1. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1 (2015-01-07). https://arxiv.org/abs/1501.01489
2. P. Groeneboom, S. Lalley and N. Temme, *Chernoff's distribution and differential equations of parabolic and Airy type*, arXiv:1305.6053v1 (2013-05-26), later version inspected. https://arxiv.org/abs/1305.6053
3. H. E. Daniels and T. H. R. Skyrme, *The maximum of a random walk whose mean path has a maximum*, Adv. Appl. Probab. 17 (1985), 85–99. https://doi.org/10.2307/1427054
4. J. Kim and D. Pollard, *Cube root asymptotics*, Ann. Statist. 18 (1990), 191–219. https://doi.org/10.1214/aos/1176347498
5. *Exact crossing-cut Green kernel and Gaussian bridge for uniform pairings*, published published-finding corpus research record (2026-10-18). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-crossing-cut-green-kernel-and-gaussian-bridge-for-uniform--1361e88632a1
