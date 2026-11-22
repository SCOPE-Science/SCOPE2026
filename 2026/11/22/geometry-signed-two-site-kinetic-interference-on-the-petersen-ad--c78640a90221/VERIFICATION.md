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

# Verification of the exact two-site adsorption identities

The Kneser-graph construction has ten vertices and degree three. For each of the two inequivalent locations of a second marked site, `verify_symbolic.py` evaluates the proven exponential-race recurrence using exact SymPy rational functions, visits 52 distinct subsets, and verifies the asserted rational formula by symbolic cancellation. The test passed for both classes.

Independently, `verify_priority.py` enumerates all \(8!\) permutations of the ordinary vertices for each of 90 possible ordered marked-site priority pairs. Its 3,628,800 deterministic priority decisions per geometry class independently reproduce the terminal-support assertion. The priority probabilities are then summed with exact `fractions.Fraction` arithmetic at six positive rate pairs, agreeing with the closed formulas in all twelve cases. This test passed.

To reproduce, place both companion scripts beside this file and run `python verify_symbolic.py` and `python verify_priority.py` from a Python 3 installation with SymPy installed. The second program uses only the Python standard library. The symbolic recurrence constitutes an exact proof of the finite identities; the separate priority enumeration provides cross-validation but does not on its own prove the formula for all real rate parameters. Historical priority was assessed from available literature and is not externally certified.
