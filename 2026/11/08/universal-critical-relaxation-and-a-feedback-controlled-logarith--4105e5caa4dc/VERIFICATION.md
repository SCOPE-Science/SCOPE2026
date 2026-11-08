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

# Reproducibility and limits

Run `python verify.py` with Python 3 and the SymPy package from `requirements.txt`. The checker tests six exact symbolic coefficient relations, two feedback leading-jet equalities, five symbolic/parameter assertions for the sign-change family, and 576 exact rational jet-residual coefficient checks from the original four-compartment differential equations for both feedback choices. Algebraic identities are checked over symbolic parameters subject to nonzero positive denominators; their positivity ranges and the full asymptotic theorem rely on the written proof in `RESULT.md`.

The global convergence proof uses the exact critical infected equation, two stable linear comparison estimates, ratios, and convolution decay. The logarithmic constant is established by an integrable derivative estimate, not by fitting numerical trajectories. A finite-time numerical IVP trial at two feedback strengths and both definitions was consistent with the leading coefficient and logarithmic correction, but numerical output is not treated as proof or an independent check of the asymptotic limit.

The routine does not prove exhaustive literature originality or independently certify the mathematical argument. Independent audit: not yet performed.
