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

# Verification record

The exact polynomial identities and finite numerical tests can be reproduced from `verify.py` using Python 3 with SymPy and SciPy installed, by executing `python verify.py` in the directory containing the accompanying files. Four polynomial orders were checked symbolically; four positive-parameter cases were integrated through 30 complete turns; eight cases at the first radial order were integrated through logarithmic-radius time \(s=140\). All scripted assertions passed.

For the infinite-time statements, the operative mathematical evidence is the analytic proof in `RESULT.md`: exact radial reduction, the explicit scalar supersolution for finite turning, the divergence criterion for infinite turning, and the frozen-period/slow-radial-variation comparison giving the limiting inverse-radius increment. The numerical comparisons are illustrative rather than exhaustive. The initial conditions and parameters in the checker are concrete samples; no software test substitutes for the proof of the universal hypotheses.

No independent mathematical audit, external certification, or generalized perturbation analysis has been performed.
