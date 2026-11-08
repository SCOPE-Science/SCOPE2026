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

`python3 verify_prism.py > verification_output.jsonl` constructs the full graph and all matchings for \(3\le n\le7\), enumerates every legal two-edge switch by explicit adjacency tests, verifies the number and size of components, and checks every orbit type against its exact formula. Independently, `python3 verify_formula.py > formula_output.jsonl` enumerates pairs of perfect matchings of the residual complete cliques and checks every possible alternating-cycle partition and global degree formula for \(3\le n\le8\). Outputs are supplied; exact byte comparison of freshly generated JSONL against those records is a reproducibility check. Both algorithms use the Python standard library.

The complete graph counts for orders \(3,4,5,6,7\) are respectively \(4,16,56,376,1912\) perfect matchings and \(3,30,130,1860,11256\) flip edges. The independent formula count for order \(8\) is \(17984\) matchings and \(181888\) flips. Finitary checks verify instances, not the theorem over all \(n\); universal claims depend on the complete bijective proof and move classification in `RESULT.md`. No external review or formal proof certification is asserted.
