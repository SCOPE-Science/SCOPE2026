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

The deterministic Python 3 standard-library checker in `VERIFY.py` evaluates the exact reduced-state recurrence and separately enumerates the full labeled-vertex matching process for small graphs. Its recurrence, transition, factorial-moment and error-inequality checks are finite corroboration, not an infinite proof.

The analytic proof in `RESULT.md` establishes the universal bounds by tracking the first two factorial moments and explicitly summing a nonnegative error. Reproduction command: `python VERIFY.py`. A complete run returns `VERIFY_OK 4287 checks`.

The 1991 primary full text was not accessible; priority is unverified. Independent scientific validation has not been performed.
