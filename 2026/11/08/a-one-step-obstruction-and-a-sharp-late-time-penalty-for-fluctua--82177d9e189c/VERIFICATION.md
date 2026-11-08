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

Run `python verify.py` using Python 3 with installed NumPy and SciPy. The recorded execution passed 168 checks and returned modes \(u_2=1.253877441969\ldots\), \(u_3=3.047804959898\ldots\), and \(u_5=8.463252358833\ldots\). The program constructs independent finite killed-generator evolution, checks exact rational Taylor jets, checks derivative signs and mode bounds, compares exact Bernoulli-clock mixtures with generator evolution, and tests the sharp leading \(t^{-3/2}\) coefficient at increasing horizons.

All numerically truncated generators used for tests have upper boundaries far enough from the starting state that their observed finite-horizon effects fall below the stated tolerance; their outputs are not claimed to be exact infinite-half-line certificates. The theorem for arbitrary positive bounded rate laws, every integer starting site and all horizons is derived analytically in `RESULT.md`, not inferred from finite tests. No independent external proof audit has been performed.
