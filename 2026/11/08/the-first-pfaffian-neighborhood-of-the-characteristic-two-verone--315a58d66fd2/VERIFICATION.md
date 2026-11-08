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

The standalone script `verify.py` implements sparse exact polynomial operations over \(\mathbb F_2\). It constructs the odd alternating matrix, its maximal principal Pfaffians, and the polynomial \(F=Q(w)\) without invoking a computer algebra library. It confirms \(Bw=0\), every derivative \(\partial F/\partial a_i=w_i^2\), and every derivative \(\partial F/\partial b_{ij}=w_iw_j\) in orders \(3\), \(5\), and \(7\). Actual recorded output is in `verification_output.txt`.

Reproduce with `python3 verify.py` from this directory. No external packages are required.

The source of the all-dimension argument is the general Pfaffian kernel identity and formal chain rule, provided in RESULT.md. The checker tests three matrix orders, not an infinite family. The transverse length \(4\) is established by the alternating Schur-complement local form and the explicit quotient of three transverse variables by their squared maximal ideal; it is not inferred from the finite symbolic checks.
