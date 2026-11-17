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

# Verification of the connected stacked-sphere double
The accompanying standard-library Python program `stacked_double_verify.py` builds the stacked three-sphere from its tetrahedral facets, explicitly enumerates all two-faces used as double vertices, and obtains each double graph edge as a pair of opposite edges of a tetrahedral facet. It independently recomputes vertex, facet and double-edge counts, connected components and graph cycle ranks.

The program tested every stacking history through three facet-stackings (1, 5, 40 and 440 construction histories for 5, 6, 7 and 8 vertices). It also used 40 deterministic pseudorandom sequences for each of 9, 12, 16 and 20 vertices. The script printed `STACKED_DOUBLE_PASS` and the exact count table recorded in `stacked_double_output.txt`. To replay: `python3 stacked_double_verify.py`. Only Python's standard library is required.

The universal claim is not proved by finite enumeration. Its certificate is the four-step combinatorial proof: the base Petersen graph, a complete enumeration of local opposite-edge adjacencies after a stacking, a connectivity argument for the replacement gadget, and the spanning-tree formula for a connected graph. The source formula is independent of any tested upper bound. The result does not certify other triangulated three-spheres or higher-dimensional doubling.
