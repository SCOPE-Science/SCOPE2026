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

# Reproducibility and verification

Execute `python verify.py` (Python standard library; no third-party packages). The expected output is `VERIFY_OK 964 exact-rational polygon hull/profile cases`.

The verifier constructs six convex-polygon vertices from the edge normal form, computes the convex hull of all 36 pairwise vertex differences using independent exact cross products, calculates ordinary shoelace areas, and separately constructs the midpoint Wigner triangle. It verifies \(A(P-P)-4A(P)=t^2\), the oriented-area magnitude \(t^2/8\), both fixed-asymmetry endpoint inequalities, the exact variance identity, and balanced/boundary witnesses. A successful finite test is not an infinite proof; all real parameters are covered by the analytic optimization in RESULT.md.

The first publicly available motivating preprint was dated 27 August 2026 (arXiv:2609.27931v1), not its October revision. Historical novelty was assessed against accessible published mathematical records and primary literature, but is not a formal priority certification. Independent validation was not performed.
