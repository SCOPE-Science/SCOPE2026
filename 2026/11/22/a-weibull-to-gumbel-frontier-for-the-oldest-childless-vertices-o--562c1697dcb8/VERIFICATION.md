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

Run `python3 verify.py` with Python 3 and no third-party dependencies. The verification program enumerates twelve entire finite parent-choice sample spaces (not samples of configurations), evaluates every subset of childless labels, compares rational joint probabilities with formula (1), and checks mean/covariance expressions. It also tests deterministic first-intensity approximations in several fixed and logarithmic fan-in cases. An actual replay from the complete package reported 497 passing checks.

Analytic validity of point-process convergence rests on the exact all-order probability (1), its product domination, the vanishing maximum one-point mass, convergent cumulative intensities, and the absolutely dominated Laplace-functional series. These are proved for unbounded graph sizes in RESULT.md; tests alone cannot establish them. The reversed-Gumbel minimum additionally uses control of the unbounded left tail, and the full macroscopic frontier uses explicit expectation and covariance bounds. No independent external audit or certification has occurred.
