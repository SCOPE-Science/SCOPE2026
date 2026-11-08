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

# Verification

Run `python verify.py`. No nonstandard packages or external data are required.

The implementation directly enumerates all labeled graphs at \(n=4,5,6\), weighting each graph by its exact Bernoulli probability for \(p=1/3,2/3,4/5\). It independently compares exact triangle variance, induced-four-cycle variance and their covariance to the formulas in `RESULT.md` (27 checks). From the complete 64-graph four-vertex space it computes centered-Bernoulli orthogonal coefficients by direct expectation and checks support-level formulas (3 more checks), the critical exact support values (1), three covariance-sign conditions at each of three sizes (9), and five large-size correlation diagnostics (5). In total 45 checks pass. The diagnostic tolerance does not establish the analytic limit.

All-n correctness rests on the overlap enumeration, Parseval decomposition and asymptotic expansion presented in `RESULT.md`; this checker tests representative cases rather than establishing those arguments exhaustively. Independent audit has not been performed.
