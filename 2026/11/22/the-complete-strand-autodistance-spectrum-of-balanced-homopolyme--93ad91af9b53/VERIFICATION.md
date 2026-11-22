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
# Reproducibility and verification

Run `python3 verify.py` with standard Python 3 from this package directory. The checker enumerates every original word of length two through ten satisfying the input constraint and compares distance histograms to independent sixteen-state paired transfer counts. It also computes moments via a separate low-memory recurrence and checks the supports for the first six half-lengths. All direct checks passed.

The external-independent status is unperformed. Finite tests do not certify the all-length theorem. The all-length transfer is proved by an explicit bijection; the support follows by constructions; and the Gaussian/self-complement asymptotics follow from spectral covariance and Markov local-limit arguments stated in RESULT.md. Primary literature comparisons remain subject to independent historical verification.
