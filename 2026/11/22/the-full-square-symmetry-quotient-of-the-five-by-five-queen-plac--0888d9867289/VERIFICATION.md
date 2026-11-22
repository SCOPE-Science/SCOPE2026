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

The included `verify_queen_d4.py` uses only the Python standard library. Executing it in a Python 3 environment reproduces the exhaustive face counts, all flag-orbit cells of the genuine geometric symmetry quotient, signed boundary compositions, maximal-free-face collapses, and reversible Tietze eliminations. `verification_output.txt` is an actual execution result, not an expected-value-only statement.

Checks performed on this claim:

- All legal queen subsets and all barycentric flags are exhaustively generated and checked invariant under all eight square symmetries.
- Every quotient orbit face relation is represented without inversions and with distinct boundary facets; all cellular boundary compositions are zero.
- Each of 823 removed cell pairs meets the strict elementary-collapse condition, including maximality of the unique coface.
- A quotient two-skeleton spanning tree gives 311 generators; a deterministic algorithm validates each of the 311 reversible Tietze elimination steps and ends with an empty presentation.
- Independent Burnside Euler calculation uses fixed flag posets for all eight symmetries and returns 5.
- Standard Hurewicz and Whitehead implications are applied to the verified connected simply connected two-dimensional CW complex.

The finite verifier does not certify an infinite class of boards, mathematical publication priority, nor independent expert validation. All listed conclusions pertain only to the ordinary five-by-five board and the full eight-element square-symmetry quotient.
