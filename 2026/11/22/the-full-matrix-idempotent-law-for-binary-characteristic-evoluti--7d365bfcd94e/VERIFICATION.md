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

# Reproducible verification

The standalone `verify.py` computes the predicted full-matrix law using exact rational Gaussian-binomial inversion and separately exhausts all structure matrices and all nonzero vectors over small binary finite fields. It uses polynomial presentations \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\), each with explicit multiplication, and checks each histogram exactly. The matrix totals over seven parameter pairs sum to 70,422. The program output is reproduced in `verification_output.txt` and ends `VERIFY_OK`.

Use `python3 verify.py`. No external package is required. The computations verify finite cases, not the general theorem. General correctness rests on the proof of the independent-fixed-vector lemma, exact uniform matrix-frame constraints, Gaussian inversion, and the limiting summability estimate.
