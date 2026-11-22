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

# Reproducibility and limits

Run `python3 verify_matching_cap.py` with an ordinary Python 3 installation; no external packages are used. The checker directly loops over all integer edge vectors in the stated finite sample graphs and dilations, filters degree inequalities and the odd-cycle blossom inequality, and compares exact counts with the proposed binomial sum. It also solves the alternating cycle equations in exact rational arithmetic for every missing-simplex vertex. The expected success message is `ODD_UNICYCLE_MATCHING_CAP_PASS 47 integer_dilations_cases; all simplex vertices exact`. Finite verification does not replace the determinant, vertex-integrality, and index-two lattice proofs. The public mathematical write-up states all hypotheses and remaining priority risks.
