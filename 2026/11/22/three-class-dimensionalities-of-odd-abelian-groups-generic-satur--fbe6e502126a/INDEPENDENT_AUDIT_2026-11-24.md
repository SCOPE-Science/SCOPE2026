# Independent mathematical audit

## correctness

PASS

For each fixed target u, x↦u−x is an involution, with one fixed point by invertibility of doubling. Excluding the fixed point and {0,u} leaves (n−3)/2 disjoint nonzero unequal pairs for u≠0, and (n−1)/2 for u=0. Independent fair colors give the stated failure bounds for the two monochromatic patterns and the mixed pattern; additional diagonal representations can only help. Union bounding over targets and dividing successful labeled colorings by two gives the stated uniform lower bound even if it is vacuous for small n. Saturation directly gives every D2 lift (identity products are unchanged), so the claimed proportions follow from the bound and the exact total 2^(n−2)−1. For n≤7 a smaller class of size at most (n−1)/2 has fewer than n unordered pairs with repetition. I reproduced the remaining finite cutoff checks with `python3 /workspace/review-evidence/check_5.py`: target-sum buckets of unordered pairs, tracking color-count patterns 0,1,2, gave zero successes among 256, 256 and 1024 labeled colorings of C9, C3×C3 and C11. Independent invariant-factor enumeration gave all 13 necessary types for 13≤n≤31, and the check verified all 15 listed witnesses by reading the frozen dictionary as data, not executing its script. The replay also gave ε_33=474054603/536870912; each term decreases along odd orders n≥33 since its ratio is (1+2/n) times 3/4 or 1/2. The quotient has ordinary identity products and every nonidentity product full, satisfying relational associativity, but A has both A and B as inverses. Inversion preserves the partition exactly when every opposite pair is monochromatic or every pair is bichromatic, giving ((2^m−2)+2^m)/2=2^m−1 with m=(n−1)/2. Inversion commutes with group automorphisms and therefore permutes their orbits, proving the asymptotic exclusion as well. The threshold is for full saturation, not for existence of any dimensionality; fixed-group D3 is not generally computed.

## originality

PASS

The substantive contribution is the uniform odd-abelian estimate and the sharp universal threshold for the simultaneous three full sumsets. Jenča supplies the support-lifting and quotient framework; the random matching device itself is elementary and not credited as new. The most similar older partition classifications impose inversion preservation, which precludes full saturation, and the closest same-day record concerns first inverse incompatibility rather than the full triad or its typicality.

## value

PASS

The result identifies a typical and concrete three-class quotient, rather than just an isolated non-hypergroup example. The uniform rate across invariant-factor types makes clear how support-level closure differs from inverse-compatible partition theories, and the exact threshold answers when that same quotient can first be realized by full saturation in every odd abelian group. Finite computation is confined to the natural cutoff, not presented as a count for all orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
