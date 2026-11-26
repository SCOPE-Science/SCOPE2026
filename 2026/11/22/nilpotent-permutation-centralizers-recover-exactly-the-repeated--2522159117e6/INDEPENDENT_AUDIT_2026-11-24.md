# Independent mathematical audit

## correctness

PASS

Equality of the partial maps forces σ-invariance of the domain. Equivariance and injectivity then identify the map with partial injections on equal-length cycle labels, with d possible phase choices per arrow of a length-d block. A label cycle forbids nilpotence regardless of phases; a chain with j labels contributes j−1 arrows and dies at the jth power. Thus with k arrows there are r−k ordered chains as an unordered collection: permute the labels, choose k noncut positions among r−1 gaps, and divide by (r−k)!. With a bound s on chain size, a j-chain has exponential generating series weight d^(j−1)z^(d(j−1))u^j because its j! orderings cancel the j! label denominator. The exponential can be taken over Q and the extracted counts are integral. A block with r=0 or 1 is invisible; otherwise its first coefficient is d r(r−1) in degree d. After dividing out the recovered factors, the least nonzero residual degree identifies the next d without knowing n, and that coefficient identifies r≥2 uniquely. Divisions lower degree, so this also proves termination and exact ambiguity. The empty map has index 1, and taking a single chain in each nonempty block attains both stated maxima.

## originality

PASS

The structural equal-length wreath/phase decomposition and Lah chain counts are known ingredients, and applying them gives the forward product. The supported contribution is the exact information retained by the nilpotent rank statistic for total permutations, including its unavoidable singleton ambiguity, together with the rank/index refinement. The closest checked reconstruction and centralizer results change the objects, counted elements, or rank and do not supply this equivalence.

## value

PASS

A natural subfamily of commuting maps discards every singleton cycle, yet its one-variable domain-rank counts retain all repeated lengths and multiplicities even across degrees. This exact loss-of-information boundary is useful when only the nilpotent part of a centralizer is observed and is not an ordinary isomorphism classification of the whole centralizer. The index cutoff adds a separate usable count for bounded escape in the partial map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
