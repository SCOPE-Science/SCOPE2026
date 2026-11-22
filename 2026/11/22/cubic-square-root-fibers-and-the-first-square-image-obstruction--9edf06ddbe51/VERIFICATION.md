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

# Reproducibility and scope
Run `python3 nottingham_square_check.py` from the directory containing the checker. It uses the Python standard library only, composes every truncated substitution directly, and exhaustively checks field orders \(q=2,4,8,16\). The stored `nottingham_square_check_output.txt` contains the actual output and concludes `NOTTINGHAM_SQUARE_FIBERS_OK`.

The proof of the general theorem is in `RESULT.md`. Finite tests establish only the checked cases; the symbolic proof provides the universal assertions. No independent mathematical audit has been performed.
