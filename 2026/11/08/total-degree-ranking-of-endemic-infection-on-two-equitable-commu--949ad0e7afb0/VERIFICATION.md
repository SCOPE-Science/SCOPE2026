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

# Verification and limits

- The attached `check.py` was executed using Python 3 standard-library exact `fractions.Fraction` arithmetic and returned PASS.
- Verified a labeled six-vertex graph is connected and has the claimed equitable quotient, degrees and isolated threshold values.
- Verified rational subsolution \((855/1000,896/1000)\) and supersolution \((858/1000,899/1000)\) by evaluating the full rational polynomial quotient map. Combining the inequalities with monotonicity and uniqueness proves the exact coordinate enclosure.
- Enumerated all cross-degree integer possibilities for the only unequal positive internal-degree configuration on five vertices, proving the stated minimality boundary.
- Verified the symmetric three-cell quotient and the exact Rayleigh lower bound \(137/26>26/5\). The three-cell ordering reversal is an analytic near-threshold consequence of its positive Perron vector.
- Verified strict all-parameter inequalities in the mathematical proof analytically, using the second derivative of the product map, Perron-vector comparison and connectedness of the supercritical parameter region. A finite computer check is not evidence for the infinite-parameter quantifier.
- No claim is made of independent peer review, a stochastic stationary distribution, or global transient convergence.
