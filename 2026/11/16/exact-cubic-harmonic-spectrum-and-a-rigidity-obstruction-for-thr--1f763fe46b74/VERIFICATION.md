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

Run `python verify_unequal.py` with the dependencies in `requirements.txt` from the same extracted package. The checker verifies all 28 full-sphere and cap Gram pair products by symbolic exact integration; harmonicity and orthonormality; the six polynomial formulas and matrix-block trace; the strict nonisotropy polynomial identities; and four independent numerical cap integrations.

The symbolic assertions are polynomial identities valid for every real threshold in the claimed range. Strict positivity of the derivative and of the two eigenvalue gap factors is proved analytically in RESULT.md using interval signs. The independent numerical quadrature agreements (largest entry error below \(1.5\times10^{-15}\)) are corroborating finite computations, not a substitute for the proof or an independent external review.

All comparisons are self-review. Independent mathematical audit has not yet been performed. Bibliographic priority is conditioned on the inspected literature and may be affected by an unindexed equivalent treatment.
