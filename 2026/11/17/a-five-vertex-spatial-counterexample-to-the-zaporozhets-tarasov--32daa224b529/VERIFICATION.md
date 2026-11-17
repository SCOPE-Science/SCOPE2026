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

The standalone `CHECK.py` was run with Python 3 from the same contents embedded in this finding. The output verified all six support-plane signs, exact squared facet areas, axial CDF and Gini identities, root isolations, and the strict rational margin \(\(31158/4375\)\). It uses exact fractions and no random sampling.

The proof is analytic: the script is a reproducibility aid for its finite rational identities and determinant checks. The supporting inequality is derived in the text from projection and the Euclidean triangle inequality; no incomplete enumeration is used to infer an infinite assertion. Independent audit has not been performed.
