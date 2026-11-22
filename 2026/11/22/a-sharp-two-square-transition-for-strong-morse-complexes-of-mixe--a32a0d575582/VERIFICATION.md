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

# Verification instructions and limits

The scientific proof is `RESULT.md`; `verify.py` is a separate, deterministic, Python 3 standard-library checker. Execute `python3 verify.py` in the directory containing that file, and compare with `verification_output.txt`. No external data, package installation, or network connection is required. Every assertion must pass and the last line must read `ALL_VERIFY_OK`.

The program enumerates all strict vertex orders for each listed small graph, generates strong-filter incidence matchings by the unique-earlier-neighbor criterion, closes under faces, and *independently* constructs the proposed join-plus-hub-cones simplicial complex. It compares entire face sets; computes reduced mod-two Betti ranks by exact bitwise Gaussian elimination; checks the symbolic face enumerator coefficient by coefficient; and for square count at least two, executes and verifies elementary relative free-face collapses onto the no-hub join. The mixed cases are \((p,q)=(1,1),(2,1),(1,2)\); the printed boundary cases are \((1,0),(2,0),(0,1),(0,2)\), included only for consistency checks against known one-type results.

The integral theorem for all positive \(p,q\) is not inferred from finite data or mod-two ranks. It follows from the exact petal-local classification and the joins, relative collapses, and nullhomotopic cone attachments proved in `RESULT.md`. The checker does not compute integral equivariant representations or any higher-polygon cases. Publication-priority verification and independent mathematical audit have not been performed.
