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

# Verification of the coefficient certificate

Run `python3 verify.py` with a standard Python 3 interpreter. The script calculates the exact rational degree-39 polynomial from the logarithmic derivative of the generating function, checks that the constant coefficient has \(\nu_5=5\), the next two coefficients have \(\nu_5=4\) with normalized residues 3, and all higher-degree coefficients have valuation at least 6. It also performs an independent finite Euler-product construction for eight tuple orders, compares integer counts, and tests both simple-root branches through modulus \(5^8\).

The all-index statement follows from the exact rational coefficient certificate and Hensel's lemma. Finite comparisons are supporting checks, not substitutes for the algebraic proof. No human or external independent audit has been performed.
