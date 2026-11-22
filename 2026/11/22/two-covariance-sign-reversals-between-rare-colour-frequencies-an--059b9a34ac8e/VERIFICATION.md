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

# Verification details

The pure-Python checker in `check.py` independently enumerates every ordered sample word on a bounded grid of 2- and 3-colour schemes using rational weights derived directly from the sequential predictive rule. For each word it computes temporal changes and exact-frequency colour counts separately, then compares their empirical exact covariance to the analytical covariance. The run completed 186 parameter/frequency cases and symbolic checks of root-critical identities without assertion failures. Independent enumeration is a finite diagnostic; the uniform-position and conditional Pólya expectation argument and strict quadratic sign proof in RESULT.md supply the infinite mathematical conclusion.

The initial mass is a positive real and may be rational or irrational. The checker samples rational values only; the proof handles all positive real masses. The large-frequency scaling is likewise verified symbolically, not by a finite truncation argument. No independent mathematical audit or external certification has been performed.
