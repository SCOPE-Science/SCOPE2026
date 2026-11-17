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

# Reproducibility and verification

The analytical check uses the exact determinant formula \(V=D|z-h|/6\), the normalized latitude density, the bound \(p_\varepsilon/\varepsilon\le6/D\) and the integrable inverse-distance identity. A separate deterministic quadrature of the projected-sphere Coulomb potential at transverse radii \(0,1/4,1/2,4/5,19/20\) yielded \(\pi/2\) to numerical quadrature accuracy. The inverse-distance transform identity is established in the proof rather than entrusted to these calculations.

Execution: `python check_nearflat_tetra.py` using `requirements.txt` (NumPy). The provided script integrates over the fourth point exactly in latitude and samples only three first vertices, providing a lower-variance check of the rare event. With 1,500,000 triples and the fixed seed, completion message `SPHERE_TETRA_SMALL_VOLUME_UNIFORM_CHORD_OK` was observed. At \(\varepsilon=0.0001\), estimated \(\Pr(E_\varepsilon)/\varepsilon\) was 9.2860 (analytical limit \(3\pi\)), and weighted chord mean was 1.0134 (analytical limit one). Slower convergence is expected because of near-collinear first-three-point events; the checker tests finite approximations only.

No independent audit or formal verification is represented. Unavailability of the complete Miles (1971) text is a historical-priority limitation, not a mathematical proof gap.
