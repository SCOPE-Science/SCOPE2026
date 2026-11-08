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

# Reproduction and verification

Execute `python3 check_cusp.py` in the same directory as this document using Python 3 and its standard library. The file checks the high-distance exact survival integral, the three-term expansion, and the direct upper-half-plane simulation of independent uniform-area points. Its deterministic random seed fixes the five batches of 220,000 point pairs each. It returns `TRUNCATED_HYPERBOLIC_CUSP_TAIL_AND_MC_OK 1100000` when all tests pass.

The checker computes the geodesic distance from the upper-half-plane formula after choosing the nearest horizontal deck translate; this is independent of the exponentially distributed height-difference derivation of the exact integral. The code also numerically compares the two expressions for each sampled pair and evaluates the stated asymptotic truncation. Floating-point quadrature and sample tests only detect errors; they cannot certify a theorem over all widths, radii or sample paths.

The analytic argument verifies the unrestricted quantifiers and is supplied in `RESULT.md`. The full small-radius CDF, ambient distances in a larger surface, and any external independent audit remain outside this verification.
