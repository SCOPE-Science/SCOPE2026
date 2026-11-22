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

The symbolic proof independently establishes all values of \(m\ge3\) and all positive exponents. The standalone `verify_power_maps.py` independently implements Demazure multiplication using right descents, rather than constructing product powers from the asserted closed formula. It enumerates powers, image fibers, idempotent-root counts and first absorption times for \(3\le m\le80\), and checks associativity for \(3\le m\le9\). Its recorded output in `checker_output.txt` reports `PASS` and 380120 checked element powers. It also checks sample probabilities at three larger dihedral parameters; those numerical checks are not used to prove convergence.

**Limits:** Finite examples do not prove the infinite assertion or exclude unlocated priority claims. The result is a power-map classification for one Coxeter family, and does not claim uniqueness of the heavy-tailed limiting law across all monoids.
