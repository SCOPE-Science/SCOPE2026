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
# Reproduction and boundaries

Run `python3 verify.py` using Python 3.8+ and the standard library. `verify.py` constructs the complete explicit candidate negative-curve intersection data in integral coordinates, checks the root-contact list, computes the exact independence-polynomial recurrence, and separately visits all \(2^{21}\) subsets by a different bit-mask dynamic program. The resulting coefficient vectors are checked against explicit constants, and the result is compared with an independent smooth-cubic computation using twenty-seven exceptional classes.

The executed output is embedded as `verification_output.txt`. Critical lines are `nonroot_support_profile=(1, 21, 135, 370, 465, 237, 21)`, `root_support_profile=(0, 1, 21, 120, 260, 210, 36)`, `combined_support_profile=(1, 22, 156, 490, 725, 447, 57)`, and `ALL_CHECKS_PASSED`.

These calculations certify the **finite** combinatorics of the explicitly listed curves. The infinite/geometric step—exhaustiveness of the negative curve list—uses adjunction, nefness of the anticanonical class, the intersection lattice, and the six-point incidence assumptions, as proved in `RESULT.md`. A finite test is not asserted to prove the geometric classification by itself. The chamber correspondence is a previously proved theorem, not independently re-proved by the code.

No independent external scientific validation has been performed. Historical priority beyond the inspected sources is unresolved.
