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

# Reproducibility

Run `python3 verify.py` in the same directory as this file. The script requires only Python's standard library and prints `VERIFY_OK` after all assertions pass.

The script constructs the proposed graded polynomial by convolution, then independently enumerates every ternary order relation between each old point and a new point. It checks transitivity directly on all triples of the enlarged relation, finding agreement for all 66 disjoint-chain isomorphism profiles with one through eight named elements. It then checks the triangular recovery method on every integer partition of sizes one through 30 (28,628 total profiles), verifies that all lower truncations fail at sizes two through 30 using explicit witnesses, and confirms the four-point grade comparison and 17-point scalar collision.

The all-size assertions are supported by the combinatorial proof in `RESULT.md`, not by extrapolating from the finite checks. No independent mathematical review has been performed. The captured execution record is `verify_output.txt`.
