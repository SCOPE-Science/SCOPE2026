# Thirteen species are sharp for a fixed-budget functional-cover ranking reversal

## Finding

Let two communities have the same total number \(S\) of species and the same number \(g\) of disjoint, nonempty functional groups. Draw exactly \(k\) surviving species uniformly without replacement, and call a community *functionally complete* when every group retains at least one species. Write \(H_{\mathbf a}(k)\) for its probability of completeness when its sorted group-size profile is \(\mathbf a=(a_1,\ldots,a_g)\).

**Sharp cutoff and first-layer classification.** For every integer \(S\le12\), no two group-size profiles having the same \(S\) and \(g\) reverse their strict \(H(k)\) ranking between two survivor budgets. The minimum possible total is \(S=13\). At \(S=13\), exactly **three unordered profile pairs**, up to permuting group names, exhibit a strict reversal:

| \(g\) | Profile \(\mathbf a\) | Profile \(\mathbf b\) | Sign of \(H_{\mathbf a}(k)-H_{\mathbf b}(k)\) |
|---|---|---|---|
| 4 | \((1,3,4,5)\) | \((2,2,2,7)\) | Positive for \(k=4,5,6\); negative for \(k=7,\ldots,12\) |
| 4 | \((1,4,4,4)\) | \((2,2,2,7)\) | Positive for \(k=4,\ldots,7\); negative for \(k=8,\ldots,12\) |
| 5 | \((1,3,3,3,3)\) | \((2,2,2,2,5)\) | Positive for \(k=5,6\); negative for \(k=7,\ldots,12\) |

All other budgets give equality for these pairs. For the second pair, the probabilities of functional completeness at \(k=4\) are exactly \(64/715\) and \(56/715\); at \(k=8\) they are exactly \(768/1287\) and \(819/1287\). Thus the ranking switches despite identical species counts and function counts.

**Unbounded family with four functions.** For every integer \(m\ge5\), the two profiles
\[
\mathbf a_m=(1,3,4,m),\qquad \mathbf b_m=(2,2,2,m+2)
\]
have equal total \(S=m+8\) and four functions, and reverse their functional-completeness ranking between \(k=4\) and \(k=S-1\).

## Assumptions and scope

All species belong to exactly one of the \(g\) functional groups, each group represents one binary function, and any surviving species retains that group function. All subsets of exactly \(k\) survivors are equiprobable. The comparisons fix both total species richness \(S\) and functional richness \(g\), varying only the allocation of species across groups. A *strict ranking reversal* means that for two budgets \(k_1,k_2\) one probability difference is strictly positive and the other strictly negative; equality at other budgets is allowed. This is a theoretical null model, not a claim about trait-overlapping functions or nonrandom extinctions.

## Proof

**Exact coverage counting.** Let \(N_{\mathbf a}(k)\) denote the number of \(k\)-element survivor subsets intersecting all groups. By independently choosing a nonempty subset of each group,
\[
N_{\mathbf a}(k)=[z^k]\prod_{i=1}^g\big((1+z)^{a_i}-1\big),\qquad
H_{\mathbf a}(k)=\frac{N_{\mathbf a}(k)}{\binom Sk}.
\]
An independent inclusion-exclusion expression is
\[
N_{\mathbf a}(k)=\sum_{J\subseteq\{1,\ldots,g\}}(-1)^{|J|}
\binom{S-\sum_{j\in J}a_j}{k},
\]
where a binomial coefficient vanishes if its upper argument is below \(k\). Consequently the ranking sign is exactly the sign of the integer coefficient difference. For \(k=g\) the only successful subsets have exactly one species per group, and for \(k=S-1\) the omitted species cannot belong to a singleton group. Therefore
\[
N_{\mathbf a}(g)=\prod_i a_i,\qquad
N_{\mathbf a}(S-1)=S-s_1(\mathbf a),
\]
where \(s_1(\mathbf a)\) is the number of singleton groups. These formulas give a useful general crossing criterion: if \(\prod_i a_i>\prod_i b_i\) but \(s_1(\mathbf a)>s_1(\mathbf b)\), then the ranking must reverse between these two budgets (provided \(g<S-1\)).

**Finite sharpness and complete first layer.** Every nondecreasing positive integer tuple summing to \(S\) is generated once by the recursion that chooses its first part \(j\) between the current lower bound and the remaining sum, and then recursively chooses parts no smaller than \(j\). This is a bijection with all unlabeled group-size profiles, by induction on the remaining sum. For every \(S\) from 1 through 13, group these tuples by their number of parts \(g\). Compare every unordered pair within each group using *all* coefficient differences for \(k=0,\ldots,S\), computed via the polynomial recurrence above. The embedded `verify_function_cover.py` implements exactly this finite exhaustion with unbounded integers, and independently checks every coefficient against inclusion-exclusion. It visits respectively \(1,2,3,5,7,11,15,22,30,42,56,77,101\) profiles at totals 1 through 13, and compares 1,355 pairs of profiles of equal total and number of groups. There are zero reversing pairs for every \(S\le12\) and exactly the three tabulated pairs at 13. It separately compares the three full probability numerators against direct enumeration of every species subset. No pruning by a heuristic or unproved bound occurs. This exact finite certificate proves minimality within the stated domain; it does not assert any statement about larger unexamined totals beyond the family below.

**Infinite family.** For \(m\ge5\), the two four-group profiles have common total \(S=m+8\). At the minimum full-coverage budget \(k=4\),
\[
N_{\mathbf a_m}(4)-N_{\mathbf b_m}(4)
=12m-8(m+2)=4(m-4)>0.
\]
At \(k=S-1\), profile \(\mathbf a_m\) has one singleton while \(\mathbf b_m\) has none, so
\[
N_{\mathbf a_m}(S-1)-N_{\mathbf b_m}(S-1)=-1<0.
\]
The shared positive denominator \(\binom Sk\) preserves each sign, proving a strict ranking reversal for every \(m\ge5\).

## Verification

Run `python3 verify_function_cover.py` (Python standard library only). The checker performs the complete equal-\(S\), equal-\(g\) partition-pair census through \(S=13\), checks two independently implemented integer formulas for every profile and budget, directly enumerates the survivor subsets for each of the three first-layer pairs, and verifies the infinite family's two endpoint identities at additional sample values. The unbounded family is proved algebraically above, not inferred from these sample values. Successful replay prints `PASS: 1355 all-profile pair comparisons through n=13`.

## Relationship to prior work

Fonseca and Ganade (2001) formulate the ecological species-to-function random-extinction framework and motivate functional redundancy as a conservation measure. The present result concerns a different, more stringent event—*all* group functions surviving—and classifies the first equal-richness profile pairs whose full-retention probabilities reverse across fixed survivor budgets. The earlier general species–function expectation/variance framework does not itself state the sharp thirteen-species classification. Petchey and Gaston (2002) study the effects of extinction on trait-based and group-based diversity, rather than a complete finite classification of full-coverage ranking reversals. May (2008) develops quota-based coupon collection under independent draws *with replacement*, not fixed-budget sampling of distinct species without replacement. Classic sequential sampling work by Mallows (1973) has a related stopping-time viewpoint; its full text was not accessible for comparison, so historical priority relative to general stopping-time inequalities is not fully resolved. Our three pairs are incomparable by the usual partition-majorization ordering, which is why generic balancing comparisons do not directly settle their relative risk curves.

## Limitations

The model presumes disjoint, exchangeable species within each functional group, uniform random loss, and binary retention of function. It excludes multifunctionality, species interactions, variable contribution strengths, dependence among extinctions, and ecologically estimated group assignments. A strict crossover in this model is not evidence for an empirical ecosystem crossover. The finite enumeration is exhaustive only through thirteen species; arbitrary larger communities are covered only by the explicit infinite family, not by an all-profile classification. Historical novelty is assessed against inspected accessible sources and remains subject to independent literature verification.

## References

1. Fonseca, C. R. and Ganade, G. (2001). *Species functional redundancy, random extinctions and the stability of ecosystems*. Journal of Ecology 89, 118–125. First published 21 December 2001. https://doi.org/10.1046/j.1365-2745.2001.00528.x
2. Petchey, O. L. and Gaston, K. J. (2002). *Extinction and the loss of functional diversity*. Proceedings of the Royal Society B 269, 1721–1727. https://doi.org/10.1098/rspb.2002.2073
3. May, R. (2008). *Coupon Collecting with Quotas*. Electronic Journal of Combinatorics 15, N31. https://doi.org/10.37236/906
4. Mallows, C. L. (1973). *Sequential Sampling of Finite Populations with and without Replacement*. SIAM Journal on Applied Mathematics 24, 164–168. https://doi.org/10.1137/0124017
