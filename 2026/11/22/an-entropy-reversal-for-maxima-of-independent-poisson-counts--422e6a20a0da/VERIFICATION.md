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

The discrete law was evaluated using \(p_k=e^{-\lambda}\lambda^k/k!\), \(F_k=\sum_{j=0}^kp_j\), and \(r_k=p_k\sum_{j=0}^{m-1}F_k^{m-1-j}F_{k-1}^j\). The standalone `checker.py` calculates its Shannon entropy by summation and the Gaussian maximum second moment by fixed-step numerical quadrature. It tests sample sizes 2, 3, 5 and 10, the positive small-intensity and negative large-intensity differences, the small-intensity leading terms, and the exact limiting constant \(1/2-\log2\) when \(m=2\). These are numerical consistency checks, not certificates of every parameter or infinity-limit claim.

The complete analytical proof establishes the small-intensity entropy-tail control, uniform integrability needed for the large-intensity logarithmic term, Gaussian maximum entropy strictness, and crossover existence for all fixed integers \(m\ge2\). No zero uniqueness, explicit universal crossing intensity, growing-sample asymptotics, or external independent verification is asserted. Invoke `python checker.py` with Python 3 and the standard library only.
