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
# Reproducibility and independent validation status

The included `verify.py` was run with Python 3 and SymPy from the supplied source path and reported symbolic agreement of the nondegenerate Taylor coefficients, exact thinning coefficients, and 2,376 exact-rational test triples. Example leading-order coefficients were checked exactly. The mathematical proof in RESULT.md supplies the quantifiers that a finite checker cannot certify. Independent mathematical audit has not been performed, and no global weak convergence, coupled-reaction generalization or practical efficiency result is claimed.
