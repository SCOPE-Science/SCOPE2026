# Scientific review — uniform pollen packet threshold

## Correctness (PASS)

The all-or-none success model has exact Poisson upper-tail probabilities at every integer packet size. The proof reduces intermediate sizes to a proportional-mean sequence, whose normalized consecutive differences are strictly increasing; the sequence can have a valley but no interior maximum. Strict endpoint dominance therefore holds for all admissible parameters. A separate log-derivative analysis proves exactly one positive switch between the two surviving packet sizes, including the tie case; the normal approximation is upgraded to a limit by bracketing with the proved sign orientation. Exact rational coefficient tests and 143276 deterministic checks independently diagnose the critical algebra; finite testing is not used in place of proof.

## Originality (PASS, with residual priority risk)

The full 2014 Timerman et al. study measures pollen dispersal unit sizes, the full 2015 Schreiber et al. paper (first online in 2014) optimizes reproductive resource allocation under variable pollen receipt, and the full 2023 Heiling et al. article optimizes pollen presentation for male donation and grooming. None of their inspected mathematical models has both homogeneous Poisson packet receipt at fixed expected grain count and all-or-none seed-quorum success, so their statements do not imply the exact endpoint-only theorem. Relevant mathematical results on coupon packets, point-mass reversals and Gamma upper tails have different observables or threshold scalings. Harder and Johnson's 2008 aggregate-pollen review could not be inspected in full; historical precedence of an equivalent theorem remains a genuine priority risk.

## Mathematical and ecological value (PASS)

Fixed mean pollen receipt and discrete aggregated dispersal-unit sizes are motivated by pollen-packaging and pollen-limitation literature. The theorem supplies a natural complete optimal-design classification across all integer packet sizes, establishes a nontrivial uniform endpoint-dominance property rather than selected numerical instances, and locates an explicit scarcity-to-abundance phase switch with a normal-quantile scaling law. It is an idealized structural result, not a recommendation about any particular species.

## Limits and sources

All claims require perfect cohesive delivery, independent Poisson packet arrivals with mean \(\lambda/k\), fixed grain budget and a strict \(r\)-grain threshold. Heterogeneous packets, different per-grain success probabilities, pollen incompatibility and partial seed production are not covered. References: Timerman et al. (2014), DOI 10.1086/676301; Schreiber et al. (2015), DOI 10.1086/678982; Heiling et al. (2023), DOI 10.1002/ajb2.16158; Harder and Johnson (2008), DOI 10.1086/523364 (full text inaccessible).

Self-review: passed. Independent audit: not yet performed.
