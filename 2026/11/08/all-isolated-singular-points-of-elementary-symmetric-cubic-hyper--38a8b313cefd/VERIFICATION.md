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

The file `verify.py` is a stand-alone Python 3 standard-library enumerator. It checks every point of \(\mathbb P^{n-1}(\mathbb F_3)\) for \(3\leq n\leq11\), evaluating the original cubic and its first derivatives, and compares with an independently generated set of support, signed-bipartition and boundary-partition points. It tests \(43\) geometric predictions for \(n=8\), \(34\) prime-field points on the positive-dimensional \(n=11\) boundary, and prints `CERTIFICATE_OK` on success.

These finite checks do not establish the absence of extension-field singularities or prove the all-\(n\) result. The proof of exhaustive geometric classification is the quadratic common-root argument followed by characteristic-three binomial coefficient identities in `RESULT.md`. The claim concerns reduced support, not the primary structure of the singular scheme.
