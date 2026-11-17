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

# Verification of the Fano matroid homology character

Run `python verify_fano.py` using Python 3 and SymPy. The program enumerates the full binary-linear automorphism group and Fano complex from first principles; its expected exact output is provided in `verification_output.txt`.

The checks include: 7 points, 7 projective lines, 21 edges and 28 independent triangles; seven tetrahedral sphere boundaries with disjoint facet supports; all minimum mod-two cycle supports up to size four; rank 15 of the integral triangle-to-edge boundary; a \(7\)-by-\(7\) determinant of absolute value one extracted from the sphere-cycle matrix; all 168 automorphism chain-equivariance identities; all six conjugacy-class characters and independent direct rational kernel traces; and exact norm/orthogonality identities identifying the character rows.

**Proof-versus-computation boundary:** The integer homology rank, geometric saturation, and rational character are exact finite calculations; the general integral minimum-support assertion also requires the four-triangle edge-cancellation argument in `RESULT.md`. SymPy rational nullspace calculations are not used to assert integer saturation. The calculation does not certify any larger finite-projective-plane family or an integral equivariant splitting. Independent mathematical verification has not occurred.
