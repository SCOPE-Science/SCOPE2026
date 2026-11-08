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

The analytic result is proved by factorial moments and entropy decomposition in `RESULT.md`. Run `python CHECK.py`: its rational-grid checks test antipodal arc counting and conditional pairwise independence; the combinatorial checks verify the matching enumerator. A complete executed run returned 36653 passed assertions. Tests are finite consistency checks, not an infinite certificate. 

The Poisson limit uses fixed integer factorial moments; total-variation convergence is on the discrete count space. Entropy convergence also requires uniform higher moments and explicit bounds on rare nonmatching configurations. The literature-priority comparison is bounded and independent expert validation has not occurred.
