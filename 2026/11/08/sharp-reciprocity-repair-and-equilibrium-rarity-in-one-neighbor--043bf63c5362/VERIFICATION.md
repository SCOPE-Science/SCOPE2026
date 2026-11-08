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

# Reproducibility and limits

Run `python3 verify.py` (Python standard library). The verifier independently constructs all mappings with no fixed points on two to six labeled vertices, enumerates all specialized binary profiles, and checks against odd-cycle parity and rational coefficients from the tree-function Lagrange-inversion formula. It independently adds every possible reverse arc to each mapping with exactly one odd cycle component and checks full best-response feasibility against the cycle/direct-child criterion. A distinct two-odd-cycle test verifies the lower bound and the count of nine minimal repairs in two disjoint 3-cycles. The script produces PASS only after all assertions succeed.

The infinite mapping enumeration, structural lower bound, general repair construction, and singularity-transfer asymptotics are supplied as proofs in RESULT.md, not inferred from finite computer checks. Independent audit: not performed. Inaccessible or unindexed overlapping mathematical literature is a residual risk.
