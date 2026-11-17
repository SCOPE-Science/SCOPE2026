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

# Reproducibility and scope

The standalone Python 3 file `snake_metric_checker.py` requires only the standard library. Run `python3 snake_metric_checker.py` in the directory containing that file. The actual replay yielded:

```
TYPE_C_SNAKE_METRIC_PASS n=2..11 profiles=2046 ordered_pairs=19684660 full_diameter_profiles=124
```

It independently enumerates every feasible zero-one vector from suffix inequalities, explicitly accumulates every ordered squared-Hamming-distance polynomial, and separately calculates the polynomial via four-state matrix transfer. It verifies identity of every polynomial coefficient, the full-diameter block condition, the number of full-diameter profiles in each dimension and the exact leading coefficient for all such profiles. It covers dimensions 2 through 11; the theorem is stated for every dimension at least 3. The unbounded proof is the binary suffix-state bijection, four-state transition calculation, and odd/even suffix-count argument in RESULT.md. No numerical extrapolation, independent audit or external formal certification is claimed.
