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

`python3 checker.py` uses only the Python standard library. It checks the exact three-by-three composition table, the three diagonal unique long edges that allow elementary collapses, the six retained triangle labels and double-incidence condition, the three circular vertex links, the Euler characteristic, and the orientability-sign obstruction. It also asserts the three product equalities which reduce the fundamental group to the Klein bottle presentation.

A separate exact integer Smith-normal-form computation on the full 12-by-9 triangle boundary matrix produced nine nonzero factors (eight ones and a two), consistent with integral first homology equal to a rank-one free group plus a single order-two cyclic summand and vanishing integral second homology. The source argument independently proves the manifold classification from vertex links and orientability.

No check beyond the finite table is needed for the universal quantification of this particular theorem: it concerns exactly one explicitly defined finite category and the minimality of three objects. This is an internal mathematical review only, not independent verification, publication-priority certification or proof of any claim about other surfaces.
