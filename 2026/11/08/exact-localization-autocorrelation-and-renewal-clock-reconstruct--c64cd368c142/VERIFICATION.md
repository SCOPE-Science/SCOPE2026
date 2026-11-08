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

# Reproducibility checks

Run `python3 CHECKER.py` using only the Python standard library. The finite checker covers exponential-clock exact correlations, a deterministic-clock compact-support boundary, three Lomax inversion examples, two independent stationary two-time Monte Carlo experiments, and five power-law parameter classes against a numerical logarithmic derivative. The exact all-parameter result follows from the renewal argument in `RESULT.md`; no finite experiment proves the continuum of waiting laws, the inverse theorem, or the weak-reset asymptotics.

The original one-time stationary atom is independently obtained from \(1-\mathbb E[e^{-rW}]=r\int_0^\infty e^{-rt}\Psi(t)dt\). No independent audit or experimental verification was performed.
