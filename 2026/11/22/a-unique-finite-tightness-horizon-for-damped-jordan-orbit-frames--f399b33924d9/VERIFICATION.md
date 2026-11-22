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

# Verification and reproducibility

Run `python3 verify.py` using Python 3 and only its standard library. The checker evaluates the exact centered Gram matrix against independent Simpson integration for random complex generators, tests the determinant invariance and optimality at arbitrary noncentral generating vectors, verifies the weighted-moment identity, and checks monotonicity and unique root behavior for positive parameter examples. It printed `VERIFY_OK 862 independent numerical assertions`.

The infinite-parameter theorem is proved by explicit exact integration, the two-by-two spectral trace–determinant identity, and strict monotonicity of \(s/\sinh s\); the finite tests cannot independently certify that theorem or historical novelty. The frame normalization is Lebesgue time measure on \([0,T]\), Euclidean state norm and the ratio of the optimal upper and lower bounds. Analytic limits at zero and infinity are stated in the main result. No independent mathematical audit was performed.
