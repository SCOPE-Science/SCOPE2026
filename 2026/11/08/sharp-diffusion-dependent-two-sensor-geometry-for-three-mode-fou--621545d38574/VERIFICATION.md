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

The analytical block reduction is exact for the raw sample matrix with columns corresponding to Fourier frequencies \(-1,0,1\). The determinant \(8u(1-q)^2\) of the even Gram block and the odd Gram eigenvalue \(4(1+q^2)(1-u)\) establish the precise rank boundary. Strict monotonicity of the smaller even eigenvalue and the odd eigenvalue gives the global maximum, and the crossing quadratic yields its unique root in \((1/2,1)\).

The bundled standalone script `CHECK.py`, requiring Python 3 and NumPy, executed with `HEAT_TWO_SENSOR_CHECKS_PASS 1695`. It checks 549 direct matrix spectra across nine time parameters, over a thousand competing-angle inequalities, special-rank cases, and the two endpoint limits. Finite checks do not establish universal validity; the proof is contained in `RESULT.md`. No independent audit has been performed.
