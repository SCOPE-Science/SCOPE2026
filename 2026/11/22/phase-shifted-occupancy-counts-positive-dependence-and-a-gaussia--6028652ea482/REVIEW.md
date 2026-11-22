# Scientific review

## Correctness
**PASS.** Exact bin-union enumeration proves the covariance formula; a binomial expansion proves its sign, equality cases and unique minimizer. Independent quarter-cell membership proves the exceptional independence. Poissonization with independent elementary Poisson cells gives a cyclic one-dependent CLT for each fixed collection of phases; a sequential-addition martingale and vacancy-concentration argument handles the fixed-size correction. The Fourier formulas and the phase-average spacing identity are analytic integrations. `verify_phase.py` passed 325 exact/numeric checks. Remaining mathematical limitation: functional tightness is not claimed or required.

## Originality
**PASS, subject to historical priority.** Scott (1985) studies density estimates and integrated squared-error risk of averaged histograms, not the joint number-of-nonempty-bin statistics. Barbour–Gnedin (2008) study occupancy-frequency CLTs in fixed-frequency schemes, not phase-indexed overlapping partitions. Searches for rotated-bin occupancy covariance, Gaussian phase kernels and half-bin independence identified relevant surrounding occupancy and histogram methods, but no exact covering statement. A broader general theorem for two overlapping partitions, or an earlier computation of this same statistic, remains a real residual risk; independent literature audit is not yet performed.

## Value
**PASS.** Two highly relevant uses are stability of the count of represented histogram categories under choice of grid origin, and variance reduction by phase averaging. The exact half-bin optimality, universal positive-dependence obstruction for at least three bins, and isolated two-bin independence exception reveal a structural boundary that a single-grid occupancy CLT cannot describe. The spectral kernel quantifies multi-phase uncertainty and yields the phase-average variance without arbitrary numerical simulation.

## Scope and limitations
The point model is uniform and circular; the finite-dimensional Gaussian law uses sample-to-bin ratio approaching a fixed positive constant. Positive covariance is not a statement of association or general independence. No functional convergence, nonuniform-density extension or general optimal-density-estimation claim is made. Only the stated case of independence is asserted; all independent-audit channels remain unperformed.

Self-review: passed. Independent audit: not yet performed.
