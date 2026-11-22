# Self-review

## Correctness

PASS. In the standard pair-rate-one Kingman topology, a designated leaf avoids mergers with probability \(2/[n(n-1)]\); the events for distinct leaves are disjoint for \(n\ge3\). Conditional on this event, the remaining \(n-1\) leaf-merger topology is again uniform Kingman. The singleton-stage expectation \(m(m-1)/(n-2)\) and independent exponential waiting times yield the exact conditional mean and covariance. A coupled rescaling of waiting times shows that the rest of the external length differs from a standard \((n-1)\)-sample external sum by a nonnegative term of mean \(4(H_n-3/2)/(n-2)\); the latter concentrates at two, while the surviving leaf has the full nondegenerate Kingman height. Complete exact enumeration through seven leaves corroborates, but does not establish, the general proof.

## Originality

PASS under the inspected evidence, with historical priority qualified. Janson and Kersting's full-text treatment derives unconditional limit and long-edge behavior, not the basal-singleton conditional total-length result. Reppell and Zöllner's full HTML treatment gives conditional single-branch length construction and branch-count algorithms, not the stated aggregate event conditioning. The closest plausible unresolved source is Disanto and Wiehe (2020), which explicitly studies the longest external edge in relation to root balance; only its abstract was accessible, and the full article could still contain relevant formulas. Search and implication comparisons are recorded in AUDIT.json. No claim of exhaustive uniqueness or independent certification is made.

## Value

PASS. The basal singleton is a natural maximally asymmetric genealogy, a rare topology of probability order \(1/n\). The theorem quantifies a previously unchecked statistical consequence: despite unconditional concentration of total external length at two, conditional root asymmetry leaves an order-one random coalescent-height contribution. This is pertinent to unusually large pendant mutation burden and demonstrates why an unconditional Gaussian approximation can overlook structurally defined rare subsets. Both an exact finite-sample dependence and the full non-Gaussian conditional limit are supplied, not merely a normalization check.

## Limitations and closest literature

The single-lineage survival rule and ordinary external-length variance are established background; the full conditional aggregate law is the assessed claim. The strong comparison risk is the inaccessible full 2020 article about longest branches and root balance, which is distinguished from the present total-branch statistic only at abstract level. The 2021 coalescent covariance compendium was not fully accessible and is another weaker residual source risk. No results are claimed for non-Kingman merger rules or other rare root splits.

Self-review: passed. Independent audit: not yet performed.
