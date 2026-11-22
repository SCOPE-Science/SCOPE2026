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

Run `python CHECK.py` with Python 3 and SymPy from the directory containing this file. The checker exactly verifies one-dimensional convolution polynomials, Plancherel-derived radial integral coefficients, sphere moments and the normalized quartic formula. It does not stand in for the global real/complex inequalities; these are reconstructed in the proof, using the standard equality conditions in Cauchy–Schwarz and trace extremization. The stated theorem has not been independently audited or externally certified.
