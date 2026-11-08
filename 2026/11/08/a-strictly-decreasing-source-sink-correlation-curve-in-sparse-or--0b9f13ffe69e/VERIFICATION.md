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

# Reproducible checks and limits

Run `python3 verify.py` in the same directory as this file, using Python 3.8 or later. The program needs only Python's standard library. It independently enumerates directed edge subsets for \(n=2,3,4,5\) at four exact rational edge probabilities and for \(n=6\) at probability \(1/2\). It checks exact first and second moments, the triangular source–sink indicator covariance profile, and conditional martingale covariances against independently enumerated edge choices. It also evaluates finite-size sparse-covariance limits and samples the analytic correlation formula numerically. Assertion counts and results are printed by the program.

The finite enumerations and floating-point tests are consistency checks, not general proofs, novelty certifications, exhaustive literature checks, or independent audits. The all-size and limit claims rely on the explicit combinatorial identities, martingale argument, and calculus in RESULT.md. Mathematical scope excludes other directed-acyclic-graph sampling measures.
