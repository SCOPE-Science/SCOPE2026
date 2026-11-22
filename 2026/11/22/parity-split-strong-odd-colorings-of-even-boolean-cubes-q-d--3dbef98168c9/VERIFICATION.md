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

# Finite verification and proof boundaries

Run `python3 verification/check_rank.py` and `python3 verification/check_direct.py` from the extracted artifact directory. Both are standard-library-only. Exact expected output is in `verification/expected.txt`.

`check_rank.py` constructs the labelled parity incidence matrices and computes their binary row ranks for even dimensions 2, 4, 6, 8. Its checks are exact integer bit operations, and it exhaustively scans all side-indicators for dimensions 2 and 4. `check_direct.py` independently scans the same two small cubes by vertex-color assignments and validates every properness and odd-neighborhood constraint for all parity-split assignments.

The finite computations do not constitute an infinite proof. The latter is provided by the group-algebra rank argument, exact affine-solvability witness and color-class equivalence in RESULT.md. No nonsplit coloring count is inferred, and there is no independent mathematical audit.
