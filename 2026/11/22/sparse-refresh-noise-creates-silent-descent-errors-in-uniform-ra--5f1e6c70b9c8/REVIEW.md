# Review of sparse-refresh descent noise

## Correctness — PASS

The cross-covariance decomposition uses only the same-site and adjacent-site dependencies of two coupled independent-score rankings; its finite formulas were also checked by exhaustive exact arithmetic. A solitary interior refresh creates marks \((0,0),(1,1),(-1,1),(0,2)\) with respective probabilities \(1/2,1/6,1/6,1/6\), independently across disjoint three-site neighborhoods. Removing nearby refresh pairs costs at most \(2p+2np^2\), and categorical-to-Poisson approximation and rate adjustment give the stated total-variation bound. Higher joint cumulants of the bounded one-dependent descent-difference array are \(O_r(np)\), establishing the Gaussian large-refresh regime. The exact checker passed 49 assertions; the proof establishes the infinite limit separately.

## Originality — PASS, with residual risk

The nearest full-text primary comparisons are Borodin–Diaconis–Fulman (2009), sections 2 and 5, and Chatterjee–Diaconis (2016), Theorems 1.1 and 1.2. They treat descent patterns and normal limits for single permutations, including inverse-descent couplings, but not the independently refreshed score-ranking pair or its joint signed/disagreement Poisson marks. Published research record searches and exact-phrase literature queries identified no direct covering theorem. Standard Skellam and local Poisson/normal approximation tools are acknowledged; originality is attributed to the explicit two-ranking model and joint conditional-mark constants. An equivalent result embedded in a general noise-sensitivity or local-statistic theorem may exist beyond inspected records.

## Value — PASS

Descent count is a widely used coarse ranking diagnostic. The theorem quantifies how independent small edits change local comparisons, proves a critical \(np\) transition, and identifies the nonvanishing chance of undetected local ranking errors when the coarse total remains fixed. The finite covariance and quantitative critical-window bound calibrate comparisons of replicated or repaired rankings, rather than merely restating a one-sample Eulerian law.

## Limits

The ranking scores must be independent and drawn from a common atomless distribution, replacements are independent by position, and the Gaussian regime has no claimed convergence rate. The historical priority assessment is limited to the inspected accessible literature and records; no external independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
