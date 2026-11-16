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

# Reproducibility verification

The finite claims were checked from the actual `check.cpp` and `SPECTRUM_Q4.csv` files in this package. Both use integer arithmetic throughout, including the cyclotomic encoding of ternary Fourier values in \(\mathbb Z[\omega]\), where \(\omega^2+\omega+1=0\).

Run from the directory containing both files:

```sh
c++ -O2 -std=c++17 check.cpp -o check
./check
```

Expected markers:

```
THREE_COLOR_PASS colorings=120 frequencies=59049 zero=39366 rank=19683 min_nonzero=3 representative=98 multiplier=3
FOUR_COLOR_PASS colorings=12960 frequencies=1048576 zero=801222 balanced_extra_zero=14790 rank=247354 min_nonzero=16 projection_abs_sum=87263536 projection_norm=5453971/65536 minimum_extra_degree=6 count_at_degree6=1110 witness=1450 direct_positive=6480 direct_negative=6480 balanced_orbits=513 spectral_levels=83
```

Assertions check the Petersen graph's 15 edges and both classical colouring counts; the palette-four independent-set partitions into 20 three-class and 520 four-class types; exact Parseval; the complete signed spectrum certificate; nullities, additional zero-degree distribution and Fourier gaps; a directly evaluated balanced six-vertex cancellation; 513 independently recomputed direct character sums covering all balanced frequencies; the exact projection-kernel absolute sum; and a ternary extremizing multiplier evaluated independently of the cyclotomic transform.

The endpoint optimality proof uses translation averaging; no finite search over arbitrary projections is asserted. The three-colour nonvanishing theorem has a separate exact orbit argument. Unproved extensions to other graphs, colours or higher dimensions are outside the claim. The verification is not an independent external audit.
