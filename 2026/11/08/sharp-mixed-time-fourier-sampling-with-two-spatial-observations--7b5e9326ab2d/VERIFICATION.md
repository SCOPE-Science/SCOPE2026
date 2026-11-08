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
# Verification of the stated theorem

The analytical certificate is the self-contained five-step proof in `RESULT.md`. The nonstandard part is the exact conversion from a mixed measurement frame to two principal angles and the complete modular count of optimizers. The two-projection calculation can be verified directly by its displayed two-by-two determinant, without relying on numerical evidence.

The accompanying `CHECK.py` uses NumPy to reconstruct the full complex mixed measurement matrix, rather than constructing the prediction from principal-angle blocks. For each \(n\) from 4 through 19, it independently enumerates every ordered choice of unordered two-site/time and two-site/missing-frequency sets for the arithmetic counts. It tests complete matrix eigenvalues on every case through dimension eight and on seeded random cases at larger dimensions. It checks both extremal spectral endpoints and the identity that they sum to two, and reports 129,994 passed assertions/checks. This is a bounded finite test, not an infinite certificate or a claim of independent validation.

Run with `python -m pip install -r requirements.txt` followed by `python CHECK.py`. The proof is valid for all \(n\ge4\); the finite checker covers only the stated dimensions and sampled cases. Potential equivalent literature under the terminology of complementary projections remains a priority risk. Independent audit has not been performed.
