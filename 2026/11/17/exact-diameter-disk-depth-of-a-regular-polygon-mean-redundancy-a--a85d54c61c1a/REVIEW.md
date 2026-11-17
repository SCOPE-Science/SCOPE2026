# Review of the diameter-disk depth theorem

## Correctness: PASS
The statement fixes every geometric convention, the boundary inclusion rule, and the uniform-area probability law. The first step is a closed-form disk–regular-polygon intersection: the only active supporting lines for a disk anchored at a vertex are its two adjacent sides, and their removed circular caps are disjoint. An explicit trigonometric factorization proves the nonadjacent-side claim for every integer \(n\ge3\). This yields the exact expected depth by indicator integration. Angular site counting supplies a sharp deterministic discrepancy, and total-variation comparison with the unit disk gives the stated quantitative CDF estimate. The variance follows from the limiting density. The independent numerical verifier compares the exact area with a separate clipping construction and tests the count law on sampled interior and exact boundary configurations. Analytic arguments, not numerics, prove the universal claim.

## Originality: PASS (subject to historical-priority risk)
Bose et al.'s 2025 full preprint and open conference version were examined at the section on diametral disks; those statements optimise the number of *input sites* in a selected disk and do not imply the continuous multiplicity of a fixed family of vertex-to-centroid disks. The relevant 2025/2026 extended algorithmic treatment likewise seeks suitable *pairs* of sites, not area means. The more general 1996 existence theorem does not itself provide an explicit overlap-area calculation. A published simplex result concerning the same Thales-ball defining inequality treats extremal gauges and contact counts for a different (simplex) family, not these regular-polygon area statistics. Search comparisons also distinguished random diameter-disk inclusion probabilities and circular-normal approximation inequalities from this claim. Residual risk: not all older primary sources on diameter disks were available in full, and semantic search cannot certify absolute priority.

## Mathematical value: PASS
This is a full, nontrivial all-\(n\) answer for a natural integral-geometric overlap statistic of an established disk-incidence model. The explicit mean quantifies the total coverage redundancy, the deterministic inequality is globally sharp, and the limiting depth law remains random with a computable variance. The boundary-clipping geometry and quantified disk approximation are reusable for regular-polygon geometric integration. This is not offered as a resolution of unrestricted disk-enclosure extremal questions, and no stronger general theorem is claimed.

## Limits and external validation
The full finite-size probability mass function and arbitrary-polygon extensions remain unresolved. The reproducibility checks are finite diagnostics, not a proof certificate. Historical novelty is assessed from available materials and remains subject to external scrutiny.

Self-review: passed. Independent audit: not yet performed.
