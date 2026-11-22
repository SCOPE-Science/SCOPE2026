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

## Executed verification

From the extracted package root:

```sh
python3 code/verify_tietze_full_quotient.py
```

The actual console transcript is in `verification/output.txt`. The verifier checks the complete graph automorphism group by adjacency backtracking, every subset matching and barycentric flag, group orbits and a Burnside count, all integral boundary squares, successive valid free-cell collapses, integer-unit chain cancellation and a direct nonabelian fundamental-group presentation. The output terminates with `TIETZE_FULL_MATCHING_ORBIT_S3_VERIFIED` only if all assertions pass.

## Precisely established and remaining limits

The integral chain equivalences prove all ordinary integral homology groups. The topological collapses preserve the actual homotopy type, and relator substitutions prove the quotient's trivial fundamental group. The standard Hurewicz and Whitehead deductions then establish a homotopy three-sphere. Chain-level unit cancellations are not claimed as geometric collapses. The calculation covers only the specified finite graph and complete symmetry group; it is not a proof for a graph family. No independent mathematical audit has been performed.
