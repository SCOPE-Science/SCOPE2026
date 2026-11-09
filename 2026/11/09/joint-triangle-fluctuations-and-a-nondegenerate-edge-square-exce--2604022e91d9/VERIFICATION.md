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

# Verification and limitations

Run `python check_motif.py` with Python 3.9 or newer. The checker is standalone and requires no third-party packages. It exhaustively checks all binary creation words with lengths one through ten, comparing graph-edge and graph-triangle enumeration with the closed expressions and verifying the exact quadratic remainder identity at rational baseline probability \(\rho=2/5\). For memory lengths one through five and four rational baseline/reinforcement combinations, it also checks stationarity of the exact Pólya word law, within-word covariances, the innovation-variance formula, and exact covariance integrals. Expected last line: `PASS 8615 exact assertions; final excess coefficient = 2/15`.

The separate `simulate_motif.py` script reproduces a seeded numerical experiment using \(M=3\), \(\rho=0.4\), \(\delta=0.7\), 2,500 vertices and 2,300 independent samples; it gives empirical variance \(0.0347349534\) against the theorem's asymptotic variance \(0.0354785882\). The experiment is not an exhaustive test or a proof of a limit law. Finite verification does not substitute for the analytic martingale functional central limit theorem and the displayed deterministic remainder bound.

The self-contained statement concerns only fixed memory and the unconditioned graph construction. Historical priority, independent theorem review, and external validation remain unperformed. Scientific caveats are in `RESULT.md`.
