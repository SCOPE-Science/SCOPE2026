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

The complete universal proof uses the power-zero obstruction and groupwise inversion in each maximal subgroup; it does not depend on finite enumeration. The included `checker.py` uses actual Rees multiplication for thirteen test configurations (including sparse matrices, a nonabelian group, and nonidentity sandwich labels). It tests all elements of each full-support configuration for the two-complete identity and for involutivity of local inversion. It tests the square-zero element count in every sparse configuration. It also enumerates all permutations fixing zero for two size-five Rees semigroups at exponents one and two. The stored `verification_output.txt` is the actual output of the checked script. The tests are finite corroboration only. No independent audit has been performed.
