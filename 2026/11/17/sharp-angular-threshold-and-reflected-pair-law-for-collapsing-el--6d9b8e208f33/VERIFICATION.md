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

# Verification and reproducibility

The theorem is proved by the exact ellipse-chord identity, a geometric angular localization argument, a local blow-up at reflection-paired parameters, and dominated convergence plus Scheffé's lemma. Every limiting step is written out in `RESULT.md`.

Run `python verify.py` using Python 3 with NumPy and SciPy installed. It verifies the chord identity and compares independently computed Euclidean-angle event probabilities with the three theoretical leading coefficients (at \(110^\circ\), \(120^\circ\), and \(140^\circ\)). Importance sampling is restricted to the proved leading-order reflected-pair bands; it cannot replace the analytical argument for negligible complementary cases.

The numerical results for the smallest tested aspect \(\varepsilon=0.002\) are close to the stated constants, with no assertion of exact equality at a positive aspect ratio. Neither the code nor these checks performs an independent mathematical audit, establishes publication priority, or verifies unexamined literature.
