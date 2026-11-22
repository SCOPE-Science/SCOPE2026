# Scientific review

## Correctness — PASS

The claimed inverse theorem has three logically separable steps: the full Katětov triangle table gives independent cluster factors; the Bang–Zsigmondy theorem yields a primitive prime for each Mersenne exponent at least two other than six; and the sole exceptional identity changes both total named-point count and cluster count by a nonzero amount. The proof states all hypotheses and quantifiers. The `artifacts/check.py` program independently enumerates 44 complete distance-type histograms through seven points, verifies the scalar formulas on 28,628 integer-partition profiles through size thirty, and checks every numerical collision not exceeding one million. These finite tests support, but do not replace, the infinite primitive-divisor argument.

## Originality — PASS, with historical-priority limits

The general weighted one-point type polynomial on arbitrary graph-metric bases and its Widom–Rowlinson interpretation are already published; specializing that theorem to disjoint cliques gives the present product formula and is **not** a new claim. The Bang–Zsigmondy theorem also supplies the underlying number theory. The independently assessed finding is the complete inverse classification of scalar-type multiplicative collisions, including rigidity after either natural size datum is given. Source searches and materially inspected prior works did not state this particular inverse classification. It remains possible that it is implicit in an unindexed treatment of Mersenne product identities.

The closest relevant prior works are Sauer, *Partitions of metric spaces with finite distance sets* (arXiv:1010.4212), Conant, *Neostability in countable homogeneous metric spaces* (arXiv:1504.02427), and *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space* (publicly available 2026-10-04). A prior related cluster result using intercluster distance three has different counting factors and does not imply the distance-two inverse classification.

## Mathematical value — PASS

The question asks how much of a finite named metric parameter structure can be reconstructed from the mere number of logically possible nonalgebraic singleton extensions, not from a full polynomial or higher-arity data. The complete inverse classification is uniform in all cluster sizes. Its one exceptional operation is forced by an arithmetic primitive-divisor obstruction; the result determines exactly which minimal extra datum eliminates it and the smallest unavoidable collision without that datum. This complements existing broader type-counting formulas with a precise rigidity/ambiguity theorem rather than just a computational specialization.

## Boundaries

This establishes no reconstruction for arbitrary finite metrics, arbitrary distance-one graphs, or different distance alphabets. The proof imports the classical primitive-divisor theorem; historical novelty is assessed against located sources rather than certified globally. Independent mathematical audit has not been undertaken.

Self-review: passed. Independent audit: not yet performed.
