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

# Reproduction and limitations

Run `python verify_path_chebyshev_covariance.py` with Python 3 and no third-party packages. The verifier computes integer matrices \(2T_j(A_n)\) using the recurrence \(B_{j+1}=J B_j-B_{j-1}\), where \(J\) is the unweighted path adjacency and \(B_0=2I\), \(B_1=J\).

Successful execution checked **216224** reflected-kernel matrix entries for \(2\le n\le30\), **9454** covariance pairs, **203** exact full-sign-space covariance enumerations for \(2\le n\le8\), and **9454** null-polynomial matrix entries. All checks passed on the delivered source. The sign-space checks enumerate all \(2^n\) sign vectors for each tested \(n\), but do not enumerate arbitrarily large graphs. Generality follows instead from the explicit spectral identity and exact pair-count proof in `RESULT.md`.

The verification is reproducible finite corroboration, not a formal machine proof, external validation, or publication-priority certificate. The proof is for common Rademacher probes and precisely the first \(n\) positive Chebyshev degrees of a path half-adjacency matrix.
