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

# Reproducible verification

Run `python verify_total_rainbow_windmills.py` in Python 3 with no third-party dependencies. The verifier constructs each bouquet's graph, enumerates all four labels at every vertex, applies the two defining open-neighborhood conditions to each label assignment, and separately expands the claimed polynomial with integer polynomial arithmetic. It compares all coefficients, minimum weight, and minimum multiplicities, not just the scalar total.

A full run returned:

`VERIFY_OK clique_bouquets=126 labelings_examined=5197632 feasible_labelings=2461279 full_polynomials=PASS minimum_multiplicities=PASS`

All cases with total petal order between two and seven and at least two ordered petals were included; additional larger examples cover repeated size-two petals and mixed sizes. The code is an independent finite check but is not a proof over all positive petal sizes. The displayed symbolic argument establishes the unrestricted formula and fixed-size reliability limit. No external independent audit is claimed.
