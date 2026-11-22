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

The proof is analytic. The main checks are (i) the exact variation-of-constants identity and uniform tail estimate, (ii) the strict difference-amplification inequality with \(\lambda=\mu-B>1\), (iii) contractions on one-sided and bilateral bounded sequence spaces, (iv) the unit-circle eigenvalue exclusion by homotopy, and (v) the three-equilibrium sharpness construction. The standalone `check.py` carries out supplementary symbolic and finite numerical diagnostics and prints `VERIFY_OK` when they pass.

No finite test is used to certify an infinite quantifier. The theorem concerns real unwrapped trajectories, \(\mu>1+B\), and a *coefficient-uniform* threshold. Endpoint and weak-feedback behavior are not resolved. Full comparison with the general Chen–Li invariant-manifold paper remains limited by publicly accessible text. Independent audit: not performed.
