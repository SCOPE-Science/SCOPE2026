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

# Exact finite verification
Run `python3 verify.py` using the Python standard library. It builds the specified forest complex and every octahedral automorphism from first principles, computes all flag-orbit boundary maps, checks every consecutive boundary composition, calculates independent modular ranks, and performs exact integral unit-pivot reduction. Its resulting differential has Smith factors \(2,2,2\). The exact recorded output is in `verification_output.txt`.

This verifies the finite integer chain computation for this 6-vertex graph; it is not a machine proof of the standard shellability, Armstrong orbit-space, or Hurewicz theorems. No larger-graph or infinite-family computation is asserted.
