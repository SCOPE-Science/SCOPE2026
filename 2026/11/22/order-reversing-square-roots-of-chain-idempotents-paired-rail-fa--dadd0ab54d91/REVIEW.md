# Review of order-reversing square-root fibers

## Correctness

PASS. The full proof derives the unique reversal of the square's fixed-point set, the necessary and sufficient endpoint conditions for each coupled rail pair, and the weighted double generating function for those pairs. Its coefficient extraction proves the pointwise root polynomial; summing over all rooted interval fibers proves the global rank identity. The additional one-sided calculation independently reconstructs the isotone benchmark. `verify.py` actually computes all opposite-rail possibilities through lengths six and every map of both monotonicities on chains through nine points. It checks every individual idempotent-root polynomial, not just aggregate counts. Finite checking supplements the arbitrary-dimension proof; it does not extend the brute-force range to infinity.

## Originality

PASS relative to inspected literature, subject to historical-priority risk. The published isotone joint-rank result already contains the same numerical binomial coefficient and rational generating function. Those *numeric formulas by themselves are not claimed novel*. The new claim concerns order-reversing square roots of **each given idempotent**, with a product over reversed pairs of its side lengths; the global equality with isotone ranks then emerges by a separate sum. The fact that an idempotent on five points with one middle fixed point has antitone root polynomial \(1+8v+3v^2\), compared with the isotone \(1+2v+v^2\), establishes that the existing isotone formula cannot merely be transplanted pointwise. The 2022 study of the full monotone transformation monoid treats endomorphisms, the 2005 study addresses congruences, and the separately published injective partial-Catalan root formula concerns a different object. An earlier unpublished or poorly indexed general root-count theorem could subsume the result; no global originality certification is claimed.

## Value

PASS. The main object—composition-square roots of idempotents inside the order-reversing part of a natural finite transformation monoid—is structurally motivated by the presence of nontrivial two-cycles and by the fact that a square returns to the order-preserving submonoid. The exact idempotent-by-idempotent fiber polynomial distinguishes root counts that cannot be determined by the size or rank of the target alone, while the aggregate equidistribution identifies an unexpected invariant shared with order-preserving maps. The formula applies to arbitrary fiber profiles and all positive chain lengths, rather than isolated small examples. No general theorem on other transformation families is asserted.

## Closest sources and limitations

The closest statement in the literature is *Joint stable-rank and image-rank enumeration of quasi-idempotents on a finite chain* (2026-11-02), which determines the isotone joint-rank expression but not the antitone square-root fibers. D. B. Li and V. H. Fernandes, *Endomorphisms of semigroups of monotone transformations* (arXiv:2204.07838, posted 2022-04-16), supplies the setting but asks different questions. Fernandes, Gomes and Jesus (2005) describe congruences; Imam et al. (2023) treat the isotone class. The older literature on order-reversing quasi-idempotent generating ranks was only located in an abstract, making broad unindexed overlap a residual risk. The calculation neither constructs a canonical pairing of isotone and antitone solutions nor treats nonmonotone or partial transformations.

Self-review: passed. Independent audit: not yet performed.
