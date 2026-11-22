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

## Reproducibility

From this package directory, run `python3 CHECK.py` with the Python standard library. The checker constructs the forced inverse and its finite-boundary correction for several positive diffusivity exponents, pure-power growth profiles, critical logarithmic profiles, and finite observation positions. It verifies the backward equation, correction derivative, admissible-domain exact identity and selected asymptotic derivative ratios, plus exact Gumbel-profile identities on both singular critical-distance scales. The packaged run passed 1131 finite assertions.

## Analytical checks and limits

The proof requires three independent identities: (i) the forced inverse derivative follows algebraically from the backward generator; (ii) the identity `exp(-U)=-d exp(-W)/dx` evaluates the tail integral exactly, including its nonzero boundary term when `W_inf` is finite; (iii) the residual-to-prescribed-time factor is `1-exp(-Q)`, with `Q=W_inf-W`, so regular-variation integration produces the sharp physical asymptotic. The finite checker is not a substitute for proving these identities, the integral divergence threshold, the inaccessible natural boundary or the infinite-distance asymptotics. No independent review has been performed.
