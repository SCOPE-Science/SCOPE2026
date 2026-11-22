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

The character-coefficient formula, rational adjacent-index difference, and continuous derivative numerator were symbolically simplified and checked for equality in exact arithmetic. The standalone `su2_resolvent_checker.py` requires only Python's standard library and ran successfully with 3,748 exact-rational assertions. Run it from the directory containing this file and `RESULT.md` using `python su2_resolvent_checker.py`.

The checker probes rational masses, consecutive-index polynomials, positivity threshold examples, and transition sign brackets. It is a supplementary reproducibility test, not an infinite proof: all-parameter coverage comes from the signed coefficient criterion, Descartes' rule and strict unimodality in `RESULT.md`. No independent mathematical audit or independent validation has been performed. Literature-priority assessment is provisional.
