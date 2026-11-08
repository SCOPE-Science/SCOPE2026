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

# Verification instructions and scope

Run `python3 checker.py` using only the Python standard library. The program implements the occupancy-indicator variance identity and an independent exact Markov update for observed-species subsets, comparing the two methods for 55 rational-probability/sample-depth cases. It also confirms four strict inequalities for the explicit three-species example, and numerically illustrates scale separation with a four-species vector.

The proof, not any finite experiment, establishes the arbitrarily large finite-species construction. Its key analytical limits and strictness argument are in `RESULT.md`: at \(\lfloor\log(2)/\varepsilon^j\rfloor\), a single rare species has asymptotic detection probability \(1/2\); between rare-species scales observed richness becomes deterministic; strict local maxima are ensured by choosing a sufficiently small transcendental \(\varepsilon\).

This verification documents a self-review of a mathematical claim. It provides neither an independent scientific audit nor confirmation that all potentially equivalent historical theorems have been found. The primary full text on infinite urn occupancy was compared; the inaccessible original rarefaction article and geometric-sample paper remain priority risks.
