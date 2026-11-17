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

# Verification and limitations

The proof independently establishes all positive edge lengths and arbitrary integer \(m\ge2\) by Kirchhoff reduction, exact integration, Cauchy–Schwarz, and a three-variable symmetric-polynomial bound. The standalone `check_resistance.py` assembles resistor network nodes including the two sampled interior points and solves grounded Kirchhoff equations, independently of the derived formulas. It tested 400 direct pairs, independently integrated the resistance kernels, compared Gauss quadrature against the symbolic expectation, tested 99 cycle subdivisions, and assessed 40,000 three-arm length vectors. It reported `DIRECT_CIRCUITS_AND_EXACT_MEAN_OK` and `THREE_PATH_SHARP_BOUNDS_AND_TWO_PATH_INVARIANCE_OK`.

Run `python3 check_resistance.py` with NumPy installed, using the accompanying dependency declaration. These finite checks corroborate the proof only and cannot certify infinite-domain claims. An independent mathematical or historical audit has not been performed. The bound \(\mathbb E R<L/6\) is strict for positive lengths and its limiting value is unattained.
