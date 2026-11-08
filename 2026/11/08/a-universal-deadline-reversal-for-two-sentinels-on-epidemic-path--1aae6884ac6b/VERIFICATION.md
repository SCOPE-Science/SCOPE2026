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

The proof uses the independent exponential passage times along each unique path and their left/right independence to obtain an exact finite-time formula. The short-horizon comparison follows from cut-edge counts. The long-horizon comparison follows from exponential-order separation, \(e^{-2x}\) versus a lower bound \(e^{-x}\) for any pair leaving a path endpoint unobserved. Four-vertex symbolic formulas provide the unique positive switch and equal mean values.

The extracted standalone `verify.py` was run successfully. It performed 336 comparisons between the path formula and the full infected-subset continuous-time Markov generator, along with 950 sampled short/long comparisons. Symbolic identities and mean-time integrations passed. These finite checks are not treated as substitutes for the general proof.

No independent audit or external validation has been performed. Historical priority is limited by the inspected sources and remaining possible first-passage/reliability equivalences.
