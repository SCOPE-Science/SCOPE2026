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

# Reproducible verification

Run `python3 artifacts/verify.py` from the root of the extracted package. It requires only Python 3 and its standard library and uses exact fractions throughout.

Observed successful output:

`SPLIT_TREE_COVARIANCE_CHECKS_PASSED profiles=64 trees=20219 enumerated_entries=1565`

The checker independently enumerates all labeled spanning trees for nine small graphs (20,219 total tree instances) and compares the exact edge-incidence covariance matrices entry-by-entry against a matrix computed from the split-graph Laplacian pseudoinverse (1,565 entries). For 64 profiles \(2\le p,q\le9\), it separately checks the complete predicted spectral trace and squared trace against direct covariance calculations, together with exact signs and determinant identities governing the transition.

The **infinite-family proof** consists of the symbolic projection decomposition and the displayed strict rational inequalities in `RESULT.md`. Finite enumeration, matching two spectral traces, and printed success are independent corroboration, not a substitute for a proof of completeness. No independent mathematical audit is available; no external certification is claimed.
