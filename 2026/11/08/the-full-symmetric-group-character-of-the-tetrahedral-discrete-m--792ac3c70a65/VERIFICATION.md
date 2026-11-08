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

Three standalone Python programs use only the standard library and reconstruct the finite tetrahedral Morse-matching complex from first principles. Execute `python3 tetra_sym.py`, `python3 orbit_check.py`, and `python3 mod2_check.py` in a directory containing the three scripts; compare their terminal output with `VERIFY_OUTPUT.txt`.

The first enumerates every nonempty acyclic matching, checks the published face vector, computes signed trace and all rational irreducible multiplicities. The second constructs arrow orbits for five representative permutations and counts admissible invariant simplices independently, applying the Euler sign at the orbit-block level. The third computes the full mod-two chain boundary ranks (not a substitute for the published integral homology theorem). The first two independently obtain character \((99,1,-1,0,-1)\) and all five class Lefschetz numbers \((100,2,0,1,0)\).

The known integral homology result in Scoville's arXiv:2604.18172v1, Theorem 20, is an explicit mathematical input. The computation proves the class traces and finite representation decomposition, but does not independently establish integer Smith normal forms, integral equivariant splittings, higher-simplex behavior, or literature completeness. Independent mathematical audit is not performed.
