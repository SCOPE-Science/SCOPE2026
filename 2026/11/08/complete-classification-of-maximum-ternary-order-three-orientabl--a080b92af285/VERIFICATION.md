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

Use Python 3 with only standard-library modules. Execute `python3 verify_euler.py` and `python3 verify_direct.py` from the extracted files; each script uses only its own source and no downloaded data or external package.

The edge-based program enumerates all 512 reversal-pair choices, validates the ten degree-balanced choices, the two strongly connected choices, the exact 5-by-5 directed matrix-tree determinants of four, and four anchored tours for each. Its expected output begins `EULER_VERIFY_OK 10` and ends `cycles=8`.

The independently formulated direct program enumerates all 19,683 ternary rooted cyclic words of length nine, checks the unique orientation of each of the nine nonpalindromic reversal classes, verifies the complete eight-word rotation-canonical catalog and confirms its S3-plus-reversal orbit partition of sizes six and two. Its expected output begins `DIRECT_VERIFY_OK 8`.

Both checks are exhaustive in the specified finite domain, and the graph argument proves why length nine is maximal. They do not establish a formula for general alphabet sizes or orders. No external independent audit has been performed. Historical originality remains qualified by potentially inaccessible early classifications.
