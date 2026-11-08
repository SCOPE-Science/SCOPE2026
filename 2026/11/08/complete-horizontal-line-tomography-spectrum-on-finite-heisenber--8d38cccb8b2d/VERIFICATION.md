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

The universal spectral theorem follows algebraically from exact incidence counts, central-character orthogonality, and the trace of a symplectic Fourier involution. No numerical computation is needed for the proof.

Reproducibility: install the NumPy dependency declared in `requirements.txt`, then execute `python CHECK.py`. The checker independently generates all distinct horizontal lines and an incidence matrix for the prime-field instances \((q,n)=(3,1),(5,1),(3,2)\); it checks the Gram multiplicities, null witnesses and all predicted eigenvalues. Expected final line: `CHECK_OK assertions=86391`.

The explicit characteristic-three and characteristic-five experiments are sanity checks rather than exhaustive tests of the infinite family of allowed prime powers. Exact rank formulas for all cases follow from the written proof. Independent external mathematical audit: not performed.
