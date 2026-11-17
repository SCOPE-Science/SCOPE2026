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

# Verification

The companion `checker.py`, run with Python 3 and no third-party packages, asserts exact rational sign changes for the deterministic four-return fixed point, an exact multiplier enclosure \((-0.031,-0.030)\), and an exact noise-mean-coefficient enclosure \((-0.548,-0.546)\). It solves the four-periodic second-moment and mean recurrences without floating-point proof assumptions. Expected diagnostic output includes `CHECKED: variance/mean recursions yield -0.548 < coefficient < -0.546`.

Analytic reasoning, rather than finite experiments, establishes existence and uniqueness of a stationary measure on the four-interval trapping set, differentiability of the stationary pullback response, and the actual asymptotic inequality. The supplied proof explicitly uses bounded independent uniform noise and the local contraction of four-step compositions. The checker neither proves global attraction nor tests publication priority, and no independent mathematical audit is reported.
