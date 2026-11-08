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

# Reproducibility and limitations

Run `python verify.py` with SymPy installed. The script checks the four equations imposed on a Grassmann chart by the Fermat cubic cone and the universal Taylor formula for an arbitrary homogeneous cubic. It also verifies the explicit local elimination at a Fermat flex, the nonflex square-zero equation, the Hessian's nine simple intersections, the flex nilpotent residue, and the Euler characteristic identity yielding \(6n+12\). The exact observed transcript is embedded in `verification_output.txt` and terminates with `ALL_CHECKS_PASSED`.

This is exact symbolic algebra over the rationals; no floating-point fitting or extrapolation establishes the universal theorem. The proof that every smooth complex cubic has nine simple flexes uses characteristic-zero elliptic-curve geometry. The identification of the first nilpotent layer with \(\mathcal O_E(1)\) uses the tautological Grassmannian bundle and the gradient exact sequence, not a numerical test. No independent mathematical audit has been performed.
