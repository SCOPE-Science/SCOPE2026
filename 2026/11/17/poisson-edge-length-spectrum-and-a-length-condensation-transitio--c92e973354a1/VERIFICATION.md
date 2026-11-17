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

Run `python verify_edges.py` from the directory containing the files, using Python 3 with SymPy. The checker enumerates all candidate vertices and all independently computed facet intersections at \(m=2,3,4\), each at \(n=m\) and \(n=m+2\). It checks every facial-edge pair and its squared Euclidean length against the exact spectrum. Successful output ends in `PARTIAL_PERMUTOHEDRON_EDGE_PASS`.

The e-series and factorial identities are proved in `RESULT.md`. The program is a bounded finite cross-check, not an infinite proof, independent research audit or historical-priority certification.
