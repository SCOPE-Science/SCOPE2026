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

# Verification details

The theorem is established by the explicit arrowhead spectral projector, its ordered sign blocks, the strict convex-order inequality for the initial slope, and the generalized Descartes bound on zeros of exponential sums. Each step, including repeated conductances, is proved in `RESULT.md`.

For a reproducible independent numerical spot check, install `numpy` and `scipy` and run:

```bash
python verify_star.py
```

The checker reconstructs the symmetric weighted graph Laplacian and uses `scipy.linalg.eigh` and `scipy.optimize.brentq`. It checks the leaf-pair identity \((L^2)_{ij}=w_iw_j\), the nonnegativity window, hub–leaf positivity, row-sum preservation, and sign changes on 216 weighted configurations/orders, yielding 1,608 pair-level trials. Tested examples include repeated weights and several unequal-weight configurations. This checker passed in the present package. It uses floating-point arithmetic, so it is not a formal certificate, exhaustive search, proof of unique roots, or independent validation. The universal proof is analytic and does not assume untested numerical limits.

A simple symbolic check is the uniform star formula, where all leaf pairs share the kernel
\[
\frac1{m+1}-\frac1m e^{-tw^\alpha}+\frac1{m(m+1)}e^{-t((m+1)w)^\alpha}.
\]
The proof's ordering argument also treats nonuniform and tied weights by class-level spectral projections; it does not extrapolate the uniform example.

Scientific limits: only symmetric combinatorial weighted stars with strictly positive spokes are covered. The times of positivity recovery are implicit finite spectral roots, and the identity of the last leaf pair is not generally resolved. Independent audit is unperformed.
