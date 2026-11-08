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

# Verification of the integral homotopy claim

Run `python3 verify_paley13.py` from a directory also containing `paley13_certificate.json`. Both files are provided with this result. No external packages are required.

The verifier first recomputes the nonzero quadratic residues in \(\mathbb Z/13\mathbb Z\) and all thirteen open neighborhoods. It checks the strong-regularity intersections, reconstructs simplices both as subfaces of neighborhoods and as subsets whose common-neighbor intersection is nonempty, and compares all \(8191\) nonempty subsets. It checks the complete claimed face vector and Euler characteristic.

It next reconstructs 286 matched pairs by the explicitly specified sequence of vertex toggles. The stored certificate contains every pair, every critical face, and an explicit topological ordering of all 598 cells. All 2067 codimension-one incidences are independently regenerated and checked against the stored order. A separate Kahn topological sort also succeeds, establishing directed acyclicity. The resulting critical-cell vector is one zero-cell and 25 two-cells. The standard discrete-Morse theorem yields the full integral homotopy equivalence; the computed modular ranks alone would not justify it.

As a cross-check, sparse signed simplicial boundary matrices are reduced separately modulo 2, 3, 5, and 7. The boundary ranks in positive degrees are \((12,66,130,65,13)\), and the reduced Betti vector is \((0,0,25,0,0,0)\) in each characteristic. `verification_output.txt` is the actual recorded stdout from the verifier.

The source graph is finite, and the calculation is exhaustive for the specified thirteen vertices, not an experimental extrapolation. Results for other quadratic-residue orders, alternative neighborhood conventions, or automorphism-equivariant topology are not claimed. Independent validation has not been performed.
