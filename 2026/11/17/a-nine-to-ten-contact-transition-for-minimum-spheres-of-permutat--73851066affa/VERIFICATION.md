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

# Verification instructions

Execute `python3 verify.py` with Python 3.10+ and no third-party packages. The verifier constructs every center, contact weight and squared radius in exact `fractions.Fraction` arithmetic, converts the universal squared-distance bound into an integer inequality, enumerates every permutation in all nine claimed orders, and verifies that precisely the claimed X-rays attain equality. It also checks the exact rational squared radii and the support transition at order ten.

The full run completed with no assertion failures. At order ten exactly 3,628,800 permutations were inspected, nine attaining equality and all others strictly inside. All nine integer orders together were checked, and the program reported PASS.

This validates the finite exhaustive certificate; it does not provide independent scientific validation or establish a uniform formula beyond the stated range. The proof additionally uses the classical permutation-vertex theorem and the exact convex-combination lower-bound argument given in RESULT.md.
