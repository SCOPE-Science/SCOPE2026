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

# Reproducibility checks

Use Python 3 to run `python check_small.py` and `python check_independent.py` in the directory containing those two files. The first script imports only the Python standard library. Both scripts run internal assertions and print completed finite checks. The two scripts use different graph representations, different propagation code, and independent reconstruction of the sliding graph.

The first check enumerates every vertex subset until a minimum size appears for each \(3\le n\le7\), and confirms exact identity of the optimizer family and slide graph. Its printed counts for \(n=3,4,5,6,7\) are respectively 6, 18, 40, 75, 126 optimum configurations; 6, 24, 60, 120, 210 slides; and diameters 3, 4, 5, 6, 6.

The second check enumerates minimum power dominating sets directly for \(3\le n\le6\), reconstructs the unique Johnson-edge midpoint for every type-B state at \(3\le n\le10\) and at \(n=12,16\), and computes all-pairs eccentricity classes through \(n=10\). Both checks passed when run. Assertions stop with an error if any tested property fails.

These finite computations corroborate the definitions, formulas and small boundary cases, but cannot certify the all-order statement. The all-order graph isomorphism and distance bounds are proved in `RESULT.md`. No independent mathematical audit has been performed.
