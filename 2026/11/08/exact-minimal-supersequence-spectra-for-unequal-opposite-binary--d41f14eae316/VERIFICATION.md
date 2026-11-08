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

# Reproducibility and verification

The theorem is proved symbolically in `RESULT.md`. The self-contained program `verification/verify.py` implements subsequence membership, coordinate-by-coordinate deletion minimality, direct word enumeration, central-run constructive generation and the analytic binomial formula. It exhaustively checks all binary words of the candidate lengths for all 16 ordered parameter pairs with \(1\le a,b\le4\), independently checks merging/interleaving enumerations for four larger asymmetric pairs, and reproduces the exact length frequencies.

Run with `python3 verification/verify.py`. Expected output begins `OPPOSITE_RUN_MCS_VERIFY_OK`. The verifier also checks diagonal parameters for boundary sanity but these are outside the stated novelty claim.

The finite computation cannot prove the result for all parameter values; the proof is combinatorial. Bibliographic completeness and independent mathematical auditing have not been established.
