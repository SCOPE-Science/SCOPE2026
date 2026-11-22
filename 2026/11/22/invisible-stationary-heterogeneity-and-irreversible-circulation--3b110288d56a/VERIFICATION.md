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

# Reproducible mathematical verification

The proof in `RESULT.md` is analytical: it calculates one exact Kolmogorov cycle ratio for each pair of distinct participants and constructs detailed-balance weights for the equal-cost case. The two-participant stationary formula is checked by all four balance equations.

Execute `python3 verify_finite_chain.py` using Python 3.8 or later. The script uses exact rational arithmetic to reconstruct discrete transition matrices, checks the explicit 2-player stationary law and current, compares its stationary distribution with a homogeneous-contribution model, and verifies homogeneous detailed balance up to five players. It also computes the near-full-cooperation square product for multiple unequal-cost cases. The rational probabilities correspond to positive Fermi costs, so these are admissible parameters.

The exact computation does not establish uniqueness or reversibility for all population sizes; those conclusions are proved separately in the general argument. Published work was examined for related results, but uninspected sources may contain equivalent earlier statements. No independent audit is claimed.
