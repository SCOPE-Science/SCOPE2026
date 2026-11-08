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

# Verification and reproducibility

The proof establishes the all-parameter claim by exact integration, derivative signs, two-branch pushforward, and edge expansions; no numerical grid is used to conclude a universal statement.

To reproduce the finite checks, execute `python verify_shell.py` with Python, SymPy and SciPy installed. It verifies symbolic piecewise identities, branch derivatives, joins and stationary survival differentiation, then performs direct quadrature, CDF/density comparisons, limit coefficients and conditional fold-weight tests at six separated parameter triples. The script reports `PASS: 381 independent symbolic and numerical assertions` on successful execution.

The code uses no external data files, random seeds, private credentials or network services. The numerical checks cannot certify limiting exponents or publication priority independently of the analytical proof and source comparison.
