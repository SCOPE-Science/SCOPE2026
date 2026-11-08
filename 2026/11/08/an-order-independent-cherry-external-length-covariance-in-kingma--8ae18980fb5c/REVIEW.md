# Scientific review: cherry count and external branch length

## Correctness

PASS. The claim specifies the standard pair-rate-one Kingman genealogy, a fixed sample size \(n\ge4\), and exact definitions of cherries and total external length. Counting survival of labeled singleton lineages gives explicit factorial moments. A forward recurrence for past cherries and backward recurrence for future cherries yield the all-epoch covariance profile; independent exponential waiting times then make the weighted sum exactly \(-2/9\). The special orders \(n=2,3\) are excluded from the constant law and handled separately. A separate rational dynamic-programming computation for \(2\le n\le30\), and exhaustive merger histories through eight leaves, agree. The finite checks are not the proof; the algebraic recurrences establish the infinite family.

## Originality

PASS with residual historical-priority risk. Janson–Kersting (arXiv:1004.5011) treats external branch length and singleton-lineage dynamics without cherry-count mixed moments. Disanto–Wiehe (arXiv:1112.1295) treats topology-only cherries and pitchforks without continuous branch lengths. Alimpiev–Rosenberg (arXiv:2103.13467) treats correlations among six coalescent length/time statistics, omitting the cherry count. The 2020 Disanto–Wiehe discrete external-rank paper is relevant but its available material does not establish the continuous-time mixed law. Blum–François (2005) treats a marked-leaf minimal clade and associated branch, while François–Mioland (2007) studies total cherry *height* and total external length; neither is the present unweighted cherry count, but their full texts were unavailable for a decisive implication comparison. The present exact epoch-indexed covariance is not implied by any marginal distribution alone, and the weighting-to-constant argument is a separate structural step. Potential implicit coverage in additional historical joint-distribution papers cannot be ruled out without independent expert review.

## Value

PASS. Cherry count is a standard gene-tree balance/shape statistic, while total external length controls the expected number of singleton mutations under a constant-rate mutation model. Their mixed covariance is a natural required input for joint shape/sequence summaries. Its exact constancy across all \(n\ge4\), despite changing individual marginals, is structural and non-obvious; the stagewise sign law identifies its mechanism. No downstream theorem is required to motivate the exact joint invariant.

## Limits and assessment

Only neutral binary Kingman mergers and the specified rate normalization are covered. The result does not provide the full joint law, extend to multiple-merger coalescents, or certify historical uniqueness. Source inspections and exact tests are documented in AUDIT.json and VERIFICATION.md.

Self-review: passed. Independent audit: not yet performed.
