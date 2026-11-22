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

The theorem is proved by finite-character duality, an exact binomial-valuation lemma, integer polynomial division, and compact-group Haar disintegration; the attached `check.py` is a supplementary finite diagnostic, not a replacement for the general proof.

Run `python3 check.py` from the directory containing this file. The standard-library-only program independently checks polynomial division, kernel-projection cardinalities, and decoder congruences. The expected diagnostics are 2,457 divisibility-index tests, 222 finite-kernel tests, and 1,026 decoder tests.

The tests do not exhaust unbounded parameters, and no external independent audit has been performed. Prime-power ring alphabets must not be confused with finite fields of the same cardinality.
