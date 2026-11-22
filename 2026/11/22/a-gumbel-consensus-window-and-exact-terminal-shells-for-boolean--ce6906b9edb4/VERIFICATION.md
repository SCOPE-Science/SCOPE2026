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

# Reproducible verification and limitations

The unrestricted proof is in `RESULT.md`; the following are independently organized finite checks of its statements and computations. Run with Python 3 and no third-party packages:

```
python check_hypercube.py
python check_radius.py
python check_window.py
```

`check_hypercube.py` classifies every labelled state at dimensions two, three and four by exact visited-state cycle detection, giving entrance histograms `(4,12)`, `(4,140,112)`, `(4,33852,27648,4032)` in time order. The full exact terminal formulas are asserted only for dimensions at least three.

`check_radius.py` separately enumerates all support subsets of each cube parity class through dimension five and computes covering radii; for dimensions three, four and five, the terminal support categories `(N,U)` are `(4,10)`, `(8,64)`, `(16,336)`.

`check_window.py` implements a separate bit-parallel Boolean updater and tests the exact second factorial moment of missing vertices for dimensions eight, ten, twelve, sixteen and twenty. It independently samples 12,000 uniform initial states at each dimension six, eight, ten and twelve, comparing probabilities with the predicted limit. Such finite samples are approximations and not an infinite limit proof.

Unproved: a closed formula for every earlier intermediate entrance-time population and a formal identification of historical priority against all potentially related Poisson-limit theorems. The full archival 1987 reference was inaccessible, and independent mathematical validation remains unperformed.
