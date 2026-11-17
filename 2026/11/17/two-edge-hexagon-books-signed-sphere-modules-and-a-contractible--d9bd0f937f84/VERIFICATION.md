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

# Reproduction

Run `python3 verify_double_spine.py` (Python standard library only) and compare with `verification_output.txt`. The program constructs the graph and all distances from scratch, enumerates every finite clique, independently checks the cone/octahedron face decomposition and all intersections, performs complete mod-two boundary reductions, and computes signed Lefschetz traces for the pole swap and first-two-arm swap. Inputs cover 1 through 6 arms; the claimed theorem starts at 2.

The exact integral representation and contractible geometric orbit space are proved algebraically and topologically in `RESULT.md`, not inferred from finite-field ranks. Verification code does not provide an independent proof of the uniform statements, and the orbit-space contraction is not replaced by an invariant-dimension calculation. There has been no independent mathematical audit.
