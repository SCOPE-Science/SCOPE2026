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

# Reproducibility

In a directory containing both `RESULT.md` and `CHECK.py`, run `python3 CHECK.py` (Python 3.10 or newer recommended). The checker uses only the standard library for exact combinatorial assertions on odd sizes \(N=3,5,7,9,11\). If NumPy is installed, it additionally builds the full symmetric parity-sector generator and checks the first-order low spectral eigenvalues at positive weak-bond rate \(\varepsilon=10^{-4}\) for \(N=3,5,7\). During preparation, 240 exact finite assertions and 18 floating-point spectral and slow-coverage comparisons passed.

The analytical proof of the arbitrary fixed odd ring length and the perturbative \(\varepsilon\downarrow0\) limit is in `RESULT.md`. The finite checker does not certify arbitrary lengths or control the remainder uniformly in system size. Stationary-state claims assume the initially empty, even-original-occupation sector. Scientific comparison with the 1994 defective-bond diffusion paper was limited to its accessible abstract.
