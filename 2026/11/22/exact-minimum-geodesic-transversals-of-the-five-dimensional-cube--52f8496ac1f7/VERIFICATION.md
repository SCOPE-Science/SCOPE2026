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

# Reproducible exact finite check

Compile `verify.cpp` with `c++ -O2 -std=c++17 verify.cpp -o verify` and execute `./verify`. The code builds the 1920 maximal geodesic vertex masks from all coordinate flip orders; checks each of the 32 proposed radius-two sphere witnesses; and exhausts all 7,888,725 normalized 9-sets and 20,160,075 normalized 10-sets. Counts of accepted sets are exactly zero and ten, respectively, and the ten accepted normalized sets are compared against the predicted translated spheres. All operations are exact integer and bit-mask computations.

Expected terminal statuses: `MAXIMAL_GEODESIC_SETS 1920 PASS`, `SHELL_CONSTRUCTIONS 32 DISTINCT ALL_HIT PASS`, `NORMALIZED_SIZE_9 tested=7888725 valid=0 PASS`, `NORMALIZED_SIZE_10 tested=20160075 valid=10 PASS`, `CLASSIFICATION_ALL_32_MINIMA_PASS`, `GT_Q5_10_PASS`.

The source constitutes a complete finite certificate but is not a symbolic argument or an independently audited implementation. The status front matter records the absence of external independent audit only.
