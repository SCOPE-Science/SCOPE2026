---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The main argument reconstructs the Green diagonal of the bounded screened half-line and finite-path inverses; differentiating it yields the rank-one Nyström trace capture. The finite threshold proof uses a simple positive crossing derivative, a uniform exponential remainder, and an implicit local root; the separate global comparison excludes all other sites near each fixed limiting threshold.

The independent test implementation `checker.py` constructs finite combinatorial Laplacians over \(2\le n\le12\), exactly inverts them for four rational values of \(q\), checks the Green diagonal and every pairwise capture ordering, verifies root monotonicity and Rolle brackets using high precision, and tests the first finite-size exponential asymptotic at seven path sizes. Execute `python checker.py` with SymPy and mpmath installed; its captured output is in `checker_output.txt`.

These finite tests do not certify all integers, all real screenings, or generalizations to nonuniform path parameters. Infinite-volume statements are justified analytically in `RESULT.md`. The trace of the infinite Green operator is not finite; only the rank-one trace capture is compared. Independent mathematical audit is not performed.
