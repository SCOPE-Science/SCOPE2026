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

Exact-rational verification: `python verify.py` with standard Python 3. The program reported `PASS 56706 exact-rational step assertions` on the supplied source file. Tested graph orders 3–9, all admissible common-neighbor degrees, varied additional graph edges, random rational perturbations, five forgetting regimes, exact first-activation formula and equality cases. These computations test only finite cases; the universal assertion follows from the matrix and induction proof in RESULT.md. The proof and test use strict receptivity, so equality with the confidence bound is not an interaction. Independent external audit has not been performed.
