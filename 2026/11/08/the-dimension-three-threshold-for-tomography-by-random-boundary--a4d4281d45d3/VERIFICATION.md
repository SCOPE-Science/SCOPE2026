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

# Verification notes

The proof in `RESULT.md` is analytic and covers each fixed integer dimension \(d\ge2\) and each positive facet-pair probability vector.

Run `python verify_midpoint.py` with NumPy and SymPy. Its independent simulations cover two rectangle aspect ratios, two boxes, a four-dimensional orthotope, and a five-dimensional orthotope: 220,000 midpoint pairs per shape, 1,320,000 in total. Checked quantities are the fraction landing in the continuous interior component, each centered tensor moment, and the exact algebraic reconstruction for \(d\ge3\). An additional independent cube-integral Monte Carlo check verifies the density normalization for each configuration. SymPy exact rational integrations check both three-cube total-variation values.

Expected terminal marker: `VERIFY_OK simulated_shapes=6 monte_carlo_midpoints=1320000 conditional_tv_cube=13/96 unconditional_tv_cube=521/1536`.

The simulation tolerances are finite numerical diagnostics only. Structural correctness rests on the exact probability decomposition, coordinate-factor integrals, and algebraic inversion. The verification does not establish publication priority, robustness under measurement error, or reconstruction of the full Euclidean geometry of skew parallelotopes.
