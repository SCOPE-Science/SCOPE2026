# Conformity orders every neutral monotone voting rule in a zealot–contrarian electorate

## Finding

**Theorem (rule-uniform strict conformity order).** Fix an integer \(n\ge 1\), exogenous influence weights \(a,b>0\), and an inertia parameter \(0\le \ell<1\). In the fully mixed binary zealot–contrarian voter model described below, let \(Y_r\in\{0,1\}^{n}\) denote the unique stationary vector of free votes under conformity probability \(r\in(1/2,1]\). Let \(F:\{0,1\}^{n}\to\{0,1\}\) be any coordinatewise nondecreasing, self-dual binary aggregation rule, meaning
\[
F(\mathbf1-y)=1-F(y)\quad\text{for every }y\in\{0,1\}^{n}.
\]
Then, for every \(1/2<r_1<r_2\le1\),
\[
\operatorname{sgn}\!\bigl(\mathbb E F(Y_{r_2})-\mathbb E F(Y_{r_1})\bigr)
=\operatorname{sgn}(a-b),
\]
where the difference is **strictly nonzero** whenever \(a\ne b\). In addition, \(\lim_{r\downarrow1/2}\mathbb E F(Y_r)=1/2\), and \(\mathbb E F(Y_r)=1/2\) for every \(r\) if \(a=b\). Thus, if the correct alternative has stronger committed influence, every such rule is strictly more accurate at greater conformity; if the incorrect alternative has stronger influence, every rule's correct-choice probability strictly decreases instead.

The theorem includes ordinary strict majority for odd \(n\), every weighted majority rule with a deterministic self-dual tie resolution, dictatorial rules, and hierarchical assemblies built from self-dual monotone subrules. It makes no assumption that the aggregation rule is anonymous.

**Exact finite-electorate illustration.** For two units of correct influence and one of incorrect influence, ordinary majority on \(n=2m+1\) free voters satisfies
\[
\mathbb P\{\mathrm{majority}=1\}
=\frac12+
\frac{(2m+1)\binom{2m}{m}\mathrm B(c+m+1,c+m+1)}{c\,\mathrm B(c,c)},
\qquad c=1+\frac{(1-r)(n+2)}{2r-1},
\]
for every \(r>1/2\). Here \(\mathrm B\) is the beta function. This is a reproducible exact formula, not a new stationary law.

## Assumptions and scope

There are \(n\) free voters taking values in \(\{0,1\}\), plus two fixed influence sources of weights \(a\) (correct choice \(1\)) and \(b\) (incorrect choice \(0\)). At each discrete update, a free voter is sampled uniformly. With probability \(\ell\) the vote is retained. Otherwise the voter samples one of the other \(n-1\) free voters, each with unit weight, or the fixed sources, with total source weight \(a+b\); with probability \(r\) the sampled value is copied and with probability \(1-r\) it is flipped. The weights may be arbitrary positive real numbers. Positive source weights and \(\ell<1\) imply an irreducible, aperiodic finite chain.

The result is a stationary statement after arbitrarily long social updating. It does not assert monotonicity of a finite-time election held before equilibrium, nor of asymmetric/non-neutral rules or arbitrary network topologies. For an even electorate the standard unqualified strict majority has a tie outcome and is not a binary self-dual rule; self-dual tie resolution or another neutral rule is required.

## Proof

1. **Stationary exchangeable beta mixture.** Let \(X=\sum_{i=1}^nY_i\). The primary source's birth–death detailed-balance calculation gives, for \(r>1/2\),
\[
\mathbb P(X=k)=\binom nk\frac{(a+t)_k(b+t)_{n-k}}{(a+b+2t)_n},\quad
 t=\frac{(1-r)(n-1+a+b)}{2r-1},\quad k=0,\ldots,n.
\]
For clarity, \((z)_j=z(z+1)\cdots(z+j-1)\), with \((z)_0=1\). Because both committed sources have positive weights, every named free voter has positive probability of switching either way at each update; hence the complete labeled-state chain is irreducible. Its unique stationary distribution is invariant under every permutation of free-voter labels. Therefore every individual binary configuration with \(k\) ones has equal stationary probability, and the unique stationary law is the mixture
\[
P_t\sim\mathrm{Beta}(a+t,b+t),\qquad
(Y_1,\ldots,Y_n)\mid P_t=p\ \sim\ \mathrm{Bernoulli}(p)^{\otimes n}.
\]
This is an exact identity for the full stationary vector, not merely an approximation based on moments. The source's transition probabilities are strictly positive between adjacent count states, so no additional invariant laws occur. The inertia factor cancels from detailed balance.

2. **Order of the unsigned beta bias.** Write \(Z_t=|P_t-1/2|\in(0,1/2)\). Its density, up to a positive normalizing constant, is
\[
w_t(z)=\bigl(\tfrac14-z^2\bigr)^t
\left[(\tfrac12+z)^{a-1}(\tfrac12-z)^{b-1}
+(\tfrac12-z)^{a-1}(\tfrac12+z)^{b-1}\right].
\]
For \(t_2>t_1\ge0\), the likelihood ratio \(w_{t_2}(z)/w_{t_1}(z)\), with normalization included, is proportional to \((1/4-z^2)^{t_2-t_1}\). It is strictly decreasing throughout \((0,1/2)\). The single-crossing argument for two positive normalized densities implies that \(Z_{t_2}\) is **strictly stochastically smaller** than \(Z_{t_1}\): its expectation of every strictly increasing continuous function is strictly smaller (assuming boundedness, as holds here).

3. **A sign law independent of the aggregation rule.** Define \(g(p)=\mathbb E[F(B_1,\ldots,B_n)]\), where the \(B_i\) are independent \(\mathrm{Bernoulli}(p)\). By self-duality, \(g(1-p)=1-g(p)\), so \(g(1/2)=1/2\). By monotonicity, \(g\) is increasing; in fact it is **strictly** increasing on \((0,1)\). To verify strictness, \(F(\mathbf0)=0\) and \(F(\mathbf1)=1\) by monotonicity and self-duality, and a path changing bits from all zeroes to all ones has an edge on which \(F\) changes from zero to one. A shared-uniform-variable coupling at any \(p<p'\) has positive probability of realizing this pivotal transition, hence \(g(p)<g(p')\).

Conditional on \(Z_t=z\), the probability that \(P_t=1/2+z\), rather than \(1/2-z\), is
\[
s(z)=\frac{1}{1+\left(\frac{1/2-z}{1/2+z}\right)^{a-b}}.
\]
Crucially, the common beta-density factor \(p^t(1-p)^t\) cancels, making \(s\) independent of \(t\). Using self-duality once more,
\[
\mathbb E[F(Y_r)]-\tfrac12
=\mathbb E\left[
\bigl(2s(Z_t)-1\bigr)
\bigl(g(\tfrac12+Z_t)-\tfrac12\bigr)
\right].
\]
If \(a>b\), both factors in the integrand are positive and strictly increasing in \(z>0\), so the product is strictly increasing. If \(a<b\), the first factor is negative and strictly decreasing, while the second is positive and strictly increasing; the product is strictly decreasing. If \(a=b\), the first factor vanishes. Applying the strict stochastic ordering from Step 2 proves the corresponding strict sign of the difference with respect to \(t\).

4. **Return to conformity and endpoints.** The map \(r\mapsto t\) is strictly decreasing from \(+\infty\) to \(0\) on \((1/2,1]\). Hence the sign of the comparison in \(r\) is exactly the sign of \(a-b\). As \(t\to\infty\), the \((1/4-z^2)^t\) factor concentrates \(Z_t\) at zero; the bounded integrand in Step 3 vanishes there, proving the limiting value \(1/2\). At \(r=1/2\), the primary model has fair independent votes and self-duality gives probability \(1/2\). All statements follow.

5. **Exact illustrative formula.** For \(a=2,b=1\), put \(c=1+t\). The beta mixing density \(\mathrm{Beta}(c+1,c)\) is \(2p\) times the symmetric \(\mathrm{Beta}(c,c)\) density. For \(n=2m+1\), set \(g(p)=\mathbb P(\mathrm{Bin}(n,p)\ge m+1)\). Then
\[
 g'(p)=(2m+1)\binom{2m}{m}p^m(1-p)^m.
\]
Since \(\frac{d}{dp}[p^c(1-p)^c]=-c(2p-1)p^{c-1}(1-p)^{c-1}\), integrating by parts with vanishing endpoint terms yields
\[
\mathbb E_{P\sim\mathrm{Beta}(c+1,c)}g(P)-\tfrac12
=\frac{(2m+1)\binom{2m}{m}}{c\,\mathrm B(c,c)}
\int_0^1p^{c+m}(1-p)^{c+m}\,dp.
\]
The integral equals \(\mathrm B(c+m+1,c+m+1)\), giving the claimed expression without approximation.

## Verification

Run the included standard-library program `checker.py` with `python checker.py`. It tests 960 rational count-chain invariants and conformity comparisons, 76 pairs of exact checks covering **all** monotone self-dual Boolean rules on one through four free voters over four leader-weight pairs and five conformism values, plus 30 exact finite-majority beta-function formula identities. A numerical near-boundary illustration is also printed but is not used in the proof. The analytical steps above, especially continuous likelihood-ratio ordering and the all-rule quantifiers, supply the infinite proof; finite tests alone do not certify them.

## Relationship to prior work

Braha and de Aguiar (2026) establish the exact stationary beta–binomial law, the finite-electorate Condorcet-type advantage over one free voter, and a fixed-conformity large-population dichotomy (Theorems 1, 3, 5, 6). None of those statements compares **all finite** conformity values simultaneously for **every** self-dual monotone aggregation rule, and the rule-uniform likelihood-ratio proof is separate. The stationary law is explicitly credited to that paper.

An independent public review of that paper already identifies a near-conformity scaling limit when conformism changes with the population size; that limit is **not claimed here as new**. Berend and Sapir (2007) address improvement with *committee size* under dependence, rather than variation in the copying/contrarian parameter for a fixed electorate and arbitrary self-dual aggregation functions. Arab, Oliveira and Wiklund (2021) characterize beta transform orders and probabilities exceeding the *mean or mode*; their first-order beta dominance comparison requires one shape to increase while the other decreases, unlike the common positive addition \((a+t,b+t)\) here. These are statement-level distinctions, not arguments that absence of a keyword proves novelty.

## Limitations

The result is a mathematical stationary-order theorem under common, fully mixed contact weights and positive committed influence; social-network heterogeneity can break the exchangeable beta representation. The voting rule must be coordinatewise monotone and self-dual; biased thresholds or abstention rules are not covered. It provides neither a finite-time social-mixing bound nor empirical accuracy forecasts. The literature comparison is best-effort and cannot establish worldwide priority, particularly where related full texts remain inaccessible. No independent mathematical audit has been performed.

## References

1. D. Braha and M. A. M. de Aguiar, *Majority Correctness in Social Networks: From Well-Mixed Electorates to Complex Networks*, first public release July 15, 2026, arXiv:2607.14288, https://arxiv.org/abs/2607.14288 . Theorems 1, 3, 5 and 6, Sections 4–5 and appendices.
2. D. Berend and L. Sapir, *Monotonicity in Condorcet's Jury Theorem with dependent voters*, Social Choice and Welfare 28 (2007), 507–528, https://doi.org/10.1007/s00355-006-0179-y .
3. I. Arab, P. E. Oliveira and T. Wiklund, *Convex transform order of Beta distributions with some consequences*, Statistica Neerlandica 75 (2021), 238–256, https://doi.org/10.1111/stan.12233 .
4. Public reading note for arXiv:2607.14288, https://pith.science/paper/2607.14288 (its identified near-conformity limit is cited only as prior discussion, not as part of the new finding).
