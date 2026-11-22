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

The exact-rational checker `check_bcc_tail.py` ran on the package's actual source and reported 24 Voronoi vertices, minimum squared pair separation \(1/8\), Voronoi volume \(1/2\), covering radius squared \(5/16\), and coefficient sequence \(128,1024,53248/5,2097152/15,15204352/7,266338304/7,229252268032/315\) in powers \(\varepsilon^3\) through \(\varepsilon^9\). The checker independently enumerates intersection candidates from all 14 exact rational supporting inequalities and checks the cone identity and Jacobian.

The universal identity for the continuous cell, the exact probability for every \(0<\varepsilon<1/64\), and convergence of its series are analytic arguments in `RESULT.md`; finite enumeration is not an infinite proof. The checker neither verifies novelty nor supplies external or independent validation. No independent audit has been performed.
