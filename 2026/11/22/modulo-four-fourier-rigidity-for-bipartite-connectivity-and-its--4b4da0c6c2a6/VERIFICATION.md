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

The self-contained script `verify.py` recomputes all Boolean connectivity indicators on the 16 edges of \(K_{4,4}\) and transforms the entire 65,536-entry array using integer butterflies. In a logically separate calculation it enumerates the 15 partitions of the four left vertices, applies the partition-lattice Möbius formula to each of the 65,536 frequency sign matrices, and checks equality coefficient by coefficient.

Observed exact outcomes: 36,317 connected edge subsets, 49 signed coefficient levels, 65,536 nonzero multipliers, 11,664 multipliers of magnitude three (all equal to \(-3\)), maximum magnitude 36,317, and 131,072 pointwise formula-and-residue assertions. The finite Parseval check \(\sum_{\xi}W(\xi)^2=2^{16}\cdot36317\) also passed. The histogram is stored in `spectrum.csv`. No stochastic computation or floating-point tolerance is involved.

The all-size modulo-four congruence and the thin-shore sharpness are derived symbolically from partition-lattice Möbius inversion and constructive sign choices in `RESULT.md`; the finite checker is corroboration, not an infinite certificate. External independent audit has not been performed.
