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

# Verification and reproducibility

Run `python3 verify_petersen_a5.py` in a Python 3 environment using the standard library. It enumerates all graph edges and all matching faces from the defining two-subset graph, constructs all barycentric chains, computes all \(60\) even-label automorphisms, and forms orbit representatives and signed boundaries.

The exact reproduction checks are: original face counts \((15,75,145,90,6)\) and \(331\) nonempty faces; barycentric chain counts \((331,2460,5010,3600,720)\); orbit cell counts \((14,58,94,60,12)\); every consecutive boundary composition zero; \(118\) exact integral \(\pm1\) cancellations leaving one degree-zero and one degree-two generator and no residual differentials; original presentation consisting of \(61\) non-tree generators and \(145\) triangle relators with all \(61\) generators eliminated; and one explicit three-cycle stabilizing a matching two-simplex.

As an extra consistency check, the program computes modulo \(2,3,5,7,1009\) the differential rank vector \((0,13,45,48,12,0)\), giving Betti numbers \((1,0,1,0,0)\). Modular ranks alone would not establish integral torsion-freeness and are not used in place of the integral cancellation.

The finite verification establishes the particular graph's exact chain and presentation calculations. The implications to orbit-space fundamental group and complete homotopy type use the stated classical topological theorems. Neither an infinite family nor independent mathematical validation is asserted.
