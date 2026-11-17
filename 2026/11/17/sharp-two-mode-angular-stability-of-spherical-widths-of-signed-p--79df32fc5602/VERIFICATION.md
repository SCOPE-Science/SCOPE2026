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

# Reproducibility

The mathematical result uses the Euclidean unit sphere and all signed-permutation orbit vertices. Run `python3 verify_signed_width.py` from this directory with a standard Python 3 installation; no external modules or network access are required. Its successful completion marker is `SIGNED_B_PERMUTO_WIDTH_EXACT_PASS`.

The checker independently enumerates every ternary sign-support pattern through dimension eight, uses exact integer inequalities for the centered-step and unsigned-step certificates through dimension eighty, and checks both sharp pure-mode witnesses and 51,816 deterministically chosen integer tangent vectors. It does not certify all real perturbations numerically. The all-dimensional proof is the rearrangement identity, the strict stratum argument, the positive upper-step decompositions, and the exact spherical tangent decomposition in `RESULT.md`.

The fixed-angle formula holds for \(0<\theta<\arctan(1/(2\sqrt{k}))\) and is not asserted beyond that range. Historical priority is provisional. No independent mathematical audit has been performed.
