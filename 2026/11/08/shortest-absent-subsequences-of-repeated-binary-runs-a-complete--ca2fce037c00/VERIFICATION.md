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

# Reproduction and scope of verification

Execute `python3 verify.py` from the directory containing the extracted script; it uses only the Python 3 standard library. The expected terminal line is `RUN_BLOCK_SAS_VERIFY_OK 175 354076 49`.

The checker compares a direct scattered-subsequence scanner with a maximal-run host-index calculation and the independent explicit characterization, verifies complete presence at all shorter lengths, and independently counts absent words using a finite-state dynamic program. It exhaustively checks 175 small parameter triples (354,076 candidate words at the claimed shortest absent lengths) and 49 additional larger parameter triples. All checks passed on the packaged version.

Finite verification cannot establish the infinitely quantified theorem. The proof in `RESULT.md` independently derives the greedy index, equality cases, full candidate languages, and rational generating functions. Neither a Lean certificate nor an independent mathematical audit is claimed.
