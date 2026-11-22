# Mathematical review

## Correctness
PASS. For exponential pairs, the normalized absolute difference is uniform, giving single-matching variance \(1/(6N)\). The projection integral is derived by splitting at the conditioning variable, and its variance \(\zeta\) is positive and strictly below \(1/24\). Conditional expectation over matching designs is exactly the complete pair U-statistic, whose covariance follows by counting shared-index edges. Total variance yields the finite-\(B\) law. The fixed-\(B\) CLT follows from a bounded-degree dependency graph, with overlapping edges of separate matchings negligible in proportion, and the diverging-\(B\) CLT from the U-statistic projection and an \(L^2\) bound. The original numerical computation and matching enumerations passed 54 reproducibility checks. Boundary \(N=2\) has zero reducible variance; all positive claims of strict gain begin at \(N=4\).

## Originality
PASS with residual priority risk. Section 3.2 and equation (12) of Karagrigoriou et al. (2023) employ 50 data permutations; they do not provide this exact \(B\)-dependent covariance/variance and its explicit integral constant. The earlier 2021 thesis includes simulation analysis but no such theorem in the material inspected. Generic U-statistic, Rao–Blackwell, and dependency-graph results cover the techniques, not the quantitative calculation tied to this exponential kernel. The 2022 book-chapter predecessor was identified bibliographically but not inspected in full. Relevant research-record searches for the ratio kernel, incomplete U-statistics, and matching variance found no directly dominating claim. An independent historical-priority check remains important.

## Value
PASS. This test uses random pairings, with the original implementation recommending 50. The exact variance floor and 50-pairing savings quantify a real calibration and computational design decision: 50 pairings achieve 98% of the maximum pairing-driven reduction, yet most sampling variance remains. The 19.66-fold hypothetical underestimation demonstrates that repeats of one dataset cannot be modeled as independent datasets. The precise object is a naturally studied zero-threshold baseline of the published test, not an arbitrary parameter slice. Positive-threshold test power is not addressed.

## Limits and closest literature
Karagrigoriou et al., Risks 2023, 11, 169, equations (10)–(13), and Papasotiriou's 2021 thesis are the primary comparisons. The older 2022 book chapter was not inspected; a synonymous normalized pair-difference U-statistic could exist elsewhere. Computations support, but do not replace, proof. Statistical conclusions for adaptive or positive thresholds are unproved.

Self-review: passed. Independent audit: not yet performed.
