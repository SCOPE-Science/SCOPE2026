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

Run `python verify.py` with `mpmath` installed. The script reconstructs the full linearized six-state matrix, calculates the eigenvalue from zero at small spatial frequency by a high-precision eigensolver, and computes the difference between heading and bisector directions. Its measured coefficient, normalized by the exact sixth-order prediction, approaches one as the wave number decreases, with the discrepancy shrinking when the wave number is halved in all four tested parameter pairs. It also checks the exact half-filled eigenvector equation at nonzero wave numbers and angles, and verifies the angular winding denominator. The checks executed successfully. The existence of a uniform small-wave-number analytic branch and the exact angular coefficient are established in `RESULT.md`; finite numerical evaluations do not constitute a proof of any asymptotic series.

The assumptions are the six-component deterministic PDE, positive finite Péclet number, occupancy strictly between zero and one, and the local eigenvalue branch emerging from the conserved density. No direct microscopic simulation, nonlinear phase-separation assertion, independent audit or publication-priority certification is supplied.
