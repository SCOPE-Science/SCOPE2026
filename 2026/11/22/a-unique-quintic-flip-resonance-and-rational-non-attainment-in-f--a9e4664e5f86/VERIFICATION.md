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

# Reproducible checks and their limits

Install the dependencies in `requirements.txt` and execute `python3 verify.py` from the extracted package. The expected marker is `GRAZING_FLIP_PHASE_CHECK_OK`.

The checker verifies with exact symbolic algebra the cubic doubled-return coefficient, the fact that its quartic coefficient vanishes when the cubic does, and the explicit negative quintic coefficient on the degeneracy locus. It checks rational examples where the phase switches, evaluates the quintic jet at three independently solved critical exponents using 75-digit arithmetic, and directly iterates sample physical maps to verify the claimed branch itinerary.

The finite tests are not a proof of the universal claims. The text proof establishes their quantified ranges. A sharp fourth-root asymptotic is derived analytically from the local quintic return, not from numerical long-run fitting. The result is local and no external independent review is asserted.
