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

# Reproducible checks and limits

Execute `python3 verify.py` with the Python 3.10+ standard library. The companion `verify_output.txt` is the output from an actual run. The program independently enumerates all 1024 vertex subsets to check the face predicate, then checks 496 faces, 120 generators, 238 reduced matching pairs, and 1860 Hasse incidences. It constructs and reduces the oriented integral chain boundary, confirms a determinant-one seven-by-seven minor and a nonzero left-null row relation, and computes full ordinary reduced homology over five different prime fields.

The determinant and relation prove exactly seven unit Smith factors, so the integral attaching map, not merely mod-prime ranks, is determined. A CW model with one vertex, eight three-cells and twelve four-cells is obtained from the acyclic matching after retaining the vertex formerly paired to the empty face. Since the two-skeleton contains no positive-dimensional critical cells, \(\pi_3(\bigvee^8 S^3)\) classifies every four-cell attachment, and the Smith form gives the stated homotopy type.

This is an exhaustive finite computation for a precisely defined ten-vertex graph. It does not prove a theorem for larger Kneser graphs or exclude an equivalent unindexed publication. No independent external audit has been performed.
