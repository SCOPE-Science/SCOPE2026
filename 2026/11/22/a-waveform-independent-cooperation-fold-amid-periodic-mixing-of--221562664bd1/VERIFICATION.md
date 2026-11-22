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

The analytical proof is in `RESULT.md` and is the basis of the universal parameter assertions. Execute `python verify.py` with dependencies in `requirements.txt`. The checker performs exact SymPy assertions for stationary vertex coefficients, the unique game-composition pin, the radical expression for the neutral fold, and the cosine small-forcing coefficient; it then solves six Poincaré double-point systems (two frequencies and three amplitudes) with SciPy and integrates eight finite-amplitude neutral trajectories (two frequencies, two amplitudes, two waveform shapes). All checks passed when extracted from these files. The differential identities proving the infinite-parameter and arbitrary-waveform results are not inferred from those finite runs. No independent review has occurred.
