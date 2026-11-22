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

# Reproducibility checks and limits

Run `python verify.py` with standard Python 3.9+ and no external packages. The program deterministically checks the two-observation secant intercept against directly computed reciprocal velocities, the analytic bias bound and sample-date monotonicity, the exact apparent-exponent formula against its derivative definition, strict location and sign of the exponent maximum, the equal-amplitude constants, asymptotic checks at large amplitude ratios, and the Cauchy–Schwarz gap for mixtures with more than two modes.

Actual replay: `PASS: 14809 deterministic numerical checks; universal results require the written proofs`.

Critical infinite-parameter steps are proved in `RESULT.md`: Cauchy–Schwarz with equality characterization; strict concavity and secant comparison; rational intercept algebra; strict monotonicity of the auxiliary critical cubic; and the asymptotic balance. Randomized finite checks, floating-point comparisons and passing output alone do not prove universal statements. The scripts do not validate a physical slope, observation hardware, safety threshold, or independent scientific priority.
