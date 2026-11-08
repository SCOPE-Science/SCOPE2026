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

# Reproducibility and scope

Run `python3 verification/check_osculation.py` using Python 3.8 or later. The code uses only the standard library and constructs the Hasse matrices from exact binomial coefficients \(\prod_j\binom{e_j}{\alpha_j}\) for all monomial exponent vectors \(e\) and all multiindices \(\alpha\) with \(|\alpha|\le3\).

The script checks every order \(0,1,2,3\) for dimensions \(2\le n\le8\) and characteristics \(2,3,5,7\), and checks characteristic zero using exact rational elimination for dimensions \(2\le n\le5\). It separately tests the characteristic-two vanishing of all mixed quadratic rows and linear independence of the pure-square coordinates. The included `verification/output.txt` records the produced output.

These checks cannot establish the theorem for unbounded \(n\) and arbitrary fields. The written proof uses exact polynomial expansions and independence of distinct monomials to cover that domain, and establishes the inseparable degree by a rational function-field calculation. Ordinary second derivatives alone are not an adequate verification in characteristic two.
