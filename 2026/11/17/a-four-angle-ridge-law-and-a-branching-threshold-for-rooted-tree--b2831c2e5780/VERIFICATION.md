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

# Reproducibility and limitations

Run `python VERIFY.py` with Python 3, NumPy and NetworkX installed. The verification enumerates all unlabeled free trees with \(2\le n\le9\), roots each at every vertex, builds the entire finite Boolean-vertex set of the canonical order polytope, and checks affine ranks of all facet-pair intersections against the claimed angle law. The check includes 748 instances, with no sampling for these dimensions. The analysis does **not** extrapolate this enumeration into an infinite proof; the unrestricted theorem and sharp angular concentration criterion are proved symbolically in RESULT.md. Scientific priority beyond inspected sources and independent mathematical audit remain unperformed.
