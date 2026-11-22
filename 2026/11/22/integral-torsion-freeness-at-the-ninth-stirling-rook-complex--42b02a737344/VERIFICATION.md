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

# Exact reproducibility and limits

Run `python3 stirling9_verify.py` in the same directory; no non-standard packages, external datasets, solver licenses or network calls are needed. `stirling9_check_output.txt` records a completed run of the packaged source. The program independently enumerates the augmented face poset and checks its Stirling-number face counts, constructs a deterministic vertex-priority matching, and exhaustively verifies the absence of directed alternating cycles over all Hasse edges. It computes signed integral Morse differentials, verifies adjacent compositions vanish, and applies only unimodular row/column operations at unit pivots. Residual zero matrices, rather than finite-field rank equality, certify the absence of torsion. The eight-row published Betti table supplies an external control.

The algorithm checks exactly the displayed finite complexes and does not certify an infinite family. The full homotopy type of the nine-row complex and publication priority beyond inspected sources are not established. An independent audit has not been performed.
