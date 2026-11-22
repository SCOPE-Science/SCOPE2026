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

# Verification and reproducibility

The theorem concerns a finite directed acyclic Markov chain, not a limiting probability inferred from samples. A recoloring is enabled if and only if it strictly improves the exact count of monochromatic edges, and every enabled ordered recoloring fires at rate one.

Run `python verify_kneser.py` and `python verify_pentagonal.py` with Python 3. Each executable independently enumerates all 59,049 initial configurations and computes exact fractions from the complete state-transition graph. The first implementation constructs disjoint two-subsets, uses a digit-coded state and a memoized absorption recursion. The second constructs an outer pentagon, an inner pentagram and spokes, uses tuples of colors, tests complete energy changes, and solves in descending energy-score order.

Compare the printed data with `EXACT_RESULTS.json`. Both codes explicitly assert the five geometrical classes of the 360 labeled \((7,2,1)\) minority placements and the nonzero \(11/270\) case. The stronger terminal-absorption classification is computed exactly rather than extrapolated from the smaller seeded configurations.

Scientific scope: unit coupling, three named spin colors, ten Petersen vertices, asynchronous independent rate-one clocks for each strictly energy-lowering ordered recoloring, and rejection of neutral updates. The proof is an exhaustive finite certificate; it does not apply to larger graphs, standard neutral-accepting Glauber moves or nonuniform parameters. No independent external verification has been performed.
