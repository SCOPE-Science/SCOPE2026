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

# Reproduction and limitations

Use Python 3.8 or later and run `python3 verify.py` from the extracted package directory. Only the Python standard library is used. The program constructs finite simple connected cubic graphs and computes all named two-edge-colour assignments by direct enumeration of edge-neighbourhood counts. Separately, it enumerates every vertex subset of size one quarter of the order and checks the exact closed-neighbourhood perfect-code condition. The two full sets of colourings are compared after the constructive translation, and the circular-ladder count is independently checked through twelve columns.

The final replay on the included `verify.py` completed with `VERIFY_OK`. It tested complete and complete-bipartite examples, the Petersen graph, prisms, Möbius ladders, and deterministic connected cubic samples up to twelve vertices. The numerical output is diagnostic, not an assumption in the proof. Finite enumeration cannot certify the claim for all cubic graphs; unrestricted correctness is justified by the local degree-sum case split in `RESULT.md`. No external proof assessment has been performed.
