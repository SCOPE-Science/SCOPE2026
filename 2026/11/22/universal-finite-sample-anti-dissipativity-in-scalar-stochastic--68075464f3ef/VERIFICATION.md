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

# Verification scope

Run `python verify.py` after extracting this package. It uses Python standard-library `fractions.Fraction` and `itertools.product` and checks finite exact-rational consequences: \(G=9/2\), \(H=-1/2\), population \(\lambda=-1/9\), the Richardson stability boundary \(h=18\), the continuous event's algebraic minimum pointwise ratio \(1/3\), and fitted-generator lower bounds on exhaustive *finite* rational test grids. These tests supplement, but do not establish, the measure-theoretic all-sample-size proof in RESULT.md. No independent audit or validation has been performed.
