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

# Verification and limits

Run the accompanying standalone Python 3 program `verify_path_fibre_spread.py`. It uses only the standard library (`fractions.Fraction`) and exact integer enumeration. The observed final marker on replay was `ALL_PATH_FIBRE_VARIANCE_CHECKS_OK`.

The program checks two metric geometries (within-fibre distance one or two), fibre sizes two and three, and lengths three through five as specified in its finite case table. Each profile is normalized by pinning its first value to zero. It checks the analytic deficit decomposition for every enumerated profile; it also checks unbalanced conditional atomic probabilities for three and four fibres. Finally, a two-layer complete-bipartite metric realizes variance \(1/2\), greater than the two-index baseline \(1/4\).

The exact summation and equality arguments in `RESULT.md` are the infinite-family proof. The finite checker does not certify all real-valued functions, all dimensions, all conditional measures or novelty in unindexed literature. Independent mathematical review has not been performed.
