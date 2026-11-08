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

# Reproducibility and limits

Run `python verify.py` from the directory containing this file and `verify.py` with Python 3. No third-party packages are required. The script independently constructs prism and Möbius-ladder adjacency lists, enumerates all 3-color assignments supported on either side of their bipartitions, and checks open-neighborhood coverage directly. It checks prisms of circumference 6 and 12 and Möbius ladders of order 6 and 18. Complete support-and-color enumeration up to the half-order threshold is also carried out for the 12-vertex prism and 6-vertex Möbius ladder. An independent orbit comparison tests rotation and all six color permutations for the smaller examples; three non-equality cases are included.

Expected terminal line: `VERIFY_OK`. All results should be obtained from the packaged `verify.py`, not from unrecorded files. These are finite checks, not a computational proof for unbounded graph orders. The mathematical proof uses the bipartition equality condition and exact cyclic period-three recurrences; no external certificate or independent validation has been performed.
