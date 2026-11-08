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

The proof is analytic and self-contained in `RESULT.md`. The normalized point-to-edge distance was independently evaluated by enumerating actual finite cubical edges (dimensions 3–5). The closed cubic CDF was checked against direct one-dimensional ordered-statistic quadrature. The first-clipping correction was checked numerically in dimensions 3–8 using an independent quadrature of the exact beta-integral representation. Direct simulations used 1,200,000 uniform samples over specified radii, with reported tolerance checks. The squared moment was corroborated against generated examples in three tested dimensions. Execute `python check.py` after installing the packages in `requirements.txt`; the successful test concludes with `CUBIC_EDGE_CLEARANCE_EXACT_DISTRIBUTION_OK 1200000`.

The finite tests cannot certify arbitrary dimension or the limiting exponents; those follow from the geometric integral and the dominated-convergence argument in `RESULT.md`. The stated small-radius cubic formula in dimension three is classical and excluded from the novelty claim. Historical priority is unconfirmed, especially relative to older intersecting-cylinder analyses. No independent audit or independent validation has been carried out.
