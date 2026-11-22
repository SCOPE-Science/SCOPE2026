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

Run `python3 verify.py` from a directory containing the extracted standalone script. No external data or Python packages are required. Its completed output is:

```text
VERIFY_OK coloring_cases=830839 direct_boolean_closures=4435 forest_cases=5913 sharp_paths=30
```

The script enumerates canonical increasing-parent finite out-forests on up to seven vertices, builds bottom-up depth-observation signatures, and independently compares generation with leaf-colour injectivity and with the falling-factorial count. In smaller cases it directly builds the Boolean/modal subalgebra by closing truth sets under complement, conjunction and successor-existence. It also checks sharp depth on monochromatic paths of thirty distinct positive heights. Counting cases from code is finite validation; the unrestricted result follows from the leaf-ancestor isolation argument in `RESULT.md`.

Manual mathematical checks include the empty tuple (one palette word), isolated-vertex forests (height zero), any outward path (one leaf), and stars (arbitrarily coloured root). Check the exact orientations: edges are from parent to child, and the modal arrow is not reflexive or transitively closed. No external or independent audit evidence exists for this claim.
