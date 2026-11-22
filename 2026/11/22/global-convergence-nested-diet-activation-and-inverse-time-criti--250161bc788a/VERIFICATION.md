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

# Verification record

The primary arguments are the explicit scalar water-level equation, the exact dissipation identity for the joint entropy functional, the invariant-set argument, and the critical two-source asymptotic convolution calculation in `RESULT.md`. Their hypotheses and end-point equalities are stated there. A finite numerical sample is not used as proof of global convergence, sharpness in continuous parameters, or inverse-time asymptotics.

Run `python check.py` with NumPy and SciPy. On the supplied local execution it passed:

- 1,500 random dimension/parameter tuples checking the water-level equilibrium identities, exact Lyapunov derivative identity, and its sign;
- 9 independent long-time numerical integrations at 3 population pressures and 3 adaptation speeds;
- critical two-source integration at 3 late times, with computed \(t x_2(t)\) equal approximately to \(0.298957\), \(0.299741\), and \(0.299860\) at \(t=1000,5000,10000\), consistent with the proved \(3/10\) limit.

The code uses a fixed random seed and makes no network requests. The software and finite computations do not certify mathematical originality. Historical priority and independent external audit have not been established. The result does not calibrate biological rates or validate the model against field data.
