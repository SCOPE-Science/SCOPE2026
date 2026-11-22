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

The main proof consists of two matching certificates. In the supercritical regime, \(z=2(abT^2-1)/(2abT+a+b)\) gives positive matrices \(P\pm M\), with the nontrivial determinant reduced identically to zero; this proves the operator and completely bounded upper bound \(1+z\). The unit vector with partwise coordinate squares \(\alpha=(bT+1)/(2abT+a+b)\) and \(\beta=(aT+1)/(2abT+a+b)\) yields a two-dimensional residual discriminant exactly \(T^2\), and hence an attained trace-norm lower bound \(1+z\). These are exhaustive algebraic and operator arguments for all dimensions and all real \(t\).

The standalone standard-library script `VERIFY.py` passed with output:

```
BICLIQUE_EXACT_IDENTITIES_OK 909454
```

The script checks rational positive-order, normalization, discriminant, witness, idempotent-boundary and supplementary parameter identities over explicit finite ranges. The countably infinite conclusion is proved analytically by a diagonal conditional expectation and a pair of unitary conjugation maps, together with finite-corner exhaustion; no extrapolation from the script is used.

Literature comparison covers the established unweighted projection \(T=1\), the singleton-class weighted star, and the general positive-order Schur multiplier theorem. It does not certify global priority against every possible older equivalent matrix-norm formula. No independent audit has been performed.
