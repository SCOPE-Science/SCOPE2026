# Sharp Nash-welfare gap for proposer-optimal stable marriage

## Finding

Consider a complete strict stable-marriage market with \(n\ge2\) men, \(n\) women and positive rank-induced utilities \(u_a(\mu)=n-r_a(\mu(a))\), where \(r_a\) is the zero-based rank. Let \(\mu_{\mathrm{DA}}\) denote the men-proposing deferred-acceptance outcome and \(\mu_*\) any stable matching maximizing the Nash product \(P(\mu)=\prod_{a\in M\cup W}u_a(\mu)\). Then

\[
1\le \frac{P(\mu_*)}{P(\mu_{\mathrm{DA}})}\le (n-1)^n.
\]

Both bounds are sharp, for every \(n\); in geometric-mean Nash social welfare \(\operatorname{NSW}(\mu)=P(\mu)^{1/(2n)}\), the sharp worst-case optimum-to-DA ratio is \(\sqrt{n-1}\). For \(n=2\), every instance has ratio one. For every \(n\ge3\), equality at the upper bound is equivalent to the following simultaneous conditions for \(\mu_{\mathrm{DA}}\) and some Nash-optimal stable \(\mu_*\): all pairs change; each man ranks his DA partner first and his \(\mu_*\) partner second; each woman ranks her DA partner last and her \(\mu_*\) partner first. At equality the maximizing stable matching is unique. The exact number of labeled strict preference profiles attaining equality is

\[
n!\,!n\,((n-2)!)^{2n},
\]

where \(!n\) is the number of derangements of \(n\) elements. For independent uniformly random preference lists, the extremal probability is \(n!\,!n/[n(n-1)]^{2n}\). At \(n=3\), exactly \(12\) of \(46{,}656\) profiles reach the maximum Nash-product factor \(8\).

## Assumptions and scope

Two distinct labeled sides \(M=\{m_0,\ldots,m_{n-1}\}\) and \(W=\{w_0,\ldots,w_{n-1}\}\), each of cardinality \(n\ge2\), have complete strict rankings of the opposite side. A matching is a bijection. Stability means no unmatched man-woman pair strictly prefer one another to their assigned partners. All utilities are strictly positive integers from \(1\) to \(n\); replacing them by arbitrary cardinal utilities is outside scope. The Nash product includes all \(2n\) participants. All ratios are of positive real numbers. The extremal-count statement concerns labeled profiles, not symmetry classes.

## Proof

**Upper bound.** The classical man-optimality property of men-proposing Gale--Shapley states that no man prefers any stable matching to \(\mu_{\mathrm{DA}}\). Fix another stable matching \(\nu\), and let \(k\) be the number of men with changed partners. Since both matchings are bijections, exactly \(k\) women also change partners. Every switched man strictly loses utility; writing his old utility as \(t\in\{2,\ldots,n\}\), his new utility is at most \(t-1\), hence his utility ratio is at most \((t-1)/t\le(n-1)/n\). Every switched woman has ratio at most \(n\), because every woman's utility lies in \([1,n]\). For an unchanged participant the ratio is one. Multiplying gives

\[
\frac{P(\nu)}{P(\mu_{\mathrm{DA}})}\le\left(\frac{n-1}{n}\right)^k n^k=(n-1)^k\le(n-1)^n.
\]

The first inequality of the finding follows because \(\mu_*\) maximizes \(P\) over stable matchings and \(\mu_{\mathrm{DA}}\) is stable. When \(n=2\), the upper bound equals one, proving universal equality.

**Sharp construction.** For any \(n\ge2\), index both sides modulo \(n\). Each man \(m_i\) ranks \(w_i\) first and \(w_{i+1}\) second, with the others in any strict order. Each woman \(w_j\) ranks \(m_{j-1}\) first and \(m_j\) last, with the others in any strict order. The identity matching \(\mu_0(m_i)=w_i\) is stable because all men get their first choice. It is also the men-proposing deferred-acceptance matching. The cyclic matching \(\mu_1(m_i)=w_{i+1}\) is stable because all women get their first choice. At \(\mu_0\) men get utility \(n\) and women get utility \(1\), so \(P(\mu_0)=n^n\). At \(\mu_1\) men get utility \(n-1\) and women get utility \(n\), so \(P(\mu_1)=n^n(n-1)^n\). The proved upper bound forces \(\mu_1\) to be Nash-optimal. Thus the constant is sharp for all \(n\), with \(\operatorname{NSW}(\mu_1)/\operatorname{NSW}(\mu_0)=\sqrt{n-1}\).

**Characterization of equality for \(n\ge3\).** Since \(n-1>1\), equality in the last bound forces \(k=n\). Equality in the product of positive ratios forces every switched man's ratio to equal \((n-1)/n\): each has utility \(n\) at \(\mu_{\mathrm{DA}}\) and \(n-1\) at \(\mu_*\). Equality also forces every switched woman's ratio to equal \(n\): her utility is \(1\) at \(\mu_{\mathrm{DA}}\) and \(n\) at \(\mu_*\). These are exactly the claimed rank conditions. Conversely those conditions force \(\mu_{\mathrm{DA}}\) stable by everyone's top male choice, \(\mu_*\) stable by everyone's top female choice, and the exact product ratio \((n-1)^n\). Any maximizing stable matching in such a profile must assign every man his unique second-ranked woman; hence it equals \(\mu_*\).

**Exact enumeration.** For \(n\ge3\), choose the DA perfect matching in \(n!\) ways. Choose the disjoint maximizing perfect matching in \(!n\) ways relative to it, because all \(n\) men change partners. Each man has fixed first and second choices; the other \(n-2\) women have \((n-2)!\) orders. Each woman has fixed first and last choices; the remaining \(n-2\) men have \((n-2)!\) orders. This produces exactly \(n!\,!n\,((n-2)!)^{2n}\) labeled profiles. No duplicates arise: in an extremizer, the DA matching is uniquely determined by men's first choices and the unique maximizing matching by men's second choices. The total number of labeled full strict profiles is \((n!)^{2n}\). Division and \(n!=n(n-1)(n-2)!\) give the claimed probability.

## Verification

The self-contained Python 3 standard-library program `VERIFY.py` computes Gale--Shapley independently, tests stability by every blocking pair, enumerates all stable matchings for every labeled \(2\times2\) and \(3\times3\) strict profile, and checks the exact-rational product ratios. It also validates the cyclic construction for \(2\le n\le9\), and samples \(1{,}000\) four-pair and \(150\) five-pair profiles. Reproduction: run `python3 VERIFY.py` next to this file. Observed output:

```
VERIFY_OK cyclic_sizes=2..9 exhaustive_2=16 exhaustive_3=46656
THREE_BY_THREE extremal_count=12 strict_gain_profiles=5424 max_product_ratio=8
SAMPLED_OK n4=1000 n5=150
```

Finite testing is a supplement to the all-\(n\) proof, not an exhaustive verification beyond \(n=3\). The independent brute-force implementation tests each putatively stable permutation against all man-woman blocking pairs.

## Relationship to prior work

Desai, Rasheed M, Ghalme, and Gujar [1] formalize Nash-welfare optimization under the **same** rank-derived utilities and provide an algorithm to find an optimal stable matching. Their analyses and comparisons concern computing and experimentally evaluating welfare-maximizing stable outcomes. Inspection of the original preprint, including definitions, theorems, algorithmic sections, experiments, and conclusion, did not identify the present universal *comparison with the men-proposing deferred-acceptance baseline*, the sharp extremizer classification, or extremal-profile count. The classical Gale--Shapley man-optimality theorem, used as a premise here, is not new. Jain and Vaish [2] investigate two-sided Nash welfare with capacity and unrestricted cardinal matching choices; those results do not establish the stated stable-marriage bound.

Related published small-market calculations [3,4] count stable-marriage structures and compare other fairness objectives, respectively. Their reported results do not state the all-size Nash-product ratio or the strict extremizer characterization. Earlier work on Nash-product versus minimax-regret optimization compares distinct objectives rather than the proposer-optimal-baseline approximation factor. The elementary product argument and the sharp construction are both necessary to obtain the exact theorem.

## Limitations

The result depends on strict, complete, balanced bipartite preferences and the precise rank utility scale \(n-r\). It is not an approximation guarantee for arbitrary cardinal valuations, incomplete preference lists, capacities, unmatched agents, nor the welfare of an arbitrary stable matching. The comparison is between a welfare-optimal stable matching and the **men-proposing** deferred-acceptance outcome, not a general claim that every stable matching incurs this much loss. The exact equality census excludes \(n=2\), where the ratio is identically one. Search and document inspection cannot rule out unindexed or unreviewed equivalent results; independent scientific audit is outstanding.

## References

[1] P. Desai, Rasheed M, G. Ghalme, S. Gujar, *Fair Stable Matching: A Nash Social Welfare Approach*, arXiv:2609.02354v1, first submitted 2026-09-02. https://arxiv.org/abs/2609.02354

[2] P. Jain, R. Vaish, *Maximizing Nash Social Welfare under Two-Sided Preferences*, AAAI 2024, DOI:10.1609/aaai.v38i9.28839; original preprint arXiv:2312.09167. https://arxiv.org/abs/2312.09167

[3] *Full-symmetry census of three-by-three stable-marriage profiles*, published-finding corpus record `2026/10/4/SCOPE-full-symmetry-census-of-three-by-three-stable-marriage-profiles--58b281ed93c1`.

[4] *Sharp three-by-three conflict layer for rank-maximal and sex-equal stable marriage*, published-finding corpus record `2026/10/4/SCOPE-sharp-three-by-three-conflict-layer-for-rank-maximal-and-sex-equ--8dcd874ae6a3`.
