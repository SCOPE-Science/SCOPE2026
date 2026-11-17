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

# Checks performed

The mathematical argument is reconstructible from the polar arclength density \(q/P\), the exact segment distance \(ab|\sin\delta|/\sqrt{a^2+b^2+2ab\cos\delta}\), the angular-window sandwich, and the integral identity for the deficit. The proof explicitly includes flat sides, corners, a.e. radial derivatives, quantifier order, and sharpness by a strictly convex perturbation.

The standalone `checks/central_chord_check.py` ran with Python, NumPy and SciPy. It computed \(\kappa_{[-1,1]^2}=0.5738967873481594\), independently checked the value from the opposite-side endpoint-coordinate diamond with \(d=|u|/\sqrt{1+v^2}\), verified the elementary square closed form, and measured stability ratios 1.00000075, 1.00067444 and 1.0074324 for radial perturbations of sizes 0.001, 0.03 and 0.1. A simulation of 3,500,000 independent pairs of square-perimeter points used clipped segment distances, with hit-probability/linear-asymptotic ratios approximately 1.0058, 1.0055, 1.0106, 1.0161 at radii 0.04, 0.02, 0.01 and 0.005. All diagnostics completed with `CENTRAL_CHORD_INTENSITY_DIAGNOSTICS_OK`.

Numerical tests cannot establish the universal inequality or archival novelty; the literature comparison is necessarily finite and the potentially related 1981 Ehlers–Enns surface-random-secant study and a 2014 containment paper were accessible only by abstract. Neither independent mathematical review nor independent historical validation is claimed.
