# Strict coverage-time majorization and rare-colour tails for reinforced urns

## Finding

Consider the classical unit-reinforcement Pólya urn with \(k\ge 2\) colours and strictly positive initial masses \(a_1,\ldots,a_k\). Let \(T_a\) denote the first draw index at which every colour has appeared. The same model with real positive masses is defined through the usual predictive probability rule. Put \(A=\sum_{i=1}^k a_i\) and \((x)_{\overline t}=\prod_{j=0}^{t-1}(x+j)\).

**Strict stochastic majorization.** If \(a,b\in(0,\infty)^k\) have the same sum and \(a\) majorizes \(b\), then for every integer \(t\ge0\),
\[
\Pr(T_a>t)\ge \Pr(T_b>t).
\]
If \(b\) is not a permutation of \(a\), the inequality is strict for every \(t\ge k\). For \(0\le t<k\), both sides equal one. Thus equal initial masses uniquely minimize the entire coverage-time distribution in stochastic order at fixed total initial mass, up to colour relabeling.

**Exact survival and rare-colour law.** For each integer \(t\ge1\),
\[
\Pr(T_a>t)=\sum_{\varnothing\ne S\subsetneq[k]}(-1)^{|S|+1}\frac{(A-a_S)_{\overline t}}{(A)_{\overline t}},\qquad a_S=\sum_{i\in S}a_i.
\]
Writing \(\alpha=\min_i a_i\) and \(m=|\{i:a_i=\alpha\}|\),
\[
\Pr(T_a>t)\sim \frac{m\Gamma(A)}{\Gamma(A-\alpha)}t^{-\alpha}\quad(t\to\infty).
\]
Conditioned on \(T_a>t\), with probability tending to one there is exactly one still-unseen colour, and that colour is asymptotically uniform over the \(m\) initially least-mass colours. Furthermore, for every real \(s>0\),
\[
\mathbb E[T_a^s]<\infty\quad\Longleftrightarrow\quad s<\alpha.
\]

## Assumptions and scope

At each discrete draw, choose colour \(i\) with probability its present mass divided by total present mass, replace the chosen ball, and add unit mass of the same colour. Initially every mass is positive. For integer initial masses this is the literal urn; real positive masses use the identical predictive process. A vector \(a\) majorizes \(b\) if, after sorting both in decreasing order, their first \(j\) coordinate sums satisfy \(\sum_{i\le j}a_{(i)}\ge\sum_{i\le j}b_{(i)}\) for \(1\le j<k\) and their totals agree. The law of \(T_a\) takes values in \(\{k,k+1,\ldots\}\); no large-\(k\) or integer-mass assumption is made. The case \(k=1\) is excluded because the cover time is deterministically one and the gamma ratio would be undefined.

## Proof

**1. Exact distribution.** The exchangeable colour sequence is a Dirichlet mixture: sample \(P\sim\operatorname{Dirichlet}(a_1,\ldots,a_k)\), then conditionally take independent draws with probabilities \(P_i\). Consequently, for any proper subset \(S\) and integer \(t\ge1\), the chance that no colour in \(S\) appears among the first \(t\) draws is
\[
\mathbb E[(1-P_S)^t]=\frac{(A-a_S)_{\overline t}}{(A)_{\overline t}}.
\]
Inclusion–exclusion over missing colours proves the displayed survival formula. In particular, \(\Pr(T_a=k)=k!\prod_i a_i/(A)_{\overline k}\).

**2. A strict two-coordinate balancing lemma.** Hold the sum \(h=a_i+a_j\) fixed and fix all other coordinates. Dirichlet aggregation writes \(Q=P_i+P_j\) and \(U=P_i/Q\). The joint law of \(Q\) and the outside probabilities is independent of the split of \(h\), and \(U\sim\operatorname{Beta}(a_i,a_j)\) is independent of these aggregated probabilities. Let \(M\) count the first \(t\) draws landing in the pair. Conditional on \(M\) and on which outside colours appeared, the probability that both pair colours appeared is zero for \(M=0,1\) and, for \(M\ge2\), exactly
\[
1-\frac{(a_i)_{\overline M}+(a_j)_{\overline M}}{(h)_{\overline M}}.
\]
For each integer \(M\ge2\), the function \(x\mapsto(x)_{\overline M}\) has strictly positive second derivative on \((0,\infty)\): it is a product of positive affine factors, at least two of which contribute a strictly positive term in its second derivative. Hence \(x\mapsto(x)_{\overline M}+(h-x)_{\overline M}\) is strictly convex and symmetric about \(h/2\). Any nontrivial balancing transfer between the pair therefore strictly increases the conditional probability that both colours occur when \(M\ge2\), without altering the law of the aggregate/outside observations. The full coverage probability increases strictly for \(t\ge k\), since an event on which every one of the other \(k-2\) colours is seen and at least two pair draws occur has positive probability. At \(t<k\), full coverage is impossible.

The finite sequence of two-coordinate averaging (Robin Hood) transfers characterizing majorization then proves the stochastic order for all vectors. If the vectors are not permutations, at least one nontrivial transfer occurs, so the order is strict for each \(t\ge k\). The balanced vector is majorized by every vector with the same positive sum, establishing its unique extremality.

**3. Exact tail index and last unseen colour.** For a single colour \(i\), the probability it has not appeared by time \(t\) is
\[
\frac{(A-a_i)_{\overline t}}{(A)_{\overline t}}=\frac{\Gamma(A)}{\Gamma(A-a_i)}\frac{\Gamma(A-a_i+t)}{\Gamma(A+t)}\sim \frac{\Gamma(A)}{\Gamma(A-a_i)}t^{-a_i}.
\]
Two distinct absent colours \(i,j\) have joint absence probability of order \(t^{-(a_i+a_j)}\), strictly smaller than \(t^{-\alpha}\) because every initial mass is positive. Thus the singleton union bound and the first Bonferroni correction have the same leading order, and only the \(m\) smallest masses contribute. This gives the sharp survival constant and, by dividing individual absence probabilities by the union probability, the asserted unique last-unseen-colour limit. Finally, the discrete tail-sum identity for positive moments shows \(\mathbb E[T_a^s]\) is finite exactly when \(\sum_{t\ge1}t^{s-1}\Pr(T_a>t)\) converges; the sharp power law makes this equivalent to \(s<\alpha\).

## Verification

The accompanying standard-library-only `verify.py` independently computes full-colour survival probabilities by (i) the subset inclusion–exclusion expression, (ii) full Dirichlet–multinomial occupancy enumeration, and (iii) direct enumeration of sequential reinforced paths. It also checks strict balancing for integer and rational initial masses, convexity of pair-split kernels and numerical gamma-ratio tail estimates. Replay with `python3 verify.py`; the expected output is `VERIFY_OK 2981`. All these finite tests corroborate, but do not replace, the preceding all-parameter proof.

## Relationship to prior work

Henze and Holmes (2019) establish the first-arrival waiting-time power-tail and moment threshold for one distinguished colour in a two-colour reinforced urn. The present tail calculation extends this known single-colour mechanism to the union of missing colours and determines the asymptotically unique unobserved colour. Zoroa and collaborators (2016) establish strict majorization ordering of coupon collection for independent trials at a **fixed** unequal probability vector. That result does not itself compare two reinforced urns whose Dirichlet mixing laws have different concentration vectors; the strict beta-split argument supplies this comparison. Dean (2022) proves functional limits for Pólya urn compositions under growing initial configurations, rather than fixed-configuration complete-coverage stochastic ordering. These antecedents are fully credited, and the independent majorization argument is the specifically scoped contribution.

## Limitations

The result requires the classical identity-reinforcement rule and strictly positive initial masses; arbitrary replacement matrices, colour extinction, random numbers of colours and nonunit reinforcement without matching rescaling are not covered. It is not a statement of likelihood-ratio ordering, stochastic ordering of coverage-time point masses, or monotonicity when the total initial mass changes. It does not assert historical priority beyond the inspected sources or provide independent mathematical validation.

## References

- N. Henze and M. P. Holmes, *Curiosities regarding waiting times in Pólya’s urn model*, arXiv:1911.01052, first public 2019-11-04, https://arxiv.org/abs/1911.01052.
- N. Zoroa, E. Lesigne, M.-J. Fernández-Sáez, P. Zoroa and J. Casas, *The coupon collector urn model with unequal probabilities in ecology and evolution*, arXiv:1608.00155, first public 2016-07-30, https://arxiv.org/abs/1608.00155.
- C. B. C. Dean, *Functional limit theorems for Pólya urns with growing initial compositions*, arXiv:2206.05138, first public 2022-06-10, https://arxiv.org/abs/2206.05138.
