# Scientific review: exponential commutativity law for finite-chain partial translations

## Correctness — PASS
The finite-chain partial-isometry monoid is represented by signed displacements and arbitrary eligible source subsets. The established cardinality is used correctly, and the exact mixed commuting-pair census follows from a concrete forest: the edges of a nonzero translation have no cycles, so there are \(n-r\) connected components and hence \(2^{n-r}\) commuting partial identities. Multiplication by the exact displacement/rank count proves the mixed formula.

For the remaining ordered pairs of two nonidempotents, the proof uses the exact pointwise commutation equation. Each of at least \((n-4h)/5\) independent constraints equates two independent Bernoulli products and holds with probability \(5/8\). The dependency graph has maximum degree four, and the complementary large-displacement contribution is bounded by a geometric tail. These two estimates imply exponential suppression of all remaining commuting pairs. The resulting limit and concentration on pairs of idempotents follow algebraically. The standalone program exhaustively enumerated the actual monoid through size nine and checked all claimed finite identities. No finite check was treated as proof of the asymptotic result.

## Originality — PASS, with priority limitations
The 2010 foundational paper [1] and the 2014 counting paper [2] provide monoid size and one-element statistics but not the claim's mixed-idempotent fiber classification, ordered commuting proportion, or asymptotic estimate. A relevant complete published product-rank law [4] computes the distribution of \(\operatorname{rank}(fg)\), not the **joint equality event** \(fg=gf\); a marginal product-rank distribution cannot determine that event. A published three-tenths commutation law [5] counts a different inverse monoid restricted to interval domains, rather than arbitrary subsets. Independent searches under partial translations, inverse semigroup commuting probability, rank, and idempotent centralizers did not identify a statement dominating this combined claim. Uninspected general results may still imply the limit, so the priority conclusion is provisional, not a claim of exhaustive uniqueness.

## Value — PASS
The probability that two uniform elements of a natural, exponentially large inverse semigroup commute is an intrinsic structural statistic. The one-ninth law is not merely the known idempotent fraction: the difficult content is the uniform exponential bound showing that the other elements contribute negligibly, together with exact rank-refined mixed commuting fibers. It distinguishes the all-subsets partial-translation monoid from the interval-only rook monoid, whose commuting limit is three tenths and arises from a different mechanism. This is motivated enumeration and a nontrivial asymptotic structural boundary, not a renamed cardinality identity.

## Closest literature and limitations
[1] R. Kehinde and A. Umar, *On the semigroup of partial isometries of a finite chain*, arXiv:1101.0049v1, 2010, particularly Theorem 3.6.

[2] F. Al-Kharousi, R. Kehinde and A. Umar, *Combinatorial results for certain semigroups of partial isometries of a finite chain*, Australasian J. Combin. 58 (2014), 365–375.

[4] *The product-rank law of finite-chain partial translations*, accessible 2026 mathematical research record, full theorem, proof and limitations compared.

[5] *A three-tenths commutativity law for interval-translation rook monoids*, accessible 2026 mathematical research record, full theorem, proof and limitations compared.

The exact number of commuting pairs of two nonidempotents remains undetermined. The exponential upper bound need not give the optimal convergence exponent. Completeness of priority search and mathematical independence have not been established.

Self-review: passed. Independent audit: not yet performed.
