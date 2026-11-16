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

Run `python3 verify_direct.py` and `python3 verify_coefficient.py` from the extracted directory. Both checks completed with all assertions satisfied. The first checks 4096 edge orientations, 38 balanced states, 144 rational covariance identities, the explicit cycle projector and the 24-state complete-graph baseline. The second independently computes coefficients of twelve-edge signed generating polynomials with degree-two caps and verifies all 144 entries. Exact integer and rational arithmetic is used throughout. The finite case is exhaustive; the programs are not a general-graph checker. No independent external audit has been performed.
