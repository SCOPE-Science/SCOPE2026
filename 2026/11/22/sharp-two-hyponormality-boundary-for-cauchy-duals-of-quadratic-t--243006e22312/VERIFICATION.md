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

The mathematical result rests on an exact analytic proof using shifted Hankel matrices, polynomial discriminants, and the unique signed Hausdorff density. The accompanying `checker.py` verifies the two Hankel determinant factorizations, the two discriminant identities, the one-hyponormal boundary substitution, the explicit rational example, and finite shifted blocks. These checks were actually executed with SymPy; the script is included for independent replay.

The infinite parameter range is not inferred from finite testing. Source comparison considered reciprocal-rational Hausdorff moments, Cauchy dual subnormality for two-isometries, signed Berger charges, toral three-isometries, and standard weighted-shift Hankel tests. Their general theorems and subject boundaries do not, as inspected, supply the exact one-variable two-hyponormality criterion. A complete historic priority search is not certified. Independent mathematical validation has not been performed.
