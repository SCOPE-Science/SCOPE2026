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

The rule is synchronous and uses two distinct successor-coloured open neighbours. Two standalone, dependency-free Python programs check the theorem from different representations.

`code/verify_labelled.py` reconstructs the adjacency of the labelled graph and enumerates all colourings for one through five petals. It checks the global identity after three updates, the exact period-versus-basin test, and the closed basin formula. Output is in `evidence/verify_labelled.out`.

`code/verify_symbolic.py` uses fixed tags for six initial petal types and capped counts 0, 1, >=2. Saturation is sufficient because every threshold comparison is to two and count merges do not increase beyond that distinction. It tests the global identity on 2187 symbolic classes, including the exact tag transitions of present petals. It separately performs weighted six-type enumeration through 27 petals and compares the closed formula. Output is in `evidence/verify_symbolic.out`.

Both programs were executed from the paths included here and returned successfully. The general theorem is proved analytically; the code is a consistency check rather than a substitute for infinite proof. No external independent audit has occurred.
