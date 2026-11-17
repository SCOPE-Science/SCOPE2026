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

# Reproduction and limits

Run `python verify_endpoint.py` with SymPy, NumPy, and SciPy installed. The checker reconstructs from the Bloch--Wigner differential identity the homogeneous Taylor terms up to order four, differentiates the complete source density including both logarithmic terms, and simplifies the angular coefficient exactly. It verifies the closed form against independent quadrature of the original positive simplex integral, and confirms the two-term probability law numerically for three finite deficits.

The symbolic calculations are local finite identities. The proof of the global maximizer, the reduction to two local caps, and the analytic \(O(\varepsilon^3)\) remainder are mathematical arguments in RESULT.md, not claims inferred from finite tests. The source supplies the density; it does not independently certify this asymptotic claim. Independent mathematical audit has not been performed.
