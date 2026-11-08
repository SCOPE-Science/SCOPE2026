# Scientific review

## Correctness — PASS

The source facet system for strictly positive integer parameters is stated in [1], Theorem 2.3(c); the unusual redundant cardinality when the first parameter equals one is handled explicitly. The Euclidean normal of a size-\(k\) subset inequality has norm \(\sqrt k\). Symmetrization reduces the Chebyshev-center problem to one scalar, eliminating which yields the exact lower/upper barrier \(r(k+\sqrt k)\le H_k-k\). The explicit diagonal center attains the minimum; equality for any minimizing facet orbit combined with lower-coordinate barriers forces uniqueness. Strict convexity of the planar curve \((u(t),v(t))\) gives ordered crossover parameters and hence the existence of a unique contact rank for every \(k\). The integer realization approaches those strict phase inequalities and is therefore eventually exact. An independent finite LP implementation verifies 150 examples and 104 rank-realization examples. No exhaustive computer search or unproved asymptotic assertion is used as an infinite proof.

## Originality — PASS (historical priority provisional)

The full arbitrary-parameter facet description [1] and general normal-fan results [3] give structural prerequisites but no Euclidean inball or all-ranks realization. The two-parameter metric result [5] is strictly narrower, with only endpoint facet ranks competing; it cannot entail the construction of interior contact ranks, as the explicit eight-dimensional example already lies outside that two-parameter family. The inspected 2022 foundational study [2] and 2026 lattice/Ehrhart study [4] treat different geometric/enumerative invariants. Queries on equivalent terminology (inball, Chebyshev center, symmetric polymatroid, parking-function and generalized permutahedral variants) did not identify the full formula or realization theorem. This is not a proof of global publication priority; an equivalent symmetric-polymatroid metric theorem could exist.

## Mathematical value — PASS

The principal contribution is the all-ranks realization theorem, not just a routine facet-distance computation. It produces a sharp qualitative contrast with the previously studied two-parameter geometry: for any dimension, one can choose a parameter vector realizing any designated cardinality as the sole upper tangent orbit, including the middle rank with \(\binom n{\lfloor n/2\rfloor}\) simultaneous tangencies, while the combinatorial type remains that of the stellohedron. The exact inradius and unique center make the contact transition calculable. No conjectured downstream theorem is assumed.

## Closest literature and limits

[1] Bayer et al., arXiv:2403.07387, Theorem 2.3(c) and Corollary 3.14, proves the facets/combinatorial type, not the new Euclidean conclusions. [2] Hanada et al., arXiv:2212.06885, establishes the special two-parameter geometry/volume. [3] Liu–Thawinrak, arXiv:2512.14199, studies normal fans and Ehrhart theory. [4] Hill et al., arXiv:2607.15503, treats lattice slices/Ehrhart. [5] Published research record `53d2c657716a` proves a two-phase inball for \(\mathbf b=(a,b,\ldots,b)\), without interior phases. The result is coordinate-metric-specific; ties among multiple upper ranks are not classified. Independent mathematical assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
