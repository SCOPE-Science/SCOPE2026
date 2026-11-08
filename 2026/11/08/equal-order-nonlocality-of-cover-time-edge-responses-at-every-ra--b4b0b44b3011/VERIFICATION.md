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

# Verification and limits

The analytic proof is in `RESULT.md`. Replay the self-contained executable with `python3 verify.py`; no third-party Python modules are needed. The checker constructs the two graphs at several radii, compares their marked induced neighborhoods and full-graph degree labels, checks the common order and resistance argument's bridge topology, verifies the exact positivity polynomial and negative inequality, and separately solves finite visited-set cover-time equations with `fractions.Fraction` for a smaller example.

The finite example uses a clique of size three instead of the general theorem's larger clique; it checks the analytic mechanism but is not the basis for the universal result. The central infinite inequalities — complete-graph excursion tail, probability of reaching the central cut vertex, Poisson thinning, and the exact path calculation — are proved in the result. A finite run cannot establish a universal statement on its own. No independent external audit has been performed.
