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

# Reproducibility and limits

Execute `python verify.py` with the Python standard library. It checks exact-fraction boundary identities and simplex sums, representative parameter grids on both sides of the sharp frontier, the exact \((\rho,\tau)=(5,1)\) witness, the \((5,4/5)\) equality case, and rational unsafe-interval endpoints at \((8,1/4)\).

The complete proof is in `RESULT.md`: (i) directly modeled components are nonnegative; (ii) the reconstructed component is affine decreasing in the susceptible fraction at fixed infected fraction; (iii) boundary evaluation gives the exact factor \(1+\tau\rho-\tau\rho^2i(1-i)\); and (iv) maximizing \(i(1-i)\) on \([0,1]\) proves both directions, including all boundary cases. Universal conclusions do not rest on finite tests.

For learned rate outputs different from \(G_I=\beta SI\), \(L_S=\beta I\), \(L_I=\gamma\), this proof does not apply. Independent mathematical audit has not been performed.
