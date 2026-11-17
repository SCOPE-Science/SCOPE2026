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

The mathematical proof is self-contained in `RESULT.md`, including the exact one-cell Fourier certificate and infinite-dimensional equality analysis. The Python 3 / NumPy source `check.py` was executed from the extracted final package, and all reported finite diagnostic assertions passed. Checks cover exact basis moments, a rigorous sign-certificate numeric margin, finite Fourier test vectors, uniform-mesh cell orthogonality and sharp normalized ratios, and random positive-mesh witnesses. Numerical testing does not establish the infinite theorem or publication novelty.

The earliest motivating preprint version is arXiv:2611.10371v1, publicly submitted 2026-11-07 UTC. The prior comparison was limited to accessible full primary text and retrieved scholarly records; possible older equivalent formulations remain a scientific limitation. The boundary between a derivative-seminorm statement and the full \(H^1\) statement is intentional and explicitly addressed in the proof.
