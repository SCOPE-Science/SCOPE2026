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

Run `python checks/check_parabolic_circumradii.py` with Python 3, NumPy, and SymPy. The actual standalone run printed `PARABOLIC_CIRCUMRADIUS_ENDPOINTS_CHECKS_OK`.

Analytic tests reconstruct the Vandermonde determinant, verify the Hessian matrix \(H=I_3+\mathbf1\mathbf1^{\mathsf T}\) with determinant \(4\), and compute the exact \(-1/5\) spherical mean of the quartic correction. Deterministic spherical quadrature at \(\varepsilon=0.01,0.03,0.06\) agrees with the two-term lower coefficient to absolute error below \(0.003\) after division by \(\varepsilon^{3/2}\) for \(a=1\). Direct chord-and-area circumradius calculations were compared against the product formula at 200 independent test triples. The upper-corner gradient was checked at three positive arc widths.

Finite quadrature and numerical examples are not proofs of asymptotic or conditional total-variation statements. The proof in RESULT.md establishes the global extremizers, localizations, volume expansions, uniform remainder bounds at fixed \(a>0\), and convergence in total variation. No arclength-uniform result, full cumulative distribution, or independent mathematical validation is claimed.
