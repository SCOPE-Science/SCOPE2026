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

Execute `python verify.py` with Python 3 and SymPy. The script checks exact polynomial identities and small-case quotient dimensions for \(2\le n\le10\). It does not establish the theorem by finite enumeration.

General proof checks: derive \(R=\frac{n+2}{2}G-\frac z2G_z\) by weighted Euler identity; prove the scalar intersection ideal using normal monomials of \(xy+R\); prove \(G_n,G_{n,z}\) coprime off the origin by the ODE and positive endpoint coefficients; apply the graded complete-intersection Koszul resolution; reduce modulo \(w\) for the first layer. These steps justify the all-parameter formulas independently of script output.

Limitations: higher nilradical-power quotients, their representation decompositions and the filtered arc-space series are not determined. No independent audit has been performed.
