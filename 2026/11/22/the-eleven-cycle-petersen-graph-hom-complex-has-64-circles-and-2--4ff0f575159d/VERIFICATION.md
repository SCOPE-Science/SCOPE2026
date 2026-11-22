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

Run `python3 verify.py` (standard-library Python 3.9+). The checker reconstructs the Petersen graph as disjoint pairs of two-subsets of five labels. It independently calculates all labeled length-eleven closed walks and one-coordinate Hom adjacencies, then counts the 50 subset-neighborhood transfer states and all closed mask transitions with degree weights. It asserts exactly the component-size distribution, complete CW-cell vector, and Euler characteristic described in RESULT.md. Expected output is in `expected_output.txt`.

The universal point-or-circle constraint is Theorem 1.2 of Fujii–Kimura–Nozaki (arXiv:2412.19039), not a consequence of sampling. This checker does not claim to reprove that published theorem, certify publication priority, or provide an independent audit.
