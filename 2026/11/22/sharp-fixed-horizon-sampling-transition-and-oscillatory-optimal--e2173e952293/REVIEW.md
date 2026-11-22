# Review: sharp pinned-rotation frame sampling

## Correctness — PASS
The explicit Cauchy–Binet determinant and derivative sinusoid are valid for every positive damping, frequency and horizon; strict amplitude inequality prevents degenerate stationary points. The endpoint sign change gives the exact threshold, period decay confines the global optimum to the first rotation, and a uniform implicit expansion produces alternating long-horizon deviations. The independent Python diagnostic checks 382 finite examples, not the universal theorem.

## Originality — PASS, qualified
The published equal-spaced oscillator calculation uses times 0,h,2h and does not optimize an independently free third event at fixed terminal time. Pinned two-real-exponential and pinned Jordan-frame results were inspected in full and have different regression families, thresholds and nonoscillatory limiting behavior. The 2026 semigroup-frame paper and 2017 complex OU design article have different mathematical objectives. Older specialized optimal-design literature may implicitly contain an equivalent theorem, so publication priority is not guaranteed.

## Mathematical value — PASS
This complete classification specifies exactly when independent endpoint replication is optimal, proves uniqueness and global first-rotation localization for arbitrarily long horizons, and identifies an infinite oscillatory sign reversal invisible to finite-horizon or real-mode analogues. It is a natural sensor-placement invariant with directly motivated experimental meaning, not an arbitrary numerical sample.

## Limitations and closest work
The result has three equal-variance independent scalar events, two fixed endpoints, known stable planar rotation, and determinant rather than E-optimal or unknown-frequency objective. Full closest inspected records: equal-spaced oscillator frame (2026/11/2), pinned exponential pair (2026/11/8), pinned Jordan regression (2026/11/2); see RESULT.md for identifiers and source comparison. A broader published exact-design theorem may imply it.

Self-review: passed. Independent audit: not yet performed.
