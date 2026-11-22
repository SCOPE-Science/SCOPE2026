# Scientific assessment

## Correctness — PASS
A window-maximizer changes exactly when the maximum of the enlarged \((k+1)\)-window occurs at one of its endpoints. The complete two-event enumeration has three feasible endpoint cases of rank weights \(1,2,1\); at lag exactly \(k\) a fourth, coincident-endpoint event contributes \(1/(2k+1)\). These prove the negative/positive covariance kernel, after which summation gives an exact harmonic variance. Strict Jensen gives a positive variance, making the standard bounded finite-dependence CLT applicable. The delivered standalone enumerator performs 76 exact assertions, including exhaustive orders through nine observations and complete cyclic permutations through nine positions. Computation is supplemental, not proof of the infinite result.

## Originality — PASS, qualified
Austin, Fagen, Lehrer and Penney (1957) fully own the linear total-count distribution; neither their known result nor the fixed-width CLT is treated as novel. The assessed distinction is the *entire lag-resolved covariance kernel* on the circle and its unique positive rebound, not a renaming of the total-count law. The faithful published 1957 mathematical restatement and the full Alon–Feldheim (2014) preprint provide relevant comparisons; the latter addresses uniform long-run probabilities rather than exact local covariances. Meaning-based published-result searches found related deterministic cyclic maximum-filter sensitivity and consecutive-pattern covariance results but no direct coverage of this precise joint-event law. The inaccessible full original 1957 paper is a material historical-priority risk, so this is same-model original-work assessment, not independently established priority.

## Value — PASS
The problem is to quantify how often a streaming maximum changes and how update events cluster as one advances the window. The positive rebound at the exact window length is not inferred from the known expected update count and is qualitatively opposite to the strictly negative covariances at shorter lags. The all-width exact variance and covariance are usable for uncertainty estimation, simulation validation, and dependence-aware calibration of cyclic moving-maximum summaries. This is a structural local-dependence law, not an arbitrary finite slice or a marginal expectation recomputation.

## Closest literature and limits
Austin et al. (1957), DOI 10.1214/aoms/1177706893: complete *linear* total-count distribution known. Full primary PDF unavailable; accessible complete theorem restatement examined. Alon and Feldheim (2014), arXiv:1402.1975: broader block-factor context, but no matching explicit pair kernel found in its examined theorems. Other possible general sliding-extremum formulas are a priority risk. No assertion of independent certification is made. A finite checker cannot establish the fixed-width CLT.

Self-review: passed. Independent audit: not yet performed.
