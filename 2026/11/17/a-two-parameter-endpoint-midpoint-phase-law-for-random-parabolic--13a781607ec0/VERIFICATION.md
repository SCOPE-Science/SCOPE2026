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

The proof in `RESULT.md` is analytical. It uses direct tangent-line intersections, a unique global maximum, a nonnegative deficit decomposition, explicit scaling of three ordered tangency locations, an integrable dominating function for each fixed \(p,q>0\), and the gamma-function simplex integral.

Run `python check.py` with the dependencies in `requirements.txt`. The checker independently calculates line-intersection triangle areas for 1000 deterministic-seed triples; normalizes three beta–Jacobi densities; evaluates exact finite-threshold survival probabilities by nested adaptive quadrature for the cases \((p,q)=(1,1),(2,2),(1,3)\) and thresholds \(0.025\) and \(0.007\); and checks the limit prefactor against their predicted rates. It also checks the exact uniform specialization \(32\sqrt2/45\). The observed finite-threshold/predicted ratios approach one as the threshold decreases.

Successful execution prints `JACOBI_TANGENT_TWO_SCALE_TAIL_DIAGNOSTICS_OK`. Finite quadrature and samples are evidence of implementation consistency, not an infinite proof. The historical priority of the variable-density theorem is not independently certified.
