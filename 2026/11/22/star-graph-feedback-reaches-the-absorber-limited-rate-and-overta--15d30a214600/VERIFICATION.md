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

`python check.py` with the NumPy dependency specified in `requirements.txt` verifies 146 independent finite spectral, sign and normalization checks. It also implements the local Kraus adjoint action explicitly on \(n=3,4,5\) qubits and confirms its equality with the pair-graph generator for every singlet-pair projector. The computation passed on the supplied source. The mathematical proof is finite-dimensional block diagonalization and an all-integer-order inequality; the checker is diagnostic rather than a replacement for the proof.

The statement is about the exact pair-projector invariant sector, not an unconditional equality with the full Liouvillian gap. No per-site measurement capacity is imposed; a hub carries many independent Poisson measurement clocks. Originality remains subject to independent literature assessment.
