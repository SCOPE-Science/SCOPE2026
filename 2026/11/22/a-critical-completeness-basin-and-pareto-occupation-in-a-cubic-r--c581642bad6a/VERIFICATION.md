---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope

Execute `python3 verify.py` in a Python 3 environment using only the standard library. The script checks Fourier-coefficient identities for the linear inverse-square equation at exact rational inputs, the critical-angle identity for multiple real parameters and both signs, and the exact area formula against an independently evaluated quadrature for multiple radii. It also checks the analytically derived exponential radius at the indicated angular phases on representative complete trajectories; these phases are not times of radial maxima.

The all-parameter and infinite-time assertions are proven analytically in RESULT.md, not by finite experiments. At critical anisotropy, the proof separates positive, zero, and negative homogeneous-solution coefficients and treats nonzero boundary data and the origin. The area expression follows by exact integration of disk chords, not partial sampling. Time occupation uses dominated convergence on each full turn and an explicit null set of exceptional angles.

The source literature already supplies the general Bernoulli radial formula and the existence of limit-cycle connections at infinity. The scientific addition assessed here is the exact critical complete-initial-condition geometry and original-time occupation tail. Historical-priority uncertainties, including one inaccessible older cubic classification full text, are described in REVIEW.md and AUDIT.json. Independent mathematical audit has not been performed.
