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
# Verification of the two edge-orbit matching-complex homotopy maps

Run `python3 verify_torus_fault.py`; no packages beyond the standard library are required. The included `verification_output.txt` contains the complete output of the actual successful verification.

The program independently regenerates all simplices of the intact twelve-vertex graph, two edge deletions, and two endpoint-deletion links. At every elementary collapse it checks the free codimension-one face and maximal upper face; at every critical deletion it checks maximality. It then independently checks acyclicity of the full reversed-cover Hasse diagram, exact unit-pivot integer chain cancellations, zero final integral Morse differentials, reduced mod-two boundary ranks, and transitivity of each graph edge orbit. It accounts for every face. The mixed link has exactly two critical two-cells and two critical three-cells with zero *integral* attaching differential.

The cofiber calculations and the Smith normal forms of the inclusion maps are deduced mathematically from the resulting integral homotopy types and the deletion-link long exact sequence, not inferred from modular experiments. The claim is exhaustive only for the specific product \(C_3\square C_4\), not for arbitrary toroidal dimensions or multi-edge faults. No independent external review is claimed.
