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

Run `python3 verify.py` in the same directory as `RESULT.md` to reproduce numerical and deterministic checks. The checker uses only the Python standard library. It directly enumerates the eight projected vertices for 25,000 independent random unit normals, tests the predicted integral CDF against 100,000 freshly generated samples, checks monotonicity on 159 interior thresholds, and compares numerical limiting coefficients near both endpoints and the interior transition. The checker returned `CUBE_SHADOW_RADIUS_PHASE_LAW_OK 100000 25000 159` on the packaged source.

The analytic steps are the signed body-diagonal norm minimization, the 48-chamber spherical integral, a quadratic onset from a shrinking integration interval, six local diamonds near coordinate-axis normals, and four transverse great-circle strips near the maximal radius. These are the proof obligations; the numerical experiments cannot establish the continuum claim or originality. Independent audit has not been performed.
