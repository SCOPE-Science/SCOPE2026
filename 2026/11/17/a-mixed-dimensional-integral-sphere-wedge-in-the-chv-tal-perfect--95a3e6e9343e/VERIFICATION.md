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

# Reproducibility

Run `python verify.py` under a recent Python 3 interpreter; the script requires only the Python standard library. The graph edge list, matching construction, the twenty-four-coordinate acyclic matching order, exact integer gradient reductions, full directed acyclicity check, and the independent mod-two boundary-rank check are all contained in that file.

Observed output (also in `verify_output.txt`):

```
MORSE_PAIRS 930 CRITICAL {0: 1, 2: 17, 3: 1}
DIRECTED_HASSE_ACYCLIC 1879 vertices 6816 arrows
INTEGRAL_MORSE_BOUNDARY_3_TO_2_ZERO 17 critical 2-cells 1 critical 3-cell
CHVATAL_PERFECT_MATCHING_MIXED_WEDGE_PASS
INDEPENDENT_MOD_TWO_BOUNDARY_RANKS [23, 181, 414, 260, 52]
INDEPENDENT_MOD_TWO_BETTI 17 1
```

This is a complete finite proof certificate coupled with standard discrete Morse and Hurewicz theorems. The enumeration does not establish an analogous statement for any other graph. The integer Morse argument, rather than the mod-two check, is what rules out integral torsion and identifies the wedge homotopy type. Independent verification by an external reviewer has not been performed.
