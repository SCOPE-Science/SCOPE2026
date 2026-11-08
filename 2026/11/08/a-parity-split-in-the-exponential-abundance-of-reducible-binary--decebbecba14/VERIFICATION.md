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

From the directory containing these files, run `python verify.py` using Python 3. No third-party packages are needed. The checker directly enumerates all rank-preserving nonunit outer maps, inner maps of equal weighted image length, and distinct length-uniform composites, deduplicating multiple factorizations. It additionally checks the Fibonacci construction and the even-length square construction.

Observed complete reducible counts at image lengths two through eight are respectively `10, 38, 144, 374, 1648, 2970, 13316`, and the program terminates with `VERIFY_OK`. See `verification_output.txt` for the actual recorded output. The checker terminates after finite lengths and does **not** validate the infinite limits by exhaustion. Those are established in `RESULT.md` using explicit uniform upper and lower bounds.

No independent mathematical audit has been performed.
