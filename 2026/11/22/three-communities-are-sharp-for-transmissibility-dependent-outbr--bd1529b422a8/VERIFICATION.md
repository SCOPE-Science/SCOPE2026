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

## Executed checks

Run `python3 verify.py` from the extracted package directory. The checker requires the Python standard library only. It validates all rational numerical witnesses that appear in the proof, confirms positivity and row sums of the explicit matrix, iterates the survival fixed-point equations for two tested transmissibility scales, and checks the two-type sign relation for a deterministic randomized sample of positive matrices. The analytic proof establishes the universal theorem; finite checks serve only as consistency tests.

At \(\tau=1\), the computed survival vector is approximately \((0.0058185383,0.7968144267,0.0008913727)\). At \(\tau=20\), the first two survival probabilities are so close to one that binary64 rounds both to one. Their strict ordering is established instead by the exact exponential bounds in `RESULT.md`; the checker compares the respective logarithmic extinction exponents and does not claim to resolve their probability difference in binary64.

## Limits

The evidence is mathematical and self-reviewed, not independently audited. No exhaustive search of all possible historic publications was possible. A non-accessible supporting appendix about overdispersed offspring does not affect the Poisson calculations, but remains a literature-coverage limitation.
