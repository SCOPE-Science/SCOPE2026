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

# Reproducible exact calculations

Execute `python3 check.py` with Python 3 (standard library only) from the directory containing this file. The program performs exact fraction-field arithmetic in \(\mathbb Q(\sqrt{3/7})\), enumerates all 56 ambient monomials of total degree at most five, verifies the normalized mass, tests the precise nonzero sixth-degree Legendre obstruction, and checks the quadratic-harmonic eigenvalue sector formulas at the unique tight radius, and checks the general-radius eigenvalue, trace, difference, and Legendre obstruction formulas by exact rational-polynomial coefficient comparison.

The entire two-sector general-radius factorization, equality iff \(0<t<1\) and \(7t^2-3=0\), and maximal exact cubature order are established in RESULT.md by polar moment integrals and invariance. The checker is an exact finite verification of the critical computations; it is not a separate proof of any infinite-dimensional claim.

Expected terminal marker: `ALL_OCTAHEDRAL_CAP_CUBATURE_CHECKS_OK`.
