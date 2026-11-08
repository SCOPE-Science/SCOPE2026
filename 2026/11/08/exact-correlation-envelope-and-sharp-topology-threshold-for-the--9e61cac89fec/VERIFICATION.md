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

# Verification scope

The result is proved for all finite connected simple nonregular graphs of at least three vertices by exact algebra, with hypotheses and strict boundaries given in `RESULT.md`. The rational-arithmetic reproduction script `verify.py` checks graph sums, sharpness identities, the fixed-degree-correlation Gram bound, zero-gap supremum witnesses, and the paw-network threshold.

To run: `python3 verify.py`. The check requires only the Python standard library (3.9 or later). The successful package run covered all 752 connected nonregular labeled simple graphs on three through five vertices and checked the paw graph's squared threshold \(2/27\) exactly. Finite graph checks do not certify the universal theorem, whose proof is in `RESULT.md`.

Independent audit: not performed. In particular, the literature-priority comparison is a bounded review, not an exhaustive uniqueness guarantee. The setting is limited to fixed undirected networks and arbitrary numerical vertex attributes with nonzero variance.
