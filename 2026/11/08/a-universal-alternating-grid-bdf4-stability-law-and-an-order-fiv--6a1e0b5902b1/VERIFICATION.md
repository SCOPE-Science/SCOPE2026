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

Execute `python3 verify.py` with standard Python 3; there are no external library dependencies. The separately reconstructed Lagrange derivative weights, homogeneous BDF difference transfers, exact BDF4 Floquet polynomial, four positivity identities, and exact BDF5 quartic at selected rational arguments are checked with rational arithmetic. The recorded actual program output is `PASS 169 exact rational assertions` (also embedded in `verify_output.txt`).

The universal claim for all \(r>0\) is certified analytically by the rational polynomial formula and strictly positive Jury numerators in `RESULT.md`. Rational checks at finitely many ratios are confirmatory, not an exhaustive scan or a proof of all-ratio stability. At \(r=10\), the exact determinant sign gives an infinite-time instability proof through the intermediate-value theorem, not a finite-iteration simulation. All scientific claims remain subject to independent specialist review; none has been independently audited.
