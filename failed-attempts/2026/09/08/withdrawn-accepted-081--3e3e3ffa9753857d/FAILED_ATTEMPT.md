# FAILED ATTEMPT — NOT A VALIDATED FINDING

This accepted record was withdrawn after the 2026-09-22 independent three-axis audit campaign was executed on 2026-09-26 UTC.

**Decisive reason:** the main Fibonacci star-discrepancy fractions are correct, but the record also claims an exact dual-lattice diagnostic for all nonzero dual vectors with `||h||_inf <= 12`. The committed verifier searches only `[-N,N]^2`, which truncates that box for (N=5) and (N=8). Consequently two published rows are false:

- N=5: correct hit count 124 and Q_12 = 3837623/415800 (~9.2294925445), not 24 and 5.126667.
- N=8: correct hit count 78 and Q_12 = 4418807/831600 (~5.3136207311), not 36 and 4.139484.

The exact star-discrepancy table itself independently rechecks, and the originality/scientific-value axes pass, but an accepted record with known false exact entries cannot receive a passing correctness verdict.

Evidence: `INDEPENDENT_AUDIT_2026-09-22.md` and `INDEPENDENT_AUDIT_2026-09-22.json`.

Legitimate retry condition: fix `spectral_witness` to enumerate `[-H,H]^2`, update the two affected rows and generated artifacts, and obtain a fresh independent three-axis audit of the corrected package.
