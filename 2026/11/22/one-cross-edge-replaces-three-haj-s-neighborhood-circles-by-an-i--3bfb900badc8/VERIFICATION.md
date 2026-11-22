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

# Verification details

The graph is defined by the full two-clique Hajós adjacency list and one cross-edge. The proof enumerates all five original generating neighborhood subcomplexes and both new ones for arbitrary integer parameters. Exact pairwise intersections of the new simplices with the original complex give two circle wedges, and the relative integral boundary has a unit determinant minor. These uniform identities, not experimental extrapolation, establish the theorem.

Run `python3 hajos_one_cross_verifier.py` with standard Python 3. The test program covers nine parameter pairs with \(5\le a\le7\) and \(a\le b\le8\), reconstructs all neighborhoods, checks full simplicial faces and attachment intersections, and verifies mod-two chain ranks and the unit minor. All checks passed in the current calculation.

Independent audit was not performed. No external proof assistant or independently commissioned certification was used. An integral homotopy decomposition of the augmented complex is not asserted.
