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

# Reproducible checks
Run `python3 check_near.py`; no third-party Python modules are required. The program independently constructs quotient generators by all residue-pair combinations modulo the divisor, then computes Apéry representatives using shortest paths and reconstructs pseudo-Frobenius numbers without invoking the proposed record formula. It checks the Sylvester-coordinate model against this independent representation, and runs an exhaustive unit-residue census for the near-top rigidity statement over all moduli 5 through 100. The separate witness test uses moduli through 300.

The actual stdout is embedded as `verification_output.txt`. All assertions succeeded. Computation cannot establish the universally quantified theorem and is not evidence of absolute novelty or independent peer review. The proof is in `RESULT.md`.
