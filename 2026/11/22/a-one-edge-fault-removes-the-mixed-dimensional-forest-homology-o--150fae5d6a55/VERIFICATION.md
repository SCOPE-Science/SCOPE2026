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
Run `python3 verify_edgefault.py` from the extracted directory with Python 3.10 or later. It constructs the graph, checks all 256 ambient subsets twice (union–find and independent depth-first-search acyclicity), builds every face-poset cover incidence, and performs exhaustive acyclicity checks of the four Morse matchings. The recorded run produced four face-vector and critical-cell reports, then checked that the ten listed free-face pairs leave precisely the degree-two forest complex. It ended with `ALL_CHECKS_PASS`. All steps are deterministic, and no external files, services, or dependencies are required beyond Python's standard library.

These are exact finite combinatorial certificates; they imply the stated homotopy types through discrete Morse theory. The result covers every single edge deletion by graph automorphism, but no larger graph size and no assertion about integral maps from the intact cube is certified.
