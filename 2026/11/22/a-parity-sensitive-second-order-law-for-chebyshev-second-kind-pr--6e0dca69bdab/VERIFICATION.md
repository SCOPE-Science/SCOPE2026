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

# Reproducibility and scientific limits

The finite verification is a standalone Python 3 standard-library script `checker.py`, executable as `python3 checker.py`. It independently computes the exact rational coefficient of \(\pi^{-2}\) in the midpoint curvature in two ways for the first 100 cutoffs, then checks 56 finite Parseval/tail residual pairs, 10 sampled asymptotic and odd-parity differences, and 6 dense finite-grid probes. The curvature identity and asymptotic supremum have analytical proofs in `RESULT.md`; no finite test is claimed to establish those infinite statements.

The scientific scope is ordinary real distributional bounded variation in the open interval under the normalized semicircle weight. One-sided endpoint limits are constants and have zero residual. The proof of the two-term asymptotic includes endpoint exclusion and a uniform summation-by-parts expansion, so no numerical grid or finite cutoff stands in for a supremum certificate. Exact global finite-cutoff extremizers, apart from the local midpoint classification, remain unclassified.
