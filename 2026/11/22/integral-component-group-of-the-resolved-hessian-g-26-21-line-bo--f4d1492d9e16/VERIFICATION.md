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

# Reproducible verification

Run `python verify.py` with the SymPy dependency described in `requirements.txt`. The checker rebuilds every projective intersection in exact \(\mathbb Q(\omega)\) arithmetic, reconstructs the 42-vertex graph, verifies 132 nodes and genus 91, computes the rational Schur determinant and characteristic polynomial, and checks five local Smith lists for two different choices of deleted vertex. Its required success marker is `G26_HESSIAN_STABLE_BOUNDARY_INTEGRAL_CRITICAL_GROUP_OK`.

The p-adic eliminations are exact modular integer operations: the working modulus for each prime is \(p^N\) with \(N\) larger than the determinant valuation, so an elementary divisor cannot be mistaken for zero. No external mathematical validation has been performed. Results beyond the precisely specified stable curve and unit-thickness regular semistable smoothing are not asserted.
