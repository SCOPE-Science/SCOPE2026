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

The exact reproducible proof component is `CHECK.py`, which requires only Python 3.8 or later. Run `python3 CHECK.py`. The expected success text begins `VERIFY_OK_24CELL_TETRA_SPECTRUM` and certifies exact enumeration of 10626 unordered root-vertex quadruples, two determinant methods, 72 maximizers, 1152 verified symmetry maps, and the absence of a common three-vertex subset among distinct maximizers. This command was executed against the packaged checker code. The separate analytical wedge-convexity and equality-rigidity proof is recorded in `RESULT.md`; it is not a computation over a continuum. Independent audit has not been performed.
