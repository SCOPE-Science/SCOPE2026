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

Reproduce the ordinary standalone tests with `python3 artifacts/verify.py`. The code enumerates all possible edge subsets in the tested graphs, applies the defining perfect-edge-domination condition directly, independently constructs the proposed white-set classes, and verifies the exact formula. It also checks the equality for length-two arms in larger parameter ranges. These experiments are finite and do not establish the infinite assertion; the complete proof uses the white-set bijection, forbidden-word counts, and exhaustive root case distinction. No independent mathematical audit has been performed.
