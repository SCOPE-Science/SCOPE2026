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

# Verification of the two-ring peak-count theorem

Run `python3 two_ring_check.py` using Python 3. The script uses exact rational and integer arithmetic; it prints `TWO_RING_MAXIMA_CERTIFICATE_PASS` if and only if all coded identities, signs, and example bounds hold. It does not numerically certify the infinite family. The proof of the infinite family instead uses the exact discriminant inequality, Descartes' sign theorem, the strict negative-ray angular Hessian, and the two-extremum analysis of \(B_n\).

The order-eleven witness yields four simple radial critical radii by four exact sign changes. For all larger orders, the two-turning-point construction produces four simple roots for sufficiently small positive \(a\). Stable roots and strict Hessian inequalities give an open parameter neighborhood. The universal ceiling is valid for all real \(0<a<b\), including parameters where critical points coalesce or become degenerate.

Unproved: the least degree at which the ceiling is attained, and global ordering of peak heights. Independent audit: not performed.
