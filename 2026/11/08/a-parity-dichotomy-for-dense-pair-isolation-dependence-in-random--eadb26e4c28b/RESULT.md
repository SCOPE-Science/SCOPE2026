# A parity dichotomy for dense pair-isolation dependence in random even graphs

## Finding

Let \(G\) be the independent-edge random graph \(G(n,p)\), conditioned on the event \(\mathcal E_n\) that every vertex has even degree. Let \(I_v\) be the indicator that vertex \(v\) is isolated in the conditioned graph, and let \(v\ne w\). For every integer \(n\ge3\), the conditional covariance \(\operatorname{Cov}(I_v,I_w\mid\mathcal E_n)\) is strictly positive at \(p=1/2\). In the dense limit, its sign has a complete parity dichotomy: it is strictly **negative** for all \(p\) sufficiently close to one when \(n\ge4\) is even, and strictly **positive** there when \(n\ge3\) is odd. Thus every even graph order has at least one sign reversal in \((1/2,1)\), although the underlying edges are independent before conditioning. This holds for every even order, not only a fixed small graph.
Without degree-parity conditioning, the same two isolation indicators satisfy \(\operatorname{Cov}_{G(n,p)}(I_v,I_w)=p(1-p)^{2n-3}>0\) for every \(0<p<1\); hence the dense negative dependence is specifically induced by the global parity constraint.

The two endpoints are explicit:
\[
\operatorname{Cov}(I_v,I_w\mid\mathcal E_n)\big|_{p=1/2}=2^{4-2n}>0\qquad(n\ge3),
\]
\[
\operatorname{Cov}(I_v,I_w\mid\mathcal E_n)
\sim-\frac{(1-p)^{n-2}}{((n-1)!!)^{2}}\quad(p\uparrow1),\qquad n\ge4\ \text{even}.
\]
For odd \(n\ge3\), the corresponding fixed-order dense asymptotic has the opposite sign:
\[
\operatorname{Cov}(I_v,I_w\mid\mathcal E_n)\sim (1-p)^{2n-3}\quad(p\uparrow1),\qquad n\text{ odd}.
\]
For the smallest even order, \(n=4\), the full exact formula is
\[
\operatorname{Cov}(I_v,I_w\mid\mathcal E_4)
=\frac{p^3(1-p)^2(2-3p)}{(6p^2-4p+1)^2},
\]
so its unique sign crossing is \(p=2/3\). For general even \(n\ge6\), uniqueness of the crossing is **not** asserted.

## Assumptions and scope

Take an integer \(n\ge3\), \(0<p<1\), and distinct labeled vertices \(v,w\) of the complete graph on \(n\) vertices. Every edge is initially present with probability \(p\) independently. Write \(q=1-p\). Condition on \(\mathcal E_n=\{\deg_G(u)\text{ even for all vertices }u\}\); the conditioning probability is strictly positive for \(0<p<1\), as the empty graph belongs to \(\mathcal E_n\). The indicator \(I_v\) is one precisely when \(\deg_G(v)=0\). The covariance and all probabilities here refer to this conditioning unless a displayed probability explicitly mentions the underlying independent-edge graph. Odd \(n\) are covered by the positive dense-limit law, not by a claim of sign reversal.

Define \(P_m(p)=\Pr(G(m,p)\text{ has every degree even})\) for \(m\ge1\) and \(P_0(p)=1\). With \(x=1-2p\),
\[
P_m(p)=2^{-m}\sum_{k=0}^{m}\binom{m}{k}x^{k(m-k)}\qquad(m\ge1).
\]
The convention \((n-1)!!=1\cdot3\cdots(n-1)\) applies when \(n\) is even.

## Proof

**Parity partition function.** For any fixed graph \(H\), the even-degree indicator equals \(2^{-m}\sum_{\sigma\in\{-1,1\}^m}\prod_u\sigma_u^{\deg_H(u)}\). Taking expectation edge by edge under \(G(m,p)\) gives \(2^{-m}\sum_{\sigma}\prod_{i<j}(q+p\sigma_i\sigma_j)\). If exactly \(k\) signs are negative, there are \(k(m-k)\) unequal-sign pairs, each supplying the factor \(q-p=x\); equal-sign pairs supply one. This proves the formula for \(P_m\).

**Joint isolation calculation.** Under the independent-edge law, making a specified vertex isolated deletes \(n-1\) edges, after which the other \(n-1\) vertices must form an even graph. For two distinct vertices, the total number of incident edges to delete is \(2n-3\). Therefore,
\[
\Pr(I_v=1\mid\mathcal E_n)=\frac{q^{n-1}P_{n-1}(p)}{P_n(p)},\qquad
\Pr(I_v=I_w=1\mid\mathcal E_n)=\frac{q^{2n-3}P_{n-2}(p)}{P_n(p)}.
\]
Subtracting the square of the first probability yields the exact identity
\[
\operatorname{Cov}(I_v,I_w\mid\mathcal E_n)=
\frac{q^{2n-3}}{P_n(p)^2}\left(P_{n-2}(p)P_n(p)-qP_{n-1}(p)^2\right).
\tag{1}
\]
This is an identity for all \(n\ge3\); the sign-change result below concerns even \(n\).

**Uniform even graphs.** At \(p=1/2\), the parity sum has only the two all-equal sign patterns nonzero, so \(P_m(1/2)=2^{1-m}\) for all \(m\ge1\). For \(n\ge3\), substitution in (1) gives exactly \(2^{4-2n}>0\).

**Dense limit for even order.** Suppose \(n\ge4\) is even and let \(q\downarrow0\). The complement of a graph of even degree has every degree odd because \(n-1\) is odd. Any graph on even \(n\) vertices with all degrees odd has at least \(n/2\) edges; equality holds precisely for a perfect matching, of which there are \((n-1)!!\). Consequently,
\[
P_n(p)\sim(n-1)!!\,q^{n/2},\qquad
P_{n-2}(p)\sim(n-3)!!\,q^{(n-2)/2}.
\]
For \(n-1\) odd, the complete graph has every degree even, hence \(P_{n-1}(p)\to1\). Thus
\[
\Pr(I_v=1\mid\mathcal E_n)\sim\frac{q^{n/2-1}}{(n-1)!!},
\qquad
\Pr(I_v=I_w=1\mid\mathcal E_n)\sim\frac{q^{2n-4}}{n-1}.
\]
Since \(2n-4>n-2\) for \(n\ge4\), the joint-isolation probability is negligible compared with the square of the individual probability, proving the stated strictly negative covariance asymptotic. Its sign is negative in an interval next to one. Continuity of (1), together with its positive value at one half, proves existence of at least one zero and a sign reversal in \((1/2,1)\) for every even \(n\ge4\).

**Dense limit for odd order.** Now suppose \(n\ge3\) is odd. Its complete graph has even degree \(n-1\), so \(P_n(p)\to1\) and \(P_{n-2}(p)\to1\) as \(p\uparrow1\). The complement of a graph of even degree on \(n-1\) (an even number of) vertices has every degree odd, hence \(P_{n-1}(p)\sim(n-2)!!\,q^{(n-1)/2}\). Consequently the pair-isolation probability is asymptotic to \(q^{2n-3}\), whereas the product of one-point probabilities has order \(q^{3n-3}\). Therefore \(\operatorname{Cov}(I_v,I_w\mid\mathcal E_n)\sim q^{2n-3}>0\), establishing the other half of the parity dichotomy.

**Sharp four-vertex boundary.** For \(n=4\), the even graphs consist of the empty graph, four labeled triangles each with one isolated vertex, and three labeled four-cycles. Their unconditional probability is \(P_4(p)=(1-p)^2(6p^2-4p+1)\). Direct substitution in (1) simplifies to the displayed rational formula. Its denominator is strictly positive because \(6p^2-4p+1=6(p-1/3)^2+1/3\), while the remaining factors have positive sign except \(2-3p\). Hence the unique zero occurs at \(p=2/3\), with strict positivity below and strict negativity above it.

## Verification

Run `python3 verify_even_isolation.py` using Python's standard library. The checker calculates the finite parity sum and the two isolation probabilities using exact rational arithmetic. It independently enumerates every simple labeled graph on \(3\) through \(6\) vertices, filters for even degree, and compares weighted isolation covariances at seven rational edge probabilities. It also checks the \(p=1/2\) identity through \(n=18\), the four-vertex rational identity at 99 rational probabilities, example negative dense values for even \(n\le22\), and positive dense values with asymptotic-ratio comparisons for odd \(n\le23\). These finite tests cross-check arithmetic but do **not** prove the assertions for every \(n\). The infinite-order assertions are established by the parity and complement arguments above.

## Relationship to prior work

The random-even-graph model and its Ising/random-cluster representation are established by Grimmett and Janson (2007/2009). Their later study of random graphs with forbidden vertex degrees (2007/2010) includes an explicit classification of the even graphs on four vertices in Example 5.4 and analyzes sparse degree-conditioned graphs. Therefore the underlying four-vertex enumeration is known and is **not** claimed as a new census. The distinctive assertion here is the complete odd/even fixed-order dense-limit sign dichotomy, the entire unbounded family of even-order conditional pair-isolation reversals, and their endpoint covariance scales. The general parity projection is also classical. We found no explicit statement of this conditional pair-isolation sign theorem in the cited primary texts; implicit or earlier coverage remains possible.

## Limitations

The theorem guarantees at least one crossing for each even \(n\ge4\), not exactly one for all orders; a uniqueness statement is currently unproved here. For odd \(n\), positivity is established at \(p=1/2\) and near one, not necessarily for all \(0<p<1\). No claim is made about multivariate positive/negative association or a universal sign outside the proven neighborhoods. The dense asymptotic holds for each **fixed** even \(n\) as \(p\uparrow1\); it is not a uniform two-parameter asymptotic as \(n\to\infty\). Historical originality is conditional on the inspected literature, not a certification of priority.

## References

1. Geoffrey Grimmett and Svante Janson, *Random even graphs*, arXiv:0709.3039 (first submitted September 19, 2007), *Electronic Journal of Combinatorics* 16 (2009), R46. https://arxiv.org/abs/0709.3039 . DOI: 10.37236/135.
2. Geoffrey Grimmett and Svante Janson, *Random graphs with forbidden vertex degrees*, arXiv:0712.0270 (first submitted December 3, 2007), *Random Structures & Algorithms* 37 (2010), 137–175. https://arxiv.org/abs/0712.0270 . DOI: 10.1002/rsa.20307.
