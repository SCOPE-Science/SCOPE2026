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

# Verification and limits

Run `python3 affine_retracts_verify.py` with Python 3's standard library. The script independently enumerates group endomorphisms from generator images for the finite fields of orders \(3,4,5,7,8,9\), tests the homomorphism condition using the complete multiplication table, isolates every idempotent, verifies their left-regular-band multiplication, computes the ordered commutation counts, compares every graph degree with the formula, and checks disconnectedness or diameter. The expected final output is `AFFINE_RETRACTION_GRAPH_VERIFIED`; the complete tested cases and counts are printed by the script. These checks are finite and do not establish the theorem for unbounded field orders. The general proof is algebraic and appears in `RESULT.md`. The external literature and priority assessment are provisional; independent mathematical review has not been performed.
