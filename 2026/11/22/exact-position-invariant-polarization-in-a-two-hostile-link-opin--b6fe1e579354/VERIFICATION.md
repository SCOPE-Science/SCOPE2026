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
The self-contained analytic proof is in `RESULT.md`. The supplementary `CHECK.py` was executed using NumPy and SciPy and printed `PASS: 750 finite numerical checks; no numerical test substitutes for the all-size proof.` It compares exact rank-two threshold eigenvalues, all feasible hostile path-edge positions, nonlinear positive stationary equations, positive-definite Hessians at minimizing profiles, invariant minimum energy and critical amplitude. A numerical test cannot establish an all-size theorem or historical novelty.

For reproduction, execute `python CHECK.py`. The source model and Appendix C are in Boyce et al., arXiv:2512.05725 and DOI 10.1007/s00332-026-10333-0. No external validated certificate or independent review is claimed.
