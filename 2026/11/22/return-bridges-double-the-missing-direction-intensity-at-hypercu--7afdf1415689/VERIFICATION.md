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

# Verification record

Run `python3 verify.py` with standard-library Python 3. The independent finite-sample enumerator and exact rational coefficient calculations returned:

`PASS exact assertions: 482`

The checker evaluates all \(1\le d\le7\), \(1\le L/2\le8\), comparing coefficient and combinatorial counts, nonnegativity, exact first and second moments, and brute-force coordinate words for \(d\le4\) and \(L\le8\). Nine fixed-density constants are evaluated numerically as diagnostics. This is finite corroboration only; the displayed infinite conditional Gaussian and Poisson limits require the generating-function, conditioning and local-limit arguments in `RESULT.md`.

The exact bridge law is for even fixed \(L\) and one flip per step. The analytic claim does not include first-return conditioning, a finite-sample rate in either limit, or nonuniform coordinate probabilities. Scientific limitations and remaining literature-priority risks are described in `RESULT.md` and `REVIEW.md`.
