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

# Reproducibility

Run `python3 verify.py` with a standard Python installation. It requires no third-party packages, network access, or external files and prints `VERIFY_OK 5868` on successful completion.

The verifier checks the exact potential variance against a separate closed-sum evaluation for small and medium graphs, constructs reduced Laplacian inverses over rational numbers and sums pairwise resistances for all permissible new links for graphs through nine vertices, exhaustively searches all eligible pairs through 140 vertices, and tests the balanced-candidate transition sign. The proof for arbitrarily many vertices is the algebraic argument in `RESULT.md`; finite checking is not claimed to prove the infinite theorem.

The exact scientific domain is one new unit-conductance edge on a path with all original conductances one, for every integer path order at least three. No further computational input or precomputed certificate is required.
