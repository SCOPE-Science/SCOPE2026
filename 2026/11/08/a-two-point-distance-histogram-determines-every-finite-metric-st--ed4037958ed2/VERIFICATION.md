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

# Verification scope

Run `python3 check_star.py` from the same directory as this file. The program uses only the Python 3 standard library. It checks the exact distributional-kink measure and collision-safe inverse reconstruction for 77 positive rational arm-length lists, including repeated lengths and additive coincidences; it checks density normalization for each case, 230 exact kink jumps, and equality between the one- and two-arm interval laws at 20 rational distances per subdivision. A 140,000-pair Monte Carlo test checks a separate mean-distance identity against direct random point sampling.

Expected successful output begins `CHECK_OK exact_inverse_cases=77 integrated_laws=77 kink_checks=230 interval_equivalence=checked monte_carlo_pairs=140000`. There are no downloaded inputs, nonstandard dependencies, claimed formal proof certificates, or externally delegated audits. Exact rational arithmetic verifies the sampled finite identities, while the written proof establishes the theorem for arbitrary positive real arm lengths. The verifier does not prove historical novelty or noise robustness.
