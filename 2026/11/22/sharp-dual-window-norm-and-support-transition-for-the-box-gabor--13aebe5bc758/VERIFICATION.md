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

# Verification of the box-window dual transition

The analytic proof in `RESULT.md` is sufficient for the claimed continuum: it uses the Janssen–Ron–Shen duality identity and exact interval inclusion. The lower bounds and equality cases do not require numerical experiments or the finite reduction from the primary paper.

To replay the supplementary exact arithmetic tests, run `python3 CHECK.py`. The program enumerates rational modulation values strictly between the two thresholds, derives the complete partition of each fiber on which box membership is constant, checks all duality equations for shift indices from minus five to plus five, and checks the sharp fiber costs. Its observed final output is: `PASS: 59 rational parameters; 26532 exact correlation identities, plus fiber cost checks`. This script does not prove the result for irrational parameters, and does not constitute independent mathematical validation.

The case at the upper endpoint and all other window shapes are outside the claim. A self-review was performed; no independent audit has been performed.
