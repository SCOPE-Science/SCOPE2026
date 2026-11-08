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

The reproducible checker `verify_jacobi.py` was executed with SymPy. It verified the normalized quartic from raw even moments, all three critical sign factorizations, the projective stationary point and exact square deficit, and separately computed Beta raw moments through the Beta-binomial expansion through degree eight. Thirty-six exact fourth moments were reconstructed directly from the polynomial; 13 rational shape values with 1,001 rational energy values each were compared against their exact endpoint and stationary candidates.

The universal proof is the endpoint-derivative sign analysis in RESULT.md. The finite rational comparisons are diagnostics, not exhaustive validation for all positive real shapes. Mathematical originality assessment is qualified by inaccessible or unindexed literature. Independent audit has not been performed.
