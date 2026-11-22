# Scientific assessment

## Correctness

PASS. The graph distance is the coordinatewise maximum. Allocating three pairwise distances to maximizing coordinates bounds the perimeter by twice the largest coordinate span plus the second-largest span, and an explicit three-vertex construction attains that bound. In the unique-longest regime, equality forces exactly two opposite-endpoint pairs in that coordinate; the other pair must be diametral in the remaining product. The count follows from an ordered-pair complement. In the tied-longest regime, a three-event inclusion-exclusion count per coordinate gives an exact exhaustive enumeration of diametral triples. The limiting law follows from all joint absence probabilities and conditioning on distinct points. All dimensions \(d\ge2\) and path orders \(q_i\ge2\) are covered. The independent finite checker corroborates the claim, but does not substitute for proof.

## Originality

PASS under the accessible-source comparison; historical priority remains provisional. Hak and Kozerenko (arXiv:2611.17259v1) establish general triameter inequalities and characterize extremal graphs under packing/connectivity hypotheses, but do not calculate these strong-product extremal triples. Bujtás et al. (arXiv:2510.02749, DOI 10.1007/s00026-026-00814-0) give the Chebyshev distance identity on strong products and results on packing domination, not a triameter optimizer census. Searches for king-graph triameters, Chebyshev maximum-perimeter triples and exact strong-product triametral counts did not identify a covering formula. The distance identity and inclusion-exclusion are standard and not claimed new. Unindexed equivalent geometric counting results remain a residual priority risk.

## Value

PASS. The triameter is a natural three-terminal distance invariant. The theorem solves both the extremal value and **every** maximum-triple count for a broad two-parameter-and-beyond family of king-grid networks, including a sharp transition when the two largest side lengths become equal. Its uniform-power corollary identifies the exact quadratic dimension scale on which a random triple shifts from almost never to almost always maximizing total pairwise distance, and a full limiting binomial defect law. This is a motivated structural census and scaling phenomenon, not a selection of arbitrary small graph cases.

## Literature and remaining limits

The closest inspected papers are arXiv:2611.17259v1 and arXiv:2510.02749 / DOI 10.1007/s00026-026-00814-0. Their contributions and the nonimplication of the claimed exact counting formulas are explained in `RESULT.md` and the structured assessment. Some geometric literature may use different terminology for Chebyshev-diameter triangles; independent literature priority review remains necessary. No claims are made outside finite path strong products.

Self-review: passed. Independent audit: not yet performed.
