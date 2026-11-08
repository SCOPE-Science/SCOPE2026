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

The file `verify.py` runs with the Python standard library using `python verify.py`. The actual execution yielded 4,952 direct semantic-vs-graph comparisons and complete minimal-falsifier spectra for `1x5`, `2x2`, `2x3`, `2x4`, `2x5`, `3x3`, `3x4`, and `4x4`; all assertions passed. The last case enumerates all 65,536 binary teams.

The checker is not a proof beyond the enumerated sizes. The general proof uses bicircular edge-minimality, degree bounds and theta subdivision. The two lowest coefficient counts were independently checked by enumerating the graph edge masks. No external independent audit or formal proof certification has been performed.
