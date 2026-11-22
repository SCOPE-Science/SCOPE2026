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

# Reproduction and limits

Both scripts run from this directory without remote access. Compile the C++17 checker using `g++ -O2 -std=c++17 verify_meg.cpp -o verify_meg` and run `./verify_meg`. Run the alternate checker with `python3 verify_meg_independent.py`. They must print `MEG_ALL_CHECKS_OK` and `MEG_INDEPENDENT_ALL_CHECKS_OK`. The attached `verification_output.txt` records actual executions after source file creation.

The first enumerator uses an edge-removal distance test; the second independently uses shortest-path multiplicities. Each enumerates all \(2^{10}\) or \(2^{20}\) labelled subsets, tests exact minimality, determines the component sizes under allowed single-vertex addition/removal, and asserts the reported values. The second also enumerates all independent subsets and verifies the covering comparisons. No noninteger rounding or statistical evidence is involved. All results are finite, not statements about arbitrary generalized Petersen graphs. Neither script constitutes outside expert verification.
