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

The `CHECK.py` file reproduces the volume and surface area through two independent algorithms: (1) enumerating feasible intersections of defining hyperplanes and computing the convex hull's ordinary Euclidean volume and boundary area; (2) diagonalizing the transfer matrix and evaluating the analytic derivative formula. It checks \(s=3,4\) at several link ratios straddling \(t_*=1-1/\sqrt2\) and at \(t=1/2\), plus \(s=5\) at \(t=0.3\). It additionally tests the derivative identity and numerical improvement for dimensions three through twenty.

These finite tests support but do not replace the all-dimensional proof from first variations and strict Brunn–Minkowski concavity. A successful checker run does not establish historical priority or constitute independent mathematical audit. No general link range beyond \(0\le t\le1/2\) is claimed.
