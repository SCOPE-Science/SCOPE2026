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

# Computational verification

Run `python3 verify.py` with Python 3 standard library. The script independently counts crossing uniform hyperedges, evaluates the support-range width of the Minkowski simplex sum, and checks every centered cut candidate for small dimensions. It additionally compares exact-integer squared widths over 11,172 parameter profiles up through dimension 150 and checks 16 larger off-critical scalings. The observed finite candidates in those profiles have no interior cut-size minimizers, but the theorem does not claim or rely on that empirical pattern.

The analytic cut-ray reduction and asymptotic trichotomy are the proof for all admissible dimensions; finite enumeration and random directions do not certify all dimensions or all continuous directions. The critical scaling \(c=2\) is not assigned an eventual minimizer type. No external independent mathematical audit was performed.
