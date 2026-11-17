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

The analytic proof is in `RESULT.md`. The standalone `pedal_moment_check.py` uses Python's standard library and exact rational arithmetic, without downloads or external packages. Execute `python3 pedal_moment_check.py` in the same directory. The checker tests four exact barycentric projections in each of an acute, right and obtuse triangle and compares the area ratio with its circumcenter expression; it recomputes the Dirichlet moments and the Heron–circumradius identity for all three geometries and checks the distinct one-moment witness. The successful observed terminal marker is `PEDAL_MOMENT_TOMOGRAPHY_CHECKS_OK`.

The finite rational checks do not constitute the proof for the continuum of triangles, which rests on exact symbolic integration and Vieta's theorem. No independent audit, external certification, or statistical noise analysis is claimed. The earliest day-precise archived online source is dated 2009-01-20; the original printed Steggall article is from February 1893, for which an exact day was not verified.
