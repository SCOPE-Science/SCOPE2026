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

Execute `python3 verify_windmill.py` using Python 3's standard library from the directory containing the script. This independently enumerates all functions from each tested graph vertex set to its vertices plus an undefined symbol; it tests idempotence and checks every singleton and edge inverse image as a face. The expected final line is `VERIFY_OK`.

Compared parameters are the nine blade-size tuples `(1,)`, `(2,)`, `(1,1)`, `(2,1)`, `(2,2)`, `(1,1,1)`, `(3,1)`, `(2,2,1)`, `(2,3)`. The full output is stored in `verification_output.txt`.

Finite exhaustive enumeration verifies the stated instances only. Generality over all integers is supplied by the case-split proof. The asymptotic rank law is derived analytically from nonnegative coefficient domination and the classical iid central limit theorem, not inferred from histograms. The same-model correctness, originality and value assessments appear in `REVIEW.md` and `AUDIT.json`; no independent audit has been performed.
