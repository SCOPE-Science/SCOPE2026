---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

`python check.py` with the NumPy dependency specified in `requirements.txt` verifies 146 finite spectral, sign and normalization checks. It also implements the local Kraus adjoint action on \(n=3,4,5\) qubits and compares it against the pair decay matrix. The computation passed on the supplied source. The all-size proof is the block diagonalization and exact ring comparison; the checker is diagnostic rather than a replacement for the proof.

These checks concern the pair-projector sector. The equality of its lowest rate with the Liouvillian gap for the specified connected SWAP measurement-feedback protocol follows from arXiv:2611.13094v2, Eq. (78), not from the finite tests. The absorber-fraction bound is \(2\lambda/n\) for trees with feedback on every edge, whereas it depends on the number of feedback edges in general. No per-site measurement capacity is imposed; a hub carries many independent Poisson measurement clocks. The comparisons do not establish absolute priority.
